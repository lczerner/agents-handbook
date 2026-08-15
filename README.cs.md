<!--
SPDX-FileCopyrightText: Copyright 2026, Lukáš Czerner <lukas@czerner.cz>
SPDX-License-Identifier: CC-BY-4.0
-->

# Používání AI agentů pro reálnou práci

### Příručka pro lidi, kteří neprogramují

**Verze 0.3.0** - stejné číslo najdete na webu i v PDF, takže poznáte, jestli
čtete aktuální vydání.

---

> ## ⚠️ Než začnete číst
>
> **Toto je český překlad. Závazný je anglický originál: [README.md](README.md), [HANDBOOK.md](HANDBOOK.md), [WALKTHROUGHS.md](WALKTHROUGHS.md).**
>
> Překlad je tu z jediného důvodu: abyste koncepty pochopili rychleji. Jakmile je pochopíte, přejděte na angličtinu.
>
> **Co zůstalo anglicky, a schválně:**
> - názvy souborů a adresářů (`AGENTS.md`, `knowledge/`, `PROGRESS.md`, `SKILL.md`)
> - odborné termíny (agent, skill, context window, MCP, prompt, session)
> - **všechny prompty a ukázky souborů** - všechno, co je v blocích kódu nebo v rámečku „TYPE THIS". Ty se kopírují tak, jak jsou. Nepřekládejte je.
>
> **Proč anglicky:** jazykové modely fungují v angličtině výrazně spolehlivěji než v češtině. Instrukce se dodržují přesněji, pravidla se méně obcházejí a výsledky jsou konzistentnější. Pracovním jazykem workspace - tedy `AGENTS.md`, knowledge base, prompty, plány i poznámky - by proto měla být **angličtina**.
>
> To nijak neomezuje, v jakém jazyce publikujete. Pokud píšete česky, napište to do pravidel jako kteroukoli jinou instrukci:
>
> ```
> - Always write published copy in Czech. Internal notes and planning: English.
> ```

---

Tahle sada učí marketingový, obsahový nebo provozní tým, jak používat AI
agenta - **Claude Code, OpenAI Codex CLI, opencode nebo pi** - na psaní,
plánování, rešerše a tvorbu kampaní.

