#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright 2026, Lukáš Czerner <lukas@czerner.cz>
# SPDX-License-Identifier: MIT
"""Generate the PDF editions of the handbook from the Markdown sources.

The Markdown files are the source of truth, and web/build.py already turns them
into the HTML the site serves. This script reuses that same rendering — same
sections, same prompts, same anchors — and puts it in a printed shell instead:
a cover, a table of contents with page numbers, running heads, and an outline.
One PDF per language, written next to the page in docs/ so GitHub Pages serves
them alongside it.

Unlike the page, the PDFs are not rebuilt by `make build`. Run `make pdf` when
you want to publish a new edition; `make check` says when they have fallen
behind.

Usage:
    python3 web/pdf.py            # write both PDFs
    python3 web/pdf.py --check    # exit 1 if either is out of date

Requires weasyprint (`pip install -r requirements.txt`), which in turn needs
pango — `brew install pango` on macOS.
"""

from __future__ import annotations

import html
import os
import re
import sys

# Every font in a PDF is embedded as a subset, and fontTools stamps each subset
# with the moment it was cut. Left alone, two builds of the same Markdown differ
# in bytes for a reason no reader could ever see, and --check could not compare
# them. fontTools reads SOURCE_DATE_EPOCH — the reproducible-builds convention —
# so pin it to a fixed date, while still honouring one set from outside.
os.environ.setdefault("SOURCE_DATE_EPOCH", "1735689600")  # 2025-01-01T00:00:00Z

from weasyprint import CSS, HTML

import build

ROOT = build.ROOT
STYLE = ROOT / "web" / "print.css"

OUTPUT = {
    "en": ROOT / "docs" / "working-with-ai-agents.pdf",
    "cs": ROOT / "docs" / "prace-s-ai-agenty.pdf",
}

AUTHOR = "Lukáš Czerner"
SITE = "https://lczerner.github.io/agents-handbook/"

WORDS = {
    "en": {
        "contents": "Contents",
        "online": "The current version is always at",
        "license": "CC BY 4.0 - credit the author and keep the license.",
    },
    "cs": {
        "contents": "Obsah",
        "online": "Aktuální verze je vždy na",
        "license": "CC BY 4.0 - uveďte autora a zachovejte licenci.",
    },
}

# Each handbook opens with its own list of sections, which is how you navigate
# a Markdown file or the page. The PDF has a real table of contents with page
# numbers, so listing that list in it would be listing a contents page twice.
# The section itself stays where it is, links and all.
SKIP_IN_CONTENTS = {"contents", "cs-obsah"}

# The page is one document holding both languages, so its Czech ids carry a
# `cs-` prefix. A PDF is one language, but the ids come from the same builder
# and the links inside the text point at the prefixed ones, so they stay.
PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{title}</title>
<meta name="author" content="{author}">
<meta name="description" content="{description}">
</head>
<body>
{cover}
{contents}
<main>
{body}
</main>
</body>
</html>
"""

MASTHEAD = re.compile(r'^\s*(<header class="masthead">.*?</header>)\s*', re.S)


def cover(lang: str, masthead: str) -> str:
    """The masthead, set as a title page with the address of the live site.

    A PDF is the copy that travels furthest from the repository, so the terms
    it is under are printed on it rather than left in a file nobody downloaded.
    """
    return (
        f'<div class="cover">\n{masthead}\n'
        f'<p class="colophon">{html.escape(AUTHOR)}<br>'
        f'{WORDS[lang]["online"]} <a href="{SITE}">{SITE}</a><br>'
        f"{html.escape(build.COPYRIGHT)}<br>"
        f'{WORDS[lang]["license"]}</p>\n</div>'
    )


def contents(lang: str, toc: list[tuple[str, str, str, str]]) -> str:
    """The same rows the site's navigation is built from, with page numbers.

    The numbers themselves come from print.css: `target-counter()` resolves each
    link to the page its section landed on, which is only known once the whole
    document has been laid out.
    """
    groups: dict[str, list[str]] = {}
    for group, ident, num, title in toc:
        if ident in SKIP_IN_CONTENTS:
            continue
        groups.setdefault(group, []).append(
            f'<li><a href="#{ident}"><b>{html.escape(num or "·")}</b>'
            f"<span>{title}</span></a></li>"
        )
    blocks = [
        f"<h2>{html.escape(group)}</h2>\n<ol>\n" + "\n".join(items) + "\n</ol>"
        for group, items in groups.items()
        if items
    ]
    return (
        f'<nav class="toc">\n<h1>{WORDS[lang]["contents"]}</h1>\n'
        + "\n".join(blocks)
        + "\n</nav>"
    )


def document(lang: str) -> str:
    content, _nav, toc = build.build_lang(lang)

    m = MASTHEAD.match(content)
    if not m:
        raise SystemExit("web/build.py no longer opens the content with the masthead")
    body = content[m.end():]

    title = re.sub(r"<[^>]+>", "", re.search(r"<h1>(.*?)</h1>", m.group(1), re.S).group(1))

    return PAGE.format(
        lang=lang,
        title=html.escape(title, quote=True),
        author=html.escape(AUTHOR, quote=True),
        description=html.escape(build.DESCRIPTION, quote=True),
        cover=cover(lang, m.group(1)),
        contents=contents(lang, toc),
        body=body,
    )


def render(lang: str) -> tuple[bytes, int]:
    doc = HTML(string=document(lang), base_url=str(ROOT)).render(
        stylesheets=[CSS(filename=str(STYLE))]
    )
    return doc.write_pdf(), len(doc.pages)


def main() -> int:
    checking = "--check" in sys.argv
    stale = False

    for lang, target in OUTPUT.items():
        data, pages = render(lang)
        name = target.relative_to(ROOT)

        if checking:
            current = target.read_bytes() if target.exists() else b""
            if current != data:
                print(f"{name} is out of date; run make pdf")
                stale = True
            else:
                print(f"{name} is up to date")
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        print(f"wrote {name} ({pages} pages, {len(data) // 1024} KB)")

    return 1 if stale else 0


if __name__ == "__main__":
    raise SystemExit(main())
