---
name: fetching-isap-sejm
title: fetching-isap-sejm
description: Use when retrieving Polish legislation text from the official portal isap.sejm.gov.pl (Internetowy System Aktów Prawnych) — fetching specific historical redactions by date, verifying current validity of a norm, tracking amendments, working with consolidated texts (tekst jednolity), or constructing URLs for Polish codes and acts
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/skills/pl/law-pl-fetching-isap-sejm
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: general
language: pl
---

# fetching-isap-sejm

ISAP — Internetowy System Aktów Prawnych Sejmu RP. Wraz z dziennikustaw.gov.pl stanowi jedyne autorytatywne źródło tekstów polskich aktów prawnych. Prawidłowy URL pozwala uzyskać brzmienie obowiązujące lub na konkretną datę historyczną.

## Pierwotne źródła

| Źródło | URL | Kiedy używać |
|---|---|---|
| ISAP — wyszukiwarka aktów | https://isap.sejm.gov.pl/ | Brzmienia obecne i historyczne, karta dokumentu |
| Dziennik Ustaw (e-Dziennik) | https://dziennikustaw.gov.pl/ | Oficjalna publikacja nowych aktów (PDF urzędowy) |
| Monitor Polski | https://monitorpolski.gov.pl/ | Akty wewnętrzne, obwieszczenia, uchwały Sejmu / Senatu |
| EUR-Lex (polska wersja) | https://eur-lex.europa.eu/homepage.html?locale=pl | Akty UE (rozporządzenia, dyrektywy) — pierwszeństwo nad prawem krajowym |

## Wzorce URL ISAP

| Cel | URL |
|---|---|
| Karta dokumentu | `https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id={ID}` |
| Tekst aktu w pliku PDF | `https://isap.sejm.gov.pl/isap.nsf/download.xsp/{ID}/T/T{nr_pliku}.pdf` |
| Tekst jednolity | dostępny przez kartę aktu — link „Tekst ujednolicony" |
| Wyszukiwarka | `https://isap.sejm.gov.pl/isap.nsf/byyear.xsp` (po roku publikacji) |

gdzie `{ID}` ma format `WDU{rok}{nr_dz_u}{poz}` (np. `WDU19640160093` — Dz.U. 1964 nr 16 poz. 93 = pierwotny KC).

**Uwaga**: na karcie aktu — kluczowe pola: „Status aktu prawnego", „Data ogłoszenia", „Data wejścia w życie", „Akty zmieniające", „Tekst ujednolicony", „Akty wykonawcze". **Zawsze sprawdzać** datę ostatniego tekstu jednolitego oraz daty kolejnych nowelizacji po jego opublikowaniu.

## Kluczowe akty — dane do wyszukiwania

| Akt | Pierwotne Dz.U. | Aktualny tekst jednolity (sprawdzać!) |
|---|---|---|
| Konstytucja RP | Dz.U. 1997 nr 78 poz. 483 | — |
| Kodeks cywilny | Dz.U. 1964 nr 16 poz. 93 | Dz.U. 2024 ... (sprawdzać aktualny) |
| Kodeks postępowania cywilnego | Dz.U. 1964 nr 43 poz. 296 | Dz.U. 2024 ... |
| Kodeks rodzinny i opiekuńczy | Dz.U. 1964 nr 9 poz. 59 | — |
| Kodeks karny | Dz.U. 1997 nr 88 poz. 553 | Dz.U. 2024 ... |
| Kodeks postępowania karnego | Dz.U. 1997 nr 89 poz. 555 | Dz.U. 2024 ... |
| Kodeks pracy | Dz.U. 1974 nr 24 poz. 141 | Dz.U. 2023 ... |
| Kodeks postępowania administracyjnego | Dz.U. 1960 nr 30 poz. 168 | Dz.U. 2024 ... |
| Prawo o postępowaniu przed sądami administracyjnymi | Dz.U. 2002 nr 153 poz. 1270 | — |
| Kodeks spółek handlowych | Dz.U. 2000 nr 94 poz. 1037 | Dz.U. 2024 ... |
| Ordynacja podatkowa | Dz.U. 1997 nr 137 poz. 926 | Dz.U. 2023 ... |
| Prawo o adwokaturze | Dz.U. 1982 nr 16 poz. 124 | Dz.U. 2022 ... |
| Ustawa o radcach prawnych | Dz.U. 1982 nr 19 poz. 145 | Dz.U. 2022 ... |
| Ustawa o dostępie do informacji publicznej | Dz.U. 2001 nr 112 poz. 1198 | Dz.U. 2022 poz. 902 |
| Ustawa o kosztach sądowych w sprawach cywilnych | Dz.U. 2005 nr 167 poz. 1398 | Dz.U. 2024 ... |
| Ustawa o komornikach sądowych | Dz.U. 2018 poz. 771 | — |
| Ustawa o kosztach komorniczych | Dz.U. 2018 poz. 770 | — |
| Ustawa o ochronie danych osobowych | Dz.U. 2018 poz. 1000 | Dz.U. 2019 poz. 1781 |
| RODO (rozp. UE 2016/679) | Dz.Urz. UE L 119 z 04.05.2016 | EUR-Lex |

