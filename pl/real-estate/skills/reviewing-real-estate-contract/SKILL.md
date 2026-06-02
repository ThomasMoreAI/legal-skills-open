---
name: reviewing-real-estate-contract
title: reviewing-real-estate-contract
description: Use when auditing Polish real-estate contract (umowa przedwstępna / sprzedaży nieruchomości) — KW (działy I–IV), obciążenia (hipoteka, służebności, dożywocie), prawo pierwokupu (KOWR, gmina, spółdzielnia, SP), forma aktu notarialnego pod rygorem nieważności (art. 158 KC), zadatek vs zaliczka (art. 394 KC), PCC-3 2% (fallback) vs VAT 8%/23% (fallback), rejestry (ekw.ms.gov.pl, EGiB, MPZP, zabytki)
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/plugins/pl/skills/reviewing-real-estate-contract
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: real-estate
language: pl
---

# reviewing-real-estate-contract

Umowa sprzedaży nieruchomości — **forma aktu notarialnego pod rygorem nieważności** (art. 158 KC). Projekt aktu prowadzi notariusz; rola prawnika — wczytać projekt, wskazać ryzyka klientowi przed podpisem, często równolegle sporządzić **umowę przedwstępną** (art. 389 KC) zabezpieczającą pozycję klienta na czas finansowania (kredyt, BGK, środki własne). Ten skill — checklist audytu i lista rejestrów do weryfikacji przed podpisaniem.

## Obowiązkowa weryfikacja przed zakupem

| Rejestr / dokument | URL | Co sprawdzić | Koszt |
|---|---|---|---|
| **Księga wieczysta** (KW) | `https://ekw.ms.gov.pl` (EKW — Elektroniczne Księgi Wieczyste) | Dział II (właściciel), Dział III (ograniczenia / ostrzeżenia / służebności), Dział IV (hipoteki), Dział I-Sp (spis praw związanych), Dział I-O (oznaczenie nieruchomości) | Bezpłatne podglądanie; odpis zupełny — 30–60 zł (przez notariusza lub EKW po zalogowaniu) |
| **Ewidencja Gruntów i Budynków** (EGiB) | Starostwo powiatowe / e-starostwo; `geoportal.gov.pl` | Dane katastralne — powierzchnia, klasa użytku, oznaczenie geodezyjne | Bezpłatne (geoportal); wypis — 50–150 zł |
| **MPZP** (Miejscowy Plan Zagospodarowania Przestrzennego) | Urząd gminy / miasta; portal mapowy gminy | Przeznaczenie działki (MN, MW, U, P itd.), wskaźniki zabudowy, możliwa zabudowa | Bezpłatne wypisy (do 100 zł od wypisu + rysunku) |
| **Studium uwarunkowań i kierunków zagospodarowania** | Gmina | Jeżeli brak MPZP — studium wskazuje kierunek | Bezpłatne |
| **Decyzja o warunkach zabudowy** (WZ) | Dla nieruchomości niezabudowanej w obszarze bez MPZP | Aktualna WZ? Dla kogo wydana? Ważność? | Bezpłatne |
| **Pozwolenie na budowę / użytkowanie** | Starostwo / Powiatowy Inspektor Nadzoru Budowlanego (PINB) | Dla zabudowanej — legalność; samowole | Bezpłatne na miejscu |
| **Rejestr zabytków** | `nid.pl` (NID), wojewódzki konserwator | Wpis obiektu — ograniczenia prac budowlanych, prawo pierwokupu woj. konserwatora | Bezpłatne |
| **Rejestr Natura 2000 / obszary chronione** | `geoserwis.gdos.gov.pl` | Ograniczenia środowiskowe | Bezpłatne |
| **KOWR** (Krajowy Ośrodek Wsparcia Rolnictwa) | Dla nieruchomości rolnych > 1 ha — weryfikacja wymogów ustawy z 11.04.2003 o kształtowaniu ustroju rolnego | Prawo pierwokupu KOWR + ograniczenia nabywcy | Przez KOWR (właściwe biuro terenowe) |
| **Zaświadczenie o braku zaległości w opłatach** | Spółdzielnia / wspólnota / gmina (czynsz, podatek od nieruchomości, opłata za użytk. wieczyste) | Zadłużenie obciąża nieruchomość w trybie egzekucji | Bezpłatne — za zaświadczeniem wnioskować |
| **PINB / PSSE — nakazy / zalecenia** | Powiatowy Inspektor Nadzoru Budowlanego | Otwarte decyzje o rozbiórce, nakazy poprawy | Bezpłatne, przez wniosek |

