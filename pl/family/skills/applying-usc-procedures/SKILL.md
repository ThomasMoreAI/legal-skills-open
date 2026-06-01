---
name: applying-usc-procedures
title: applying-usc-procedures
description: Use when navigating Polish USC procedures — rejestracja urodzenia (art. 60–69 ASC), małżeństwo cywilne / konkordatowe (art. 76–85), zmiana imienia / nazwiska (ustawa z 17.10.2008), transkrypcja aktów zagranicznych (art. 104–108), sprostowanie / unieważnienie aktu, odpisy (zupełne, skrócone, wielojęzyczne CIEC). Dokumenty, opłata skarbowa, terminy KPA, odwołania. Ustawa z 28.11.2014 o aktach stanu cywilnego
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/plugins/pl/skills/applying-usc-procedures
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: family
language: pl
---

# applying-usc-procedures

Urząd Stanu Cywilnego (USC) — organ administracji wykonujący zadania państwa dotyczące rejestracji stanu cywilnego. Prowadzi akty urodzenia, małżeństwa, zgonu, przyjmuje oświadczenia, wydaje zaświadczenia. Regulowany **ustawą z 28.11.2014 o aktach stanu cywilnego** (Dz.U. 2014 poz. 1741 ze zm., skrót: **ASC**). Poza ASC — **ustawa z 17.10.2008 o zmianie imienia i nazwiska** (Dz.U. 2008 nr 220 poz. 1414) — dla zmian imienia/nazwiska; **KPA** (art. 35 ff.) — dla terminów i trybu odwoławczego.

**Źródła urzędowe (primary):**
- ISAP — ustawa ASC: `https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20140001741`.
- Gov.pl — formularze i e-usługi: `https://www.gov.pl/web/gov/uslugi-dla-obywatela#akty-stanu-cywilnego`.
- Urząd miasta / gminy — lokalna strona właściwego USC.

**Forma wniosków:**
- Papierowa (wniosek do kierownika USC miasta/gminy);
- Elektroniczna przez **ePUAP** / **mObywatel** / **mOjbywatel** aplikacja;
- Wiele odpisów — wyłącznie elektronicznie przez `moj.gov.pl` (Profil Zaufany / e-dowód).

## Aktualne parametry — pobrać przed konsultacją

| Parametr | Źródło | Sposób pobrania | Fallback _(ostatnio zweryfikowany)_ |
|---|---|---|---|
| Opłaty skarbowe USC | Ustawa o opłacie skarbowej (Dz.U. 2006 nr 225 poz. 1635) | WebFetch: `https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20062251635` — załącznik (tabela opłat) | Tabela poniżej _(stan na 2024)_ |
| Opłata za akt małżeństwa | j.w. | j.w. | 84 zł _(stan na 2024)_ |
| Kara za nieterminowe zgłoszenie urodzenia | KRO art. 49 | WebFetch ISAP: KRO | 1 500 zł _(stan na 2024)_ |

**Zasady:**
1. **Fetch udany** → użyj pobranej wartości, podaj źródło i datę.
2. **Fetch nieudany** → użyj fallback. Ostrzeż: «⚠ Opłata pochodzi ze stanu na [data]. Sprawdź w ISAP.»

## Rejestracja urodzenia dziecka

| Parametr | Regulacja |
|---|---|
| **Właściwość** | USC miejsca urodzenia (art. 60 ASC) |
| **Termin zgłoszenia** | **21 dni** od urodzenia; dla dziecka martwo urodzonego — 3 dni (art. 60 ust. 2 ASC) |
| **Podmiot uprawniony** | Matka lub ojciec (obecność rodzica — wystarczy jednego); pełnomocnik (nieupoważniony do oświadczenia o uznaniu ojcostwa) |
| **Wymagane dokumenty** | Karta urodzenia (wystawia szpital — elektronicznie przesyłana do USC); dowód tożsamości rodziców; akt małżeństwa (jeśli są w związku); oświadczenie o uznaniu ojcostwa (dla dzieci pozamałżeńskich — formularz UK-1); decyzja sądu o ustaleniu ojcostwa (gdy było postępowanie) |
| **Wydawane** | Akt urodzenia + nr PESEL (nadawany automatycznie); pierwszy odpis skrócony — bezpłatny (art. 44 ust. 1 ASC) |
| **Opłata skarbowa** | **Bezpłatne** — rejestracja urodzenia zwolniona z opłaty skarbowej (zał. do ustawy o opłacie skarbowej, poz. 3) |

