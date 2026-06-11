---
name: applying-cudzoziemcy-procedures
title: applying-cudzoziemcy-procedures
description: Use when navigating Polish immigration / residence / work procedures — pobyt czasowy (art. 98, 114, 127, 144, 159, 187 UC), pobyt stały (art. 195), rezydent długoterminowy UE (art. 211), zezwolenie na pracę (typy A-E), oświadczenie o powierzeniu pracy, obywatelstwo (ustawa z 02.04.2009 — nadanie przez Prezydenta / uznanie wojewody). Dokumenty, biometria, MOS, terminy, odwołanie (Szef UdSC → WSA / NSA)
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/plugins/pl/skills/applying-cudzoziemcy-procedures
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: immigration
language: pl
---

# applying-cudzoziemcy-procedures

Procedury pobytowe, pracy i obywatelstwa dla cudzoziemców w Polsce są rozproszone między **urzędy wojewódzkie** (wydziały spraw cudzoziemców), **Szefa Urzędu do Spraw Cudzoziemców** (UdSC — II instancja), **Prezydenta RP** (nadanie obywatelstwa) i **powiatowe urzędy pracy / starostę** (testy rynku pracy, niektóre zezwolenia).

**Ustawy kluczowe:**
- **UC** — ustawa z 12.12.2013 o cudzoziemcach (Dz.U. 2013 poz. 1650) — pobyt czasowy, stały, rezydent UE, odmowa wjazdu.
- **UdSC** — ustawa z 12.12.2013 o udzielaniu cudzoziemcom ochrony (uchodźstwo, ochrona uzupełniająca, pobyt humanitarny, tolerowany).
- **PrZa** — ustawa z 20.04.2004 o promocji zatrudnienia i instytucjach rynku pracy (zezwolenia na pracę).
- **UOb** — ustawa z 02.04.2009 o obywatelstwie polskim (Dz.U. 2012 poz. 161).
- **KPA** — tryb, terminy, odwołania (stosowany podmocnie w UC).
- **Rozporządzenia wykonawcze** MSWiA, MRiPS, MZ (wykazy zawodów, stawki, formularze).

**Źródła urzędowe:**
- **Urząd do Spraw Cudzoziemców (UdSC)**: `https://www.gov.pl/web/udsc`.
- **MOS** (Moduł Obsługi Spraw): `https://mos.cudzoziemcy.gov.pl` — elektroniczne wnioski, konta cudzoziemców.
- Konkretne urzędy wojewódzkie — lokalne strony (np. `https://www.mazowieckie.pl/pl/urzad/cudzoziemcy`).
- Gov.pl: `https://www.gov.pl/web/gov/zamieszkaj-w-polsce`.
- ISAP: `https://isap.sejm.gov.pl`.

**Forma**: częściowo elektronicznie przez **MOS**; stawiennictwo osobiste **wymagane** dla złożenia odcisków palców (biometria) i osobistego doręczenia karty pobytu.

## Aktualne parametry — pobrać przed konsultacją

| Parametr | Źródło | Sposób pobrania | Fallback _(ostatnio zweryfikowany)_ |
|---|---|---|---|
| Opłata za pobyt czasowy | Rozp. MSWiA | WebSearch: «opłata za zezwolenie na pobyt czasowy [bieżący rok]» site:isap.sejm.gov.pl | 440 zł _(stan na 2024)_ |
| Opłata za pobyt stały / rezydenta UE | Rozp. MSWiA | j.w. | 640 zł _(stan na 2024)_ |
| Opłata za kartę pobytu | Rozp. MSWiA | j.w. | 100 zł _(stan na 2024)_ |
| Opłata za wizę | Rozp. MSZ | WebSearch: «opłata za wizę krajową [rok]» site:isap.sejm.gov.pl | 100 / 200 zł _(stan na 2024)_ |

**Zasady:**
1. **Fetch udany** → użyj pobranej wartości, podaj źródło i datę.
2. **Fetch nieudany** → użyj fallback. Ostrzeż: «⚠ Opłata pochodzi ze stanu na [data]. Sprawdź w ISAP lub na gov.pl.»

