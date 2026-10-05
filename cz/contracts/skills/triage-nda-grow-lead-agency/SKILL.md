---
name: triage-nda-grow-lead-agency
title: /triage-nda -- Předběžná kontrola NDA
description: Rychle proveďte triage příchozí NDA a klasifikujte ji jako ZELENOU (standardní schválení), ŽLUTOU (revize právníka) nebo ČERVENOU (plná právní revize). Použijte, když přijde nová NDA od obchodu nebo oddělení rozvoje, při kontrole vložených doložek o zákazu přetahování, konkurenčních doložek nebo chybějících výjimek, nebo při rozhodování, zda lze NDA podepsat v rámci standardní delegace pravomocí.
author: grow-lead-agency
author_url: https://github.com/grow-lead-agency/ak-sladek/tree/master/skills/triage-nda
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cz
practice: contracts
language: cs
---

# /triage-nda -- Předběžná kontrola NDA

> Pokud narazíte na neznámé zástupné symboly nebo si potřebujete ověřit, které nástroje jsou připojeny, viz [CONNECTORS.md](../../CONNECTORS.md).

Proveďte triage NDA: @$1

Rychle proveďte triage příchozích NDA oproti standardním kontrolním kritériím. Klasifikujte NDA pro směrování: standardní schválení, revize právníka nebo plná právní revize.

**Důležité**: Tento plugin pomáhá s právními workflow, ale neposkytuje právní poradenství ve smyslu zákona č. 85/1996 Sb. o advokacii. Veškeré závěry ověřte u kvalifikovaného advokáta.

## Jak používat (pro uživatele)

Vyvolej skill `/triage-nda` a přilož NDA (PDF, DOCX nebo vložený text). AI provede:

1. **KYC protistrany** v obchodním rejstříku přes DirectCase (existence, statutární orgán, oprávnění k podpisu, insolvence).
2. **Rychlou kontrolu NDA** proti checklistu — vzájemnost, doba trvání, definice důvěrných informací, výjimky, problematické doložky (zákaz přetahování, konkurence, reziduály).
3. **Klasifikaci**: **ZELENÁ** (standardní schválení) → **ŽLUTÁ** (revize právníka) → **ČERVENÁ** (plná právní revize).
4. **Ověření judikatury** k případným sporným doložkám (smluvní pokuty za porušení mlčenlivosti, platnost konkurenčních doložek) přes DirectCase.
5. **Strukturované doporučení** — co podepsat, co vyjednat, co odmítnout, s odkazem na konkrétní problémové doložky.

> ⚙ Sekce s technickými detaily (názvy nástrojů DirectCase) jsou ve zbytku skillu označené poznámkou „Pro AI agenta". Při čtení skillu jako uživatel je můžete přeskočit.

## Krok 0 — startovací kontrola DirectCase konektoru

Před zahájením triage NDA ověř, zda je dostupný **DirectCase konektor** pro vyhledávání v obchodním rejstříku a české judikatuře, a zeptej se uživatele, zda ho má v procesu použít.

**Postup:**

1. Zjisti stav DirectCase konektoru. Pokud konektor není připojený nebo je v této konverzaci vypnutý, zobraz uživateli kartu pro jeho povolení.
2. Polož uživateli otázku: *„Před triage NDA — chcete, abych přes DirectCase ověřil protistranu v obchodním rejstříku a případně judikaturu k sporným doložkám (smluvní pokuty, konkurence)?"*
3. Postupuj podle odpovědi:
   - **Ano + konektor aktivní** → DirectCase aktivně použij v sekci „Ověření protistrany a judikatury přes DirectCase" níže.
   - **Ano + konektor není aktivní** → počkej, dokud uživatel konektor nepovolí nebo nenapíše „pokračuj".
   - **Ne** → pokračuj bez něj a v závěru uveď, že údaje o protistraně z OR a citace judikatury nebyly nezávisle ověřeny.

Tento krok přeskoč pouze tehdy, byl-li už proveden v této konverzaci.

