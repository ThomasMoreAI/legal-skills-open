---
name: reviewing-vehicle-contract
title: reviewing-vehicle-contract
description: Use when auditing Polish vehicle sale contract (umowa kupna-sprzedaży pojazdu) — VIN / przebieg, title chain, obciążenia (zastaw rejestrowy, leasing, przewłaszczenie), import / cło, obowiązkowe klauzule, PCC-3, typowe schematy oszustwa (cofnięty licznik, klonowany VIN, pełnomocnictwa-pułapki, parallel imports), rejestry (CEPiK, Mój Pojazd, Rejestr Zastawów, biała lista VAT, historiapojazdu.gov.pl)
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/plugins/pl/skills/reviewing-vehicle-contract
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: contracts
language: pl
---

# reviewing-vehicle-contract

Umowa kupna-sprzedaży pojazdu (UKS) to umowa sprzedaży wg art. 535 KC. Forma — dowolna (wystarczy pisemna). Problem nie w formie, a w ukrytych ryzykach: podrobiony VIN, ukryte obciążenia, odmiana stanu licznika, leasing niezakończony, pojazd z kradzieży. Ten skill — checklist audytu i lista rejestrów do weryfikacji przed podpisem.

## Obowiązkowa weryfikacja przed zakupem

| Rejestr | URL | Co sprawdzić | Koszt |
|---|---|---|---|
| **CEPiK** (Centralna Ewidencja Pojazdów i Kierowców) | `https://historiapojazdu.gov.pl` | Historia pojazdu: właściciele, data rejestracji, VIN, przebieg historyczny, badania techniczne, OC | Bezpłatne |
| **Mój Pojazd** (zarejestrowani) | `https://moj.gov.pl` (po logowaniu profilem zaufanym) | Rozszerzona historia, status aktualny | Bezpłatne |
| **Rejestr Zastawów Skarbowych** | `https://rz.ms.gov.pl` | Zastaw rejestrowy na pojeździe (art. 7 ustawy z 06.12.1996 o zastawie rejestrowym) | Bezpłatny podgląd; odpis z rejestru — płatny |
| **KRS / CEIDG** | `https://ekrs.ms.gov.pl`, `https://aplikacja.ceidg.gov.pl` | Sprzedawca-osoba prawna / przedsiębiorca — reprezentacja, upadłość | Bezpłatne |
| **Biała lista VAT** | `https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka/` | Sprzedawca-czynny podatnik VAT (B2B); rachunek do wpłaty | Bezpłatne |
| **Interpol / Stolen Motor Vehicles** | `https://www.interpol.int/How-we-work/Databases/Stolen-Motor-Vehicles` | Pojazd z bazy kradzieży (w UE oprócz Interpolu — dane krajowe) | Dostęp przez organy ścigania / handlarzy |
| **Historia ASO / serwisowa** | Od dealera / ASO marki | Rzeczywiste przebiegi, naprawy, wymiany | Zwykle bezpłatne dla właściciela |
| **Raport VIN** (platforma komercyjna) | `autoDNA`, `Carfax` (auta z USA), `CarVertical` | Kompleksowa historia z różnych źródeł | Płatne |
| **Euro NCAP / OEM recall** | `euroncap.com`, strona producenta | Akcje serwisowe (recall) otwarte na VIN | Bezpłatne |

**Minimum obowiązkowe**: historia pojazdu (historiapojazdu.gov.pl), rejestr zastawów, weryfikacja VIN (porównanie — nadwozie + szyba + komputer + dowód rejestracyjny + umowa).

## Red flags — najczęstsze zagrożenia

