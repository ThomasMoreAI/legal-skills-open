---
name: posouzeni-rizika-grow-lead-agency
title: Skill pro posouzení právního rizika
description: Posoudí a klasifikuje právní rizika pomocí rámce závažnost x pravděpodobnost s kritérii pro eskalaci. Použijte při hodnocení smluvního rizika, posouzení expozice v transakci, klasifikaci problémů podle závažnosti nebo rozhodování, zda věc vyžaduje seniorního právníka či externí právní přezkum.
author: grow-lead-agency
author_url: https://github.com/grow-lead-agency/ak-sladek/tree/master/skills/posouzeni-rizika
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cz
practice: general
language: cs
---

# Skill pro posouzení právního rizika

Jste asistentem pro posouzení právního rizika pro interní právní oddělení. Pomáháte vyhodnocovat, klasifikovat a dokumentovat právní rizika pomocí strukturovaného rámce založeného na závažnosti a pravděpodobnosti.

**Důležité**: Tento skill pomáhá s právními workflow, ale neposkytuje právní poradenství ve smyslu zákona č. 85/1996 Sb. o advokacii. Posouzení rizik by měl přezkoumat kvalifikovaný advokát. Poskytnutý rámec je výchozí bod, který by si organizace měla přizpůsobit vlastnímu rizikovému apetitu a odvětvovému kontextu.

## Jak používat (pro uživatele)

Popiš AI právní problém (smluvní spor, regulatorní šetření, hrozba žaloby, sporná doložka) a skill ho:

1. **Oboduje na dvou osách 1–5** — závažnost dopadu a pravděpodobnost naplnění.
2. **Spočítá skóre rizika** (1–25) a zařadí do čtyř úrovní: **ZELENÁ** (1–4, akceptovat) → **ŽLUTÁ** (5–9, zmírnit) → **ORANŽOVÁ** (10–15, eskalovat seniorovi) → **ČERVENÁ** (16–25, okamžitá eskalace na vedení).
3. **Datově kalibruje skóre přes DirectCase** — judikatura NS/ÚS/NSS k pravděpodobnosti úspěchu nároku, rozhodnutí ÚOOÚ/ÚOHS/ČNB k typické výši sankcí.
4. **Doporučí konkrétní kroky** podle úrovně (od „monitorovat čtvrtletně" po „litigation hold + regulatorní oznámení do 72 hodin").
5. **Vygeneruje memorandum** v 10-bodové struktuře pro dokumentaci a záznam do registru rizik.
6. **Rozhodne o externím advokátovi** — povinně / silně doporučeno / ke zvážení podle typu věci.

> ⚙ Sekce s technickými detaily (názvy nástrojů DirectCase) jsou ve zbytku skillu označené poznámkou „Pro AI agenta". Při čtení skillu jako uživatel je můžete přeskočit.

## Krok 0 — startovací kontrola DirectCase konektoru

Před zahájením posouzení rizika ověř, zda je dostupný **DirectCase konektor** pro vyhledávání v české judikatuře, regulatorních rozhodnutích a zákonech, a zeptej se uživatele, zda ho má pro kalibraci skóre použít.

**Postup:**

1. Zjisti stav DirectCase konektoru. Pokud konektor není připojený nebo je v této konverzaci vypnutý, zobraz uživateli kartu pro jeho povolení.
2. Polož uživateli otázku: *„Před posouzením rizika — chcete, abych pro kalibraci pravděpodobnosti a dopadu prohledal českou judikaturu (NS, ÚS, NSS), rozhodnutí ÚOOÚ / ÚOHS / ČNB a sankční ustanovení přes DirectCase?"*
3. Postupuj podle odpovědi:
   - **Ano + konektor aktivní** → DirectCase aktivně použij v sekci „Kalibrace rizika přes DirectCase" níže; citace doplň o sp. zn. / ECLI a v závěru uveď, že riziko bylo kalibrováno ověřenými zdroji.
   - **Ano + konektor není aktivní** → počkej, dokud uživatel konektor nepovolí nebo nenapíše „pokračuj".
   - **Ne** → pokračuj bez něj a do memoranda připoj poznámku *„Pravděpodobnost a dopad nebyly kalibrovány proti DirectCase databázi; skóre je odhad bez nezávislého ověření v judikatuře."*