**E-usługa**: rejestracja urodzenia przez `gov.pl` — **tylko dla dzieci ze związku małżeńskiego** i pod warunkiem autentykacji Profilem Zaufanym. Dla pozamałżeńskich — wymagane osobiste stawiennictwo z oświadczeniem o uznaniu ojcostwa.

## Zawarcie małżeństwa cywilnego

| Parametr | Regulacja |
|---|---|
| **Właściwość** | USC wybranego przez nupturientów miasta/gminy (art. 76 ASC); nie musi być USC miejsca zamieszkania |
| **Zgłoszenie zamiaru** | **Co najmniej 31 dni przed** (art. 76 ust. 3 ASC); max 6 miesięcy |
| **Wymagane dokumenty** | Dowody tożsamości; odpisy skrócone aktów urodzenia (nie starsze niż 3 miesiące); jeżeli rozwiedziony — wyrok + klauzula prawomocności; jeżeli wdowiec/wdowa — odpis aktu zgonu małżonka; dla cudzoziemca — **zaświadczenie o zdolności do zawarcia związku małżeńskiego** z kraju pochodzenia (przetłumaczone przysięgle) lub zwolnienie sądu z jego przedstawienia (art. 79 ust. 1 pkt 1 ASC w zw. z art. 1146 KPC — zwolnienie postanowieniem sądu) |
| **Opłata skarbowa** | **84 zł** _(fallback; stan na 2024)_ — za sporządzenie aktu małżeństwa |
| **Formularz** | Oświadczenie stron o wstąpieniu w związek małżeński (USC) + pisemne zapewnienie o braku przeszkód (art. 76 ust. 1 pkt 1 ASC) |

**Małżeństwo poza lokalem USC** (plener, restauracja) — art. 85 ASC; opłata dodatkowa **1000 zł** _(fallback; stan na 2024)_.

## Małżeństwo konkordatowe (kościelne)

Uregulowane **konkordatem z 28.07.1993** + ustawą z 17.05.1989 o stosunku Państwa do Kościoła Katolickiego i ustawami o stosunku Państwa do innych kościołów/związków wyznaniowych.

| Parametr | Regulacja |
|---|---|
| **Zaświadczenie do zawarcia małżeństwa wyznaniowego** | Wydaje kierownik USC na wniosek nupturientów (art. 8 § 2 KRO w zw. z art. 86 ASC) |
| **Ważność zaświadczenia** | **6 miesięcy** od wydania |
| **Opłata skarbowa za zaświadczenie** | **Bezpłatne** (zwolnienie w ramach zawarcia małżeństwa konkordatowego) |
| **Akt małżeństwa** | Sporządza kierownik USC na podstawie zaświadczenia od duchownego (art. 87 ASC) — duchowny przekazuje USC w **5 dni** od ceremonii |
| **Opłata za akt małżeństwa** | **84 zł** _(fallback; stan na 2024)_ |

## Zmiana imienia lub nazwiska

**Podstawa**: ustawa z 17.10.2008 o zmianie imienia i nazwiska (Dz.U. 2008 nr 220 poz. 1414).

**Zasada**: zmianę dopuszcza się z **ważnych powodów** (art. 4 ustawy) — przesłanki ustawowe, m.in.: imię / nazwisko ośmieszające, z obcego języka, zgodnie z prawdą biologiczną / faktycznym używaniem.

| Parametr | Regulacja |
|---|---|
| **Właściwość** | Kierownik USC miejsca pobytu wnioskodawcy |
| **Forma** | Wniosek pisemny lub ePUAP |
| **Termin rozstrzygnięcia** | KPA art. 35: **1 miesiąc** (sprawy zwykłe) / **2 miesiące** (sprawy szczególnie skomplikowane) |
| **Opłata skarbowa** | **37 zł** _(fallback; stan na 2024)_ — za wydanie decyzji (zał. do ustawy o opłacie skarbowej, cz. I poz. 8) |
| **Zmiana nazwiska małżonka** | W chwili zawarcia małżeństwa lub w **3 miesięcy** po; potem tylko w trybie ustawy |
| **Odwołanie** | Wojewoda (art. 127 § 2 KPA) w **14 dni** |
| **Sąd administracyjny** | WSA / NSA po odwołaniu |

