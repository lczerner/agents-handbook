#!/usr/bin/env python3
"""Generate the web version of the handbook from the Markdown sources.

The Markdown files are the source of truth. This script renders them into the
design in web/template.html and writes docs/index.html, the page GitHub Pages
serves. It is never edited by hand.

Usage:
    python3 web/build.py            # write docs/index.html
    python3 web/build.py --check    # exit 1 if it is out of date

Requires markdown-it-py (`pip install markdown-it-py`).
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "web" / "template.html"
OUTPUT = ROOT / "docs" / "index.html"

DESCRIPTION = (
    "How to use AI agents such as Claude Code, Codex, opencode and pi for "
    "writing, planning and campaign work. A handbook for people who don't "
    "write code, in English and Czech."
)

# Without the viewport meta a phone renders the desktop layout zoomed out;
# without the charset the page depends on the server sending one.
STANDALONE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="description" content="{description}">
{head}
</head>
<body>
{body}
</body>
</html>
"""

# Each language is built from three documents, in this order. The `key` is
# language independent and is what pairs an English section with its Czech
# counterpart when the reader switches language.
DOCS = {
    "en": [
        ("handbook", "HANDBOOK.md", "Part one — Concepts"),
        ("walkthroughs", "WALKTHROUGHS.md", "Part two — Walkthroughs"),
        ("prompts", "PROMPTS.md", "Part three — Prompt sheet"),
    ],
    "cs": [
        ("handbook", "HANDBOOK.cs.md", "Část první — Koncepty"),
        ("walkthroughs", "WALKTHROUGHS.cs.md", "Část druhá — Walkthroughs"),
        ("prompts", "PROMPTS.cs.md", "Část třetí — Tahák s prompty"),
    ],
}

NAV_GROUPS = {
    "en": {"handbook": "Concepts", "walkthroughs": "Walkthroughs", "prompts": "Reference"},
    "cs": {"handbook": "Koncepty", "walkthroughs": "Walkthroughs", "prompts": "Reference"},
}

NAV_LABEL = {"en": "Contents", "cs": "Obsah"}

# Relative links cannot resolve inside a single page. Links to a sibling
# document become in-page anchors; everything else loses its link and keeps
# its text.
DOC_LINKS = {
    "HANDBOOK.md": "handbook", "HANDBOOK.cs.md": "handbook",
    "WALKTHROUGHS.md": "walkthroughs", "WALKTHROUGHS.cs.md": "walkthroughs",
    "PROMPTS.md": "prompts", "PROMPTS.cs.md": "prompts",
}

# html=False matters: every angle bracket in the sources is a placeholder —
# <slug>, <channel>, <what you need from a human> — and CommonMark would treat
# them as raw HTML tags and drop them from the page. Escaped, they show as
# written. The `<a id="...">` anchors are consumed before rendering.
md = MarkdownIt("commonmark", {"html": False}).enable("table").enable("strikethrough")

# Fences whose contents people are meant to copy: terminal commands, and file
# contents that go into their own files. An untagged fence is a directory tree
# or a sample of the agent's output, and gets no copy button.
COPY_FENCES = ("bash", "markdown")


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_]+", "-", text).strip("-") or "section"


def split_number(title: str) -> tuple[str, str]:
    """Pull a leading marker out of a heading so it can be set apart visually.

    "4. AGENTS.md — the house rules"  -> ("04", "AGENTS.md — the house rules")
    "Walkthrough 2 — Write an article" -> ("W2", "Write an article")
    "Appendix A — Which file..."       -> ("A",  "Which file...")
    """
    m = re.match(r"^(\d+)\.\s+(.*)$", title)
    if m:
        return m.group(1).zfill(2), m.group(2)
    m = re.match(r"^Walkthrough\s+(\d+)\s*[—-]\s*(.*)$", title, re.I)
    if m:
        return "W" + m.group(1), m.group(2)
    m = re.match(r"^(?:Appendix|Příloha)\s+([AB])\s*[—-]+\s*(.*)$", title, re.I)
    if m:
        return m.group(1).upper(), m.group(2)
    return "", title


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def split_sections(text: str) -> list[tuple[str | None, str, str]]:
    """Split a document on `## ` headings.

    Returns (heading or None for the preamble, explicit anchor id or "", body).
    An `<a id="x"></a>` line immediately above a heading supplies its id, which
    keeps the anchors already used in the Markdown files working.
    """
    lines = text.split("\n")
    out: list[tuple[str | None, str, str]] = []
    heading: str | None = None
    anchor = ""
    pending = ""
    buf: list[str] = []
    fence = False

    for line in lines:
        if line.lstrip().startswith("```"):
            fence = not fence
        m = re.match(r'^<a id="([^"]+)"></a>\s*$', line)
        if m and not fence:
            pending = m.group(1)
            continue
        if not fence and line.startswith("## "):
            out.append((heading, anchor, "\n".join(buf)))
            heading = line[3:].strip()
            anchor, pending = pending, ""
            buf = []
            continue
        buf.append(line)
    out.append((heading, anchor, "\n".join(buf)))
    return out


