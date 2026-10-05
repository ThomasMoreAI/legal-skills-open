---
name: prehled-pravni-grow-lead-agency
title: /prehled-pravni -- Přehled pro právní tým
description: Generování kontextových přehledů pro právní práci — denní přehled, tematická rešerše nebo reakce na incident. Použijte na začátku dne, když potřebujete skenování právně relevantních položek napříč e-mailem, kalendářem a smlouvami, při rešerši konkrétní právní otázky v interních zdrojích, nebo když vyvíjející se situace (únik dat, hrozba soudního sporu, regulatorní dotaz) vyžaduje rychlý kontext.
author: grow-lead-agency
author_url: https://github.com/grow-lead-agency/ak-sladek/tree/master/skills/prehled-pravni
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cz
practice: general
language: cs
---

# /prehled-pravni -- Přehled pro právní tým

> Pokud narazíte na neznámé zástupné symboly nebo si potřebujete ověřit, které nástroje jsou připojené, podívejte se na [CONNECTORS.md](../../CONNECTORS.md).

Generuje kontextové přehledy pro právní práci. Podporuje tři režimy: denní přehled, tematický přehled a krizový přehled.

**Důležité**: Tento plugin pomáhá s právními workflow, ale neposkytuje právní poradenství ve smyslu zákona č. 85/1996 Sb. o advokacii. Veškeré závěry ověřte u kvalifikovaného advokáta.

## Jak používat (pro uživatele)

Vyvolej skill `/prehled-pravni` v jednom ze tří režimů. AI provede:

1. **Denní přehled** (`daily`) — ranní souhrn právně relevantních položek napříč e-mailem, kalendářem, chatem, CLM a úložištěm dokumentů. Zvýrazní urgentní, blížící se termíny, dnešní jednání vyžadující právní přípravu.
2. **Tematický přehled** (`topic <dotaz>`) — rešerše konkrétní právní otázky v interních zdrojích plus aktuální judikatura, zákony a regulatorika z DirectCase. Strukturovaný výstup se shrnutím, pozadím, interním precedentem a doporučenými kroky.
3. **Krizový přehled** (`incident <téma>`) — rychlý přehled pro vyvíjející se situaci (únik dat, hrozba sporu, regulatorní dotaz). Časová osa, okamžité právní úvahy, oznamovací lhůty, doporučené kroky.

> ⚙ Sekce s technickými detaily (názvy nástrojů DirectCase) jsou ve zbytku skillu označené poznámkou „Pro AI agenta". Při čtení skillu jako uživatel je můžete přeskočit.

## Krok 0 — startovací kontrola DirectCase konektoru

V tematickém a krizovém režimu může být užitečné prohledat i externí autoritativní zdroje (judikatura, zákony, regulatorika). Před zahájením zjisti stav **DirectCase konektoru** a zeptej se uživatele, zda ho má použít.

**Postup:**

1. Zjisti stav DirectCase konektoru. Pokud konektor není připojený nebo je v této konverzaci vypnutý, zobraz uživateli kartu pro jeho povolení.
2. Polož uživateli otázku: *„Pro tematický / krizový přehled — chcete, abych přes DirectCase doplnil aktuální judikaturu, zákonná ustanovení a regulatorní stanoviska k tématu?"*
3. Postupuj podle odpovědi:
   - **Ano + konektor aktivní** → DirectCase aktivně použij v sekci tematického přehledu níže; citace doplň o sp. zn. / ECLI / č. Sb.
   - **Ano + konektor není aktivní** → počkej, dokud uživatel konektor nepovolí nebo nenapíše „pokračuj".
   - **Ne** → pokračuj jen s interními zdroji a v přehledu jasně uveď, že externí právní zdroje nebyly prohledány.

V denním režimu se DirectCase obvykle nepoužívá — jde o souhrn z interních systémů. Krok 0 přeskoč pouze tehdy, byl-li už proveden v této konverzaci.

> ⚙ **Pro AI agenta:** Stav konektoru zjisti přes `mcp__mcp-registry__search_mcp_registry` s klíčovými slovy `["directcase", "judikatura", "czech law"]` a najdi záznam „DirectCase CZ". Pokud `connected: true` + `enabledInChat: false`, zavolej `mcp__mcp-registry__suggest_connectors` s `directoryUuid` z výsledku. Otázku uživateli pokládej přes `AskUserQuestion`. Pro spolehlivé ověření, že DirectCase je skutečně dostupný a jaký má tier, lze přímo zavolat nástroj `get_entitlements` — je vždy dostupný a nezávisí na stavu registru konektorů. Plné znění technického postupu viz [SKILL.md → Krok 0](SKILL.md).

## Spuštění

```
/prehled-pravni daily              # Ranní přehled právně relevantních položek
/prehled-pravni topic [dotaz]      # Rešerše ke konkrétní právní otázce
/prehled-pravni incident [téma]    # Rychlý přehled k vyvíjející se situaci
```

Pokud není režim zadán, zeptejte se uživatele, jaký typ přehledu potřebuje.

## Režimy

---

### Denní přehled

