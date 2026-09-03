#!/usr/bin/env python3
"""
One-time migration script: scrapes the old WordPress blog posts listed in
blog_urls.txt and converts each into a content/blog/<slug>.md file the
Decap CMS / build.py blog pipeline can pick up directly.

Uses only the Python standard library (urllib + html.parser) — this
project deliberately avoids pip dependencies in its build tooling (see
build.py's own docstring), so this script follows the same convention
rather than requiring `pip install requests beautifulsoup4`.

Extraction is written against billedright.com's actual WordPress/HealSoul
theme markup, confirmed by inspecting a live post before writing this:
  - Title:     <meta property="og:title"> (the theme's own <h1> is just
               the literal word "Blog" on every post, so it's unusable —
               falls back to <title> then that <h1> only if og:title is
               missing).
  - Body:      <div class="entry-content"> ... </div>
  - Image:     <meta property="og:image">
  - Category:  first <a href="/category/...">
  - Date:      <meta property="article:published_time">
  - Description: <meta name="description"> (falls back to og:description)

The body HTML is converted to the markdown subset build.py's
markdown_to_html() actually supports: H2/H3 headings, paragraphs, bullet
lists, bold text, links, and simple pipe tables. Nested lists are
flattened to a single level since the site has no nested-list renderer.
Inline images/figures are dropped — only the one featured image
per post is kept.

Usage:
    python3 scrape_blogs.py            # skips any URL already in content/blog/
    python3 scrape_blogs.py --force    # re-scrapes and overwrites every URL,
                                        # even ones already saved
"""
import argparse
import html
import re
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
URLS_FILE = ROOT / "blog_urls.txt"
CONTENT_BLOG_DIR = ROOT / "content" / "blog"
IMAGES_DIR = ROOT / "assets" / "blog"
ERROR_LOG = ROOT / "scrape_errors.txt"

REQUEST_DELAY_SECONDS = 1
REQUEST_TIMEOUT = 20
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 "
    "BilledRightBlogMigration/1.0"
)


# ─────────────────────────────────────────────────────────────────────────
# HTTP
# ─────────────────────────────────────────────────────────────────────────