## 1. Zezwolenie na pobyt czasowy

**Właściwość**: wojewoda właściwy ze względu na miejsce zamieszkania cudzoziemca.

**Okres**: do 3 lat (większość podstaw).

**Formularz**: załącznik nr 1 do rozporządzenia MSWiA z 17.04.2019 w sprawie wzoru formularza wniosku o udzielenie cudzoziemcowi zezwolenia na pobyt czasowy; w MOS — elektronicznie.

### Podstawy najczęstsze

| Podstawa | Artykuł UC | Wymagania kluczowe |
|---|---|---|
| **Praca** | art. 114 | Umowa z pracodawcą + zezwolenie na pracę albo zawód z wykazu zawodów zwolnionych z testu; wynagrodzenie ≥ stawka minimalna (i spełniające wymogi rozporządzenia dla konkretnych typów) |
| **Praca dla cudzoziemca wykwalifikowanego (Blue Card)** | art. 127 | Dyplom wyższej szkoły; oferta pracy na co najmniej 12 mies.; wynagrodzenie ≥ 1,5x średniego krajowego |
| **Studia** | art. 144 | Zaświadczenie z uczelni; środki utrzymania; ubezpieczenie zdrowotne |
| **Członek rodziny obywatela UE / Polaka** | art. 158/159/166 | Akt małżeństwa / urodzenia; wspólne zamieszkanie; środki utrzymania (dla członka rodziny obywatela państwa trzeciego); dla małżonka Polaka — uproszczone |
| **Prowadzenie działalności gospodarczej** | art. 142 | Spółka z ograniczoną odpowiedzialnością / S.A.; określone przychody i zatrudnienie pracowników (zwykle min. 2 etaty); wpływ na polski rynek pracy |
| **Praca sezonowa** | art. 185a | Do 9 miesięcy w roku kalendarzowym; rolnictwo, ogrodnictwo, turystyka |
| **Pobyt humanitarny / tolerowany** | art. 187 / ustawa o ochronie cudzoziemców | Okoliczności humanitarne; niedopuszczalność zwrotu (non-refoulement) |
| **Pozostałe** (ofiara handlu ludźmi, delegacja, wolontariat, szkolenie zawodowe) | art. 176–181 | — |

### Wymagane dokumenty (wspólny rdzeń)

- Wniosek + **4 aktualne fotografie** biometryczne (opłata za złożenie wniosku — patrz dalej).
- Kopia **wszystkich wypełnionych stron paszportu** (oryginał przy złożeniu wniosku do wglądu).
- Potwierdzenie zameldowania lub oświadczenie o miejscu pobytu / umowa najmu.
- Potwierdzenie ubezpieczenia zdrowotnego (NFZ lub prywatne — dla niektórych kategorii).
- Potwierdzenie środków utrzymania (umowa o pracę / rozliczenie PIT / wyciąg z konta / oświadczenie poręczyciela).
- Potwierdzenie uiszczenia opłaty skarbowej.

### Opłaty

| Czynność | Opłata |
|---|---|
| Wniosek o zezwolenie na pobyt czasowy | **440 zł** _(fallback; stan na 2024)_ (opłata skarbowa) |
| Wniosek o pobyt stały | **640 zł** _(fallback; stan na 2024)_ |
| Wniosek o rezydenta długoterminowego UE | **640 zł** _(fallback; stan na 2024)_ |
| Karta pobytu (wydanie / wymiana) | **100 zł** _(fallback; stan na 2024)_ (opłata administracyjna) |
| Szybka procedura biometrii | — |

Opłata skarbowa na rachunek urzędu miasta/gminy (gdzie znajduje się urząd wojewódzki).

### Termin rozpatrzenia

- **Standardowy**: 1–2 miesiące (art. 35 § 3 KPA), **w praktyce w największych wojewódzkich urzędach** (Mazowieckie, Małopolskie, Dolnośląskie) zwykle **6–12 miesięcy**, a czasem dłużej.
- **Obligatoryjne czynności w trakcie**: biometria (odciski palców), rozmowa (przy wątpliwościach).
- **Stempel w paszporcie**: potwierdzenie złożenia wniosku — legalizuje pobyt do zakończenia sprawy (art. 108 UC).

