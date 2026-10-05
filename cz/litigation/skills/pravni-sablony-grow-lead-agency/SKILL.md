---
name: pravni-sablony-grow-lead-agency
title: /pravni-sablony — Knihovna právních úloh
description: Knihovna právních úloh — žaloba, vyjádření k žalobě, odvolání, dovolání, právní stanovisko, memorandum, upomínka, dodatek ke smlouvě, uznání dluhu, porovnání verzí dokumentu, shrnutí pro klienta, anonymizace, překlad, posudek, FAQ, checklist procesu a další. Upgrade šablon ze semináře AI pro právníky (11/2025) — stejná struktura, ale s ochranou proti halucinaci citací a formátem kanceláře. Použij když advokát potřebuje sepsat či zpracovat právní dokument, který nemá vlastní specializovaný skill.
author: grow-lead-agency
author_url: https://github.com/grow-lead-agency/ak-sladek/tree/master/skills/pravni-sablony
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cz
practice: litigation
language: cs
---

# /pravni-sablony — Knihovna právních úloh

**Důležité**: Výstupy jsou návrhy ke kontrole advokátem (zák. č. 85/1996 Sb.). Nikdy je nepředávej klientovi bez advokátní kontroly.

## Nejdřív routing — má úloha specializovaný skill?

| Úloha | → Použij místo šablony |
|---|---|
| Kupní smlouva + úschova (nemovitost) | `/generuj-smlouvu` (vzory kanceláře) |
| Přeformátovat dokument do stylu kanceláře | `/formatuj-smlouvu` |
| Revize/analýza smlouvy na rizika | `/revize-smlouvy` |
| NDA posouzení | `/triage-nda` |
| Kontrola podpisových práv, KYC | `/kontrola-podpis`, `/kontrola-dodavatele` |
| GDPR/compliance check | `/kontrola-souladu` |
| Judikatura, rešerše, prověrka čehokoli | `/hloubkovy-research` |
| Riziko, jednání, šablonové odpovědi, přehled | `/posouzeni-rizika`, `/priprava-jednani`, `/pravni-odpoved`, `/prehled-pravni` |

Nic z toho? → pokračuj šablonou níže.

## Upgrade vrstva (platí pro VŠECHNY šablony — neobcházet)

1. **Doptej se před psaním** — každá šablona končí „zeptej se mě na vše, co potřebuješ" — MYSLÍ SE TO VÁŽNĚ. Chybí-li fakta, ptej se, nevymýšlej.
2. **Citace jen ověřené** — §, judikatura, sp. zn. VÝHRADNĚ přes DirectCase (`get_law_detail`, `search_caselaw_parallel`) nebo primární zdroj. Bez ověření → `[neověřeno]`. Nikdy nevydávej neověřenou citaci za fakt. Parallel search nástroje lze zavolat jen 1× za konverzaci (víc dotazů → pole `queries[]`); Basic (free) = 20 volání/nástroj celkem, Pro = 25/den — pro follow-upy preferuj `search_keyword` / `get_law_detail`.
3. **Formát kanceláře** — finální dokument protáhni `/formatuj-smlouvu` house rules (Tahoma 10,5, bez mezer, částky s haléři, podpisy ve sloupcích).
4. **Playbook kanceláře** — existuje-li `legal.local.md`, respektuj jeho pozice a eskalační pravidla.
5. **Eskalace** — před draftem zkontroluj `references/eskalace.md`; červený trigger = STOP a shrnutí advokátovi.
6. **Osobní údaje** — do dokumentů jen údaje dodané advokátem; při anonymizaci konzistentní náhrady (Osoba 1, Společnost A).

## Šablony (struktura: Role · Rozsah · Formát · Účel)

Každou spouštěj vzorem: *„[Role]. [Rozsah]. Formát: [formát]. Účel: [účel]. Zeptej se mě na všechno, co potřebuješ vědět."*