> ⚙ **Pro AI agenta:** Stav konektoru zjisti přes `mcp__mcp-registry__search_mcp_registry` s klíčovými slovy `["directcase", "obchodní rejstřík", "judikatura"]` a najdi záznam „DirectCase CZ". Pokud `connected: true` + `enabledInChat: false`, zavolej `mcp__mcp-registry__suggest_connectors` s `directoryUuid` z výsledku. Otázku uživateli pokládej přes `AskUserQuestion`. Pro spolehlivé ověření, že DirectCase je skutečně dostupný a jaký má tier, lze přímo zavolat nástroj `get_entitlements` — je vždy dostupný a nezávisí na stavu registru konektorů. Plné znění technického postupu viz [SKILL.md → Krok 0](SKILL.md).

## Vyvolání

```
/triage-nda
```

## Ověření protistrany a judikatury přes DirectCase

Pokud je v Kroku 0 potvrzeno použití DirectCase, využij jej pro:

- **KYC protistrany** — ověření v obchodním rejstříku (IČO, sídlo, statutární orgán, způsob jednání, oprávněné osoby k podpisu); kontrola insolvenčního rejstříku a sbírky listin.
- **Zákonný rámec NDA** — relevantní ustanovení českého práva (§ 504 OZ ochrana obchodního tajemství, § 1730 OZ předsmluvní odpovědnost, § 2985 a násl. OZ ochrana proti nekalé soutěži, zák. č. 143/2001 Sb. ochrana hospodářské soutěže).
- **Judikatura k sporným doložkám** — soudní praxe k vymahatelnosti NDA, smluvním pokutám za porušení mlčenlivosti, platnosti konkurenčních doložek a doložek o zákazu přetahování.

**Pravidlo: každý DirectCase parallel search nástroj (`search_law_parallel`, `search_caselaw_parallel`) lze v rámci jedné konverzace zavolat jen JEDNOU.** Nástroj bere pole `queries[]` — u běžné NDA si vystačíš s jedním dotazem na judikaturu k typicky sporným doložkám v jednom volání; pokud potřebuješ víc tematických okruhů, přidej je jako další položky do stejného pole `queries[]`, nevolej nástroj vícekrát.

> ⚙ **Pro AI agenta — konkrétní nástroje DirectCase:** `search_company` / `search_identifier` (obchodní rejstřík), `search_company_documents` (sbírka listin, insolvenční rejstřík), `search_law_parallel` (zákonný rámec NDA), `search_caselaw_parallel` (judikatura k vymahatelnosti NDA, smluvním pokutám, konkurenčním doložkám). Parallel search nástroje = **1× za konverzaci**. **Rate limit:** Basic (free) = 20 volání/nástroj celkem, Pro = 25/den, Premium = 75/den. Pro follow-up dotazy preferuj `search_keyword` / `search_identifier` (vyšší limit: Pro 200/den) místo dalšího parallel search volání.

## Pracovní postup

### Krok 1: Převzetí NDA

Převezměte NDA v libovolném formátu:
- **Nahraný soubor**: PDF, DOCX nebo jiný formát dokumentu
- **URL**: Odkaz na NDA v systému pro správu dokumentů
- **Vložený text**: Text NDA vložený přímo

Pokud NDA není poskytnuta, vyzvěte uživatele, aby ji dodal.

### Krok 2: Načtení playbooku pro NDA

Vyhledejte kontrolní kritéria pro NDA v lokálním nastavení (např. `legal.local.md`).

Playbook (interní příručka) pro NDA by měl definovat:
- Požadavky na vzájemnost vs. jednostrannost
- Přijatelné doby trvání
- Požadované výjimky
- Zakázaná ustanovení
- Specifické požadavky organizace

**Pokud není playbook pro NDA nakonfigurován:**
- Pokračujte s přiměřenými tržně standardními výchozími hodnotami
- Jasně upozorněte, že jsou používány výchozí hodnoty
- Aplikované výchozí hodnoty:
  - Vyžadují se vzájemné závazky (pokud organizace není jen informace poskytující stranou)
  - Doba trvání: 2–3 roky standardně, až 5 let u obchodních tajemství
  - Vyžadují se standardní výjimky: nezávisle vytvořené, veřejně dostupné, legitimně získané od třetí strany, vyžadované zákonem
  - Žádná ustanovení o zákazu přetahování nebo konkurenci
  - Žádná doložka o reziduálech (nebo úzce vymezená, pokud je přítomna)
  - Rozhodné právo v rozumné obchodní jurisdikci

