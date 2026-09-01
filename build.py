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

Also copies assets/, netlify.toml, sitemap.xml, robots.txt, and llms.txt into dist/.

Blog posts are authored as markdown + frontmatter in content/blog/*.md (this
is what the Decap CMS admin panel writes to). Each one is rendered against
templates/blog-post-template.html and written to pages/blog/<slug>/index.html
— a generated page source, just like the hand-written ones — so it flows
through the normal {{NAV}}/{{FOOTER}} injection pass below. No third-party
markdown/YAML packages are used (Netlify's build step deliberately avoids
depending on `pip install` succeeding; see the netlify.toml comment), so
frontmatter parsing and markdown rendering are both hand-rolled below,
supporting only what the CMS fields and the template actually need.
"""
import html
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES_DIR = ROOT / "pages"
TEMPLATES_DIR = ROOT / "templates"
DIST_DIR = ROOT / "dist"
CONTENT_BLOG_DIR = ROOT / "content" / "blog"
SITE_URL = "https://billedright.com"

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


def parse_frontmatter(raw: str):
    """Split a `---`-delimited frontmatter block from the markdown body.

    Minimal by design: handles the flat `key: value` pairs the Decap CMS
    blog collection actually produces (string, select, and datetime
    widgets), with optional quotes around the value. Not a general YAML
    parser.
    """
    raw = raw.lstrip("﻿")
    parts = raw.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Missing or malformed frontmatter block")

    fields = {}
    for line in parts[1].split("\n"):
        line = line.rstrip()
        if not line.strip() or line.strip().startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        fields[key] = value

    body = parts[2].lstrip("\n")
    return fields, body


def render_inline_markdown(text: str) -> str:
    text = html.escape(text, quote=True)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text


def markdown_to_html(md: str) -> str:
    """Convert the subset of markdown the blog post template supports:
    H2/H3 headings, paragraphs, bullet lists, bold text, and links."""
    lines = md.replace("\r\n", "\n").split("\n")
    out = []
    in_list = False
    para = []

    def flush_para():
        if para:
            out.append("<p>" + render_inline_markdown(" ".join(para).strip()) + "</p>")
            para.clear()

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_para()
            close_list()
        elif stripped.startswith("### "):
            flush_para()
            close_list()
            out.append("<h3>" + render_inline_markdown(stripped[4:].strip()) + "</h3>")
        elif stripped.startswith("## "):
            flush_para()
            close_list()
            out.append("<h2>" + render_inline_markdown(stripped[3:].strip()) + "</h2>")
        elif stripped.startswith("- "):
            flush_para()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append("<li>" + render_inline_markdown(stripped[2:].strip()) + "</li>")
        else:
            close_list()
            para.append(stripped)

    flush_para()
    close_list()
    return "\n".join(out)


def parse_post_date(raw_date: str, filename_date: str | None):
    raw_date = (raw_date or "").strip()
    candidates = [raw_date]
    if "T" in raw_date:
        candidates.append(raw_date.split("T")[0])
    for candidate in candidates:
        for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S"):
            try:
                return datetime.strptime(candidate, fmt)
            except ValueError:
                continue
    if filename_date:
        try:
            return datetime.strptime(filename_date, "%Y-%m-%d")
        except ValueError:
            pass
    return None


def slug_from_filename(filename: str) -> str:
    stem = filename[:-3] if filename.endswith(".md") else filename
    match = re.match(r"^\d{4}-\d{2}-\d{2}-(.+)$", stem)
    return match.group(1) if match else stem


def build_blog_posts() -> dict:
    """Render content/blog/*.md against templates/blog-post-template.html,
    writing each to pages/blog/<slug>/index.html. Returns a dict in the
    same shape as PAGE_OUTPUT_PATHS so the caller can merge it in and let
    the normal {{NAV}}/{{FOOTER}} pass below pick the generated pages up."""
    md_files = sorted(CONTENT_BLOG_DIR.glob("*.md")) if CONTENT_BLOG_DIR.exists() else []
    if not md_files:
        return {}

    template = load_template("blog-post-template.html")

    posts = []
    for md_path in md_files:
        fields, body_md = parse_frontmatter(md_path.read_text(encoding="utf-8"))
        date_match = re.match(r"^(\d{4}-\d{2}-\d{2})-", md_path.stem)
        posts.append({
            "slug": slug_from_filename(md_path.name),
            "title": fields.get("title", "").strip(),
            "author": fields.get("author", "Billed Right").strip() or "Billed Right",
            "category": fields.get("category", "").strip(),
            "meta_description": fields.get("meta_description", "").strip(),
            "title_image": fields.get("title_image", "").strip(),
            "body_md": body_md,
            "date_obj": parse_post_date(fields.get("date", ""), date_match.group(1) if date_match else None),
        })

    # Most recently published first; posts with an unparseable date sort last.
    posts.sort(key=lambda p: p["date_obj"] or datetime.min, reverse=True)

    output_paths = {}
    for post in posts:
        related = [
            p for p in posts
            if p is not post and p["category"] and p["category"] == post["category"]
        ][:3]
        if related:
            related_html = "\n".join(
                '<a href="/blog/{slug}/" class="br-related-post">\n'
                '  <div class="br-related-thumb"></div>\n'
                '  <div class="br-related-info">\n'
                '    <div class="br-related-title">{title}</div>\n'
                '    <div class="br-related-cat">{category}</div>\n'
                '  </div>\n'
                '</a>'.format(
                    slug=r["slug"],
                    title=html.escape(r["title"], quote=True),
                    category=html.escape(r["category"], quote=True),
                )
                for r in related
            )
        else:
            related_html = '<p class="br-related-empty">More articles coming soon.</p>'

        if post["title_image"]:
            og_image = post["title_image"] if post["title_image"].startswith("http") else SITE_URL + post["title_image"]
            title_image_block = '<img src="{src}" alt="{alt}" class="br-post-hero-image" width="1200" height="480">'.format(
                src=html.escape(post["title_image"], quote=True),
                alt=html.escape(post["title"], quote=True),
            )
        else:
            og_image = f"{SITE_URL}/og-image.jpg"
            title_image_block = ""

        canonical_url = f"{SITE_URL}/blog/{post['slug']}/"
        date_iso = post["date_obj"].strftime("%Y-%m-%d") if post["date_obj"] else ""
        date_display = (
            f"{post['date_obj'].strftime('%B')} {post['date_obj'].day}, {post['date_obj'].year}"
            if post["date_obj"] else ""
        )

        def j(value: str) -> str:
            # Inner text for a JSON string literal already wrapped in
            # quotes by the template — not full JSON, just its escaping.
            return json_escape(value)

        replacements = {
            "{{POST_TITLE}}": html.escape(post["title"], quote=True),
            "{{POST_META_DESCRIPTION}}": html.escape(post["meta_description"], quote=True),
            "{{POST_CANONICAL_URL}}": canonical_url,
            "{{POST_OG_IMAGE}}": og_image,
            "{{POST_DATE_ISO}}": date_iso,
            "{{POST_DATE_DISPLAY}}": date_display,
            "{{POST_AUTHOR}}": html.escape(post["author"], quote=True),
            "{{POST_CATEGORY}}": html.escape(post["category"], quote=True),
            "{{POST_TITLE_IMAGE_BLOCK}}": title_image_block,
            "{{POST_BODY_HTML}}": markdown_to_html(post["body_md"]),
            "{{POST_RELATED_HTML}}": related_html,
            "{{POST_TITLE_JSON}}": j(post["title"]),
            "{{POST_META_DESCRIPTION_JSON}}": j(post["meta_description"]),
            "{{POST_CANONICAL_URL_JSON}}": j(canonical_url),
            "{{POST_OG_IMAGE_JSON}}": j(og_image),
            "{{POST_AUTHOR_JSON}}": j(post["author"]),
            "{{POST_CATEGORY_JSON}}": j(post["category"]),
            "{{POST_DATE_ISO_JSON}}": j(date_iso),
        }

        rendered = template
        for placeholder, value in replacements.items():
            rendered = rendered.replace(placeholder, value)

        out_path = PAGES_DIR / "blog" / post["slug"] / "index.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(rendered, encoding="utf-8")
        print(f"  content/blog/{post['slug']}.md -> {out_path.relative_to(ROOT)}")

        output_paths[f"blog/{post['slug']}"] = f"blog/{post['slug']}/index.html"

    return output_paths


def json_escape(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\r", "")
    )


def build():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    # Render markdown blog posts to pages/blog/<slug>/index.html before the
    # main pass below, so they get {{NAV}}/{{FOOTER}} injected and copied to
    # dist/ exactly like every hand-written page.
    blog_output_paths = build_blog_posts()
    all_output_paths = {**PAGE_OUTPUT_PATHS, **blog_output_paths}

    nav_html = load_template("nav-template.html")
    footer_html = load_template("footer-template.html")

    for slug, output_rel_path in all_output_paths.items():
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

    # Copy static/ files (e.g. the Decap CMS admin panel) to the dist root.
    if (ROOT / "static").exists():
        shutil.copytree(
            ROOT / "static",
            DIST_DIR,
            ignore=shutil.ignore_patterns(".DS_Store"),
            dirs_exist_ok=True,
        )
        print("  static/ -> dist/")

    # Copy root-level static files needed at the site root.
    for filename in ("netlify.toml", "sitemap.xml", "robots.txt", "llms.txt"):
        src = ROOT / filename
        if src.exists():
            shutil.copy2(src, DIST_DIR / filename)
            print(f"  {filename} -> dist/{filename}")

    print(f"\nBuild complete: {len(all_output_paths)} pages written to {DIST_DIR}")


if __name__ == "__main__":
    build()
