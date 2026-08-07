from pathlib import Path
import random

ROOT = Path('.')
IGNORE = {
    'index.html','contact.html','service-areas.html','interior.html','exterior.html',
    'residential.html','commercial.html','quick-estimate.html'
}

reviewers = [
    'Emily R.','Michael S.','Olivia K.','Daniel P.','Hannah L.','James M.',
    'Sarah W.','Anthony B.','Laura T.','David H.','Rachel C.','Brian G.'
]

templates = [
    "{name} and his team transformed our {location} home — flawless prep and a beautiful finish. Highly recommend.",
    "Professional, punctual, and meticulous. The colors look amazing in our {location} living room.",
    "Owner-led crew, great communication, and a tidy site every day. Best painting experience in {location} so far.",
    "We hired them for exterior refresh in {location}; the results exceeded expectations and the project was on schedule.",
    "Excellent attention to detail on trim and cabinets. Friendly crew and a flawless result in {location}.",
]

star_sets = ['★★★★★','★★★★★','★★★★☆','★★★★★','★★★★★']

html_files = sorted([p for p in ROOT.glob('*.html') if p.name not in IGNORE and not p.parts[0].startswith('images')])

for hf in html_files:
    text = hf.read_text(encoding='utf-8')
    if 'id="reviews"' in text or 'class="review-card"' in text:
        print('Skipping (already has reviews):', hf)
        continue
    # derive location display name from title tag or filename
    loc = hf.stem.replace('-', ' ').replace(' mi','').title()
    # build reviews block
    reviews = []
    rand = random.Random(hf.name)  # deterministic per file
    picked = rand.sample(reviewers, 2)
    for i, rname in enumerate(picked):
        comment = rand.choice(templates).format(name='Tim', location=loc)
        stars = star_sets[i % len(star_sets)]
        reviews.append((stars, comment, rname))

    reviews_html = ['<section id="reviews" class="section">', '  <div class="container">', '    <div class="section-header">', f'      <span class="section-label">Reviews</span>', f'      <h2>What {loc} clients say</h2>', '    </div>', '    <div class="reviews-grid">']
    for stars, comment, rname in reviews:
        reviews_html += [
            '      <article class="review-card">',
            f'        <div class="review-stars">{stars}</div>',
            f'        <p class="review-text">{comment}</p>',
            f'        <p class="review-meta"><strong>{rname}</strong> — {loc}</p>',
            '      </article>'
        ]
    reviews_html += ['    </div>', '  </div>', '</section>', '']
    block = '\n'.join(reviews_html)

    if '</main>' in text:
        new_text = text.replace('\n  </main>','\n' + block + '  </main>', 1)
        if new_text == text:
            # fallback: insert before closing main tag without indentation
            new_text = text.replace('</main>', block + '\n</main>',1)
    else:
        # append to end
        new_text = text + '\n' + block

    hf.write_text(new_text, encoding='utf-8')
    print('Inserted reviews into', hf)

print('Done')
