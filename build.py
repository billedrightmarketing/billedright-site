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

Also copies assets/, netlify.toml, sitemap.xml, robots.txt, and the favicon
files (favicon.ico, favicon-32x32.png, favicon-16x16.png,
apple-touch-icon.png) into dist/.

Blog posts are authored as markdown + frontmatter in content/blog/*.md (this
is what the Decap CMS admin panel writes to). Each one is rendered against
templates/blog-post-template.html and written to pages/blog/<slug>/index.html
— a generated page source, just like the hand-written ones — so it flows
through the normal {{NAV}}/{{FOOTER}} injection pass below. No third-party
markdown/YAML packages are used (Netlify's build step deliberately avoids
depending on `pip install` succeeding; see the netlify.toml comment), so
frontmatter parsing and markdown rendering are both hand-rolled below,
supporting only what the CMS fields and the template actually need.

dist/llms.txt and dist/okf/ (an Open Knowledge Format v0.2 bundle) are
generated — not copied — by generate_ai_files(), from the same
PAGE_OUTPUT_PATHS/page metadata/blog post list as everything else. See that
function's own comment for what's included/excluded.
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
    "credentialing": "services/credentialing/index.html",
    "about": "about/index.html",
    "blog": "blog/index.html",
    "resources": "resources/index.html",
    "resources/denial-write-off-calculator": "resources/denial-write-off-calculator/index.html",
    "resources/aging-ar-risk-calculator": "resources/aging-ar-risk-calculator/index.html",
    "resources/in-house-vs-outsourced-calculator": "resources/in-house-vs-outsourced-calculator/index.html",
    "resources/documentation-compliance-assessment": "resources/documentation-compliance-assessment/index.html",
    "resources/prior-authorization-burden-calculator": "resources/prior-authorization-burden-calculator/index.html",
    "resources/credentialing-readiness-assessment": "resources/credentialing-readiness-assessment/index.html",
    "resources/payer-enrollment-backlog-calculator": "resources/payer-enrollment-backlog-calculator/index.html",
    "resources/rcm-health-check-quiz": "resources/rcm-health-check-quiz/index.html",
    "case-studies": "case-studies/index.html",
    "case-studies/primary-care": "case-studies/primary-care/index.html",
    "case-studies/cardiology-denial-reduction": "case-studies/cardiology-denial-reduction/index.html",
    "case-studies/multispecialty-ar-cleanup": "case-studies/multispecialty-ar-cleanup/index.html",
    "case-studies/pain-management-denial-reduction": "case-studies/pain-management-denial-reduction/index.html",
    "case-studies/medical-center-turnaround": "case-studies/medical-center-turnaround/index.html",
    "case-studies/independent-cardiology-benchmark": "case-studies/independent-cardiology-benchmark/index.html",
    "case-studies/cardiology": "case-studies/cardiology/index.html",
    "case-studies/allergy": "case-studies/allergy/index.html",
    "case-studies/credentialing": "case-studies/credentialing/index.html",
    "testimonials": "testimonials/index.html",
    "contact": "contact/index.html",
    "psychiatry-rcm-services": "specialties/psychiatry-rcm-services/index.html",
    "cardiology-rcm-services": "specialties/cardiology-rcm-services/index.html",
    "behavioral-health-rcm-services": "specialties/behavioral-health-rcm-services/index.html",
    "internal-medicine-rcm-services": "specialties/internal-medicine-rcm-services/index.html",
    "rheumatology-rcm-services": "specialties/rheumatology-rcm-services/index.html",
    "nephrology-rcm-services": "specialties/nephrology-rcm-services/index.html",
    "urgent-care-rcm-services": "specialties/urgent-care-rcm-services/index.html",
    "pain-management-rcm-services": "specialties/pain-management-rcm-services/index.html",
    "gastroenterology-rcm-services": "specialties/gastroenterology-rcm-services/index.html",
    "primary-care-rcm-services": "specialties/primary-care-rcm-services/index.html",
    "vascular-surgery-rcm-services": "specialties/vascular-surgery-rcm-services/index.html",
    "allergy-rcm-services": "specialties/allergy-rcm-services/index.html",
    "pulmonary-rcm-services": "specialties/pulmonary-rcm-services/index.html",
    "insurance-eligibility": "services/insurance-eligibility/index.html",
    "charge-posting": "services/charge-posting/index.html",
    "documentation-review": "services/documentation-review/index.html",
    "claim-submission": "services/claim-submission/index.html",
    "denial-management": "services/denial-management/index.html",
    "medical-coding": "services/medical-coding/index.html",
    "payment-posting": "services/payment-posting/index.html",
    "patient-ar-collections": "services/patient-ar-collections/index.html",
    "ar-follow-up": "services/ar-follow-up/index.html",
    "ar-rescue": "services/ar-rescue/index.html",
    "financial-assessment": "services/financial-assessment/index.html",
    "reporting": "services/reporting/index.html",
    "authorizations": "services/authorizations/index.html",
    "account-management": "services/account-management/index.html",
    "documentation-management": "services/documentation-management/index.html",
    "contract-renegotiation": "services/contract-renegotiation/index.html",
    "why-billed-right": "why-billed-right/index.html",
    "leadership": "leadership/index.html",
    "awards": "awards/index.html",
    "recognition": "recognition/index.html",
    "private-equity": "private-equity/index.html",
    "who-we-serve": "who-we-serve/index.html",
    "who-we-serve/cpas-healthcare-financial-advisors": "who-we-serve/cpas-healthcare-financial-advisors/index.html",
    # Redirect-landing page for the retired Custom Billing Service of Ohio
    # (billingmyservices.com) domain — not linked from nav and deliberately
    # excluded from sitemap.xml (see the page's own noindex meta tags).
    "welcome-cbs": "welcome-cbs/index.html",
    "locations": "locations/index.html",
    "careers-us": "careers-us/index.html",
    "careers-india": "careers-india/index.html",
    "privacy-policy": "privacy-policy/index.html",
    "sms-consent": "sms-consent/index.html",
    "terms-and-conditions": "terms-and-conditions/index.html",
    "faq": "faq/index.html",
    "eclinicalworks-billing-services": "services/eclinicalworks-billing-services/index.html",
    "emr-billing-platforms": "services/emr-billing-platforms/index.html",
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
    # Netlify's custom-error-page convention: a 404.html at the publish
    # directory ROOT (not nested in a folder) is served automatically for
    # any unmatched route, no redirect rule required. Must stay a flat
    # top-level path here for that to work.
    "404": "404.html",
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
    H2/H3 headings, paragraphs, bullet lists, bold text, links, and
    simple GitHub-style pipe tables (| cell | cell |, with a |---|---|
    separator row right under the header)."""
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

    def is_table_row(s: str) -> bool:
        return len(s) > 1 and s.startswith("|") and s.endswith("|")

    def is_separator_row(s: str) -> bool:
        cells = [c.strip() for c in s.strip("|").split("|")]
        return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c) for c in cells)

    def split_row(s: str) -> list:
        return [c.strip() for c in s.strip("|").split("|")]

    i = 0
    n = len(lines)
    while i < n:
        stripped = lines[i].strip()
        if not stripped:
            flush_para()
            close_list()
            i += 1
        elif stripped.startswith("### "):
            flush_para()
            close_list()
            out.append("<h3>" + render_inline_markdown(stripped[4:].strip()) + "</h3>")
            i += 1
        elif stripped.startswith("## "):
            flush_para()
            close_list()
            out.append("<h2>" + render_inline_markdown(stripped[3:].strip()) + "</h2>")
            i += 1
        elif stripped.startswith("- "):
            flush_para()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append("<li>" + render_inline_markdown(stripped[2:].strip()) + "</li>")
            i += 1
        elif is_table_row(stripped) and i + 1 < n and is_separator_row(lines[i + 1].strip()):
            flush_para()
            close_list()
            header = split_row(stripped)
            ncols = len(header)
            i += 2  # skip the header row and the |---|---| separator row
            body_rows = []
            while i < n and is_table_row(lines[i].strip()):
                body_rows.append(split_row(lines[i].strip()))
                i += 1
            table = ['<div class="br-table-wrap"><table><thead><tr>']
            table += [f"<th>{render_inline_markdown(c)}</th>" for c in header]
            table.append("</tr></thead><tbody>")
            for row in body_rows:
                padded = (row + [""] * ncols)[:ncols]
                table.append("<tr>" + "".join(f"<td>{render_inline_markdown(c)}</td>" for c in padded) + "</tr>")
            table.append("</tbody></table></div>")
            out.append("".join(table))
        else:
            close_list()
            para.append(stripped)
            i += 1

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


def build_blog_posts() -> tuple:
    """Render content/blog/*.md against templates/blog-post-template.html,
    writing each to pages/blog/<slug>/index.html. Returns (output_paths,
    posts): output_paths is a dict in the same shape as PAGE_OUTPUT_PATHS
    so the caller can merge it in and let the normal {{NAV}}/{{FOOTER}}
    pass below pick the generated pages up; posts is the parsed, sorted
    list, reused by render_blog_archive() so it doesn't have to re-parse
    every markdown file a second time."""
    md_files = sorted(CONTENT_BLOG_DIR.glob("*.md")) if CONTENT_BLOG_DIR.exists() else []
    if not md_files:
        return {}, []

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
            # CMS "Draft" checkbox (static/admin/config.yml). Draft posts still
            # render on the live site like any other post (unchanged behavior)
            # but are excluded from the generated llms.txt / okf/ AI-readable
            # files by generate_ai_files() below — see TEST_POST_SLUGS, which
            # this field supersedes for future posts.
            "draft": fields.get("draft", "").strip().lower() == "true",
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

    return output_paths, posts


def json_escape(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\r", "")
    )


# CMS test entries created while trying out the Decap CMS — real content,
# but not meant for the public archive.
TEST_POST_SLUGS = {"sd", "this-is-a-test-blog-post"}


def category_slug(category: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", category.lower()).strip("-")
    return slug or "general"


def render_blog_card(post: dict, featured: bool) -> str:
    category = post["category"] or "General"
    img_style = (
        f"background-image:url('{html.escape(post['title_image'], quote=True)}');"
        f"background-size:cover;background-position:center"
        if post["title_image"] else
        "background:linear-gradient(135deg,#1a2535,#31425E)"
    )
    date_label = (
        f"{post['date_obj'].strftime('%B')} {post['date_obj'].day}, {post['date_obj'].year}"
        if post["date_obj"] else ""
    )
    return (
        f'<a href="/blog/{post["slug"]}/" class="br-blog-card" data-cat="{category_slug(category)}">'
        f'<div class="br-blog-img{" tall" if featured else ""}" style="{img_style}">'
        f'<div class="br-blog-overlay">'
        f'<span class="br-blog-cat">{html.escape(category, quote=True)}</span>'
        f'<div class="br-blog-img-title">{html.escape(post["title"], quote=True)}</div>'
        f'</div></div>'
        f'<div class="br-blog-body">'
        f'<p>{html.escape(post["meta_description"], quote=True)}</p>'
        f'<div class="br-blog-foot">'
        f'<span class="br-blog-kw">{date_label}</span>'
        f'<span class="br-blog-read">Read <svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>'
        f'</div></div></a>'
    )


def render_blog_archive(all_posts: list) -> tuple:
    """Build the /blog/ archive's filter-button row and post-card grid
    from the same parsed post list build_blog_posts() already produced.
    Returns (filter_buttons_html, grid_html)."""
    posts = [p for p in all_posts if p["slug"] not in TEST_POST_SLUGS]

    categories = sorted({p["category"] for p in posts if p["category"]})
    buttons = ['<button class="br-filter-btn active" onclick="brFilterBlog(\'all\',this)">All Resources</button>']
    for category in categories:
        buttons.append(
            f'<button class="br-filter-btn" onclick="brFilterBlog(\'{category_slug(category)}\',this)">'
            f'{html.escape(category, quote=True)}</button>'
        )

    cards = [render_blog_card(post, featured=(i == 0)) for i, post in enumerate(posts)]
    return "".join(buttons), "\n".join(cards)


# ─────────────────────────────────────────────────────────────────────────
# AI-readable site files: /llms.txt and /okf/ (Open Knowledge Format v0.2).
#
# Both are generated from the same data every other page is built from —
# PAGE_OUTPUT_PATHS, each page's own <title>/<meta description>/<h2> markup,
# and the parsed blog post list — so a new specialty/service page or blog
# post is picked up automatically the next time build.py runs, with no
# separate file to hand-maintain. Design-only edits (CSS, images, spacing)
# never touch title/meta/h2 text, so they never produce a diff here.
#
# Pages are excluded automatically by rule (see ai_file_excluded()) rather
# than via a hand-maintained include list: the 404 page, the retired
# welcome-cbs redirect landing page, every thank-you/* confirmation page,
# and the legal/compliance pages (Privacy Policy, Terms, SMS Consent —
# already noindex and already absent from sitemap.xml, so this keeps the
# same policy consistent here). Draft blog posts (CMS "Draft" checkbox,
# or the two known legacy test posts in TEST_POST_SLUGS) are excluded the
# same way. Individual blog posts are deliberately left out of llms.txt
# itself (only the /blog/ hub is linked there, per llms.txt's own intent
# to stay concise) but each gets a lightweight OKF concept file.
# ─────────────────────────────────────────────────────────────────────────

LEGAL_SLUGS = {"privacy-policy", "sms-consent", "terms-and-conditions"}

# Short, deliberately conservative company summary for the llms.txt
# blockquote. NOT sourced from pages/home.html's own <meta description>,
# which currently repeats several claims
# (docs/BILLED_RIGHT_FACTS_AND_GUARDRAILS.md lists "$2B+ billed", "94%
# client retention", etc. under "Existing Staging Claims Requiring
# Validation") — this file shouldn't propagate an unverified number into a
# new AI-facing surface just because it's easy to scrape. Update this by
# hand only if the company's core positioning statement changes.
LLMS_TXT_SUMMARY = (
    "Billed Right is a healthcare Revenue Cycle Management company and "
    "Enterprise Revenue Performance Partner, founded in 2006 and "
    "headquartered in Longwood, Florida. It provides end-to-end RCM "
    "services — billing, denial management, credentialing, and revenue-cycle "
    "analytics — to healthcare organizations across the United States."
)

_HTML_TAG_RE = re.compile(r"<[^>]+>")
_TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
_DESCRIPTION_RE = re.compile(r'<meta\s+name="description"\s+content="(.*?)"', re.S)
_H2_RE = re.compile(r"<h2[^>]*>(.*?)</h2>", re.S)


def _clean_text(raw: str) -> str:
    return html.unescape(_HTML_TAG_RE.sub("", raw)).strip()


def extract_page_meta(html_text: str) -> dict:
    """Pull the same title/description/heading data already authored on
    every page — no new content, just reuse of what's already there."""
    title_m = _TITLE_RE.search(html_text)
    desc_m = _DESCRIPTION_RE.search(html_text)
    h2s = [_clean_text(h) for h in _H2_RE.findall(html_text)]
    return {
        "title": _clean_text(title_m.group(1)) if title_m else "",
        "description": _clean_text(desc_m.group(1)) if desc_m else "",
        "h2s": [h for h in h2s if h][:8],
    }


def ai_file_excluded(slug: str) -> bool:
    if slug in LEGAL_SLUGS or slug in ("404", "welcome-cbs"):
        return True
    if slug.startswith("thank-you/"):
        return True
    return False


def canonical_url_for(output_rel_path: str) -> str:
    if output_rel_path == "index.html":
        return f"{SITE_URL}/"
    if output_rel_path.endswith("/index.html"):
        return f"{SITE_URL}/{output_rel_path[:-len('index.html')]}"
    return f"{SITE_URL}/{output_rel_path}"


_SECTION_PREFIXES = [
    ("specialties/", "Specialties", "specialties"),
    ("services/", "Services", "services"),
    ("case-studies/", "Case Studies", "case-studies"),
    ("blog/", "Blog", "blog"),
]


def classify_page(output_rel_path: str) -> tuple:
    """Returns (llms_txt_section_name, okf_subdirectory) for a page, based
    purely on its own URL structure — matches the site's actual
    information architecture instead of a separately maintained list."""
    for prefix, section, subdir in _SECTION_PREFIXES:
        if output_rel_path.startswith(prefix):
            return section, subdir
    return "Company", "company"


def okf_concept_path(output_rel_path: str, slug: str) -> str:
    _, subdir = classify_page(output_rel_path)
    if output_rel_path == "index.html":
        return "company/home.md"
    if output_rel_path == f"{subdir}/index.html":
        # A section hub (services/specialties/case-studies/blog index) —
        # sits as a file beside its own subdirectory of concept files.
        return f"{subdir}.md"
    leaf = slug.rsplit("/", 1)[-1]
    return f"{subdir}/{leaf}.md"


def okf_frontmatter(concept_type: str, title: str, description: str, resource: str, tags: list) -> str:
    lines = ["---", f"type: {concept_type}"]
    if title:
        lines.append(f"title: {yaml_scalar(title)}")
    if description:
        lines.append(f"description: {yaml_scalar(description)}")
    lines.append(f"resource: {resource}")
    if tags:
        lines.append("tags: [" + ", ".join(tags) + "]")
    lines.append("---")
    return "\n".join(lines)


def yaml_scalar(value: str) -> str:
    # Minimal safe YAML scalar quoting — same "don't need a real parser/
    # library" philosophy as parse_frontmatter() above.
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def generate_ai_files(all_output_paths: dict, blog_posts: list):
    """Writes dist/llms.txt and the dist/okf/ bundle. See the module
    comment above this function for what's included/excluded and why."""
    okf_dir = DIST_DIR / "okf"
    okf_dir.mkdir(parents=True, exist_ok=True)

    sections = {"Company": [], "Services": [], "Specialties": [], "Case Studies": [], "Blog": []}

    for slug, output_rel_path in all_output_paths.items():
        if ai_file_excluded(slug):
            continue
        if slug.startswith("blog/"):
            continue  # blog posts handled separately below (OKF only)

        source_path = PAGES_DIR / f"{slug}.html"
        if not source_path.exists():
            source_path = PAGES_DIR / slug / "index.html"
        if not source_path.exists():
            continue
        meta = extract_page_meta(source_path.read_text(encoding="utf-8"))
        resource = canonical_url_for(output_rel_path)
        section, subdir = classify_page(output_rel_path)
        concept_rel = okf_concept_path(output_rel_path, slug)

        sections[section].append({
            "title": meta["title"] or slug,
            "description": meta["description"],
            "resource": resource,
            "concept_rel": concept_rel,
        })

        concept_type = {
            "Specialties": "SpecialtyPage",
            "Services": "ServicePage",
            "Case Studies": "CaseStudyPage",
            "Blog": "WebPage",
            "Company": "WebPage",
        }[section]
        tag_singular = {
            "specialties": "specialty",
            "services": "service",
            "case-studies": "case-study",
            "blog": "blog",
            "company": "company",
        }[subdir]
        tags = [tag_singular]
        body_lines = [f"# {meta['title'] or slug}", ""]
        if meta["description"]:
            body_lines += [meta["description"], ""]
        if meta["h2s"]:
            body_lines.append("## On This Page")
            body_lines += [f"- {h}" for h in meta["h2s"]]
            body_lines.append("")
        body_lines.append(f"[View live page]({resource})")

        concept_path = okf_dir / concept_rel
        concept_path.parent.mkdir(parents=True, exist_ok=True)
        concept_path.write_text(
            okf_frontmatter(concept_type, meta["title"] or slug, meta["description"], resource, tags)
            + "\n\n" + "\n".join(body_lines) + "\n",
            encoding="utf-8",
        )

    # Blog posts: OKF concept files only (not listed individually in
    # llms.txt — the /blog/ hub link above covers that, per llms.txt's own
    # intent to stay a concise index rather than a full content dump).
    for post in blog_posts:
        if post["slug"] in TEST_POST_SLUGS or post.get("draft"):
            continue
        resource = f"{SITE_URL}/blog/{post['slug']}/"
        tags = ["blog"]
        if post["category"]:
            tags.append(category_slug(post["category"]))
        body_headings = [
            line[3:].strip().strip("*").strip() for line in post["body_md"].splitlines()
            if line.strip().startswith("## ")
        ][:8]
        body_lines = [f"# {post['title']}", ""]
        if post["meta_description"]:
            body_lines += [post["meta_description"], ""]
        if post["category"]:
            body_lines += [f"Category: {post['category']}", ""]
        if body_headings:
            body_lines.append("## On This Page")
            body_lines += [f"- {h}" for h in body_headings]
            body_lines.append("")
        body_lines.append(f"[View live page]({resource})")

        concept_path = okf_dir / "blog" / f"{post['slug']}.md"
        concept_path.parent.mkdir(parents=True, exist_ok=True)
        concept_path.write_text(
            okf_frontmatter("BlogPosting", post["title"], post["meta_description"], resource, tags)
            + "\n\n" + "\n".join(body_lines) + "\n",
            encoding="utf-8",
        )

    # okf/index.md — bundle-root directory listing. Not itself a concept
    # (index.md is a reserved OKF filename), so no `type` field.
    index_lines = [
        "---", 'okf_version: "0.2"', "---", "",
        "# Billed Right — Open Knowledge Format Bundle", "",
        "Machine-readable concept files describing Billed Right's public",
        "website content. Each concept links back to its live page via its",
        "`resource` field.", "",
    ]
    for section_name in ("Company", "Services", "Specialties", "Case Studies", "Blog"):
        items = sections[section_name]
        if not items:
            continue
        index_lines.append(f"## {section_name}")
        for item in sorted(items, key=lambda x: x["title"]):
            index_lines.append(f"- [{item['title']}](./{item['concept_rel']})")
        index_lines.append("")
    real_blog_posts = [p for p in blog_posts if p["slug"] not in TEST_POST_SLUGS and not p.get("draft")]
    if real_blog_posts:
        index_lines.append("## Blog Posts")
        index_lines.append(f"- [{len(real_blog_posts)} articles](./blog/) — see individual concept files under `blog/`")
        index_lines.append("")

    (okf_dir / "index.md").write_text("\n".join(index_lines), encoding="utf-8")

    # llms.txt
    lines = ["# Billed Right", "", f"> {LLMS_TXT_SUMMARY}", ""]
    for section_name in ("Company", "Services", "Specialties", "Case Studies"):
        items = sections[section_name]
        if not items:
            continue
        lines.append(f"## {section_name}")
        for item in sorted(items, key=lambda x: x["title"]):
            desc = f": {item['description']}" if item["description"] else ""
            lines.append(f"- [{item['title']}]({item['resource']}){desc}")
        lines.append("")
    blog_items = sections["Blog"]
    if blog_items:
        lines.append("## Blog")
        for item in blog_items:
            desc = f": {item['description']}" if item["description"] else ""
            lines.append(f"- [{item['title']}]({item['resource']}){desc}")
        lines.append("")

    (DIST_DIR / "llms.txt").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"  generated dist/llms.txt and dist/okf/ ({sum(len(v) for v in sections.values())} pages + {len(real_blog_posts)} blog posts)")


def build():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    # Render markdown blog posts to pages/blog/<slug>/index.html before the
    # main pass below, so they get {{NAV}}/{{FOOTER}} injected and copied to
    # dist/ exactly like every hand-written page.
    blog_output_paths, blog_posts = build_blog_posts()
    all_output_paths = {**PAGE_OUTPUT_PATHS, **blog_output_paths}
    blog_filter_buttons, blog_grid_html = render_blog_archive(blog_posts)

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
        if slug == "blog":
            html = html.replace("{{BLOG_FILTER_BUTTONS}}", blog_filter_buttons)
            html = html.replace("{{BLOG_POSTS_GRID}}", blog_grid_html)

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

    # Copy signature/ (email signature assets, e.g. the 20 years GIF) so
    # they're reachable at /signature/... rather than nested under /assets/.
    if (ROOT / "signature").exists():
        shutil.copytree(
            ROOT / "signature",
            DIST_DIR / "signature",
            ignore=shutil.ignore_patterns(".DS_Store"),
        )
        print("  signature/ -> dist/signature/")

    # Copy root-level static files needed at the site root.
    for filename in (
        "netlify.toml", "sitemap.xml", "robots.txt",
        "favicon.ico", "favicon-32x32.png", "favicon-16x16.png", "apple-touch-icon.png",
    ):
        src = ROOT / filename
        if src.exists():
            shutil.copy2(src, DIST_DIR / filename)
            print(f"  {filename} -> dist/{filename}")

    # dist/llms.txt and dist/okf/ are generated, not copied — see
    # generate_ai_files()'s own docstring/comment for what's included.
    generate_ai_files(all_output_paths, blog_posts)

    print(f"\nBuild complete: {len(all_output_paths)} pages written to {DIST_DIR}")


if __name__ == "__main__":
    build()