def raw_blockquotes(body: str) -> list[str]:
    """The Markdown source of every blockquote, in document order.

    Blockquotes are classified after rendering, by which point the source is
    gone — but the copy button has to hand back what was written, backticks and
    line breaks included, not what the browser happens to show. The sources use
    no lazy continuation, so a blockquote is exactly a run of `>` lines.
    """
    out: list[str] = []
    buf: list[str] = []
    fence = False

    for line in body.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence and line.startswith(">"):
            buf.append(re.sub(r"^>[ \t]?", "", line))
            continue
        if buf:
            out.append("\n".join(buf).strip())
            buf = []
    if buf:
        out.append("\n".join(buf).strip())
    return out


def copy_attr(text: str) -> str:
    """A data-copy attribute carrying `text` verbatim for the clipboard.

    Newlines become `&#10;` so one prompt stays one line of generated HTML;
    the browser turns them back into newlines when it reads the attribute.
    """
    return ' data-copy="' + html.escape(text, quote=True).replace("\n", "&#10;") + '"'


def mark_code(out: str) -> str:
    """Give the copyable fences their clipboard text; leave the rest alone."""

    def code(m: re.Match) -> str:
        lang, body = m.group(1), m.group(2)
        if lang not in COPY_FENCES:
            return m.group(0)
        # A trailing newline would run a pasted command before it was read.
        attr = copy_attr(html.unescape(body).rstrip("\n"))
        return f'<pre{attr}><code class="language-{lang}">{body}</code></pre>'

    return re.sub(r'<pre><code class="language-([\w-]+)">(.*?)</code></pre>',
                  code, out, flags=re.S)


def render_body(body: str, lang: str) -> str:
    """Markdown to HTML, then the presentational conventions of this design."""
    quotes = raw_blockquotes(body)
    used = 0
    out = md.render(body)

    # Headings shift down one level: `##` is a section title (h3), so the
    # `###`/`####` beneath it become h4/h5.
    for src, dst in ((4, 5), (3, 4)):
        out = out.replace(f"<h{src}>", f"<h{dst}>").replace(f"</h{src}>", f"</h{dst}>")

    # A blockquote opening in bold is an aside; anything else is text meant to
    # be typed to the agent, and gets the "TYPE THIS" treatment.
    def blockquote(m: re.Match) -> str:
        nonlocal used
        raw = quotes[used] if used < len(quotes) else ""
        used += 1
        inner = m.group(1).strip()
        # A quote that opens with a heading is an aside titled by that heading.
        head = re.match(r"<h\d>(.*?)</h\d>(.*)$", inner, re.S)
        if head:
            return f'<div class="block">\n<h5>{head.group(1)}</h5>\n{head.group(2).strip()}\n</div>'
        # A quote that opens in bold is an aside titled by the bold run.
        lead = re.match(r"<p><strong>(.*?)</strong>[.:]?\s*(.*?)</p>(.*)$", inner, re.S)
        if lead:
            rest = (f"<p>{lead.group(2)}</p>" if lead.group(2).strip() else "") + lead.group(3)
            return f'<div class="block">\n<h5>{lead.group(1)}</h5>\n{rest.strip()}\n</div>'
        # Anything else is text meant to be typed to the agent, and carries the
        # source of the prompt so the page can offer it to the clipboard.
        return f'<div class="say"{copy_attr(raw)}>\n{inner}\n</div>'

    out = re.sub(r"<blockquote>(.*?)</blockquote>", blockquote, out, flags=re.S)
    # The pairing above is positional. If the two counts ever drift — a nested
    # blockquote, a change of parser — every prompt after that point would copy
    # the wrong text, so stop rather than publish it.
    if used != len(quotes):
        raise SystemExit(
            f"blockquote mismatch: {used} rendered, {len(quotes)} in the source"
        )

    out = mark_code(out)

    # Wide content scrolls inside its own container rather than the page body.
    out = re.sub(r"<table>.*?</table>", lambda m: f'<div class="scroll">{m.group(0)}</div>',
                 out, flags=re.S)

    out = fix_links(out, lang)
    return out.strip()


def fix_links(out: str, lang: str) -> str:
    prefix = "cs-" if lang == "cs" else ""

    def link(m: re.Match) -> str:
        href = m.group(1)
        if href.startswith(("http://", "https://", "mailto:")):
            return m.group(0)
        # markdown-it percent-encodes non-ASCII targets; the ids are raw UTF-8,
        # so "#1-jedna-my%C5%A1lenka" has to come back to "#1-jedna-myšlenka".
        href = unquote(href)
        if href.startswith("#"):
            return f'<a href="#{prefix}{href[1:]}">'
        base, _, frag = href.partition("#")
        if base in DOC_LINKS:
            target = f"{prefix}{frag}" if frag else f"{prefix}{DOC_LINKS[base]}"
            return f'<a href="#{target}">'
        return "<!--UNLINK-->"

    out = re.sub(r'<a href="([^"]+)">', link, out)
    # Relative paths (starter-kit/, images) cannot resolve in a single page:
    # keep the words, drop the link.
    out = re.sub(r"<!--UNLINK-->(.*?)</a>", r"<code>\1</code>", out, flags=re.S)
    return out