**Specyficzne sytuacje**:
- Dziecko > 13 lat — wymagana jego zgoda (art. 8 ustawy).
- Małżonek — wymagana zgoda drugiego małżonka (art. 6 ust. 1 pkt 2 ustawy) w przypadku zmiany wspólnego nazwiska.
- Zmiana imienia dziecka w pierwszych 6 miesiącach życia — uproszczona procedura (art. 70 ASC).

## Transkrypcja zagranicznych aktów stanu cywilnego

**Podstawa**: art. 104–108 ASC.

Wpisanie do polskiej księgi aktów stanu cywilnego dokumentu sporządzonego za granicą (akt urodzenia, małżeństwa, zgonu). Konieczne m.in. dla nadania numeru PESEL dziecku urodzonemu za granicą lub rejestracji zawartego za granicą małżeństwa.

| Parametr | Regulacja |
|---|---|
| **Właściwość** | Kierownik USC wybranego przez wnioskodawcę |
| **Wymagane** | Oryginał aktu zagranicznego + tłumaczenie przysięgłe na polski; dokument tożsamości; potwierdzenie pokrewieństwa (gdy dotyczy innej osoby) |
| **Apostille / legalizacja** | Dla państw konwencji haskiej 1961 — **apostille**; poza nimi — legalizacja konsulatem RP lub konsulatem danego państwa w RP |
| **Opłata skarbowa** | **50 zł** _(fallback; stan na 2024)_ — transkrypcja (zał. do ustawy o opłacie skarbowej) |
| **Termin** | 1 miesiąc (KPA art. 35) |

**Wyjątki**: z niektórych państw akty stanu cywilnego są uznawane bez transkrypcji (Konwencja CIEC Nr 16 z 08.09.1976 — akty wielojęzyczne); lista w rozporządzeniu MSW.

## Sprostowanie / unieważnienie aktu

**Sprostowanie** (art. 35–36 ASC) — błąd pisarski (literówka, błąd w dacie) — kierownik USC z urzędu lub na wniosek.

**Unieważnienie** (art. 39 ASC) — akt sporządzony sprzecznie z prawem lub podwójnie — decyzja sądu.

| Parametr | Regulacja |
|---|---|
| **Sprostowanie — opłata** | **39 zł** _(fallback; stan na 2024)_ za decyzję w trybie administracyjnym |
| **Unieważnienie — tryb** | Sąd rejonowy wydziału cywilnego — wniosek w trybie postępowania nieprocesowego (art. 609 KPC i nast.) |

## Wydawanie odpisów aktów stanu cywilnego

| Typ odpisu | Opłata | E-usługa |
|---|---|---|
| **Odpis skrócony** (PL) | **22 zł** _(fallback; stan na 2024)_ | Tak — `moj.gov.pl` |
| **Odpis zupełny** (PL) | **33 zł** _(fallback; stan na 2024)_ | Tak — `moj.gov.pl` |
| **Odpis wielojęzyczny** (CIEC, format międzynarodowy) | **22 zł** _(fallback; stan na 2024)_ | Tak — `moj.gov.pl` |
| **Zaświadczenie o stanie cywilnym** | **38 zł** _(fallback; stan na 2024)_ | Tak |
| **Zaświadczenie o zamieszczonych lub niezamieszczonych danych** | **24 zł** _(fallback; stan na 2024)_ | Tak |

**Forma e-odpisu**: plik PDF z kwalifikowanym podpisem elektronicznym kierownika USC; ważny tak samo jak papierowy.

**Wszystkie opłaty** — jak wyżej, zgodnie z załącznikiem do ustawy z 16.11.2006 o opłacie skarbowej.

## Terminy odpowiedzi organu (KPA)

