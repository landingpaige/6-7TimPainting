"""Implements the internal-linking report recommendations. Run from repo root."""
import re, glob, sys, collections

SKIP = {"index", "residential", "commercial", "interior", "exterior", "service-areas",
        "contact", "quick-estimate", "privacy-policy"}

NAMES = {
    "berkley-mi": "Berkley", "beverly-hills-mi": "Beverly Hills", "bingham-farms-mi": "Bingham Farms",
    "birmingham-mi": "Birmingham", "bloomfield-hills-mi": "Bloomfield Hills", "clawson-mi": "Clawson",
    "clinton-township-mi": "Clinton Township", "franklin-mi": "Franklin",
    "grosse-pointe-farms-mi": "Grosse Pointe Farms", "grosse-pointe-mi": "Grosse Pointe",
    "grosse-pointe-shores-mi": "Grosse Pointe Shores", "grosse-pointe-woods-mi": "Grosse Pointe Woods",
    "huntington-woods-mi": "Huntington Woods", "lake-orion": "Lake Orion",
    "lathrup-village-mi": "Lathrup Village", "macomb-township-mi": "Macomb Township",
    "metamora-mi": "Metamora", "new-baltimore-mi": "New Baltimore", "oakland-township": "Oakland Township",
    "orchard-lake-mi": "Orchard Lake", "oxford-mi": "Oxford", "pleasant-ridge-mi": "Pleasant Ridge",
    "rochester-hills": "Rochester Hills", "rochester-mi": "Rochester", "romeo-mi": "Romeo",
    "royal-oak-mi": "Royal Oak", "shelby-township": "Shelby Township",
    "sterling-heights-mi": "Sterling Heights", "sylvan-lake-mi": "Sylvan Lake", "troy-mi": "Troy",
    "utica-mi": "Utica", "washington-township-mi": "Washington Township",
    "west-bloomfield-mi": "West Bloomfield",
}
BY_NAME = {v: k for k, v in NAMES.items()}

# Geographic neighbor map (made reciprocal below). Priority markets listed first where relevant.
NEIGHBORS = {
    "oakland-township": ["rochester-hills", "lake-orion", "oxford-mi", "rochester-mi", "shelby-township"],
    "rochester-hills": ["oakland-township", "rochester-mi", "troy-mi", "shelby-township", "lake-orion"],
    "rochester-mi": ["rochester-hills", "oakland-township", "shelby-township"],
    "lake-orion": ["oakland-township", "oxford-mi", "metamora-mi", "rochester-hills"],
    "oxford-mi": ["lake-orion", "metamora-mi", "oakland-township", "romeo-mi"],
    "metamora-mi": ["oxford-mi", "lake-orion", "oakland-township", "romeo-mi"],
    "romeo-mi": ["washington-township-mi", "oxford-mi", "metamora-mi"],
    "washington-township-mi": ["romeo-mi", "shelby-township", "macomb-township-mi", "oakland-township"],
    "shelby-township": ["rochester-hills", "utica-mi", "macomb-township-mi", "sterling-heights-mi", "washington-township-mi"],
    "utica-mi": ["shelby-township", "sterling-heights-mi", "clinton-township-mi"],
    "sterling-heights-mi": ["utica-mi", "clinton-township-mi", "shelby-township", "troy-mi"],
    "macomb-township-mi": ["shelby-township", "clinton-township-mi", "washington-township-mi", "new-baltimore-mi"],
    "clinton-township-mi": ["macomb-township-mi", "sterling-heights-mi", "utica-mi", "new-baltimore-mi"],
    "new-baltimore-mi": ["macomb-township-mi", "clinton-township-mi"],
    "birmingham-mi": ["bloomfield-hills-mi", "troy-mi", "beverly-hills-mi", "franklin-mi", "royal-oak-mi"],
    "bloomfield-hills-mi": ["birmingham-mi", "troy-mi", "west-bloomfield-mi", "bingham-farms-mi", "orchard-lake-mi"],
    "troy-mi": ["rochester-hills", "birmingham-mi", "bloomfield-hills-mi", "clawson-mi", "royal-oak-mi"],
    "beverly-hills-mi": ["birmingham-mi", "bingham-farms-mi", "franklin-mi", "lathrup-village-mi"],
    "bingham-farms-mi": ["bloomfield-hills-mi", "beverly-hills-mi", "franklin-mi", "lathrup-village-mi"],
    "franklin-mi": ["birmingham-mi", "bingham-farms-mi", "beverly-hills-mi"],
    "lathrup-village-mi": ["beverly-hills-mi", "bingham-farms-mi", "berkley-mi"],
    "west-bloomfield-mi": ["bloomfield-hills-mi", "orchard-lake-mi", "sylvan-lake-mi"],
    "orchard-lake-mi": ["west-bloomfield-mi", "sylvan-lake-mi", "bloomfield-hills-mi"],
    "sylvan-lake-mi": ["orchard-lake-mi", "west-bloomfield-mi", "bloomfield-hills-mi"],
    "royal-oak-mi": ["birmingham-mi", "troy-mi", "berkley-mi", "clawson-mi", "huntington-woods-mi", "pleasant-ridge-mi"],
    "berkley-mi": ["royal-oak-mi", "huntington-woods-mi", "clawson-mi", "pleasant-ridge-mi"],
    "clawson-mi": ["troy-mi", "royal-oak-mi", "berkley-mi"],
    "huntington-woods-mi": ["royal-oak-mi", "berkley-mi", "pleasant-ridge-mi"],
    "pleasant-ridge-mi": ["royal-oak-mi", "huntington-woods-mi", "berkley-mi"],
    "grosse-pointe-mi": ["grosse-pointe-farms-mi", "grosse-pointe-woods-mi", "grosse-pointe-shores-mi"],
    "grosse-pointe-farms-mi": ["grosse-pointe-mi", "grosse-pointe-woods-mi", "grosse-pointe-shores-mi"],
    "grosse-pointe-woods-mi": ["grosse-pointe-mi", "grosse-pointe-farms-mi", "grosse-pointe-shores-mi"],
    "grosse-pointe-shores-mi": ["grosse-pointe-mi", "grosse-pointe-farms-mi", "grosse-pointe-woods-mi"],
}
for a, lst in list(NEIGHBORS.items()):
    for b in lst:
        if a not in NEIGHBORS[b]:
            NEIGHBORS[b].append(a)