### Odmowa i odwołanie

**Organ I instancji**: wojewoda.

**Odwołanie**: **Szef UdSC** w **14 dni** od doręczenia decyzji (art. 127 § 2 KPA w zw. z UC).

**Skarga do WSA**: 30 dni od doręczenia decyzji II instancji; następnie skarga kasacyjna do NSA.

## 2. Zezwolenie na pobyt stały (art. 195 UC)

**Najczęstsze podstawy**:
- Małżonek obywatela Polskiego (po 3 latach ważnego związku).
- Dziecko obywatela Polskiego lub cudzoziemca z pobytem stałym.
- Pochodzenie polskie (polska narodowość; karta Polaka).
- Rezydent długoterminowy UE w innym państwie członkowskim (po spełnieniu dodatkowych wymogów).
- Ofiara handlu ludźmi (po odpowiednich procedurach).
- Bezterminowy — zezwolenie stałe.

**Wymagania**: długość / typ poprzedniego pobytu, dokumenty potwierdzające podstawę.

**Termin rozpatrzenia**: 3 miesiące; w praktyce 6–12 miesięcy.

## 3. Zezwolenie rezydenta długoterminowego UE (art. 211 UC)

**Wymagania kluczowe**:
- **5 lat** legalnego i nieprzerwanego pobytu w RP (niektóre okresy nie są zaliczane, np. pobyt studenci — w połowie zalicza się).
- **Stabilne i regularne źródło dochodu** (nie niższe niż kwota uprawniająca do świadczeń socjalnych dla rodziny).
- **Ubezpieczenie zdrowotne**.
- **Znajomość języka polskiego** potwierdzona certyfikatem (zdany egzamin państwowy B1 lub świadectwo szkolne).

## 4. Zezwolenie na pracę — typy (A–E)

Podstawa: **PrZa** art. 88.

| Typ | Sytuacja |
|---|---|
| **A** | Zatrudnienie cudzoziemca na podstawie umowy z podmiotem mającym siedzibę w RP (większość przypadków) |
| **B** | Cudzoziemiec w zarządzie osoby prawnej wpisanej do KRS; > 6 miesięcy w roku |
| **C** | Delegowany przez podmiot zagraniczny do oddziału / zakładu w RP |
| **D** | Delegowany do tymczasowego świadczenia usługi eksportowej przez pracodawcę z zagranicy |
| **E** | Delegowany do innych celów niewymienionych w A–D |

**Test rynku pracy** (informacja starosty) — wymagany dla większości zezwoleń; wyjątki — zawody deficytowe z obwieszczenia MRiPS / pracownicy już zatrudnieni i wieloletni.

**Procedura** (typ A):
1. Pracodawca składa wniosek w **urzędzie wojewódzkim** (czasami z informacją starosty o braku możliwości zaspokojenia potrzeb kadrowych z lokalnego rynku pracy).
2. Decyzja — zwykle 2–3 miesiące.
3. Zezwolenie — wydawane **na okres wskazany w umowie o pracę**, max 3 lata.

**Opłata**: **100 zł** _(fallback; stan na 2024)_ za wniosek (dla zezwolenia < 3 miesięcy) lub **200 zł** _(fallback; stan na 2024)_ (dla zezwolenia > 3 miesięcy).

## 5. Oświadczenie o powierzeniu wykonywania pracy

**Kto może skorzystać**: obywatele **Armenii, Białorusi, Gruzji, Mołdawii, Ukrainy** — art. 88z PrZa (lista może być aktualizowana rozporządzeniem MRiPS).

**Tryb**: uproszczony — pracodawca składa **oświadczenie** w powiatowym urzędzie pracy (PUP), bez decyzji, bez testu rynku pracy.

**Okres**: **do 24 miesięcy** (od 01.11.2023 — dawniej 6 miesięcy w ciągu 12).

**Rejestracja**: elektroniczna w portalu `https://praca.gov.pl`.

**Opłata**: **100 zł** _(fallback; stan na 2024)_ (pracodawca).

**Wjazd i pobyt cudzoziemca**: na podstawie wizy / ruchu bezwizowego + oświadczenia wpisanego do ewidencji.