### Krok 3: Rychlá kontrola

Hodnoťte NDA systematicky proti každému kontrolnímu kritériu.

#### 1. Struktura smlouvy
- [ ] **Identifikován typ**: vzájemná (oboustranná) NDA, jednostranná (strana poskytující informace) nebo jednostranná (strana přijímající informace)
- [ ] **Vhodnost pro kontext**: Je typ NDA vhodný pro obchodní vztah? (např. vzájemná pro úvodní jednání, jednostranná pro jednostranné poskytování informací)
- [ ] **Samostatná smlouva**: Potvrďte, že NDA je samostatnou smlouvou, nikoli doložkou o mlčenlivosti vloženou do širší obchodní smlouvy

#### 2. Definice důvěrných informací
- [ ] **Přiměřený rozsah**: Není příliš široká (vyhněte se „všechny informace jakéhokoli druhu bez ohledu na to, zda jsou označeny jako důvěrné")
- [ ] **Požadavky na označení**: Pokud je označení vyžadováno, je prakticky proveditelné? (Písemné označení do 30 dnů od ústního sdělení je standardem.)
- [ ] **Přítomné výjimky**: Jsou definovány standardní výjimky (viz Standardní výjimky níže)
- [ ] **Žádné problematické zahrnutí**: Nedefinuje veřejně dostupné informace ani nezávisle vytvořené materiály jako důvěrné

#### 3. Povinnosti přijímající strany
- [ ] **Standard péče**: Přiměřená péče, minimálně stejná jako péče o vlastní důvěrné informace
- [ ] **Omezení použití**: Omezeno na uvedený účel
- [ ] **Omezení zpřístupnění**: Omezeno na osoby s potřebou vědět, které jsou vázány obdobnými povinnostmi
- [ ] **Žádné obtížné povinnosti**: Žádné nepraktické požadavky (např. šifrování veškeré komunikace, vedení fyzických záznamů)

#### 4. Standardní výjimky
Měly by být přítomné všechny následující výjimky:
- [ ] **Veřejně známé**: Informace, které jsou nebo se stanou veřejně dostupnými bez zavinění přijímající strany
- [ ] **Předchozí držba**: Informace již známé přijímající straně před sdělením
- [ ] **Nezávislý vývoj**: Informace vyvinuté nezávisle bez použití nebo odkazu na důvěrné informace
- [ ] **Získání od třetí strany**: Informace legitimně získané od třetí strany bez omezení
- [ ] **Zákonné vynucení**: Právo zpřístupnit informace, vyžaduje-li to zákon, regulace nebo právní proces (s oznámením poskytující straně, pokud to právo umožňuje)

#### 5. Povolené zpřístupnění
- [ ] **Zaměstnanci**: Možnost sdílet se zaměstnanci s potřebou vědět
- [ ] **Dodavatelé/poradci**: Možnost sdílet s dodavateli, poradci a profesními konzultanty vázanými obdobnými povinnostmi mlčenlivosti
- [ ] **Přidružené osoby**: Možnost sdílet s přidruženými osobami (je-li to potřebné pro obchodní účel)
- [ ] **Právní/regulatorní**: Možnost zpřístupnit, vyžaduje-li to právo nebo regulace

#### 6. Doba trvání
- [ ] **Doba trvání smlouvy**: Přiměřená doba pro obchodní vztah (1–3 roky jsou standardem)
- [ ] **Přetrvání mlčenlivosti**: Povinnosti přetrvávají přiměřenou dobu po ukončení (2–5 let je standardem; u obchodních tajemství může být déle)
- [ ] **Nikoli trvalé**: Vyhněte se neomezeným nebo trvalým povinnostem mlčenlivosti (výjimka: obchodní tajemství, která mohou odůvodnit delší ochranu)

#### 7. Vrácení a zničení
- [ ] **Spuštění povinnosti**: Při ukončení nebo na vyžádání
- [ ] **Přiměřený rozsah**: Vrácení nebo zničení důvěrných informací a všech kopií
- [ ] **Výjimka pro uchování**: Umožňuje uchování kopií vyžadovaných zákonem, regulací nebo interními pravidly compliance/zálohování
- [ ] **Potvrzení**: Potvrzení o zničení je přiměřené; přísežné prohlášení je přehnané

#### 8. Nápravné prostředky
- [ ] **Soudní zákaz**: Standardní je uznání, že porušení může způsobit nenapravitelnou újmu a spravedlivý nápravný prostředek může být vhodný
- [ ] **Žádná předem stanovená náhrada škody**: Vyhněte se doložkám o smluvních pokutách v NDA
- [ ] **Nikoli jednostranné**: Ustanovení o nápravných prostředcích se uplatňují stejně pro obě strany (u vzájemných NDA)

#### 9. Problematická ustanovení k označení
- [ ] **Žádný zákaz přetahování**: NDA by neměla obsahovat doložky o zákazu přetahování zaměstnanců
- [ ] **Žádná konkurenční doložka**: NDA by neměla obsahovat konkurenční doložky
- [ ] **Žádná výlučnost**: NDA by neměla žádnou stranu omezovat v jednáních s jinými subjekty
- [ ] **Žádný standstill**: NDA by neměla obsahovat standstill nebo obdobná restriktivní ustanovení (výjimkou je kontext M&A)
- [ ] **Žádná doložka o reziduálech** (nebo úzce vymezená): Je-li doložka o reziduálech přítomna, měla by být omezena na informace uchované v nepodporované paměti jednotlivců a neměla by se vztahovat na obchodní tajemství nebo patentované informace
- [ ] **Žádné postoupení nebo licence k IP**: NDA by neměla udělovat žádná práva k duševnímu vlastnictví
- [ ] **Žádná práva auditu**: Ve standardních NDA neobvyklé

#### 10. Rozhodné právo a jurisdikce
- [ ] **Přiměřená jurisdikce**: Zavedená obchodní jurisdikce
- [ ] **Konzistence**: Rozhodné právo a jurisdikce by měly být ve stejné nebo souvisejících jurisdikcích
- [ ] **Žádné povinné rozhodčí řízení** (u standardních NDA): Pro spory z NDA je obvykle preferován soudní spor

### Krok 4: Klasifikace

Na základě výsledků kontroly přiřaďte klasifikaci:

#### ZELENÁ — Standardní schválení

Musí platit **všechny** následující podmínky:
- NDA je vzájemná (nebo jednostranná ve správném směru)
- Všechny standardní výjimky jsou přítomny
- Doba trvání je ve standardním rozsahu (1–3 roky, přetrvání 2–5 let)
- Žádný zákaz přetahování, konkurenční doložka ani výlučnost
- Žádná doložka o reziduálech, nebo je úzce vymezená
- Přiměřená jurisdikce rozhodného práva
- Standardní nápravné prostředky (bez smluvních pokut)
- Povolená zpřístupnění zahrnují zaměstnance, dodavatele a poradce
- Ustanovení o vrácení/zničení obsahují výjimku pro uchování pro právní účely / compliance
- Definice důvěrných informací má přiměřený rozsah

**Směrování**: Schválit v rámci standardní delegace pravomocí. Revize právníka není nutná.
- **Akce**: Postoupit k podpisu v rámci standardní delegace pravomocí

#### ŽLUTÁ — Potřebná revize právníka

Je přítomno **jedno nebo více** z následujícího, ale NDA není zásadně problematická:
- Definice důvěrných informací je širší, než je preferováno, ale není nepřiměřená
- Doba trvání je delší než standard, ale v rámci tržního rozsahu (např. 5 let pro dobu trvání, 7 let pro přetrvání)
- Chybí jedna standardní výjimka, kterou lze snadno doplnit
- Je přítomna doložka o reziduálech, ale úzce vymezená na nepodporovanou paměť
- Rozhodné právo v přijatelné, ale nepreferované jurisdikci
- Drobná asymetrie ve vzájemné NDA (např. jedna strana má mírně širší povolená zpřístupnění)
- Požadavky na označení, ale prakticky proveditelné
- Vrácení/zničení bez explicitní výjimky pro uchování (pravděpodobně implikováno, ale mělo by být doplněno)
- Neobvyklá, avšak neškodlivá ustanovení (např. povinnost oznámit potenciální porušení)

**Směrování**: Označit konkrétní problémy pro revizi právníkem. Právník je pravděpodobně vyřeší drobnými úpravami v jednom revizním kole.
- **Akce**: Právník pravděpodobně vyřeší v jednom revizním kole

#### ČERVENÁ — Významné problémy

Je přítomno **jedno nebo více** z následujícího:
- **Jednostranná, kde je vyžadována vzájemná** (nebo nesprávný směr pro vztah)
- **Chybí kritické výjimky** (zejména nezávislý vývoj nebo zákonné vynucení)
- **Doložky o zákazu přetahování nebo konkurenci** vložené do NDA
- **Výlučnost nebo standstill** bez odpovídajícího obchodního kontextu
- **Nepřiměřená doba trvání** (10+ let nebo trvalá bez odůvodnění obchodním tajemstvím)
- **Příliš široká definice**, která by mohla zahrnout veřejné informace nebo nezávisle vytvořené materiály
- **Široká doložka o reziduálech**, která fakticky vytváří licenci k použití důvěrných informací
- **Postoupení nebo licence k IP** skrytá v NDA
- **Smluvní pokuty nebo sankční ustanovení**
- **Práva auditu** bez přiměřeného rozsahu nebo požadavků na oznámení
- **Velmi nepříznivá jurisdikce** s povinným rozhodčím řízením
- **Dokument ve skutečnosti není NDA** (obsahuje věcné obchodní podmínky, výlučnost nebo jiné povinnosti nad rámec mlčenlivosti)

**Směrování**: Vyžaduje plnou právní revizi. Nepodepisovat. Vyžaduje vyjednávání, protinávrh se standardním formulářem NDA organizace, nebo odmítnutí.
- **Akce**: Nepodepisovat; vyžaduje vyjednávání nebo protinávrh

### Krok 5: Generování triage reportu

Vytvořte strukturovaný report:

```
## Triage report NDA

**Klasifikace**: [ZELENÁ / ŽLUTÁ / ČERVENÁ]
**Strany**: [jména stran]
**Typ**: [Vzájemná / Jednostranná (poskytující) / Jednostranná (přijímající)]
**Doba trvání**: [délka]
**Rozhodné právo**: [jurisdikce]
**Základ revize**: [Playbook / Výchozí standardy]

## Výsledky kontroly

| Kritérium | Stav | Poznámky |
|-----------|--------|-------|
| Vzájemné povinnosti | [PASS/FLAG/FAIL] | [detaily] |
| Rozsah definice | [PASS/FLAG/FAIL] | [detaily] |
| Doba trvání | [PASS/FLAG/FAIL] | [detaily] |
| Standardní výjimky | [PASS/FLAG/FAIL] | [detaily] |
| [atd.] | | |

## Zjištěné problémy

### [Problém 1 -- ŽLUTÁ/ČERVENÁ]
**Co**: [popis]
**Riziko**: [co se může pokazit]
**Navrhované řešení**: [konkrétní znění nebo přístup]

[Opakujte pro každý problém]

## Doporučení

[Konkrétní další krok: schválit, poslat k revizi s konkrétními poznámkami, nebo odmítnout/vznést protinávrh]

## Další kroky

1. [Úkol 1]
2. [Úkol 2]
```

### Krok 6: Návrh směrování

Na základě klasifikace doporučte vhodný další krok:

| Klasifikace | Doporučená akce | Obvyklý časový rámec |
|---|---|---|
| ZELENÁ | Schválit a směrovat k podpisu v rámci delegace pravomocí | Tentýž den |
| ŽLUTÁ | Poslat určenému revizorovi s označenými konkrétními problémy | 1–2 pracovní dny |
| ČERVENÁ | Zapojit právníka pro plnou revizi; připravit protinávrh nebo standardní formulář | 3–5 pracovních dnů |

Pro klasifikace ŽLUTÁ a ČERVENÁ:
- Identifikujte konkrétní osobu nebo roli, která má provést revizi (má-li organizace definovaná pravidla směrování)
- Přiložte stručné shrnutí problémů, aby revizor rychle pochopil klíčové body
- Pokud má organizace standardní formulář NDA, doporučte jej zaslat jako protinávrh u NDA klasifikovaných jako ČERVENÉ

## Časté problémy v NDA a standardní pozice

### Problém: Příliš široká definice důvěrných informací
**Standardní pozice**: Důvěrné informace by měly být omezeny na neveřejné informace sdělené v souvislosti s uvedeným účelem, s jasně vymezenými výjimkami.
**Přístup k úpravě**: Zúžit definici na informace, které jsou označeny nebo identifikovány jako důvěrné, nebo u nichž by rozumná osoba pochopila jejich důvěrnou povahu vzhledem k jejich povaze a okolnostem sdělení.

### Problém: Chybějící výjimka pro nezávislý vývoj
**Standardní pozice**: Musí obsahovat výjimku pro informace nezávisle vyvinuté bez odkazu na důvěrné informace nebo jejich použití.
**Riziko při absenci**: Mohlo by založit nároky, že interně vyvinuté produkty nebo funkce byly odvozeny z důvěrných informací protistrany.
**Přístup k úpravě**: Doplnit standardní výjimku pro nezávislý vývoj.

### Problém: Zákaz přetahování zaměstnanců
**Standardní pozice**: Doložky o zákazu přetahování do NDA nepatří. Patří do pracovních smluv, smluv o M&A nebo konkrétních obchodních smluv.
**Přístup k úpravě**: Ustanovení zcela vypustit. Pokud protistrana trvá, omezit na cílené získávání (nikoli obecný nábor) a stanovit krátkou dobu (12 měsíců).

### Problém: Široká doložka o reziduálech
**Standardní pozice**: Doložkám o reziduálech se bránit. Je-li vyžadována, omezit na: (a) obecné myšlenky, koncepty, know-how nebo techniky uchované v nepodporované paměti osob s oprávněným přístupem; (b) výslovně vyloučit obchodní tajemství a patentovatelné informace; (c) neuděluje žádnou licenci k IP.
**Riziko, je-li příliš široká**: Fakticky uděluje licenci k použití důvěrných informací poskytující strany k jakémukoli účelu.

### Problém: Trvalá povinnost mlčenlivosti
**Standardní pozice**: 2–5 let od sdělení nebo ukončení, podle toho, co nastane později. Obchodní tajemství mohou odůvodnit ochranu po dobu, po kterou zůstávají obchodními tajemstvími.
**Přístup k úpravě**: Nahradit trvalou povinnost vymezenou dobou. Nabídnout výjimku pro obchodní tajemství s delší ochranou kvalifikujících informací.

## Poznámky

- Pokud dokument ve skutečnosti není NDA (např. je označen jako NDA, ale obsahuje věcné obchodní podmínky), okamžitě jej označte jako ČERVENÝ a doporučte plnou revizi smlouvy
- U smluv o mlčenlivosti (NDA), které jsou součástí širší smlouvy (např. doložka o mlčenlivosti v rámcové smlouvě), upozorněte, že kontext širší smlouvy může ovlivnit analýzu
- Vždy uveďte, že jde o kontrolní nástroj a právník by měl revidovat jakékoli položky, u nichž si uživatel není jistý

<!-- Origin: DirectCase pravo-skills v1.1.0 (MIT, LICENSE-directcase-pravo-skills) | Import: 2026-07-14 do ak-sladek pluginu, review bez adaptaci (Cowork-native reference OK) | Inspiration: https://www.directcase.ai/cz/cs/news/claude-legal-plugin-cs -->
