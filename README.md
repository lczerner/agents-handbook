# Using AI agents for real work

### A training kit for people who don't write code

**Version 0.1.2** — the published page and the PDF editions carry the same
number, so you can tell whether the copy you are reading is the current one.

This kit teaches a marketing, content or operations team how to use an AI agent —
**Claude Code, OpenAI Codex CLI, opencode, or pi** — for writing, planning,
research and campaign work.

An agent is not ChatGPT in a browser tab. It runs on your computer and writes
real files. You need one installed before any of this is useful —
[Before you start](HANDBOOK.md#before-you-start) covers which four tools qualify,
how to install one, and how to check in a minute that you are really talking to
an agent. After that, this kit teaches the part that actually determines output
quality: **what you put in the directory.**

> ### 📖 Read it online
>
> **https://lczerner.github.io/agents-handbook/**
>
> The handbook, the walkthroughs and the prompt sheet on one page, in English and
> Czech, with a language switcher. Same content as the Markdown files here —
> generated from them, so it cannot drift. Send colleagues this link.

> **🇨🇿 Czech translation available** — [README.cs.md](README.cs.md) ·
> [HANDBOOK.cs.md](HANDBOOK.cs.md) · [WALKTHROUGHS.cs.md](WALKTHROUGHS.cs.md) ·
> [PROMPTS.cs.md](PROMPTS.cs.md)
>
> The Czech versions exist to speed up initial understanding only. File names,
> directories, technical terms and every prompt stay in English, because agents
> follow instructions more reliably in English. The English files here are
> authoritative; work in English once the concepts have landed.

---

## Start here

| Read this | Time | What it gives you |
|---|---|---|
| **[Before you start](HANDBOOK.md#before-you-start)** | 5 min | What an agent is, what a harness is, which tool to install, and a one-minute check that you have one. Do this first — everything else depends on it. |
| **[HANDBOOK.md](HANDBOOK.md)** | 40 min | The concepts. `AGENTS.md`, plans and progress, the knowledge base, skills, MCP. Read sections 1–8 before doing anything. |
| **[WALKTHROUGHS.md](WALKTHROUGHS.md)** | Do them | Four hands-on exercises. Examples to get a feel for the agent, ideally adapted to what you actually want to produce. |
| **[PROMPTS.md](PROMPTS.md)** | Keep open | A cheat sheet of things to type. |
| **[starter-kit/](starter-kit/)** | Copy it | A complete example workspace. Every file filled in and working. |

**If you have ten minutes:** read [section 1 of the handbook](HANDBOOK.md#1-the-one-idea)
and then Walkthrough 1 step 2. That's enough to start.

---

## The idea in one paragraph

An agent is not a chatbot. It runs inside a directory on your computer, reads
and writes the files in it, searches the web, and uses your other tools. It also
**forgets everything between sessions**. So the job is not writing clever
prompts; it is leaving the right things in the directory for it to find. Five
kinds of thing: house rules it reads every time (`AGENTS.md`), reference
material it reads when relevant (`knowledge/`), a plan and a logbook so long
jobs survive (`PLAN.md`, `PROGRESS.md`), written procedures it picks up when a
task matches (skills), and connections to systems outside the directory (MCP).

---

## What people get wrong

- **Never getting an agent at all.** Reading the walkthroughs and pasting the
  prompts into ChatGPT or Claude in a browser. You get plausible answers and not
  one file on your computer. Check before you start:
  [Before you start](HANDBOOK.md#before-you-start).
- **Treating it like ChatGPT.** Asking for text in the chat window and copying it
  out. The output should land in a file, in a project directory, where you can
  iterate.
- **Skipping `AGENTS.md`.** Then re-explaining the brand voice every
  session, forever.
- **Writing a 900-line `AGENTS.md`.** Longer files get
  followed *less*. Keep it under 200 lines and move the detail into
  `knowledge/`.
- **Vague rules.** "Be professional" is unfollowable. "No
  sentence over 25 words" is checkable.
- **Asking for the whole job at once.**
  Ask for a plan, approve it, then run one phase at a time.
- **Trusting a
  number because it sounds right.** Check every statistic, quote, date and name
  that reaches a published page.

---

## Setup checklist

Your first week, in order:

- [ ] Install one of the four tools, and confirm it can write a file on your
      computer ([Before you start](HANDBOOK.md#before-you-start))
- [ ] Create a workspace directory your team shares
- [ ] Write `AGENTS.md` (Walkthrough 1 — let the agent interview you)
- [ ] Add `CLAUDE.md` containing `@AGENTS.md`, if anyone uses Claude Code
- [ ] Write one channel file and one voice file
- [ ] Do one real piece of work with it (Walkthrough 2)
- [ ] After that piece: ask *"what should I have written down that I didn't?"*

Everything else — more channels, entity files, skills, MCP connectors — comes
later, when you feel the specific problem each one solves.

---

## A note on judgement

Two rules that never move:

1. **Check the facts yourself.** The guardrails in this kit reduce invention a
   great deal. They don't eliminate it.
2. **Nothing publishes without a human.** Keep that rule in `AGENTS.md`, and keep
   it true — especially once you connect tools that could technically do it.

---

## Sources

Written August 2026 against current documentation:

- [AGENTS.md](https://agents.md/) — the open standard, now under the Linux
  Foundation's Agentic AI Foundation
- [Agent Skills specification](https://agentskills.io/specification) — the
  `SKILL.md` format, supported by 40+ tools
- [Claude Code: quickstart](https://code.claude.com/docs/en/quickstart) ·
  [memory](https://code.claude.com/docs/en/memory) ·
  [skills](https://code.claude.com/docs/en/skills) ·
  [MCP](https://code.claude.com/docs/en/mcp)
- [Codex: quickstart](https://learn.chatgpt.com/docs/codex/cli) ·
  [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) ·
  [skills](https://learn.chatgpt.com/docs/build-skills)
- [opencode: docs](https://opencode.ai/docs/) ·
  [rules](https://opencode.ai/docs/rules/)
- [pi: quickstart](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/quickstart.md) ·
  [coding agent docs](https://github.com/earendil-works/pi)
- [Model Context Protocol](https://modelcontextprotocol.io/)

Tool details move quickly. If a file path in [Appendix A](HANDBOOK.md#appendix-a--which-file-does-my-tool-read)
doesn't work, check your tool's current docs — the concepts hold regardless.