**Minimum obowiązkowe**: KW (odpis zupełny na dzień aktu), EGiB (wypis), MPZP (wypis z zaświadczeniem o zgodności z planem).

## Red flags — najczęstsze zagrożenia

| Zagrożenie | Znak | Co zrobić |
|---|---|---|
| **Hipoteki w Dziale IV** | Wpis hipoteki bankowej / umownej / przymusowej; nie wykreślona | Warunkowo: wpłata ceny na rachunek banku hipotecznego (wykreślenie hipoteki po spłacie). Lista zobowiązań banku z BGK — aktualna. |
| **Roszczenia ujawnione w Dziale III** | Ostrzeżenie o niezgodności; prawo pierwokupu; służebności (drogi konieczne, przesyłu, osobiste); dożywocie | Każde roszczenie = poważne. Ostrzeżenie o niezgodności — potencjalne spór własnościowy. Dożywocie / służebność osobista — może uniemożliwić korzystanie. |
| **Prawo pierwokupu gminy** | Dział III; ustawa o gospodarce nieruchomościami art. 109 i nast. (gmina może mieć pierwokup do działek miejskich) | Notariusz musi powiadomić gminę; 1 miesiąc na wykonanie; dopiero potem akt ostateczny. |
| **Prawo pierwokupu KOWR** | Rola / grunty rolne > 0,3 ha w zakresie umów o nabycie przez osoby niebędące rolnikami | Ustawa z 11.04.2003 o kształtowaniu ustroju rolnego: pozwolenie KOWR obowiązkowe; ograniczenia nabywcy. |
| **Prawo pierwokupu spółdzielni mieszkaniowej** | Dla lokali spółdzielczych — art. 18 ustawy z 15.12.2000 o spółdzielniach mieszkaniowych | Notariusz informuje spółdzielnię; 3 miesiące na wykonanie. |
| **Samowola budowlana** | Budynek nie zgadza się z księgą; brak dokumentacji budowlanej; brak pozwolenia na użytkowanie | Kosztowna legalizacja (lub nakaz rozbiórki — art. 48 Prawa budowlanego). Wymagać legalizacji przed aktem lub obniżki ceny. |
| **Ziemia rolna z nabywcą niepewnym** | Nabywca nie jest rolnikiem indywidualnym, nie ma pozwolenia KOWR | Umowa nieważna; KOWR może żądać stwierdzenia nieważności. |
| **Nieruchomość ze spadku, niewyjasniona** | Brak stwierdzenia nabycia spadku / notarialnego poświadczenia; jedno z imion w KW ma adnotację „sp." (spadkobiercy) | Wymagać stwierdzenia nabycia spadku i wpisu wszystkich spadkobierców przed aktem. |
| **Podwójna sprzedaż / podwójne akty** | Ostrzeżenie o niezgodności; postanowienie sądu wieczystoksięgowego | Nie podpisywać. Spór możliwy w sądzie; pierwszeństwo wg daty ujawnienia (art. 5 ustawy o KW i hipotece). |
| **Długi lokatorów / najemców** | Wspólnota zgłasza zaległości | Zaległości czynszowe — obciążenie; weryfikacja zaświadczenia. |
| **Służebność drogi koniecznej** | Dział III — obcy ma prawo przechodu | Zwykle do rozliczenia; nie możliwe do usunięcia jednostronnie. |
| **Dożywocie (art. 908 KC)** | Dział III — zbywca / osoba trzecia ma prawo dożywotniego utrzymania | **Zwykle nie da się usunąć** bez zgody uprawnionego; nieruchomość obciążona na lata. Większy upust ceny lub odstąpić. |
| **Teren zalewowy / Natura 2000** | Brak MPZP lub MPZP ogranicza zabudowę; inspektorat ochrony środowiska | Ograniczenie inwestycji; opis w studium. |

## Forma aktu notarialnego (art. 158 KC)

**Rygor**: bez aktu notarialnego — **czynność nieważna** (art. 73 § 2 KC).

**Rola notariusza**:
- Weryfikacja tożsamości stron (paszporty / dowody).
- Weryfikacja umocowania (dla spółek — KRS, pełnomocnictwa — sprawdzane notariusz-do-notariusza).
- Odpis zupełny KW na dzień aktu.
- Zaświadczenia o braku zaległości, zgodności z MPZP.
- Złożenie wniosku o wpis do KW (art. 92 § 4 PrNot) — z dokumentem uiszczenia opłaty.

