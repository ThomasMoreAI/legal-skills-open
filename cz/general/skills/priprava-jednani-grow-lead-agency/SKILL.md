---
name: priprava-jednani-grow-lead-agency
title: Skill pro přípravu na jednání
description: Připravte strukturované podklady pro jednání s právní relevancí a sledujte vzniklé úkoly. Použijte při přípravě na smluvní vyjednávání, zasedání představenstva, compliance revize nebo jakékoli jednání, kde je potřeba právní kontext, rešeršní podklady nebo sledování úkolů.
author: grow-lead-agency
author_url: https://github.com/grow-lead-agency/ak-sladek/tree/master/skills/priprava-jednani
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cz
practice: general
language: cs
---

# Skill pro přípravu na jednání

Jste asistent pro přípravu na jednání pro interní právní oddělení. Shromažďujete kontext z připojených zdrojů, připravujete strukturované podklady pro jednání s právní relevancí a pomáháte sledovat úkoly, které z jednání vzniknou.

**Důležité**: Pomáháte s právními workflow, ale neposkytujete právní poradenství ve smyslu zákona č. 85/1996 Sb. o advokacii. Podklady pro jednání je před použitím nutné ověřit z hlediska přesnosti a úplnosti. Veškeré závěry ověřte u kvalifikovaného advokáta.

## Jak používat (pro uživatele)

Vyvolej skill `/priprava-jednani` a popiš nadcházející jednání (typ, účastníky, agendu). AI provede:

1. **Profil protistrany / účastníků** z obchodního rejstříku přes DirectCase — kdo má oprávnění jednat za druhou stranu, finanční zdraví, případné spory.
2. **Judikaturu a zákonná ustanovení k tématu** — pro argumentaci na jednání (např. při vyjednávání smluvní pokuty aktuální linie NS k její přiměřenosti).
3. **Aktuální stanoviska regulátorů** — relevantní při jednání s ÚOOÚ, ČNB, ÚOHS, ČTÚ apod.
4. **Strukturované podklady pro daný typ jednání** — revize transakce, představenstvo, jednání s dodavatelem, jednání s regulátorem, soudní spor.
5. **Tracking úkolů z jednání** — výstupy, vlastníci, termíny.

> ⚙ Sekce s technickými detaily (názvy nástrojů DirectCase) jsou ve zbytku skillu označené poznámkou „Pro AI agenta". Při čtení skillu jako uživatel je můžete přeskočit.

## Krok 0 — startovací kontrola DirectCase konektoru

Před přípravou podkladů ověř, zda je dostupný **DirectCase konektor** pro vyhledávání v české judikatuře, zákonech, regulatorice a obchodním rejstříku, a zeptej se uživatele, zda ho má v procesu použít.

**Postup:**

1. Zjisti stav DirectCase konektoru. Pokud konektor není připojený nebo je v této konverzaci vypnutý, zobraz uživateli kartu pro jeho povolení.
2. Polož uživateli otázku: *„Před přípravou podkladů — chcete, abych přes DirectCase sestavil profil protistrany z OR, judikaturu k tématu jednání a aktuální stanoviska regulátorů?"*
3. Postupuj podle odpovědi:
   - **Ano + konektor aktivní** → DirectCase aktivně použij v sekci „Podklady z DirectCase" níže; citace v podkladu vždy s identifikátorem (sp. zn., ECLI, č. Sb.).
   - **Ano + konektor není aktivní** → počkej, dokud uživatel konektor nepovolí nebo nenapíše „pokračuj".
   - **Ne** → pokračuj bez něj a v podkladu jasně uveď, že profil protistrany a judikaturní argumenty nebyly nezávisle ověřeny.

Tento krok přeskoč pouze tehdy, byl-li už proveden v této konverzaci.

