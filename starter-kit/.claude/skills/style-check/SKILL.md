---
name: style-check
description: Audit any text against our house voice, channel rules and factual guardrails, then fix what fails. Use when asked to review, edit, proofread, tighten, or check the tone of a draft, email, post, or page — including text a human wrote.
---

# Style check

Works on anything: our drafts, a colleague's copy, a page already published.

## Step 1 — Establish the target
Ask which channel this is for if it isn't obvious, then read:
- `knowledge/voice/house-voice.md` (always)
- the relevant `knowledge/channels/<channel>.md`
- the author file, if it's bylined

## Step 2 — Mechanical pass
Produce a table. One row per issue. Columns: **line/quote · rule broken · fix**.

Check, in this order:
1. Banned words and phrases from the voice file
2. Em dashes
3. Sentences over 25 words
4. Paragraphs over three sentences
5. Passive voice where an actor could be named
6. First person plural ("we", "our company") where second person would work
7. Vague scale words where a number exists ("significantly", "dramatically")
8. Channel format rules: length, heading frequency, CTA placement, meta description

## Step 3 — Factual pass
List every factual claim. For each: the source, or mark it **UNSOURCED**.

Flag separately:
- Any product claim not in `knowledge/entities/products.md`
- Any person's name, title or pronoun that doesn't match `knowledge/entities/people.md`
- Any event name, date or status that doesn't match `knowledge/entities/events.md`
- Any statistic without a link and a publication date

Then say which unsourced claim would be most damaging if it turned out to be wrong.

## Step 4 — Voice pass
Quote every sentence that sounds like it was written by AI or by a marketing
department rather than by us. Say why, and rewrite each one in our voice.

The test from the voice file: would you say this to a foreman standing in front
of you?

## Step 5 — Report, then fix
Give me the report first. Ask before rewriting — sometimes I want the report only.

When I say go: apply the fixes to the file in place, change nothing else, and
list what you changed.

## Never
- Never "improve" something that wasn't flagged by a rule. Scope creep in an
  edit pass is how a draft loses its voice.
- Never remove a `[NEEDS SOURCE]` marker by filling in a plausible number.
