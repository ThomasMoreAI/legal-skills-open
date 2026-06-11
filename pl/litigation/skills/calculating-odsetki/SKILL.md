---
name: calculating-odsetki
title: calculating-odsetki
description: Use when calculating Polish odsetki — ustawowe (art. 359 KC), za opóźnienie (art. 481 KC), w transakcjach handlowych (ustawa z 08.03.2013), maksymalne (art. 359 § 2¹). Stawka na dany okres, rekompensata 40/70/100 euro w B2B
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/plugins/pl/skills/calculating-odsetki
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: litigation
language: pl
---

# calculating-odsetki

Polski system ma **trzy reżimy** odsetek cywilnoprawnych, każdy z własnym algorytmem stawki i zakresem stosowania. Mylenie ich jest najczęstszym błędem w pozwach. Ten skill mapuje reżimy, pokazuje jak dobrać stawkę na datę i jak liczyć kwotę.

## Trzy reżimy odsetek

### 1. Odsetki ustawowe (art. 359 § 2 KC) — „cywilne"

**Zakres:** od wszelkich sum pieniężnych, jeżeli ich wysokość **nie jest określona umową** ani innym szczególnym przepisem. Dotyczy głównie spraw **cywilnoprawnych** (nie handlowych B2B).

**Stawka (art. 359 § 2 KC):** stopa referencyjna NBP + **3,5 punktu procentowego**.

Ogłoszenie Ministra Sprawiedliwości — uodo.gov.pl / gov.pl.

### 2. Odsetki ustawowe za opóźnienie (art. 481 § 2 KC) — „od opóźnienia w spełnieniu świadczenia pieniężnego"

**Zakres:** gdy dłużnik opóźnia się ze spełnieniem świadczenia pieniężnego. Dotyczy **wszystkich** świadczeń pieniężnych (cywilnych i niektórych handlowych, jeżeli nie wchodzi w grę reżim nr 3).

**Stawka (art. 481 § 2 KC):** stopa referencyjna NBP + **5,5 punktu procentowego**.

**Maksymalne odsetki za opóźnienie** (art. 481 § 2¹ KC) = **2 × odsetki ustawowe za opóźnienie**.

### 3. Odsetki w transakcjach handlowych (ustawa z 08.03.2013 o przeciwdziałaniu nadmiernym opóźnieniom w transakcjach handlowych, Dz.U. 2023 poz. 1790)

**Zakres:** transakcje handlowe między przedsiębiorcami (B2B) oraz z udziałem podmiotów publicznych. Dotyczy roszczeń o zapłatę wynagrodzenia z tytułu **dostawy towaru lub świadczenia usługi** w ramach działalności gospodarczej.

**Stawka (art. 4a ustawy):** stopa referencyjna NBP + **8 punktów procentowych** (dla standardowych transakcji); dla dużych przedsiębiorstw wobec MŚP dolne progi bardziej wyrównane.

**Rekompensata za koszty odzyskiwania należności (art. 10 ustawy):**
- **40 euro** — gdy należność < 5 000 zł _(fallback; art. 10 ustawy 2013)_;
- **70 euro** — gdy 5 000 zł ≤ należność < 50 000 zł _(fallback)_;
- **100 euro** — gdy należność ≥ 50 000 zł _(fallback)_.

Przeliczenie na złote — wg kursu średniego NBP z ostatniego dnia roboczego miesiąca poprzedzającego miesiąc wymagalności.

**Termin zapłaty:**
- B2B — co do zasady 60 dni; umowne ograniczenie możliwe, ale maksymalnie 30 dni dla dużego przedsiębiorstwa wobec MŚP jest bezskuteczne bez uzasadnienia (art. 7 ustawy).
- Z podmiotem publicznym — 30 dni (art. 8); wyjątek 60 dni dla niektórych sektorów.

## Aktualne parametry — pobrać przed obliczeniem