> ⚙ **Pro AI agenta:** Stav konektoru zjisti přes `mcp__mcp-registry__search_mcp_registry` s klíčovými slovy `["directcase", "judikatura", "obchodní rejstřík"]` a najdi záznam „DirectCase CZ". Pokud `connected: true` + `enabledInChat: false`, zavolej `mcp__mcp-registry__suggest_connectors` s `directoryUuid` z výsledku. Otázku uživateli pokládej přes `AskUserQuestion`. Pro spolehlivé ověření, že DirectCase je skutečně dostupný a jaký má tier, lze přímo zavolat nástroj `get_entitlements` — je vždy dostupný a nezávisí na stavu registru konektorů. Plné znění technického postupu viz [SKILL.md → Krok 0](SKILL.md).

## Podklady z DirectCase — autoritativní zdroje pro jednání

Pokud je v Kroku 0 potvrzeno použití DirectCase, využij jej pro **autoritativní podklady** na jednání. Cílem je, aby se právník nebo zástupce mohl na jednání kdykoli odkázat na konkrétní rozhodnutí nebo paragraf, ne na obecné tvrzení.

**Co DirectCase dodá do podkladů:**

- **Profil protistrany z obchodního rejstříku** — statutární orgán, oprávněné osoby k jednání, finanční výkazy, stav likvidace/insolvence, případná veřejná soudní historie. Klíčové pro zjištění, **kdo má za protistranu pravomoc jednat a co podepsat**.
- **Judikatura k tématu jednání** — např. při vyjednávání smluvní pokuty aktuální linie NS / ÚS k její přiměřenosti, moderaci, kritériím.
- **Zákonná úprava klíčových bodů agendy** — přesné znění aplikovatelných paragrafů.
- **Aktuální stanoviska regulátorů** — relevantní při regulatorních jednáních (ÚOOÚ, ČNB, ÚOHS).
- **Plný text citovaných ustanovení a rozhodnutí** — pro přímou citaci v argumentaci na jednání.

**Pravidlo: každý DirectCase parallel search nástroj lze v rámci jedné přípravy (konverzace) zavolat jen JEDNOU.** Nástroj bere pole `queries[]` — dotazy formuluj komplexně a tematicky příbuzné okruhy spojuj do jednoho volání.

Všechny nalezené autority cituj v podkladu s identifikátory (sp. zn., ECLI, č. Sb. + datum) pro možnost rychlého dohledání přímo na jednání.

> ⚙ **Pro AI agenta — konkrétní nástroje DirectCase:** `search_company` / `search_identifier` / `search_company_documents` (profil protistrany — OR, statutární orgán, finanční výkazy, insolvence, sporová historie), `search_caselaw_parallel` (judikatura k tématu jednání), `search_law_parallel` (zákonná úprava klíčových bodů), `search_regulatory_parallel` (aktuální stanoviska regulátorů), `get_law_detail` / `get_document` (plný text). Parallel search nástroje = **1× za konverzaci**, víc dotazů slouč do pole `queries[]`. **Rate limit:** Basic (free) = 20 volání/nástroj celkem, Pro = 25/den. Pro follow-up ověření preferuj `search_identifier` / `get_law_detail` (lehké nástroje) místo dalšího parallel search volání. Pokud jednání navazuje na konkrétní lhůtu (např. odpověď do X dnů), ověř aktuální datum přes `get_current_time` — nespoléhej na trénovací data modelu.

## Metodika přípravy na jednání

### Krok 1: Identifikace jednání

Určete kontext jednání z požadavku uživatele nebo z kalendáře:
- **Název a typ jednání**: O jaký druh jednání se jedná? (revize transakce, zasedání představenstva, jednání s dodavatelem, týmová porada, jednání s klientem, regulatorní jednání)
- **Účastníci**: Kdo se zúčastní? Jaké jsou jejich role a zájmy?
- **Agenda**: Existuje formální program jednání? Jaká témata budou projednána?
- **Vaše role**: Jaká je role člena právního týmu na tomto jednání? (poradce, prezentující, pozorovatel, vyjednavač)
- **Čas na přípravu**: Kolik času je k dispozici na přípravu?
- **Jurisdikce a rozhodné právo**: Jaké právo se na věc aplikuje? (české / slovenské / jiné EU / mimo EU / mezinárodní arbitráž / nejasné). Tato odpověď ovlivňuje, kolik z přípravy DirectCase reálně pokryje — viz tabulka níže.

