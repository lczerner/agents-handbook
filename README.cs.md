# Používání AI agentů pro reálnou práci

### Příručka pro lidi, kteří neprogramují

---

> ## ⚠️ Než začnete číst
>
> **Toto je český překlad. Závazný je anglický originál: [README.md](README.md), [HANDBOOK.md](HANDBOOK.md), [WALKTHROUGHS.md](WALKTHROUGHS.md).**
>
> Překlad existuje z jediného důvodu — aby se koncepty pochopily rychleji. Jakmile je pochopíte, přejděte na angličtinu.
>
> **Co zůstalo anglicky, a schválně:**
> - názvy souborů a složek (`AGENTS.md`, `knowledge/`, `PROGRESS.md`, `SKILL.md`)
> - odborné termíny (agent, skill, context window, MCP, prompt, session)
> - **všechny prompty a ukázky souborů** — všechno, co je v blocích kódu nebo v rámečku „TYPE THIS". Tyto texty jsou určené ke zkopírování. Nepřekládejte je.
>
> **Proč anglicky:** jazykové modely fungují v angličtině výrazně spolehlivěji než v češtině. Instrukce se dodržují přesněji, pravidla se méně obcházejí a výsledky jsou konzistentnější. Pracovním jazykem workspace — tedy `AGENTS.md`, knowledge base, prompty, plány i poznámky — by proto měla být **angličtina**.
>
> To nijak neomezuje jazyk výstupu. Pokud publikujete česky, napište to do pravidel jako kteroukoli jinou instrukci:
>
> ```
> - Always write published copy in Czech. Internal notes and planning: English.
> ```

---

Tato sada učí marketingový, obsahový nebo provozní tým používat AI agenta —
**Claude Code, OpenAI Codex CLI, opencode nebo pi** — na psaní, plánování,
rešerše a tvorbu kampaní.

Předpokládá, že nástroj už máte nainstalovaný. Učí tu část, která ve skutečnosti
rozhoduje o kvalitě výstupu: **co dáte do složky.**

---

## Začněte tady

| Přečtěte si | Čas | Co z toho máte |
|---|---|---|
| **[HANDBOOK.cs.md](HANDBOOK.cs.md)** | 40 min | Koncepty. `AGENTS.md`, plány a progress, knowledge base, skills, MCP. Sekce 1–8 přečtěte dřív, než začnete cokoli dělat. |
| **[WALKTHROUGHS.cs.md](WALKTHROUGHS.cs.md)** | Projděte je | Čtyři praktická cvičení, která na vaší reálné práci postaví funkční setup. |
| **[PROMPTS.md](PROMPTS.md)** | Mějte otevřené | Tahák s prompty. Zůstává anglicky — jsou to texty k okopírování. |
| **[starter-kit/](starter-kit/)** | Zkopírujte si ji | Kompletní ukázkový workspace. Každý soubor vyplněný a funkční. |

**Pokud máte deset minut:** přečtěte si [sekci 1 příručky](HANDBOOK.cs.md#1-jedna-myšlenka)
a pak krok 2 z prvního walkthroughu. To stačí na začátek.

---

## Myšlenka v jednom odstavci

Agent není chatbot. Běží uvnitř složky na vašem počítači, čte a zapisuje soubory
v ní, hledá na webu a používá vaše další nástroje. Zároveň **mezi sezeními
všechno zapomene**. Práce tedy nespočívá v psaní chytrých promptů, ale
v tom nechat ve složce správné věci, které si najde. Pět druhů věcí: pravidla,
který čte pokaždé (`AGENTS.md`), referenční materiály, které čte, když jsou
relevantní (`knowledge/`), plán a deník, aby dlouhá práce přežila napříč dny
(`PLAN.md`, `PROGRESS.md`), zapsané postupy, které si vezme, když sedí na zadání
(skills), a napojení na systémy mimo složku (MCP).

---

## Co lidé dělají špatně

- **Chovají se k tomu jako k ChatGPT.** Chtějí text v chatovacím okně a kopírují
  si ho ven. Výstup má přistát v souboru, v projektové složce, kde na něm můžete
  dál pracovat.
- **Přeskočí `AGENTS.md`.** A pak donekonečna vysvětlují styl v každém sezení.
- **Napíšou `AGENTS.md` na 900 řádků.** Delší soubory se dodržují *hůř*.
  Držte ho pod 200 řádky a detaily přesuňte do `knowledge/`.
- **Píšou vágní pravidla.** „Buď profesionální" se nedá dodržet. „Žádná věta nad
  25 slov" se dá zkontrolovat.
- **Zadají celou práci najednou.** Vyžádejte si plán, schvalte ho a pak nechte
  běžet jednu fázi po druhé.
- **Věří číslu, protože zní věrohodně.** Zkontrolujte každou statistiku, citaci,
  datum a jméno, které se dostane do publikovaného textu.

---

## Checklist pro první týden

- [ ] Vytvořte složku workspace, kterou bude tým sdílet
- [ ] Napište `AGENTS.md` (Walkthrough 1 — nechte se od agenta vyzpovídat)
- [ ] Přidejte `CLAUDE.md` s obsahem `@AGENTS.md`, pokud někdo používá Claude Code
- [ ] Napište jeden channel file a jeden voice file
- [ ] Udělejte s tím jeden reálný kus práce (Walkthrough 2)
- [ ] Po něm se zeptejte: *„co jsem si měl zapsat a nezapsal?"*

Všechno ostatní — další kanály, entity files, skills, MCP konektory — přijde
později, až ucítíte konkrétní problém, který každá z těch věcí řeší.

---

## Poznámky

Dvě pravidla, která se nemění:

1. **Fakta si ověřte sami.** Mantinely v této sadě výmysly výrazně omezí.
   Neodstraní je.
2. **Bez člověka se nic nepublikuje.** Nechte to pravidlo v `AGENTS.md` a nechte
   ho platit — zvlášť až připojíte nástroje, které by to technicky uměly.

---

## Zdroje

Psáno v srpnu 2026 proti aktuální dokumentaci:

- [AGENTS.md](https://agents.md/) — otevřený standard, dnes pod Agentic AI
  Foundation při Linux Foundation
- [Agent Skills specification](https://agentskills.io/specification) — formát
  `SKILL.md`, podporovaný 40+ nástroji
- [Claude Code: memory](https://code.claude.com/docs/en/memory) ·
  [skills](https://code.claude.com/docs/en/skills) ·
  [MCP](https://code.claude.com/docs/en/mcp)
- [Codex: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) ·
  [skills](https://learn.chatgpt.com/docs/build-skills)
- [opencode: rules](https://opencode.ai/docs/rules/)
- [pi: coding agent docs](https://github.com/earendil-works/pi)
- [Model Context Protocol](https://modelcontextprotocol.io/)

Detaily nástrojů se mění rychle. Pokud nějaká cesta k souboru
v [Příloze A](HANDBOOK.cs.md#příloha-a--který-soubor-čte-můj-nástroj) nefunguje,
podívejte se do aktuální dokumentace svého nástroje — koncepty platí dál.
