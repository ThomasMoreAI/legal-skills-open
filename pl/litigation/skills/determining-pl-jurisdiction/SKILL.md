---
name: determining-pl-jurisdiction
title: determining-pl-jurisdiction
description: Use when determining the proper Polish court for a lawsuit — identifying the correct type of proceedings (civil/commercial/administrative/criminal), territorial jurisdiction (which specific court), subject-matter jurisdiction (sąd rejonowy vs okręgowy), exclusive vs alternative vs contractual jurisdiction, or handling jurisdictional conflicts
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/skills/pl/law-pl-determining-pl-jurisdiction
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: litigation
language: pl
---

# determining-pl-jurisdiction

Niewłaściwe ustalenie właściwości = przekazanie sprawy lub zwrócenie pozwu, utrata czasu i terminów procesowych. Sprawdzenie właściwości — pierwszy krok przed sporządzeniem pozwu.

## Krok 1. Tryb postępowania (właściwość rzeczowa)

| Typ sporu | Tryb |
|---|---|
| Spory cywilne między osobami fizycznymi; cywilnoprawne między osobą fizyczną a osobą prawną; spadkowe; rodzinne; dotyczące ochrony konsumentów | **Cywilny** (KPC) |
| Sprawy gospodarcze: między przedsiębiorcami w zakresie ich działalności gospodarczej; spory korporacyjne; postępowania upadłościowe / restrukturyzacyjne; spory z umów handlowych | **Gospodarczy** (KPC, ale w odrębnym dziale IVa, art. 458¹ i nast. — odrębne wydziały) |
| Sprawy z ubezpieczeń społecznych | **Z ubezpieczeń społecznych** (KPC, sąd okręgowy — wydział pracy i ubezpieczeń społecznych) |
| Sprawy z prawa pracy | **Pracy** (KPC, sąd rejonowy / okręgowy — wydział pracy) |
| Skarga na decyzję administracyjną; skarga na bezczynność / przewlekłość organu | **Administracyjny** (PPSA — WSA / NSA) |
| Sprawa karna | **Karny** (KPK — sąd rejonowy / okręgowy) |
| Sprawa o wykroczenie | **W sprawach o wykroczenia** (KPW — sąd rejonowy) |
| Sprawa nieletniego | **Nieletnich** (ustawa o postępowaniu w sprawach nieletnich) |

## Krok 2. Właściwość rzeczowa — sąd rejonowy vs okręgowy

### Sprawy cywilne (art. 16–17 KPC)

**Sąd rejonowy** — co do zasady (właściwość ogólna, art. 16 KPC).

**Sąd okręgowy** (art. 17 KPC) — m.in.:
- Sprawy o **prawa niemajątkowe** i łącznie z nimi dochodzone roszczenia majątkowe (z wyjątkami).
- Sprawy o **ochronę praw autorskich i pokrewnych**, prawa własności przemysłowej, ochronę dóbr osobistych.
- Sprawy o **roszczenia wynikające z prawa prasowego**.
- Sprawy o **prawa majątkowe**, w których wartość przedmiotu sporu **przekracza 100 000 zł** (z wyjątkami: alimenty, czynsz, spory o stanowisko pracy itp. — pozostają w sądach rejonowych).
- Sprawy o **rozwód, separację, ustalenie nieistnienia / unieważnienie małżeństwa**.
- Sprawy o roszczenia z **rękojmi i gwarancji** w niektórych konfiguracjach.
- **Wpis do rejestru** w sprawach gospodarczych (KRS) — sądy rejonowe (gospodarcze KRS).

### Sprawy gospodarcze (art. 458² KPC)

**Sąd gospodarczy** = wydział gospodarczy sądu **rejonowego** lub **okręgowego** (zależnie od WPS i kategorii).

**Definicja sprawy gospodarczej** (art. 458² KPC): m.in.:
- Spory między przedsiębiorcami w zakresie prowadzonej działalności.
- Spory o roszczenia z umów spółki (między spółką a jej organami / wspólnikami).
- Spory upadłościowe i restrukturyzacyjne.
- Spory z prawa ochrony konkurencji (UOKiK).