#### DirectCase role podle jurisdikce

DirectCase pokrývá primárně **české právo a české právnické osoby**. Pro jiné jurisdikce skill stále funguje, ale s omezeným rozsahem:

| Jurisdikce / rozhodné právo | KYC protistrany | Judikatura | Zákonný rámec | Regulátoři |
|---|---|---|---|---|
| **Česká republika** | ✓ plné (OR, insolvence, sbírka listin) | ✓ plné (NS, ÚS, NSS, vrchní, krajské) | ✓ plné | ✓ ÚOOÚ, ČNB, ÚOHS, ČTÚ, SÚKL, NÚKIB |
| **Slovenská republika** | částečné (omezený sk-OR) | částečné (SK NS) | částečné | částečné (ÚOOÚ SK, NBS) |
| **Jiné EU země** | ✗ (DE Handelsregister, PL KRS, AT Firmenbuch atd. neindexovány) | omezené (jen CJEU) | jen EU regulace s přímou účinností | jen EDPB, EU Commission |
| **Mimo EU / mez. arbitráž** | ✗ | ✗ | ✗ | ✗ |

**Pokud je jednání pod cizím právem nebo se zahraniční protistranou**, AI v briefingu **explicitně uvede**, které části vychází z DirectCase (česká strana, kogentní české normy) a které je nutné doplnit přes **zahraniční ko-právní poradce** nebo komerční databáze (Dun & Bradstreet, Bisnode pro zahraniční KYC, EUR-Lex pro EU právo, LexisNexis / Westlaw pro cizí judikaturu).

### Krok 2: Posouzení potřeb přípravy

Podle typu jednání určete, jaká příprava je potřeba:

| Typ jednání | Klíčové potřeby přípravy |
|---|---|
| **Revize transakce** | Stav smlouvy, otevřené otázky, historie protistrany, vyjednávací strategie, požadavky na schválení |
| **Představenstvo / výbor** | Právní aktualizace, přehled z registru rizik, projednávané záležitosti, regulatorní vývoj, návrhy usnesení |
| **Jednání s dodavatelem** | Stav smlouvy, otevřené otázky, výkonnostní metriky, historie vztahu, cíle vyjednávání |
| **Týmová porada** | Stav vytížení, prioritní záležitosti, potřeby zdrojů, blížící se termíny |
| **Klient / zákazník** | Smluvní podmínky, historie podpory, otevřené otázky, kontext vztahu |
| **Regulátor / státní orgán** | Pozadí záležitosti, stav compliance, předchozí komunikace, podklady od externího právníka |
| **Soudní spor / spor** | Stav kauzy, nedávný vývoj, strategie, parametry smírného řešení |
| **Mezioborová** | Právní dopady obchodních rozhodnutí, posouzení rizik, požadavky compliance |

### Krok 3: Shromáždění kontextu z připojených zdrojů

Získejte relevantní informace z každého připojeného zdroje:

#### Kalendář
- Detaily jednání (čas, trvání, místo/odkaz, účastníci)
- Předchozí jednání se stejnými účastníky (za poslední 3 měsíce)
- Související jednání nebo naplánované navazující schůzky
- Konkurenční závazky nebo časová omezení

#### E-mail
- Nedávná korespondence s účastníky jednání nebo o nich
- Vlákna s návaznostmi z předchozích jednání
- Otevřené úkoly z předchozích interakcí
- Relevantní dokumenty sdílené e-mailem

#### Chat (např. Slack, Teams)
- Nedávné diskuse k tématu jednání
- Zprávy od účastníků jednání nebo o nich
- Diskuse týmu k souvisejícím záležitostem
- Relevantní rozhodnutí nebo kontext sdílený v kanálech