- **Niezwłocznie** — gdy nie trzeba postępowania wyjaśniającego (wydanie odpisu, rejestracja urodzenia przy kompletnym zgłoszeniu).
- **1 miesiąc** — sprawy zwykłe (art. 35 § 3 KPA).
- **2 miesiące** — sprawy szczególnie skomplikowane (art. 35 § 3 KPA).

Brak decyzji w terminie — **ponaglenie** (art. 37 KPA) do wojewody.

## Odwołanie i sąd administracyjny

**Od decyzji kierownika USC**:
1. **Odwołanie** do wojewody (art. 127 § 2 KPA) w **14 dni** od doręczenia decyzji.
2. **Skarga** do WSA po wyczerpaniu odwołania (art. 50 i nast. PPSA); **30 dni** na skargę.
3. **Skarga kasacyjna** do NSA w **30 dni** od doręczenia wyroku WSA.

**Podstawa opłat sądowych w sprawach administracyjnych**: ustawa z 30.08.2002 — PPSA.

## Najczęstsze błędy i pułapki

- **Brak apostille przy transkrypcji** — USC nie przyjmie aktu bez apostille (z państw haskiej konwencji) lub legalizacji.
- **Tłumaczenie „zwykłe" zamiast przysięgłego** — odrzucone.
- **Upływ 21 dni od urodzenia** — po tym terminie rejestracja nadal jest dokonywana, ale przy możliwej grzywnie (art. 62 ust. 2 ASC) — do 1500 zł _(fallback; stan na 2024)_.
- **Mylenie odpisu skróconego ze zupełnym** — do spraw sądowych wymagany odpis zupełny; do urzędowych najczęściej skrócony wystarczy; CIEC dla spraw zagranicznych.
- **Małżeństwo konkordatowe — brak zaświadczenia** — ceremonia się odbyła, ale akt USC nie powstanie bez zaświadczenia USC; 6-miesięczna ważność — pilnować.
- **Transkrypcja aktu urodzenia dziecka zagranicznego bez zgody drugiego rodzica** — gdy jedno z rodziców nie jest wnioskodawcą, wymaga się formalnej zgody; unikać składania jednostronnie.

## Szablon wniosku o transkrypcję (skrót)

```
[Wnioskodawca: imię, nazwisko, PESEL, adres, tel.]

Kierownik Urzędu Stanu Cywilnego w [miasto]
ul. [adres USC]

WNIOSEK O TRANSKRYPCJĘ ZAGRANICZNEGO AKTU STANU CYWILNEGO
(art. 104 ustawy z 28.11.2014 o aktach stanu cywilnego)

Wnoszę o wpisanie (transkrypcję) do polskich ksiąg stanu cywilnego aktu:
   [rodzaj aktu — urodzenia/małżeństwa/zgonu]
   sporządzonego w [państwo, miejscowość] w dniu [___],
   przez [urząd wydający akt],
   nr [___].

Akt dotyczy [mnie/osoby: imię, nazwisko, PESEL/numer akt.].

Uzasadnienie wniosku (interes prawny): [np. potrzeba rejestracji meldunku,
uzyskania dowodu osobistego, nadania PESEL dziecku].

W załączeniu:
1. Oryginał aktu z apostille/legalizacją.
2. Tłumaczenie przysięgłe aktu na język polski.
3. Kopia dokumentu tożsamości.
4. Dowód opłaty skarbowej — 50 zł _(fallback; stan na 2024)_.

[data, podpis]
```

## Kiedy ten skill uzupełniany jest agentem / innym skillem

- Dla spraw rodzinnych po transkrypcji (rozwód, alimenty, ustalenie ojcostwa) — agent `pl:family-drafter`.
- Dla odmowy kierownika USC w sprawie zmiany imienia / nazwiska i skargi do sądu — agent `pl:appeal-drafter` (odwołanie KPA + skarga PPSA).
- Dla odmowy transkrypcji z powodów sprzeczności z porządkiem publicznym (np. akty małżeństw jednopłciowych z państw, które uznają — sprawa kontrowersyjna, opinia rzecznika) — rozważyć konsultację; agent `pl:legal-memo`.
- Dla sporu między rodzicami o imię / nazwisko dziecka (władza rodzicielska) — agent `pl:family-drafter`.