Ranní souhrn všeho, co člen právního týmu potřebuje vědět, aby mohl zahájit svůj den.

#### Zdroje ke skenování

Zkontrolujte každý připojený zdroj pro právně relevantní položky:

**E-mail (pokud je připojen):**
- Nové žádosti o smlouvy nebo jejich revizi
- Compliance dotazy nebo hlášení
- Odpovědi protistran v aktivních jednáních
- Označené nebo urgentní položky z e-mailové schránky právního oddělení
- Komunikace s externími právníky
- Newslettery o regulatorních nebo právních novinkách

**Kalendář (pokud je připojen):**
- Dnešní jednání, která vyžadují právní přípravu (zasedání představenstva, revize transakcí, jednání s dodavateli)
- Blížící se termíny tento týden (expirace smluv, procesní lhůty, lhůty pro odpověď)
- Pravidelné porady právního týmu

**Chat (pokud je připojen):**
- Noční zprávy v kanálech právního týmu
- Přímé zprávy s žádostí o právní vstup
- Zmínky o právně relevantních tématech (smlouva, compliance, ochrana údajů, NDA, podmínky)
- Eskalace nebo urgentní žádosti

**CLM (pokud je připojen):**
- Smlouvy čekající na revizi nebo podpis
- Blížící se data expirace (příštích 30 dní)
- Nově podepsané smlouvy

**CRM (pokud je připojen):**
- Obchodní případy postupující do fází, které vyžadují zapojení právního oddělení
- Nové příležitosti označené k právní revizi

#### Formát výstupu

```
## Denní právní přehled -- [Datum]

### Urgentní / Vyžaduje akci
[Položky vyžadující okamžitou pozornost, seřazeno dle naléhavosti]

### Stav smluv
- **Čekají na vaši revizi**: [počet a seznam]
- **Čekají na odpověď protistrany**: [počet a seznam]
- **Blížící se termíny**: [položky tento týden]

### Nové žádosti
[Žádosti o revizi smluv, žádosti o NDA, compliance dotazy obdržené od posledního přehledu]

### Dnešní kalendář
[Jednání s právní relevancí a jaká příprava je potřeba]

### Aktivita týmu
[Klíčové zprávy nebo aktualizace z kanálů právního týmu]

### Termíny tohoto týdne
[Blížící se termíny a lhůty pro podání]

### Nedostupné zdroje
[Zdroje, které nebyly připojeny nebo vrátily chybu]
```

---

### Tematický přehled

Rešerše a přehled ke konkrétní právní otázce nebo tématu napříč dostupnými zdroji.

#### Postup

1. Převezměte tematický dotaz od uživatele
2. Vyhledávejte napříč připojenými zdroji:
   - **Dokumenty**: Interní memoranda, dřívější analýzy, playbooky, vzorová dokumentace
   - **E-mail**: Předchozí komunikace k tématu
   - **Chat**: Diskuse týmu k tématu
   - **CLM**: Související smlouvy nebo ustanovení
   - **DirectCase MCP (externí právní zdroje ČR/EU)** — viz níže
3. Syntetizujte zjištění do strukturovaného přehledu

#### Externí rešerše přes DirectCase

Pokud je v Kroku 0 potvrzeno použití DirectCase, využij jej pro **autoritativní právní zdroje** mimo interní systémy. To je často klíčové, protože interní memoranda a playbooky nemusejí reflektovat aktuální právní stav.

**Co DirectCase dodá do tematického přehledu:**

- **Judikatura k tématu** — relevantní rozhodnutí NS, ÚS, NSS, vrchních a krajských soudů. Pro pochopení, jak soudy konzistentně dané otázce přistupují.
- **Aktuální znění zákonů a podzákonných předpisů** — včetně novel, které mohly změnit interní pozici.
- **Regulatorní dokumenty** — stanoviska ČNB, ÚOOÚ, ÚOHS a dalších dozorových orgánů.
- **Plný text konkrétních ustanovení nebo rozhodnutí** pro přesnou citaci.

**Pravidlo: každý DirectCase parallel search nástroj lze v rámci jednoho tematického přehledu (konverzace) zavolat jen JEDNOU.** Nástroj bere pole `queries[]` — formuluj dotazy komplexně a spojuj je do jednoho volání.

Výsledky cituj pomocí identifikátorů (sp. zn., ECLI, č. Sb. + datum) v sekcích přehledu.

> ⚙ **Pro AI agenta — konkrétní nástroje DirectCase:** `search_caselaw_parallel` (judikatura NS, ÚS, NSS, vrchních a krajských soudů), `search_law_parallel` (zákony a předpisy), `search_regulatory_parallel` (regulatorní dokumenty ČNB, ÚOOÚ, ÚOHS), `search_keyword` (klíčové vyhledávání napříč celou databází ~1,4 M zdrojů), `search_similar` (dokumenty podobné klíčovému nálezu), `get_document` / `get_law_detail` (plný text). Parallel nástroje = **1× za konverzaci**, víc dotazů slouč do pole `queries[]`. **Rate limit:** Basic (free) = 20 volání/nástroj celkem, Pro = 25/den (AI search), 200/den (lehké nástroje). Pro follow-up dotazy preferuj `search_keyword` / `search_similar` místo dalšího parallel search volání.

