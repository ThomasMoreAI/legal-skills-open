---
name: determining-wps
title: determining-wps
description: Use when calculating wartość przedmiotu sporu (WPS) under Polish KPC (art. 19–26) — determining its impact on subject-matter jurisdiction (rejonowy vs okręgowy), applicable court fee (opłata stosunkowa), rules for summing up multiple claims, treatment of interest, recurring benefits, claims concerning ownership / possession, and claims for declaration
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/plugins/pl/skills/determining-wps
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: litigation
language: pl
---

# determining-wps

Wartość przedmiotu sporu (WPS) — kluczowa kategoria procesowa w sprawach cywilnych. Decyduje o:
- **Właściwości rzeczowej** — sąd rejonowy vs. okręgowy (art. 17 pkt 4 KPC — okręgowy przy WPS > 100 000 zł _(art. 17 pkt 4 KPC — weryfikować w ISAP)_ w sprawach majątkowych; z wyjątkami).
- **Opłacie sądowej** — opłata stosunkowa vs. stała; tabelaryczna skala do 20 000 zł _(art. 505¹ KPC — weryfikować w ISAP)_, od 20 000 zł — 5% WPS (skill `calculating-oplata-sadowa`).
- **Trybie postępowania** — uproszczone (do 20 000 zł — art. 505¹ KPC).
- **Kosztach zastępstwa procesowego** — stawki minimalne wg WPS (rozporządzenie o opłatach za czynności adwokackie / radcy prawnego).

## Podstawa prawna

- **KPC art. 19–26** — ustalanie WPS.
- **KPC art. 17 pkt 4** — właściwość rzeczowa okręgowa od WPS > 100 000 zł (sprawy majątkowe).
- **KPC art. 20** — co nie wchodzi do WPS.
- **UKSC** — stawki opłat.

## Reguły ogólne (art. 19–26 KPC)

### Roszczenia pieniężne (art. 19 § 1 KPC)

**WPS = kwota dochodzona w pozwie** — należność główna, niezależnie od tego, jak powód ją podzielił w żądaniu.

**Bez odsetek** — odsetki umowne i ustawowe za opóźnienie naliczone **do dnia wniesienia pozwu** **nie wchodzą** do WPS (art. 20 KPC).

**Wyjątek:** odsetki skapitalizowane, które stały się samoistną częścią roszczenia (rzadko).

**Kary umowne, odszkodowania, rekompensaty** — wchodzą do WPS jako kwota dochodzona.

### Świadczenia powtarzające się (art. 22 KPC)

Dla roszczeń o świadczenia powtarzające się (np. alimenty, renta, czynsz z trwałego stosunku):

**WPS = suma świadczeń za 1 rok** (miesięczna rata × 12); jeżeli świadczenia są ograniczone w czasie do okresu krótszego niż rok — suma rzeczywistych świadczeń.

**Przykład:**
- Alimenty 1 000 zł/mies., bez ograniczenia → **WPS = 12 000 zł**.
- Renta 800 zł/mies. na okres 5 lat → **WPS = 48 000 zł** (nie ogranicza się do roku).

### Roszczenia o zwolnienie / wykonanie zobowiązania (art. 21 KPC)

Gdy żądanie dotyczy **zwolnienia z długu** lub **wykonania zobowiązania** — **WPS = wartość długu / zobowiązania**.

### Sprawy o własność, użytkowanie, współwłasność (art. 23 KPC)

**WPS = wartość rzeczy / prawa** — ustalana wg:
- Wycenę biegłego.
- Średnie ceny rynkowe (dla ruchomości).
- Wartość z aktu notarialnego (dla nieruchomości — ale zwykle wartość rynkowa z operatu szacunkowego biegłego lub z innej wyceny).

**Współwłasność** — WPS = wartość udziału dochodzonego.

### Sprawy o posiadanie (art. 24 KPC)

**WPS = wartość posiadania** — w praktyce wartość rzeczy lub praw posiadanych.

### Sprawy z najmu, dzierżawy (art. 25 KPC)

Gdy spór dotyczy umowy najmu / dzierżawy:
- **Na czas oznaczony** — WPS = suma świadczeń za cały okres trwania umowy, ale **nie więcej niż za 1 rok**.
- **Na czas nieoznaczony** — WPS = suma świadczeń za **6 miesięcy**.

### Dział spadku / zniesienie współwłasności (art. 26 KPC)

Opłata jest stała (500 zł / 1 000 zł dla działu — art. 38 UKSC; 300 zł dla zniesienia — art. 40 UKSC); WPS wykazuje się dla celów oznaczenia (nie wpływa na opłatę stałą, ale wpływa na koszty zastępstwa).

### Sprawy z zakresu prawa pracy (art. 22 KPC)

**Spory o prawa majątkowe dotyczące świadczeń powtarzających się** (wynagrodzenie, dodatki) — **WPS = suma świadczeń za 1 rok** (12 miesięcy).