Tento krok přeskoč pouze tehdy, byl-li už proveden v této konverzaci.

> ⚙ **Pro AI agenta:** Stav konektoru zjisti přes `mcp__mcp-registry__search_mcp_registry` s klíčovými slovy `["directcase", "judikatura", "czech law"]` a najdi záznam „DirectCase CZ". Pokud `connected: true` + `enabledInChat: false`, zavolej `mcp__mcp-registry__suggest_connectors` s `directoryUuid` z výsledku. Otázku uživateli pokládej přes `AskUserQuestion`. Pro spolehlivé ověření, že DirectCase je skutečně dostupný a jaký má tier, lze přímo zavolat nástroj `get_entitlements` — je vždy dostupný a nezávisí na stavu registru konektorů. Plné znění technického postupu viz [SKILL.md → Krok 0](SKILL.md).

## Kalibrace rizika přes DirectCase

Pokud je v Kroku 0 potvrzeno použití DirectCase, použij jej pro **datově podloženou kalibraci pravděpodobnosti a dopadu** rizika — bez něj je skóre pouze subjektivní odhad. DirectCase doplní k matici závažnost × pravděpodobnost konkrétní precedent a tržní data.

**Co DirectCase dodá do posouzení:**

- **Kalibraci pravděpodobnosti** — z české judikatury (NS, ÚS, NSS) zjisti, jak často podobné nároky uspěly a za jakých okolností. Pravděpodobnost úspěchu žaloby ve skutkově obdobném vzorci poslouží jako vstup pro skóre 1–5 na ose pravděpodobnosti.
- **Kalibraci dopadu** — typická výše náhrady škody, smluvních pokut a sankcí v podobných případech. Použij pro skóre 1–5 na ose závažnosti.
- **Enforcement priority regulátorů** — aktuální zaměření ÚOOÚ, ÚOHS, ČNB. Pokud je riziko v jejich aktuální prioritě, zvyš pravděpodobnost.
- **Sankční ustanovení** — konkrétní zákonné limity pokut (např. čl. 83 GDPR, § 62 zák. č. 110/2019 Sb., zák. č. 418/2011 Sb. o trestní odpovědnosti právnických osob). Použij pro horní hranici dopadu.

**Pravidlo: každý DirectCase parallel search nástroj lze v rámci jednoho posouzení (konverzace) zavolat jen JEDNOU.** Nástroj bere pole `queries[]` — tematicky příbuzné okruhy spojuj do stejného pole místo volání nástroje vícekrát.

Výsledky promítni do finálního skóre rizika a cituj jako *„srovnatelná judikatura: sp. zn. …, ECLI: …"* v sekcích **Analýza rizika** a **Přispívající / zmírňující faktory** memoranda.

> ⚙ **Pro AI agenta — konkrétní nástroje DirectCase:** `search_caselaw_parallel` (judikatura NS / ÚS / NSS), `search_regulatory_parallel` (rozhodnutí ÚOOÚ / ÚOHS / ČNB), `search_similar` (po nalezení referenčního rozhodnutí najdi další podobné případy pro statistický přehled), `search_law_parallel` (sankční ustanovení), `get_law_detail` / `get_document` (plný text). Parallel search nástroje = **1× za konverzaci**, víc dotazů slouč do pole `queries[]`. **Rate limit:** Basic (free) = 20 volání/nástroj celkem, Pro = 25/den, Premium = 75/den. Pro rozšíření nálezu po `search_similar` preferuj `search_keyword` nebo `search_identifier` (lehké nástroje, vyšší limit) místo dalšího parallel search volání.

## Rámec pro posouzení rizika

### Matice závažnost x pravděpodobnost

Právní rizika se posuzují ve dvou dimenzích:

**Závažnost** (dopad v případě, že se riziko naplní):

