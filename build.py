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
    "case-studies/primary-care": "case-studies/primary-care/index.html",
    "case-studies/cardiology": "case-studies/cardiology/index.html",
    "case-studies/allergy": "case-studies/allergy/index.html",
    "case-studies/credentialing": "case-studies/credentialing/index.html",
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
    "charge-posting": "charge-posting/index.html",
    "documentation-review": "documentation-review/index.html",
    "claim-submission": "claim-submission/index.html",
    "denial-management": "denial-management/index.html",
    "medical-coding": "medical-coding/index.html",
    "payment-posting": "payment-posting/index.html",
    "patient-ar-collections": "patient-ar-collections/index.html",
    "ar-follow-up": "ar-follow-up/index.html",
    "reporting": "reporting/index.html",
    "authorizations": "authorizations/index.html",
    "account-management": "account-management/index.html",
    "documentation-management": "documentation-management/index.html",
    "contract-renegotiation": "contract-renegotiation/index.html",
    "why-billed-right": "why-billed-right/index.html",
    "leadership": "leadership/index.html",
    "awards": "awards/index.html",
    "recognition": "recognition/index.html",
    "private-equity": "private-equity/index.html",
    "locations": "locations/index.html",
    "careers-us": "careers-us/index.html",
    "careers-india": "careers-india/index.html",
    "privacy-policy": "privacy-policy/index.html",
    "sms-consent": "sms-consent/index.html",
    "terms-and-conditions": "terms-and-conditions/index.html",
    "faq": "faq/index.html",
    "eclinicalworks-billing-services": "eclinicalworks-billing-services/index.html",
    "emr-billing-platforms": "emr-billing-platforms/index.html",
    "thank-you/psychiatry": "thank-you/psychiatry/index.html",
    "thank-you/cardiology": "thank-you/cardiology/index.html",
    "thank-you/behavioral-health": "thank-you/behavioral-health/index.html",
    "thank-you/internal-medicine": "thank-you/internal-medicine/index.html",
    "thank-you/rheumatology": "thank-you/rheumatology/index.html",
    "thank-you/allergy": "thank-you/allergy/index.html",
    "thank-you/nephrology": "thank-you/nephrology/index.html",
    "thank-you/urgent-care": "thank-you/urgent-care/index.html",
    "thank-you/pain-management": "thank-you/pain-management/index.html",
    "thank-you/gastroenterology": "thank-you/gastroenterology/index.html",
    "thank-you/primary-care": "thank-you/primary-care/index.html",
    "thank-you/vascular-surgery": "thank-you/vascular-surgery/index.html",
    "thank-you/pulmonary": "thank-you/pulmonary/index.html",
    "thank-you/contact": "thank-you/contact/index.html",
    "thank-you/consultation": "thank-you/consultation/index.html",
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
        # Most pages are flat files (pages/<slug>.html). A few, like the
        # thank-you pages, are organized as real nested folders
        # (pages/<slug>/index.html) so the source tree mirrors dist/.
        source_path = PAGES_DIR / f"{slug}.html"
        if not source_path.exists():
            source_path = PAGES_DIR / slug / "index.html"
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