**Przywrócenie do pracy / odszkodowanie za niezgodne wypowiedzenie** — WPS = 12 × miesięczne wynagrodzenie (art. 45 KP).

## Wyłączenia z WPS (art. 20 KPC)

**Nie wchodzą:**
- Odsetki.
- Koszty procesu.
- Koszty zastępstwa procesowego.
- Kary umowne i inne roszczenia uboczne **tylko wtedy**, gdy mają charakter **uboczny** wobec roszczenia głównego.

**Uwaga:** kara umowna dochodzona **jako samodzielne roszczenie** — wchodzi do WPS (nie jest uboczna).

## Sumowanie roszczeń (art. 21 KPC)

Gdy powód dochodzi kilku roszczeń **w tym samym pozwie** — WPS = **suma wartości wszystkich**.

**Wyjątek:** jeżeli żądania są **z różnych tytułów**, sąd może rozdzielić sprawy, ale dla celów WPS sumuje się.

**Roszczenia ewentualne** — WPS ustala się od roszczenia głównego; ewentualne nie podlega sumowaniu (orzecznictwo SN — postanowienie z 27.03.2014 r., III CZ 9/14).

**Odszkodowanie + zadośćuczynienie** — sumują się (oba są roszczeniami majątkowymi o własnych kwotach).

## Rozszerzenie / ograniczenie powództwa

**Rozszerzenie** — wpływa na WPS; pociąga **uzupełnienie opłaty sądowej** (art. 18 UKSC).

**Ograniczenie / cofnięcie** — WPS nie zmienia się formalnie; możliwy zwrot części opłaty (art. 79 UKSC — 75% lub 50%, zależnie od etapu).

## Roszczenia o ustalenie (art. 189 KPC)

**Sprawy o ustalenie istnienia / nieistnienia stosunku prawnego lub prawa** — dotyczą spraw majątkowych, ale bez bezpośrednio dochodzonej kwoty.

**WPS w sprawach o ustalenie:**
- Brak jednolitej zasady; orzecznictwo:
  - **Wartość prawa / stosunku**, którego dotyczy ustalenie (np. wartość umowy, wartość nieruchomości).
  - Dla frankowiczów (kredyt CHF) — wartość pozostałego kredytu albo wartość wszystkich pozostałych rat; sądy okręgowe często przyjmują wartość kredytu na dzień pozwu.

**Sprawy niemajątkowe** (np. ustalenie ojcostwa) — **brak WPS**, opłata stała.

## Przykłady

### Przykład 1 — pozew o zapłatę 80 000 zł + odsetki od 2023

- Kwota główna: 80 000 zł.
- Odsetki skapitalizowane na dzień pozwu: 12 000 zł.
- **WPS = 80 000 zł** (odsetki poza WPS).
- Opłata: **4 000 zł** (5% od 80 000).
- Właściwość: **rejonowy** (< 100 000 zł).

### Przykład 2 — pozew o alimenty 1 500 zł/mies.

- Rata miesięczna: 1 500 zł.
- **WPS = 18 000 zł** (1 500 × 12).
- Opłata — **bez opłaty** (art. 96 ust. 1 pkt 2 UKSC — zwolnienie).
- Właściwość: **rejonowy** (sąd rodzinny).

### Przykład 3 — pozew o wydanie nieruchomości (windykacyjny)

- Wartość nieruchomości z operatu: 800 000 zł.
- **WPS = 800 000 zł**.
- Opłata: 5% × 800 000 = 40 000 zł (< pułap 200 000).
- Właściwość: **okręgowy** (> 100 000 zł).

### Przykład 4 — pozew o zapłatę + odszkodowanie + kara umowna

- Zapłata należności: 50 000 zł.
- Odszkodowanie (za zwłokę): 10 000 zł.
- Kara umowna (samodzielna): 8 000 zł.
- **WPS = 68 000 zł**.
- Opłata: 5% × 68 000 = 3 400 zł.

### Przykład 5 — pozew frankowiczowski

- Żądanie główne: ustalenie nieważności umowy kredytu (kredyt pozostały — 400 000 zł).
- Żądanie pieniężne: zwrot uiszczonych rat — 250 000 zł.
- **WPS:**
  - Linia 1 (ostrożna): suma = 650 000 zł.
  - Linia 2 (sądy warszawskie) — WPS wg roszczenia pieniężnego + ustalenia: 400 000 + 250 000 = 650 000 zł.
- Opłata: 5% × 650 000 = 32 500 zł (na konsumenta — wniosek o zwolnienie art. 102 UKSC).
- Właściwość: **okręgowy**.

### Przykład 6 — pozew pracowniczy o przywrócenie do pracy