### Podání a spory
- **Žaloba** — procesní právník; kompletní žaloba: účastníci, rozhodující skutečnosti, důkazy, právní posouzení, petit; náležitosti dle o.s.ř., číslované odstavce. Před psaním ověř přes DirectCase aktuální judikaturu k nároku.
- **Vyjádření k žalobě** — obhajoba: procesní námitky, věcná obrana, důkazní návrhy, návrh na zamítnutí; strukturováno podle bodů žaloby.
- **Odvolání** — vady prvostupňového rozhodnutí (hmotné i procesní), rozsah napadení, odvolací důvody, petit; citace z napadeného rozhodnutí.
- **Dovolání** — přípustnost, právní otázka zásadního významu, judikatura NS (POUZE ověřená přes DirectCase!).
- **Upomínka / předžalobní výzva** — specifikace dluhu, výzva s lhůtou, důsledky. ⚠️ HARD GATE: nárok na náhradu nákladů řízení vyžaduje výzvu **min. 7 dnů před podáním žaloby** na doručovací adresu (§ 142a o.s.ř.) — vždy zkontroluj a upozorni. Pro výpočet lhůty ověř aktuální datum přes DirectCase `get_current_time`, nespoléhej na paměť modelu.
- **Uznání dluhu** — identifikace stran, specifikace dluhu (důvod + výše), splátkový kalendář; náležitosti pro přerušení promlčení.

### Smlouvy a korporátní (mimo vzory kanceláře)
- **Nájemní smlouva** — prostory, nájemné, služby, údržba, ukončení; dle NOZ.
- **Darovací smlouva** — specifikace daru, prohlášení dárce, podmínky, odvolání daru; u nemovitostí vkladové řízení (KEP + časové razítko — viz katastr gate).
- **Pracovní smlouva** — povinné náležitosti (druh, místo, nástup), mzda, konkurenční doložka; kogentní ustanovení ZP.
- **Smlouva o dílo / společenská smlouva / konkurenční doložka / dohoda o narovnání** — dle seminárních šablon; u narovnání: sporné vztahy → ústupky → nové uspořádání → konečnost vypořádání.
- **Dodatek ke smlouvě** — přesná identifikace původní smlouvy, číslování, co se ruší a čím nahrazuje, účinnost.

### Analytické a klientské výstupy
- **Právní stanovisko / posudek** — definice problému → analýza legislativy a judikatury (DirectCase!) → interpretační varianty → rizika → doporučení; executive summary na začátek.
- **Klientské memorandum** — 1 strana shrnutí + možnosti s výhodami/nevýhodami + doporučený postup s harmonogramem a náklady; srozumitelný jazyk.
- **Shrnutí složitého dokumentu** — klíčové body, práva/povinnosti, lhůty, rizika; laickým jazykem, tabulka + časová osa.
- **Porovnání verzí dokumentu** — tabulka změn (přidáno/odebráno/upraveno), právní dopad každé změny, doporučení akceptovat/odmítnout.
- **Překlad právního dokumentu** — zachovat právní význam a strukturu; termíny bez ekvivalentu označit s vysvětlením.
- **Anonymizace** — odstranit osobní/identifikační/důvěrné údaje, konzistentní náhrady, zachovat právní podstatu.
- **Due diligence report / kontrola úplnosti dokumentace** — struktura dle právních oblastí, risk matrix, red flags, chybějící dokumenty.
- **Interní směrnice / FAQ / prezentace / checklist procesu** — dle seminárních šablon; checklist vždy s lhůtami a odpovědnostmi.

## Poznámka k původu
Šablony vychází ze semináře „AI pro právníky" (4.11.2025), který JUDr. Sládek absolvoval — stejná logika Role/Rozsah/Formát/Účel, kterou zná, ale upgradovaná: trvalé skilly místo copy-paste promptů, ověřené citace místo halucinací, formát kanceláře místo generického výstupu.

<!-- Origin: upgrade seminárních šablon (AI seminář pro právníky 4.11.2025, PDF od JUDr. Sládka) | Vytvořeno: 2026-07-14 | Inspiration: interní PDF "ŠABLONY PROMPTŮ PRO PRÁVNÍ DOKUMENTY" -->