| Parametr | Źródło | Sposób pobrania | Fallback _(ostatnio zweryfikowany)_ |
|---|---|---|---|
| Stopa referencyjna NBP | RPP / NBP | WebFetch: `https://www.nbp.pl/home.aspx?f=/dzienne/stopy.htm` | 5,75% _(stan na 2024-10-03)_ |
| Kurs EUR/PLN (dla rekompensaty) | NBP | WebFetch: `https://www.nbp.pl/home.aspx?f=/kursy/kursya.html` | Weryfikować na datę wymagalności |

**Zasady:**
1. **Fetch udany** → użyj pobranej wartości, podaj źródło i datę pobrania.
2. **Fetch nieudany** → użyj fallback. Ostrzeż użytkownika: «⚠ Stopa referencyjna NBP = [fallback] pochodzi ze stanu na [data]. Sprawdź aktualną na nbp.pl.»

Stopa referencyjna NBP (kluczowa stawka polityki pieniężnej) ustalana przez RPP. Historyczne stawki — NBP publikuje na nbp.pl (archiwum uchwał). Dla każdego okresu spornego — ustalić stopę obowiązującą na dany podokres.

## Tabela stawek (fallback — weryfikować aktualne przez fetch-blok wyżej)

| Reżim | Wzór | Przykładowa stawka przy referencyjnej 5,75% |
|---|---|---|
| Odsetki ustawowe (art. 359 KC) | ref + 3,5 pp | 9,25% rocznie |
| Odsetki za opóźnienie (art. 481 KC) | ref + 5,5 pp | 11,25% rocznie |
| Maksymalne za opóźnienie (art. 481 § 2¹ KC) | 2 × za opóźnienie | 22,50% rocznie |
| Transakcje handlowe (ustawa 2013) | ref + 8 pp | 13,75% rocznie |
| Odsetki maksymalne (art. 359 § 2¹ KC) | 2 × ustawowe | 18,50% rocznie |

**Uwaga:** stawki się **zmieniają** wraz z uchwałami RPP. Dla obliczenia odsetek za okres — dzielić okres na podokresy wg obowiązującej wówczas stopy.

## Wzór obliczeniowy

`Odsetki = Kwota × Stopa roczna × Dni / 365`

Dla okresu z różnymi stawkami — sumować per podokres.

**Uwaga dla lat przestępnych (366 dni)** — orzecznictwo SN (wyrok z 16.02.2016 r., V CSK 292/15) akceptuje obie metody, ale **konwencja praktyczna — 365 dni** (tak też w wyroku SA w Warszawie z 15.03.2017 r., I ACa 2208/15).

## Odsetki kapitałowe (art. 359 § 1 KC) — umowne

Jeżeli strony w umowie określiły stopę — obowiązuje umowna, z **ograniczeniem maksymalnym** (art. 359 § 2¹ KC):

`Odsetki maksymalne kapitałowe = 2 × odsetki ustawowe (art. 359 § 2 KC)`

Strony mogą umówić się na mniej, ale nie więcej. Powyżej — nieważność co do nadwyżki (art. 359 § 2² KC); stosuje się stawkę maksymalną.

## Odsetki za opóźnienie — kiedy biegną

**Ogólnie:** od dnia wymagalności (art. 481 § 1 KC).

- **Umowa terminowa** — od dnia upływu terminu.
- **Umowa bezterminowa** — art. 455 KC: od dnia wezwania do zapłaty (+ rozsądny termin na zapłatę — jeżeli wezwanie nie wskazuje, sąd ustala).
- **Odszkodowanie z tytułu czynu niedozwolonego** — od wezwania (art. 455 KC); w niektórych przypadkach orzecznictwo SN — od dnia zdarzenia (szczególnie przy karach umownych).
- **Zwrot nienależnego świadczenia** (art. 410 KC) — od wezwania.
- **Zachowek** — od dnia wezwania.
- **Zasądzenie** — zwykle od dnia wniesienia pozwu, jeżeli wcześniej nie było wezwania.

## Zbieg reżimów — zasady