**Dla obywateli Ukrainy** — od 24.02.2022 specustawa (ustawa z 12.03.2022 o pomocy obywatelom Ukrainy w związku z konfliktem zbrojnym) → uproszczone reguły; od 01.07.2024 — powiadomienie pracodawcy w **7 dni**.

## 6. Karta Polaka

Ustawa z 07.09.2007 o Karcie Polaka.

**Warunki**: polskie pochodzenie (przynajmniej jedno z rodziców / dziadków / dwóch pradziadków — narodowość polska); znajomość języka polskiego; deklaracja przynależności do narodu polskiego.

**Organ**: konsul RP w państwie zamieszkania wnioskodawcy.

**Ważność**: 10 lat (odnawialna); karta jest bezpłatna.

**Uprawnienia**:
- Preferencyjny dostęp do studiów (bez opłat za niektóre kierunki).
- Darmowe wizy do Polski.
- Świadczenia: dofinansowanie do nauki, do osiedlenia się (w określonych programach).
- Podstawa do **zezwolenia na pobyt stały** po osiedleniu się w RP (art. 195 ust. 1 pkt 9 UC).

## 7. Obywatelstwo polskie

Ustawa z 02.04.2009 o obywatelstwie polskim.

### Dwa tryby:

### A. Nadanie przez Prezydenta RP (art. 18 i nast. UOb)

- **Wniosek**: przez wojewodę (jeśli cudzoziemiec mieszka w RP) lub konsula RP (jeśli za granicą).
- **Brak terminu**: procedura uznaniowa Prezydenta — może trwać od kilku miesięcy do kilku lat.
- **Brak odwołania** — decyzja Prezydenta nie jest zaskarżalna.

### B. Uznanie za obywatela polskiego (art. 30 UOb)

- **Decyzja wojewody** — procedura administracyjna, z obowiązkiem uzasadnienia; odwołanie do Ministra SWiA; skarga do WSA.
- **Warunki alternatywne**:
  - Co najmniej **3 lata** ważnego pobytu stałego / rezydenta długoterminowego UE + stabilne źródło dochodu + tytuł prawny do mieszkania;
  - lub pobyt stały + małżeństwo z obywatelem RP **minimum 3 lata**;
  - lub pobyt stały ≥ 2 lat + status uchodźcy;
  - kilka innych przesłanek.
- **Znajomość języka polskiego** — certyfikat B1 lub świadectwo ukończenia polskiej szkoły.
- **Nieposiadanie innego obywatelstwa** — **nie jest wymagane** (Polska akceptuje podwójne obywatelstwo).

### C. Przywrócenie obywatelstwa polskiego (art. 38 UOb)

- **Wniosek** do **Ministra SWiA**.
- **Warunki**: utrata obywatelstwa przed 01.01.1999 i nie z własnej woli (np. przez małżeństwo za granicą w okresie PRL).

### Opłata skarbowa

- Nadanie przez Prezydenta — **bezpłatne** (art. 2 ust. 1 pkt 7 ustawy o opłacie skarbowej).
- Uznanie za obywatela — **219 zł** _(fallback; stan na 2024)_ (decyzja wojewody).
- Przywrócenie — **219 zł** _(fallback; stan na 2024)_.

## 8. Karta pobytu i jej odbiór

Po wydaniu pozytywnej decyzji — **karta pobytu** (KP):
- Zamawiana automatycznie przez urząd.
- **Opłata**: 100 zł _(fallback; stan na 2024)_.
- **Odbiór**: osobiście w urzędzie wojewódzkim.
- **Okres ważności**: tyle, ile ważne zezwolenie (max 3 lata dla czasowego; 10 lat dla stałego/rezydenta UE).

## 9. Przedłużenie pobytu — obowiązek wcześniejszego wniosku

**Zasada krytyczna**: wniosek o przedłużenie / nowe zezwolenie należy złożyć **przed upływem dotychczasowego zezwolenia**. Stempel w paszporcie legalizuje pobyt do rozstrzygnięcia sprawy (art. 108 UC).

