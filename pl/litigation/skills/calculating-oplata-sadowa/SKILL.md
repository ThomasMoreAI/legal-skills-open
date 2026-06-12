---
name: calculating-oplata-sadowa
title: calculating-oplata-sadowa
description: Use when calculating Polish court fees (opłata sądowa) for civil lawsuits, appeals, or procedural filings under ustawa o kosztach sądowych w sprawach cywilnych (UKSC), checking whether opłata stosunkowa, stała, or podstawowa applies, applying statutory exemptions, or drafting motions for exemption / installment of fees
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/skills/pl/law-pl-calculating-oplata-sadowa
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: litigation
language: pl
---

# calculating-oplata-sadowa

Opłaty sądowe w sprawach cywilnych regulowane są **ustawą z dnia 28 lipca 2005 r. o kosztach sądowych w sprawach cywilnych (UKSC)** — Dz.U. 2005 nr 167 poz. 1398 z późn. zm. Po reformie z 21.08.2019 r. system został znacznie uproszczony.

## Aktualne parametry — pobrać przed obliczeniem

| Parametr | Źródło | Sposób pobrania | Fallback _(ostatnio zweryfikowany)_ |
|---|---|---|---|
| Skala opłat stosunkowych (art. 13 UKSC) | UKSC — Dz.U. 2005 nr 167 poz. 1398 | WebFetch: `https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20051671398` — tekst jednolity, art. 13 | Tabela poniżej _(skala od 21.08.2019)_ |
| Opłaty stałe (art. 26–37 UKSC) | UKSC j.w. | j.w. — art. 26–37 | Tabela poniżej _(stan na 2024)_ |

**Zasady:**
1. **Fetch udany** → użyj pobranej wartości, podaj źródło i datę.
2. **Fetch nieudany** → użyj fallback. Ostrzeż: «⚠ Skala opłat pochodzi ze stanu na [data]. Weryfikuj w ISAP.»

## Trzy rodzaje opłat (art. 12 UKSC)

1. **Opłata stosunkowa** — od pism procesowych w sprawach o prawa majątkowe.
2. **Opłata stała** — od pism wskazanych konkretnie w UKSC (kwota stała).
3. **Opłata podstawowa** — gdy ustawa nie określa innej (30 zł — art. 14 UKSC).

## Opłata stosunkowa (art. 13 UKSC)

**Skala obowiązująca po reformie z 21.08.2019 r.**:

| Wartość przedmiotu sporu (WPS) | Opłata |
|---|---|
| do 500 zł | 30 zł |
| ponad 500 zł do 1 500 zł | 100 zł |
| ponad 1 500 zł do 4 000 zł | 200 zł |
| ponad 4 000 zł do 7 500 zł | 400 zł |
| ponad 7 500 zł do 10 000 zł | 500 zł |
| ponad 10 000 zł do 15 000 zł | 750 zł |
| ponad 15 000 zł do 20 000 zł | 1 000 zł |
| **ponad 20 000 zł** | **5% WPS, max 200 000 zł** |

*Skala — fallback; weryfikować przez fetch-blok wyżej.*

## Opłaty stałe (przykłady — art. 26–37 UKSC)

