---
name: generuj-smlouvu-grow-lead-agency
title: /generuj-smlouvu — Generování smluv ze vzorů kanceláře
description: Vygeneruje smlouvy z vlastních vzorů kanceláře — kupní smlouva na nemovitost + smlouva o advokátní úschově jako propojený pár z jednoho zadání. Uživatel nadiktuje fakta případu (strany, nemovitost dle LV, cena, platby), AI je namapuje na strukturovaná data, deterministický šablonovací engine vyplní schválený vzor kanceláře. Použij při přípravě dokumentů k převodu nemovitosti, prodeji bytu/pozemku s úschovou kupní ceny, nebo když uživatel řekne „připrav kupní smlouvu a úschovu".
author: grow-lead-agency
author_url: https://github.com/grow-lead-agency/ak-sladek/tree/master/skills/generuj-smlouvu
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: cz
practice: real-estate
language: cs
sources:
- title: Sources
  path: references/sources.md
---

# /generuj-smlouvu — Generování smluv ze vzorů kanceláře

**Důležité**: Tento skill pomáhá s právními workflow, ale neposkytuje právní poradenství ve smyslu zákona č. 85/1996 Sb., o advokacii. Výstup je NÁVRH ke kontrole advokátem — nikdy ho nepředávej klientovi bez advokátní kontroly.

## Jak to funguje (princip)

**AI text smlouvy NEPÍŠE.** Text pochází ze schválených vzorů kanceláře (docxtpl šablony). AI pouze:
1. vytěží fakta případu ze zadání uživatele (přirozený jazyk, LV, rezervační smlouva…),
2. namapuje je na JSON dle `vzory/prevod-nemovitosti/schema.json`,
3. zvaliduje (chybějící pole = STOP a doptat se, ne hádat),
4. spustí deterministický render (`scripts/render.py`) → hotové .docx v jednotném formátu kanceláře.

Tím je vyloučena halucinace klauzulí — každá věta v dokumentu je z odsouhlaseného vzoru.

## Pracovní postup

### Krok 1 — Převzetí faktů
Uživatel dodá fakta případu volným textem, nebo přiloží podklady (výpis LV, rezervační smlouvu, e-mail s dohodou). Vytěž:
- **Strany**: jméno/název, r.č. nebo IČ, adresa; u PO rejstříkový zápis + zástupce; u manželů oba (SJM)
- **Nemovitost**: přesný popis dle LV (jednotka/pozemky/stavba, podíly, k.ú., katastrální pracoviště)
- **Cena a platby**: celková cena, záloha (hotovost/už uhrazená), doplatek do úschovy
- **Kontakty**: e-maily obou stran (notifikace o pohybech na účtu úschovy)
- **Výplatní účet prodávajícího** (č.ú.) — POVINNÝ, bez něj úschovu nelze sestavit

### Krok 2 — KYC ověření (s DirectCase konektorem)
Pokud je připojen DirectCase MCP, ověř strany v obchodním rejstříku (`search_company` / `search_identifier`):
existence, sídlo, statutární orgán, **způsob jednání** (samostatně × společně!), insolvence.
Nesoulad → upozorni PŘED generováním. Bez konektoru výslovně uveď, že údaje nebyly nezávisle ověřeny.

### Krok 3 — Mapování na schéma
Sestav JSON dle `vzory/prevod-nemovitosti/schema.json`. Řádky stran (`radek1`–`radek5`) skládej dle vzorů v schema description. Částky formátuj `3.500.000,00`, lhůty `deseti (10)`.
- prodávající v úschově = **Strana příjemce** (musí mít č.ú.)
- kupující v úschově = **Strana uschovatele**
- `cena.doplatek` MUSÍ = `uschova.castka`

### Krok 4 — Kontrola s uživatelem
Před generováním ukaž **přehlednou rekapitulaci** (strany, nemovitost, částky, účty, lhůty) a nech ji potvrdit. Netriviální odchylky od standardu (jiná banka úschovy, nestandardní lhůty) výslovně zvýrazni.