**Po upływie, bez wniosku** — nielegalny pobyt; ryzyko zobowiązania do powrotu (art. 298 UC), zakazu wjazdu do Schengen.

## 10. Odmowa — powody najczęstsze

- **Braki formalne** wniosku (brak załącznika, niewłaściwa fotografia, niepełna opłata) — uzupełnienie w **7 dni** (art. 64 § 2 KPA).
- **Niewystarczające środki utrzymania** — wynagrodzenie poniżej minimum, brak stabilności.
- **Brak tytułu prawnego do zamieszkania** — bez umowy najmu / zameldowania.
- **Zaległości podatkowe / ZUS**.
- **Fałszywe informacje / podrobione dokumenty** — karalne (art. 270, 273 KK).
- **Zagrożenie dla bezpieczeństwa państwa** — opinia ABW (art. 56 ust. 1 pkt 4 UC).
- **Małżeństwo fikcyjne** — weryfikacja przez wywiad urzędnika: wspólne pożycie, znajomość codziennych szczegółów partnera.

## Szablon wniosku o przedłużenie pobytu czasowego (skrót)

W praktyce wypełnia się w **MOS** (moduł elektroniczny); formularz papierowy tu nie jest pokazywany w całości, ale kluczowe elementy:

- Dane cudzoziemca (imię, nazwisko, data i miejsce urodzenia, obywatelstwo, nr paszportu, PESEL jeśli nadany).
- Dotychczasowe zezwolenie (nr karty pobytu, data ważności).
- Nowa podstawa wnioskowania (jeśli inna).
- Wymagane załączniki (zależne od podstawy).
- Dane pracodawcy / uczelni / rodziny.
- Oświadczenie o zgodności danych, art. 233 KK (odpowiedzialność karna za fałszywe zeznanie).

## Najczęstsze błędy i pułapki

- **Złożenie wniosku po upływie dotychczasowego pobytu** — stempel nie działa wstecznie; pobyt nielegalny.
- **Brak zmiany adresu w urzędzie** — korespondencja na stary adres → pominięcie terminów → decyzja po rozstrzygnięciu.
- **Ignorowanie wezwań urzędu** — w procedurze czynnego udziału (art. 10, 49–50 KPA) ignorowanie wezwania = ryzyko niekorzystnej decyzji.
- **Błędne fotografie** (standard biometryczny — 35x45 mm, tło jasne, bez okularów, bez nakrycia głowy) — zwrot wniosku lub prośba o uzupełnienie.
- **Niezarejestrowanie NIP dla JDG** podczas procedury o pobyt na podstawie działalności gospodarczej — wniosek odrzucony.
- **Umowy cywilnoprawne zamiast o pracę** dla pobytu „na pracę" — zasadniczo wymagana umowa o pracę lub szczególnie uzasadniona podstawa (np. B2B w zawodach IT, wysokich specjalizacji — dopuszczalne, ale wymaga argumentacji).
- **Brak oficjalnego tłumaczenia przysięgłego** dokumentów zagranicznych — wniosek niekompletny.
- **Fałszywe zaświadczenia o zatrudnieniu** — weryfikowane przez wojewodę poprzez kontakt z pracodawcą; wykrycie = art. 233 KK.

## Kiedy ten skill uzupełniany jest agentem / innym skillem

- Dla odwołania od decyzji wojewody lub Szefa UdSC, albo skargi do WSA — agent `appeal-drafter` (tryb KPA + PPSA).
- Dla pozwu pracowniczego cudzoziemca (np. mobbing, odprawa, ustalenie stosunku pracy) — agent `labor-drafter`.
- Dla rejestracji działalności gospodarczej cudzoziemca — odrębne kanały (CEIDG / KRS) — agent `contract-drafter` (umowa spółki) + skill `searching-krs`.
- Dla spraw rodzinnych (ustalenie ojcostwa, rozwód cudzoziemców w RP) — agent `family-drafter`; uwaga na rozp. Rzym III (prawo właściwe).
- Dla uchodźstwa / ochrony uzupełniającej (różne organy i procedury) — w tej wersji skill **nie obejmuje** spraw UdSC o ochronę; odrębna ścieżka.
