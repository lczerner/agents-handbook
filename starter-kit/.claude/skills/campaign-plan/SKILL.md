---
name: campaign-plan
description: Turn a brief into a phased, multi-channel campaign plan with a dated calendar, asset list, owners and measurement. Use when asked to plan a campaign, launch, promotion, or any multi-channel piece of marketing work.
---

# Campaign plan

Never produce campaign copy while running this skill. This skill produces a plan.

## Phase 0 — Is there a real brief?
If there's no `BRIEF.md`, create one by interviewing me, one question at a time:
what we're launching, the date, the audience, the one message, the channels, the
budget, who's involved, what success looks like **in numbers**, and any hard
constraints — embargoes, legal, approvals, people's holidays.

Do not proceed on "we need a campaign for X". ⏸

## Phase 1 — Read the ground
Read `BRIEF.md`, `knowledge/INDEX.md`, the channel file for every channel named,
`knowledge/entities/products.md`, and `knowledge/entities/events.md` for status
and embargoes.

Say explicitly what the brief doesn't answer. ⏸

## Phase 2 — Write the plan
Write `PLAN.md`. 5–7 phases. For each:
- **Goal** in one sentence
- **Inputs** needed
- **Outputs** — actual file paths
- **Done when** — a checkable condition

Rules for the phases:
- Each must be finishable in one sitting.
- At least two must end in a decision only a human can make. Mark those 👤.
- Anything needing external approval (Legal, Product, an exec) gets its own early
  phase. Discovering a five-day approval turnaround in week three is how launches slip.
- Order by dependency, not by importance.

End with an **Assumptions** section: everything you had to guess, and what breaks
if the guess is wrong. ⏸ Wait for approval before any phase runs.

## Phase 3 — Execute one phase at a time
Do exactly one phase, then stop and update `PROGRESS.md`. Never two.

## Phase 4 — Package
When all phases are complete, produce `CAMPAIGN.md`: the whole campaign on one page.

- **Messaging spine** — the one message, the three supporting points, the
  objection each has to survive
- **Calendar** — table: date · channel · asset · owner · depends on
- **Assets** — table: file path · status · who approves
- **Measurement** — what number we're watching, where it comes from, when we check
- **Blocked on humans** — who owes what, by when

## Phase 5 — Stress test
Read `CAMPAIGN.md` as three sceptics in turn and report what each would say:
1. **The CFO** — what would you refuse to fund or approve?
2. **The customer** — why would you ignore all of this?
3. **The person who has to execute it** — what's unrealistic about these dates?

Then list the three changes that would most improve the plan.