### Krok 5 — Render
```
python skills/generuj-smlouvu/scripts/render.py \
  skills/generuj-smlouvu/vzory/prevod-nemovitosti  data-pripadu.json  vystup/
```
Vyžaduje `pip install docxtpl`. Validace ve skriptu při chybě generování ZASTAVÍ (exit 1) — chybu vyřeš doptáním, nikdy ji neobcházej vymyšlenou hodnotou.

### Krok 6 — Předání
Vrať uživateli oba dokumenty + shrnutí: co bylo vygenerováno, jaké hodnoty byly použity z defaultů kanceláře (účet úschovy, lhůty, stejnopisy), co zbývá doplnit ručně (datum a místo podpisu). Připomeň kontrolu advokátem.

## Další vzory (render_doc.py — jednotlivé dokumenty s gates)

| Vzor | Render | Kódový gate |
|---|---|---|
| `vzory/plna-moc` | `scripts/render_doc.py vzory/plna-moc data.json out/` | katastr → vynucen úředně ověřený podpis |
| `vzory/predzalobni-vyzva` | `scripts/render_doc.py vzory/predzalobni-vyzva data.json out/` | **§142a: lhůta < 7 dnů = STOP**; povinná doručovací adresa; připomenutí odeslat ≥7 dnů před žalobou |

Texty těchto vzorů jsou návrh GrowLead v house stylu — JUDr. Sládek je při prvním použití zreviduje a případné úpravy se zapíší do šablony (pak jsou to jeho vzory).

## Eskalace (Escalation-Router)

PŘED draftováním zkontroluj [`references/eskalace.md`](../../references/eskalace.md) (root pluginu): sporná vlastnická struktura (poznámka spornosti, exekuce na LV), nestandardní úschova, cizinecký prvek, insolvence protistrany, „dva jednatelé společně" → **STOP, nedraftuj, shrň advokátovi**. Nejistota = eskalace, ne odhad.

## Hard gates (neobcházet)

- **Advokátní úschova**: zákaz hotovostních vkladů/výběrů z účtu úschovy; jeden účet = jedna úschova; úschova se hlásí do Elektronické knihy úschov ČAK (před přijetím, po přijetí, po vyplacení). Připomeň uživateli EKÚ hlášení.
- **Katastr**: k elektronickému vkladu je nutná vkladová listina s úředně ověřenými podpisy; prosté skeny katastr zamítá.
- Chybí-li povinný údaj → **zeptej se, nikdy nedopĺňuj odhadem** (jde o právní dokument).
- Judikaturu/§ cituj jen s ověřeným identifikátorem z DirectCase; bez konektoru citace označ jako neověřené.
- **Datum-disciplína**: u znění zákonů přes DirectCase používej `date` parametr (temporal validity) a do výstupu uveď, ke kterému dni znění platí — legislativa úschov/advokacie se v 2026 měnila. Pro výpočet lhůt (§142a předžalobní výzva, lhůty úschovy) ověř aktuální datum přes DirectCase `get_current_time`, nespoléhej na paměť modelu.

## Konfigurace kanceláře

`config/kancelar.json` v rootu pluginu — konstanty advokáta (jméno, ČAK, sídlo), účet úschovy, výchozí lhůty, počty stejnopisů. Data případu je mohou přepsat (`uschova.ucet`, `lhuty.*`).

## Omezení verze 0.1 (řekni uživateli, když narazí)

- Pokrytá struktura obchodu: záloha uhrazená v hotovosti před podpisem + doplatek do advokátní úschovy. Varianty (hypoteční financování, provize zprostředkovatele z první části, bez zálohy) zatím nejsou — vyžadují úpravu šablony, ne improvizaci v datech.
- Prodávající = 1 osoba (FO/PO). Manželé (SJM) a více spoluvlastníků zatím jen na straně kupující omezeně — ověř výstup.
- Podpisový blok se zástupcem podporuje jen kupující stranu (PO prodávající = zkontroluj podpisy ručně).

<!-- Origin: GrowLead ak-sladek plugin (interní vzory kanceláře JUDr. Sládka) | Vytvořeno: 2026-07-14 | Inspiration: interní docxtpl vzory kanceláře (kupní smlouva, smlouva o úschově, plná moc, předžalobní výzva) -->
