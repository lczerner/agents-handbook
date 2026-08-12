# Prompt cheat sheet

Keep this open for your first fortnight. Copy, paste, adapt.

> **Starting points, not battle-tested prompts.** These are simple examples to get you going. Change them to fit your work and keep whatever works best for you.

---

## Every session

**Start of a session on an existing project**
> Read `PROGRESS.md` and `PLAN.md` in `projects/<name>/`. Tell me in five lines where we are and what the next action is. Don't start work yet.

**End of every session - never skip this**
> Stop here. Update `PROGRESS.md`: status, the single next action, decisions made today with the reason for each, and today's log entry with the files you produced. Write it so someone who wasn't here today could pick it up cold.

**When quality drops mid-session** *(it repeats itself, forgets a decision, contradicts the outline)*
> Update `PROGRESS.md` with where we are. I'm starting a fresh session.

Then clear the session (`/clear` in Claude Code) and start again.

---

## Getting set up

**Write your AGENTS.md**
> I want to create an `AGENTS.md` for this workspace. Don't write it yet. First interview me, one question at a time, up to fifteen questions, about what we publish, who reads it, our rules, the mistakes you could make that would embarrass us, what you should never do without asking, and what "done" looks like. Wait for my answer before each next question.

**Derive a voice guide from your own published work**
> Read every article in `knowledge/library/articles/`. Write `knowledge/voice/house-voice.md`: our voice in one sentence, concrete rules, at least ten "do this, not that" pairs using real sentences from those articles, a banned words list, and punctuation conventions. Base it only on what's actually there - don't invent rules that sound good.

**Write a channel file**
> Interview me about our <channel>, one question at a time, then write `knowledge/channels/<name>.md`: purpose, who arrives and why, format and length, structure rules, SEO rules, what we never do here, and which past pieces are good examples.

**Build a product fact sheet**
> Interview me about <product> and write `knowledge/entities/products.md`. Include what it does, **what it explicitly does not do**, approved claims with their sources, claims we must never make, pricing, and approved boilerplate. Add "Last verified: <today>" at the top.

---

## Planning

**Get a plan, not a draft**
> Read `BRIEF.md` and the relevant knowledge files. Write a phased plan to `PLAN.md`. **Do not do any of the work yet.** 5–7 phases; for each: goal in one sentence, inputs needed, files produced, how we'll know it's done. Each phase small enough for one sitting. At least two must end with a decision I have to make. List your assumptions at the end.

**Work one phase**
> Do Phase 2 only. Stop when it's done.

**Change the plan**
> Three changes to `PLAN.md`: <...>. Update the file and tell me what else those changes affect.

---

## Writing

**Angles before drafting**
> Give me three angles. For each: the promise to the reader in one sentence, why we're credible on it, and what evidence we'd need. Recommend one and say why. Don't write the piece.

**Research with real sources**
> Search the web for supporting data. For every source give the link, the publication date, and the exact claim it supports. Prefer primary sources. Skip anything you can't date. Save to `research.md`. Anything we need but can't source: `[NEEDS SOURCE: ...]`.

**Outline with the opening written out**
> Write an outline: H2s with one line each on what that section does for the reader, plus the opening paragraph in full. Don't draft the rest.

**Draft to a file**
> Write the full draft to `drafts/<slug>.md`, following the outline and the channel format rules.

**Self-review - the one prompt here that improves a draft most**
> Audit your own draft against `knowledge/voice/house-voice.md` and the channel file. A table: each rule, ✅ or ❌, and the specific fix for each ❌. Check especially banned words, sentences over 25 words, paragraphs over three sentences, passive voice, em dashes, and unsourced claims. Be genuinely critical - a review that finds nothing is a review you didn't do. Then apply every fix and tell me what you changed.

**Surgical edits**
> In the draft file: cut section 3, it repeats section 1. Tighten the intro to four sentences. **Leave everything else exactly as it is.**

**Package it**
> Add to the top: three headline options, a meta description under 155 characters, a suggested slug, two internal links from our library. Add at the bottom: an image brief and every `[NEEDS SOURCE]` marker collected in one list.

---

## Pressure-testing

**Hostile reader**
> Read this as our most skeptical reader - <describe them>. List every sentence they'd roll their eyes at, and why. Don't fix anything yet.

**The approver**
> You're the CFO / Legal / our head of sales reading this for the first time. What would you refuse to approve, and why?

**Find the weak claims**
> List every factual claim in this draft. For each: the source, or mark it unsourced. Then tell me which unsourced claim would be most damaging if it were wrong.

**Kill the AI smell**
> Find every sentence that sounds like it was written by AI rather than by us. Quote it, say why, and rewrite it in our voice.

---

## Repurposing

> Turn `drafts/<slug>.md` into: a 400-word newsletter piece, five LinkedIn posts, and an Instagram carousel outline. Read each channel's file first and write each one properly for that channel - do not paste the same paragraphs across formats. Save each to `drafts/repurposed/`.

---

## Maintaining the system

**After every piece of work**
> What did I correct today that you should have got right the first time? For each, tell me which file should have prevented it, and make the edit.

**File a correction immediately**
> Add that to the right file so it holds from now on. Tell me which file you chose and why.

**Health check on your setup**
> Read `AGENTS.md` and everything in `knowledge/`. Tell me: anything that contradicts anything else, anything too vague for you to actually follow, anything out of date, and the three things missing that would most improve your output.

**Turn a session into a skill**
> Turn what we just did into a skill at `<skills directory>/<name>/SKILL.md`, including every correction I made along the way. Frontmatter with `name` matching the directory and a `description` saying what it does and when to use it, using the words I'd actually type. Mark with ⏸ every point where you must stop and wait for me.

---

## Phrases worth memorizing

| Say this | To get this |
|---|---|
| **"Don't do the work yet."** | A plan you can fix cheaply |
| **"One phase, then stop."** | Control over a long job |
| **"Save it to `<path>`."** | Output in a file, not lost in the terminal |
| **"Leave everything else exactly as it is."** | Surgical edits instead of a full rewrite |
| **"Give me three options and recommend one."** | You stay the editor |
| **"Audit that against `<file>`, rule by rule."** | Real self-correction |
| **"Ask me before you..."** | A checkpoint where it matters |
| **"Which file should have prevented that?"** | A system that improves itself |
| **"Read `<file>` first."** | No guessing |
| **"If you don't have a source, write `[NEEDS SOURCE: ...]`."** | Honest gaps instead of invented facts |

---

## Two things no prompt can fix

**Check the facts yourself.** Every statistic, quote, date, price, and spelling of a person's name that reaches a published page. The guardrails reduce invention a great deal. They don't eliminate it. Your `[NEEDS SOURCE]` markers tell you where to look first, but they are not a complete list of what to check.

**Nothing publishes without a human.** Keep "never publish, post, send, or schedule" in `AGENTS.md`, and keep it true - especially once you've connected MCP tools that could technically do it.