CLUSTERS = [
    ("North Oakland", "Our home base", ["oakland-township", "rochester-hills", "rochester-mi", "lake-orion", "oxford-mi", "metamora-mi"]),
    ("Birmingham &amp; Bloomfield", "Oakland County", ["birmingham-mi", "bloomfield-hills-mi", "troy-mi", "west-bloomfield-mi", "orchard-lake-mi", "sylvan-lake-mi", "beverly-hills-mi", "bingham-farms-mi", "franklin-mi", "lathrup-village-mi"]),
    ("Macomb County", "East side", ["shelby-township", "utica-mi", "macomb-township-mi", "sterling-heights-mi", "washington-township-mi", "romeo-mi", "clinton-township-mi", "new-baltimore-mi"]),
    ("Royal Oak &amp; Woodward", "South Oakland", ["royal-oak-mi", "berkley-mi", "clawson-mi", "huntington-woods-mi", "pleasant-ridge-mi"]),
    ("Grosse Pointe", "Wayne County", ["grosse-pointe-mi", "grosse-pointe-farms-mi", "grosse-pointe-woods-mi", "grosse-pointe-shores-mi"]),
]
assert sorted(s for _, _, l in CLUSTERS for s in l) == sorted(NAMES)

log = collections.defaultdict(list)


def name_pattern(name):
    tail = ""
    if name == "Rochester":
        tail = r"(?! Hills)"
    if name == "Grosse Pointe":
        tail = r"(?! (?:Farms|Shores|Woods))"
    return re.compile(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])(?! (?:Road|Rd|Avenue|Ave|Street|St)\b)" + tail)


def link_mentions(slug, html):
    """Link the first prose mention of each other covered city inside <p> tags in the body."""
    head, rest = html.split("</header>", 1)
    body, foot = rest.split("<footer", 1)
    already = set(re.findall(r'href="/([a-z-]+)"', body))
    done = set()

    def fix_para(m):
        para = m.group(0)
        # split into link / non-link segments so we never nest anchors
        parts = re.split(r"(<a\b.*?</a>|<[^>]+>)", para, flags=re.S)
        for i, seg in enumerate(parts):
            if not seg or seg.startswith("<"):
                continue
            # longest names first so "Grosse Pointe Farms" wins over "Grosse Pointe"
            for target, name in sorted(NAMES.items(), key=lambda kv: -len(kv[1])):
                if target == slug or target in done or target in already:
                    continue
                pat = name_pattern(name)
                mm = pat.search(seg)
                if mm:
                    seg = seg[:mm.start()] + f'<a href="/{target}">{name}</a>' + seg[mm.end():]
                    done.add(target)
                    log[slug].append(f"linked mention → /{target}")
                    # re-split handled by restarting on this segment: keep simple, one link per segment pass
                    parts[i] = seg
                    # further names in the remainder of this segment
                    pre, post = seg.split("</a>", 1) if "</a>" in seg else (seg, "")
                    break
            parts[i] = seg
        return "".join(parts)

    # run a few passes so one paragraph can receive multiple links
    for _ in range(4):
        body = re.sub(r"<p\b[^>]*>.*?</p>", fix_para, body, flags=re.S)
    return head + "</header>" + body + "<footer" + foot