### Sprawy karne (art. 24–25 KPK)

**Sąd rejonowy** — co do zasady (właściwość ogólna).

**Sąd okręgowy** (art. 25 KPK) — m.in.:
- Zbrodnie (przestępstwa zagrożone karą pozbawienia wolności od 3 lat lub surowszą).
- Występki przeciwko bezpieczeństwu RP, zdrowiu publicznemu, niektóre kwalifikowane.
- Sprawy z aktem oskarżenia od prokuratury IPN.

### Sprawy administracyjne

- **WSA (wojewódzki sąd administracyjny)** — pierwsza instancja (art. 13 PPSA — wg siedziby organu, którego decyzja jest zaskarżana).
- **NSA** — druga instancja, wyłącznie skargi kasacyjne (art. 173 PPSA).

## Krok 3. Właściwość miejscowa

### Cywilne (art. 27–46 KPC)

#### Ogólna (art. 27 KPC)

- Pozwany — osoba fizyczna: sąd jego **miejsca zamieszkania** (art. 25–28 KC: miejsce zamieszkania = miejscowość, w której osoba przebywa z zamiarem stałego pobytu).
- Pozwany — osoba prawna / jednostka organizacyjna bez osobowości prawnej: sąd jej **siedziby**.
- Skarb Państwa: sąd, w którego okręgu ma siedzibę jednostka organizacyjna SP związana ze sprawą (art. 29 KPC).

#### Przemienna (art. 31–37¹ KPC) — na wybór powoda

Powód może wnieść powództwo do sądu właściwości ogólnej **lub** do innego określonego sądu, zależnie od typu sprawy:

- **Roszczenia z umowy** (art. 34 KPC) — sąd miejsca wykonania umowy.
- **Roszczenia z czynu niedozwolonego** (art. 35 KPC) — sąd, w którego okręgu nastąpiło zdarzenie wywołujące szkodę.
- **Alimenty** (art. 32 KPC) — sąd miejsca zamieszkania osoby uprawnionej.
- **Sprawy konsumenckie** — od 2019 r. konsument może wybrać sąd swojego miejsca zamieszkania (art. 37¹ KPC).
- **Sprawy o roszczenia z umów najmu** lokali — sąd miejsca położenia lokalu.

#### Wyłączna (art. 38–42 KPC) — nie podlega umownej zmianie

- **Powództwa o prawa rzeczowe na nieruchomościach**, posiadanie, użytkowanie wieczyste — sąd miejsca położenia nieruchomości (art. 38 KPC).
- **Sprawy spadkowe** — sąd ostatniego miejsca zwykłego pobytu spadkodawcy w Polsce; gdy nie da się ustalić — sąd miejsca położenia majątku spadkowego (art. 39 KPC).
- **Sprawy ze stosunku członkostwa spółdzielni / spółki / stowarzyszenia** — sąd siedziby (art. 40 KPC).
- **Sprawy małżeńskie** (rozwód, separacja, unieważnienie) — sąd ostatniego wspólnego miejsca zamieszkania małżonków, jeżeli choć jedno z nich tam jeszcze przebywa (art. 41 KPC).

#### Umowna (art. 46 KPC)

- Strony mogą umówić się na sąd inny niż wynikający z właściwości ogólnej / przemiennej.
- **Wyłączna jest niemożliwa do zmiany umownej.**
- W umowach z konsumentami — od 2019 r. (po nowelizacji w związku z dyrektywą 93/13/EWG i orzecznictwem TSUE) — istotne ograniczenia; klauzula prorogacyjna w umowie konsumenckiej często jest niedozwoloną klauzulą umowną (art. 385³ pkt 23 KC).

### Administracyjne (art. 13 PPSA)

WSA według siedziby organu, którego działanie / bezczynność jest zaskarżana.

### Karne (art. 31 KPK)

- Sąd, w którego okręgu popełniono przestępstwo.
- Subsydiarnie — sąd miejsca ujawnienia / ujęcia sprawcy lub jego miejsca zamieszkania.

## Krok 4. Hierarchia instancyjna