- Miesięczne wynagrodzenie: 7 000 zł brutto.
- **WPS = 84 000 zł** (7 000 × 12).
- Opłata: zwolnienie (art. 96 ust. 1 pkt 4 UKSC — pracownik przy WPS ≤ 50 000 zł _(art. 96 ust. 1 pkt 4 UKSC — weryfikować)_ zwolniony; przy 84 000 zł — opłata od nadwyżki ponad 50 000, czyli od 34 000 = 1 700 zł).
- Właściwość: **rejonowy** (< 100 000 zł).

## Wpływ WPS na tryb postępowania

| WPS | Tryb |
|---|---|
| ≤ 20 000 zł | Postępowanie uproszczone (art. 505¹ KPC) — prekluzja dowodowa, ograniczone środki zaskarżenia |
| > 20 000 zł, ≤ 100 000 zł | Postępowanie zwykłe w sądzie rejonowym |
| > 100 000 zł | Postępowanie zwykłe w sądzie okręgowym |

**Sprawy gospodarcze** — odrębny wydział (art. 458² KPC), niezależnie od WPS (jeśli spór wynika ze stosunku cywilnego między przedsiębiorcami związanego z działalnością).

## Właściwość rzeczowa (art. 16–17 KPC)

**Sąd rejonowy** — zasada ogólna (art. 16 KPC).

**Sąd okręgowy** (art. 17 KPC):
- pkt 1: sprawy o prawa niemajątkowe (rozwód, separacja, unieważnienie małżeństwa, ustalenie / zaprzeczenie ojcostwa itp., art. 17 pkt 1 — rozwód, pkt 2 — ochrona dóbr osobistych, pkt 3 — prawa autorskie).
- pkt 4: sprawy o roszczenia majątkowe, których wartość przedmiotu sporu przewyższa **100 000 zł** (oprócz spraw o alimenty, naruszenie posiadania, o ustanowienie rozdzielności majątkowej).
- pkt 4²: niektóre sprawy gospodarcze szczególne.

**Wyjątki:** niektóre sprawy są zawsze w sądzie rejonowym niezależnie od WPS (alimenty, posiadanie), niektóre zawsze w okręgowym (rozwód, dobra osobiste).

## Cytowanie w pozwie

**W petitum pozwu:** „wartość przedmiotu sporu: [X] zł".

**Jeśli sąd zakwestionuje** — postanowienie o sprawdzeniu WPS (art. 25 KPC); sąd może przekazać sprawę do właściwego sądu.

## Źródła

- **KPC** — art. 19–26 (WPS), art. 16–17 (właściwość rzeczowa), art. 20 (wyłączenia), art. 505¹ (uproszczone). ISAP: `WDU19640430296`.
- **UKSC** — art. 13 (opłata stosunkowa), art. 18 (uzupełnienie), art. 79 (zwrot). ISAP: `WDU20051671398`.
- **Rozporządzenie MS o stawkach minimalnych za czynności adwokackie / radcy prawnego** — zawierają tabele wg WPS.
- **Orzecznictwo SN** — postanowienia w kwestii sumowania, ewentualnych, skapitalizowanych odsetek. Przez skill `searching-orzeczenia`.

## Najczęstsze błędy

- **Włączanie odsetek do WPS.** Art. 20 KPC jednoznacznie wyłącza. Nawet odsetki za okres przed pozwem — nie wchodzą.
- **Włączanie kosztów zastępstwa / kosztów procesu.** Art. 20 KPC.
- **Nie zastosowanie art. 22 KPC do świadczeń powtarzających się.** Alimenty, renta, czynsz z trwałego stosunku — WPS = 12 × rata, nie pojedyncza rata.
- **Pominięcie 12× w pozwie pracowniczym.** Miesięczne wynagrodzenie × 12 dla przywrócenia do pracy.
- **WPS = sumą żądań ewentualnych.** Ewentualne nie sumują się z głównym; orzecznictwo SN.
- **WPS od roszczeń ubocznych.** Odsetki, koszty — uboczne — nie liczą się.
- **Mylenie opłaty stałej z opłatą stosunkową.** Dział spadku / zniesienie współwłasności — opłata stała; WPS wpływa tylko na koszty zastępstwa.
- **Wartość rzeczy wg wartości księgowej.** Dla pozwów o rzecz — wartość **rynkowa**, nie księgowa.
- **Zaniżanie WPS celowo dla uniknięcia SO.** Sąd sprawdza WPS (art. 25 KPC) i może przekazać. Ryzyko uznania za nadużycie.
- **Pomijanie rozszerzenia powództwa.** Rozszerzenie = uzupełnienie opłaty. Pominięcie = ewentualny zwrot pozwu w części rozszerzonej (art. 130 KPC).
- **Ustalanie WPS dla spraw o ustalenie.** Zależy od przedmiotu ustalenia; dla konkretnych kategorii (frankowicze) — aktualna praktyka sądów okręgowych jest kluczowa.