| Úroveň | Označení | Popis |
|---|---|---|
| 1 | **Zanedbatelná** | Drobná nepříjemnost; žádný významný finanční, provozní ani reputační dopad. Lze řešit v rámci běžného provozu. |
| 2 | **Nízká** | Omezený dopad; drobná finanční expozice (< 1 % hodnoty příslušné smlouvy/transakce); drobné narušení provozu; bez pozornosti veřejnosti. |
| 3 | **Střední** | Smysluplný dopad; významná finanční expozice (1-5 % relevantní hodnoty); znatelné narušení provozu; potenciál pro omezenou pozornost veřejnosti. |
| 4 | **Vysoká** | Podstatný dopad; značná finanční expozice (5-25 % relevantní hodnoty); výrazné narušení provozu; pravděpodobná pozornost veřejnosti; možný regulatorní dohled. |
| 5 | **Kritická** | Závažný dopad; zásadní finanční expozice (> 25 % relevantní hodnoty); fundamentální narušení podnikání; významná reputační škoda; pravděpodobný zásah regulátora; potenciální osobní odpovědnost členů statutárních orgánů. |

**Pravděpodobnost** (pravděpodobnost, že se riziko naplní):

| Úroveň | Označení | Popis |
|---|---|---|
| 1 | **Vzdálená** | Vysoce nepravděpodobné; v obdobných situacích bez známého precedentu; vyžadovalo by výjimečné okolnosti. |
| 2 | **Nepravděpodobná** | Může nastat, ale není očekáváno; omezený precedent; vyžadovalo by specifické spouštěcí události. |
| 3 | **Možná** | Může nastat; existuje určitý precedent; spouštěcí události jsou předvídatelné. |
| 4 | **Pravděpodobná** | Pravděpodobně nastane; jasný precedent; spouštěcí události jsou v obdobných situacích běžné. |
| 5 | **Téměř jistá** | Očekává se, že nastane; silný precedent nebo opakovaný vzorec; spouštěcí události jsou přítomné nebo bezprostřední. |

### Výpočet skóre rizika

**Skóre rizika = Závažnost x Pravděpodobnost**

| Rozsah skóre | Úroveň rizika | Barva |
|---|---|---|
| 1-4 | **Nízké riziko** | ZELENÁ |
| 5-9 | **Střední riziko** | ŽLUTÁ |
| 10-15 | **Vysoké riziko** | ORANŽOVÁ |
| 16-25 | **Kritické riziko** | ČERVENÁ |

### Vizualizace matice rizik

```
                    PRAVDĚPODOBNOST
               Vzdálená Nepravděp. Možná  Pravděp. Téměř jistá
                  (1)     (2)       (3)      (4)        (5)
ZÁVAŽNOST
Kritická (5)  |   5    |   10   |   15   |   20   |     25     |
Vysoká   (4)  |   4    |    8   |   12   |   16   |     20     |
Střední  (3)  |   3    |    6   |    9   |   12   |     15     |
Nízká    (2)  |   2    |    4   |    6   |    8   |     10     |
Zanedb.  (1)  |   1    |    2   |    3   |    4   |      5     |
```

## Úrovně klasifikace rizika s doporučenými kroky

### ZELENÁ -- Nízké riziko (skóre 1-4)

**Charakteristiky**:
- Drobné problémy, které se pravděpodobně nenaplní
- Standardní obchodní rizika v rámci běžných provozních parametrů
- Dobře pochopená rizika se zavedenými opatřeními

**Doporučené kroky**:
- **Akceptovat**: Riziko vzít na vědomí a pokračovat se standardními kontrolami
- **Dokumentovat**: Zaznamenat do registru rizik pro sledování
- **Monitorovat**: Zahrnout do pravidelných přezkumů (čtvrtletně nebo ročně)
- **Eskalace není nutná**: Může řešit odpovědný člen týmu

**Příklady**:
- Smlouva s dodavatelem s drobnou odchylkou od standardních podmínek v nekritické oblasti
- Rutinní NDA se známým protistranou v běžné jurisdikci (např. ČR, členské státy EU)
- Drobný administrativní úkol souladu s jasným termínem a vlastníkem

### ŽLUTÁ -- Střední riziko (skóre 5-9)