def nearby_block(slug):
    city = NAMES[slug]
    links = "\n".join(
        f'          <a href="/{n}">{NAMES[n]}, MI</a>' for n in NEIGHBORS[slug]
    )
    return f'''    <section class="section bg-cream" id="nearby-areas">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-label">Nearby Communities</span>
          <h2>Also Painting Homes<br><em>Near {city}.</em></h2>
        </div>
        <p class="reveal" style="text-align:center;max-width:700px;margin:0 auto 2rem;">
          The same owner-led crew and the same prep standard travel with us to the communities around {city}. Explore our local painting pages below, or see <a href="/service-areas">every community we serve across Metro Detroit</a>.
        </p>
        <div class="nearby-links reveal" aria-label="Painting services in communities near {city}">
{links}
        </div>
      </div>
    </section>

'''


def process_location(fn):
    slug = fn[:-5]
    html = open(fn, encoding="utf-8").read()
    if 'id="nearby-areas"' in html:
        print("already processed", fn); return
    html = link_mentions(slug, html)
    assert html.count('<div class="cta-band">') == 1, fn
    html = html.replace('    <div class="cta-band">', nearby_block(slug) + '    <div class="cta-band">', 1)
    log[slug].append(f"nearby block → {NEIGHBORS[slug]} + /service-areas")
    open(fn, "w", encoding="utf-8").write(html)


def sub1(html, old, new, fn, count=1):
    n = html.count(old)
    assert n >= 1, f"{fn}: not found: {old[:80]}"
    log[fn].append(f"{old[:60]!r} → {new[:60]!r} (x{n if count is None else min(n, count)})")
    return html.replace(old, new) if count is None else html.replace(old, new, count)


def sitewide(fn):
    html = open(fn, encoding="utf-8").read()
    # footer: service sub-items to the exact section
    html = html.replace('<li><a href="/interior">Trim &amp; Crown Molding</a></li>', '<li><a href="/interior#trim">Trim &amp; Crown Molding</a></li>')
    html = html.replace('<li><a href="/interior">Drywall Repair</a></li>', '<li><a href="/interior#drywall">Drywall Repair</a></li>')
    html = html.replace('<li><a href="/exterior">Power Washing</a></li>', '<li><a href="/exterior#powerwash">Power Washing</a></li>')
    # footer: add Contact link next to Privacy Policy on every page
    old = '<a href="/privacy-policy">Privacy Policy</a></p>'
    if '<a href="/contact">Contact</a>' not in html and old in html:
        html = html.replace(old, '<a href="/privacy-policy">Privacy Policy</a>&nbsp;·&nbsp;<a href="/contact">Contact</a></p>', 1)
    open(fn, "w", encoding="utf-8").write(html)


def homepage():
    fn = "index.html"
    html = open(fn, encoding="utf-8").read()
    html = sub1(html, '<a href="/interior" class="btn-text">Learn more</a>', '<a href="/interior#trim" class="btn-text">Explore trim &amp; crown molding painting</a>', fn)
    html = sub1(html, '<a href="/interior" class="btn-text">Learn more</a>', '<a href="/interior#drywall" class="btn-text">See our drywall repair &amp; prep</a>', fn)
    html = sub1(html, '<a href="/exterior" class="btn-text">Learn more</a>', '<a href="/exterior#powerwash" class="btn-text">See exterior power washing &amp; prep</a>', fn)
    html = sub1(html, 'Visit our <a href="/contact">contact page</a>.', 'You can also <a href="/contact">contact Tim MacDonough Painting directly</a>.', fn)
    # service-area section: link every city that has its own page
    sec_start = html.index('<section class="section bg-cream" id="service-area">')
    sec_end = html.index("</section>", sec_start)
    sec = html[sec_start:sec_end]
    def li(m):
        name = m.group(1)
        if name in BY_NAME:
            log[fn].append(f"service-area list → /{BY_NAME[name]}")
            return f'<li><a href="/{BY_NAME[name]}">{name}</a></li>'
        return m.group(0)
    sec = re.sub(r"<li>([^<]+)</li>", li, sec)
    sec = sec.replace('<p>Not on the list? Call anyway — chances are we cover you.</p>',
                      '<p>Not on the list? <a href="/service-areas">See all the communities we serve</a> — or call anyway. Chances are we cover you.</p>')
    html = html[:sec_start] + sec + html[sec_end:]
    open(fn, "w", encoding="utf-8").write(html)


def quick_estimate():
    fn = "quick-estimate.html"
    html = open(fn, encoding="utf-8").read()
    html = sub1(html, 'Visit our <a href="/contact">contact page</a>.', 'You can also <a href="/contact">contact Tim MacDonough Painting directly</a>.', fn)
    open(fn, "w", encoding="utf-8").write(html)


