---
name: calculating-alimenty
title: calculating-alimenty
description: Use when determining the amount of alimony under Polish KRO — calculating justified needs of the entitled person vs. earning/property capacity of the obligor (art. 135 KRO), applying equal-standard-of-living principle, setting up documentary evidence, drafting interim security motions under art. 754¹ KPC, or coordinating with the Fundusz Alimentacyjny when enforcement fails
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/plugins/pl/skills/calculating-alimenty
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: family
language: pl
---

# calculating-alimenty

Alimenty w prawie polskim nie mają sztywnych tabel (inaczej niż w Niemczech z Düsseldorfer Tabelle czy niektórych stanach USA). Każdą sprawę sąd ocenia indywidualnie wg dwóch osi: **usprawiedliwionych potrzeb uprawnionego** i **zarobkowych oraz majątkowych możliwości zobowiązanego** (art. 135 § 1 KRO). Tam, gdzie decyduje zbieranie dowodów — ten skill jest mapą.

## Podstawa prawna

| Akt | Artykuły | Zakres |
|---|---|---|
| KRO | art. 128–144 | Obowiązek alimentacyjny |
| KRO | art. 133 | Alimenty rodziców wobec dziecka |
| KRO | art. 135 | Zakres świadczeń — potrzeby vs. możliwości |
| KRO | art. 137 | Osoba uprawniona i zobowiązana |
| KRO | art. 138 | Zmiana wysokości w razie zmiany stosunków |
| KRO | art. 60 | Alimenty od byłego małżonka po rozwodzie |
| KPC | art. 754¹ | Zabezpieczenie roszczeń alimentacyjnych |
| KPC | art. 1081–1088 | Egzekucja alimentów |
| Ustawa z 07.09.2007 o pomocy osobom uprawnionym do alimentów | cały | Fundusz Alimentacyjny |
| KK | art. 209 | Niealimentacja — przestępstwo |

## Krąg zobowiązanych (art. 128–130 KRO)

Obowiązek alimentacyjny obciąża **krewnych w linii prostej oraz rodzeństwo** (art. 128 KRO). Kolejność:

1. **Zstępni** (dzieci, wnuki) wobec wstępnych (rodziców, dziadków) — gdy wstępny w niedostatku.
2. **Wstępni** wobec zstępnych — rodzice wobec dzieci (art. 133 KRO) bez względu na niedostatek dziecka.
3. **Rodzeństwo** — w ostatniej kolejności (art. 128 KRO).
4. **Małżonkowie** — obowiązek wzajemnej pomocy w trakcie małżeństwa (art. 27 KRO); alimenty po rozwodzie — art. 60 KRO.

**Zasada subsydiarności (art. 132 KRO):** obowiązek zstępnych dalszych (np. dziadków) uruchamia się dopiero, gdy brak rodziców albo rodzice nie mogą płacić.

## Dzieci — szczegółowo (art. 133 KRO)

**§ 1:** rodzice są obowiązani do alimentacji dziecka, które **nie jest w stanie utrzymać się samodzielnie**, chyba że dochody z majątku dziecka wystarczają na jego utrzymanie.

**§ 2:** obowiązek istnieje także wobec pełnoletniego dziecka, które kontynuuje naukę albo z powodu stanu zdrowia nie może podjąć pracy.

**§ 3:** wyjątek — jeżeli obowiązek alimentacyjny wobec pełnoletniego dziecka jest połączony z **nadmiernym uszczerbkiem** dla rodzica lub dziecko **nie dokłada starań**, by uzyskać możność samodzielnego utrzymania się.

**Brak górnej granicy wieku** — jedyna przesłanka to niesamodzielność (nauka, choroba, niepełnosprawność). W praktyce: alimenty dla studenta studiów stacjonarnych — standard; alimenty dla doktoranta — możliwe, wymaga uzasadnienia; alimenty dla 30-latka bezrobotnego bez uzasadnienia — zwykle oddalenie.