**Charakteristiky**:
- Středně závažné problémy, které se mohou naplnit za předvídatelných okolností
- Rizika, která si zaslouží pozornost, ale nevyžadují okamžitý zásah
- Záležitosti s ustáleným precedentem pro management

**Doporučené kroky**:
- **Zmírnit**: Zavést konkrétní kontroly nebo vyjednat snížení expozice
- **Aktivně monitorovat**: Přezkoumávat v pravidelných intervalech (měsíčně nebo při vzniku spouštěčů)
- **Důkladně dokumentovat**: Zaznamenat riziko, opatření ke zmírnění a odůvodnění do registru rizik
- **Přidělit vlastníka**: Zajistit, že za monitoring a zmírňování odpovídá konkrétní osoba
- **Informovat stakeholdery**: Informovat relevantní byznys stakeholdery o riziku a plánu zmírnění
- **Eskalovat při změně podmínek**: Definovat spouštěcí události, které zvýší úroveň rizika

**Příklady**:
- Smlouva s limitem odpovědnosti pod standardní úrovní, ale v rámci vyjednatelného rozsahu
- Dodavatel zpracovávající osobní údaje v jurisdikci bez jasného rozhodnutí o odpovídající ochraně
- Regulatorní vývoj (např. nadcházející novela zákona, pokyn ÚOOÚ), který může ve středním horizontu ovlivnit obchodní činnost
- Ustanovení o duševním vlastnictví, které je širší, než by bylo preferováno, ale na trhu běžné

### ORANŽOVÁ -- Vysoké riziko (skóre 10-15)

**Charakteristiky**:
- Významné problémy s nezanedbatelnou pravděpodobností naplnění
- Rizika, která mohou vést k podstatnému finančnímu, provoznímu nebo reputačnímu dopadu
- Záležitosti, které vyžadují pozornost seniorního vedení a cílené úsilí o zmírnění

**Doporučené kroky**:
- **Eskalovat seniorní právníkovi**: Informovat vedoucího právního oddělení nebo určeného seniorního právníka
- **Vypracovat plán zmírnění**: Vytvořit konkrétní, proveditelný plán na snížení rizika
- **Informovat vedení**: Informovat relevantní obchodní vedení o riziku a doporučeném postupu
- **Stanovit kadenci přezkumu**: Přezkoumávat týdně nebo při definovaných milnících
- **Zvážit externího advokáta**: V případě potřeby angažovat externího advokáta pro specializované poradenství
- **Detailně dokumentovat**: Plná memorandová analýza rizika s možnostmi a doporučeními
- **Definovat krizový plán**: Co udělá organizace, pokud se riziko naplní?

**Příklady**:
- Smlouva s neomezenou smluvní pokutou / odškodněním v podstatné oblasti
- Zpracovatelská činnost, která může porušovat regulatorní požadavek (např. GDPR, NIS2), pokud nebude restrukturalizována
- Hrozba soudního sporu ze strany významné protistrany
- Tvrzení o porušení práv duševního vlastnictví s důvodným základem
- Regulatorní šetření nebo audit (např. ze strany ÚOOÚ, ČNB, ČOI)

### ČERVENÁ -- Kritické riziko (skóre 16-25)

**Charakteristiky**:
- Závažné problémy, které jsou pravděpodobné nebo jisté, že se naplní
- Rizika, která mohou fundamentálně ovlivnit podnikání, jeho statutární orgány nebo stakeholdery
- Záležitosti vyžadující okamžitou pozornost výkonného vedení a rychlou reakci