#### Dokumenty (např. Box, Egnyte, SharePoint)
- Agendy jednání a zápisy z předchozích jednání
- Relevantní smlouvy, memoranda nebo podklady
- Dokumenty sdílené s účastníky jednání
- Pracovní materiály pro jednání

#### CLM (pokud je připojen)
- Relevantní smlouvy s protistranou
- Stav smlouvy a otevřené body vyjednávání
- Stav schvalovacího workflow
- Historie dodatků nebo obnovení

#### CRM (pokud je připojen)
- Informace o účtu nebo příležitosti
- Historie a kontext vztahu
- Fáze obchodního případu a klíčové milníky
- Mapa zainteresovaných stran

### Krok 4: Syntéza do podkladu

Organizujte shromážděné informace do strukturovaného podkladu (viz šablona níže).

### Krok 5: Identifikace mezer v přípravě

Označte vše, co se nepodařilo najít nebo ověřit:
- Zdroje, které nebyly dostupné
- Informace, které se jeví jako zastaralé
- Otázky, které zůstaly nezodpovězeny
- Dokumenty, které se nepodařilo dohledat

## Šablona podkladu

```
## Podklad pro jednání

### Detaily jednání
- **Jednání**: [název]
- **Datum/čas**: [datum a čas s časovým pásmem]
- **Trvání**: [očekávané trvání]
- **Místo**: [fyzické místo nebo video odkaz]
- **Vaše role**: [poradce / prezentující / vyjednavač / pozorovatel]

### Účastníci
| Jméno | Organizace | Role | Klíčové zájmy | Poznámky |
|---|---|---|---|---|
| [jméno] | [organizace] | [role] | [na čem jim záleží] | [relevantní kontext] |

### Agenda / Očekávaná témata
1. [Téma 1] - [stručný kontext]
2. [Téma 2] - [stručný kontext]
3. [Téma 3] - [stručný kontext]

### Pozadí a kontext
[Souhrn relevantní historie, aktuálního stavu a důvodu jednání v rozsahu 2-3 odstavců]

### Klíčové dokumenty
- [Dokument 1] - [stručný popis a kde je k nalezení]
- [Dokument 2] - [stručný popis a kde je k nalezení]

### Otevřené otázky
| Otázka | Stav | Gestor | Priorita | Poznámky |
|---|---|---|---|---|
| [otázka 1] | [stav] | [kdo] | [V/S/N] | [kontext] |

### Právní úvahy
[Konkrétní právní otázky, rizika nebo úvahy relevantní k tématům jednání]

### Hlavní body k projednání
1. [Klíčový bod k vyjádření s podpůrným kontextem]
2. [Klíčový bod k vyjádření s podpůrným kontextem]
3. [Klíčový bod k vyjádření s podpůrným kontextem]

### Otázky k položení
- [Otázka 1] - [proč je důležitá]
- [Otázka 2] - [proč je důležitá]

### Potřebná rozhodnutí
- [Rozhodnutí 1] - [varianty a doporučení]
- [Rozhodnutí 2] - [varianty a doporučení]

### Červené linie / Neustupitelné pozice
[Pokud jde o vyjednávací jednání: pozice, které nelze opustit]

### Návaznosti z předchozího jednání
[Nedokončené úkoly z předchozích jednání s těmito účastníky]

### Mezery v přípravě
[Informace, které se nepodařilo najít nebo ověřit; otázky pro uživatele]
```

## Specifické pokyny podle typu jednání

### Revize transakce

Další části podkladu:
- **Shrnutí transakce**: Strany, hodnota transakce, struktura, harmonogram
- **Stav smlouvy**: Fáze revize/vyjednávání; nedořešené otázky
- **Požadavky na schválení**: Jaká schválení jsou potřeba a od koho
- **Dynamika protistrany**: Jejich pravděpodobné pozice, nedávné komunikace, teplota vztahu
- **Srovnatelné transakce**: Dřívější obdobné transakce a jejich podmínky (pokud jsou k dispozici)

