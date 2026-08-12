# AGENTS.md

<!-- Rules for any agent working in this repo. Keep under ~200 lines.
     The second time the same correction is needed, it goes in here.
     Claude Code reads CLAUDE.md, which imports this file. -->


## What this is

A training kit that teaches non-technical people how to use AI agents — Claude
Code, OpenAI Codex CLI, opencode, pi — for writing, planning and campaign work.
It ships in English and Czech, with four hands-on walkthroughs and a starter
workspace people copy.

This is a living document. Lukáš keeps editing it, adds walkthroughs specific to
what his colleagues actually do, and corrects the Czech.

You help write, translate, restructure and fact-check. You do not publish it and
you do not commit it.

## Who reads it

Non-technical colleagues. They will follow the walkthroughs, copy the starter
kit, and otherwise never open a terminal. Assume no prior knowledge of Git,
Markdown, the terminal, or how models work, and define every term in plain
language on first use.

They read it and refer back to it. Lukáš is the only person who edits the repo.

## Where things live

- `AGENTS.md` — this file. `CLAUDE.md` is one line importing it, so every tool
  reads the same rules. Edit this one, never the import.
- `README.md` / `README.cs.md` — orientation and first-week checklist
- `HANDBOOK.md` / `HANDBOOK.cs.md` — the concepts, twelve sections. The main document.
- `WALKTHROUGHS.md` / `WALKTHROUGHS.cs.md` — four exercises
- `PROMPTS.md` / `PROMPTS.cs.md` — prompt cheat sheet. The prompts themselves stay
  English in both: they are copy-paste material. Only labels and commentary are translated.
- `starter-kit/` — a complete example workspace for a fictional company,
  Lighthouse. People copy it and replace the content.
- `web/build.py` — the generator. `web/template.html` holds the design.
- `web/pdf.py` — the PDF generator. It reuses `build.py`'s rendering and puts it
  in a printed shell; `web/print.css` holds that design.
- `docs/index.html` — **generated. Never edit it by hand.** The published site,
  https://lczerner.github.io/agents-handbook/, served from `master` / `/docs`.
  It goes live on push; there is no separate publish step.
- `docs/working-with-ai-agents.pdf` / `docs/prace-s-ai-agenty.pdf` — **generated.**
  The same three documents as the page, one PDF per language, published from the
  same directory and linked from the page.
- `notes` — Lukáš's, untracked. Do not read, edit or commit it.

**The Markdown files are the source of truth.** After changing any of the six
source documents, regenerate:

```bash
make setup    # once: create .venv, install dependencies, enable the git hook
make build    # regenerate docs/index.html
make check    # fail if it is out of date, and say if the PDFs are behind
make pdf      # regenerate the two PDFs — a republication, so only when asked
```

The page is rebuilt with every change; the PDFs are not. Run `make pdf` when
Lukáš asks for a new edition, not because a paragraph moved.

A pre-commit hook in `.githooks/` blocks a commit that changes a source document
without staging the rebuilt page. If it fires, run `make build` and stage
`docs/index.html` — don't reach for `--no-verify`. The same hook mentions PDFs
that have fallen behind, but never blocks on them.

Any hand edit to the generated file is destroyed by the next build. If the page
needs something the Markdown cannot express, change `web/template.html` or the
generator, not the output.

## Versioning

The kit carries a version so a reader can tell which edition they have. It is
written in exactly one place: `VERSION` in `web/build.py`. From there it reaches
the masthead of the page and the cover of both PDFs. The two READMEs state the
same number in prose — `**Version 0.1.2**` and `**Verze 0.1.2**` — and
`web/build.py` refuses to build if they disagree with the constant, so a bump
that misses one stops instead of publishing two answers.

What a bump means:

- **patch** (0.1.2 → 0.1.3) — corrections, wording, a paragraph, a fixed link
- **minor** (0.1.2 → 0.2.0) — a new section, a new walkthrough, a new feature of
  the page or the build
- **major** — a restructuring that invalidates what people already learnt.
  Unused so far

**The version is bumped before a push, and never by you.** Pushing publishes, so
the number people see should already match what they are about to read. Before
any push, say: what the current version is, what has changed since it, and which
bump you would suggest. Then stop. Whether it is time for a new version, and
which number it gets, is Lukáš's decision — a reminder is your part of it.

Bumping means all four in one commit: `VERSION`, both READMEs, and a rebuilt
`docs/index.html`. The PDFs are still republished only when he asks.

## Guardrails

### Never

- Never restore something Lukáš deleted. He cut the pronouns passage in §6.3, the
  closing "on what this changes about the work" paragraphs, and "Go home."
  Deletions are decisions, not omissions.
- Never commit. He commits, or asks you to.
- Never push. Pushing publishes: the repo is public and the site rebuilds.
- Never open, edit or commit `notes`.
- Never silently correct his wording. If something reads like a typo, say so and
  let him decide.
- Never state that a tool does something without checking its current
  documentation. **WebOps' MCP server and author database do not exist yet** —
  nothing may imply they do.
- Never add motivational or summarising closers. He has cut two already.
- Never translate Czech word-for-word. See below.
- Never bump the version on your own initiative. Remind him it is due, propose a
  number, and leave it to him.

### Always

- Always make the change in Markdown first.
- Always match the surrounding prose: short paragraphs, concrete examples in
  place of abstraction.
- Always write English prose in Lukáš's voice, which is described in his separate
  style project and comes down to: a spaced hyphen ` - ` and never an em dash,
  American spelling with `behaviour` as the one exception, long and short
  sentences alternating, no semicolons in long-form, and nothing oversold —
  least of all the kit itself. Example files inside fenced blocks are a
  different thing: they belong to the fictional company, not to him.