| Sprawa | Opłata |
|---|---|
| Rozwód / separacja | 600 zł |
| Sprawa o alimenty (od dochodzącego) | Bez opłaty (art. 96 ust. 1 pkt 2 UKSC — zwolnienie ustawowe) |
| Sprawa o ustalenie ojcostwa / macierzyństwa | 200 zł |
| Sprawa o naruszenie posiadania | 200 zł |
| Wniosek o wpis hipoteki / służebności do KW | 200 zł |
| Wniosek o stwierdzenie nabycia spadku | 100 zł |
| Wniosek o dział spadku | 500 zł (1000 zł, jeżeli zgodny projekt) |
| Wniosek o ogłoszenie upadłości | 1 000 zł |
| Wniosek o restrukturyzację | wg trybu (np. 1 000 zł) |
| Skarga na czynność komornika | 100 zł |
| Wniosek o nadanie klauzuli wykonalności | 6 zł (przeciwko jednemu dłużnikowi) |
| Wniosek o uzasadnienie wyroku | 100 zł (zaliczana na poczet apelacji) |
| Apelacja / skarga kasacyjna | wg WPS (jak od pozwu, tj. 5% przy WPS > 20 tys.) |
| Zażalenie na postanowienie kończące postępowanie | 1/5 opłaty od pozwu / wniosku, ale nie mniej niż 30 zł i nie więcej niż 200 zł |
| Wniosek o zabezpieczenie powództwa | 100 zł (przed wszczęciem postępowania); w toku — bez opłaty |
| Sprzeciw od wyroku zaocznego | 1/2 opłaty od pozwu |
| Zarzuty od nakazu zapłaty (postępowanie nakazowe) | 3/4 opłaty od pozwu (art. 19 ust. 4 UKSC) |
| Sprzeciw od nakazu zapłaty (postępowanie upominawcze) | bez opłaty |
| Pozew w postępowaniu nakazowym | 1/4 opłaty od pozwu (art. 19 ust. 2 UKSC) |
| EPU (e-Sąd) | 1/4 opłaty stosunkowej (min. 30 zł) |

## Opłata podstawowa (art. 14 UKSC)

- **30 zł** — od pism wnoszonych w sprawach niemajątkowych, gdy ustawa nie określa innej.

## Sprawy wieczystoksięgowe — specyficzne opłaty

| Wpis | Opłata |
|---|---|
| Założenie nowej KW | 100 zł |
| Wpis własności (sprzedaż / darowizna nieruchomości) | 200 zł |
| Wpis hipoteki | 200 zł |
| Wpis ostrzeżenia | 60 zł |
| Wpis służebności | 200 zł |
| Wpis spadkowy | 150 zł |
| Sprostowanie wpisu | 60 zł |

## Zwolnienia ustawowe (art. 95 i nast. UKSC)

Bez opłaty — m.in.:
- Sprawy o alimenty (po stronie dochodzącego — art. 96 ust. 1 pkt 2 UKSC).
- Sprawy o przyznanie zasiłku rodzinnego, świadczeń pomocowych.
- Sprawy z zakresu prawa pracy (po stronie pracownika, gdy WPS ≤ 50 000 zł — art. 96 ust. 1 pkt 4 UKSC).
- Sprawy z ubezpieczenia społecznego (po stronie ubezpieczonego — art. 96 ust. 1 pkt 4 UKSC).
- Wnioski Rzecznika Praw Obywatelskich.
- Strony zwolnione z mocy prawa (m.in. dłużnicy alimentacyjni w postępowaniach o alimenty, pracownicy do 50 tys.).

## Zwolnienie na wniosek (art. 102 UKSC)

**Przesłanki**: strona nie jest w stanie ponieść kosztów bez uszczerbku dla utrzymania koniecznego dla siebie i rodziny.

**Wymagania formalne**:
- Wniosek pisemny.
- Załączone **oświadczenie o stanie majątkowym i o źródłach utrzymania** — formularz urzędowy (wzór: rozporządzenie MS).
- Dokumenty potwierdzające stan majątkowy (zaświadczenia o dochodach, wyciągi bankowe, umowy najmu, orzeczenia o niepełnosprawności).

**Zakres**:
- Pełne zwolnienie (od całości kosztów).
- Częściowe zwolnienie (od części — np. od opłaty od pozwu, ale nie od kosztów dowodów).
- Rozłożenie na raty (art. 105 UKSC).

**Postanowienie sądu** — zaskarżalne zażaleniem.

**Uwaga**: zwolnienie od kosztów sądowych nie zwalnia od obowiązku zwrotu kosztów procesu stronie wygrywającej (art. 108 UKSC).

## Zwrot opłaty (art. 79 UKSC)

W określonych przypadkach sąd zwraca część opłaty:
- Cofnięcie pozwu przed wysłaniem pozwanemu: **100% zwrotu**.
- Cofnięcie pozwu po wysłaniu pozwanemu, przed rozprawą: **75% zwrotu**.
- Zawarcie ugody przed pierwszym posiedzeniem: **75% zwrotu**.
- Zawarcie ugody w toku postępowania: **50% zwrotu**.
- Skierowanie sprawy do mediacji na pierwszej rozprawie / przed nią: **75% zwrotu** (jeżeli ugoda).

