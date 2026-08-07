from pathlib import Path

ROOT = Path('.')
html_files = sorted([p for p in ROOT.glob('*.html')])

social_html = '''    <div class="social-links" aria-hidden="false">
      <a class="social-link" href="https://www.facebook.com/timmacdonoughpainting/" target="_blank" rel="noopener" aria-label="Facebook">
        <!-- Facebook SVG -->
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.99 3.66 9.12 8.44 9.88v-6.99H7.9v-2.9h2.54V9.41c0-2.5 1.49-3.89 3.77-3.89 1.09 0 2.23.2 2.23.2v2.45h-1.25c-1.23 0-1.61.77-1.61 1.56v1.88h2.74l-.44 2.9h-2.3v6.99C18.34 21.12 22 16.99 22 12z"/></svg>
      </a>
      <a class="social-link" href="https://www.instagram.com/timmacdonoughpainting/" target="_blank" rel="noopener" aria-label="Instagram">
        <!-- Instagram SVG -->
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"/><path d="M17.5 6.5h.01"/></svg>
      </a>
      <a class="social-link" href="https://www.tiktok.com/@timmacdonoughpaintingcompany" target="_blank" rel="noopener" aria-label="TikTok">
        <!-- TikTok SVG -->
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2v12.2A4 4 0 1016 18V6h4V2h-8z"/></svg>
      </a>
      <a class="social-link" href="https://www.linkedin.com/company/tim-macdonough-painting-company/" target="_blank" rel="noopener" aria-label="LinkedIn">
        <!-- LinkedIn SVG -->
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5C4.98 4.88 3.88 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1 4.98 2.12 4.98 3.5zM0 8h5v15H0V8zm7 0h4.8v2.2h.1c.7-1.3 2.4-2.7 4.9-2.7 5.2 0 6.2 3.4 6.2 7.9V23h-5V15.6c0-1.8 0-4.1-2.5-4.1-2.5 0-2.9 1.9-2.9 3.9V23H7V8z"/></svg>
      </a>
    </div>'''

for f in html_files:
    txt = f.read_text(encoding='utf-8')
    if 'class="social-links"' in txt:
        print('Already present in', f.name)
        continue
    # find footer-bottom div
    idx = txt.find('<div class="footer-bottom">')
    if idx == -1:
        # try footer-brand area fallback
        idx2 = txt.find('<div class="container footer-grid">')
        if idx2 == -1:
            print('No footer container found in', f.name)
            continue
        # insert social links before footer-bottom area by finding footer-copy
        insert_point = txt.find('<p class="footer-copy">', idx2)
        if insert_point == -1:
            print('No footer-copy found in', f.name)
            continue
        # place social links before footer-copy
        new_txt = txt[:insert_point] + social_html + '\n' + txt[insert_point:]
        f.write_text(new_txt, encoding='utf-8')
        print('Inserted socials into', f.name)
        continue
    # find closing of footer-bottom div
    end = txt.find('</div>', idx)
    if end == -1:
        print('Cannot find end of footer-bottom in', f.name)
        continue
    # insert socials before footer-copy or before footer-bottom close
    copy_idx = txt.find('<p class="footer-copy">', idx, end+200)
    if copy_idx != -1:
        new_txt = txt[:copy_idx] + social_html + '\n' + txt[copy_idx:]
    else:
        new_txt = txt[:end] + social_html + '\n' + txt[end:]
    f.write_text(new_txt, encoding='utf-8')
    print('Inserted socials into', f.name)

print('Done')
