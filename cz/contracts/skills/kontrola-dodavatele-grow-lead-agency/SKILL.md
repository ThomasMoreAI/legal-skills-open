---
name: kontrola-dodavatele-grow-lead-agency
title: /kontrola-dodavatele -- Stav smluv s dodavatelem
description: Zkontrolujte stav stávajících smluv s dodavatelem napříč všemi propojenými systémy — CLM, CRM, e-mail a úložiště dokumentů — včetně analýzy mezer a blížících se termínů. Použijte při zavádění nebo obnovení dodavatele, když potřebujete konsolidovaný přehled o tom, co je podepsáno a co chybí (rámcová smlouva, smlouva o zpracování osobních údajů, dílčí smlouva o dílo, smlouva o mlčenlivosti, SLA atd.), nebo při kontrole blížících se konců platnosti a přetrvávajících závazků.
author: grow-lead-agency
author_url: https://github.com/grow-lead-agency/ak-sladek/tree/master/skills/kontrola-dodavatele
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cz
practice: contracts
language: cs
---

# /kontrola-dodavatele -- Stav smluv s dodavatelem

> Pokud narazíte na neznámé zástupné symboly nebo potřebujete zjistit, které nástroje jsou propojeny, viz [CONNECTORS.md](../../CONNECTORS.md).

Zkontrolujte stav stávajících smluv s dodavatelem napříč všemi propojenými systémy. Poskytuje konsolidovaný pohled na právní vztah.

**Důležité**: Tento příkaz pomáhá s právními workflow, ale neposkytuje právní poradenství ve smyslu zákona č. 85/1996 Sb. o advokacii. Hlášení o stavu smluv je třeba ověřit oproti originálním dokumentům kvalifikovaným advokátem.

## Jak používat (pro uživatele)

Vyvolej skill `/kontrola-dodavatele` a uveď název nebo IČO dodavatele. AI provede:

1. **Externí KYC dodavatele** přes DirectCase — obchodní rejstřík (IČO, sídlo, statutární orgán, oprávněné osoby k podpisu), insolvenční rejstřík, účetní závěrky pro posouzení finančního zdraví, případnou veřejnou judikaturu k subjektu.
2. **Interní prohledání všech propojených systémů** — CLM (smlouvy), CRM (stav účtu), e-mail (vyjednávání), úložiště dokumentů (podepsané smlouvy), chat (relevantní diskuse).
3. **Konsolidovaný přehled smluv** — typ, stav, účinnost, konec platnosti, automatické prodloužení, klíčové podmínky.
4. **Analýza mezer** — co existuje a co chybí (např. máte rámcovou smlouvu, ale chybí smlouva o zpracování osobních údajů, přestože dodavatel zpracovává osobní údaje).
5. **Strukturované hlášení** — přehled vztahu, blížící se termíny, doporučené akce.

> ⚙ Sekce s technickými detaily (názvy nástrojů DirectCase) jsou ve zbytku skillu označené poznámkou „Pro AI agenta". Při čtení skillu jako uživatel je můžete přeskočit.

## Krok 0 — startovací kontrola DirectCase konektoru

Před zahájením kontroly dodavatele ověř, zda je dostupný **DirectCase konektor** pro vyhledávání v obchodním a insolvenčním rejstříku, a zeptej se uživatele, zda ho má v procesu použít. **DirectCase je pro tento skill klíčový** — bez něj chybí jádro KYC (ověření v OR, insolvenci, veřejné judikatuře).

**Postup:**

1. Zjisti stav DirectCase konektoru. Pokud konektor není připojený nebo je v této konverzaci vypnutý, zobraz uživateli kartu pro jeho povolení.
2. Polož uživateli otázku: *„Před kontrolou dodavatele — chcete, abych přes DirectCase prověřil obchodní rejstřík, insolvenční rejstřík, finanční výkazy a relevantní veřejnou judikaturu k tomuto subjektu?"*
3. Postupuj podle odpovědi:
   - **Ano + konektor aktivní** → DirectCase aktivně použij v sekci „DirectCase — veřejné registry a due diligence" níže; v hlášení uveď datum dotazu a označ, že KYC bylo provedeno ověřenými zdroji.
   - **Ano + konektor není aktivní** → počkej, dokud uživatel konektor nepovolí nebo nenapíše „pokračuj".
   - **Ne** → upozorni uživatele, že bez DirectCase je kontrola dodavatele výrazně omezená (chybí KYC z OR, kontrola insolvence, finanční výkazy, sporová historie); pokračuj jen v rozsahu interních systémů a v hlášení jasně uveď, že externí ověření v OR neproběhlo.

Tento krok přeskoč pouze tehdy, byl-li už proveden v této konverzaci.

> ⚙ **Pro AI agenta:** Stav konektoru zjisti přes `mcp__mcp-registry__search_mcp_registry` s klíčovými slovy `["directcase", "obchodní rejstřík"]` a najdi záznam „DirectCase CZ". Pokud `connected: true` + `enabledInChat: false`, zavolej `mcp__mcp-registry__suggest_connectors` s `directoryUuid` z výsledku. Otázku uživateli pokládej přes `AskUserQuestion`. Pro spolehlivé ověření, že DirectCase je skutečně dostupný a jaký má tier, lze přímo zavolat nástroj `get_entitlements` — je vždy dostupný a nezávisí na stavu registru konektorů. Plné znění technického postupu viz [SKILL.md → Krok 0](SKILL.md).