**Taksa notarialna**: art. 4-5 rozp. Min. Spraw. z 28.06.2004; zwykle między 0,25% a 1% _(fallback; stan na 2024)_ wartości transakcji (dla wyższych nieruchomości — degresywnie).

## Obowiązkowe elementy aktu notarialnego

| Element | Uwagi |
|---|---|
| **Dane stron** | Imię, nazwisko, PESEL, stan cywilny (dla osób fizycznych — istotne przy wspólności ustawowej małżeńskiej!), dowód tożsamości, adres; dla spółek — KRS, NIP, reprezentacja |
| **Stan cywilny / rozdzielność majątkowa** | Małżeństwo = wspólność ustawowa (art. 31 KRO) — **obie strony potrzebują zgody**; chyba że rozdzielność majątkowa (art. 47 KRO — przez akt notarialny) |
| **Przedmiot sprzedaży** | Dokładny opis: księga wieczysta (KW), nr działki, obręb, powierzchnia, oznaczenie z EGiB, adres, stan zabudowy (odniesienie do pozwolenia / zaświadczenia); udział we wspólnej nieruchomości (dla mieszkań w budynkach wielolokalowych) |
| **Cena** | Kwota w cyfrach i słownie. Waluta. Forma płatności. |
| **Warunki płatności** | Zaliczka / zadatek przy podpisaniu; spłata hipoteki z ceny (z zobowiązaniem banku); termin zapłaty reszty; sposób (przelew bankowy, często depozyt notarialny dla bezpieczeństwa obu stron — art. 108 PrNot) |
| **Oświadczenia sprzedawcy** | Że jest wyłącznym właścicielem; brak ograniczeń; brak zaległości w opłatach; zgodność z MPZP; brak samowoli |
| **Termin wydania** | Zwykle: po wpłacie pełnej ceny; protokół zdawczo-odbiorczy z opisem stanu |
| **Koszty aktu** | Kto ponosi: taksę notarialną, PCC-3, opłaty sądowe (wpis do KW) — standardowo kupujący |
| **Wnioski do KW** | O wpis prawa własności na kupującego; o wykreślenie wygasłych praw (hipoteki po spłacie, ograniczeń) |
| **Oświadczenia do celów podatkowych** | PCC-3 lub VAT; zwolnienia; grupa podatkowa przy darowiźnie |

## Umowa przedwstępna (art. 389 KC)

Etap często stosowany przy kupnie mieszkania na kredyt:

- **Forma** — może być w formie zwykłej pisemnej **lub** w formie aktu notarialnego (bardziej zabezpieczona — art. 390 § 2 KC: roszczenie o zawarcie umowy przyrzeczonej w trybie pozwu o złożenie oświadczenia woli + wpis ostrzeżenia do KW).
- **Elementy**: przedmiot, cena, termin zawarcia umowy przyrzeczonej, zadatek / zaliczka, warunki (np. uzyskanie kredytu przez kupującego), kary umowne.
- **Zadatek (art. 394 KC)** — dwustronne zabezpieczenie: sprzedawca odstąpi → zwrot w podwójnej wysokości; kupujący odstąpi → traci zadatek.
- **Zaliczka** — tylko dla sprzedającego; kupujący w razie swojej rezygnacji ją odzyskuje, ale nie ma zabezpieczenia po stronie sprzedającego.

**Dla klienta-kupującego**: umowa przedwstępna w formie aktu notarialnego + zadatek + klauzula „pod warunkiem uzyskania kredytu".

## Zadatek vs zaliczka — krytyczne rozróżnienie

| Cecha | Zadatek (art. 394 KC) | Zaliczka |
|---|---|---|
| Kto odstępuje → | Sprzedający → zwraca w podwójnej wysokości | Sprzedający → zwraca w pojedynczej wysokości |
| | Kupujący → traci zadatek | Kupujący → otrzymuje zwrot |
| Prawna natura | Wzmocniony środek zabezpieczenia | Wyłącznie prepayment |
| Uregulowanie | Ustawowe, domniemanie przy kwalifikacji | Umowne, brak domyślnej regulacji |
| Kiedy wybrać | Kupujący — gdy chce mocnego zabezpieczenia | Sprzedający — gdy chce elastyczności |

**Zasada domyślna**: bez dookreślenia „zadatek" / „zaliczka" — sąd może interpretować jako zadatek (art. 394 § 1 KC wskazuje na domniemanie zadatku, ale najnowsza linia orzecznicza SN w tym zakresie jest różna — sprawdzić).