## Zakres świadczeń (art. 135 KRO)

> „Zakres świadczeń alimentacyjnych zależy od usprawiedliwionych potrzeb uprawnionego oraz od zarobkowych i majątkowych możliwości zobowiązanego."

**§ 2:** wykonanie obowiązku wobec dziecka może polegać, w całości lub w części, na osobistych staraniach o jego utrzymanie lub wychowanie — wtedy świadczenie obejmuje jedynie część pieniężną.

### Usprawiedliwione potrzeby

Wszystkie wydatki związane z utrzymaniem i rozwojem uprawnionego **na odpowiednim poziomie**. Dla dziecka — *zasada równej stopy życiowej*: ten sam standard jak rodzic.

**Kategorie (do wyliczenia w pozwie):**

| Kategoria | Zakres | Dowody |
|---|---|---|
| Wyżywienie | Żywność, napoje, posiłki szkolne / w pracy | Faktury / paragony (wyrywkowo); biegłe szacunki miesięczne |
| Mieszkanie | Czynsz / rata kredytu, media, Internet, TV | Rachunki, umowa najmu, zaświadczenie |
| Ubranie | Odzież, obuwie, bielizna | Paragony, sezonowe szacunki |
| Zdrowie | Wizyty lekarskie, leki, rehabilitacja, stomatolog | Faktury, recepty, dokumentacja medyczna |
| Edukacja | Przedszkole, szkoła, podręczniki, zajęcia dodatkowe, korepetycje, studia (czesne, materiały) | Umowy, faktury |
| Hobby i rozrywka | Zajęcia sportowe, klub, wycieczki, książki | Umowy, paragony |
| Komunikacja | Bilet miesięczny, dojazdy do szkoły | Bilety |
| Higiena | Kosmetyki, środki higieniczne | Paragony (wyrywkowo) |
| Urodziny / święta | Roczny koszt podzielony na 12 | Szacunki |
| Wakacje | Roczny koszt podzielony na 12 | Szacunki / umowa biura podróży |
| Ubezpieczenie | OC / zdrowotne dobrowolne | Polisy |

**Standard dowodzenia:** zestawienie miesięczne, pozycja po pozycji, z załącznikiem dokumentów. Orzecznictwo SN akceptuje oszacowania rozsądne — nie wymaga każdego paragonu. Ale im lepsza dokumentacja, tym wyższe szanse pełnego uwzględnienia.

### Zarobkowe i majątkowe możliwości zobowiązanego

**Nie tylko rzeczywiste dochody**, ale także **potencjalne** — jeżeli zobowiązany celowo zaniża albo nie wykorzystuje możliwości (SN: wyrok z 27.10.2000 r., IV CKN 1614/00; wyrok z 16.05.1975 r., III CRN 48/75).

**Co sąd bierze pod uwagę:**

- Zatrudnienie — umowa o pracę, B2B, umowa o dzieło, zlecenie, dywidendy.
- PIT-y za ostatnie 2-3 lata (żądanie z sądu do US albo przedstawienie przez stronę).
- Zaświadczenie o wynagrodzeniu od pracodawcy.
- Dochody z najmu nieruchomości, dzierżawy.
- Wiek, wykształcenie, kwalifikacje, doświadczenie zawodowe.
- Stan zdrowia i zdolność do pracy.
- Sytuacja na lokalnym rynku pracy (w razie bezrobocia).
- Majątek (nieruchomości, samochody, oszczędności) — dochody możliwe z niego.

**Nowe dzieci** — kolejne dziecko od nowej partnerki / partnera **nie zwalnia** z obowiązku wobec poprzednich. Dzieli tylko możliwości (więcej dzieci = niższa rata na każde).

**Obciążenia uzasadnione** — kredyt mieszkaniowy na mieszkanie zobowiązanego, koszty leczenia, dzieci z innych związków — uwzględniane. **Wydatki uznaniowe** (drogie samochody, wakacje, hobby) — **nie**.

