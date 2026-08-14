"""
Restructures JSON-LD on the 33 location pages:
  - removes the full LocalBusiness/HousePainter re-declaration (was duplicated
    on every page with no @id, effectively 33 disconnected copies of the
    business entity)
  - consolidates the 1-4 per-city "X Painting in {City}" Service nodes into
    ONE Service entity for the page ("Painting Services in {City}, MI"),
    referencing the business by @id and using a proper City areaServed
  - adds a WebPage node (isPartOf #website, about the location Service,
    mentions the 4 main service pages by @id)
  - gives the FAQPage node a stable @id
  - leaves the existing BreadcrumbList script untouched

Run: python3 restructure_location_pages.py
"""
import re
import json
import glob

DOMAIN = "https://www.timmacdonoughpainting.com"
BUSINESS_ID = f"{DOMAIN}/#business"
WEBSITE_ID = f"{DOMAIN}/#website"
MAIN_SERVICE_IDS = [
    f"{DOMAIN}/interior#service",
    f"{DOMAIN}/exterior#service",
    f"{DOMAIN}/residential#service",
    f"{DOMAIN}/commercial#service",
]

LOCATIONS = sorted(
    set(glob.glob("*.html"))
    - {
        "index.html", "residential.html", "commercial.html", "interior.html", "exterior.html",
        "service-areas.html", "contact.html", "quick-estimate.html", "privacy-policy.html",
    }
)


def extract_city_full(graph):
    for node in graph:
        if node.get("@type") == "Service":
            area = node.get("areaServed", "")
            m = re.match(r"^(.*?) and nearby", area)
            if m:
                return m.group(1)
    return None


def process(fn):
    text = open(fn, encoding="utf-8").read()

    script_pattern = re.compile(
        r'(<script type="application/ld\+json">\s*)(\{.*?"@graph".*?\})(\s*</script>)', re.S
    )
    m = script_pattern.search(text)
    assert m, f"no @graph ld+json block found in {fn}"
    data = json.loads(m.group(2))
    graph = data["@graph"]

    city_full = extract_city_full(graph)
    assert city_full, f"could not determine city name in {fn}"

    canon_m = re.search(r'<link rel="canonical" href="([^"]+)"', text)
    assert canon_m, f"no canonical tag in {fn}"
    page_url = canon_m.group(1)

    title_m = re.search(r"<title>(.*?)</title>", text)
    page_name = title_m.group(1) if title_m else city_full

    service_id = f"{page_url}#service"
    webpage_id = f"{page_url}#webpage"
    faq_id = f"{page_url}#faq"

    new_graph = []
    faq_present = False
    for node in graph:
        t = node.get("@type")
        if t in (["LocalBusiness", "HousePainter"], "LocalBusiness"):
            continue  # drop full business re-declaration
        if t == "Service":
            continue  # dropping per-city service fragments; replaced below
        if t == "FAQPage":
            node["@id"] = faq_id
            faq_present = True
        new_graph.append(node)

    location_service = {
        "@type": "Service",
        "@id": service_id,
        "name": f"Painting Services in {city_full}",
        "url": page_url,
        "provider": {"@id": BUSINESS_ID},
        "areaServed": {"@type": "City", "name": city_full},
        "serviceType": ["Interior Painting", "Exterior Painting", "Residential Painting", "Commercial Painting"],
        "description": f"Interior, exterior, residential, and commercial painting services provided by Tim MacDonough Painting Company in {city_full}.",
    }
    new_graph.insert(0, location_service)

    webpage_node = {
        "@type": "WebPage",
        "@id": webpage_id,
        "url": page_url,
        "name": page_name,
        "isPartOf": {"@id": WEBSITE_ID},
        "about": {"@id": service_id},
        "mentions": [{"@id": sid} for sid in MAIN_SERVICE_IDS],
        "inLanguage": "en-US",
    }
    new_graph.insert(0, webpage_node)

    assert faq_present, f"no FAQPage node found in {fn}"

    data["@graph"] = new_graph
    new_json = json.dumps(data, indent=2, ensure_ascii=False)
    new_block = m.group(1) + "\n  " + new_json.replace("\n", "\n  ") + "\n  " + m.group(3).strip() + "\n"
    text = text[: m.start()] + new_block + text[m.end():]

    open(fn, "w", encoding="utf-8").write(text)
    return city_full


if __name__ == "__main__":
    ok, failed = 0, []
    for fn in LOCATIONS:
        try:
            city = process(fn)
            ok += 1
        except AssertionError as e:
            failed.append((fn, str(e)))
    print(f"Updated {ok} files")
    if failed:
        print("FAILED:")
        for fn, err in failed:
            print(" -", fn, err)
