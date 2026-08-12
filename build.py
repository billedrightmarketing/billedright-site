#!/usr/bin/env python3
"""
Build script for the BilledRight static site.

Reads each page in pages/*.html, injects the shared nav and footer
templates in place of the {{NAV}} / {{FOOTER}} placeholders, and writes
the result to dist/ using a clean-URL folder structure:

    pages/home.html         -> dist/index.html
    pages/services.html     -> dist/services/index.html
    pages/about.html        -> dist/about/index.html
    ...

Also copies assets/, netlify.toml, sitemap.xml, and robots.txt into dist/.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES_DIR = ROOT / "pages"
TEMPLATES_DIR = ROOT / "templates"
DIST_DIR = ROOT / "dist"

# Maps a pages/*.html source file to its output path under dist/.
# "home" is the site root; every other slug gets its own folder so the
# URL renders clean (e.g. /services/ instead of /services.html).
PAGE_OUTPUT_PATHS = {
    "home": "index.html",
    "services": "services/index.html",
    "specialties": "specialties/index.html",
    "credentialing": "credentialing/index.html",
    "about": "about/index.html",
    "blog": "blog/index.html",
    "resources": "resources/index.html",
    "case-studies": "case-studies/index.html",
    "testimonials": "testimonials/index.html",
    "contact": "contact/index.html",
    "psychiatry-rcm-services": "psychiatry-rcm-services/index.html",
    "cardiology-rcm-services": "cardiology-rcm-services/index.html",
    "behavioral-health-rcm-services": "behavioral-health-rcm-services/index.html",
    "internal-medicine-rcm-services": "internal-medicine-rcm-services/index.html",
    "rheumatology-rcm-services": "rheumatology-rcm-services/index.html",
    "nephrology-rcm-services": "nephrology-rcm-services/index.html",
    "urgent-care-rcm-services": "urgent-care-rcm-services/index.html",
    "pain-management-rcm-services": "pain-management-rcm-services/index.html",
    "gastroenterology-rcm-services": "gastroenterology-rcm-services/index.html",
    "primary-care-rcm-services": "primary-care-rcm-services/index.html",
    "vascular-surgery-rcm-services": "vascular-surgery-rcm-services/index.html",
    "allergy-rcm-services": "allergy-rcm-services/index.html",
    "pulmonary-rcm-services": "pulmonary-rcm-services/index.html",
    "insurance-eligibility": "insurance-eligibility/index.html",
}


def load_template(name: str) -> str:
    return (TEMPLATES_DIR / name).read_text(encoding="utf-8")


def build():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    nav_html = load_template("nav-template.html")
    footer_html = load_template("footer-template.html")

    for slug, output_rel_path in PAGE_OUTPUT_PATHS.items():
        source_path = PAGES_DIR / f"{slug}.html"
        if not source_path.exists():
            raise FileNotFoundError(f"Missing page source: {source_path}")

        html = source_path.read_text(encoding="utf-8")
        html = html.replace("{{NAV}}", nav_html)
        html = html.replace("{{FOOTER}}", footer_html)

        out_path = DIST_DIR / output_rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html, encoding="utf-8")
        print(f"  {source_path.relative_to(ROOT)} -> {out_path.relative_to(ROOT)}")

    # Copy static assets (skip OS junk files like .DS_Store).
    if (ROOT / "assets").exists():
        shutil.copytree(
            ROOT / "assets",
            DIST_DIR / "assets",
            ignore=shutil.ignore_patterns(".DS_Store"),
        )
        print("  assets/ -> dist/assets/")

    # Copy root-level static files needed at the site root.
    for filename in ("netlify.toml", "sitemap.xml", "robots.txt"):
        src = ROOT / filename
        if src.exists():
            shutil.copy2(src, DIST_DIR / filename)
            print(f"  {filename} -> dist/{filename}")

    print(f"\nBuild complete: {len(PAGE_OUTPUT_PATHS)} pages written to {DIST_DIR}")


if __name__ == "__main__":
    build()