Agent není ChatGPT v záložce prohlížeče. Běží na vašem počítači a zapisuje
skutečné soubory. Bez nainstalovaného agenta je zbytek k ničemu.
V sekci [Než začnete](HANDBOOK.cs.md#než-začnete) najdete, které čtyři nástroje
to jsou, jak si jeden nainstalovat a jak si za minutu ověříte, že opravdu
mluvíte s agentem. Zbytek sady učí to, na čem kvalita výstupu stojí nejvíc:
**co dáte do adresáře.**

> ### 📖 Čtěte online
>
> **https://lczerner.github.io/agents-handbook/**
>
> Příručka, cvičení i tahák s prompty na jedné stránce, česky i anglicky,
> s přepínačem jazyka. Je to stejný obsah jako v souborech tady - stránka se
> z nich generuje, takže se nemůže rozejít. Kolegům posílejte tenhle odkaz.

---

## Začněte tady

| Přečtěte si | Čas | Co z toho máte |
|---|---|---|
| **[Než začnete](HANDBOOK.cs.md#než-začnete)** | 5 min | Co je agent, co je harness, který nástroj si nainstalovat a minutové ověření, že ho máte. Začněte tímhle - všechno ostatní na tom stojí. |
| **[HANDBOOK.cs.md](HANDBOOK.cs.md)** | 40 min | Koncepty. `AGENTS.md`, plány a progress, knowledge base, skills, MCP. Sekce 1–8 přečtěte dřív, než začnete cokoli dělat. |
| **[WALKTHROUGHS.cs.md](WALKTHROUGHS.cs.md)** | Projděte je | Čtyři praktická cvičení. Příklady, na kterých si osaháte chování agenta, ideálně upravené podle toho, co chcete tvořit. |
| **[PROMPTS.cs.md](PROMPTS.cs.md)** | Mějte otevřené | Tahák s prompty. Popisky česky, samotné prompty anglicky - jsou k okopírování. |
| **[starter-kit/](starter-kit/)** | Prohlédněte si ho | Kompletní ukázkový workspace. Každý soubor vyplněný a funkční. Podívejte se na něj, až budete mít vlastní, a vezměte si z něj, co potřebujete. |

**Pokud máte deset minut:** přečtěte si [sekci 1 příručky](HANDBOOK.cs.md#1-jedna-myšlenka)
a pak krok 2 z prvního cvičení. To stačí na začátek.

---

## Myšlenka v jednom odstavci

Agent není chatbot. Běží uvnitř adresáře na vašem počítači, čte a zapisuje
soubory v něm, hledá na webu a používá vaše další nástroje. Zároveň **mezi
sezeními všechno zapomene**. Nejde o to psát chytré prompty, ale nechat mu
v adresáři správné věci. Pět druhů věcí: pravidla, která čte pokaždé
(`AGENTS.md`), referenční materiály, do kterých se podívá, když jsou potřeba
(`knowledge/`), plán a deník, aby dlouhá práce přežila i několik dní
(`PLAN.md`, `PROGRESS.md`), zapsané postupy, po kterých sáhne, když jim zadání
odpovídá (skills), a napojení na systémy mimo adresář (MCP).

---

## Co lidé dělají špatně

- **Vůbec si nepořídí agenta.** Čtou cvičení a prompty z nich vkládají do
  ChatGPT nebo Claude v prohlížeči. Dostanou věrohodné odpovědi a ani jeden
  soubor na svém počítači. Ověřte si to dřív, než začnete:
  [Než začnete](HANDBOOK.cs.md#než-začnete).
- **Chovají se k tomu jako k ChatGPT.** Chtějí text v chatovacím okně a kopírují
  si ho ven. Výstup má přistát v souboru, v projektovém adresáři, kde na něm
  můžete dál pracovat.
- **Přeskočí `AGENTS.md`.** A pak v každém sezení znovu vysvětlují styl.
- **Napíšou `AGENTS.md` na 900 řádků.** Delší soubory se dodržují *hůř*. Držte
  ho pod 200 řádky a detaily přesuňte do `knowledge/`.
- **Píšou vágní pravidla.** „Buď profesionální" se nedá dodržet. „Žádná věta nad
  25 slov" se zkontrolovat dá.
- **Zadají celou práci najednou.** Vyžádejte si plán, schvalte ho a pak nechte
  běžet jednu fázi po druhé.
- **Věří číslu, protože zní věrohodně.** Zkontrolujte každou statistiku, citaci,
  datum a jméno, které se dostane do publikovaného textu.

---

## Checklist pro první týden

- [ ] Nainstalujte si jeden ze čtyř nástrojů a ověřte si, že umí na vašem
      počítači vytvořit soubor ([Než začnete](HANDBOOK.cs.md#než-začnete))
- [ ] Vytvořte adresář workspace, který bude tým sdílet
- [ ] Napište `AGENTS.md` (Walkthrough 1 - nechte se od agenta vyzpovídat)
- [ ] Přidejte `CLAUDE.md` s obsahem `@AGENTS.md`, pokud někdo používá Claude Code
- [ ] Napište jeden channel file a jeden voice file
- [ ] Udělejte s tím jeden reálný kus práce (Walkthrough 2)
- [ ] Po něm se zeptejte: *„co jsem si měl zapsat a nezapsal?"*

Všechno ostatní - další kanály, entity files, skills, MCP konektory - přijde
později, až narazíte na konkrétní problém, který každá z těch věcí řeší.

---

## Poznámky

Dvě pravidla, která se nemění:

1. **Fakta si ověřte sami.** Mantinely v této sadě výmysly výrazně omezí.
   Neodstraní je.
2. **Bez člověka se nic nepublikuje.** Nechte to pravidlo v `AGENTS.md` a nechte
   ho platit - zvlášť až připojíte nástroje, které by to technicky uměly.

---

## Zdroje

Psáno v srpnu 2026 podle aktuální dokumentace:

- [AGENTS.md](https://agents.md/) - otevřený standard, dnes pod Agentic AI
  Foundation při Linux Foundation
- [Agent Skills specification](https://agentskills.io/specification) - formát
  `SKILL.md`, podporovaný 40+ nástroji
- [Claude Code: quickstart](https://code.claude.com/docs/en/quickstart) ·
  [memory](https://code.claude.com/docs/en/memory) ·
  [skills](https://code.claude.com/docs/en/skills) ·
  [MCP](https://code.claude.com/docs/en/mcp)
- [Codex: quickstart](https://learn.chatgpt.com/docs/codex/cli) ·
  [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) ·
  [skills](https://learn.chatgpt.com/docs/build-skills)
- [opencode: dokumentace](https://opencode.ai/docs/) ·
  [rules](https://opencode.ai/docs/rules/)
- [pi: coding agent docs](https://github.com/earendil-works/pi)
- [Model Context Protocol](https://modelcontextprotocol.io/)

Detaily nástrojů se mění rychle. Pokud nějaká cesta k souboru
v [Příloze A](HANDBOOK.cs.md#příloha-a--který-soubor-čte-můj-nástroj) nefunguje,
podívejte se do aktuální dokumentace svého nástroje - koncepty platí dál.

---

## Licence

Copyright 2026, Lukáš Czerner <lukas@czerner.cz>

Příručka, cvičení a tahák s prompty - a stránka i PDF, které z nich vznikly -
jsou pod licencí
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.cs). Používejte je,
překládejte, upravujte, klidně i jako podklad pro vlastní školení, a klidně
komerčně. Tři podmínky: uveďte mě jako autora, odkažte na licenci a napište,
jestli jste něco změnili.

Dva adresáře to mají jinak, a to záměrně:

- `starter-kit/` je [CC0](starter-kit/LICENSE), tedy volné dílo. Je určený
  k tomu, abyste si ho zkopírovali a smyšlenou firmu z něj vyhodili - nemá
  smysl, aby soubory, které jste si celé přepsali, nesly moje jméno.
- `web/` je [MIT](web/LICENSE). Je to kód a licence psaná pro text o něm nic
  užitečného neříká.

Plné znění je v souboru [LICENSE](LICENSE).
