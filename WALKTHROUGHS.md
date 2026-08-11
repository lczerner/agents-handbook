# Walkthroughs

### Four exercises that build on each other

> **These are exercises, not a method.** This is not a guide to writing articles or running marketing campaigns. They are examples, and they may have nothing to do with your job. The point is to let you get a feel for how an agent behaves, and to show you some of what can be customised.
>
> Nothing here is off-limits. Ideally, swap the brief for something you actually want to produce — but keep the idea of the exercise intact.

Do these in order. Everything in **`> blockquote`** is meant to be typed to the agent, more or less as written — adapt the names to your own work. Everything in a `code block` is a file or a terminal command.

| # | Walkthrough | Time | What you end up with |
|---|---|---|---|
| 1 | [Set up your workspace](#walkthrough-1--set-up-your-workspace) | 45 min | A real `AGENTS.md` and two knowledge files |
| 2 | [Write an article](#walkthrough-2--write-an-article) | 90 min | A publish-ready draft, and a voice guide derived from your own work |
| 3 | [Plan a campaign](#walkthrough-3--plan-a-media-campaign) | 3 sessions over 2 days | A full multi-channel campaign plan, built across sessions |
| 4 | [Turn it into a skill](#walkthrough-4--turn-a-repeated-task-into-a-skill) | 30 min | A reusable procedure you invoke with one word |

Before you start: your agent tool should be installed and working, and you should be able to open a terminal in a directory and run it. If that sentence is doing a lot of work, get whoever set it up to sit with you for the first ten minutes of Walkthrough 1.

---

<a id="walkthrough-1--set-up-your-workspace"></a>
## Walkthrough 1 — Set up your workspace

**Goal:** a directory with house rules the agent follows, and enough knowledge to write something that sounds like you.
**Time:** about 45 minutes.

### Step 1 — Make the directory

Make a new directory somewhere sensible — `Documents/content-workspace` is fine. Open your terminal in it and start your agent (`claude`, `codex`, `opencode`, or `pi`).

Then, to check it can actually see and write files:

> Create a directory called `knowledge` with subdirectories `channels`, `voice`, `entities`, and `library`. Also create a directory called `projects`. Then show me the directory structure.

You should see the directories appear on disk. If it asks permission to create files, say yes. **This is the whole trick of working with agents: you are not asking for text, you are asking for changes to a directory.**

### Step 2 — Let it interview you

Don't write `AGENTS.md` from a blank page. Type this:

> I want to create an `AGENTS.md` for this workspace. This is where our team will plan and write everything we publish.
>
> Don't write the file yet. First, interview me. Ask me **one question at a time**, up to about fifteen questions, covering:
> - what our company does and who we sell to
> - what we publish and where
> - who reads it
> - our writing rules and the words we hate
> - mistakes you could make that would embarrass us
> - what you should never do without asking
> - what a finished piece of work looks like
>
> Wait for my answer before each next question. When you have enough, say so and stop.

Then answer honestly, in short sentences. Don't try to sound polished — this is raw input, not a document.

**Where people get this wrong:** answering vaguely. "We're professional but friendly" is worthless. "We sound like a site manager explaining something to a colleague, never like a vendor" is worth an hour of editing later. When it asks about words you hate, actually list ten.

### Step 3 — Get the draft, then take it over

> Now write `AGENTS.md` based on my answers. Use these sections in this order:
> What this is · Who we write for · Where things live · Guardrails (Never / Always / Ask me first) · How we work · Definition of done · How to talk to me.
>
> Keep it under 150 lines. Make every rule specific enough that I could check whether you followed it — no "write well", no "be professional".

Now **read it yourself and edit it by hand.** Open it in any text editor. This is your file, not the agent's. Three things to check:

1. **Is every rule checkable?** Delete or sharpen anything you couldn't verify with a highlighter.
2. **Does anything contradict anything else?** "Keep it concise" plus "aim for 1,800 words" is a coin flip. Pick one.
3. **Is the "Never" list honest?** Add the things that would actually get you in trouble: inventing statistics, naming competitors, claiming a product does something it doesn't, publishing anything at all.

Make sure these two lines are in there, whatever else is:

```markdown
- Never invent a statistic, quote, customer name, or case study. If you need
  one and don't have a source, write [NEEDS SOURCE: what you need] and continue.
- Never publish, post, send, or schedule anything. You draft, a human ships.
```

### Step 4 — If you use Claude Code, add one more file

Claude Code reads `CLAUDE.md`, not `AGENTS.md`. Ask for it:

> Create a `CLAUDE.md` in the project root containing exactly one line: `@AGENTS.md`

Now both work from the same source and you never maintain two files. (Codex, opencode and pi read `AGENTS.md` directly — nothing else to do.)

### Step 5 — Your first channel file

Pick the one channel you publish to most.

> Interview me about our blog, one question at a time, so you can write a channel file. Ask about: its purpose, who arrives there and why, format and length, structure rules, SEO rules, what we never do on this channel, and which past pieces are good examples.
>
> Then write it to `knowledge/channels/blog.md`.

### Step 6 — Your voice file

If you already have published work, use it — this produces a far better result than describing your voice from memory:

> I'm going to put five of our best published articles in `knowledge/library/articles/`. Read all of them, then write `knowledge/voice/house-voice.md` containing:
> - our voice in one sentence
> - concrete rules (sentence length, person, tense, paragraph length)
> - **at least ten "do this, not that" pairs using real sentences from those articles**
> - a banned words list of anything that would sound wrong in our voice
> - punctuation conventions you can see us following
>
> Base it only on what's actually in the articles. Don't invent rules that sound good.

(Copy the articles into that directory first — as `.md` or `.txt` files. If your CMS exports HTML, that's fine too, just say so.)

If you have nothing published yet, have it interview you instead, and insist on the do/don't pairs.

### Step 7 — Prove the whole thing works

Fresh session (in Claude Code, type `/clear`). Then:

> Read `AGENTS.md` and everything in `knowledge/`. Then write me a 150-word LinkedIn post announcing that we've published a new guide about [any topic you actually cover].
>
> After you write it, audit your own post against `knowledge/voice/house-voice.md`, rule by rule, with ✅ or ❌ and a fix for each ❌.

Read the output. It won't be perfect. That's the point — **whatever is wrong with it tells you exactly which file is missing something.**

Then close the loop:

> The tone is off in the second paragraph — it sounds like a press release, and we never do that. Add a rule to the right file so this doesn't happen again, and tell me which file you chose and why.

**✅ Done when:** you have `AGENTS.md`, one channel file, one voice file, and you've watched the agent follow a rule you wrote.

---

<a id="walkthrough-2--write-an-article"></a>
## Walkthrough 2 — Write an article

**Goal:** a publish-ready draft, produced in phases with you as the editor at each gate.
**Time:** about 90 minutes.
**Needs:** Walkthrough 1 finished.

### Step 1 — Set up the project

> Create `projects/2026-08-guide-article/` with a `drafts/` subdirectory. In it, create `BRIEF.md` and interview me to fill it in: what we're writing, for which channel, target reader, the one thing they should take away, target length, deadline, and what success looks like.

A brief is the cheapest thing to get right and the most expensive thing to get wrong. Five minutes here.

### Step 2 — Angles, not a draft

> Read `BRIEF.md`, the channel file, and `knowledge/voice/house-voice.md`.
>
> Then search `knowledge/library/articles/` for anything we've already published on this topic and tell me what you found.
>
> Then give me **three angles** for this piece. For each: the promise to the reader in one sentence, why we're credible on it, and what evidence we'd need to make it stand up.
>
> Do not write the article. Recommend one angle and say why.

Pick one. Push back if none are right — *"None of these. The interesting thing is X. Give me three angles on that."* Two rounds here beats fixing a finished draft.

### Step 3 — Evidence before prose

> Angle 2, please. Now collect the evidence.
>
> Search the web for supporting data. For every source: the link, the publication date, and the exact claim it supports. Prefer primary sources — original research, official statistics, named studies. Skip anything you can't date.
>
> Pull the approved product claims from `knowledge/entities/products.md`. Do not use any product claim that isn't in that file.
>
> Save it all to `research.md` in the project directory. Anything we need but can't source, list as `[NEEDS SOURCE: ...]`.

Then — and this is the step people skip — **open `research.md` and click two of the links.** You are checking whether its sources are real and say what it claims. Do this every time for the first month. It calibrates your trust, and you will find it useful to know exactly where the weak points are.

### Step 4 — Outline

> Write an outline: H2 headings, one line under each on what that section does for the reader, plus **the opening paragraph written out in full**.
>
> Follow the structure rules in the channel file. Don't draft the rest.

The opening in full is deliberate. It's where voice lives, and it costs nothing to redo now. If the opening is right, the draft usually follows.

### Step 5 — Draft

> Good. Write the full draft to `drafts/<slug>.md`, following the outline and the channel format rules.

Then leave it alone. Don't read it yet — the next step will fix half of what you'd have commented on.

### Step 6 — Make it review itself

> Now audit your own draft against `knowledge/voice/house-voice.md` and the channel file.
>
> Produce a table: each rule, ✅ or ❌, and the specific fix for each ❌. Check especially: banned words, sentences over 25 words, paragraphs over three sentences, passive voice, em dashes, and any claim without a source.
>
> Be genuinely critical. A review that finds nothing is a review you didn't do.
>
> Then apply every fix to the file and tell me what you changed.

This step consistently produces a bigger improvement than any amount of re-prompting. Generating and judging are different jobs; doing them separately works better than doing them at once.

### Step 7 — Now you read it

Open the draft. Edit as an editor, not a prompter — ask for surgical changes, in place:

> In the draft file: cut the third section entirely, it repeats section one. Tighten the intro to four sentences. Leave everything else exactly as it is.

Note "leave everything else exactly as it is." Without it you sometimes get a full rewrite and lose the parts you liked.

Then a harder pass:

> Read the draft as our most sceptical reader — an ops manager who's been sold bad software before. List every sentence they'd roll their eyes at, and why. Don't fix anything yet.

### Step 8 — Package it

> Add to the top of the draft file: three headline options, a meta description under 155 characters, a suggested slug, and two internal links from `knowledge/library/articles/`.
>
> Add at the bottom: an image brief, and every `[NEEDS SOURCE]` marker collected into one list.
>
> Then tell me in three lines: what's done, where it is, what you need from me.

### Step 9 — Bank the learning

> Which corrections did I make today that you should have got right the first time? For each, tell me which file should have prevented it, and make the edit.

Do this after every piece for the first month. It is how the workspace gets good.

**✅ Done when:** a draft exists in the directory, every source is checked, and at least one rule got added to a file because of something that went wrong today.

---

<a id="walkthrough-3--plan-a-media-campaign"></a>
## Walkthrough 3 — Plan a media campaign

**Goal:** a full multi-channel campaign plan, built across three separate sessions, proving the plan/phase/logbook system.
**Time:** three sessions of ~45 minutes, ideally on different days.
**Needs:** Walkthroughs 1–2.

This one is deliberately spread over days. The point is to watch the agent pick up cold from a logbook — the skill that makes long projects possible.

### Session 1 — Brief and plan

**Step 1.** Set up:

> Create `projects/2026-09-atlas-launch/` with `drafts/` and `research/` subdirectories.
>
> Create `BRIEF.md` and interview me one question at a time: what we're launching, the date, the audience, the one message, which channels, budget, who's involved, what success looks like in numbers, and any hard constraints (embargoes, legal, approvals).

**Step 2.** Get a plan and nothing else:

> Read `BRIEF.md`, `knowledge/INDEX.md`, and the channel files for every channel in the brief.
>
> Write a phased plan to `PLAN.md`. **Do not produce any campaign content.**
>
> 5–7 phases. For each: goal in one sentence, inputs needed, files produced, and how we'll know it's done. Every phase must be small enough to finish in one sitting. At least two phases must end with a decision I have to make.
>
> At the end, list your assumptions and anything the brief doesn't answer.

**Step 3.** Read the plan properly. This is your one big steering moment. Typical corrections:

> Three changes. Phase 2 is too big — split it into messaging and calendar. Move the press list to Phase 1, we need it earlier for embargoes. And add a phase for the sales enablement one-pager, I forgot it in the brief. Update `PLAN.md` and `BRIEF.md`.

**Step 4.** Do exactly one phase:

> Now do Phase 1 only. Stop when it's done.

**Step 5.** Close the session — this step is the whole exercise:

> Stop here. Create `PROGRESS.md` with:
>
> **Status** — current phase, the single next action, anything you're blocked on
> **Decisions made** — dated, with the reason for each
> **Log** — what you did today, which files you produced, what you learned, open questions
>
> Write it so someone who wasn't here today could pick this up cold with no other context.

Then close the tool.

### Session 2 — The cold start

**Step 6.** New day, fresh session. Type only this:

> Read `PROGRESS.md` and `PLAN.md` in `projects/2026-09-atlas-launch/`. Tell me in five lines where we are and what the next action is. Don't start work yet.

Watch what happens. It will tell you exactly where you left off, including why you made the decisions you made. **This is the moment the system clicks.** No re-explaining, no scrolling back through a chat.

If it's confused or vague, that's diagnostic: `PROGRESS.md` wasn't specific enough. Fix the log format now, while it's obvious what was missing.

**Step 7.** Continue:

> Correct. Do Phase 2 only, then stop.

**Step 8.** Same closing ritual. Every time:

> Stop here. Update `PROGRESS.md` — status, next action, decisions with reasons, and today's log entry. Keep the whole file under 100 lines by summarising older entries.

### Session 3 — Finish and package

**Step 9.** Cold start again, then work through the remaining phases — still one at a time, still logging at the end of each.

**Step 10.** When the plan is complete:

> The plan is finished. Produce `CAMPAIGN.md` in the project root: the full campaign on one page — messaging spine, channel-by-channel calendar with dates, the asset list with file paths and owners, dependencies and deadlines, and how we'll measure it.
>
> Then list everything still blocked on a human, and who needs to do what.

**Step 11.** Stress-test it before anyone else sees it:

> Now be our CFO reading this for the first time. What are the three weakest points? What would you refuse to approve and why?

**Step 12.** Bank it:

> What did we learn about how we plan campaigns that isn't written down anywhere? Propose additions to `AGENTS.md` or a new knowledge file. Show me the changes before making them.

**✅ Done when:** you've had at least one cold start that worked, and `CAMPAIGN.md` is something you'd actually send to a colleague.

---

<a id="walkthrough-4--turn-a-repeated-task-into-a-skill"></a>
## Walkthrough 4 — Turn a repeated task into a skill

**Goal:** the process from Walkthrough 2 becomes something you invoke with one word, that works identically for everyone on the team.
**Time:** 30 minutes.
**Needs:** Walkthrough 2 — you need to have done the task manually once.

### Step 1 — Find the right directory

Depends on your tool (see Appendix A of the handbook):

| Tool | Directory |
|---|---|
| Claude Code | `.claude/skills/` |
| Codex CLI | `.agents/skills/` |
| opencode | `.opencode/skills/` |
| pi | `.pi/skills/` or `.agents/skills/` |

### Step 2 — Have it write the skill from what you actually did

> Look back at how we produced the article in `projects/2026-08-guide-article/`, including every correction I made along the way.
>
> Turn that into a skill at `.claude/skills/article-draft/SKILL.md`.
>
> Requirements:
> - YAML frontmatter with `name: article-draft` and a `description` that says what it does **and when to use it**, using words I'd actually type — write, draft, article, blog post, outline, newsletter.
> - The body is the procedure, in numbered phases.
> - Mark with ⏸ every point where you must stop and wait for me.
> - Include the self-review phase where you audit your own draft against the voice file with ✅/❌ and fix every ❌.
> - Include every correction I made during the walkthrough as an explicit rule.
> - Under 200 lines. Push anything long into `references/`.

### Step 3 — Check the description

Open `SKILL.md` and look at the `description` line. It is the only part the agent sees until it decides to open the skill, so it has to contain the words you'd naturally use.

❌ `description: Helps with writing articles.`
✅ `description: Produce a publish-ready article draft from a brief, following our channel and voice rules. Use when asked to write, draft, or outline a blog post, article, or newsletter piece.`

Also check: `name` is lowercase-with-hyphens, and it **matches the directory name exactly**. That's the most common reason a skill silently doesn't load.

### Step 4 — Test both ways

**Directly** — fresh session, then type `/article-draft` (Claude Code, opencode) or `$article-draft` (Codex). It should start at Phase 1.

**Automatically** — fresh session, then type something natural:

> I need a blog post about how site diaries actually get filled in.

If the skill was written well, it starts following the procedure without being told. If it doesn't, the `description` is the problem — rewrite it with the words you just used.

### Step 5 — Now build the rest

Same pattern, in order of payoff:

- **`style-check`** — audits any text against your voice files, line by line, with fixes. Run it on human-written copy too.
- **`campaign-plan`** — the process from Walkthrough 3.
- **`repurpose`** — one article into a newsletter, five LinkedIn posts and an Instagram carousel, each in its channel's voice.
- **`brief-intake`** — refuses to proceed on a vague request until it's a real brief.

Never write a skill from imagination. **Do the task manually once, note every correction, then have the agent write the skill from what happened.** Skills written from imagination describe how you wish you worked. Skills written from a real session describe how you actually work, including the corrections — and those corrections are most of the value.

**✅ Done when:** you type one word and a multi-step process runs the way you'd run it yourself.

---

## What to do after all four

You now have the full system. The habit that keeps it working is a single question, asked at the end of every piece of work:

> What did I correct today that you should have known already — and which file should have told you?

Ask it every time for a month. The workspace will teach itself your job.
