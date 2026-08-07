from pathlib import Path
import re
import hashlib
import random

ROOT = Path('.')
files = sorted([p for p in ROOT.glob('*.html')])
section_pat = re.compile(r'(<section[^>]+id=["\']reviews["\'][\s\S]*?</section>)', re.I)
section_header_pat = re.compile(r'(<div[^>]+class=["\']section-header["\'][\s\S]*?</div>)', re.I)
# global remove patterns
article_pat = re.compile(r'<article[^>]+class=["\']review-card["\'][\s\S]*?</article>', re.I)
standalone_pair_pat = re.compile(r'<p[^>]+class=["\']review-text["\'][\s\S]*?<\/p>\s*<p[^>]+class=["\']review-meta["\'][\s\S]*?<\/p>', re.I)

article_template = '''      <article class="review-card">
        <div class="review-stars">{stars}</div>
        <p class="review-text">{text}</p>
        <p class="review-meta"><strong>{reviewer}</strong> — {location}</p>
      </article>\n'''

first_names = [
    "Daniel","Sarah","Emily","Michael","Laura","James","Olivia","Liam","Sophia","Noah",
    "Grace","Ethan","Hannah","Alexander","Rachel","Jacob","Megan","Samuel","Katie","Ryan",
    "Amanda","Josh","Ava","Logan","Maya","Brandon","Nicole","Tyler","Julia","Zoe",
    "Andrew","Lindsey","Chris","Madison","Ben","Kara","Derek","Sierra","Owen","Natalie",
    "Eleanor","Marcus","Isabel","Victor","Paula","Eli","Tanya","Violet","Caleb","Renee"
]
last_names = ["K.","M.","B.","R.","S.","L.","H.","T.","N.","G."]
projects = ["living room","kitchen","exterior","trim and doors","entryway","bedroom","office","cabinet project","porch"]
adjectives = ["flawless","beautiful","precise","exceptional","careful","meticulous","spotless","stunning"]
lead_phrases = [
    "Tim and his team transformed our",
    "Owner-led crew delivered a",
    "Professional, punctual, and meticulous—",
    "Outstanding prep and finish on our",
    "We were impressed by the craftsmanship on our"
]
ratings_map = [5,5,5,4.5,5,4.5,5,5]

all_texts = set()
used_reviewers = set()

for f in files:
    txt = f.read_text(encoding='utf-8')
    # remove all existing article review-card blocks and standalone pairs globally
    txt = article_pat.sub('', txt)
    txt = standalone_pair_pat.sub('', txt)
    m = section_pat.search(txt)
    if not m:
        continue
    section = m.group(1)
    # extract existing section header if present
    sh = section_header_pat.search(section)
    section_header_html = sh.group(1) if sh else '    <div class="section-header">\n      <span class="section-label">Reviews</span>\n      <h2>What clients say</h2>\n    </div>'
    loc_name = f.stem.replace('-', ' ').replace(' mi', ' MI').title()
    seed = int(hashlib.sha1(f.name.encode('utf-8')).hexdigest()[:8], 16)
    rand = random.Random(seed)
    # two reviewers
    reviewer_list = []
    attempts = 0
    while len(reviewer_list) < 2 and attempts < 200:
        name = rand.choice(first_names) + ' ' + rand.choice(last_names)
        if name not in used_reviewers:
            reviewer_list.append(name)
            used_reviewers.add(name)
        attempts += 1
    texts = []
    attempts = 0
    while len(texts) < 2 and attempts < 500:
        lead = rand.choice(lead_phrases)
        project = rand.choice(projects)
        adj = rand.choice(adjectives)
        verb_tail = rand.choice([f'in {loc_name}', f'on our {project}', f'at our {loc_name} home'])
        text = f"{lead} {project} — {adj} results {verb_tail}."
        if text in all_texts:
            text = text + f' ({loc_name[:3].upper()}{rand.randint(1,99)})'
        if text not in all_texts:
            texts.append(text)
            all_texts.add(text)
        attempts += 1
    ratings = [ratings_map[rand.randint(0, len(ratings_map)-1)], ratings_map[rand.randint(0, len(ratings_map)-1)]]
    def stars_for_rating(r):
        if r == 5:
            return '★★★★★'
        if r == 4.5:
            return '★★★★☆'
        if r == 4:
            return '★★★★'
        return '★★★★☆'
    new_articles = ''
    for reviewer, text, rating in zip(reviewer_list, texts, ratings):
        stars = stars_for_rating(rating)
        new_articles += article_template.format(stars=stars, text=text, reviewer=reviewer, location=loc_name)
    new_section = f'<section id="reviews" class="section">\n  <div class="container">\n{section_header_html}\n    <div class="reviews-grid">\n' + new_articles + '    </div>\n  </div>\n</section>'
    new_txt = txt[:m.start(1)] + new_section + txt[m.end(1):]
    f.write_text(new_txt, encoding='utf-8')
    print('Cleaned and updated', f.name)

print('Done')
