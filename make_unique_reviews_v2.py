from pathlib import Path
import re
import hashlib
import random

ROOT = Path('.')
files = sorted([p for p in ROOT.glob('*.html')])
section_pat = re.compile(r'(<section[^>]+id=["\']reviews["\'][\s\S]*?</section>)', re.I)
reviews_grid_pat = re.compile(r'<div[^>]+class=["\']reviews-grid["\'][\s\S]*?</div>', re.I)
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

# ratings map
ratings_map = [5,5,5,4.5,5,4.5,5,5]

all_texts = set()
used_reviewers = set()

for f in files:
    txt = f.read_text(encoding='utf-8')
    m = section_pat.search(txt)
    if not m:
        continue
    section = m.group(1)
    loc_name = f.stem.replace('-', ' ').replace(' mi', ' MI').title()
    seed = int(hashlib.sha1(f.name.encode('utf-8')).hexdigest()[:8], 16)
    rand = random.Random(seed)
    # build two unique reviewers
    reviewer_list = []
    attempts = 0
    while len(reviewer_list) < 2 and attempts < 200:
        name = rand.choice(first_names) + ' ' + rand.choice(last_names)
        if name not in used_reviewers:
            reviewer_list.append(name)
            used_reviewers.add(name)
        attempts += 1
    # build two unique review texts
    texts = []
    attempts = 0
    while len(texts) < 2 and attempts < 500:
        lead = rand.choice(lead_phrases)
        project = rand.choice(projects)
        adj = rand.choice(adjectives)
        verb_tail = rand.choice([f'in {loc_name}', f'on our {project}', f'at our {loc_name} home'])
        text = f"{lead} {project} — {adj} results {verb_tail}."
        # add a short differentiator using first initial + file hash if collision persists
        if text in all_texts:
            text = text + f' ({loc_name[:3].upper()}{rand.randint(1,99)})'
        if text not in all_texts:
            texts.append(text)
            all_texts.add(text)
        attempts += 1
    # ratings
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
    new_grid = '<div class="reviews-grid">\n' + new_articles + '    </div>'
    if reviews_grid_pat.search(section):
        new_section = reviews_grid_pat.sub(new_grid, section)
    else:
        new_section = section.replace('</section>', '\n    <div class="reviews-grid">\n' + new_articles + '    </div>\n  </section>')
    new_txt = txt[:m.start(1)] + new_section + txt[m.end(1):]
    f.write_text(new_txt, encoding='utf-8')
    print('Updated', f.name)

print('Done')
