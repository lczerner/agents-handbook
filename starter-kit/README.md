# Starter kit

A complete example workspace for a fictional company called **Lighthouse** — a
B2B software company selling site-documentation tools to construction firms.

Every file here is real and working. The structure is the point, the content is
placeholder. Read it once you have a workspace of your own, and take from it the
files you find you need.

One thing is deliberately missing: the article archive under
`knowledge/library/articles/`. That directory holds your own published work, and
Lighthouse's would be no use to you.

## What's here

```
AGENTS.md                          ← house rules. Read every session. Start here.
CLAUDE.md                          ← one line: @AGENTS.md   (only for Claude Code)

knowledge/
├── INDEX.md                       ← map of the filing cabinet
├── channels/                      ← one file per place you publish
│   ├── lighthouse-blog.md
│   ├── the-signal-newsletter.md
│   └── linkedin.md
├── voice/
│   ├── house-voice.md             ← note the do-this-not-that pairs. Those do the work.
│   └── author-jana-novak.md
├── entities/                      ← the facts you're allowed to state
│   ├── products.md                ← including what the product does NOT do
│   ├── people.md                  ← names, titles, pronouns, quote permissions
│   └── events.md                  ← with embargo status
└── library/
    ├── GOLD-STANDARD.md           ← your best work and why it works
    └── articles/                  ← your own archive. The kit ships none, see the note inside

projects/2026-09-atlas-launch/     ← what an in-flight project looks like
├── BRIEF.md                       ← what we were asked for
├── PLAN.md                        ← what we agreed to do, in phases
├── PROGRESS.md                    ← the logbook that survives across sessions
└── research/positioning.md        ← the working file Phase 1 produced

.claude/skills/                    ← procedures (directory name differs per tool)
├── article-draft/SKILL.md
├── style-check/SKILL.md
└── campaign-plan/SKILL.md
```

## How to use it

**Don't copy it wholesale and start writing.** The files only work when they
contain your actual rules, and every answer in here is Lighthouse's.

Build your own workspace first, with
[Walkthrough 1](../WALKTHROUGHS.md#walkthrough-1--set-up-your-workspace) - the
agent interviews you and fills in `AGENTS.md`, a channel file, a voice file, a
product fact sheet and an index. That is enough to do real work with.

Then come back here. Read a file to see the shape of one you haven't written
yet, and take it across when you find you need it: `people.md` the first time
the agent gets a job title wrong, `events.md` the first time something is true
but not yet public, `GOLD-STANDARD.md` once you have work worth pointing at.

Most teams never need all of it.

## Which skills directory do I use?

`.claude/skills/` is Claude Code. If you use something else, rename the
directory — the `SKILL.md` files themselves are identical:

| Tool | Directory |
|---|---|
| Claude Code | `.claude/skills/` |
| Codex CLI | `.agents/skills/` |
| opencode | `.opencode/skills/` |
| pi | `.pi/skills/` or `.agents/skills/` |

## Things worth noticing

- **`products.md` has a "What it does NOT do" section.** This prevents more
  embarrassment than everything else in the kit combined.
- **`people.md` spells out pronouns and exact job titles.** Two lines that
  eliminate a whole category of error the agent can't otherwise avoid.
- **`events.md` has a status field with an embargo.** Facts that are true but not
  yet public need to be marked as such.
- **`house-voice.md` is mostly do-this-not-that pairs.** Adjectives like
  "confident and warm" produce nothing. Contrast pairs produce a voice.
- **`PROGRESS.md` records decisions with reasons.** In six weeks someone will ask
  why, and the answer will be there with a date on it.
- **Every skill has a self-review phase.** Asking the agent to criticise its own
  work against a written checklist works far better than asking it to write well.

## License

This directory is public domain: CC0 1.0, see [LICENSE](LICENSE). Copy it,
rewrite it, publish whatever you make from it. Nothing to credit, no notice to
keep. The rest of the kit is CC BY 4.0 and does ask for credit.
