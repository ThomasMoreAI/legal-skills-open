---
name: revize-smlouvy-grow-lead-agency
title: /revize-smlouvy -- Revize smlouvy oproti playbooku
description: Proveďte revizi smlouvy oproti vyjednávacímu playbooku vaší organizace — označte odchylky, vygenerujte návrhy úprav (redlines) a poskytněte analýzu obchodních dopadů. Použijte při revizi smluv s dodavateli nebo zákazníky, když potřebujete analýzu ustanovení po ustanovení proti standardním pozicím, nebo při přípravě vyjednávací strategie s prioritizovanými návrhy úprav a ústupovými pozicemi.
author: grow-lead-agency
author_url: https://github.com/grow-lead-agency/ak-sladek/tree/master/skills/revize-smlouvy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cz
practice: contracts
language: cs
---

# /revize-smlouvy -- Revize smlouvy oproti playbooku

> Pokud narazíte na neznámé zástupné symboly nebo si potřebujete ověřit, které nástroje jsou připojeny, viz [CONNECTORS.md](../../CONNECTORS.md).

Proveďte revizi smlouvy oproti vyjednávacímu playbooku (interní příručce) vaší organizace. Analyzujte jednotlivá ustanovení, označte odchylky, vygenerujte návrhy úprav (redlines) a poskytněte analýzu obchodních dopadů.

**Důležité**: Tento plugin pomáhá s právními workflow, ale neposkytuje právní poradenství ve smyslu zákona č. 85/1996 Sb. o advokacii. Veškeré závěry ověřte u kvalifikovaného advokáta.

## Jak používat (pro uživatele)

Vyvolej skill `/revize-smlouvy` a přilož smlouvu (PDF, DOCX nebo vložený text). AI provede:

1. **KYC protistrany** v obchodním rejstříku přes DirectCase (existence, statutární orgán, oprávnění k podpisu, insolvence/likvidace).
2. **Analýzu doložek** proti vyjednávacímu playbooku organizace (nebo proti obecným tržním standardům, pokud playbook není nastavený).
3. **Ověření judikatury** ke sporným ustanovením v české soudní praxi (NS, ÚS, NSS) přes DirectCase.
4. **Klasifikaci nálezů** na **Kritické** (eskalace, deal-breaker), **K revizi** (vyjednatelné) a OK.
5. **Vygenerování výstupu** podle vaší volby — ve výchozím nastavení shrnutí v chatu + Word kopie smlouvy s barevně odlišenými komentáři u problémových míst.

> ⚙ Sekce s technickými detaily (názvy nástrojů, generování Word souboru, XML) jsou ve zbytku skillu označené poznámkou „Pro AI agenta". Při čtení skillu jako uživatel je můžete přeskočit.

## Krok 0 — startovací kontrola DirectCase konektoru

Před zahájením revize ověř, zda je dostupný **DirectCase konektor** pro vyhledávání v české judikatuře, zákonech a obchodním rejstříku, a zeptej se uživatele, zda ho má v revizi použít.

**Postup:**

1. Zjisti stav DirectCase konektoru. Pokud konektor není připojený nebo je v této konverzaci vypnutý, zobraz uživateli kartu pro jeho povolení.
2. Polož uživateli otázku: *„Před revizí — chcete, abych přes DirectCase ověřil protistranu v obchodním rejstříku (KYC), prohledal judikaturu k jednotlivým doložkám a aktuální zákonná ustanovení?"*
3. Postupuj podle odpovědi:
   - **Ano + konektor aktivní** → DirectCase aktivně používej v Kroku 2.5 (KYC) a v Kroku 4 (judikatorní rešerše).
   - **Ano + konektor není aktivní** → počkej, dokud uživatel konektor nepovolí nebo nenapíše „pokračuj".
   - **Ne** → pokračuj bez něj a v závěru jasně uveď, že KYC protistrany a citace judikatury nebyly nezávisle ověřeny.

Tento krok přeskoč pouze tehdy, byl-li už proveden v této konverzaci.

> ⚙ **Pro AI agenta:** Stav konektoru zjisti přes `mcp__mcp-registry__search_mcp_registry` s klíčovými slovy `["directcase", "judikatura", "czech law", "obchodní rejstřík"]` a najdi záznam „DirectCase CZ". Pokud `connected: true` + `enabledInChat: false`, zavolej `mcp__mcp-registry__suggest_connectors` s `directoryUuid` z výsledku. Otázku uživateli pokládej přes `AskUserQuestion`. Pro spolehlivé ověření, že DirectCase je skutečně dostupný a jaký má tier (Basic/Pro/Premium), lze přímo zavolat nástroj `get_entitlements` — je vždy dostupný a nezávisí na stavu registru konektorů. Plné znění technického postupu viz [SKILL.md → Krok 0](SKILL.md).

## Vyvolání

```
/revize-smlouvy <soubor se smlouvou nebo URL>
```

Proveďte revizi smlouvy: @$1

## Pracovní postup

### Krok 1: Převzetí smlouvy

Smlouvu lze převzít v libovolném z těchto formátů:
- **Nahraný soubor**: PDF, DOCX nebo jiný formát dokumentu
- **URL**: Odkaz na smlouvu v CLM systému, cloudovém úložišti (např. Box, Egnyte, SharePoint) nebo jiném systému pro správu dokumentů
- **Vložený text**: Text smlouvy vložený přímo do konverzace

Pokud smlouva není poskytnuta, vyzvěte uživatele, aby ji dodal.

### Krok 2: Získání kontextu

Před zahájením revize se uživatele zeptejte na kontext (ideálně přes `AskUserQuestion`):