### Zasada równej stopy życiowej

Dziecko ma prawo do standardu **takiego samego**, jaki ma rodzic. Sąd w tej zasadzie ma oparcie orzecznicze (SN: wyrok z 05.01.1956 r., III CR 919/55; wyrok z 25.03.1985 r., III CRN 341/84).

**Konsekwencje:**
- Jeżeli rodzic zarabia 20 000 zł _(orientacyjne)_, alimenty w wysokości 500 zł _(orientacyjne)_ na dziecko — mogą być uznane za niewystarczające.
- Jeżeli rodzic zarabia 3 000 zł _(orientacyjne)_, żądanie 3 000 zł _(orientacyjne)_ na dziecko — nierealne.

## Zmiana wysokości (art. 138 KRO)

> „W razie zmiany stosunków można żądać zmiany orzeczenia lub umowy dotyczącej obowiązku alimentacyjnego."

**„Zmiana stosunków"** — istotna, nie przejściowa:
- Wzrost potrzeb dziecka (nowa szkoła, wiek, choroba, studia).
- Zmiana dochodów zobowiązanego (wzrost albo spadek).
- Nowe dzieci zobowiązanego.
- Utrata pracy, choroba.
- Uzyskanie przez dziecko samodzielności.

**Pozew o zmianę** — tryb odrębny (nie zwykłe zabezpieczenie w istniejącej sprawie). Rozpatrywany przez sąd rejonowy wydział rodzinny.

## Zabezpieczenie alimentów w toku postępowania (art. 754¹ KPC)

**Uprzywilejowany typ zabezpieczenia** — dla roszczeń alimentacyjnych, wypłaty z tytułu umowy o pracę, rent.

**Zasada:**
- Uprawdopodobnienie **samego roszczenia** (faktu obowiązku alimentacyjnego i potrzeb) wystarczy.
- Nie wymaga uprawdopodobnienia **interesu prawnego** w zabezpieczeniu (inaczej niż w art. 730¹ KPC — zwykłe zabezpieczenie).

**Skutek:** sąd postanowieniem tymczasowo zasądza alimenty na czas postępowania. Decyzja jest natychmiast wykonalna; nadaje się do egzekucji komorniczej.

**Praktyka:** w każdym pozwie o alimenty — obowiązkowy wniosek o zabezpieczenie. W razie braku — alimenty pojawiają się dopiero po wyroku (miesiące / lata).

**Opłata:** 100 zł, jeżeli wniosek składa się przed wszczęciem postępowania; bez opłaty — jeżeli w toku (z pozwem).

## Egzekucja alimentów

**Pierwszeństwo** (art. 1025 KPC) — alimenty mają uprzywilejowane miejsce w kolejności zaspokajania wierzytelności.

**Zajęcie wynagrodzenia** (art. 1081 nn. KPC) — na alimenty komornik może zająć **do 60%** wynagrodzenia (inaczej niż zwykłe zobowiązania — 50%). Zachowana kwota wolna — tylko 50% minimalnego wynagrodzenia.

**Prawo jazdy** — komornik może wnioskować o zawieszenie (ustawa o pomocy osobom uprawnionym do alimentów) przy zaległości powyżej 3 miesięcy.

**KRD / BIK** — wpis dłużnika alimentacyjnego.

**Odpowiedzialność karna** — art. 209 KK: uporczywe uchylanie się od alimentów, jeżeli łączna wysokość zaległości przekracza równowartość 3 świadczeń okresowych → kara pozbawienia wolności do 1 roku (po nowelizacji 2017 — do 2 lat przy szczególnej uporczywości).

## Fundusz Alimentacyjny

### Aktualne parametry — pobrać przed obliczeniem

| Parametr | Źródło | Sposób pobrania | Fallback _(ostatnio zweryfikowany)_ |
|---|---|---|---|
| Kryterium dochodowe FA | Ustawa z 07.09.2007 o pomocy osobom uprawnionym do alimentów | WebSearch: «kryterium dochodowe fundusz alimentacyjny [bieżący rok]» | 1 209 zł/os. _(stan na 2024)_ |
| Maksymalna kwota FA | j.w. | j.w. | 500 zł/mies. _(stan na 2024)_ |

