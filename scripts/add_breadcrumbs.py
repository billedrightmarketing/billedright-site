#!/usr/bin/env python3
"""
One-time migration: insert a visible breadcrumb nav into every page source
that already carries BreadcrumbList JSON-LD, so the schema matches what a
visitor actually sees (docs/TECHNICAL_SEO_AND_AI_SEARCH_STANDARD.md).

Reads the existing BreadcrumbList itemListElement out of each page's own
<script type="application/ld+json"> block and renders it as a visible
<nav aria-label="Breadcrumb"> inserted between {{NAV}} and <main>.
Idempotent: skips any page that already has a br-breadcrumb-nav element.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "pages"

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

BREADCRUMB_MARKER = "br-breadcrumb-nav"


def find_source(slug: str) -> Path:
    flat = PAGES_DIR / f"{slug}.html"
    if flat.exists():
        return flat
    nested = PAGES_DIR / slug / "index.html"
    if nested.exists():
        return nested
    raise FileNotFoundError(f"No source file found for slug: {slug}")


def extract_breadcrumb_items(html: str):
    # Find every JSON-LD script block and look for one containing BreadcrumbList
    for match in re.finditer(
        r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL
    ):
        block = match.group(1)
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        graph = data.get("@graph", [data] if isinstance(data, dict) else data)
        for node in graph:
            if isinstance(node, dict) and node.get("@type") == "BreadcrumbList":
                items = sorted(node["itemListElement"], key=lambda i: i["position"])
                return [(i["name"], i["item"]) for i in items]
    return None


def render_breadcrumb_html(items) -> str:
    parts = []
    for idx, (name, url) in enumerate(items):
        is_last = idx == len(items) - 1
        if is_last:
            parts.append(
                f'<span aria-current="page" style="color:var(--text-mid,#475569);font-weight:600">{name}</span>'
            )
        else:
            path = url.replace("https://billedright.com", "") or "/"
            parts.append(
                f'<a href="{path}" style="color:var(--text-muted,#64748b);text-decoration:none">{name}</a>'
            )
        if not is_last:
            parts.append(
                '<span aria-hidden="true" style="color:var(--border,#e4eaf2);margin:0 2px">/</span>'
            )
    inner = " ".join(parts)
    return (
        f'<nav class="{BREADCRUMB_MARKER}" aria-label="Breadcrumb" '
        f'style="max-width:1240px;margin:0 auto;padding:14px 28px 0;'
        f'font-size:12.5px;display:flex;align-items:center;flex-wrap:wrap;gap:4px">'
        f"{inner}</nav>\n\n"
    )


def process(slug: str) -> str:
    path = find_source(slug)
    html = path.read_text(encoding="utf-8")

    if BREADCRUMB_MARKER in html:
        return f"SKIP (already has breadcrumb): {slug}"

    items = extract_breadcrumb_items(html)
    if not items:
        return f"SKIP (no BreadcrumbList schema found): {slug}"

    breadcrumb_html = render_breadcrumb_html(items)

    if "{{NAV}}\n\n<main" in html:
        new_html = html.replace("{{NAV}}\n\n<main", "{{NAV}}\n\n" + breadcrumb_html + "<main", 1)
    elif "{{NAV}}\n<main" in html:
        new_html = html.replace("{{NAV}}\n<main", "{{NAV}}\n" + breadcrumb_html + "<main", 1)
    else:
        return f"FAIL (unexpected NAV/main pattern): {slug}"

    path.write_text(new_html, encoding="utf-8")
    return f"OK: {slug} -> {path.relative_to(ROOT)} ({len(items)} levels)"


if __name__ == "__main__":
    for slug in SLUGS:
        print(process(slug))
