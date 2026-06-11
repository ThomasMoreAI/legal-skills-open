---
name: searching-orzeczenia
title: searching-orzeczenia
description: Use when searching Polish court decisions across the Common Courts Portal (Portal Orzeczeń Sądów Powszechnych), Supreme Court database (sn.pl), Supreme Administrative Court (NSA / WSA), Constitutional Tribunal (TK), or Court of Justice of the EU; verifying case citations; retrieving rulings by sygnatura akt; locating judicial practice on a specific legal issue
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/plugins/pl/skills/searching-orzeczenia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: litigation
language: pl
---

# searching-orzeczenia

Polskie orzecznictwo jest rozproszone po kilku bazach — w zależności od typu sądu. Każda baza ma swoją strukturę i wyszukiwarkę.

## Bazy źródłowe

| Baza | URL | Zakres |
|---|---|---|
| Portal Orzeczeń Sądów Powszechnych | https://orzeczenia.ms.gov.pl/ | Sądy rejonowe, okręgowe, apelacyjne (cywilne, gospodarcze, karne, pracy, ubezpieczeń społ., rodzinne) |
| Sąd Najwyższy — baza orzeczeń | https://www.sn.pl/orzecznictwo/SitePages/Baza_orzeczen.aspx | Orzeczenia SN (Izby: Cywilna, Karna, Pracy i Ubezpieczeń Społecznych, Kontroli Nadzwyczajnej i Spraw Publicznych, Dyscyplinarna) |
| Centralna Baza Orzeczeń Sądów Administracyjnych (CBOSA) | https://orzeczenia.nsa.gov.pl/ | NSA + wszystkie WSA |
| Trybunał Konstytucyjny | https://trybunal.gov.pl/ | Wyroki, postanowienia, sygnalizacje TK |
| TSUE (CURIA) | https://curia.europa.eu/jcms/jcms/Jo2_7045/pl/ | Orzecznictwo TSUE; wybrać język polski |
| ETPCz (HUDOC) | https://hudoc.echr.coe.int/ | Orzecznictwo ETPCz; możliwość filtrowania po Polsce |
| Krajowy Rejestr Orzeczeń | (rozproszony) | (jeszcze nie ma jednego ogólnopolskiego rejestru obejmującego wszystkie orzeczenia) |

## Sygnatura akt — struktura

**Sądy powszechne**:
```
[oznaczenie wydziału] [numer]/[rok]
```

Przykłady:
- `I C 1234/22` — I Wydział Cywilny, sprawa 1234 z 2022 r. (sąd rejonowy / okręgowy)
- `I ACa 567/23` — I Wydział Cywilny Apelacyjny (sąd apelacyjny)
- `V GC 89/24` — V Wydział Gospodarczy (sąd okręgowy)
- `II K 12/22` — II Wydział Karny

**Sąd Najwyższy**:
- `I CSK 123/22` — Izba Cywilna, Skarga Kasacyjna
- `III CZP 12/23` — Izba Cywilna, zagadnienie prawne (uchwała)
- `II UK 45/22` — Izba Pracy i Ubezpieczeń Społecznych

**Sądy administracyjne**:
- `II SA/Wa 1234/22` — WSA w Warszawie, II Wydział, skarga
- `II OSK 567/23` — NSA, Izba Ogólnoadministracyjna, skarga kasacyjna
- `II FSK 890/22` — NSA, Izba Finansowa

**Trybunał Konstytucyjny**:
- `K 12/22` — sprawa pełnoskładowa (kontrola konstytucyjności)
- `P 5/22` — pytanie prawne sądu
- `SK 7/23` — skarga konstytucyjna

## Workflow wyszukiwania

### Według sygnatury akt

1. **Sąd powszechny**: wprowadzić sygnaturę w wyszukiwarkę Portalu Orzeczeń. Wynik — orzeczenie z uzasadnieniem (jeżeli zostało udostępnione; nie wszystkie orzeczenia są w bazie).
2. **Sąd Najwyższy**: wyszukiwarka SN po sygnaturze.
3. **NSA / WSA**: CBOSA — pełnotekstowa wyszukiwarka.
4. **Trybunał Konstytucyjny**: na stronie TK lista wyroków, wyszukiwanie po sygnaturze i dacie.

### Według tematu / problemu prawnego

1. **Sąd Najwyższy**: pełnotekstowa wyszukiwarka po słowach kluczowych z tezy. Filtrowanie po izbie, dacie. Najwartościowsze: **uchwały** (zwłaszcza składów powiększonych — 7 sędziów, izby, pełnego składu).
2. **NSA**: CBOSA — wyszukiwanie pełnotekstowe + filtrowanie po sygnaturze, dacie, sądzie.
3. **Sądy powszechne**: Portal Orzeczeń — wyszukiwanie ograniczone, mało precyzyjne. Często lepiej zaczynać od SN, by ustalić linię orzeczniczą, a potem szukać konkretnych spraw.

### Weryfikacja cytatu