**Zasady:**
1. **Fetch udany** → użyj pobranej, podaj źródło i datę.
2. **Fetch nieudany** → użyj fallback. Ostrzeż: «⚠ Kryterium pochodzi ze stanu na [data]. Sprawdź aktualną wartość.»

**Ustawa z 07.09.2007 o pomocy osobom uprawnionym do alimentów** (Dz.U. 2024 poz. 1288 — weryfikować aktualne).

**Warunki otrzymania świadczenia:**
- Zasądzone alimenty z tytułem wykonawczym.
- **Bezskuteczność egzekucji** — potwierdzona przez komornika (brak ściągnięcia co najmniej za ostatnie 2 miesiące).
- **Kryterium dochodowe** — dochód rodziny nie przekracza 1 209 zł na osobę _(fallback; stan na 2024)_ (weryfikować aktualne; zmienia się okresowo).

**Kwota:**
- Do wysokości alimentów zasądzonych, maksymalnie **500 zł miesięcznie** _(fallback; stan na 2024)_ na dziecko (weryfikować; kwota była podnoszona).

**Procedura:** wniosek do gminnego / miejskiego ośrodka pomocy społecznej w miejscu zamieszkania uprawnionego.

**Skutek dla dłużnika:** fundusz wstępuje w prawa wierzyciela i prowadzi egzekucję we własnym zakresie — dług wobec państwa.

## Przykłady obliczeń

### Przykład 1 — dziecko w wieku szkolnym

- Dziecko: 10 lat, uczeń szkoły podstawowej.
- Potrzeby miesięczne (uzasadnione): 1 800 zł _(orientacyjne)_
  - Wyżywienie: 500 zł _(orientacyjne)_
  - Mieszkanie (1/3 udziału): 400 zł _(orientacyjne)_
  - Ubranie: 150 zł _(orientacyjne)_
  - Edukacja (podręczniki, angielski, basen): 250 zł _(orientacyjne)_
  - Zdrowie: 100 zł _(orientacyjne)_
  - Higiena: 50 zł _(orientacyjne)_
  - Rozrywka, hobby: 150 zł _(orientacyjne)_
  - Wakacje / urodziny (1/12): 100 zł _(orientacyjne)_
  - Komunikacja: 50 zł _(orientacyjne)_
  - Rezerwa: 50 zł _(orientacyjne)_
- Rodzic A zarabia 8 000 zł _(orientacyjne)_ netto; rodzic B — 5 000 zł _(orientacyjne)_ netto. Dziecko mieszka z rodzicem B.
- Podział proporcjonalny: A płaci 8 / (8 + 5) = 61,5% potrzeb = ~1 107 zł _(orientacyjne)_. **Żądanie alimentów: 1 100 zł _(orientacyjne)_.** Rodzic B uzupełnia resztą + osobiste starania.

### Przykład 2 — pełnoletnie dziecko, student

- Dziecko: 22 lata, student studiów magisterskich stacjonarnych.
- Czesne: 0 zł (publiczna uczelnia); stancja: 1 500 zł _(orientacyjne)_; wyżywienie: 800 zł _(orientacyjne)_; książki / materiały: 200 zł _(orientacyjne)_; komunikacja: 200 zł _(orientacyjne)_; telefon / Internet: 100 zł _(orientacyjne)_; rozrywka: 200 zł _(orientacyjne)_.
- Razem: 3 000 zł miesięcznie _(orientacyjne)_.
- Dochód własny z pracy dorywczej: 500 zł _(orientacyjne)_.
- Żądanie alimentów: 2 500 zł _(orientacyjne)_ od obojga rodziców (proporcjonalnie do ich dochodów) lub od jednego, z którym dziecko ma konflikt.