| Zagrożenie | Znak | Co zrobić |
|---|---|---|
| **Sfałszowany VIN / cloning** | VIN na tabliczce znamionowej różni się od pola bitego na nadwoziu; ślady manipulacji (szlifowanie, spawy); VIN nie zgadza się z dowodem rejestracyjnym | Odmówić zakupu. Zgłosić na Policję. |
| **Odmiana stanu licznika (cofnięty licznik)** | Rozbieżność historycznych odczytów w CEPiK; slady demontażu zestawu wskaźników; zużycie wnętrza / kierownicy / pedałów nieadekwatne do wskazań | Art. 306a § 1 KK — karalne (do 5 lat). Odstąpić; ewentualnie zgłosić. |
| **Pojazd z kradzieży** | Nietypowo niska cena; sprzedawca unika spotkania w miejscu rejestracji; brak historii ASO; VIN nie w systemie | Nie kupować; sprawdzić Interpol, CEPiK. |
| **Niezakończony leasing / zastaw rejestrowy** | Właściciel z dowodu = leasingodawca / bank; w rejestrze zastawów — wpis; brak karty pojazdu w oryginale | Wymagać oświadczenia o zwolnieniu lub bezpośredniej cesji z leasingodawcą; wpłata na rachunek leasingodawcy. |
| **Sprzedaż „na pełnomocnictwo"** | Sprzedawca twierdzi, że „właściciel jest za granicą"; notarialne pełnomocnictwo od „właściciela" (często fałszowane) | Wymagać kontaktu z właścicielem, weryfikacja pełnomocnictwa u notariusza (art. 99, 96 Prawa o notariacie). Zawsze ryzykowne — doraźne pełnomocnictwa często bywają odwołane lub fałszywe. |
| **Pojazd sprowadzony bez cła / bez akcyzy** | Brak dokumentów SAD / deklaracji akcyzy AKC-U; sprzedawca „obiecuje rejestrację" | Bez cła = nie zarejestrujesz (art. 72 Prawa o ruchu drogowym + ustawa o podatku akcyzowym). Odstąpić. |
| **Powypadkowy / odzyskany po szkodzie całkowitej** | Zróżnicowany lakier, nierówne spawy, rysy na ramie; brak w CEPiK wzmianki o „uszkodzony / szkoda całkowita", a w praktyce — był | Historia ubezpieczenia; Carfax (jeśli z USA); opinia niezależnego diagnosty. Klasyfikować jako KRYTYCZNE ryzyko, jeśli pojazd sprowadzony z zagranicy i brak dokumentacji. |
| **Sprzedawca-„słup" (komisy-krzak)** | Sprzedawca: JDG sprzed kilku tygodni, pod adresem wirtualnym, NIP nieaktywny, brak Biała lista VAT | CEIDG + VAT — jeżeli nieaktywny = ryzyko. Dla B2B > 15 000 zł — brak kosztów + odpowiedzialność solidarna (art. 22p ustawy o PIT). |
| **Tablice tymczasowe bez terminu** | Sprzedaż z tablicami tymczasowymi po przekroczonym 30-dniowym terminie | Zwykle pojazd nierejestrowalny pod nowe tablice bez dopełnień; sprawdzić. |
| **Ślady oleju, dymu, hałasów** | Standardowa diagnostyka handlarzy potrafi ukryć | Niezależny diagnosta — minimum za 200–400 zł; warto. |

## Obowiązkowe elementy umowy

Umowa sprzedaży pojazdu — elementy istotne wg art. 535 KC + wymogi praktyczne:

| Element | Uwagi |
|---|---|
| **Dane stron** | Imię, nazwisko, PESEL, adres; dla firm — pełna nazwa, KRS / NIP / REGON, reprezentacja. Kopia dowodu tożsamości po obu stronach — niezbędna przy wątpliwościach. |
| **Przedmiot sprzedaży** | Marka, model, wariant, rok produkcji, kolor, VIN, nr rejestracyjny, aktualny przebieg (z dokładną liczbą km), nr dowodu rejestracyjnego, nr karty pojazdu (gdy wydawano — do 03.11.2019 — lub „brak" przy nowszych), data pierwszej rejestracji, status prawny (np. „pojazd sprowadzony z Niemiec dnia ...", „zarejestrowany na terytorium RP od ..."). |
| **Cena** | Kwota w cyfrach i słownie. Waluta. **Forma płatności** (gotówka — z pokwitowaniem; przelew — na rachunek białej listy dla VAT > 15 000 zł). Data zapłaty. |
| **Termin wydania pojazdu** | Konkretna data; miejsce wydania. |
| **Oświadczenia sprzedawcy** | Że jest wyłącznym właścicielem; że pojazd wolny od wad prawnych (brak zastawów, kradzieży, uprzedzeń); że opisany stan techniczny i przebieg odpowiada rzeczywistemu; że pojazd nie brał udziału w wypadku (albo — szczerze — brał, z opisem naprawy). |
| **Rękojmia** | Uwaga: **wyłączenie rękojmi** jest skuteczne między osobami fizycznymi (B2C / C2C), ale **niedopuszczalne gdy sprzedawca-przedsiębiorca sprzedaje konsumentowi** (art. 558 § 1 KC + art. 43 ustawy o prawach konsumenta). W B2B — dopuszczalne. |
| **Załączniki** | Dowód rejestracyjny (oryginał); karta pojazdu (jeśli była wydana); instrukcja; klucze (liczba); protokół przekazania; CEPiK (wydruk); wydruk z rejestru zastawów; ew. pełnomocnictwa. |
| **Podpisy** | Dwóch egzemplarzy. Każda strona — własnoręcznie. |

## Klauzule opcjonalne (zabezpieczające klienta-kupującego)

- **Prawo odstąpienia w razie wad prawnych.** Gdy ujawni się obciążenie — zwrot + kara umowna (art. 555 + art. 558 KC).
- **Zadatek vs. zaliczka.** Jeżeli rezerwacja z wpłatą: **zadatek** (art. 394 KC) — zabezpieczenie dwustronne; **zaliczka** — tylko dla sprzedającego. Klient-kupujący — zadatek lepszy.
- **Oświadczenie o przebiegu.** „Sprzedawca oświadcza, że licznik nie był wymieniony, cofany, manipulowany" — naruszenie = art. 84 KC (uchylenie) + odpowiedzialność odszkodowawcza.
- **Oświadczenie o historii wypadkowej.** Gdy pojazd był w kolizji — opisać. Zatajenie = wada ukryta.
- **Opcja odbioru w serwisie.** Wydanie + weryfikacja techniczna w wybranym ASO; sprzedawca pokrywa ewentualne przedwstępne koszty.

## Obowiązki po zakupie

### Aktualne stawki — pobrać przed konsultacją

| Parametr | Źródło | Sposób pobrania | Fallback _(ostatnio zweryfikowany)_ |
|---|---|---|---|
| PCC od pojazdu | Ustawa o PCC art. 7 | WebFetch: `https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20001861150` — art. 7 | 2% _(stan na 2024)_ |
| Kara za brak OC | Obwieszczenie UFG | WebSearch: «kara za brak OC [bieżący rok] UFG» | od 420 zł _(stan na 2026)_ |
| Kara za nieterminową rejestrację | PoRD art. 140mb | WebFetch ISAP: PoRD | 200–1 000 zł _(stan na 2024)_ |

**Zasady:**
1. **Fetch udany** → użyj pobranej, podaj źródło i datę.
2. **Fetch nieudany** → użyj fallback. Ostrzeż: «⚠ Wartość pochodzi ze stanu na [data]. Sprawdź w ISAP / UFG.»

### Kupujący

| Obowiązek | Termin | Podstawa | Sankcja |
|---|---|---|---|
| **Zgłoszenie zbycia do CEPiK** | 30 dni od daty nabycia | Art. 78 ust. 2 pkt 1 PoRD | 200–1000 zł _(fallback; stan na 2024)_ (art. 140mb PoRD) |
| **Przerejestrowanie na siebie** | 30 dni | Art. 73 PoRD | 200–1000 zł _(fallback; stan na 2024)_ |
| **Zapłata PCC-3** (podatek od czynności cywilnoprawnych) | 14 dni od zawarcia umowy, deklaracja PCC-3 | Art. 3 ust. 1 pkt 1 i art. 10 ust. 1 ustawy z 09.09.2000 o PCC | 2% _(fallback; stan na 2024)_ od wartości rynkowej; kara za niezgłoszenie |
| **Zmiana ubezpieczenia OC** | Najpóźniej w dniu rejestracji | Ustawa z 22.05.2003 o ubezpieczeniach obowiązkowych | Kara za brak OC (od 420 zł _(fallback; stan na 2026)_ — dla samochodów osobowych) |
| **Zgłoszenie w miejscu zamieszkania (CEPiK)** | W momencie przerejestrowania | Ustawa o kierujących pojazdami | — |

**Wyjątki od PCC-3** — nabycie od czynnego podatnika VAT (opodatkowane VAT, a nie PCC) — sprawdzić białą listę i upewnić się, że faktura VAT, nie umowa kupna-sprzedaży.

### Sprzedawca

| Obowiązek | Termin | Podstawa |
|---|---|---|
| **Zgłoszenie zbycia do CEPiK** | 30 dni | Art. 78 ust. 2 pkt 1 PoRD |
| **Wydanie dowodu rejestracyjnego + karty** | Przy wydaniu pojazdu | Umowna + art. 71 PoRD (wymóg przy rejestracji) |
| **Wypowiedzenie OC** | Do 30 dni od sprzedaży (lub do końca okresu OC — ubezpieczenie przechodzi z mocy prawa na kupującego do końca okresu; ustawa o ubezpieczeniach obowiązkowych art. 31) | — |

## Szczególne przypadki

### Sprzedaż sprowadzonego pojazdu (import spoza UE)

Dodatkowo wymagać:
- **SAD** (Single Administrative Document — odprawa celna).
- **Deklaracja akcyzowa AKC-U** (akcyza od samochodu osobowego).
- **Faktura zakupu z kraju pochodzenia**.
- **Tłumaczenie przysięgłe dokumentów** (do rejestracji).
- **Badanie techniczne przed pierwszą rejestracją w Polsce**.

**Bez kompletu — niemożliwa rejestracja.** Jeżeli sprzedawca obiecuje „dostarczyć później" — odmówić zakupu albo zatrzymać 80% ceny jako zabezpieczenie.

### Sprzedaż pojazdu z leasingu (wykupiony)

- Protokół zakończenia leasingu + faktura wykupu leasingu na rzecz dotychczasowego korzystającego.
- Dopiero po tej transakcji pojazd staje się jego własnością i może być sprzedany dalej.

### Sprzedaż pojazdu ze szkodą całkowitą (odzyskany)

- Decyzja ubezpieczyciela o szkodzie całkowitej.
- Badanie techniczne po naprawie.
- Warto opisać w umowie: „Pojazd po szkodzie całkowitej (decyzja ... z dnia ...)" — inaczej wada ukryta.

### Sprzedaż między małżonkami / członkami rodziny

- PCC-3 — zwolnienia dla osób z I grupy podatkowej do kwoty wolnej (art. 9 ust. 1 pkt 1 ustawy o PCC); ważne sprawdzić aktualne limity.
- Ewentualnie: darowizna zamiast sprzedaży — podatek od spadków i darowizn (ustawa z 28.07.1983), korzystne progi w I grupie.

## Skład audytu — szablon

```
AUDYT UMOWY KUPNA-SPRZEDAŻY POJAZDU
Klient: [Kupujący / Sprzedawca]
Pojazd: [marka, model, VIN]
Data projektu: [___]
Data audytu: [___]

I. WERYFIKACJA REJESTROWA (przeprowadzona)
   - historiapojazdu.gov.pl — status: [OK / uwagi]
   - Rejestr Zastawów — status: [OK / wpis: ...]
   - Biała lista VAT — status: [nie dotyczy / OK / nieaktywny]
   - CEIDG / KRS sprzedawcy — status: [OK / uwagi]
   - Inne: [Carfax / autoDNA / ...]

II. WERYFIKACJA POJAZDU
   - VIN — zgodny na wszystkich elementach: [TAK/NIE, opis]
   - Przebieg — spójny z historią: [TAK/NIE]
   - Stan techniczny — opinia diagnosty: [TAK/NIE/nie wykonano]
   - Dokumenty: [dowód rej., karta poj., SAD, AKC-U, inne]

III. ZNALEZISKA NA PROJEKCIE UMOWY
   [lista ustaleń wg klasyfikacji: KRYTYCZNE / ISTOTNE / POŻĄDANE]

IV. ZALECENIE
   [podpisywać / nie podpisywać / warunkowo — pod warunkiem poprawek]
```

## Kiedy ten skill uzupełniany jest agentem / innym skillem

- Dla pełnego projektowania umowy sprzedaży pojazdu — agent `pl:contract-drafter` (sporządzanie).
- Dla weryfikacji sprzedawcy-przedsiębiorcy (reprezentacja, upadłość, VAT) — skill `pl:searching-krs`.
- Dla obliczenia PCC-3 lub postępowania sporu przed organem skarbowym — rozważyć konsultacje podatkowe (poza zakresem tego skillu).
- Dla spór sądowy o wady pojazdu — agent `pl:claim-drafter` (pozew), ewentualnie `pl:consumer-drafter` dla B2C.
