<!--
SPDX-FileCopyrightText: Copyright 2026, Lukáš Czerner <lukas@czerner.cz>
SPDX-License-Identifier: CC-BY-4.0
-->

# Walkthroughs

### Čtyři cvičení, která na sebe navazují

---

> **⚠️ Toto je český překlad.** Závazný je anglický originál:
> [WALKTHROUGHS.md](WALKTHROUGHS.md). Překlad má jediný účel - rychlejší
> pochopení. Pak pracujte anglicky.
>
> **Všechno v blocích `>` je text, který napíšete agentovi, a je schválně
> anglicky.** Neposílejte agentovi český překlad promptu - jazykové modely
> dodržují instrukce v angličtině spolehlivěji. Stejně tak zůstávají anglicky
> názvy souborů, adresářů a odborné termíny.

---

> **Jsou to cvičení, ne návod.** Není to návod na tvorbu článků ani
> marketingových kampaní. Jde pouze o příklady, které nemusí souviset s vaší
> prací, ale dají vám možnost si osahat chování agenta a ukážou vám některé
> možnosti přizpůsobení.
>
> Fantazii se meze nekladou - ideálně si zadání upravte podle toho, co chcete
> tvořit, ale dodržte myšlenku cvičení.

Cvičení dělejte v pořadí, ideálně na něčem, co chcete opravdu vytvořit. Všechno
v `blocích kódu` je soubor nebo příkaz do terminálu.