1. **Transakcja handlowa** (B2B + dostawa / usługa za wynagrodzenie) → **ustawa 2013** (art. 4a). **Nie stosuje się** 481 KC (ustawa 2013 jest lex specialis).
2. **B2B poza transakcją handlową** (np. kara umowna, odszkodowanie) → **art. 481 KC**.
3. **C2C lub B2C dla zobowiązań bezumownych** → **art. 481 KC**.
4. **Umowa określa stawkę** (w granicach maksymalnych) → **umowa**.
5. **Odsetki kapitałowe** (od pożyczki, kredytu) → **art. 359 KC** w granicach maksymalnych.

## Przykłady

### Przykład 1 — niepłacona faktura B2B (transakcja handlowa)

- Faktura: 10 000 zł, termin 30 dni.
- Data wystawienia: 01.03.2025.
- Termin zapłaty: 31.03.2025.
- Zapłata: 15.07.2025 (opóźnienie 106 dni).
- Stawka (hipotetyczna — weryfikować): ref 5,75% + 8 pp = 13,75%.
- Odsetki = 10 000 × 13,75% × 106 / 365 = **399,32 zł**.
- Rekompensata: 70 euro (bo 5 000 ≤ 10 000 < 50 000); kurs NBP na 28.02.2025 — przykładowo 4,20 zł/EUR → **294 zł**.
- **Łącznie: 399,32 + 294 = 693,32 zł** (plus kwota główna 10 000 zł).

### Przykład 2 — opóźnienie w zwrocie pożyczki C2C

- Pożyczka 5 000 zł, termin zwrotu 01.06.2025. Zwrot 01.12.2025 (183 dni opóźnienia).
- Stawka art. 481 § 2 KC: ref 5,75% + 5,5 pp = 11,25%.
- Odsetki = 5 000 × 11,25% × 183 / 365 = **281,85 zł**.

### Przykład 3 — zachowek

- Kwota: 100 000 zł.
- Wezwanie do zapłaty: 15.01.2025.
- Termin 14 dni (ustalony w wezwaniu) → wymagalność 30.01.2025.
- Niezapłacone do 01.07.2025 (152 dni opóźnienia).
- Stawka: 11,25%.
- Odsetki = 100 000 × 11,25% × 152 / 365 = **4 684,93 zł**.

### Przykład 4 — okresy z różnymi stawkami

- Kwota 50 000 zł, wymagalność 01.01.2024 do 01.10.2024 (274 dni).
- 01.01–30.06.2024 (181 dni): stawka 11,25% → 50 000 × 11,25% × 181/365 = 2 790 zł.
- 01.07–01.10.2024 (93 dni): stawka 10,75% → 50 000 × 10,75% × 93/365 = 1 369 zł.
- **Łącznie: 4 159 zł**.

## Rekompensata 40/70/100 euro — szczegóły

**Ustawa z 08.03.2013 art. 10:** rekompensata **niezależna od innych roszczeń**, należna **bez wezwania** i bez wykazywania szkody.

**Kalkulacja kursu:** wg kursu średniego NBP z ostatniego dnia roboczego miesiąca poprzedzającego miesiąc, w którym świadczenie stało się wymagalne.

**Uwaga:** dla faktur wymagalnych w kilku miesiącach — rekompensata za każdą, osobno.

**Orzecznictwo SN** (uchwała z 11.12.2015, III CZP 94/15) — rekompensata przysługuje nawet w razie częściowej zapłaty w terminie.

## Kary umowne a odsetki

**Kary umowne** (art. 483 KC) — odszkodowanie umowne za niewykonanie / nienależyte wykonanie zobowiązania niepieniężnego.

**Odsetki od kary umownej** — biegną od dnia wezwania (art. 455 KC) lub od dnia oznaczonego w umowie; stawka wg reżimu ogólnego (zwykle art. 481 KC).

**Nie można domagać się równocześnie:** kary umownej i odszkodowania za tę samą szkodę (art. 484 § 1 KC, chyba że umowa inaczej).

## Skapitalizowanie odsetek (art. 482 § 1 KC)

Od odsetek zaległych **nie można** żądać odsetek (zakaz anatocyzmu). Wyjątki:

1. Powództwo o te odsetki — od dnia wytoczenia powództwa można naliczać odsetki od odsetek (anatocyzm sądowy).
2. Umowa o doliczeniu odsetek do kapitału (częste w bankowości).

## Format cytowania w pozwie

**Żądanie:** „wnoszę o zasądzenie od pozwanego na rzecz powoda kwoty [X] zł wraz z:
- odsetkami ustawowymi za opóźnienie (art. 481 § 2 KC) od dnia [Y] do dnia zapłaty" — dla zwykłej sprawy cywilnej;

albo:

- "odsetkami ustawowymi za opóźnienie w transakcjach handlowych (art. 4a ustawy z 08.03.2013) od dnia [Y] do dnia zapłaty" — dla transakcji handlowej.

**Dla rekompensaty:** „wnoszę o zasądzenie kwoty równowartości 70 euro tytułem rekompensaty z art. 10 ust. 1 pkt 2 ustawy z 08.03.2013 r. o przeciwdziałaniu nadmiernym opóźnieniom w transakcjach handlowych, przeliczonej na złote wg kursu średniego NBP z dnia 28.02.2025 r."

## Źródła

- **KC** — `https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU19640160093` (art. 359, 481, 455, 482).
- **Ustawa z 08.03.2013** — `https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20130000403`.
- **Obwieszczenia Ministra Sprawiedliwości** — o wysokości odsetek ustawowych, publikowane w Monitorze Polskim.
- **NBP — stopa referencyjna** — `https://www.nbp.pl/home.aspx?f=/dzienne/stopy.htm`; archiwum uchwał RPP — `https://www.nbp.pl/home.aspx?f=/polityka_pieniezna/dokumenty/files/rpp_uchwaly.html`.
- **Kurs EUR/PLN** — `https://www.nbp.pl/home.aspx?f=/kursy/kursya.html`.

## Najczęstsze błędy

- **Stosowanie art. 481 KC w transakcjach handlowych.** Ustawa 2013 jest lex specialis — obowiązuje wyższa stawka i rekompensata.
- **Pomijanie rekompensaty 40/70/100 euro.** Przysługuje **bez wezwania**, nie trzeba udowadniać szkody. Często pomijana w pozwach przeciwko przedsiębiorcom-dłużnikom.
- **Stosowanie jednej stopy do całego okresu.** Stopy się zmieniają — dzielić na podokresy.
- **Mylenie odsetek kapitałowych (art. 359) z odsetkami za opóźnienie (art. 481).** Kapitałowe są „wynagrodzeniem za korzystanie z kapitału" (gdy umowa przewiduje); za opóźnienie — kara za niepłacenie w terminie. Dwa różne mechanizmy.
- **Pomijanie maksimów** (art. 359 § 2¹, 481 § 2¹) — w umowach z nawiązkami odsetkowymi powyżej maksimum stosuje się maksimum, nie umowne.
- **Bieg odsetek przy odszkodowaniu bezumownym.** Od wezwania (art. 455 KC); często pomijane, w efekcie liczone od daty zdarzenia = za dużo.
- **Przeliczanie kursu EUR nie na „ostatni dzień roboczy miesiąca poprzedzającego wymagalność".** Częsty błąd — branie kursu z dnia wniesienia pozwu. Ustawa wyraźnie wskazuje moment.
- **Anatocyzm spoza wyjątków.** Naliczanie odsetek od zaległych odsetek = naruszenie art. 482 KC, poza wyjątkami.
- **Odsetki od kary umownej jako odsetki za opóźnienie w spełnieniu świadczenia pieniężnego.** Tak, biegną od wezwania; ale obliczenie od daty zdarzenia (np. od dnia naruszenia) = niepoprawne.
- **Pomijanie dnia początkowego.** Odsetki biegną od dnia wymagalności (lub następnego), nie od dnia zdarzenia. Sprawdzać datę precyzyjnie — dzień różnicy × rok = znacząca suma przy dużych kwotach.