| Instancja | Właściwość |
|---|---|
| Sąd rejonowy | Pierwsza (sprawy cywilne, karne, gospodarcze, pracy) |
| Sąd okręgowy | Pierwsza (powyżej progów) i druga (apelacja od rejonowych) |
| Sąd apelacyjny | Druga (apelacja od okręgowych jako sądu I instancji) |
| Sąd Najwyższy | Skarga kasacyjna, wnioski o wznowienie, skargi nadzwyczajne, uchwały (zagadnienia prawne) |
| WSA | Pierwsza (skarga na decyzje administracyjne) |
| NSA | Druga (skarga kasacyjna od WSA) |
| Trybunał Konstytucyjny | Kontrola zgodności z Konstytucją; pytania prawne; skargi konstytucyjne |

## Sądy specjalne i odrębne

- **Sąd Ochrony Konkurencji i Konsumentów (SOKiK)** — XVII Wydział Sądu Okręgowego w Warszawie. Sprawy odwołań od decyzji UOKiK, URE, UKE, UTK.
- **Sąd ds. własności intelektualnej** — wyspecjalizowane wydziały w wybranych sądach okręgowych (od 2020 r. — Warszawa, Lublin, Poznań, Gdańsk, Katowice). Sprawy z prawa autorskiego, znaków towarowych, wzorów przemysłowych itd.
- **Krajowa Izba Odwoławcza (KIO)** — środki odwoławcze w zamówieniach publicznych (art. 513 i nast. PZP).

## Sprawdzenie konkretnego sądu

Przez **gov.pl/web/sprawiedliwosc** lub bezpośrednio strony sądów:
- Wyszukiwarka sądów wg kodu pocztowego / miejscowości.
- Obszar właściwości terytorialnej.
- Kontakty, godziny urzędowania, rachunek bankowy.

Każdy sąd ma stronę z BIP-em zawierającym informacje o właściwości obszarowej.

## Najczęstsze błędy

- **Cywilny vs gospodarczy.** Jeżeli choć jedna ze stron NIE jest przedsiębiorcą lub spór nie wynika z działalności gospodarczej — to NIE jest sprawa gospodarcza (chyba że szczególne wskazanie w art. 458² KPC). Przykład: spór konsumenta z przedsiębiorcą — co do zasady cywilny (postępowanie uproszczone lub zwykłe), nie gospodarczy.
- **Administracyjny vs cywilny.** Działanie organu jako władzy publicznej (decyzja, zezwolenie, koncesja) → administracyjny (WSA). Działanie organu jako strony stosunku cywilnoprawnego (np. umowa najmu nieruchomości komunalnej) → cywilny.
- **Pomijanie wyłącznej właściwości.** Nieruchomości, spadki, sprawy spółdzielcze, sprawy małżeńskie — według wyłącznych zasad niezależnie od umów stron.
- **Umowna jurysdykcja przy wyłącznej.** Umowa stron NIE pokonuje wyłącznej właściwości miejscowej.
- **Klauzule prorogacyjne w umowach z konsumentami.** Często niedozwolone (art. 385³ pkt 23 KC) — TSUE: sprawy konsumenckie powinny być rozpoznawane w sądzie miejsca zamieszkania konsumenta.
- **Mylenie sądu okręgowego jako I instancji vs II instancji.** Sąd okręgowy bywa I instancją (powyżej progów majątkowych, sprawy o niemajątkowe, rozwód) i II instancją (apelacja od sądu rejonowego).
- **Nowelizacje KPC zmieniają progi.** Próg 100 000 zł wprowadzono nowelizacją z 04.07.2019 r. (poprzednio 75 000 zł); sprawdzać aktualne brzmienie art. 17 KPC.
- **Niewłaściwe wydziały sądów gospodarczych.** Każdy sąd okręgowy ma odrębne wydziały: cywilny, gospodarczy, pracy, ubezpieczeń społ., rodzinny, karny. Skierowanie do złego wydziału wydłuża postępowanie.
- **EPU jako wybór miejscowy.** EPU (e-Sąd w Lublinie) — szczególny tryb dla powództw o zapłatę; wybór wierzyciela, ale jeżeli pozwany wniesie sprzeciw — sprawa trafia do sądu właściwego ogólnie.
