from pathlib import Path
import re
ROOT = Path('.')
IGNORE = {'index.html','contact.html','service-areas.html','interior.html','exterior.html','residential.html','commercial.html','quick-estimate.html'}
files = [p for p in ROOT.glob('*.html') if p.name not in IGNORE]
pattern = re.compile(r'(<div[^>]+class="reviews-grid"[^>]*>)(.*?)(</div>)', re.S)
article_pat = re.compile(r'<article[^>]+class="review-card"[^>]*>.*?</article>', re.S)
for f in files:
    txt = f.read_text(encoding='utf-8')
    m = pattern.search(txt)
    if not m:
        continue
    inner = m.group(2)
    articles = article_pat.findall(inner)
    if len(articles) >= 3:
        # remove the last article (third)
        # Replace only one occurrence of that article inside the inner
        third = articles[2]
        new_inner = inner.replace(third, '', 1)
        new_block = m.group(1) + new_inner + m.group(3)
        txt = txt[:m.start()] + new_block + txt[m.end():]
        f.write_text(txt, encoding='utf-8')
        print('Removed third review from', f)
print('Done')
