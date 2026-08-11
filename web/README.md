# web/

The build for the published handbook: both languages on one page with a
language switcher, generated from the Markdown sources.

Published at **https://lczerner.github.io/agents-handbook/**, served by GitHub
Pages from `master` / `docs/`. It goes live on push; there is no other publish
step.

## Files

| File | |
|---|---|
| `build.py` | The generator. Reads the six Markdown files, writes `../docs/index.html`. |
| `template.html` | The design: CSS, the language switcher, the page shell. |

The output is `docs/index.html`. **Never edit it by hand** — the next build
overwrites it.

## Rebuilding

From the repository root:

```bash
make setup      # once: create .venv, install requirements.txt, enable the hook
make build      # regenerate docs/index.html if any source changed
make rebuild    # regenerate unconditionally
make check      # exit 1 if docs/index.html is out of date
```

Run `make build` after changing any of `HANDBOOK.md`, `WALKTHROUGHS.md`,
`PROMPTS.md` or their `.cs.md` counterparts, then commit and push. `make build`
is dependency-driven, so it does nothing when everything is current.

If the page needs something the Markdown cannot express, change `template.html`
or `build.py` — never the output.

Without the Makefile, `python3 web/build.py` works too, provided
`markdown-it-py` is installed.

## The pre-commit hook

`make setup` (or `make hooks`) points `core.hooksPath` at `.githooks/`, so the
hook is versioned with the repo rather than living in one clone. It runs only
when a commit touches a source document, the template or the generator, and it
refuses the commit in two cases:

- the page is out of date, because a source changed without a rebuild
- the page was rebuilt but left unstaged, which would commit the sources alone

Both messages name the fix. `git commit --no-verify` bypasses it for one commit;
`git config --unset core.hooksPath` disables it entirely.

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