def build_lang(lang: str) -> tuple[str, str]:
    prefix = "cs-" if lang == "cs" else ""
    content: list[str] = []
    nav: dict[str, list[str]] = {}
    seen: set[str] = set()
    masthead_done = False

    for key, filename, part_title in DOCS[lang]:
        source = strip_comments((ROOT / filename).read_text(encoding="utf-8"))
        part_id = prefix + key
        seen.add(part_id)
        content.append(f'<h2 class="part" id="{part_id}">{html.escape(part_title)}</h2>')
        nav.setdefault(NAV_GROUPS[lang][key], [])

        for index, (heading, anchor, body) in enumerate(split_sections(source)):
            if heading is None:
                # Text above the first `##`: the document title and its intro.
                title_m = re.search(r"^#\s+(.*)$", body, re.M)
                sub_m = re.search(r"^###\s+(.*)$", body, re.M)
                intro = re.sub(r"^#\s+.*$|^###\s+.*$", "", body, flags=re.M)
                if not masthead_done:
                    content.insert(0, masthead(lang, title_m, sub_m))
                    masthead_done = True
                rendered = render_body(intro, lang)
                if rendered:
                    content.append(f"<section>\n{rendered}\n</section>")
                continue

            sec = f"{key}-{index}"
            ident = prefix + (anchor or slugify(heading))
            while ident in seen:
                ident += "-x"
            seen.add(ident)

            num, title = split_number(heading)
            num_html = f'<span class="num">{html.escape(num)}</span>' if num else ""
            content.append(
                f'<section id="{ident}" data-sec="{sec}">\n'
                f"<h3>{num_html}<span>{inline(title)}</span></h3>\n"
                f"{render_body(body, lang)}\n</section>"
            )
            nav[NAV_GROUPS[lang][key]].append(
                f'<li><a href="#{ident}"><b>{html.escape(num or "·")}</b>'
                f"<span>{inline(title)}</span></a></li>"
            )

    return "\n\n".join(content), render_nav(lang, nav)


def inline(text: str) -> str:
    """Render inline Markdown (code spans, emphasis) without a wrapping <p>."""
    return md.renderInline(text)


def masthead(lang: str, title_m: re.Match | None, sub_m: re.Match | None) -> str:
    eyebrow = "Team handbook" if lang == "en" else "Týmová příručka"
    title = inline(title_m.group(1)) if title_m else "Handbook"
    sub = inline(sub_m.group(1)) if sub_m else ""
    return (
        f'<header class="masthead">\n<p class="eyebrow">{eyebrow}</p>\n'
        f"<h1>{title}</h1>\n<p>{sub}</p>\n</header>"
    )


def render_nav(lang: str, groups: dict[str, list[str]]) -> str:
    blocks = []
    for group, items in groups.items():
        if items:
            blocks.append(f"<h2>{html.escape(group)}</h2>\n<ol>\n" + "\n".join(items) + "\n</ol>")
    inner = "\n".join(blocks)
    flat = "\n".join(i for items in groups.values() for i in items)
    return (
        f'<div class="navcol doc" data-lang="{lang}">\n\n'
        f'<details class="nav-mobile">\n<summary>{NAV_LABEL[lang]}</summary>\n'
        f'<nav class="nav" style="margin-top:1rem">\n<ol>\n{flat}\n</ol>\n</nav>\n</details>\n\n'
        f'<nav class="nav nav-desktop" aria-label="{NAV_LABEL[lang]}">\n{inner}\n</nav>\n\n'
        f"</div>"
    )


def build() -> str:
    template = TEMPLATE.read_text(encoding="utf-8")
    navs, docs = [], []
    for lang in ("en", "cs"):
        content, nav = build_lang(lang)
        navs.append(nav)
        docs.append(
            f'<div class="doc" data-lang="{lang}"'
            + (' lang="cs"' if lang == "cs" else "")
            + f">\n\n{content}\n\n</div><!-- /doc {lang} -->"
        )
    page = template.replace("<!--NAV-->", "\n\n".join(navs))
    page = page.replace("<!--CONTENT-->", "\n\n".join(docs))
    return page


def standalone(rendered: str) -> str:
    """Wrap the rendered page in a complete HTML document.

    The split is on the <!--HEAD-END--> marker in the template rather than on
    the shape of the output, so changing the template cannot silently move it.
    """
    head, marker, body = rendered.partition("<!--HEAD-END-->")
    if not marker:
        raise SystemExit("web/template.html is missing the <!--HEAD-END--> marker")
    return STANDALONE.format(
        description=html.escape(DESCRIPTION, quote=True),
        head=head.strip(),
        body=body.strip(),
    )


def main() -> int:
    text = standalone(build())
    name = OUTPUT.relative_to(ROOT)

    if "--check" in sys.argv:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != text:
            print(f"{name} is out of date; run make build")
            return 1
        print(f"{name} is up to date")
        return 0

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    print(f"wrote {name} ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