## Podatki

### Aktualne stawki — pobrać przed konsultacją

| Parametr | Źródło | Sposób pobrania | Fallback _(ostatnio zweryfikowany)_ |
|---|---|---|---|
| PCC od nieruchomości | Ustawa o PCC art. 7 | WebFetch: `https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20001861150` — art. 7 | 2% _(stan na 2024)_ |
| VAT na nieruchomości | Ustawa o VAT art. 41 | WebFetch: `https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20040540535` — art. 41 | 8% / 23% _(stan na 2024)_ |

**Zasady:**
1. **Fetch udany** → użyj pobranej, podaj źródło i datę.
2. **Fetch nieudany** → użyj fallback. Ostrzeż: «⚠ Stawka pochodzi ze stanu na [data]. Sprawdź w ISAP.»

### PCC-3 (Podatek od Czynności Cywilnoprawnych)

- **Podstawa**: ustawa z 09.09.2000 o PCC.
- **Stawka**: **2%** _(fallback; stan na 2024)_ od wartości rynkowej (art. 7 ust. 1 pkt 1 ustawy o PCC).
- **Zobowiązany**: kupujący.
- **Termin**: 14 dni od dnia zawarcia umowy; deklaracja PCC-3.
- **Notariusz** jako płatnik — pobiera PCC i odprowadza do US.

**Wyłączenia**: transakcje objęte VAT; zwolnienia szczególne (art. 2 i 9 ustawy o PCC).

### VAT (alternatywa do PCC-3)

- Gdy sprzedawca — czynny podatnik VAT, a transakcja podlega VAT (np. sprzedaż pierwsza, nowe mieszkanie od dewelopera) — VAT **8%** / **23%** _(fallback; stan na 2024)_ (mieszkania do 150 m² — 8%; pozostałe — 23%).
- Gdy zwolnienie z VAT (art. 43 ust. 1 pkt 10 ustawy o VAT) — wtedy PCC obowiązuje.
- Sprawdzić **białą listę VAT**, rachunek sprzedawcy.

### Podatek od spadków i darowizn

Dla darowizny — ustawa z 28.07.1983; progi, grupy podatkowe, zwolnienia dla I grupy.

### Koszty bieżące po zakupie

- **Podatek od nieruchomości** (ustawa z 12.01.1991) — zgłoszenie w urzędzie gminy w 14 dni.
- **Opłata za użytkowanie wieczyste** (jeśli grunt SP / gminny) — rocznie.
- **Opłaty wspólnoty / spółdzielni** — jeśli mieszkanie w budynku wielolokalowym.

## Klauzule opcjonalne (zabezpieczające kupującego)

- **Klauzula kredytowa** — „pod warunkiem uzyskania kredytu hipotecznego do dnia ...". Bez niej — ryzyko utraty zadatku.
- **Depozyt notarialny** (art. 108 PrNot) — cena wpłacana na konto depozytowe notariusza, zwalniana sprzedawcy po wpisie do KW + wykreśleniu obciążeń.
- **Obowiązek wydania w stanie wolnym** — od najemców, lokatorów, rzeczy; protokół zdawczo-odbiorczy.
- **Klauzula o wadach** — prawo odstąpienia w ciągu 12 miesięcy w razie wad istotnych (art. 556, 560, 562 KC).
- **Odpowiedzialność za ukryte obciążenia** — zwrot + odszkodowanie, jeżeli ujawni się obciążenie nieopisane w akcie.

## Umowa przedwstępna — tekst podstawowy (szkic)