#### Formát výstupu

```
## Tematický přehled: [Téma]

### Shrnutí
[2-3 věty výkonného shrnutí zjištění]

### Pozadí
[Kontext a historie z interních zdrojů]

### Aktuální stav
[Jaká je současná pozice nebo přístup organizace na základě dostupných dokumentů]

### Klíčové úvahy
[Důležité faktory, rizika nebo otevřené otázky]

### Interní precedens
[Dřívější rozhodnutí, memoranda nebo pozice nalezené v interních zdrojích]

### Mezery
[Jaké informace chybí nebo které zdroje nebyly dostupné]

### Doporučené další kroky
[Co by měl uživatel s těmito informacemi udělat]
```

#### Důležité poznámky
- Tematické přehledy syntetizují to, co je dostupné v připojených zdrojích; nenahrazují formální právní rešerši
- Pro aktuální právní autoritu a judikaturu využívej **DirectCase MCP** (cca 1,4 M ověřených českých a EU zdrojů — judikatura, zákony, regulatorika, obchodní rejstřík). Pokud není připojen, informuj uživatele a doporuč jeho připojení; pro vysoce rizikové otázky doporuč konzultaci s kvalifikovaným advokátem
- Vždy uveďte omezení prohledávaných zdrojů

---

### Krizový přehled

Rychlé informace pro vyvíjející se situace, které vyžadují okamžitou právní pozornost (úniky dat, hrozby soudního sporu, regulatorní dotazy, spory z duševního vlastnictví atd.).

#### Postup

1. Převezměte téma nebo popis incidentu
2. Rychle prohledejte všechny připojené zdroje pro relevantní kontext:
   - **E-mail**: Komunikace o incidentu
   - **Chat**: Diskuse a eskalace v reálném čase
   - **Dokumenty**: Relevantní interní předpisy, plány reakce, pojistné krytí
   - **Kalendář**: Naplánovaná jednání k reakci
   - **CLM**: Dotčené smlouvy, ustanovení o odškodnění, pojistné požadavky
3. Sestavte akceschopný krizový přehled

#### Formát výstupu

```
## Krizový přehled: [Téma]
**Připraveno**: [časové razítko]
**Klasifikace**: [posouzení závažnosti, pokud je určitelné]

### Shrnutí situace
[Co je o incidentu známo]

### Časová osa
[Chronologický souhrn událostí na základě dostupných zdrojů]

### Okamžité právní úvahy
[Povinnosti oznámení regulátorovi, povinnost uchování důkazů, otázky advokátního tajemství]

### Relevantní smlouvy
[Smlouvy, pojistné smlouvy nebo jiná ujednání, která mohou být dotčena]

### Interní reakce
[Jaká reakční činnost již proběhla na základě e-mailu/chatu]

### Klíčové kontakty
[Relevantní interní a externí kontakty identifikované ze zdrojů]

### Doporučené okamžité kroky
1. [Nejurgentnější akce]
2. [Druhá priorita]
3. [atd.]

### Informační mezery
[Co dosud není známo a je třeba zjistit]

### Prohledané zdroje
[Co bylo prohledáno a co nebylo dostupné]
```

#### Důležité poznámky ke krizovým přehledům
- Rychlost je klíčová. Vytvořte přehled rychle s dostupnými informacemi, místo čekání na úplné informace
- Okamžitě označte jakoukoli povinnost uchování důkazů (tzv. „litigation hold" — v ČR vychází z obecné povinnosti neničit důkazy v hrozícím nebo probíhajícím řízení a edicní povinnosti dle § 78a OSŘ, nikoli ze samostatného zákonného institutu jako v US)
- Zohledněte advokátní mlčenlivost (v případě potřeby označte přehled jako materiál chráněný advokátní mlčenlivostí podle § 21 zák. č. 85/1996 Sb. o advokacii)
- Pokud incident může představovat únik osobních údajů, upozorněte na platné oznamovací lhůty (např. 72 hodin dle GDPR / nařízení (EU) 2016/679 a zák. č. 110/2019 Sb.)
- Pokud je záležitost významná, doporučte zapojení externího právníka

## Obecné poznámky

- Pokud jsou zdroje nedostupné, mezery viditelně označte, aby uživatel věděl, co nebylo zkontrolováno
- U denních přehledů se postupně učte preferencím uživatele (co mu přijde užitečné, co chce vyfiltrovat)
- Přehledy mají být akceschopné: každá položka by měla mít jasný další krok nebo důvod pro zařazení
- Přehledy udržujte stručné. Odkazujte na zdrojové materiály, místo aby byly reprodukovány v plném rozsahu

<!-- Origin: DirectCase pravo-skills v1.1.0 (MIT, LICENSE-directcase-pravo-skills) | Import: 2026-07-14 do ak-sladek pluginu, review bez adaptaci (Cowork-native reference OK) | Inspiration: https://www.directcase.ai/cz/cs/news/claude-legal-plugin-cs -->