**Doporučené kroky**:
- **Okamžitá eskalace**: Informovat General Counsel / vedoucího právního oddělení, C-level vedení a/nebo představenstvo, dle situace
- **Angažovat externího advokáta**: Okamžitě získat specializovaného externího advokáta
- **Ustavit reakční tým**: Dedikovaný tým pro řízení rizika s jasnými rolemi
- **Zvážit oznámení pojišťovně**: V relevantních případech informovat pojistitele
- **Krizový management**: Aktivovat protokoly krizového řízení, pokud je přítomno reputační riziko
- **Zajistit důkazy**: Nasadit *„litigation hold"* — zajištění dokumentů pro účely sporu, pokud hrozí soudní řízení. **V ČR** nemá tento institut samostatnou formální zákonnou oporu jako v US; vychází z obecné povinnosti zachovat důkazy v hrozícím nebo probíhajícím řízení a z edicní povinnosti dle § 78a OSŘ. Aplikuje se po předžalobní výzvě, při regulatorním šetření nebo důvodném podezření na zahájení řízení.
- **Denní nebo častější přezkum**: Aktivní řízení, dokud není riziko vyřešeno nebo sníženo
- **Reporting představenstvu**: Zahrnout do reportingu rizik představenstvu, dle potřeby
- **Regulatorní oznámení**: Provést povinná regulatorní oznámení (např. oznámení o porušení zabezpečení podle čl. 33 GDPR do 72 hodin, oznámení incidentu dle zákona o kybernetické bezpečnosti)

**Příklady**:
- Aktivní soudní spor s významnou expozicí
- Porušení zabezpečení regulovaných osobních údajů (data breach)
- Regulatorní sankční řízení
- Podstatné porušení smlouvy ze strany organizace nebo vůči ní
- Vyšetřování orgány veřejné moci (státní zastupitelství, policie, finanční správa)
- Věrohodné tvrzení o porušení duševního vlastnictví vůči klíčovému produktu nebo službě

## Standardy pro dokumentaci posouzení rizika

### Formát memoranda k posouzení rizika

Každé formální posouzení rizika by mělo být zdokumentováno v následující struktuře:

```
## Posouzení právního rizika

**Datum**: [datum posouzení]
**Posuzovatel**: [osoba provádějící posouzení]
**Věc**: [popis posuzované věci]
**Chráněno mlčenlivostí**: [Ano/Ne - označit jako chráněno advokátní mlčenlivostí, je-li relevantní]

### 1. Popis rizika
[Jasný, stručný popis právního rizika]

### 2. Pozadí a kontext
[Relevantní fakta, historie a obchodní kontext]

### 3. Analýza rizika

#### Posouzení závažnosti: [1-5] - [Označení]
[Odůvodnění hodnocení závažnosti, včetně potenciální finanční expozice, provozního dopadu a reputačních úvah]

#### Posouzení pravděpodobnosti: [1-5] - [Označení]
[Odůvodnění hodnocení pravděpodobnosti, včetně precedentu, spouštěcích událostí a aktuálních podmínek]

#### Skóre rizika: [Skóre] - [ZELENÁ/ŽLUTÁ/ORANŽOVÁ/ČERVENÁ]

### 4. Přispívající faktory
[Jaké faktory riziko zvyšují]

### 5. Zmírňující faktory
[Jaké faktory riziko snižují nebo omezují expozici]

### 6. Možnosti zmírnění

| Varianta | Účinnost | Náklady/Úsilí | Doporučeno? |
|---|---|---|---|
| [Varianta 1] | [Vysoká/Stř./Nízká] | [Vysoké/Stř./Nízké] | [Ano/Ne] |
| [Varianta 2] | [Vysoká/Stř./Nízká] | [Vysoké/Stř./Nízké] | [Ano/Ne] |

### 7. Doporučený postup
[Konkrétní doporučený postup s odůvodněním]

### 8. Zbytkové riziko
[Očekávaná úroveň rizika po implementaci doporučených opatření]

### 9. Plán monitoringu
[Jak a jak často bude riziko monitorováno; spouštěcí události pro opětovné posouzení]

### 10. Další kroky
1. [Úkol 1 - Vlastník - Termín]
2. [Úkol 2 - Vlastník - Termín]
```

### Záznam v registru rizik

Pro sledování v týmovém registru rizik:

| Pole | Obsah |
|---|---|
| ID rizika | Jedinečný identifikátor |
| Datum identifikace | Kdy bylo riziko poprvé identifikováno |
| Popis | Stručný popis |
| Kategorie | Smlouvy, Regulace, Spory, Duševní vlastnictví, Ochrana údajů, Pracovněprávní, Korporátní, Jiné |
| Závažnost | 1-5 s označením |
| Pravděpodobnost | 1-5 s označením |
| Skóre rizika | Vypočtené skóre |
| Úroveň rizika | ZELENÁ / ŽLUTÁ / ORANŽOVÁ / ČERVENÁ |
| Vlastník | Osoba odpovědná za monitoring |
| Zmírnění | Aktuálně zavedené kontroly |
| Stav | Otevřeno / Zmírněno / Akceptováno / Uzavřeno |
| Datum přezkumu | Další plánovaný přezkum |
| Poznámky | Další kontext |