```
UMOWA PRZEDWSTĘPNA SPRZEDAŻY NIERUCHOMOŚCI
zawarta dnia ___ w ___ pomiędzy:
[Sprzedawca, dane]
a
[Kupujący, dane]

§ 1. PRZEDMIOT
   Sprzedawca zobowiązuje się sprzedać, a Kupujący — kupić nieruchomość:
   [dokładny opis z nr KW, działki, obrębu, powierzchnią]

§ 2. CENA
   Cena sprzedaży: ___ zł (słownie: ...).

§ 3. ZADATEK
   Przy podpisaniu niniejszej umowy Kupujący wpłaca Sprzedawcy zadatek w kwocie
   ___ zł. Zadatek podlega zasadom art. 394 KC.

§ 4. TERMIN UMOWY PRZYRZECZONEJ
   Umowa przyrzeczona zostanie zawarta w formie aktu notarialnego nie później
   niż do dnia ___ w kancelarii notarialnej wybranej przez Kupującego.

§ 5. WARUNEK
   Umowa przyrzeczona zostanie zawarta pod warunkiem uzyskania przez Kupującego
   kredytu hipotecznego w kwocie ___ zł nie później niż do dnia ___.
   Brak kredytu uprawnia Kupującego do odstąpienia bez skutków zadatku (zwrot
   w pojedynczej wysokości).

§ 6. KOSZTY
   [taksa notarialna, PCC, opłaty sądowe — podział]

§ 7. POSTANOWIENIA KOŃCOWE
   Forma pisemna pod rygorem nieważności zmian.
   Sąd właściwy: [sąd, w okręgu którego znajduje się nieruchomość].

[Podpisy stron]
```

## Szczególne sytuacje

### Rolnik indywidualny a nabycie gruntów rolnych

- Art. 2a ustawy o kształtowaniu ustroju rolnego — nabywca powinien być rolnikiem indywidualnym (kwalifikacje rolnicze 5 lat, zamieszkanie w gminie itd.); wyjątki (dziedziczenie, bliscy, KOWR).
- Niebędący rolnikiem — zgoda KOWR indywidualnie.
- Sankcja: nieważność bezwzględna nabycia.

### Nieruchomość w obszarze „przygranicznym" / pas ochronny

- Ograniczenia dla cudzoziemców — ustawa z 24.03.1920 o nabywaniu nieruchomości przez cudzoziemców: zgoda MSWiA, wyjątki dla obywateli EOG.

### Zabytek

- Prawo pierwokupu konserwatora (art. 10 ustawy z 23.07.2003 o ochronie zabytków).
- Ograniczenia w pracach — obowiązkowe pozwolenie konserwatorskie.

### Nieruchomość kościelna / Skarbu Państwa

- Specjalne procedury; zwykle przetarg publiczny.

## Szablon raportu audytu

```
AUDYT UMOWY SPRZEDAŻY NIERUCHOMOŚCI
Klient: [kupujący / sprzedawca]
Nieruchomość: [nr KW, adres, powierzchnia]
Forma: [umowa przedwstępna / akt notarialny — projekt]
Data projektu: [___]
Data audytu: [___]

I. WERYFIKACJA REJESTROWA
   - KW [nr] — odpis zupełny na dzień [___]:
     · Dział II (właściciel): [OK / zmiana oczekiwana]
     · Dział III (ograniczenia): [OK / wpisy: ...]
     · Dział IV (hipoteki): [OK / hipoteka na kwotę ...]
   - EGiB: [OK / niezgodność ...]
   - MPZP: [zgodny / WZ wydana / brak dokumentów]
   - PINB: [brak nakazów / są]
   - Zaświadczenia (wspólnota, gmina, ZUS, US): [stan]

II. BADANIE PRAWNE
   - Tytuł własności: [nabycie: umowa sprzedaży/darowizny/spadek]
   - Współwłasność: [są spadkobiercy? małżeńska wspólność?]
   - Stan cywilny sprzedawcy: [kawaler / małżeństwo — wspólność / rozdzielność]
   - Prawo pierwokupu: [nie / gmina / KOWR / spółdzielnia / konserwator]

III. ZNALEZISKA NA PROJEKCIE AKTU
   [lista ustaleń wg klasyfikacji: KRYTYCZNE / ISTOTNE / POŻĄDANE]

IV. PODATKI
   - PCC-3 / VAT — który reżim?
   - Zwolnienia?
   - Obliczenie: [kwota]

V. ZALECENIE
   [podpisywać / nie podpisywać / warunkowo — pod warunkiem poprawek]

VI. DALSZE DZIAŁANIA
   [co zrobić przed aktem, co przy akcie, co po akcie]
```

## Kiedy ten skill uzupełniany jest agentem / innym skillem

- Dla sporządzenia umowy przedwstępnej — agent `pl:contract-drafter` (sporządzanie).
- Dla weryfikacji sprzedawcy-spółki — skill `pl:searching-krs`.
- Dla sporu wokół nieważności umowy lub wad fizycznych / prawnych — agent `pl:claim-drafter`.
- Dla spraw spadkowych (dział spadku przed sprzedażą) — agent `pl:inheritance-drafter`.
- Dla spraw rodzinnych (rozdzielność majątkowa, podział majątku) — agent `pl:family-drafter`.
