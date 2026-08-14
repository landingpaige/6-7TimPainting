"""
Restructures JSON-LD on the 4 main service pages:
  - removes the full LocalBusiness/HousePainter re-declaration
  - adds a stable @id to the Service node, referencing the business by @id
  - adds a WebPage node (isPartOf #website, about the Service)
  - gives the FAQPage node a stable @id
Run: python3 restructure_service_pages.py
"""
import re
import json

DOMAIN = "https://www.timmacdonoughpainting.com"
BUSINESS_ID = f"{DOMAIN}/#business"
WEBSITE_ID = f"{DOMAIN}/#website"

PAGES = {
    "interior.html": {
        "slug": "interior",
        "page_name": "Interior Painting Contractor | Tim MacDonough Painting",
    },
    "exterior.html": {
        "slug": "exterior",
        "page_name": "Exterior Painting Contractor | Tim MacDonough Painting",
    },
    "residential.html": {
        "slug": "residential",
        "page_name": "Luxury Residential Painting | Tim MacDonough Painting",
    },
    "commercial.html": {
        "slug": "commercial",
        "page_name": "Commercial Painting Contractor | Tim MacDonough Painting",
    },
}


def process(fn, slug, page_name):
    text = open(fn, encoding="utf-8").read()

    script_pattern = re.compile(
        r'(<script type="application/ld\+json">\s*)(\{.*?"@graph".*?\})(\s*</script>)', re.S
    )
    m = script_pattern.search(text)
    assert m, f"no @graph ld+json block found in {fn}"
    data = json.loads(m.group(2))

    page_url = f"{DOMAIN}/{slug}"
    service_id = f"{page_url}#service"
    webpage_id = f"{page_url}#webpage"
    faq_id = f"{page_url}#faq"

    new_graph = []
    service_node = None
    faq_node = None
    for node in data["@graph"]:
        t = node.get("@type")
        if t == ["LocalBusiness", "HousePainter"] or t == "LocalBusiness":
            continue  # drop full business re-declaration
        if t == "Service":
            node["@id"] = service_id
            node["url"] = page_url
            node["provider"] = {"@id": BUSINESS_ID}
            service_node = node
        if t == "FAQPage":
            node["@id"] = faq_id
            faq_node = node
        new_graph.append(node)

    assert service_node is not None, f"no Service node found in {fn}"

    webpage_node = {
        "@type": "WebPage",
        "@id": webpage_id,
        "url": page_url,
        "name": page_name,
        "isPartOf": {"@id": WEBSITE_ID},
        "about": {"@id": service_id},
        "inLanguage": "en-US",
    }
    new_graph.insert(0, webpage_node)

    data["@graph"] = new_graph
    new_json = json.dumps(data, indent=2, ensure_ascii=False)
    new_block = m.group(1) + "\n  " + new_json.replace("\n", "\n  ") + "\n  " + m.group(3).strip() + "\n"
    text = text[: m.start()] + new_block + text[m.end():]

    open(fn, "w", encoding="utf-8").write(text)


if __name__ == "__main__":
    for fn, cfg in PAGES.items():
        process(fn, cfg["slug"], cfg["page_name"])
        print("Updated", fn)
