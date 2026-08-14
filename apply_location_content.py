"""
Applies the per-city content in location_content.py to the corresponding
location-page HTML files:
  - rewrites the hero paragraph
  - rewrites the "Local Standards" feature paragraph
  - rewrites the 4 service-card summary sentences
  - inserts a new local-context section (heading + paragraph)
  - inserts a visible FAQ section, and rewrites the FAQPage schema to match

Run: python3 apply_location_content.py
"""
import re
import json
from location_content import LOCATIONS

FAQ_ITEM_TEMPLATE = """
          <div class="reveal{reveal_mod}" style="border-bottom:1px solid rgba(14,29,58,0.12);padding-bottom:1.75rem;margin-bottom:1.75rem;">
            <h3 style="font-family:var(--font-body);font-size:1rem;font-weight:700;color:var(--navy);margin-bottom:0.5rem;">{q}</h3>
            <p style="margin:0;">{a}</p>
          </div>"""

FAQ_ITEM_TEMPLATE_LAST = """
          <div class="reveal{reveal_mod}">
            <h3 style="font-family:var(--font-body);font-size:1rem;font-weight:700;color:var(--navy);margin-bottom:0.5rem;">{q}</h3>
            <p style="margin:0;">{a}</p>
          </div>"""


def build_faq_section(city_label, faqs):
    items = []
    for i, (q, a) in enumerate(faqs):
        reveal_mod = "" if i == 0 else f" reveal-d{i}"
        tmpl = FAQ_ITEM_TEMPLATE_LAST if i == len(faqs) - 1 else FAQ_ITEM_TEMPLATE
        items.append(tmpl.format(reveal_mod=reveal_mod, q=q, a=a))
    items_html = "".join(items)
    return f'''
    <section class="section" id="faq">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-label">FAQ</span>
          <h2>Common Questions About<br><em>Painting in {city_label}.</em></h2>
        </div>
        <div style="max-width:760px;margin:0 auto;">
{items_html}
        </div>
      </div>
    </section>
'''


def build_local_section(heading, body):
    return f'''
    <section class="section bg-cream">
      <div class="container">
        <div class="section-header reveal" style="max-width:820px;">
          <h2>{heading}</h2>
          <p>{body}</p>
        </div>
      </div>
    </section>
'''


def replace_hero(text, new_hero):
    pattern = re.compile(
        r'(<div class="page-hero-content">\s*<span class="section-label">.*?</span>\s*<h1>.*?</h1>\s*<p>)(.*?)(</p>)',
        re.S,
    )
    new_text, n = pattern.subn(lambda m: m.group(1) + new_hero + m.group(3), text, count=1)
    assert n == 1, "hero paragraph not found/replaced"
    return new_text


def replace_feature_para(text, new_para):
    pattern = re.compile(
        r'(<div class="feature-body[^"]*"[^>]*>.*?<h2>.*?</h2>\s*<p>)(.*?)(</p>)',
        re.S,
    )
    new_text, n = pattern.subn(lambda m: m.group(1) + new_para + m.group(3), text, count=1)
    assert n == 1, "feature paragraph not found/replaced"
    return new_text


def replace_service_card(text, heading, new_sentence):
    pattern = re.compile(
        r'(<h3>' + re.escape(heading) + r'</h3>\s*<p>)(.*?)(</p>)',
        re.S,
    )
    new_text, n = pattern.subn(lambda m: m.group(1) + new_sentence + m.group(3), text, count=1)
    assert n == 1, f"service card '{heading}' not found/replaced"
    return new_text


def insert_local_and_faq(text, local_html, faq_html):
    # Insert right before the cta-band div, which follows the services-grid section.
    marker = '<div class="cta-band">'
    idx = text.find(marker)
    assert idx != -1, "cta-band marker not found"
    return text[:idx] + local_html + faq_html + "\n    " + text[idx:]


def update_faq_schema(text, faqs):
    # Find the first ld+json script block (the @graph one containing FAQPage)
    script_pattern = re.compile(
        r'(<script type="application/ld\+json">\s*)(\{.*?\})(\s*</script>)', re.S
    )
    matches = list(script_pattern.finditer(text))
    target_match = None
    target_data = None
    for m in matches:
        try:
            data = json.loads(m.group(2))
        except json.JSONDecodeError:
            continue
        if "@graph" in data:
            target_match = m
            target_data = data
            break
    assert target_match is not None, "could not find @graph ld+json block"

    found_faq = False
    for node in target_data["@graph"]:
        if node.get("@type") == "FAQPage":
            node["mainEntity"] = [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in faqs
            ]
            found_faq = True
            break
    assert found_faq, "FAQPage node not found in @graph"

    new_json = json.dumps(target_data, indent=2, ensure_ascii=False)
    new_block = target_match.group(1) + "\n  " + new_json.replace("\n", "\n  ") + "\n  " + target_match.group(3).strip() + "\n"
    return text[: target_match.start()] + new_block + text[target_match.end():]


def city_label_from_h1(text):
    m = re.search(r'<h1>Painting Contractor in<br><em>(.*?)\.</em></h1>', text)
    if m:
        return m.group(1)
    m = re.search(r'<h1>(.*?)</h1>', text, re.S)
    return re.sub(r'<[^>]+>', ' ', m.group(1)).strip() if m else ""


def process(fn, data):
    text = open(fn, encoding="utf-8").read()
    orig = text

    text = replace_hero(text, data["hero"])
    text = replace_feature_para(text, data["feature_para"])
    text = replace_service_card(text, "Interior Painting", data["svc_interior"])
    text = replace_service_card(text, "Exterior Painting", data["svc_exterior"])
    text = replace_service_card(text, "Residential Painting", data["svc_residential"])
    text = replace_service_card(text, "Commercial Painting", data["svc_commercial"])

    city_label = city_label_from_h1(orig)
    local_html = build_local_section(data["local_heading"], data["local_body"])
    faq_html = build_faq_section(city_label, data["faqs"])
    text = insert_local_and_faq(text, local_html, faq_html)

    text = update_faq_schema(text, data["faqs"])

    open(fn, "w", encoding="utf-8").write(text)
    return True


if __name__ == "__main__":
    ok, failed = 0, []
    for slug, data in LOCATIONS.items():
        fn = f"{slug}.html"
        try:
            process(fn, data)
            ok += 1
        except AssertionError as e:
            failed.append((fn, str(e)))
    print(f"Updated {ok} files")
    if failed:
        print("FAILED:")
        for fn, err in failed:
            print(" -", fn, err)
