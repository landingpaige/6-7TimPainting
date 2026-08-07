from pathlib import Path
import re
ROOT = Path('.')
IGNORE = {'index.html','contact.html','service-areas.html','interior.html','exterior.html','residential.html','commercial.html','quick-estimate.html'}
files = [p for p in ROOT.glob('*.html') if p.name not in IGNORE]
article_pat = re.compile(r'<article[^>]+class=["\']review-card["\'][^>]*>.*?</article>', re.S)
for f in files:
    txt = f.read_text(encoding='utf-8')
    sec_start = txt.find('<section id="reviews"')
    if sec_start == -1:
        continue
    sec_end = txt.find('</section>', sec_start)
    if sec_end == -1:
        continue
    sec_end += len('</section>')
    section = txt[sec_start:sec_end]
    articles = article_pat.findall(section)
    if len(articles) >= 3:
        third = articles[2]
        new_section = section.replace(third, '', 1)
        new_txt = txt[:sec_start] + new_section + txt[sec_end:]
        f.write_text(new_txt, encoding='utf-8')
        print('Removed third review from', f.name)
print('Done')
