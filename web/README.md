# web/

The builds for the published handbook: a page with both languages on it and a
language switcher, and a PDF of each language. All of it from the same Markdown
sources.

Published at **https://lczerner.github.io/agents-handbook/**, served by GitHub
Pages from `master` / `docs/`. It goes live on push; there is no other publish
step. The PDFs sit in the same directory, so they are published the same way and
the page can link to them by filename.

## Files

| File | |
|---|---|
| `build.py` | The generator. Reads the six Markdown files, writes `../docs/index.html`. |
| `template.html` | The design: CSS, the language switcher, the page shell. |
| `pdf.py` | The PDF generator. Reuses `build.py`'s rendering, writes the two PDFs. |
| `print.css` | The printed design: page size, running heads, contents, outline. |

The outputs are `docs/index.html`, `docs/working-with-ai-agents.pdf` and
`docs/prace-s-ai-agenty.pdf`. **Never edit them by hand** — the next build
overwrites them.

## Rebuilding

From the repository root:

```bash
make setup      # once: create .venv, install requirements.txt, enable the hook
make build      # regenerate docs/index.html if any source changed
make rebuild    # regenerate the page unconditionally
make pdf        # regenerate both PDFs
make check      # exit 1 if docs/index.html is out of date; report on the PDFs
```

Run `make build` after changing any of `HANDBOOK.md`, `WALKTHROUGHS.md`,
`PROMPTS.md` or their `.cs.md` counterparts, then commit and push. `make build`
is dependency-driven, so it does nothing when everything is current.

**`make pdf` is deliberately separate.** A new PDF is a republication — someone
has that file open, or has printed it — so it is not a side effect of editing a
paragraph. Run it when you want a new edition. Nothing enforces it: `make check`
says when the PDFs have fallen behind the sources and the pre-commit hook
mentions it, but neither refuses.

If the page needs something the Markdown cannot express, change `template.html`
or `build.py` — never the output. The same goes for `print.css` and `pdf.py`.

## The version

`VERSION` in `build.py` is the only place the kit's version is written. The
build sets it beside the eyebrow in the masthead, which puts it at the top of
the page and on both PDF covers. `../README.md` and `../README.cs.md` repeat it
in prose, and `build.py` compares them against the constant and exits rather
than build a page that disagrees with the READMEs.

Bumping it is a decision, not a step in an edit: see `Versioning` in
`../AGENTS.md`. To bump, change `VERSION` and both README lines, then
`make build`.

Without the Makefile, `python3 web/build.py` and `python3 web/pdf.py` work too,
provided the requirements are installed.

## The PDF editions

One file per language, holding the same three documents in the same order as the
page: `working-with-ai-agents.pdf` and `prace-s-ai-agenty.pdf`, named after each
document's own title. The reader gets a cover, a table of contents with page
numbers, running heads, and an outline in the PDF viewer's sidebar.

`pdf.py` imports `build.py` and calls the same `build_lang()` the page is made
from, so the two editions cannot drift: same sections, same prompts, same ids.
Only the shell around them differs, and that is all `print.css` describes.

Three things about it are worth knowing:

- **It is byte-reproducible, and has to be**, or `--check` could not compare
  anything. Every font is embedded as a subset, and fontTools stamps each subset
  with the time it was cut, so `pdf.py` pins `SOURCE_DATE_EPOCH` before it
  renders. Same Markdown, same bytes.
- **The fonts come from the machine that builds it.** Charter and the mono face
  are resolved by fontconfig and embedded. A machine without them produces a
  readable PDF that differs in bytes and in line breaks.
- **Links stay links but nothing prints a URL.** Internal references and external
  links are clickable; on paper an external link is just underlined words. The
  handbook has too many of them for footnoted addresses to be readable.

It needs `weasyprint`, which needs pango — `brew install pango` on macOS. That
is the only dependency in this repo that is not pure Python.

## The pre-commit hook

`make setup` (or `make hooks`) points `core.hooksPath` at `.githooks/`, so the
hook is versioned with the repo rather than living in one clone. It runs only
when a commit touches a source document, a template or a generator, and it
refuses the commit in two cases:

- the page is out of date, because a source changed without a rebuild
- the page was rebuilt but left unstaged, which would commit the sources alone

Both messages name the fix. It also says when the PDFs are older than the
sources, but that one is a note and the commit goes through. `git commit
--no-verify` bypasses the hook for one commit; `git config --unset
core.hooksPath` disables it entirely.

