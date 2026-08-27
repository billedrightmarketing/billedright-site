#!/usr/bin/env python3
"""
One-time migration: install the Google Tag Manager container snippet
across every page source in pages/. Idempotent — skips any page that
already has the GTM ID.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "pages"
GTM_ID = "GTM-K8DSPBH"

HEAD_SNIPPET = f"""<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','{GTM_ID}');</script>
<!-- End Google Tag Manager -->
"""

BODY_SNIPPET = f"""<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""


def process(path: Path) -> str:
    html = path.read_text(encoding="utf-8")
    if GTM_ID in html:
        return f"SKIP (already installed): {path.relative_to(ROOT)}"

    if "<head>\n" not in html or "<body>\n" not in html:
        return f"FAIL (unexpected head/body pattern): {path.relative_to(ROOT)}"

    new_html = html.replace("<head>\n", HEAD_SNIPPET, 1)
    new_html = new_html.replace("<body>\n", BODY_SNIPPET, 1)

    path.write_text(new_html, encoding="utf-8")
    return f"OK: {path.relative_to(ROOT)}"


if __name__ == "__main__":
    for f in sorted(PAGES_DIR.rglob("*.html")):
        print(process(f))