### Przykład 3 — zmiana (art. 138 KRO)

- Alimenty zasądzone 5 lat temu: 800 zł _(orientacyjne)_.
- Dziecko rozpoczęło studia, potrzeby wzrosły do 2 500 zł _(orientacyjne)_.
- Dochód zobowiązanego wzrósł z 4 000 zł do 10 000 zł _(orientacyjne)_.
- **Pozew o podwyższenie** — z 800 do 1 800 zł _(orientacyjne)_. Zmiana istotna po obu stronach.

## Workflow

1. **Ustalić zobowiązanego i uprawnionego.** Zstępny / wstępny / rodzeństwo / (były) małżonek.
2. **Zebrać dokumentację potrzeb uprawnionego** — miesięczne zestawienie wg tabeli powyżej. Faktury, paragony, umowy, polisy.
3. **Zebrać dokumentację dochodów zobowiązanego** — PIT-y, zaświadczenia, wyciągi bankowe. Jeżeli unika — wniosek do sądu o pomoc w uzyskaniu (art. 248 KPC).
4. **Zastosować zasadę równej stopy życiowej** (dla dzieci) — sprawdzić standard życia zobowiązanego vs. proponowana rata.
5. **Dobrać kwotę** — uzasadnione potrzeby × udział zobowiązanego w utrzymaniu (proporcjonalnie do dochodów obojga rodziców, jeżeli dotyczy).
6. **Wniosek o zabezpieczenie** (art. 754¹ KPC) — zawsze, o tę samą lub nieco niższą kwotę.
7. **WPS** — 12-krotność miesięcznej raty (art. 22 KPC). Wpływa na właściwość i koszty (ale nie na opłatę sądową — art. 96 UKSC zwalnia od opłaty).
8. **Dowody** — załączyć wszystkie. W toku postępowania — wezwać świadków (nauczyciele, sąsiedzi, lekarze — dla niektórych spraw).

## Najczęstsze błędy

- **Żądanie bez dokumentacji.** Sąd nie zasądzi 3 000 zł _(orientacyjne)_, jeżeli uzasadnione potrzeby nie są wykazane.
- **Pomijanie wniosku o zabezpieczenie.** Bez zabezpieczenia — dziecko bez alimentów przez cały czas postępowania (zwykle rok-dwa).
- **Stosowanie tabel z innych krajów.** Düsseldorfer Tabelle nie obowiązuje. Liczy się indywidualne rozpoznanie sprawy.
- **Pomijanie zasady równej stopy życiowej.** Jeżeli rodzic zarabia 20k _(orientacyjne)_, żądanie 700 zł _(orientacyjne)_ może być uznane za zaniżone (paradoksalnie) przez sąd z urzędu.
- **Mylenie alimentów na rzecz dziecka z alimentami między byłymi małżonkami** (art. 60 KRO). Różne przesłanki (niedostatek / istotne pogorszenie), różne terminy (5 lat / bez ograniczenia).
- **Pomijanie „potencjalnych możliwości".** Jeżeli zobowiązany nagle „stracił" pracę — sąd może uwzględnić poprzednie dochody i kwalifikacje.
- **Nieuwzględnianie nowych dzieci zobowiązanego.** Dzieli się zdolności alimentacyjne między wszystkie dzieci; pozew trzeba uzasadnić z uwzględnieniem nowych.
- **Niealimentacja jako podstawa obniżenia kolejnych alimentów.** Art. 209 KK niealimentujący nie może powołać się na własne zadłużenie jako argument na zmianę.
- **Pomijanie art. 138 KRO.** W razie zmiany stosunków — **osobny pozew**, nie „dopisanie" do istniejącego postępowania.
- **Pomijanie Funduszu Alimentacyjnego.** Przy bezskutecznej egzekucji i niskim dochodzie — ważne uzupełniające źródło.
- **Pominięcie 12× w WPS** — błędne obliczenie dla celów właściwości sądu (choć nie wpływa na opłatę).