## Spuštění

```
/kontrola-dodavatele [název dodavatele]
```

Pokud není název dodavatele uveden, vyzvěte uživatele, aby upřesnil, kterého dodavatele chce zkontrolovat.

## Workflow

### Krok 1: Identifikujte dodavatele

Přijměte název dodavatele od uživatele. Ošetřete běžné varianty:
- Úplný obchodní název vs. obchodní značka (např. „Alphabet Inc." vs. „Google")
- Zkratky (např. „AWS" vs. „Amazon Web Services")
- Vztahy mezi mateřskou společností a dceřinou společností

Pokud je název dodavatele nejednoznačný, požádejte uživatele o upřesnění.

### Krok 2: Prohledejte propojené systémy

Vyhledejte dodavatele ve všech dostupných propojených systémech v pořadí dle priority:

#### CLM (systém pro správu smluv) -- Pokud je propojen
Vyhledejte všechny smlouvy s dodavatelem:
- Aktivní smlouvy
- Smlouvy, jejichž platnost skončila (za poslední 3 roky)
- Smlouvy v jednání nebo čekající na podpis
- Dodatky a přílohy

#### CRM -- Pokud je propojen
Vyhledejte záznam dodavatele/účtu:
- Stav účtu a typ vztahu
- Související příležitosti nebo obchodní případy
- Kontaktní údaje na právní/smluvní tým dodavatele

#### E-mail -- Pokud je propojen
Vyhledejte nedávnou relevantní korespondenci:
- E-maily týkající se smluv (za posledních 6 měsíců)
- Přílohy s návrhy smluv (smlouvy o mlčenlivosti, rámcové smlouvy, dílčí smlouvy)
- Vyjednávací vlákna

#### Dokumenty (např. Box, Egnyte, SharePoint) -- Pokud jsou propojeny
Vyhledejte:
- Podepsané smlouvy
- Redline úpravy a návrhy
- Podklady pro due diligence

#### Chat (např. Slack, Teams) -- Pokud je propojen
Vyhledejte nedávné zmínky:
- Žádosti o smlouvy týkající se tohoto dodavatele
- Právní dotazy k dodavateli
- Relevantní týmové diskuse (za poslední 3 měsíce)

#### DirectCase — veřejné registry a due diligence

Pokud je v Kroku 0 potvrzeno použití DirectCase, využij jej jako **primární zdroj** pro veřejné informace o dodavateli. Z výpisu z obchodního rejstříku a navazujících zdrojů ověř:

- **Identifikační údaje** — obchodní název, IČO, DIČ, právní forma, sídlo, datum vzniku, základní kapitál.
- **Statutární orgán a oprávněné osoby k podpisu** — kdo jedná za společnost a v jakém složení (samostatně × společně × s prokuristou).
- **Stav likvidace nebo insolvenčního řízení** — pokud probíhá, je smluvní vztah s dodavatelem sporný.
- **Účetní závěrky a výroční zprávy ze sbírky listin** — pro posouzení finančního zdraví dodavatele (relevantní u dlouhodobých smluv nebo velkých závazků).
- **Veřejná judikatura** — zda dodavatel figuruje v relevantních sporech (např. opakované žaloby na vady plnění, insolvenční řízení, spory s zákazníky).

Tyto informace zahrň do přehledu dodavatele a **označ červeně**, pokud zjistíš insolvenci, exekuci, likvidaci nebo významné rozsudky v neprospěch dodavatele.

**Pravidlo: `search_caselaw_parallel` lze v rámci jedné kontroly (konverzace) zavolat jen JEDNOU.** Nástroj bere pole `queries[]` — tematicky příbuzné dotazy (spory, insolvence, sankční řízení) slouč do jednoho volání s více položkami v poli.

> ⚙ **Pro AI agenta — konkrétní nástroje DirectCase:** `search_company` (obchodní rejstřík: IČO, sídlo, statutární orgán, způsob jednání, stav likvidace/insolvence), `search_identifier` (přesné hledání podle IČO), `search_company_documents` (sbírka listin: účetní závěrky, výroční zprávy, dokumenty z insolvenčního rejstříku), `convert_file_to_markdown` (přečtení konkrétního dokumentu ze sbírky listin pro finanční analýzu — funguje jen pro důvěryhodné právní domény; **PDF mimo tyto domény převáděj lokálně**, ne přes DirectCase), `search_caselaw_parallel` (judikatura k subjektu — spory, insolvence; **1× za konverzaci**, víc dotazů slouč do pole `queries[]`). **Rate limit:** Basic (free) = 20 volání/nástroj celkem, Pro = 25/den (parallel search) resp. 200/den (lehké nástroje). Pro follow-up dotazy preferuj `search_identifier` místo dalšího `search_caselaw_parallel` volání.