def contact():
    fn = "contact.html"
    html = open(fn, encoding="utf-8").read()
    html = sub1(html, '<li><a href="/service-areas">Bloomfield Hills</a></li>', '<li><a href="/bloomfield-hills-mi">Bloomfield Hills</a></li>', fn)
    html = sub1(html, '<li><a href="/service-areas">Birmingham</a></li>', '<li><a href="/birmingham-mi">Birmingham</a></li>', fn)
    html = sub1(html, '<li><a href="/service-areas">Oxford &amp; Troy</a></li>', '<li><a href="/oxford-mi">Oxford</a></li><li><a href="/troy-mi">Troy</a></li>', fn)
    open(fn, "w", encoding="utf-8").write(html)


def interior_ids():
    fn = "interior.html"
    html = open(fn, encoding="utf-8").read()
    html = sub1(html, "<h3>Trim &amp; Baseboards</h3>", '<h3 id="trim">Trim &amp; Baseboards</h3>', fn)
    html = sub1(html, "<h3>Drywall Repair &amp; Prep</h3>", '<h3 id="drywall">Drywall Repair &amp; Prep</h3>', fn)
    open(fn, "w", encoding="utf-8").write(html)


def service_areas():
    fn = "service-areas.html"
    html = open(fn, encoding="utf-8").read()
    start = html.index('        <div class="city-directory-grid reveal">')
    end = html.index("</div>", start) + len("</div>")
    groups = []
    for title, label, slugs in CLUSTERS:
        links = "\n".join(f'            <a href="/{s}">{NAMES[s]}</a>' for s in slugs)
        groups.append(f'''        <div class="city-directory-group reveal">
          <h3><span class="area-county">{label}</span>{title}</h3>
          <div class="city-directory-grid">
{links}
          </div>
        </div>''')
    html = html[:start] + "\n".join(groups) + html[end:]
    log[fn].append("city directory regrouped into 5 clusters")
    # link the county cards' city lists where a page exists
    def li(m):
        name = m.group(1)
        if name in BY_NAME:
            log[fn].append(f"area card → /{BY_NAME[name]}")
            return f'<li><a href="/{BY_NAME[name]}">{name}</a></li>'
        return m.group(0)
    a = html.index('<div class="areas-grid">')
    b = html.index("</section>", a)
    html = html[:a] + re.sub(r"<li>([^<]+)</li>", li, html[a:b]) + html[b:]
    open(fn, "w", encoding="utf-8").write(html)


CSS = '''
/* ─── Internal linking: nearby communities + grouped city directory ─── */
.nearby-links {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  max-width: 900px;
  margin: 0 auto;
}
.nearby-links a {
  display: inline-flex;
  align-items: center;
  padding: 10px 16px;
  border-radius: var(--r-sm);
  border: 1px solid rgba(14, 29, 58, 0.12);
  background: var(--white);
  color: var(--navy);
  font-weight: 600;
  font-size: 0.9rem;
  text-decoration: none;
  transition: background var(--t), border-color var(--t);
}
.nearby-links a:hover {
  border-color: rgba(242, 179, 34, 0.55);
  background: rgba(242, 179, 34, 0.08);
}
.city-directory-group { max-width: 1200px; margin: 28px auto 0; }
.city-directory-group h3 {
  font-family: var(--font-display);
  color: var(--navy);
  font-size: 1.5rem;
  margin: 0;
}
.city-directory-group h3 .area-county { display: block; margin-bottom: 2px; }
.city-directory-group .city-directory-grid { margin: 14px auto 8px; }
@media (max-width: 900px) {
  .city-directory-group .city-directory-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
.city-directory-group + .areas-grid { margin-top: 48px; }
.area-card li a, .areas-note p a { color: var(--navy); font-weight: 600; text-decoration: underline; text-decoration-color: rgba(242, 179, 34, 0.6); text-underline-offset: 3px; transition: color var(--t); }
.area-card li a:hover, .areas-note p a:hover { color: var(--gold); }
#nearby-areas p a { color: var(--navy); text-decoration: underline; text-underline-offset: 3px; text-decoration-color: rgba(242, 179, 34, 0.7); }
'''


if __name__ == "__main__":
    for fn in sorted(glob.glob("*.html")):
        if fn[:-5] not in SKIP:
            process_location(fn)
    homepage(); quick_estimate(); contact(); interior_ids(); service_areas()
    for fn in sorted(glob.glob("*.html")):
        sitewide(fn)
    css = open("style.css", encoding="utf-8").read()
    if ".nearby-links" not in css:
        open("style.css", "a", encoding="utf-8").write(CSS)
    for k in sorted(log):
        print(k, *log[k], sep="\n   ")
