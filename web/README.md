# web/

The published one-page handbook: both languages with a switcher, generated from
the Markdown sources.

Published at: https://claude.ai/code/artifact/d4440c12-5a6d-46d1-b421-2bc930337e6c
(private until shared from the page's share menu)

## Files

| File | |
|---|---|
| `build.py` | The generator. Reads the six Markdown files, writes `handbook.html`. |
| `template.html` | The design: CSS, the language switcher, the page shell. |
| `handbook.html` | **Generated. Never edit by hand** — the next build overwrites it. |

## Rebuilding

From the repository root:

```bash
make setup      # once: create .venv and install requirements.txt
make build      # regenerate handbook.html if any source changed
make rebuild    # regenerate unconditionally
make check      # exit 1 if handbook.html is out of date
```

Run `make build` after changing any of `HANDBOOK.md`, `WALKTHROUGHS.md`,
`PROMPTS.md` or their `.cs.md` counterparts, then republish to the URL above.
`make build` is dependency-driven, so it does nothing when everything is current.

Without the Makefile, `python3 web/build.py` works too, provided `markdown-it-py`
is installed.

## The pre-commit hook

`make setup` (or `make hooks`) points `core.hooksPath` at `.githooks/`, so the
hook is versioned with the repo rather than living in one clone. It runs only
when a commit touches a source document, the template or the generator, and it
refuses the commit in two cases:

- the page is out of date, because a source changed without a rebuild
- the page was rebuilt but left unstaged, which would commit the sources alone

Both messages name the fix. `git commit --no-verify` bypasses it for one commit;
`git config --unset core.hooksPath` disables it entirely.

If the page needs something the Markdown cannot express, change `template.html`
or `build.py` — never the output.

## How the generator maps Markdown to the design

- Each source file becomes a **part**; each `##` becomes a section. An
  `<a id="…"></a>` line above a heading supplies its id, so the anchors written
  in the Markdown keep working. Otherwise the id is slugified from the heading.
- A leading `1.`, `Walkthrough 2 —` or `Appendix A —` is split off the heading
  and set as the number badge beside the title.
- **Blockquotes are classified.** One opening with a heading or with bold text
  becomes a bordered aside titled by it. Any other blockquote is text meant to be
  typed to the agent, and gets the green "TYPE THIS" box. This is why prompts in
  the sources must not open in bold.
- Tables are wrapped so wide content scrolls in its own container rather than the
  page body.
- Sections carry a language-independent `data-sec` key, so switching language
  keeps the reader on the same section even though the two trees use different
  anchor ids.
- Czech ids are prefixed `cs-`, which is what keeps both trees on one page.

## Constraints worth knowing

- **HTML parsing is off** (`html: False`). Every angle bracket in the sources is a
  placeholder — `<slug>`, `<channel>`, `<what you need from a human>` — and
  CommonMark would treat them as tags and silently drop them.
- **Links that cannot resolve in a single page lose the link and keep the text.**
  `starter-kit/` renders as code-styled words. Links to a sibling document become
  in-page anchors.
- Self-contained by necessity: the artifact host blocks every external request,
  so no CDN fonts, scripts or images.

## Checking a build

```bash
python3 - <<'PY'
import re, collections
from pathlib import Path
h = Path('web/handbook.html').read_text(encoding='utf-8')
ids = re.findall(r'\sid="([^"]+)"', h)
print("dup ids :", [k for k,v in collections.Counter(ids).items() if v>1] or "none")
print("broken  :", [a for a in set(re.findall(r'href="#([^"]+)"',h)) if a not in ids] or "none")
print("unclosed:", [t for t in ("div","section","p","ul","ol","li","table","pre")
                    if len(re.findall(r'<%s\b'%t,h)) != len(re.findall(r'</%s>'%t,h))] or "none")
PY
```