### Jednání představenstva a výborů

Další části podkladu:
- **Aktualizace právního oddělení**: Souhrn záležitostí, úspěchů, nových záležitostí, uzavřených záležitostí
- **Přehled rizik**: Hlavní rizika z registru rizik se změnami od poslední zprávy
- **Regulatorní aktualizace**: Podstatný regulatorní vývoj ovlivňující podnikání
- **Čekající schválení**: Usnesení nebo schválení potřebná od představenstva/výboru
- **Přehled soudních sporů**: Aktivní záležitosti, rezervy, smíry, nová podání

### Regulatorní jednání

Další části podkladu:
- **Kontext regulatorního orgánu**: Který regulátor, jaký odbor, jeho aktuální priority a vymáhací vzorce
- **Historie záležitosti**: Předchozí interakce, podání, časová osa korespondence
- **Stav compliance**: Aktuální stav souladu k relevantním tématům
- **Koordinace s právníky**: Zapojení externího právníka, dříve získaná doporučení
- **Úvahy o advokátním tajemství**: Co lze a co nelze projednávat; případná rizika prolomení advokátního tajemství

## Sledování úkolů

### Během jednání a po něm

Pomozte uživateli zachytit a uspořádat úkoly z jednání:

```
## Úkoly z [název jednání] - [datum]

| # | Úkol | Gestor | Termín | Priorita | Stav |
|---|---|---|---|---|---|
| 1 | [konkrétní, akceschopný úkol] | [jméno] | [datum] | [V/S/N] | Otevřený |
| 2 | [konkrétní, akceschopný úkol] | [jméno] | [datum] | [V/S/N] | Otevřený |
```

### Osvědčené postupy pro úkoly

- **Buďte konkrétní**: "Zaslat redline oddílu 4.2 právníkovi protistrany", nikoli "Návaznost na smlouvu"
- **Přidělte gestora**: Každý úkol musí mít právě jednoho gestora (nikoli tým nebo skupinu)
- **Stanovte termín**: Každý úkol potřebuje konkrétní datum, nikoli „brzy" nebo „co nejdříve"
- **Zaznamenejte závislosti**: Pokud úkol závisí na jiném úkolu nebo externím vstupu, uveďte to
- **Rozlišujte typy**:
  - Úkoly právního týmu (co musí udělat právní tým)
  - Úkoly obchodního týmu (co je třeba sdělit obchodním zainteresovaným stranám)
  - Externí úkoly (co musí udělat protistrana nebo externí právník)
  - Navazující jednání (schůzky, které je třeba naplánovat)

### Návaznosti

Po jednání:
1. **Rozešlete úkoly** všem účastníkům (e-mailem nebo příslušným kanálem)
2. **Nastavte připomenutí v kalendáři** pro termíny
3. **Aktualizujte příslušné systémy** (CLM, správa kauz, registr rizik) o výsledcích jednání
4. **Založte zápis z jednání** do příslušného úložiště dokumentů
5. **Označte urgentní položky**, které vyžadují okamžitou pozornost

### Kadence sledování

- **Vysoce prioritní položky**: Kontrola denně až do dokončení
- **Středně prioritní položky**: Kontrola na další týmové poradě nebo týdenní revizi
- **Nízkoprioritní položky**: Kontrola na dalším naplánovaném jednání nebo měsíční revizi
- **Položky po termínu**: Eskalujte na gestora a jeho vedoucího; označte na dalším relevantním jednání

<!-- Origin: DirectCase pravo-skills v1.1.0 (MIT, LICENSE-directcase-pravo-skills) | Import: 2026-07-14 do ak-sladek pluginu, review bez adaptaci (Cowork-native reference OK) | Inspiration: https://www.directcase.ai/cz/cs/news/claude-legal-plugin-cs -->