| # | Walkthrough | Čas | Co z toho máte |
|---|---|---|---|
| 1 | [Nastavení workspace](#walkthrough-1--nastavení-workspace) | 60 min | Reálný `AGENTS.md` a čtyři knowledge soubory |
| 2 | [Napsat článek](#walkthrough-2--napsat-článek) | 90 min | Draft připravený k publikaci a voice guide odvozený z vaší vlastní práce |
| 3 | [Naplánovat kampaň](#walkthrough-3--naplánovat-mediální-kampaň) | 3 sezení za 2 dny | Kompletní multikanálový plán kampaně, postavený napříč sezeními |
| 4 | [Udělat z toho skill](#walkthrough-4--udělat-z-opakované-práce-skill) | 30 min | Znovupoužitelný postup, který spustíte jedním slovem |

**Než začnete, potřebujete agenta.** Ne ChatGPT nebo Claude v prohlížeči - ty
na vašem počítači nevytvoří jediný soubor a každé cvičení tady končí souborem.
Claude Code, OpenAI Codex CLI, opencode nebo pi, nainstalovaný, a k tomu
terminál, který umíte otevřít v adresáři a spustit ho z něj. Pokud vám ta věta
dělá potíže, přečtěte si v příručce
[Než začnete](HANDBOOK.cs.md#než-začnete) a požádejte toho, kdo vám to
instaloval, ať s vámi stráví prvních deset minut prvního cvičení.

---

<a id="walkthrough-1--nastavení-workspace"></a>
## Walkthrough 1 - Nastavení workspace

**Cíl:** adresář s pravidly, který agent dodržuje, a dost znalostí na to,
aby napsal něco, co zní jako vy.
**Čas:** zhruba hodina.

### Krok 1 - Vytvořte adresář

Vytvořte nový adresář někde rozumně - `Documents/content-workspace` stačí.
Otevřete v něm terminál a spusťte agenta (`claude`, `codex`,
`opencode` nebo `pi`).

Pak si ověřte, že opravdu vidí soubory a umí je zapisovat:

> Create a directory called `knowledge` with subdirectories `channels`, `voice`, `entities`, and `library`. Also create a directory called `projects`. Then show me the directory structure.

Adresáře by se měly objevit na disku. Pokud si řekne o svolení k vytvoření
souborů, dejte mu ho. **V tomhle je celý trik: nechcete po něm text, chcete po něm
změny v adresáři.**

**Pokud se na disku neobjevilo nic, zastavte se tady.** Odpověď, která ty
adresáře popisuje, není totéž jako adresáře, které existují. Ověřte si to ve
Finderu nebo v Průzkumníku souborů, ne v odpovědi. Pokud tam nejsou, nemáte
spuštěného agenta - vraťte se na
[Než začnete](HANDBOOK.cs.md#než-začnete).

### Krok 2 - Nechte se vyzpovídat

Nepište `AGENTS.md` sami od začátku. Napište tohle:

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

Pak odpovídejte upřímně a v krátkých větách. Nesnažte se to uhladit - tohle je
surový vstup, ne dokument.

**Kde to lidé kazí:** vágními odpověďmi. „Jsme profesionální, ale přátelští" je
k ničemu. „Zníme jako stavbyvedoucí, který něco vysvětluje kolegovi, nikdy jako
dodavatel" ušetří později hodinu editace. Když se zeptá na slova, která
nesnášíte, opravdu jich vyjmenujte deset.

> **Pozn. k jazyku:** odpovídat můžete česky, agent si poradí. Ale trvejte na tom,
> aby výsledný `AGENTS.md` napsal anglicky. Přidejte si na konec promptu:
> *„Write the resulting file in English."*

### Krok 3 - Vezměte si draft a převezměte ho

> Now write `AGENTS.md` based on my answers. Use these sections in this order:
> What this is · Who we write for · Where things live · Guardrails (Never / Always / Ask me first) · How we work · Definition of done · How to talk to me.
>
> Keep it under 150 lines. Make every rule specific enough that I could check whether you followed it - no "write well", no "be professional".

Teď si to **sami přečtěte a ručně upravte.** Otevřete soubor v libovolném editoru.
Tohle je váš soubor, ne agentův. Zkontrolujte tři věci:

1. **Dá se každé pravidlo zkontrolovat?** Smažte nebo lépe specifikujte cokoli,
   co byste neuměli ověřit.
2. **Neodporuje si něco?** „Piš stručně" plus „cíl 1 800 slov" je hod mincí.
   Vyberte jedno.
3. **Je seznam „Never" úplný?** Doplňte věci, které by vám opravdu způsobily
   problém: vymýšlení statistik, jmenování konkurence, tvrzení o produktu, které
   neplatí, publikování čehokoli.

Ať už tam bude cokoli dalšího, tyhle dva řádky tam musí být:

```markdown
- Never invent a statistic, quote, customer name, or case study. If you need
  one and don't have a source, write [NEEDS SOURCE: what you need] and continue.
- Never publish, post, send, or schedule anything. You draft, a human ships.
```

### Krok 4 - Pokud používáte Claude Code, přidejte ještě jeden soubor

Claude Code čte `CLAUDE.md`, ne `AGENTS.md`. Vyžádejte si ho:

> Create a `CLAUDE.md` in the project root containing exactly one line: `@AGENTS.md`

Teď oba pracují ze stejného zdroje a vy neudržujete dva soubory. (Codex, opencode
a pi čtou `AGENTS.md` přímo - tam není co dělat.)

### Krok 5 - První channel file

Vyberte kanál, na který publikujete nejvíc.

> Interview me about our blog, one question at a time, so you can write a channel file. Ask about: its purpose, who arrives there and why, format and length, structure rules, SEO rules, what we never do on this channel, and which past pieces are good examples.
>
> Then write it to `knowledge/channels/blog.md`.

### Krok 6 - Voice file

Pokud už máte publikované texty, použijte je - výsledek je mnohem lepší než
popis vašeho stylu z paměti:

> I'm going to put five of our best published articles in `knowledge/library/articles/`. Read all of them, then write `knowledge/voice/house-voice.md` containing:
> - our voice in one sentence
> - concrete rules (sentence length, person, tense, paragraph length)
> - **at least ten "do this, not that" pairs using real sentences from those articles**
> - a banned words list of anything that would sound wrong in our voice
> - punctuation conventions you can see us following
>
> Base it only on what's actually in the articles. Don't invent rules that sound good.

(Články do toho adresáře nejdřív zkopírujte - jako `.md` nebo `.txt`.)

Pokud ještě nemáte nic publikovaného, nechte se místo toho vyzpovídat a trvejte
na těch dvojicích „do this, not that".

> **Pozn.:** pokud publikujete česky, voice file bude přirozeně obsahovat české
> ukázkové věty - to je v pořádku a je to nutné. Pravidla a struktura souboru
> ale zůstávají anglicky.

### Krok 7 - Product fact sheet

Voice file hlídá, aby agent zněl jako vy. Tenhle hlídá, aby si o vašem produktu
nic nevymýšlel.

> Interview me about our main product, one question at a time, then write `knowledge/entities/products.md`. Ask about: what it does, **what it explicitly does not do**, the claims we're allowed to make and where each one comes from, the claims we must never make, pricing, and our approved boilerplate description.
>
> Put `Last verified: <today's date>` at the top of the file.

Nejvíc se vyplatí ta část o tom, co produkt nedělá. Zeptejte se na něco, co ve
vašich souborech není, a agent tu mezeru zaplní něčím, co si vymyslí. Čte se to
úplně stejně dobře, jako kdyby to byla pravda. Proto si toho nejspíš ani
nevšimnete.

Walkthrough 2 agentovi říká, ať nepoužívá žádné tvrzení o produktu, které v tomhle
souboru není.

### Krok 8 - Napište index

Pro pouhé čtyři soubory index vlastně nepotřebujete. Raději to ale vytvořte -
buď teď, nebo až jich bude třicet a přestanete si pamatovat, co je v kterém.

> Write `knowledge/INDEX.md`. One line per file: what's in it, and **when you should read it**. Keep the whole thing under a screen.

Práci odvádí ta druhá půlka - *kdy ho číst*. Agent nejdříve přečte index a otevře
jen to, co potřebuje, místo aby pokaždé četl celý adresář. Ušetří vám to kontext.

Kdykoli přidáte do `knowledge/` soubor, přidejte sem řádek.

### Krok 9 - Ověřte, že to celé funguje

Nové sezení (v Claude Code napište `/clear`). Pak:

> Read `AGENTS.md` and everything in `knowledge/`. Then write me a 150-word LinkedIn post announcing that we've published a new guide about [any topic you actually cover].
>
> After you write it, audit your own post against `knowledge/voice/house-voice.md`, rule by rule, with ✅ or ❌ and a fix for each ❌.

Přečtěte si výstup. Nebude dokonalý. O to jde - **cokoli je na něm špatně, přesně
vám ukazuje, kterému souboru něco chybí.**

Pak uzavřete smyčku:

> The tone is off in the second paragraph - it sounds like a press release, and we never do that. Add a rule to the right file so this doesn't happen again, and tell me which file you chose and why.

**✅ Hotovo, když** máte `AGENTS.md`, jeden channel file, voice file, product fact
sheet, index a viděli jste agenta dodržet pravidlo, které jste napsali.

---

<a id="walkthrough-2--napsat-článek"></a>
## Walkthrough 2 - Napsat článek

**Cíl:** draft připravený k publikaci, vytvořený po fázích, kde jste v každém
kroku editorem vy.
**Čas:** zhruba 90 minut.
**Potřebuje:** dokončený Walkthrough 1.

### Krok 1 - Založte projekt

> Create `projects/2026-08-guide-article/` with a `drafts/` subdirectory. In it, create `BRIEF.md` and interview me to fill it in: what we're writing, for which channel, target reader, the one thing they should take away, target length, deadline, and what success looks like.

Brief je základ celé práce. Dejte si na něm záležet.

### Krok 2 - Úhly pohledu, ne draft

> Read `BRIEF.md`, the channel file, and `knowledge/voice/house-voice.md`.
>
> If there's anything in `knowledge/library/articles/`, search it for what we've already published on this topic and tell me what you found. If that directory is empty, say so and move on.
>
> Then give me **three angles** for this piece. For each: the promise to the reader in one sentence, why we're credible on it, and what evidence we'd need to make it stand up.
>
> Do not write the article. Recommend one angle and say why.

Jeden si vyberte. Když není dobrý ani jeden, zatlačte:
*„None of these. The interesting thing is X. Give me three angles on that."*
Dvě kola tady jsou lepší než opravovat hotový draft.

### Krok 3 - Podklady dřív než text

> Angle 2, please. Now collect the evidence.
>
> Search the web for supporting data. For every source: the link, the publication date, and the exact claim it supports. Prefer primary sources - original research, official statistics, named studies. Skip anything you can't date.
>
> Pull the approved product claims from `knowledge/entities/products.md`. Do not use any product claim that isn't in that file.
>
> Save it all to `research.md` in the project directory. Anything we need but can't source, list as `[NEEDS SOURCE: ...]`.

A teď krok, který lidé přeskakují: **otevřete `research.md` a proklikněte dva
odkazy.** Ověřujete, jestli jsou zdroje skutečné a jestli říkají to, co agent
tvrdí. Dělejte to první měsíc pokaždé. Zkalibruje vám to důvěru a budete vědět,
kde přesně jsou slabá místa.

### Krok 4 - Osnova

> Write an outline: H2 headings, one line under each on what that section does for the reader, plus **the opening paragraph written out in full**.
>
> Follow the structure rules in the channel file. Don't draft the rest.

Celý úvodní odstavec je tam záměrně. Právě v něm žije styl a teď nic nestojí
ho předělat. Když sedí úvod, zbytek textu obvykle sedí taky.

### Krok 5 - Draft

> Good. Write the full draft to `drafts/<slug>.md`, following the outline and the channel format rules.

Pak ho nechte být. Ještě si ho nečtěte - další krok opraví polovinu věcí, které
byste komentovali.

### Krok 6 - Ať si to zkontroluje samo

> Now audit your own draft against `knowledge/voice/house-voice.md` and the channel file.
>
> Produce a table: each rule, ✅ or ❌, and the specific fix for each ❌. Check especially: banned words, sentences over 25 words, paragraphs over three sentences, passive voice, em dashes, and any claim without a source.
>
> Be genuinely critical. A review that finds nothing is a review you didn't do.
>
> Then apply every fix to the file and tell me what you changed.

Tenhle krok přináší konzistentně větší zlepšení než jakékoli přepisování promptu.
Psát a hodnotit jsou dvě různé práce. Dělat je odděleně funguje líp než dohromady.

### Krok 7 - Teď to přečtete vy

Otevřete draft. Editujte jako editor, ne jako zadavatel promptů - chtějte
chirurgické zásahy, přímo v souboru:

> In the draft file: cut the third section entirely, it repeats section one. Tighten the intro to four sentences. Leave everything else exactly as it is.

Všimněte si té poslední věty. Bez ní občas dostanete kompletní přepis a přijdete
o části, které se vám líbily.

Pak tvrdší průchod:

> Read the draft as our most skeptical reader - an ops manager who's been sold bad software before. List every sentence they'd roll their eyes at, and why. Don't fix anything yet.

### Krok 8 - Zabalte to

> Add to the top of the draft file: three headline options, a meta description under 155 characters, a suggested slug, and two internal links from `knowledge/library/articles/` if there's anything there to link to.
>
> Add at the bottom: an image brief, and every `[NEEDS SOURCE]` marker collected into one list.
>
> Then tell me in three lines: what's done, where it is, what you need from me.

### Krok 9 - Uložte si, co jste se naučili

> Which corrections did I make today that you should have got right the first time? For each, tell me which file should have prevented it, and make the edit.

Dělejte to první měsíc po každém kusu práce. Právě takhle se workspace zlepšuje.

**✅ Hotovo, když** draft je uložený v adresáři, každý zdroj je ověřený a aspoň
jedno pravidlo přibylo do některého souboru kvůli tomu, co se dnes pokazilo.

---

<a id="walkthrough-3--naplánovat-mediální-kampaň"></a>
## Walkthrough 3 - Naplánovat mediální kampaň

**Cíl:** kompletní multikanálový plán kampaně, postavený ve třech oddělených
sezeních, který ověří systém plán / fáze / deník.
**Čas:** tři sezení po ~45 minutách, ideálně v různé dny.
**Potřebuje:** Walkthrough 1–2.

Tohle cvičení je záměrně rozložené do dnů. Jde o to vidět, jak agent naváže jen
podle deníku - dovednost, která teprve umožňuje dlouhé projekty.

### Sezení 1 - Brief a plán

**Krok 1.** Založení:

> Create `projects/2026-09-atlas-launch/` with `drafts/` and `research/` subdirectories.
>
> Create `BRIEF.md` and interview me one question at a time: what we're launching, the date, the audience, the one message, which channels, budget, who's involved, what success looks like in numbers, and any hard constraints (embargoes, legal, approvals).

**Krok 2.** Vyžádejte si plán a nic jiného:

> Read `BRIEF.md`, `knowledge/INDEX.md`, and the channel file for every channel in the brief that has one. Tell me which channels in the brief have no channel file yet.
>
> Write a phased plan to `PLAN.md`. **Do not produce any campaign content.**
>
> 5–7 phases. For each: goal in one sentence, inputs needed, files produced, and how we'll know it's done. Every phase must be small enough to finish in one sitting. At least two phases must end with a decision I have to make.
>
> At the end, list your assumptions and anything the brief doesn't answer.

**Krok 3.** Pořádně si plán přečtěte. Tohle je vaše hlavní příležitost dát tomu
směr. Typické opravy:

> Three changes. Phase 2 is too big - split it into messaging and calendar. Move the press list to Phase 1, we need it earlier for embargoes. And add a phase for the sales enablement one-pager, I forgot it in the brief. Update `PLAN.md` and `BRIEF.md`.

**Krok 4.** Udělejte přesně jednu fázi:

> Now do Phase 1 only. Stop when it's done.

**Krok 5.** Uzavřete sezení - tenhle krok je celé cvičení:

> Stop here. Create `PROGRESS.md` with:
>
> **Status** - current phase, the single next action, anything you're blocked on
> **Decisions made** - dated, with the reason for each
> **Log** - what you did today, which files you produced, what you learned, open questions
>
> Write it so someone who wasn't here today could pick this up cold with no other context.

Pak nástroj zavřete.

### Sezení 2 - Studený start

**Krok 6.** Nový den, nové sezení. Napište jenom tohle:

> Read `PROGRESS.md` and `PLAN.md` in `projects/2026-09-atlas-launch/`. Tell me in five lines where we are and what the next action is. Don't start work yet.

Sledujte, co se stane. Agent vám přesně řekne, kde jste skončili, včetně důvodů,
proč jste se rozhodli tak, jak jste se rozhodli. **V tuhle chvíli to celé zapadne.**
Žádné vysvětlování znovu, žádné rolování zpátky v chatu.

Pokud je zmatený nebo vágní, je to diagnóza: `PROGRESS.md` nebyl dost konkrétní.
Opravte formát deníku hned teď, dokud je zjevné, co v něm chybělo.

**Krok 7.** Pokračujte:

> Correct. Do Phase 2 only, then stop.

**Krok 8.** Stejný závěrečný rituál. Pokaždé:

> Stop here. Update `PROGRESS.md` - status, next action, decisions with reasons, and today's log entry. Keep the whole file under 100 lines by summarising older entries.

### Sezení 3 - Dokončit a zabalit

**Krok 9.** Zase studený start, pak projděte zbývající fáze - pořád po jedné,
pořád s deníkem na konci každé.

**Krok 10.** Až je plán hotový:

> The plan is finished. Produce `CAMPAIGN.md` in the project root: the full campaign on one page - messaging spine, channel-by-channel calendar with dates, the asset list with file paths and owners, dependencies and deadlines, and how we'll measure it.
>
> Then list everything still blocked on a human, and who needs to do what.

**Krok 11.** Prověřte to natvrdo, dřív než to uvidí kdokoli další:

> Now be our CFO reading this for the first time. What are the three weakest points? What would you refuse to approve and why?

**Krok 12.** Uložte si poznatky:

> What did we learn about how we plan campaigns that isn't written down anywhere? Propose additions to `AGENTS.md` or a new knowledge file. Show me the changes before making them.

**✅ Hotovo, když** jste zažili aspoň jeden studený start, který fungoval, a
`CAMPAIGN.md` je něco, co byste opravdu poslali kolegovi.

---

<a id="walkthrough-4--udělat-z-opakované-práce-skill"></a>
## Walkthrough 4 - Udělat z opakované práce skill

**Cíl:** postup z cvičení Walkthrough 2 se změní v něco, co spustíte jedním slovem a co
funguje stejně všem v týmu.
**Čas:** 30 minut.
**Potřebuje:** Walkthrough 2 - ten postup musíte mít jednou projitý ručně.

### Krok 1 - Najděte správný adresář

Podle nástroje (viz Příloha A v příručce):

| Nástroj | Adresář |
|---|---|
| Claude Code | `.claude/skills/` |
| Codex CLI | `.agents/skills/` |
| opencode | `.opencode/skills/` |
| pi | `.pi/skills/` nebo `.agents/skills/` |

V promptu v dalším kroku je `<skills directory>`. Než ho odešlete, dosaďte tam
řádek pro svůj nástroj z téhle tabulky.

### Krok 2 - Nechte ho napsat skill z toho, co jste opravdu dělali

> Look back at how we produced the article in `projects/2026-08-guide-article/`, including every correction I made along the way.
>
> Turn that into a skill at `<skills directory>/article-draft/SKILL.md`.
>
> Requirements:
> - YAML frontmatter with `name: article-draft` and a `description` that says what it does **and when to use it**, using words I'd actually type - write, draft, article, blog post, outline, newsletter.
> - The body is the procedure, in numbered phases.
> - Mark with ⏸ every point where you must stop and wait for me.
> - Include the self-review phase where you audit your own draft against the voice file with ✅/❌ and fix every ❌.
> - Include every correction I made during the walkthrough as an explicit rule.
> - Under 200 lines. Push anything long into `references/`.

### Krok 3 - Zkontrolujte description

Otevřete `SKILL.md` a podívejte se na řádek `description`. Je to jediná část,
kterou agent vidí, dokud se nerozhodne skill otevřít - takže musí obsahovat slova,
která byste přirozeně použili.

❌ `description: Helps with writing articles.`
✅ `description: Produce a publish-ready article draft from a brief, following our channel and voice rules. Use when asked to write, draft, or outline a blog post, article, or newsletter piece.`

Zkontrolujte taky, že `name` je malými písmeny s pomlčkami a **přesně odpovídá
názvu adresáře**. To je nejčastější důvod, proč se skill tiše nenačte.

### Krok 4 - Otestujte to oběma způsoby

**Přímo** - nové sezení, pak napište `/article-draft` (Claude Code) nebo
`$article-draft` (Codex). V opencode na to příkaz není: napište místo toho
`use the article-draft skill`. Měl by začít fází 1.

**Automaticky** - nové sezení, pak napište něco přirozeného:

> I need a blog post about how site diaries actually get filled in.

Pokud je skill napsaný dobře, začne postup dodržovat, aniž byste mu to řekli.
Pokud ne, problém je v `description` - přepište ho slovy, která jste právě použili.

### Krok 5 - A teď postavte zbytek

Stejný postup, v pořadí podle přínosu:

- **`style-check`** - projde libovolný text proti vašim voice souborům, řádek po
  řádku, s opravami. Pusťte ho i na texty psané člověkem.
- **`campaign-plan`** - postup z cvičení Walkthrough 3.
- **`repurpose`** - jeden článek na newsletter, pět LinkedIn postů a Instagram
  carousel, každý ve stylu svého kanálu.
- **`brief-intake`** - odmítne pokračovat na vágním zadání, dokud z něj není
  skutečný brief.

Nikdy nepište skill z hlavy. **Projděte si práci jednou ručně, poznamenejte si
každou opravu a pak nechte agenta napsat skill podle toho, co se stalo.**
Skills psané z hlavy popisují, jak byste si přáli pracovat. Skills psané ze
skutečného sezení popisují, jak pracujete doopravdy, včetně těch oprav - a v
těch opravách je většina hodnoty.

**✅ Hotovo, když** napíšete jedno slovo a proběhne vícekrokový postup přesně tak,
jak byste ho udělali vy.

---

## Co dělat dál

Teď máte celý systém. Návyk, který ho udržuje funkční, je jediná otázka na konci
každého kusu práce:

> What did I correct today that you should have known already - and which file should have told you?

Ptejte se tak měsíc pokaždé. Workspace se sám naučí vaši práci.

### Když si chcete prohlédnout hotový workspace

[`starter-kit/`](starter-kit/) je kompletní workspace vymyšlené firmy Lighthouse.
Každý soubor v něm je vyplněný, včetně těch, které jste ve cvičeních nepsali:
soubor o lidech se zájmeny a s tím, kdo smí být citován, soubor o akcích se
stavem embarga, seznam nejlepších textů, druhý voice file pro konkrétního autora.

Prohlédněte si, jak takové soubory vypadají, a až některý z nich budete
potřebovat, vezměte si ho. Nekopírujte ale celý adresář přes workspace, který
jste právě postavili. Odpovědi v něm jsou Lighthouse, ne vaše.
