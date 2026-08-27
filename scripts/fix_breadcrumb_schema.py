#!/usr/bin/env python3
"""
Correct each page's BreadcrumbList JSON-LD so it matches the page's own
REAL visible breadcrumb (parsed from the hero <p> element), rather than
touching any visible markup. Fixes both label-text drift ("Cardiology" vs
"Cardiology Medical Billing Services") and item-count drift (schema
skipping the visible "Services" middle step).
"""
import re
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "pages"
SITE = "https://billedright.com"

SLUGS = [
    "account-management", "allergy-rcm-services", "ar-follow-up", "authorizations",
    "awards", "behavioral-health-rcm-services", "cardiology-rcm-services",
    "careers-india", "careers-us", "case-studies/allergy", "case-studies/cardiology",
    "case-studies/credentialing", "case-studies/primary-care", "charge-posting",
    "claim-submission", "contract-renegotiation", "denial-management",
    "documentation-management", "documentation-review", "eclinicalworks-billing-services",
    "emr-billing-platforms", "faq", "gastroenterology-rcm-services",
    "insurance-eligibility", "internal-medicine-rcm-services", "leadership",
    "locations", "medical-coding", "nephrology-rcm-services",
    "pain-management-rcm-services", "patient-ar-collections", "payment-posting",
    "primary-care-rcm-services", "privacy-policy", "private-equity",
    "psychiatry-rcm-services", "pulmonary-rcm-services", "recognition",
    "reporting", "rheumatology-rcm-services", "sms-consent", "terms-and-conditions",
    "testimonials", "urgent-care-rcm-services", "vascular-surgery-rcm-services",
    "why-billed-right",
]


def find_source(slug: str) -> Path:
    flat = PAGES_DIR / f"{slug}.html"
    if flat.exists():
        return flat
    return PAGES_DIR / slug / "index.html"


# Matches the whole breadcrumb <p>...</p> block in the hero, tolerant of the
# couple of style variants used across pages.
BREADCRUMB_P_RE = re.compile(
    r'<p[^>]*>\s*(<a href="/"[^>]*>Home</a>.*?)</p>', re.DOTALL
)
# Pulls out each <a href="URL" ...>Text</a> and the trailing current-page span/text.
LINK_RE = re.compile(r'<a href="([^"]+)"[^>]*>([^<]+)</a>')
CURRENT_RE = re.compile(r'<span[^>]*>([^<]+)</span>\s*$')


def parse_visible_breadcrumb(html: str):
    m = BREADCRUMB_P_RE.search(html)
    if not m:
        return None
    frag = m.group(1)
    items = [(href, text) for href, text in LINK_RE.findall(frag)]
    cur = CURRENT_RE.search(frag)
    if not cur:
        return None
    current_text = cur.group(1)
    items.append((None, current_text))
    return items


def build_breadcrumb_json(items):
    elements = []
    for idx, (href, text) in enumerate(items, start=1):
        url = SITE + "/" if href == "/" else (SITE + href if href else None)
        if url is None:
            # current page — use canonical self reference resolved later by caller
            elements.append({"@type": "ListItem", "position": idx, "name": text, "item": "__SELF__"})
        else:
            elements.append({"@type": "ListItem", "position": idx, "name": text, "item": url})
    return elements


def replace_schema(html: str, new_elements) -> str:
    # Find the BreadcrumbList node's itemListElement array text and swap it.
    pattern = re.compile(
        r'("@type":\s*"BreadcrumbList",\s*"itemListElement":\s*\[)(.*?)(\])',
        re.DOTALL,
    )
    m = pattern.search(html)
    if not m:
        return None
    items_json = ",\n        ".join(
        json.dumps(el, ensure_ascii=False, separators=(",", ":")) for el in new_elements
    )
    new_block = m.group(1) + "\n        " + items_json + "\n      " + m.group(3)
    return html[: m.start()] + new_block + html[m.end() :]


def get_canonical(html: str) -> str:
    m = re.search(r'rel="canonical" href="([^"]+)"', html)
    return m.group(1) if m else None


def process(slug: str) -> str:
    path = find_source(slug)
    html = path.read_text(encoding="utf-8")

    visible = parse_visible_breadcrumb(html)
    if not visible:
        return f"SKIP (couldn't parse visible breadcrumb): {slug}"

    canonical = get_canonical(html)
    elements = build_breadcrumb_json(visible)
    for el in elements:
        if el["item"] == "__SELF__":
            el["item"] = canonical or (SITE + "/" + slug + "/")

    new_html = replace_schema(html, elements)
    if new_html is None:
        return f"SKIP (no BreadcrumbList schema found): {slug}"

    if new_html == html:
        return f"NOCHANGE: {slug}"

    path.write_text(new_html, encoding="utf-8")
    names = [e["name"] for e in elements]
    return f"OK: {slug} -> {names}"


if __name__ == "__main__":
    for slug in SLUGS:
        print(process(slug))