## How the generator maps Markdown to the design

- Each source file becomes a **part**; each `##` becomes a section. An
  `<a id="…"></a>` line above a heading supplies its id, so the anchors written
  in the Markdown keep working. Otherwise the id is slugified from the heading.
- A leading `1.`, `Walkthrough 2 —` or `Appendix A —` is split off the heading
  and set as the number badge beside the title. The space between the badge and
  the title is deliberate: the page lays the heading out as a grid, where
  whitespace between items is not rendered, and the PDF reads the same heading
  as plain text for its outline and running head, where it is.
- **Blockquotes are classified.** One opening with a heading or with bold text
  becomes a bordered aside titled by it. Any other blockquote is text meant to be
  typed to the agent, and gets the green "TYPE THIS" box. This is why prompts in
  the sources must not open in bold.
- **Copy buttons follow that classification.** Every "TYPE THIS" box gets one;
  asides don't. A fenced code block gets one only if the fence is tagged —
  ` ```bash ` and ` ```markdown ` are commands and file contents people paste,
  an untagged fence is a directory tree or a sample of the agent's output. To
  give a block a button, tag its fence; to take one away, untag it.
  What gets copied is the Markdown as written, backticks and line breaks
  included, carried into a `data-copy` attribute — not the text the browser
  shows. The buttons themselves are added by the page's own script, so a reader
  without JavaScript never sees a control that cannot work.
- Tables are wrapped so wide content scrolls in its own container rather than the
  page body.
- Sections carry a language-independent `data-sec` key, so switching language
  keeps the reader on the same section even though the two trees use different
  anchor ids.
- Czech ids are prefixed `cs-`, which is what keeps both trees on one page.
- The document skeleton — doctype, `charset`, `viewport`, `color-scheme`,
  `description` — is added around the rendered page. The head/body split keys off
  the `<!--HEAD-END-->` marker in `template.html`, so editing the template cannot
  silently move it.

## Constraints worth knowing

- **HTML parsing is off** (`html: False`). Every angle bracket in the sources is a
  placeholder — `<slug>`, `<channel>`, `<what you need from a human>` — and
  CommonMark would treat them as tags and silently drop them.
- **Links that cannot resolve in a single page lose the link and keep the text.**
  `starter-kit/` renders as code-styled words. Links to a sibling document become
  in-page anchors.
- **Self-contained.** No external requests: no CDN fonts, scripts or images, so
  the page works offline and has nothing that can break from the outside.
- **The PDF has no scrollbars to fall back on.** Long lines in a code block wrap
  instead, tables are set to the measure rather than to a scrolling container,
  and the copy buttons do not exist — they are added by a script the PDF never
  runs.

## Checking a build

```bash
python3 - <<'PY'
import re, collections
from pathlib import Path
h = Path('docs/index.html').read_text(encoding='utf-8')
ids = re.findall(r'\sid="([^"]+)"', h)
print("dup ids :", [k for k,v in collections.Counter(ids).items() if v>1] or "none")
print("broken  :", [a for a in set(re.findall(r'href="#([^"]+)"',h)) if a not in ids] or "none")
print("unclosed:", [t for t in ("div","section","p","ul","ol","li","table","pre")
                    if len(re.findall(r'<%s\b'%t,h)) != len(re.findall(r'</%s>'%t,h))] or "none")
PY
```

The same three checks run against what goes into the PDFs, which is a different
document — one language, no navigation column:

```bash
.venv/bin/python - <<'PY'
import re, sys, collections
sys.path.insert(0, "web")
import pdf
for lang in ("en", "cs"):
    doc = pdf.document(lang)
    ids = re.findall(r'\sid="([^"]+)"', doc)
    hrefs = set(re.findall(r'href="#([^"]+)"', doc))
    print(lang,
          "| dup:", [k for k,v in collections.Counter(ids).items() if v>1] or "none",
          "| broken:", sorted(h for h in hrefs if h not in ids) or "none")
PY
```

And after a build, that the two files still look like two handbooks — a cover,
a contents page, then the parts:

```bash
.venv/bin/python -c "
from weasyprint import HTML, CSS
import sys; sys.path.insert(0, 'web'); import pdf
for lang in ('en','cs'):
    d = HTML(string=pdf.document(lang), base_url='.').render(
        stylesheets=[CSS(filename='web/print.css')])
    print(lang, len(d.pages), 'pages')"
```