- Always write **directory**, never *folder*. In Czech **adresář**, never
  *složka*. This applies to prose, prompts and code comments alike.
- Always keep the fictional Lighthouse company in `starter-kit/` and the examples.
- Always check that in-page anchors and cross-file links still resolve after
  restructuring.

### Ask first

- Before committing or pushing.
- Before every push, whether the version should be bumped first. Ask, propose,
  wait — see [Versioning](#versioning).
- Before cutting or restructuring a whole section.
- Before adding a new top-level file.
- Before changing anything in `starter-kit/`. It is a worked example people copy,
  not a document.

## Writing Czech

The Czech versions exist so colleagues grasp the concepts faster. English is
authoritative. Lukáš corrects the Czech; your job is to leave him less to correct.

**Keep in English:** file and directory names, technical terms (agent, skill,
context window, MCP, session, prompt, workspace), every prompt, and every code
block. Prompts get pasted into agents, and agents follow English more reliably.

**Translate the meaning, not the words.** The recurring failure is calques —
English images carried into Czech where a Czech speaker would say something plain.
Every pair below is a real correction he made:

| Don't | Do |
|---|---|
| `pravidlo palce` | `obecně platí` |
| `domovní řád` | `pravidla` |
| `soubor s největší pákou` | `soubor s největším vlivem na výsledek` |
| `dva pachy, které stojí za naučení` | `dvě věci, které stojí za zapamatování` |
| `konkrétní bolest` | `konkrétní nedostatek` |
| `legální způsob, jak něco nevědět` | `legitimní způsob, jak něco nevědět` |
| `chyba stála draho` | `chyba byla drahá` |
| `nepište ho z prázdné stránky` | `nepište ho sami od začátku` |
| `context window přeteče` | `věci začnou ze stolu padat na zem` |
| `obsahový kalendář` | `redakční plán` |

When you add a pair to this table, grep the Czech files for the left-hand side
and fix every instance. A recorded rule that was never swept for is how
`domovní řád` survived in a heading for a week.

That last pair is the pattern worth learning: **the metaphors are welcome, the
abstractions are not.** Keep the desk, the filing cabinet and the shelf of
manuals, and make them physical in Czech rather than translating the abstract
noun that sat on top of them in English.

**Never decline an English word in Czech.** No `walkthroughu`, `draftů`,
`harnessy`, `setupu`, `checklistu`, `slugy`. Two ways out, and only these two:
leave the English word in its base form, or use a Czech word instead. Where the
sentence needs a case, put a Czech head noun in front and decline that one:

- `Ve walkthroughu stojí` → `Ve cvičení stojí`
- `postup z Walkthroughu 2` → `postup z cvičení Walkthrough 2`
- `opravováním draftů` → `opravováním hotových textů`
- `přepisování checklistu` → `přepisování seznamu`
- `pi jsou harnessy` → `pi - to všechno je harness`

**`prompt` and `skill` are the two exceptions and decline normally** —
`prompty`, `do skillu`, `přepisování promptu`. Lukáš named them: they are far
enough into Czech that working around them reads worse than declining them.
`Tahák s prompty` is the title of `PROMPTS.cs.md` and stays that way.

The rule also does not cover words Czech has fully absorbed — `agent`,
`server`, `model`, `text`, `projekt` decline normally — nor product names,
which are still `v Codexu`, `na GitHubu`, `v Gitu`.

Other fixed choices:

- `složka` → **`adresář`**. Note the gender change, feminine to masculine:
  every agreeing adjective, demonstrative and pronoun changes with it —
  `sdílená složka` → `sdílený adresář`, `ve složce` → `v adresáři`,
  `složku, ve které běží` → `adresář, ve kterém běží`
- `tón` → **`styl`**, everywhere
- `kampaňový tým` → **`marketingový tým`**
- "launch announcement" → **`tisková zpráva`**
- `SOP` is a term he uses; "written procedures" became `postupy a SOP`
- Wrap Czech prose at about 76 characters

Before handing Czech back, read it as if nobody had told you it was a
translation. Anything that reveals an English original underneath is wrong.

## Their tools

Use these in examples rather than generic equivalents:

- **WebOps** — their internal portal for managing multiple websites: write an
  article once, publish it to many sites. An MCP server and an author database
  are planned, not built.
- **Hapax** — rewrites text using an author's signature words so it reads like
  that author actually wrote it. Relevant wherever voice comes up, especially §6.2.
- **One Drive**, **Slack**, their CMS.

Do not reach for Notion, Google Drive or Confluence as illustrations. They were in
the first draft and Lukáš replaced every one.

## How we work

- Anything structural — a new section, a reorganisation, a new walkthrough — gets
  a short plan first. Do not start rewriting.
- One thing at a time. Finish it, say what changed, stop.
- Facts about the four tools go stale fast. Verify against current documentation
  before writing them down, and say so when you couldn't.
- When Lukáš corrects the same thing twice, add it to this file and tell him.

## Definition of done

A change is done when:

- The English Markdown is updated.
- The Czech Markdown matches, translated to the standard above.
- `make build` has been run, so `docs/index.html` matches, with anchors and
  tags still balanced.
- Links and anchors resolve across all files.
- Nothing has been committed and nothing has been pushed.
- If a push is in sight, the version has been raised with him — raised, not
  changed.
- You have said in three lines: what changed, which files, what needs a decision.

## How to talk to Lukáš

- Be direct. No preamble, no restating the request, no flattery.
- Three lines at the end: what you did, which files, what needs his decision.
- Disagree once, briefly, then do what he asked.
- Conversation in English.
- Flag anything you were unsure about rather than choosing silently.