## Workflow obliczania

1. **Tryb postępowania**: cywilne / gospodarcze / administracyjne / wieczystoksięgowe.
2. **Charakter sprawy**: majątkowa / niemajątkowa.
3. **Wartość przedmiotu sporu (dla majątkowych)**: należność główna + odsetki na dzień wniesienia pozwu + kary umowne + inne dochodzone kwoty. Koszty procesu (zastępstwo, opłata, biegli) **nie wchodzą do WPS** (art. 20 KPC).
4. **Sprawdzenie zwolnień ustawowych** (art. 95–96 UKSC).
5. **Obliczenie**:
   - Majątkowa do 20 000 zł → wg skali tabelarycznej.
   - Majątkowa powyżej 20 000 zł → 5% WPS, max 200 000 zł.
   - Niemajątkowa → opłata stała wg listy (art. 26–37 UKSC) lub podstawowa (30 zł).
6. **Modyfikatory**: pozew nakazowy 1/4, EPU 1/4, sprzeciw od wyroku zaocznego 1/2, zarzuty od nakazu w postępowaniu nakazowym 3/4 itd.
7. **Brak możliwości uiszczenia** → wniosek o zwolnienie z art. 102 UKSC + oświadczenie o stanie majątkowym.

## Przykład 1 — pozew o zapłatę 50 000 zł

- WPS = 50 000 zł
- Powyżej 20 000 zł → 5% × 50 000 = **2 500 zł**
- Tryb nakazowy (jeżeli udokumentowane) — 1/4 × 2 500 = **625 zł**
- EPU — 1/4 × 2 500 = **625 zł**
- Tryb upominawczy / zwykły — pełne **2 500 zł**

## Przykład 2 — pozew o zapłatę 1 200 zł

- WPS = 1 200 zł
- Skala: ponad 500 do 1 500 zł → **100 zł**
- Tryb nakazowy / EPU — 1/4 × 100 = 25 zł, ale nie mniej niż **30 zł** (opłata podstawowa) → 30 zł

## Przykład 3 — apelacja od wyroku zasądzającego 50 000 zł

- WPS = 50 000 zł
- Apelacja: 5% × 50 000 = **2 500 zł** (taka sama jak od pozwu)
- Wniosek o uzasadnienie (warunek apelacji od pełnego uzasadnienia): **100 zł** (zaliczane na poczet opłaty od apelacji).

## Najczęstsze błędy

- **Stosowanie starej skali** sprzed reformy z 21.08.2019 r. (przed reformą opłata stosunkowa to było 5% również dla małych spraw, bez tabelarycznych progów).
- **Włączanie kosztów do WPS.** Zastępstwo procesowe, biegli, opłata sądowa — nie wchodzą do WPS (art. 20 KPC).
- **Pomijanie minimum 30 zł** (opłaty podstawowej) przy małych roszczeniach.
- **Mylenie opłaty od pozwu z opłatą od apelacji.** Apelacja — taka sama jak od pozwu (5% w sprawach majątkowych >20 tys.); zażalenie — 1/5.
- **Pomijanie maksimum 200 000 zł** dla bardzo dużych spraw.
- **Opłata od sprzeciwu od nakazu zapłaty** — w postępowaniu **nakazowym** (zarzuty) jest 3/4; w postępowaniu **upominawczym** (sprzeciw) jest **bez opłaty**. Łatwo pomylić.
- **Pomijanie zwolnień ustawowych** (np. w sprawach pracowniczych do 50 tys. — pracownik nie płaci).
- **Wniosek o uzasadnienie bez 100 zł** — od 2019 r. obowiązkowy wniosek z opłatą; bez tego — brak prawa do apelacji od pełnego uzasadnienia.
- **Posiadane stawki nie są aktualne.** UKSC była nowelizowana — sprawdzać aktualną wersję w ISAP.