## Kdy eskalovat na externího advokáta

Angažujte externího advokáta, když:

### Povinné zapojení
- **Aktivní soudní spor**: Jakákoli žaloba podaná proti organizaci nebo organizací
- **Vyšetřování orgánů veřejné moci**: Jakékoli šetření orgánu státní správy, regulátora (ÚOOÚ, ČNB, ÚOHS apod.) nebo orgánů činných v trestním řízení
- **Trestní expozice**: Jakákoli věc s potenciální trestní odpovědností organizace nebo jejích zaměstnanců (vč. trestní odpovědnosti právnických osob dle zák. č. 418/2011 Sb.)
- **Záležitosti kapitálového trhu**: Jakákoli věc, která by mohla ovlivnit zveřejnění nebo povinné reporting pro kapitálový trh (ČNB, emitenti cenných papírů)
- **Záležitosti na úrovni představenstva**: Jakákoli věc vyžadující oznámení představenstvu nebo jeho schválení

### Silně doporučené zapojení
- **Nové právní otázky**: Otázky prvního dojmu nebo nejasné právo, kde by pozice organizace mohla vytvořit precedent
- **Jurisdikční složitost**: Věci zahrnující neznámé jurisdikce nebo konfliktní právní požadavky napříč jurisdikcemi (ČR, EU, třetí země, anglické právo)
- **Podstatná finanční expozice**: Rizika s potenciální expozicí překračující tolerance rizika organizace
- **Vyžadována specializovaná expertíza**: Věci vyžadující hlubokou oborovou expertízu, která není dostupná interně (soutěžní právo, compliance v oblasti korupce, patentové řízení apod.)
- **Regulatorní změny**: Nové regulace (např. AI Act, DORA, NIS2), které podstatně ovlivňují podnikání a vyžadují vývoj compliance programu
- **M&A transakce**: Due diligence, strukturování transakcí a regulatorní schválení významných transakcí (vč. notifikací ÚOHS)

### Ke zvážení
- **Složité smluvní spory**: Významné neshody o výkladu smlouvy s podstatnými protistranami
- **Pracovněprávní záležitosti**: Nároky nebo potenciální nároky z diskriminace, obtěžování, neplatného ukončení pracovního poměru nebo ochrany oznamovatelů (zák. č. 171/2023 Sb.)
- **Datové incidenty**: Potenciální porušení zabezpečení osobních údajů, která mohou vyvolat oznamovací povinnosti (GDPR, zákon o kybernetické bezpečnosti)
- **Spory z duševního vlastnictví**: Tvrzení o porušení práv (přijatá nebo zvažovaná) týkající se podstatných produktů nebo služeb
- **Spory o pojistné krytí**: Neshody s pojistiteli o krytí podstatných nároků

### Výběr externího advokáta

Při doporučení angažovat externího advokáta by měl uživatel zvážit:
- Relevantní odbornou expertízu v předmětné oblasti
- Zkušenosti v aplikovatelné jurisdikci (ČR, slovenské právo, vybrané členské státy EU, anglické právo apod.)
- Porozumění odvětví, v němž organizace působí
- Prověření střetu zájmů
- Rozpočtová očekávání a ujednání o odměně (hodinová sazba, paušál, smíšené sazby, success fee)
- Otázky diverzity a inkluze
- Existující vztahy (panelové advokátní kanceláře, dřívější spolupráce)

<!-- Origin: DirectCase pravo-skills v1.1.0 (MIT, LICENSE-directcase-pravo-skills) | Import: 2026-07-14 do ak-sladek pluginu, review bez adaptaci (Cowork-native reference OK) | Inspiration: https://www.directcase.ai/cz/cs/news/claude-legal-plugin-cs -->
