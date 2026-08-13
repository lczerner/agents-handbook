<!--
SPDX-FileCopyrightText: Copyright 2026, Lukáš Czerner <lukas@czerner.cz>
SPDX-License-Identifier: CC-BY-4.0
-->

# Tahák s prompty

Prvních čtrnáct dní ho mějte otevřený. Kopírujte, vkládejte, upravujte.

> **⚠️ Toto je český překlad.** Závazný je anglický originál:
> [PROMPTS.md](PROMPTS.md). **Samotné prompty zůstávají anglicky a jsou určené
> ke zkopírování tak, jak jsou** - jazykové modely dodržují instrukce
> v angličtině spolehlivěji. Česky jsou jen popisky a komentáře.

> **Příklady na začátek, ne prověřené prompty.** Jsou to jednoduché příklady,
> které vám pomůžou začít. Upravte si je podle své práce a nechte si to, co vám
> funguje nejlíp.

---

## Každé sezení

**Začátek sezení na rozpracovaném projektu**
> Read `PROGRESS.md` and `PLAN.md` in `projects/<name>/`. Tell me in five lines where we are and what the next action is. Don't start work yet.

**Konec každého sezení - tohle nikdy nevynechávejte**
> Stop here. Update `PROGRESS.md`: status, the single next action, decisions made today with the reason for each, and today's log entry with the files you produced. Write it so someone who wasn't here today could pick it up cold.

**Když se uprostřed sezení zhorší kvalita** *(opakuje se, zapomene rozhodnutí, odporuje osnově)*
> Update `PROGRESS.md` with where we are. I'm starting a fresh session.

Pak sezení vyčistěte (`/clear` v Claude Code) a začněte znovu.

---

## Než začnete

**Napsat AGENTS.md**
> I want to create an `AGENTS.md` for this workspace. Don't write it yet. First interview me, one question at a time, up to fifteen questions, about what we publish, who reads it, our rules, the mistakes you could make that would embarrass us, what you should never do without asking, and what "done" looks like. Wait for my answer before each next question.

**Odvodit voice guide z vlastních publikovaných textů**
> Read every article in `knowledge/library/articles/`. Write `knowledge/voice/house-voice.md`: our voice in one sentence, concrete rules, at least ten "do this, not that" pairs using real sentences from those articles, a banned words list, and punctuation conventions. Base it only on what's actually there - don't invent rules that sound good.

**Napsat channel file**
> Interview me about our <channel>, one question at a time, then write `knowledge/channels/<name>.md`: purpose, who arrives and why, format and length, structure rules, SEO rules, what we never do here, and which past pieces are good examples.

**Sestavit produktový fact sheet**
> Interview me about <product> and write `knowledge/entities/products.md`. Include what it does, **what it explicitly does not do**, approved claims with their sources, claims we must never make, pricing, and approved boilerplate. Add "Last verified: <today>" at the top.

---

## Plánování

**Plán, ne draft**
> Read `BRIEF.md` and the relevant knowledge files. Write a phased plan to `PLAN.md`. **Do not do any of the work yet.** 5–7 phases; for each: goal in one sentence, inputs needed, files produced, how we'll know it's done. Each phase small enough for one sitting. At least two must end with a decision I have to make. List your assumptions at the end.

**Udělat jednu fázi**
> Do Phase 2 only. Stop when it's done.

**Změnit plán**
> Three changes to `PLAN.md`: <...>. Update the file and tell me what else those changes affect.

---

## Psaní

**Úhly pohledu před psaním**
> Give me three angles. For each: the promise to the reader in one sentence, why we're credible on it, and what evidence we'd need. Recommend one and say why. Don't write the piece.

**Rešerše se skutečnými zdroji**
> Search the web for supporting data. For every source give the link, the publication date, and the exact claim it supports. Prefer primary sources. Skip anything you can't date. Save to `research.md`. Anything we need but can't source: `[NEEDS SOURCE: ...]`.

**Osnova s napsaným úvodem**
> Write an outline: H2s with one line each on what that section does for the reader, plus the opening paragraph in full. Don't draft the rest.

**Draft do souboru**
> Write the full draft to `drafts/<slug>.md`, following the outline and the channel format rules.

