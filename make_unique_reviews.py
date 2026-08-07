from pathlib import Path
import re
import hashlib
import random

ROOT = Path('.')
html_files = sorted([p for p in ROOT.glob('*.html')])
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
    "Andrew","Lindsey","Chris","Madison","Ben","Kara","Derek","Sierra","Owen","Natalie"
]
phrases = [
    "Professional, punctual, and meticulous.",
    "Owner-led team with excellent communication and cleanups.",
    "Outstanding attention to detail on trim and cabinetry.",
    "Transformed our space—thoughtful prep and flawless finish.",
    "Polite crew, on-time, and the color matched perfectly.",
    "Left the site cleaner than they found it and were very respectful.",
    "High-quality materials and finished exactly as promised.",
    "Skilled painters who cared about protecting our floors and furniture.",
    "Transparent pricing and the estimate was accurate.",
    "Fast response, thoughtful schedule, and exceptional workmanship.",
    "We appreciate the owner involvement and craftmanship throughout.",
    "They repaired minor surface imperfections before painting—excellent prep.",
    "The crew was detail-oriented and finished on schedule.",
    "Great experience from estimate to final walkthrough.",
    "Reliable, professional, and the paint job looks factory-fresh.",
]

# helper to render stars string
def stars_for_rating(r):
    # r can be 5, 4.5, 4, etc.
    if r == 5:
        return '★★★★★'
    if r == 4.5:
        return '★★★★☆'
    if r == 4:
        return '★★★★'
    return '★★★★☆'

all_texts = set()

for f in html_files:
    txt = f.read_text(encoding='utf-8')
    m = section_pat.search(txt)
    if not m:
        continue
    section = m.group(1)
    # derive location display name from page title in section header if present
    # fallback to filename without extension
    loc_name = f.stem.replace('-', ' ').replace(' mi', ' MI').title()
    # seed RNG deterministically per file so changes are repeatable
    seed = int(hashlib.md5(f.name.encode('utf-8')).hexdigest()[:8], 16)
    rand = random.Random(seed)
    # choose 2 unique reviewers
    reviewers = rand.sample(first_names, 2)
    # choose 2 unique phrases but ensure not used site-wide
    texts = []
    attempts = 0
    while len(texts) < 2 and attempts < 50:
        candidate = rand.choice(phrases)
        # add a short location-specific suffix to increase uniqueness
        suffix = ''
        if rand.random() < 0.6:
            suffix = f' We had them paint our {rand.choice(["living room","kitchen","exterior","trim","entryway","bedroom"]) } in {loc_name}.'
        full = candidate + suffix
        if full not in all_texts:
            texts.append(full)
            all_texts.add(full)
        attempts += 1
    # ratings
    ratings = [5, rand.choice([5,4.5,4])]
    # build new reviews-grid HTML
    new_articles = ''
    for reviewer, text, rating in zip(reviewers, texts, ratings):
        stars = stars_for_rating(rating)
        new_articles += article_template.format(stars=stars, text=text, reviewer=reviewer + rand.choice(['','.', '']), location=loc_name)
    new_grid = '<div class="reviews-grid">\n' + new_articles + '    </div>'
    # replace old reviews-grid
    if reviews_grid_pat.search(section):
        new_section = reviews_grid_pat.sub(new_grid, section)
    else:
        # if no grid found, insert before section close
        new_section = section.replace('</section>', '\n    <div class="reviews-grid">\n' + new_articles + '    </div>\n  </section>')
    new_txt = txt[:m.start(1)] + new_section + txt[m.end(1):]
    f.write_text(new_txt, encoding='utf-8')
    print('Updated reviews in', f.name)

print('Done')