### Krok 3: Sestavte přehled o stavu smluv

Pro každou nalezenou smlouvu uveďte:

| Pole | Detaily |
|-------|---------|
| **Typ smlouvy** | smlouva o mlčenlivosti, rámcová smlouva, dílčí smlouva o dílo / objednávka, smlouva o zpracování osobních údajů (čl. 28 GDPR), SLA, licenční smlouva atd. |
| **Stav** | Aktivní, po platnosti, v jednání, čeká na podpis |
| **Datum účinnosti** | Kdy smlouva nabyla účinnosti |
| **Datum ukončení** | Kdy končí nebo se obnovuje |
| **Automatické prodloužení** | Ano/Ne, s dobou prodloužení a výpovědní lhůtou |
| **Klíčové podmínky** | Limit odpovědnosti, rozhodné právo, ustanovení o ukončení |
| **Dodatky** | Případné dodatky nebo přílohy v evidenci |

### Krok 4: Analýza mezer

Identifikujte, které smlouvy existují a které mohou chybět:

```
## Pokrytí smlouvami

[CHECK] Smlouva o mlčenlivosti -- [stav]
[CHECK/MISSING] Rámcová smlouva -- [stav nebo „Nenalezeno"]
[CHECK/MISSING] Smlouva o zpracování osobních údajů (čl. 28 GDPR) -- [stav nebo „Nenalezeno"]
[CHECK/MISSING] Dílčí smlouva o dílo / objednávka -- [stav nebo „Nenalezeno"]
[CHECK/MISSING] SLA -- [stav nebo „Nenalezeno"]
[CHECK/MISSING] Potvrzení o pojištění -- [stav nebo „Nenalezeno"]
```

Označte všechny mezery, které mohou být potřeba podle typu vztahu (např. pokud existuje rámcová smlouva, ale chybí smlouva o zpracování osobních údajů a dodavatel osobní údaje zpracovává).

### Krok 5: Vygenerujte hlášení

Vytvořte konsolidované hlášení:

```
## Stav smluv s dodavatelem: [Název dodavatele]

**Datum prověrky**: [dnešní datum]
**Prověřené zdroje**: [seznam prohledaných systémů]
**Nedostupné zdroje**: [seznam nepropojených systémů, pokud existují]

## Přehled vztahu

**Dodavatel**: [úplný obchodní název]
**Typ vztahu**: [dodavatel/partner/zákazník atd.]
**Stav v CRM**: [pokud je k dispozici]

## Přehled smluv

### [Typ smlouvy 1] -- [Stav]
- **Účinnost**: [datum]
- **Konec platnosti**: [datum] ([automaticky se prodlužuje / neprodlužuje se automaticky])
- **Klíčové podmínky**: [shrnutí podstatných ustanovení]
- **Umístění**: [kde je uložena podepsaná kopie]

### [Typ smlouvy 2] -- [Stav]
[atd.]

## Analýza mezer

[Co je zajištěno vs. co může být potřeba]

## Nadcházející úkony

- [Případné blížící se konce platnosti nebo termíny obnovení]
- [Požadované smlouvy, které ještě nejsou uzavřeny]
- [Dodatky nebo aktualizace, které mohou být potřeba]

## Poznámky

[Jakýkoli relevantní kontext z vyhledávání v e-mailu/chatu]
```

### Krok 6: Ošetření chybějících zdrojů

Pokud klíčové systémy nejsou propojeny přes MCP:

- **Žádný CLM**: Uveďte, že žádný CLM není propojen. Doporučte uživateli zkontrolovat CLM ručně. Nahlaste, co bylo nalezeno v ostatních systémech.
- **Žádný CRM**: Přeskočte kontext CRM. Upozorněte na chybějící údaje.
- **Žádný e-mail**: Uveďte, že e-mail nebyl prohledán. Doporučte uživateli prohledat e-mail na výrazy „[název dodavatele] smlouva" nebo „[název dodavatele] mlčenlivost".
- **Žádné dokumenty**: Uveďte, že úložiště dokumentů nebylo prohledáno.

Vždy jasně uveďte, které zdroje byly prověřeny a které nikoli, aby uživatel znal úplnost hlášení.

## Poznámky

- Pokud nejsou v žádném propojeném systému nalezeny žádné smlouvy, jasně to uveďte a zeptejte se uživatele, zda má smlouvy uloženy jinde
- U skupin dodavatelů (např. dodavatel s více dceřinými společnostmi) se zeptejte, zda si uživatel přeje prověřit konkrétní subjekt, nebo celou skupinu
- Upozorněte na všechny smlouvy, kterým skončila platnost, ale mohou stále obsahovat přetrvávající závazky (mlčenlivost, odškodnění atd.)
- Pokud se smlouva blíží ke konci platnosti (do 90 dnů), výrazně na to upozorněte

<!-- Origin: DirectCase pravo-skills v1.1.0 (MIT, LICENSE-directcase-pravo-skills) | Import: 2026-07-14 do ak-sladek pluginu, review bez adaptaci (Cowork-native reference OK) | Inspiration: https://www.directcase.ai/cz/cs/news/claude-legal-plugin-cs -->