**Sebekontrola - prompt, který textu pomůže nejvíc**
> Audit your own draft against `knowledge/voice/house-voice.md` and the channel file. A table: each rule, ✅ or ❌, and the specific fix for each ❌. Check especially banned words, sentences over 25 words, paragraphs over three sentences, passive voice, em dashes, and unsourced claims. Be genuinely critical - a review that finds nothing is a review you didn't do. Then apply every fix and tell me what you changed.

**Chirurgické úpravy**
> In the draft file: cut section 3, it repeats section 1. Tighten the intro to four sentences. **Leave everything else exactly as it is.**

**Zabalit to**
> Add to the top: three headline options, a meta description under 155 characters, a suggested slug, two internal links from our library. Add at the bottom: an image brief and every `[NEEDS SOURCE]` marker collected in one list.

---

## Zátěžové testy

**Nepřátelský čtenář**
> Read this as our most skeptical reader - <describe them>. List every sentence they'd roll their eyes at, and why. Don't fix anything yet.

**Ten, kdo to schvaluje**
> You're the CFO / Legal / our head of sales reading this for the first time. What would you refuse to approve, and why?

**Najít slabá tvrzení**
> List every factual claim in this draft. For each: the source, or mark it unsourced. Then tell me which unsourced claim would be most damaging if it were wrong.

**Aby to nepůsobilo jako od AI**
> Find every sentence that sounds like it was written by AI rather than by us. Quote it, say why, and rewrite it in our voice.

---

## Přepoužití obsahu

> Turn `drafts/<slug>.md` into: a 400-word newsletter piece, five LinkedIn posts, and an Instagram carousel outline. Read each channel's file first and write each one properly for that channel - do not paste the same paragraphs across formats. Save each to `drafts/repurposed/`.

---

## Údržba systému

**Po každém kusu práce**
> What did I correct today that you should have got right the first time? For each, tell me which file should have prevented it, and make the edit.

**Založit opravu hned**
> Add that to the right file so it holds from now on. Tell me which file you chose and why.

**Kontrola zdraví nastavení**
> Read `AGENTS.md` and everything in `knowledge/`. Tell me: anything that contradicts anything else, anything too vague for you to actually follow, anything out of date, and the three things missing that would most improve your output.

**Udělat ze sezení skill**
> Turn what we just did into a skill at `<skills directory>/<name>/SKILL.md`, including every correction I made along the way. Frontmatter with `name` matching the directory and a `description` saying what it does and when to use it, using the words I'd actually type. Mark with ⏸ every point where you must stop and wait for me.

---

## Fráze, které stojí za zapamatování

| Řekněte tohle | Abyste dostali tohle |
|---|---|
| **"Don't do the work yet."** | Plán, který se dá levně opravit |
| **"One phase, then stop."** | Kontrolu nad dlouhou prací |
| **"Save it to `<path>`."** | Výstup v souboru, ne ztracený v terminálu |
| **"Leave everything else exactly as it is."** | Chirurgické úpravy místo kompletního přepisu |
| **"Give me three options and recommend one."** | Zůstáváte editorem |
| **"Audit that against `<file>`, rule by rule."** | Skutečnou sebekontrolu |
| **"Ask me before you..."** | Kontrolní bod tam, kde na tom záleží |
| **"Which file should have prevented that?"** | Systém, který se sám zlepšuje |
| **"Read `<file>` first."** | Žádné hádání |
| **"If you don't have a source, write `[NEEDS SOURCE: ...]`."** | Poctivé mezery místo vymyšlených faktů |

---

## Dvě věci, které žádný prompt nespraví

**Fakta si ověřte sami.** Každou statistiku, citaci, datum, cenu i pravopis jména, které se dostane na publikovanou stránku. Mantinely výmysly výrazně omezí. Neodstraní je. Značky `[NEEDS SOURCE]` vám řeknou, kde hledat nejdřív, ale nejsou úplným seznamem toho, co zkontrolovat.

**Bez člověka se nic nepublikuje.** Nechte v `AGENTS.md` pravidlo „never publish, post, send, or schedule" a nechte ho platit - zvlášť až připojíte MCP nástroje, které by to technicky uměly.