1. **Na které straně stojíte?** (dodavatel/poskytovatel, zákazník/odběratel, poskytovatel licence, nabyvatel licence, partner — nebo jiné). Tato odpověď určuje, koho v Kroku 2.5 ověřit jako protistranu.
2. **Termín**: Kdy musí být smlouva finalizována? (Ovlivňuje prioritizaci jednotlivých otázek.)
3. **Klíčové oblasti**: Máte konkrétní obavy? (např. „ochrana osobních údajů je zásadní", „potřebujeme flexibilitu v době trvání", „vlastnictví duševního vlastnictví je klíčové téma")
4. **Kontext obchodu**: Jaký je relevantní obchodní kontext? (např. velikost obchodu, strategický význam, stávající vztah)
5. **Preferovaný formát výstupu** (výchozí volba = obojí). Nabídni možnosti:
   - **Shrnutí v chatu a Word s komentáři** (doporučeno, výchozí)
   - **Pouze shrnutí v chatu** — bez generování Word dokumentu
   - **Pouze Word dokument s komentáři** — bez delšího shrnutí v chatu
   - **Jiné** — uživatel může zadat vlastní formát (např. PDF, prezentace, e-mail s odrážkami)

Pokud uživatel poskytne pouze částečný kontext, pokračujte s tím, co máte, a zaznamenejte učiněné předpoklady. Vybraný formát výstupu si zapamatuj pro Krok 7 a sekci „Formát výstupu".

### Krok 2.5: KYC ověření protistrany přes DirectCase

Pokud je v Kroku 0 potvrzeno použití DirectCase, **před analýzou doložek** ověř protistranu v **českém obchodním rejstříku přes DirectCase MCP konektor**. Vyhledávání v OR nemusíš (a nemáš) provádět ručně mimo DirectCase — konektor poskytuje přímý přístup k aktuálním datům z obchodního, živnostenského a insolvenčního rejstříku v rámci jednoho dotazu.

Tento krok často odhalí blokující problémy dříve, než se dojde ke smluvním ustanovením (neexistující subjekt, špatný signatář, probíhající insolvence).

> **KYC ověřuj pouze protistranu**, nikoli stranu uživatele. Pokud z Kroku 2 není jednoznačné, kterou stranu uživatel zastupuje (a tedy která je protistrana), zeptej se před zahájením KYC přes `AskUserQuestion`: „Za kterou stranu smlouvy provádím revizi? Druhou stranu pak ověřím v OR jako protistranu."

#### 2.5.1 Existence a aktuální údaje

Pomocí **DirectCase MCP** vyhledej protistranu v obchodním rejstříku podle obchodního názvu nebo IČO uvedeného v hlavičce smlouvy a získej výpis. Z výpisu ověř a porovnej s hlavičkou smlouvy:

- **Obchodní název, IČO, sídlo, datum vzniku** — shoda s hlavičkou smlouvy. Případný rozdíl označ.
- **Předmět podnikání / živnostenské oprávnění** — má protistrana oprávnění k tomu, co podle smlouvy plní? (Např. „činnost účetních poradců, vedení účetnictví, vedení daňové evidence" je vázaná živnost vyžadovaná u účetní smlouvy.)
- **Datum poslední změny v OR** — pokud hlavička obsahuje staré údaje, mohou být neaktuální.

> ⚙ **Pro AI agenta — konkrétní nástroje DirectCase:** `search_company` (hledání podle názvu, užitečné, když IČO chybí nebo je v hlavičce prázdné pole), `search_identifier` (přesné hledání podle IČO), `search_company_documents` (sbírka listin — stanovy, výkazy, smlouvy o sloučení, změny statutárního orgánu), `convert_file_to_markdown` (přečtení konkrétního dokumentu ze sbírky listin, je-li potřeba — funguje jen pro důvěryhodné právní domény jako justice.cz; **PDF mimo tyto domény převáděj lokálně**, ne přes DirectCase).

#### 2.5.2 Oprávnění k podpisu

Z výpisu z OR (stejný dotaz na DirectCase jako v 2.5.1) zjisti **statutární orgán** a **způsob jednání za společnost**. Typické varianty:

- „Jednatel jedná za společnost samostatně" → každý jednatel může podepsat sám.
- „Společnost zastupují vždy dva jednatelé společně" → jeden podpis je nedostatečný.
- „Společnost zastupuje jednatel společně s prokuristou" / „dva členové představenstva" → ověř všechny varianty.

Porovnej se signatářem ve smlouvě:

- **Pokud podepisuje jednatel uvedený v OR a způsob jednání to umožňuje** → OK, zaznamenej do KYC sekce.
- **Pokud podepisuje někdo jiný než statutární orgán** → ke smlouvě musí být přiložena **písemná plná moc** dle § 441 OZ, nebo na ni musí být v textu smlouvy odkázáno. Plná moc musí obsahovat výslovné oprávnění k podpisu této konkrétní smlouvy nebo k danému typu jednání. **Pokud plná moc chybí, označ nález jako ČERVENÝ a požádej o její doložení.**
- **Pokud podepisuje prokurista** → prokura nezahrnuje zcizení a zatížení nemovitostí, není-li v zápisu uvedeno jinak (§ 453 OZ); ověř rozsah prokury.

#### 2.5.3 Insolvence a likvidace

Ze stejného výpisu z DirectCase (sekce z insolvenčního rejstříku a údaj o probíhající likvidaci) ověř:

- **Probíhající insolvenční řízení** — pokud DirectCase uvádí insolvenci, smlouva typicky nesmí být uzavřena bez souhlasu insolvenčního správce; hrozí neúčinnost právních úkonů dle § 240–241 InsZ.
- **Likvidace** — společnost v likvidaci jedná pouze v rozsahu nutném k ukončení činnosti (§ 196 OZ); uzavření dlouhodobého smluvního vztahu s ní je sporné.

> **Poznámka:** Aktivní exekuce, daňové nedoplatky ani historie soudních sporů **nejsou součástí tohoto KYC kroku** — v běžném výpisu z OR tato data nejsou. Pokud je některá z těchto skutečností pro obchod klíčová (velký smluvní závazek, dlouhodobá vazba, regulovaný sektor), doporuč uživateli ruční kontrolu v Centrální evidenci exekucí (CEE) a u Finanční správy.

> ⚙ **Pro AI agenta:** Insolvenční status je součástí výsledku `search_company` (sekce „insolvencni_rejstrik"). Pro hlubší kontrolu lze použít `search_company_documents` (sbírka listin obsahuje informaci o likvidaci, sloučení atd.).

#### 2.5.4 Výstup KYC

Krátké shrnutí (4–6 řádků) zařaď do sekce **„Klíčová zjištění"** závěrečné revize:

- Identifikace protistrany **potvrzena / odmítnuta** (s odkazem na konkrétní výpis z OR).
- Signatář **oprávněn / vyžaduje doplnění plné moci / vyžaduje další podpis**.
- **Insolvence / likvidace**: ANO (popis rizika) / NE.

Pokud KYC odhalí blokující problém (nesoulad signatáře, insolvence, neexistující subjekt), **upozorni uživatele před analýzou doložek** a zeptej se přes `AskUserQuestion`, zda má v revizi pokračovat.

### Krok 3: Načtení playbooku

Vyhledejte playbook pro revizi smluv vaší organizace v lokálním nastavení (např. `legal.local.md` nebo podobné konfigurační soubory).

Playbook by měl definovat:
- **Standardní pozice**: Preferované podmínky organizace pro každý důležitý typ ustanovení
- **Přijatelné rozsahy**: Podmínky, které lze odsouhlasit bez eskalace
- **Spouštěče eskalace**: Podmínky vyžadující revizi vedoucím právníkem nebo zapojení externího advokáta

**Pokud není žádný playbook nakonfigurován:**
- Informujte uživatele, že playbook nebyl nalezen
- Nabídněte dvě možnosti:
  1. Pomoci uživateli s nastavením playbooku (projít definici pozic pro klíčová ustanovení)
  2. Pokračovat v obecné revizi s využitím široce uznávaných obchodních standardů jako výchozího měřítka
- Při obecném postupu jasně uveďte, že revize vychází z obecných obchodních standardů, nikoli z konkrétních pozic organizace

### Krok 4: Analýza ustanovení po ustanovení

#### Využití DirectCase MCP pro autoritativní kontext

Pokud je v Kroku 0 potvrzeno použití DirectCase, použij jej k doplnění analýzy o aktuální českou judikaturu, zákonná ustanovení a regulatorní stanoviska. Cílem je, aby každé ČERVENÉ a ŽLUTÉ označení bylo podloženo aktuální soudní praxí, nikoli pouze obecným tvrzením.

##### Povinná judikatorní rešerše

Ověř relevantní judikaturu v české soudní praxi (NS, ÚS, NSS) přes DirectCase. **Jeden vyhledávací dotaz (jedna položka v poli `queries[]`) typicky pokryje všechny související doložky** — všechno z odpovědnosti, sankcí a lhůt sloučíš do jedné položky. Pokud má smlouva tematicky úplně různé okruhy (odpovědnost vs. arbitráž vs. licenční IP), přidej je jako další položky do stejného pole `queries[]` v rámci **jediného volání** `search_caselaw_parallel` za celou revizi smlouvy (nástroj lze zavolat jen 1× za konverzaci). Témata, která mají být pokryta (jsou-li ve smlouvě relevantní):

- **Smluvní pokuty** — moderace dle § 2051 OZ, kritéria přiměřenosti (poměr k hodnotě plnění, typ porušené povinnosti, předvídatelnost škody, vztah ke smluvnímu úroku z prodlení).
- **Omezení odpovědnosti** — § 2898 OZ (zákaz vyloučení odpovědnosti za úmysl a hrubou nedbalost), výklad „hrubé nedbalosti" u profesních služeb, vyloučení nepřímých a následných škod, asymetrické limity.
- **Úroky z prodlení** — moderace nepřiměřených smluvních úroků z prodlení dle § 1972 OZ a § 6 OZ (dobré mravy), hranice oproti zákonné sazbě dle nař. vlády č. 351/2013 Sb.
- **Hranice dobrých mravů u výslovně zkrácených lhůt a sankcí** — smluvní zkrácení promlčecí lhůty dle § 630 OZ, smluvní zkrácení reklamačních a prekluzivních lhůt pro uplatnění nároků; meze dobrých mravů (§ 1, § 6 OZ) a ochrana slabší strany (§ 433 OZ); nepřiměřené sankce vázané na prodlení.
- **Podstatné porušení smlouvy** — § 2002 OZ a co soudní praxe považuje za podstatné porušení (rozdíl mezi podstatným a nepodstatným, vliv na možnost odstoupení s okamžitou účinností, povinnost dodatečné lhůty k nápravě).
- **Platnost rozhodčích doložek** — pokud smlouva obsahuje arbitráž: požadavky na ad hoc rozhodce, neplatnost doložek směřujících na konkrétního rozhodce bez transparentního výběru, rozhodčí doložky ve spotřebitelských smlouvách, výklad § 2 a § 3 zák. č. 216/1994 Sb.

> **Pravidlo: každý DirectCase parallel search nástroj lze v rámci jedné revize (konverzace) zavolat jen JEDNOU.** Nástroj ale bere pole `queries[]` — všechny tematicky příbuzné dotazy (odpovědnost, sankce, lhůty…) slouč do JEDNOHO volání s více položkami v poli, místo volání nástroje vícekrát. Pokud má smlouva tematicky úplně různé okruhy (odpovědnost vs. arbitráž vs. licenční IP), zahrň je jako samostatné položky ve stejném poli `queries[]` — pořád jde o jedno volání nástroje.
>
> ⚙ **Pro AI agenta:** Konkrétní nástroje jsou `search_caselaw_parallel` (judikatura), `search_law_parallel` (zákony), `search_regulatory_parallel` (regulatorika). Každý z nich lze zavolat jen **1× za konverzaci** — víc dotazů slouč do pole `queries[]` v jednom volání. **Rate limit:** Basic (free) = 20 volání/nástroj celkem (fakticky lifetime cap), Pro = 25/den, Premium = 75/den. Šetři volání — pro follow-up dotazy k už nalezenému rozhodnutí preferuj `search_keyword` nebo `search_identifier` (lehké nástroje s vyšším limitem: Basic 20, Pro 200/den) místo dalšího parallel search volání.

##### Doplňková rešerše pro netradiční / kontroverzní / redlinované doložky

Pokud při analýze narazíš na doložku, která je:

- **netradiční** — formulace nebo typ závazku, který není standardní pro daný typ smlouvy (např. nepojmenovaná povinnost, neobvyklé propojení odpovědnosti, atypický mechanismus krácení odměny);
- **kontroverzní** — nepřiměřeně tvrdá, asymetrická, na hraně platnosti nebo dobrých mravů;
- **redlinovaná protistranou** v aktuálním kole jednání;
- **vlastní redline uživatele**, který chceš podepřít argumentací,

→ zahrň **doplňující dotaz k judikatuře** s úzce zaměřeným zněním na konkrétní doložku jako další položku do stejného volání `search_caselaw_parallel` (pole `queries[]`) — nástroj lze za konverzaci zavolat jen jednou, takže povinnou i doplňkovou rešerši sluč do jednoho volání s více dotazy. Citaci promítni do odůvodnění redline ve formě *„V případě sporu by soud podle linie NS sp. zn. … pravděpodobně …"* nebo *„NS opakovaně judikoval, že … (sp. zn. …)".*

##### Zákonný rámec a regulatorika

Doplň analýzu o:

- **Relevantní ustanovení zákonů** k typu smlouvy (např. § 2079+ OZ pro kupní smlouvu, § 1746 odst. 2 OZ pro nepojmenované, § 2358+ OZ pro licenční, § 2586+ OZ pro smlouvu o dílo, zák. č. 563/1991 Sb. pro účetnictví, GDPR + zák. č. 110/2019 Sb. pro DPA, zák. č. 134/2016 Sb. pro veřejné zakázky).
- **Stanoviska regulátorů** (ÚOOÚ pro DPA a předání mimo EU, ÚOHS pro exkluzivitu a vertikální omezení, ČNB pro finanční služby, KAČR pro účetnictví, NÚKIB pro NIS2).
- **Plný text klíčových ustanovení nebo rozhodnutí** pro přesnou citaci v redline.

> ⚙ **Pro AI agenta:** Konkrétní nástroje DirectCase: `search_law_parallel` (zákony), `search_regulatory_parallel` (regulatorika), `get_law_detail` / `get_document` (plný text).

##### Citace ve výstupu

Každé tvrzení o judikatuře musí být ve výstupu doplněno identifikátorem rozhodnutí: **sp. zn. / ECLI / č. Sb. + datum**. Pokud se citace odvolává na konkrétní právní větu, uveď ji v uvozovkách. **Bez identifikátoru z DirectCase citaci nepoužívej** — hrozí chybná nebo neexistující citace.

#### Obecný postup revize

Použijte následující postup revize:

1. **Identifikujte typ smlouvy**: smlouva o SaaS, profesionální služby, licence, partnerství, nákup atd. Typ smlouvy ovlivňuje, která ustanovení jsou nejvýznamnější.
2. **Určete stranu uživatele**: dodavatel, zákazník, poskytovatel licence, nabyvatel licence, partner. Tento aspekt zásadně mění analýzu (např. omezení odpovědnosti chrání jiné strany v různých situacích).
3. **Přečtěte celou smlouvu** dříve, než začnete označovat problémy. Ustanovení na sebe vzájemně působí (např. neomezené odškodnění může být částečně zmírněno širokým omezením odpovědnosti).
4. **Analyzujte každé významné ustanovení** oproti pozici v playbooku.
5. **Posuďte smlouvu jako celek**: Je celkové rozložení rizik a obchodních podmínek vyvážené?

Analyzujte smlouvu systematicky, minimálně v následujícím rozsahu:

| Kategorie ustanovení | Klíčové body revize |
|----------------|-------------------|
| **Omezení odpovědnosti** | Výše limitu, výjimky, vzájemné vs. jednostranné, následné škody |
| **Vlastnictví duševního vlastnictví** | Stávající IP, nově vytvořené IP, dílo na objednávku, licenční ujednání, postoupení |
| **Ochrana osobních údajů** | Potřeba DPA, podmínky zpracování, subzpracovatelé, oznámení o porušení, přeshraniční předání |
| **Mlčenlivost** | Rozsah, doba trvání, výjimky, povinnosti vrácení/zničení |
| **Prohlášení a záruky** | Rozsah, zbavení odpovědnosti, doba přetrvání |
| **Doba trvání a ukončení** | Délka, obnovení, výpověď bez udání důvodu, odstoupení z důvodu porušení, ukončovací lhůta |
| **Rozhodné právo a řešení sporů** | Jurisdikce, místo, rozhodčí řízení vs. soudní spor |
| **Pojištění** | Požadavky na krytí, minima, doklady o pojištění |
| **Postoupení smlouvy** | Požadavky na souhlas, změna ovládání, výjimky |
| **Vyšší moc** | Rozsah, oznámení, právo na ukončení |
| **Platební podmínky** | Splatnost, úroky z prodlení, daně, navyšování cen |

U každého ustanovení posuďte soulad s playbookem (nebo obecnými standardy) a uveďte, zda je přítomné, chybí, nebo je neobvyklé.

#### Podrobné pokyny k jednotlivým ustanovením

##### Omezení odpovědnosti

**Klíčové prvky k revizi:**
- Výše limitu (pevná částka, násobek poplatků nebo neomezeně)
- Zda je limit vzájemný, nebo se vztahuje na každou stranu odlišně
- Výjimky z limitu (které závazky jsou neomezené)
- Zda jsou vyloučeny následné, nepřímé, zvláštní nebo sankční škody
- Zda je vyloučení vzájemné
- Výjimky z vyloučení následných škod
- Zda se limit uplatňuje na jednotlivý nárok, ročně, nebo kumulativně

**Časté problémy:**
- Limit nastavený na zlomek zaplacených poplatků (např. „poplatky zaplacené za předchozí 3 měsíce" u smlouvy s nízkou hodnotou)
- Asymetrické výjimky zvýhodňující stranu, která návrh sepsala
- Široké výjimky, které fakticky limit ruší (např. „jakékoliv porušení článku X", přičemž článek X pokrývá většinu povinností)
- Chybějící vyloučení následných škod pro porušení jedné ze stran

##### Duševní vlastnictví

**Klíčové prvky k revizi:**
- Vlastnictví stávajícího IP (každá strana by si měla ponechat své)
- Vlastnictví IP vytvořeného během plnění
- Ustanovení o díle na objednávku a jejich rozsah
- Licenční ujednání: rozsah, výlučnost, území, právo udělovat podlicence
- Zohlednění open source
- Ustanovení o zpětné vazbě (licence na návrhy či zlepšení)

**Časté problémy:**
- Široké postoupení IP, které by mohlo zahrnout stávající IP zákazníka
- Ustanovení o díle na objednávku sahající nad rámec dodávek
- Neomezená ustanovení o zpětné vazbě udělující trvalé, neodvolatelné licence
- Rozsah licence širší, než vyžaduje obchodní vztah

##### Ochrana osobních údajů

**Klíčové prvky k revizi:**
- Zda je vyžadována smlouva/dodatek o zpracování osobních údajů (DPA)
- Klasifikace jako správce vs. zpracovatel osobních údajů
- Práva subzpracovatelů a povinnosti oznamování
- Lhůta pro oznámení porušení zabezpečení osobních údajů (72 hodin podle GDPR, čl. 33)
- Mechanismy přeshraničního předání (standardní smluvní doložky (SCC), rozhodnutí o odpovídající úrovni ochrany, závazná podniková pravidla)
- Povinnosti výmazu nebo vrácení údajů při ukončení
- Požadavky na zabezpečení údajů a práva auditu
- Omezení účelu zpracování údajů

Aplikovatelné předpisy zahrnují GDPR a zák. č. 110/2019 Sb. o zpracování osobních údajů.

**Časté problémy:**
- Chybějící DPA při zpracování osobních údajů
- Plošné oprávnění pro subzpracovatele bez oznamovací povinnosti
- Lhůta pro oznámení porušení delší, než vyžaduje regulace
- Chybějící ochrana přeshraničních předání, pokud se data pohybují mezinárodně
- Nedostatečná ustanovení o výmazu údajů

##### Doba trvání a ukončení

**Klíčové prvky k revizi:**
- Počáteční doba trvání a podmínky obnovení
- Ustanovení o automatickém obnovení a lhůty pro vypovězení
- **Výpověď bez udání důvodu** (ukončení bez konkrétního porušení): je možná? jaká je výpovědní doba? jsou poplatky za předčasné ukončení?
- **Odstoupení z důvodu porušení**: lhůta k nápravě? co zakládá podstatné porušení podle § 2002 OZ?
- Důsledky ukončení: vrácení dat, asistence při přechodu, ustanovení trvající i po ukončení smlouvy
- Ukončovací lhůta a povinnosti v jejím rámci

**Časté problémy:**
- Dlouhá počáteční doba bez možnosti výpovědi bez udání důvodu
- Automatické obnovení s krátkými lhůtami pro vypovězení (např. 30denní lhůta při ročním obnovení)
- Chybějící lhůta k nápravě u odstoupení z důvodu porušení
- Nedostatečná ustanovení o asistenci při přechodu k novému dodavateli
- Ustanovení trvající i po ukončení smlouvy, která ji fakticky prodlužují na neurčito

##### Rozhodné právo a řešení sporů

**Klíčové prvky k revizi:**
- Volba práva (rozhodné právo)
- Mechanismus řešení sporů (soudní řízení, rozhodčí řízení, prioritní mediace)
- Místo a soudní příslušnost pro spor
- Pravidla a místo rozhodčího řízení (je-li zvoleno)
- Úhrada nákladů advokáta vítězné straně

**Časté problémy:**
- Nepříznivá jurisdikce (neobvyklé nebo vzdálené místo)
- Povinné rozhodčí řízení s pravidly zvýhodňujícími navrhovatele
- Chybějící eskalační proces před zahájením formálního řešení sporu

> **Pokud je smlouva pod cizím právem (US, UK):** Pozornost na **class action waiver** a **jury waiver**. Tyto doložky **v ČR nejsou aplikovatelné** (ČR civilní řízení nezná porotu; česká kolektivní žaloba podle zák. č. 179/2024 Sb. má opt-in model a u spotřebitelských smluv waiver neplatí — § 1813 OZ). Pro americkou matku zaměstnavatele nebo zahraniční investora ale mohou být důležité — doporuč konzultaci se zahraničním ko-právním poradcem.

### Krok 5: Označení odchylek

Klasifikujte každou odchylku od playbooku pomocí třístupňového systému:

#### ZELENÁ — Přijatelné

Ustanovení je v souladu se standardní pozicí organizace, nebo je dokonce výhodnější. Drobné odchylky, které jsou obchodně rozumné a významně nezvyšují riziko.

**Příklady:**
- Limit odpovědnosti na úrovni 18 měsíčních poplatků, když standard je 12 (výhodnější pro zákazníka)
- Vzájemná NDA s dobou trvání 2 roky, když standard jsou 3 roky (kratší, ale rozumné)
- Rozhodné právo v zavedené obchodní jurisdikci blízké té preferované

**Akce**: Zaznamenat pro informaci. Vyjednávání není nutné.

#### ŽLUTÁ — Vyjednávat

Ustanovení je mimo standardní pozici, ale v rámci vyjednatelného rozsahu. Je na trhu běžné, ale neodpovídá preferenci organizace. Vyžaduje pozornost a pravděpodobně jednání, nikoli však eskalaci.

**Příklady:**
- Limit odpovědnosti na 6 měsíců poplatků, když standard je 12 (pod standardem, ale vyjednatelné)
- Jednostranné odškodnění za porušení IP, kdy standardem je vzájemnost (běžná tržní pozice, ale nepreferovaná)
- Automatické obnovení s 60denní výpovědní lhůtou, když standard je 90 dní
- Rozhodné právo v přijatelné, ale nepreferované jurisdikci

**Akce**: Vygenerujte konkrétní text návrhu úpravy (redline). Poskytněte ústupovou pozici. Odhadněte obchodní dopady přijetí vs. vyjednávání.
- **Zahrnout**: Konkrétní text návrhu úpravy, který vrátí ustanovení ke standardní pozici
- **Zahrnout**: Ústupovou pozici pro případ, že protistrana nepřistoupí na primární návrh
- **Zahrnout**: Obchodní dopad přijetí v původní podobě vs. vyjednávání

#### ČERVENÁ — Eskalovat

Ustanovení je mimo přijatelný rozsah, splňuje některý z definovaných spouštěčů eskalace nebo představuje významné riziko. Vyžaduje revizi vedoucím právníkem, zapojení externího advokáta nebo schválení obchodním rozhodujícím subjektem.

**Příklady:**
- Neomezená odpovědnost nebo chybějící ustanovení o omezení odpovědnosti
- Jednostranné široké odškodnění bez limitu
- Postoupení stávajícího IP
- Chybějící DPA při zpracování osobních údajů
- Nepřiměřené konkurenční doložky nebo výlučnost
- Rozhodné právo v problematické jurisdikci s povinným rozhodčím řízením

**Akce**: Vysvětlete konkrétní riziko. Poskytněte tržně standardní alternativní znění. Odhadněte expozici. Doporučte eskalační cestu.
- **Zahrnout**: Proč je to ČERVENÉ (konkrétní riziko)
- **Zahrnout**: Jak vypadá standardní tržní pozice
- **Zahrnout**: Obchodní dopad a potenciální expozici
- **Zahrnout**: Doporučenou eskalační cestu

### Krok 6: Generování návrhů úprav (redlines)

Pro každou ŽLUTOU a ČERVENOU odchylku poskytněte:
- **Současné znění**: Citujte příslušný text smlouvy
- **Navrhovaný redline**: Konkrétní alternativní znění
- **Odůvodnění**: Stručné vysvětlení vhodné ke sdílení s protistranou
- **Priorita**: Zda jde o nezbytné (must-have) nebo vítané (nice-to-have) při vyjednávání

#### Osvědčené postupy při tvorbě redlines

Při generování návrhů úprav:

1. **Buďte konkrétní**: Uveďte přesné znění, nikoli vágní pokyny. Redline má být připravený k vložení.
2. **Buďte vyvážení**: Navrhujte znění, které je pevné u kritických bodů, ale obchodně rozumné. Přehnaně agresivní redlines zpomalují jednání.
3. **Vysvětlete důvod**: Přiložte stručné, profesionální odůvodnění vhodné ke sdílení s právníkem protistrany.
4. **Poskytněte ústupové pozice**: U ŽLUTÝCH položek uveďte ústupovou pozici pro případ zamítnutí hlavního požadavku.
5. **Prioritizujte**: Ne všechny redlines mají stejnou váhu. Uveďte, které jsou nezbytné a které pouze vítané.
6. **Zohledněte vztah**: Přizpůsobte tón a přístup podle toho, zda jde o nového dodavatele, strategického partnera nebo komoditního dodavatele.

#### Formát redline

Pro každý redline:
```
**Ustanovení**: [odkaz na článek a název ustanovení]
**Současné znění**: "[přesná citace ze smlouvy]"
**Navrhovaná úprava**: "[konkrétní alternativní znění; doplněné pasáže označ tučně, vymazávané přeškrtni]"
**Odůvodnění**: [1–2 věty s vysvětlením důvodu, vhodné pro externí sdílení]
**Priorita**: [Must-have (nezbytné) / Should-have (žádoucí) / Nice-to-have (vítané)]
**Ústupová pozice**: [Alternativní pozice, pokud bude primární návrh odmítnut]
```

### Krok 7: Shrnutí obchodních dopadů

Poskytněte souhrnnou sekci pokrývající:
- **Celkové posouzení rizika**: Přehled rizikového profilu smlouvy
- **3 hlavní problémy**: Nejdůležitější položky k řešení
- **Vyjednávací strategie**: Doporučený přístup (s čím začít, co ustoupit)
- **Časové aspekty**: Faktory naléhavosti ovlivňující přístup k jednání

#### Rámec priorit pro vyjednávání

Při prezentaci úprav organizujte podle vyjednávací priority:

**Tier 1 — Nezbytné (must-have, deal-breakery)**
Body, bez jejichž vyřešení organizace nemůže pokračovat:
- Neomezené nebo podstatně nedostatečné ochrany odpovědnosti
- Chybějící požadavky na ochranu osobních údajů u regulovaných dat
- Ustanovení o IP, která by mohla ohrozit klíčová aktiva
- Podmínky v rozporu s regulatorními povinnostmi

**Tier 2 — Žádoucí (should-have, silné preference)**
Body, které významně ovlivňují riziko, ale ponechávají prostor k jednání:
- Úpravy limitu odpovědnosti v rámci rozsahu
- Rozsah a vzájemnost odškodnění
- Flexibilita ukončení
- Práva auditu a kontroly compliance

**Tier 3 — Vítané (nice-to-have, kandidáti na ústupky)**
Body, které pozici vylepšují, ale lze je strategicky ustoupit:
- Preferované rozhodné právo (je-li alternativa přijatelná)
- Preference výpovědních lhůt
- Drobná vylepšení definic
- Požadavky na osvědčení o pojištění

**Vyjednávací strategie**: Začněte Tier 1. Za ústupky v Tier 3 si zajistěte úspěchy v Tier 2. V Tier 1 nikdy neustupujte bez eskalace.

### Krok 8: Směrování v CLM (pokud je připojeno)

Pokud je přes MCP připojen systém pro správu životního cyklu smluv (CLM):
- Doporučte vhodné schvalovací workflow podle typu smlouvy a úrovně rizika
- Navrhněte správnou cestu směrování (např. standardní schválení, vedoucí právník, externí advokát)
- Upozorněte na potřebné souhlasy podle hodnoty smlouvy nebo rizikových příznaků

Pokud CLM není připojeno, tento krok přeskočte.

## Formát výstupu

Výstup se řídí volbou uživatele z Kroku 2 (otázka č. 5). **Default je obojí: shrnutí v chatu + Word dokument s komentáři.**

### Default — obojí

#### A) Shrnutí v chatu

Stručná verze pro rychlé čtení v konverzaci:

```
## Shrnutí revize smlouvy

**Dokument**: [název/identifikátor smlouvy]
**Strany**: [jména stran a role]
**Vaše strana**: [dodavatel/zákazník atd.]
**Protistrana (KYC)**: [stav z Kroku 2.5 — identifikace OK / signatář OK / insolvence NE]
**Termín**: [je-li uveden]
**Základ revize**: [Playbook / Obecné standardy]

## Klíčová zjištění

[3–5 hlavních problémů s označením závažnosti — kritické / k revizi]

## Top doporučení k vyjednávání

[Tier 1 must-have, krátce]

## Další kroky

[Konkrétní akce k provedení; odkaz na Word s komentáři]
```

Ve shrnutí v chatu **necituj celé redlines** — ty patří do Word dokumentu. V chatu uveď jen identifikaci problému, závažnost a směr řešení.

#### B) Word dokument s komentáři

Vygeneruj **kopii originální smlouvy ve formátu .docx** s vloženými **komentáři Wordu** (review comments) na příslušných místech smlouvy. Pokud je vstup PDF, **převeď ho lokálně** (např. přes `pdftotext`, `pypdf`, `pdfplumber` nebo skill `pdf`, nikoli přes DirectCase — `convert_file_to_markdown` funguje jen pro dokumenty na důvěryhodných právních doménách, ne pro libovolný PDF vstup uživatele) a vytvoř Word verzi (zaznamenej do shrnutí, že bylo nutné zrekonstruovat strukturu textu).

**Pravidla pro komentáře:**

- Každý komentář **začíná kategorií** uvedenou na prvním řádku tučně a barevně podle závažnosti nálezu:
  - **„Kritické"** — tučně **červeně**; odpovídá ČERVENÉ klasifikaci z Kroku 5 (eskalace, must-have, deal-breaker, právní riziko neplatnosti, regulatorní porušení).
  - **„K revizi"** — tučně **žlutě / jantarově** (tmavší odstín, aby byl čitelný na bílém pozadí); odpovídá ŽLUTÉ klasifikaci z Kroku 5 (vyjednatelné odchylky, should-have, méně závažné, vylepšení).
  - ZELENÁ ustanovení (přijatelné) komentářem **neoznačuj**, aby Word zůstal čitelný.
- Tělo komentáře (text za pomlčkou) je v normální černé barvě.
- Po kategorii následuje krátké odůvodnění a navrhované znění.

> ⚙ **Pro AI agenta — RGB hodnoty:** Kritické = `C00000` (Word „Red"); K revizi = `BF8F00` (Word „Dark Yellow"). Čistá žlutá `FFFF00` je na bílém nečitelná, nepoužívej ji.

**Doporučená struktura jednoho komentáře:**

```
**Kritické** — [krátký popis problému, max. 1 věta]

Problémové znění (citace ze smlouvy): „…"
Navrhovaná úprava: „…"
Důvod: [1–2 věty, vhodné pro externí sdílení s protistranou]
Priorita: Must-have / Should-have / Nice-to-have
Ústupová pozice: [pokud relevantní]
[Volitelně, je-li z DirectCase] Judikatura: NS sp. zn. … — [stručný princip]
```

Komentář umísti k přesnému místu ve smlouvě, kterého se týká (článek + odstavec).

**Pojmenování souboru:** `Revize_[název_protistrany]_[YYYY-MM-DD].docx` (např. `Revize_Determinant_2026-05-08.docx`).

V závěru shrnutí v chatu předej uživateli computer:// odkaz na vygenerovaný soubor.

##### Postup tvorby Word dokumentu s komentáři

> ⚙ **Pro AI agenta — uživatel může tuto sekci přeskočit.**
> Tato podkapitola popisuje technický postup pro vytvoření .docx souboru s komentáři. Uživatele zajímá jen výstup popsaný výše (Word soubor s barevnými komentáři Kritické / K revizi). Pokud něco v generovaném souboru nesedí, podívej se na tabulku „Časté chyby a fix" na konci.

Pracuj se skillem `docx` (`anthropic-skills:docx`), který poskytuje nástroje pro úpravu .docx souborů. Tvůj cíl: vytvořit kopii originální smlouvy s vloženými komentáři Wordu pro každý nález.

**Co je potřeba na výstupu:**

1. Soubor pojmenovaný `Revize_[protistrana]_[YYYY-MM-DD].docx` v pracovní složce uživatele (ne jen v dočasné výstupní složce).
2. Identický text smlouvy jako v originálu (komentáře jen přidávají poznámky, neměníš obsah).
3. Pro každý nález jeden Word komentář s tučnou kategorií **Kritické** nebo **K revizi** na začátku, následovaný odůvodněním a navrhovaným zněním.
4. Komentáře musí být v dokumentu skutečně **viditelné po otevření v Wordu** (nestačí, že validace projde).

**Pracovní postup:**

Pracuj iterativně, ne najednou. Postupuj takto:

1. **Zkopíruj originál do outputs** pod cílovým názvem souboru.
2. **Rozbal docx** přes nástroj `unpack.py` ze skillu `docx` — získáš adresář `revize_unpacked/` s XML soubory smlouvy.
3. **Naplň všechny čtyři XML soubory komentářů najednou** (ne po jednom, jinak se Word komentáře nezobrazí):
   - `word/comments.xml` — vlastní text komentářů
   - `word/commentsExtended.xml` — metadata
   - `word/commentsIds.xml` — trvalé ID
   - `word/people.xml` — autor (Claude)
4. **Doplň povinné relationships** (`word/_rels/document.xml.rels`) a Content Types (`[Content_Types].xml`) pro tyto čtyři soubory. Bez nich Word komentáře nezobrazí, i když pack.py projde.
5. **Vlož značky komentářů do `document.xml`** — pro každý komentář dvojici `<w:commentRangeStart>` / `<w:commentRangeEnd>` + `<w:commentReference>`. Značky musí být **přímými potomky `<w:p>`** (ne uvnitř `<w:r>`) a musí být **za `<w:pPr>`**, pokud existuje (jinak schema validace selže).
6. **Zabal zpět** přes `pack.py` ze skillu `docx` s parametrem `--original` na původní soubor.
7. **Ověř, že komentáře jsou skutečně v dokumentu** (viz „Ověření" níže).
8. **Zkopíruj finální soubor do pracovní složky uživatele** (aby ho uživatel viděl přes odkaz `computer://`). Dočasná výstupní složka (outputs) je pro uživatele neviditelná.

**Tip pro vyhledávání textu pro značky komentářů**

Text smlouvy je v docx často rozsekaný do více `<w:r>` runů (kvůli formátování). Pro umístění komentáře k danému článku/odstavci hledej v `document.xml` **krátký unikátní řetězec** uvnitř jednoho `<w:t>` elementu — typicky 5–15 znaků (např. „0,10 %", „60 pracovních dnů", „smluvní pokutu ve výši"). Pozor na čísla s mezerami — „4 000 000 Kč" v XML může být `4&#xA0;000&#xA0;000` a běžné hledání selže.

**Formátování komentáře (vizuální vzor):**

Začátek komentáře je barevně tučně podle závažnosti:
- **„Kritické — "** tučně červeně
- **„K revizi — "** tučně žlutě / jantarově

Následuje text odůvodnění v normální černé barvě. Tělo komentáře obsahuje:

- krátký popis problému (max. 1 věta po kategorii),
- problémové znění citované ze smlouvy,
- navrhovanou úpravu,
- důvod (1–2 věty, vhodné pro externí sdílení s protistranou),
- prioritu (Must-have / Should-have / Nice-to-have),
- volitelně judikaturu z DirectCase (sp. zn. + krátký princip).

> ⚙ **Pro AI agenta:** První řádek komentáře tvoří dva textové runy — první s `<w:b/>` a `<w:color w:val="C00000"/>` (Kritické) nebo `<w:color w:val="BF8F00"/>` (K revizi), druhý s `<w:color w:val="000000"/>` pro tělo.

##### Ověření výstupu (povinné!)

Po vygenerování souboru **vždy** ověř, že komentáře skutečně jsou v dokumentu — ne jen v komentářovém XML. Otevři výsledný .docx jako zip a v `word/document.xml` spočítej značky `commentRangeStart`, `commentRangeEnd` a `commentReference`. Všechny tři počty musí být **stejné** a rovny počtu komentářů.

Pokud jsou všechny tři nuly, pack.py značky během validace „neviditelně" odstranil — typicky proto, že chyběly rels nebo Content Types entries pro commentsExtended / commentsIds / people. Vrať se ke kroku 4 (rels a Content Types) a opakuj.

##### Časté chyby a fix

| Symptom | Příčina | Řešení |
|---|---|---|
| Word neukáže žádné komentáře, validace přitom prošla | Chybí relationships nebo Content Types pro commentsExtended / Ids / people | Doplň všechny tři páry rels + Override entries |
| `Element '{...}pPr': This element is not expected` při validaci | Značka komentáře vložena před `<w:pPr>` | Vlož ZA `</w:pPr>`, ne před něj |
| Vyhledávání textu pro značku selže přes 0 nálezů | Hledaný řetězec je rozdělen do více `<w:r>` runů | Zkrať na 5–15 znaků uvnitř jednoho `<w:t>` |
| `commentRangeStart` v dokumentu má počet 0 i po úspěšném packu | Pack.py přepsal soubor při validaci | Doplň rels + Content Types a zopakuj insert + pack |
| Uživatel nevidí soubor po dokončení | Soubor zůstal jen v dočasné výstupní složce (outputs) | Zkopíruj do pracovní složky uživatele |

### Pouze shrnutí v chatu

Pokud si uživatel zvolil tuto variantu, vynech generování Word dokumentu a místo top doporučení vlož kompletní analýzu doložek po doložce ve formátu:

```
### [Kategorie ustanovení] — [Kritické / K revizi / OK]
**Ve smlouvě stojí**: [shrnutí ustanovení nebo přesná citace]
**Pozice playbooku / standard**: [váš standard]
**Odchylka**: [popis rozdílu]
**Obchodní dopad**: [co to prakticky znamená]
**Návrh úpravy**: [konkrétní znění, u K revizi i Kritické]
**Priorita**: Must-have / Should-have / Nice-to-have
[Volitelně z DirectCase] **Judikatura**: NS sp. zn. … — [stručný princip]

[Opakuj pro každé významné ustanovení]
```

### Pouze Word dokument s komentáři

Vygeneruj jen Word soubor (postup viz část B výše) a v chatu pošli krátkou zprávu obsahující:

- Počet kritických nálezů: X
- Počet nálezů k revizi: Y
- KYC protistrany: [krátký výsledek z Kroku 2.5]
- Odkaz na soubor: computer://...

### Jiné (vlastní formát)

Pokud si uživatel zvolil vlastní formát (např. PDF, prezentace, e-mail), zeptej se přes `AskUserQuestion` na bližší specifikaci a vygeneruj výstup v požadované formě. Kategorizace „Kritické" / „K revizi" zůstává konzistentní napříč všemi formáty.

## Poznámky

- Pokud je smlouva v jazyce jiném než v češtině, uveďte to a zeptejte se uživatele, zda chce překlad nebo revizi v původním jazyce
- U velmi dlouhých smluv (50+ stran) nabídněte, že se nejdříve zaměříte na nejvýznamnější části a teprve poté provedete kompletní revizi
- Vždy uživateli připomeňte, že tato analýza má být před využitím pro právní rozhodnutí ověřena kvalifikovaným advokátem

<!-- Origin: DirectCase pravo-skills v1.1.0 (MIT, LICENSE-directcase-pravo-skills) | Import: 2026-07-14 do ak-sladek pluginu, review bez adaptaci (Cowork-native reference OK) | Inspiration: https://www.directcase.ai/cz/cs/news/claude-legal-plugin-cs -->