def fetch_url(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def download_image(url: str, dest: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
        dest.write_bytes(resp.read())


# ─────────────────────────────────────────────────────────────────────────
# Small helpers
# ─────────────────────────────────────────────────────────────────────────

def log_error(message: str) -> None:
    with ERROR_LOG.open("a", encoding="utf-8") as f:
        f.write(message + "\n")


def slug_from_url(url: str) -> str:
    path = urlparse(url).path.strip("/")
    segments = [s for s in path.split("/") if s]
    return segments[-1] if segments else "post"


def read_urls() -> list:
    if not URLS_FILE.exists():
        raise FileNotFoundError(f"{URLS_FILE} not found")
    urls = []
    for line in URLS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            urls.append(line)
    return urls


def yaml_safe(value: str) -> str:
    """Quote a frontmatter scalar only if it needs it (contains ':' or
    starts with a character that would confuse the flat parser build.py
    uses to read these files back)."""
    value = value.strip()
    if not value:
        return ""
    if ":" in value or value[0] in "\"'#[]{}" or value != value.strip():
        escaped = value.replace('"', '\\"')
        return f'"{escaped}"'
    return value


# ─────────────────────────────────────────────────────────────────────────
# Metadata extraction — regex over <head>. WordPress meta tags are simple,
# single-line, self-closing, so this is reliable without a full HTML parser.
# ─────────────────────────────────────────────────────────────────────────

def extract_meta(html_text: str, attr: str, key: str) -> str:
    pattern = re.compile(
        r'<meta[^>]+' + re.escape(attr) + r'=["\']' + re.escape(key) + r'["\'][^>]+content=["\']([^"\']*)["\']',
        re.IGNORECASE,
    )
    match = pattern.search(html_text)
    if not match:
        # some themes emit content= before the property/name attribute
        pattern2 = re.compile(
            r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+' + re.escape(attr) + r'=["\']' + re.escape(key) + r'["\']',
            re.IGNORECASE,
        )
        match = pattern2.search(html_text)
    return html.unescape(match.group(1)).strip() if match else ""


def extract_title_tag(html_text: str) -> str:
    match = re.search(r"<title[^>]*>(.*?)</title>", html_text, re.IGNORECASE | re.DOTALL)
    return html.unescape(match.group(1)).strip() if match else ""


def extract_h1(html_text: str) -> str:
    match = re.search(r"<h1[^>]*>(.*?)</h1>", html_text, re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    text = re.sub(r"<[^>]+>", " ", match.group(1))
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def extract_title(html_text: str) -> str:
    og_title = extract_meta(html_text, "property", "og:title")
    if og_title:
        return og_title
    title_tag = extract_title_tag(html_text)
    if title_tag:
        for sep in (" - ", " | ", " — "):
            if sep in title_tag:
                return title_tag.split(sep)[0].strip()
        return title_tag
    return extract_h1(html_text) or "Untitled Post"


def extract_date(html_text: str) -> str:
    published = extract_meta(html_text, "property", "article:published_time")
    if not published:
        match = re.search(r'<time[^>]+datetime=["\']([^"\']+)["\']', html_text, re.IGNORECASE)
        published = match.group(1) if match else ""
    return published[:10] if published else ""  # keep just YYYY-MM-DD


def extract_category(html_text: str) -> str:
    # The first /category/ link on the page is often from a nav mega-menu
    # or sidebar widget, not the post's own category tag — scope the
    # search to the theme's <div class="post-categories"> when present
    # (confirmed against a live post) so we get the post's real category,
    # not whatever category happens to be listed first in navigation.
    scope = html_text
    div_match = re.search(
        r'<div[^>]+class=["\'][^"\']*post-categories[^"\']*["\'][^>]*>(.*?)</div>',
        html_text, re.IGNORECASE | re.DOTALL,
    )
    if div_match:
        scope = div_match.group(1)

    match = re.search(
        r'<a[^>]+href=["\'][^"\']*/category/[^"\']*["\'][^>]*>(.*?)</a>',
        scope, re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return ""
    text = re.sub(r"<[^>]+>", " ", match.group(1))
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def extract_meta_description(html_text: str) -> str:
    return extract_meta(html_text, "name", "description") or extract_meta(html_text, "property", "og:description")


def extract_featured_image(html_text: str) -> str:
    og_image = extract_meta(html_text, "property", "og:image")
    if og_image:
        return og_image
    match = re.search(
        r'class=["\'][^"\']*(?:post-thumbnail|featured-image|wp-post-image)[^"\']*["\'][^>]*src=["\']([^"\']+)["\']',
        html_text, re.IGNORECASE,
    )
    if match:
        return match.group(1)
    match = re.search(
        r'src=["\']([^"\']+)["\'][^>]*class=["\'][^"\']*wp-post-image',
        html_text, re.IGNORECASE,
    )
    return match.group(1) if match else ""


def extract_entry_content_html(html_text: str) -> str:
    """Pull the raw HTML inside <div class="entry-content">...</div>,
    tracking div nesting depth so it stops at the correct closing tag
    (a plain non-greedy regex would stop at the first nested </div>)."""
    match = re.search(r'<div[^>]+class=["\'][^"\']*entry-content[^"\']*["\'][^>]*>', html_text, re.IGNORECASE)
    if not match:
        return ""
    start = match.end()
    depth = 1
    tag_re = re.compile(r"<(/?)div\b[^>]*>", re.IGNORECASE)
    for tm in tag_re.finditer(html_text, start):
        depth += -1 if tm.group(1) else 1
        if depth == 0:
            return html_text[start:tm.start()]
    return html_text[start:]


# ─────────────────────────────────────────────────────────────────────────
# Body HTML -> the markdown subset the site's build.py can render
# (H2/H3, paragraphs, bullet lists, bold, links).
# ─────────────────────────────────────────────────────────────────────────

class EntryContentToMarkdown(HTMLParser):
    # Tags with real closing tags whose entire subtree should be dropped
    # (WordPress uses these for images/captions/embeds/forms we can't
    # render, and for inline scripts/styles).
    SKIP_TAGS = {"script", "style", "figure", "figcaption", "iframe", "noscript", "form", "button"}
    RESET_ON_START = {"p", "h2", "h3", "h4", "h5", "h6", "li", "blockquote", "td", "th"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lines = []
        self.buf = []
        self.skip_depth = 0
        self.pending_href = ""
        self.table_rows = []
        self.current_row = []

    def _flush(self) -> str:
        text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        self.buf = []
        return text

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in self.RESET_ON_START:
            self.buf = []
        if tag in ("strong", "b"):
            self.buf.append("**")
        elif tag in ("em", "i"):
            self.buf.append("_")
        elif tag == "a":
            self.pending_href = dict(attrs).get("href", "")
            self.buf.append("[")
        elif tag == "br":
            self.buf.append(" ")
        elif tag == "tr":
            self.current_row = []
        elif tag == "table":
            self.table_rows = []

    def handle_startendtag(self, tag, attrs):
        # Self-closed void tags (e.g. <img />) — no-op, matches
        # handle_starttag's SKIP_TAGS guard doing nothing for "img".
        pass

    def handle_endtag(self, tag):
        if tag in self.SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if tag in ("strong", "b"):
            self.buf.append("**")
        elif tag in ("em", "i"):
            self.buf.append("_")
        elif tag == "a":
            text = self._flush()
            # rebuild "[text](href)" — _flush already stripped the
            # leading "[" marker along with everything else, so re-add it
            href = self.pending_href
            self.pending_href = ""
            rendered = f"[{text.lstrip('[')}]({href})" if href else text.lstrip("[")
            self.buf.append(rendered)
        elif tag in ("h2", "h3", "h4", "h5", "h6"):
            text = self._flush()
            if text:
                prefix = "##" if tag == "h2" else "###"
                self.lines.append(f"{prefix} {text}")
        elif tag in ("p", "blockquote"):
            text = self._flush()
            if text:
                self.lines.append(text)
        elif tag == "li":
            text = self._flush()
            if text:
                self.lines.append(f"- {text}")
        elif tag in ("td", "th"):
            self.current_row.append(self._flush())
        elif tag == "tr":
            if self.current_row:
                self.table_rows.append(self.current_row)
            self.current_row = []
        elif tag == "table":
            self._emit_table()
            self.table_rows = []

    def _emit_table(self):
        """Emit a real GitHub-style pipe table (build.py's markdown_to_html
        parses these back into an actual <table>) instead of flattening
        rows into bullets — WP posts use tables for genuine tabular data
        (comparisons, benchmarks) that reads poorly as a bullet list."""
        if len(self.table_rows) < 2:
            return
        header, body_rows = self.table_rows[0], self.table_rows[1:]
        ncols = len(header)

        def cell_text(value: str) -> str:
            # A literal "|" would be misread as a column boundary by
            # build.py's parser; real WP table cells are short phrases,
            # so swapping it for a dash is a safe, simple trade-off
            # rather than teaching both sides pipe-escaping.
            return (value or "").replace("|", "-").strip()

        def row_line(cells: list) -> str:
            padded = cells + [""] * (ncols - len(cells))
            return "| " + " | ".join(cell_text(c) for c in padded[:ncols]) + " |"

        table_lines = [row_line(header), "| " + " | ".join(["---"] * ncols) + " |"]
        table_lines += [row_line(row) for row in body_rows]
        self.lines.append("\n".join(table_lines))

    def handle_data(self, data):
        if not self.skip_depth:
            self.buf.append(data)

    def get_markdown(self) -> str:
        # Consecutive bullets join with a single newline so build.py's
        # markdown_to_html() sees one continuous <ul> — a blank line
        # between them would close the list after every single item.
        # Every other block boundary (heading/paragraph/list transitions)
        # still gets a full blank line.
        result = ""
        prev_was_bullet = False
        for line in self.lines:
            is_bullet = line.startswith("- ")
            if result:
                result += "\n" if (is_bullet and prev_was_bullet) else "\n\n"
            result += line
            prev_was_bullet = is_bullet
        return result


def body_html_to_markdown(entry_html: str) -> str:
    parser = EntryContentToMarkdown()
    parser.feed(entry_html)
    parser.close()
    return parser.get_markdown()


# ─────────────────────────────────────────────────────────────────────────
# Image handling
# ─────────────────────────────────────────────────────────────────────────

def save_featured_image(image_url: str, slug: str) -> tuple:
    """Returns (title_image_value, ok). On any failure, falls back to the
    remote URL itself as title_image and reports ok=False so the caller
    can log it."""
    if not image_url:
        return "", True

    filename = Path(urlparse(image_url).path).name
    if not filename:
        filename = f"{slug}.jpg"

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    dest = IMAGES_DIR / filename

    try:
        download_image(image_url, dest)
        return f"/assets/blog/{filename}", True
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
        log_error(f"IMAGE DOWNLOAD FAILED for {slug}: {image_url} — {exc}")
        return image_url, False


# ─────────────────────────────────────────────────────────────────────────
# Frontmatter + file output
# ─────────────────────────────────────────────────────────────────────────

def write_post_markdown(slug: str, title: str, date: str, category: str,
                         meta_description: str, title_image: str, body_md: str) -> Path:
    CONTENT_BLOG_DIR.mkdir(parents=True, exist_ok=True)
    frontmatter = (
        "---\n"
        f"title: {yaml_safe(title)}\n"
        "author: Billed Right\n"
        f"date: {date}\n"
        f"category: {yaml_safe(category)}\n"
        f"meta_description: {yaml_safe(meta_description)}\n"
        f"title_image: {title_image}\n"
        "---\n\n"
    )
    out_path = CONTENT_BLOG_DIR / f"{slug}.md"
    out_path.write_text(frontmatter + body_md.strip() + "\n", encoding="utf-8")
    return out_path


# ─────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────

def scrape_one(url: str) -> str:
    page_html = fetch_url(url)

    title = extract_title(page_html)
    date = extract_date(page_html)
    category = extract_category(page_html)
    meta_description = extract_meta_description(page_html)
    image_url = extract_featured_image(page_html)
    entry_html = extract_entry_content_html(page_html)

    if not entry_html:
        raise ValueError("could not find .entry-content on the page")

    body_md = body_html_to_markdown(entry_html)
    slug = slug_from_url(url)
    title_image, image_ok = save_featured_image(image_url, slug)

    write_post_markdown(slug, title, date, category, meta_description, title_image, body_md)

    if not image_ok:
        return f"{title}  (saved — image download failed, using remote URL fallback)"
    return title


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force", action="store_true",
        help="Re-scrape and overwrite posts already saved to content/blog/, "
             "instead of skipping them. Use this to pick up new markdown/build.py "
             "fixes on already-imported posts — but note it will discard any "
             "hand edits (e.g. an SEO rewrite) made to that post's .md file since.",
    )
    args = parser.parse_args()

    if ERROR_LOG.exists():
        ERROR_LOG.unlink()

    urls = read_urls()
    total = len(urls)
    print(f"Found {total} URL(s) in {URLS_FILE.name}\n")

    succeeded = 0
    skipped = 0
    failed = 0

    for i, url in enumerate(urls, start=1):
        print(f"[{i}/{total}] {url}")

        slug = slug_from_url(url)
        existing = CONTENT_BLOG_DIR / f"{slug}.md"
        if existing.exists() and not args.force:
            print(f"    -> SKIPPED: {existing.relative_to(ROOT)} already exists (use --force to re-scrape)")
            skipped += 1
            continue

        try:
            result = scrape_one(url)
            print(f"    -> OK: {result}")
            succeeded += 1
        except Exception as exc:
            print(f"    -> ERROR: {exc}")
            log_error(f"FAILED {url} — {exc}")
            failed += 1

        if i < total:
            time.sleep(REQUEST_DELAY_SECONDS)

    print(f"\nDone. {succeeded} succeeded, {skipped} skipped, {failed} failed.")
    if failed:
        print(f"See {ERROR_LOG.name} for details on failed URLs.")


if __name__ == "__main__":
    main()