## Workflow

1. **Identyfikacja aktu** — przez wyszukiwanie na ISAP po słowach kluczowych z nazwy. Wyniki posortowane wg daty publikacji.
2. **Karta dokumentu** — sprawdzić: status („obowiązujący" / „uchylony" / „akt indywidualny"), datę ostatniego tekstu jednolitego, listę aktów zmieniających po tekście jednolitym.
3. **Tekst aktualny** — kliknąć link „Tekst ujednolicony" lub „Tekst aktu" — pobierze PDF z aktualnym brzmieniem na datę ostatniego tekstu jednolitego. Po tym terminie — sprawdzić listę nowelizacji.
4. **Tekst historyczny na konkretną datę** — w karcie dokumentu sekcja „Tekst aktu w wersji historycznej" lub można zrekonstruować przez listę aktów zmieniających (każda zmiana ma swoją kartę z datą wejścia w życie).
5. **Cytowanie** — artykuł + akt + Dz.U. (wskazanie publikatora) + brzmienie obowiązujące od daty + URL do ISAP.

## Cytowanie publikatora

**Format pełny** (przy pierwszym przywołaniu):
```
ustawa z dnia 23 kwietnia 1964 r. — Kodeks cywilny
(Dz.U. 1964 nr 16 poz. 93 z późn. zm., t.j. Dz.U. 2024 poz. ___)
```

**Format skrócony** (przy kolejnych):
```
KC
```

**Przy cytowaniu konkretnego artykułu**:
```
art. 117 § 1 Kodeksu cywilnego (KC)
```

## Najczęstsze błędy

- **Cytowanie bez wskazania brzmienia.** Przy nowelizacjach — istotne, czy norma była identycznie brzmiąca w przeszłości. Bez daty brzmienia cytat jest niepewny.
- **Mylenie tekstu jednolitego z tekstem pierwotnym.** Tekst jednolity to konsolidacja na konkretną datę; po nim mogły być kolejne zmiany.
- **Stare numeracje artykułów.** Reformy KPC (np. 2019, 2023) zmieniły numerację niektórych przepisów — np. dawny art. 207 KPC o odpowiedzi na pozew został uchylony, regulacja przeniesiona / przekształcona.
- **Komercyjne agregatory jako primary source.** Lex (Wolters Kluwer), Legalis (C.H. Beck), LexLege, Lexlege.pl — można używać do nawigacji, ale **autorytatywne źródło to ISAP / Dziennik Ustaw**.
- **Pomijanie aktów wykonawczych.** Wiele norm ramowych jest doprecyzowanych w rozporządzeniach Ministrów — sprawdzać sekcję „Akty wykonawcze" w karcie ustawy.
- **Brak weryfikacji w EUR-Lex.** W obszarach harmonizowanych (np. RODO, prawo konsumenckie, VAT, prawo pracy) — sprawdzać akty UE (rozporządzenia stosowane bezpośrednio; dyrektywy implementowane).
- **Wsteczne stosowanie nowelizacji.** Norma działa „od" konkretnej daty; do stosunków powstałych wcześniej — często stosuje się brzmienie z daty czynności (lex retro non agit; szczegóły w przepisach przejściowych konkretnej nowelizacji).
