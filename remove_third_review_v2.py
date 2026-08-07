from pathlib import Path
import re
ROOT = Path('.')
IGNORE = {'index.html','contact.html','service-areas.html','interior.html','exterior.html','residential.html','commercial.html','quick-estimate.html'}
files = [p for p in ROOT.glob('*.html') if p.name not in IGNORE]
article_pat = re.compile(r'<article[^>]+class="review-card"[^>]*>.*?</article>', re.S)
for f in files:
    txt = f.read_text(encoding='utf-8')
    start_idx = txt.find('<div class="reviews-grid">')
    if start_idx == -1:
        continue
    end_idx = txt.find('</div>', start_idx)
    if end_idx == -1:
        continue
    # end_idx points to the close of reviews-grid div
    block = txt[start_idx:end_idx+6]
    articles = article_pat.findall(block)
    if len(articles) >= 3:
        third = articles[2]
        new_block = block.replace(third, '', 1)
        new_txt = txt[:start_idx] + new_block + txt[end_idx+6:]
        f.write_text(new_txt, encoding='utf-8')
        print('Removed third review from', f.name)
print('Done')