- Otworzyć oryginał w odpowiedniej bazie.
- Sprawdzić **prawomocność** — czy orzeczenie nie zostało zaskarżone i uchylone w wyższej instancji. Dla sądów powszechnych — sprawdzić wyrok II instancji w tej samej sprawie.
- Sprawdzić **stan rzeczy** — orzeczenie mogło być uchylone wyrokiem TK lub w wyniku skargi nadzwyczajnej.

## Hierarchia mocy stanowisk

| Organ | Moc orzecznicza |
|---|---|
| Trybunał Konstytucyjny | Powszechnie obowiązująca; usuwa normę z obrotu (art. 190 Konstytucji) |
| Uchwały SN składu pełnego, izby, połączonych izb | Mają moc zasady prawnej w obrębie SN; wiążą inne składy SN |
| Uchwały SN składu 7 sędziów | Mają moc zasady prawnej w obrębie SN, gdy SN tak postanowi |
| Uchwały NSA (rozszerzone) | Wiążą wszystkie składy NSA i sądy administracyjne |
| Wyroki TSUE | Wiążą sądy państw członkowskich w zakresie wykładni prawa UE |
| Wyroki ETPCz | Wiążą Polskę co do indywidualnej sprawy; wyrok TK / SN może uznawać konsekwencje |
| Wyroki SN (zwykłe składy) | Stanowiska istotne, ale nie mają mocy zasady prawnej automatycznie |
| Wyroki sądów apelacyjnych / okręgowych | Tylko dla konkretnej sprawy; w praktyce — wskazówka dla niższych instancji |
| Wyroki sądów I instancji | Tylko dla konkretnej sprawy |

## Format cytowania

**Wyrok SN**:
```
Wyrok Sądu Najwyższego z dnia 15.03.2023 r., sygn. I CSK 123/22
(opubl. www.sn.pl, OSNC 2023/4/45 — jeżeli opublikowany w zbiorach urzędowych).
```

**Uchwała SN**:
```
Uchwała Sądu Najwyższego z dnia 15.03.2023 r., sygn. III CZP 12/22
(skład 3 sędziów / 7 sędziów / izby).
```

**Wyrok NSA**:
```
Wyrok NSA z dnia 15.03.2023 r., sygn. II OSK 567/22 (CBOSA).
```

**Wyrok TK**:
```
Wyrok Trybunału Konstytucyjnego z dnia 15.03.2023 r., sygn. K 12/22
(OTK Seria A 2023/3/45).
```

**Wyrok TSUE**:
```
Wyrok TSUE z dnia 15.03.2023 r., C-123/22, ECLI:EU:C:2023:123, [Strony].
```

**Wyrok ETPCz**:
```
Wyrok ETPCz z dnia 15.03.2023 r., skarga nr 12345/20, [Strony] przeciwko Polsce.
```

## Zbiory urzędowe (pomocniczo)

| Skrót | Pełna nazwa | Sąd |
|---|---|---|
| OSNC | Orzecznictwo Sądu Najwyższego — Izba Cywilna | SN, Izba Cywilna |
| OSNK | Orzecznictwo Sądu Najwyższego — Izba Karna | SN, Izba Karna |
| OSNP | Orzecznictwo Sądu Najwyższego — Izba Pracy | SN, Izba Pracy |
| OSNwSK | Orzecznictwo Sądu Najwyższego w Sprawach Karnych | SN, Izba Karna |
| ONSAiWSA | Orzecznictwo NSA i WSA | NSA, WSA |
| OTK | Orzecznictwo Trybunału Konstytucyjnego | TK |

## Najczęstsze błędy

- **Cytowanie spraw „z pamięci".** Sygnatury akt bez weryfikacji — ryzyko halucynacji. Zawsze sprawdzać.
- **Pomijanie biegu sprawy.** Wyrok I instancji mógł zostać uchylony apelacją / kasacją — cytat uchylonego aktu jest bezpodstawny.
- **Mylenie izb SN.** Izba Cywilna, Karna, Pracy i Ubezpieczeń Społecznych, Kontroli Nadzwyczajnej, Dyscyplinarna — każda ma swoją linię. Przy konflikcie — uchwała pełnego składu / izby ma pierwszeństwo.
- **Poleganie na wyciągach z komentarzy.** Kontekst często ginie; czytać oryginalny tekst.
- **Mylenie sygnatur.** Sygnatura akt sprawy w I instancji ≠ sygnatura w II instancji ≠ sygnatura SN (jednej i tej samej sprawy). Każdy etap ma swoją.
- **Pomijanie zasady prawnej.** Niektóre uchwały SN / NSA mają **moc zasady prawnej** — wiążą inne składy. Brak respektowania → ryzyko uchylenia.
- **Cytowanie postanowień jako wyroków.** Postanowienia (procesowe, oddalające skargę nadzwyczajną, odmawiające przyjęcia kasacji) mają inny charakter niż wyroki merytoryczne.
- **Brak sprawdzenia w bazie.** Komercyjne systemy (Lex, Legalis) bywają opóźnione lub mają ograniczony zakres — autorytatywne są bazy oficjalne.
