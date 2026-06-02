---
name: reviewing-b2b-service-contract
title: reviewing-b2b-service-contract
description: Use when auditing Polish B2B service contract (umowa o świadczenie usług / umowa współpracy / kontrakt B2B / staff augmentation / IT outsourcing) — zakaz konkurencji B2B (art. 353¹ KC, SN II CSK 58/18), klauzule wyłączności vs pozorny stosunek pracy (art. 22 § 1¹ KP), kary umowne (art. 483-484 KC, miarkowanie), IP (prawa autorskie do kodu / dzieła), JDG-specyficzne (Prawo Przedsiębiorców art. 6, CEIDG), obowiązek pierwszeństwa, rejestry (CEIDG, KRS, biała lista VAT)
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/plugins/pl/skills/reviewing-b2b-service-contract
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: commercial
language: pl
---

# reviewing-b2b-service-contract

Umowa o świadczenie usług w obrocie B2B (umowa współpracy, umowa ramowa, kontrakt IT, staff augmentation, outsourcing) to umowa nienazwana regulowana przez art. 750 KC (odpowiednie stosowanie przepisów o zleceniu) i art. 353¹ KC (zasada swobody umów). Problem nie w formie (wystarczy pisemna, a nawet dokumentowa — art. 77² KC), lecz w klauzulach ograniczających: zakaz konkurencji, wyłączność, kary umowne, IP. Ten skill — checklist audytu i lista red flags dla takich umów, w szczególności dla JDG (jednoosobowej działalności gospodarczej).

## Zakres stosowania

| Typ umowy | Charakter | Przykłady |
|---|---|---|
| Umowa o świadczenie usług (art. 750 KC) | Starannego działania | Consulting, programowanie, marketing, doradztwo |
| Umowa współpracy (ramowa) | Ramowa + zlecenia wykonawcze | Framework agreement + zamówienia szczegółowe |
| Staff augmentation / body leasing | Udostępnienie specjalisty | IT, inżynieria, finanse |
| IT outsourcing (T&M / fixed price) | Kompleksowe świadczenie | Development, maintenance, DevOps |
| Managed services | Utrzymanie / SLA | Infrastruktura, helpdesk, monitoring |

## Obowiązkowa weryfikacja kontrahenta

| Rejestr | URL | Co sprawdzić | Koszt |
|---|---|---|---|
| **CEIDG** | `https://aplikacja.ceidg.gov.pl` | Status JDG, PKD, data wpisu, adres, zawieszenia | Bezpłatne |
| **KRS** | `https://ekrs.ms.gov.pl` | Sp. z o.o. / S.A. — reprezentacja, kapitał, upadłość, likwidacja | Bezpłatne |
| **Biała lista VAT** | `https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka/` | Status czynnego podatnika VAT, rachunek do przelewu | Bezpłatne |
| **REGON** | `https://wyszukiwarkaregon.stat.gov.pl` | Numer REGON, PKD, status statystyczny | Bezpłatne |
| **KRD / BIG InfoMonitor** | `https://krd.pl`, `https://www.big.pl` | Zaległości płatnicze kontrahenta | Płatne (raport) |

**Minimum obowiązkowe**: CEIDG/KRS (status), biała lista VAT (czynny podatnik, rachunek bankowy), REGON (PKD). Dla kontraktów > 50 000 zł netto — dodatkowo KRD/BIG.

## Zakaz konkurencji w B2B

### Podstawa prawna — art. 353¹ KC, nie Kodeks pracy

Zakaz konkurencji w umowie B2B między przedsiębiorcami **nie** jest regulowany przez art. 101¹–101⁴ KP — te przepisy stosują się **wyłącznie** do stosunku pracy. W obrocie B2B klauzula zakazu konkurencji jest elementem swobody umów (art. 353¹ KC) i podlega ocenie w granicach trzech ograniczeń:

1. **Właściwość (natura) stosunku** — klauzula nie może zaprzeczać naturze stosunku B2B (współpraca niezależnych przedsiębiorców).
2. **Ustawa** — nie może naruszać przepisów bezwzględnie obowiązujących.
3. **Zasady współżycia społecznego** (art. 58 § 2 KC) — nie może być rażąco niesprawiedliwa.

Klauzula naruszająca te granice jest **nieważna** (art. 58 § 1–2 KC) — od początku, z mocy prawa, bez potrzeby orzeczenia sądu (nieważność bezwzględna).

### Test ważności klauzuli

- [ ] **Zakres podmiotowy precyzyjny?** Nazwani konkurenci / lista klientów — nie „każdy podmiot o podobnej działalności" czy „branża IT". Klauzula obejmująca całą branżę = potencjalnie nieważna (SN II CSK 58/18).
- [ ] **Czas trwania proporcjonalny?** W praktyce SN akceptuje 6–24 miesięcy po zakończeniu umowy. Brak terminu (bezterminowy) = potencjalnie nieważna (SA Szczecin, 05.10.2017).
- [ ] **Zakres terytorialny ograniczony?** Polska / UE / konkretne miasta — nie „cały świat" (chyba że uzasadnione globalnym rynkiem klienta).
- [ ] **Zakres przedmiotowy ograniczony?** Konkretna technologia / segment — nie „wszelkie usługi IT" czy „wszelka działalność zbliżona".
- [ ] **Wynagrodzenie za zakaz po ustaniu?** Między przedsiębiorcami brak wynagrodzenia ≠ automatyczna nieważność (V CSK 30/13), ale brak kompensacji **istotnie osłabia** egzekwowalność i wspiera argument o nieproporcjonalności (II CSK 58/18).
- [ ] **Kara umowna proporcjonalna?** Kara > 24-krotność miesięcznego wynagrodzenia z umowy — ryzyko miarkowania (art. 484 § 2 KC).
- [ ] **Klauzula nie wyłącza JDG z rynku?** Jeżeli zakaz obejmuje całą branżę, w której JDG prowadzi działalność (zgodnie z PKD) — narusza naturę stosunku B2B i jest potencjalnie nieważna.
- [ ] **Uzasadniony interes?** Zakaz musi chronić konkretny interes zleceniodawcy (tajemnice przedsiębiorstwa, baza klientów, know-how) — nie służyć wyłącznie ograniczeniu konkurencji.

### Orzecznictwo SN — kluczowe wyroki

| Sygnatura | Data | Teza | Znaczenie |
|---|---|---|---|
| **SN II CSK 58/18** | 05.03.2019 | Zakaz konkurencji w B2B musi odpowiadać „uzasadnionej potrzebie", być proporcjonalny i nie wyłączać strony z rynku | Klucz: szeroki zakaz obejmujący całą branżę = potencjalnie nieważny |
| **SN V CSK 30/13** | 05.12.2013 | Bezpłatny zakaz konkurencji po ustaniu umowy B2B nie jest sam w sobie nieważny; swoboda umów między przedsiębiorcami jest szersza | Odróżnia B2B od prawa pracy; brak wynagrodzenia ≠ nieważność |
| **SN IV CSK 804/14** | 19.11.2015 | Bezpłatność zakazu nie przesądza o nieważności — ocena w kontekście całokształtu umowy | Wzmacnia V CSK 30/13; proporcjonalność decyduje |
| **SN III CKN 579/01** | 11.09.2003 | Bezpłatny 3-letni zakaz po ustaniu umowy może naruszać zasady współżycia społecznego | Wczesny precedens — nadmierny czas + brak wynagrodzenia = nieważność |
| **SA Szczecin (05.10.2017)** | 05.10.2017 | Niejasny, nieograniczony w czasie zakaz uniemożliwiający swobodę kontraktowania — nieważny na podst. art. 58 § 2 KC | Bezterminowy + niejasny = nieważny |

⚠ **Uwaga**: sygnatury zweryfikuj przed powołaniem w dokumentach klienckich przez skill `pl:searching-orzeczenia`. Orzecznictwo SN w sprawie B2B non-compete jest niejednorodne — każda sprawa oceniana indywidualnie.

### Klauzula bez wynagrodzenia

W prawie pracy brak wynagrodzenia za zakaz konkurencji po ustaniu stosunku pracy oznacza nieważność klauzuli (art. 101² § 1 KP — minimum 25% wynagrodzenia). W B2B jest inaczej: SN w wyroku V CSK 30/13 stwierdził, że brak wynagrodzenia **nie przesądza** o nieważności zakazu między przedsiębiorcami. Jednakże brak jakiejkolwiek kompensacji stanowi istotny argument na rzecz **nieproporcjonalności** klauzuli (SN II CSK 58/18) i może prowadzić do jej uznania za sprzeczną z zasadami współżycia społecznego, szczególnie gdy JDG jest stroną słabszą ekonomicznie.

## Klauzule wyłączności i pozorny stosunek pracy

### Cechy wskazujące na stosunek pracy (art. 22 § 1¹ KP)

| Cecha | Opis | Klasyfikacja |
|---|---|---|
| Zakaz pracy dla innych klientów | Wyłączność = cecha podporządkowania | **KRYTYCZNE** |
| Stałe godziny pracy wyznaczone przez zleceniodawcę | Podporządkowanie czasowe | ISTOTNE |
| Jeden zleceniodawca przez dłuższy czas | Zależność ekonomiczna | ISTOTNE |
| Obowiązek zgłaszania innych zleceń / klientów | Kontrola nad swobodą działalności | ISTOTNE |
| Praca w siedzibie zleceniodawcy pod nadzorem | Podporządkowanie organizacyjne i miejscowe | ISTOTNE |
| Zleceniodawca dostarcza narzędzia (laptop, licencje, biurko) | Cecha pracodawcy | ISTOTNE |
| Obowiązek osobistego wykonania (bez podwykonawców) | Osobisty charakter = cecha pracy | ISTOTNE |
| Stała miesięczna stawka niezależna od wyników | Wynagrodzenie jak za pracę | POŻĄDANE |

### Ryzyko kumulacyjne

Wystąpienie jednej cechy = niskie ryzyko. Jednoczesne wystąpienie **3 lub więcej** cech = wysokie ryzyko przekwalifikowania. PIP (Państwowa Inspekcja Pracy) i ZUS mogą z urzędu wszcząć postępowanie kontrolne. Powództwo o ustalenie istnienia stosunku pracy (art. 189 KPC) może złożyć pracownik, PIP lub ZUS.

### Skutki przekwalifikowania

- Retroaktywne składki ZUS (emerytalne, rentowe, chorobowe, wypadkowe, zdrowotne) — **za cały okres** „B2B" — obciążają zleceniodawcę (traktowanego jako pracodawca) z odsetkami.
- Pracownik nabywa uprawnienia: urlop, L4, nadgodziny, ochrona przed wypowiedzeniem, odprawy.
- Korekta PIT — zleceniodawca odprowadza zaliczki na PIT jako pracodawca.
- Potencjalna odpowiedzialność karnoskarbowa za nieopłacanie składek.

## Kary umowne w kontekście B2B (art. 483–484 KC)

- Art. 483 § 1 KC — kara umowna zastrzegalna **wyłącznie za zobowiązanie niepieniężne**. Zakaz konkurencji jest zobowiązaniem niepieniężnym — kara umowna za jego naruszenie jest co do zasady **dopuszczalna**.
- Art. 484 § 1 KC — wierzyciel nie musi udowadniać wysokości poniesionej szkody; wystarczy wykazać naruszenie.
- Art. 484 § 2 KC — **miarkowanie**: sąd może zmniejszyć karę umowną, jeżeli jest **rażąco wygórowana** lub jeżeli zobowiązanie zostało w znacznej części wykonane.

Orientacyjna ocena proporcjonalności:

| Kara (w stosunku do miesięcznego wynagrodzenia z umowy) | Ocena |
|---|---|
| ≤ 6x | Niska — raczej proporcjonalna |
| 6x–12x | Umiarkowana — akceptowalna przy uzasadnionym interesie |
| 12x–24x | Wysoka — ryzyko miarkowania |
| > 24x | Bardzo wysoka — znaczne ryzyko miarkowania (art. 484 § 2 KC) |

⚠ Powyższa skala jest **orientacyjna**. Sąd ocenia proporcjonalność in casu, uwzględniając: wartość umowy, czas trwania współpracy, zakres naruszenia, wysokość poniesionej szkody, zachowanie stron.

## JDG — szczególne zagadnienia

- **Art. 6 Prawo Przedsiębiorców (ustawa z 06.03.2018)**: podejmowanie, wykonywanie i zakończenie działalności gospodarczej jest wolne dla każdego na równych prawach. Klauzula B2B ograniczająca tę wolność musi mieć silne uzasadnienie.
- **Art. 8 Prawo Przedsiębiorców**: niedające się usunąć wątpliwości co do treści normy prawnej rozstrzyga się na korzyść przedsiębiorcy.
- **CEIDG i PKD**: JDG ma zarejestrowane kody PKD. Zakaz konkurencji obejmujący **wszystkie** kody PKD = faktyczne zawieszenie działalności = potencjalnie nieważny.
- **Jednoklientowość**: JDG z jednym klientem, wyłącznością, stałymi godzinami i brakiem podwykonawców = kompletny profil pozornego stosunku pracy.
- **Prawo Przedsiębiorców vs. KP**: JDG to przedsiębiorca, nie pracownik. Traktowanie JDG jak pracownika (kontrola, raportowanie, wyłączność) podważa naturę stosunku B2B.

## Prawa własności intelektualnej (IP)

- **Art. 1 ustawy o prawie autorskim** (04.02.1994) — utwór: każdy przejaw działalności twórczej (kod, dokumentacja, architektura, grafiki).
- **Art. 12** — utwór pracowniczy: prawa do pracodawcy, ale **tylko w stosunku pracy**. W B2B — art. 12 **nie stosuje się**; prawa do utworu pozostają przy twórcy (zleceniobiorcy/JDG), chyba że umowa stanowi inaczej.
- **Art. 74** — programy komputerowe: majątkowe prawa autorskie do programu stworzonego w wyniku obowiązków z umowy o pracę → pracodawca (art. 74 ust. 3). W B2B — brak takiego domniemania; potrzebna **wyraźna klauzula przeniesienia** (art. 53 — wymóg formy pisemnej pod rygorem nieważności).
- **Red flags w klauzulach IP**:
  - „Wszelkie prawa do utworów stworzonych w czasie obowiązywania umowy" — **KRYTYCZNE**: obejmuje prywatne projekty, open source, niezwiązane z umową.
  - Przeniesienie bez wyraźnego wskazania pól eksploatacji (art. 50) — **nieważne**: konieczne wymienienie każdego pola.
  - Zrzeczenie się autorskich praw osobistych — **niedopuszczalne** na gruncie art. 16 (prawa osobiste niezbywalne).

## Obowiązek pierwszeństwa (priority obligation)

Klauzule zobowiązujące JDG do „nadawania priorytetu" usługom dla jednego klienta (np. „Contractor shall prioritize Client's services over other business activities") — dozwolone co do zasady, ale:

- Priorytet **bez** limitu godzinowego + **bez** prawa do odmowy = de facto wyłączność → ryzyko pozornego stosunku pracy.
- Priorytet **z** gwarantowanym minimum godzin (np. 140h/mies.) i prawem JDG do dyspozycji resztą czasu = dopuszczalny.
- Priorytet + wyłączność + obowiązek informowania = kumulacja → klasa KRYTYCZNE.

## Red flags — audyt umowy B2B

| Zagrożenie | Znak | Klasyfikacja | Co zrobić |
|---|---|---|---|
| **Całkowita wyłączność** | „Zleceniobiorca nie będzie świadczył usług na rzecz żadnego innego podmiotu" | **KRYTYCZNE** | Ryzyko pozornego stosunku pracy; renegocjować lub odmówić |
| **Zakaz obejmujący całą branżę** | „w branży IT" / „w sektorze technologicznym" bez dalszego dookreślenia | **KRYTYCZNE** | Potencjalnie nieważny (SN II CSK 58/18); zaproponować listę nazwanych konkurentów |
| **Bezterminowy zakaz konkurencji** | Brak daty końcowej, brak maksymalnego czasu trwania | **KRYTYCZNE** | Nieważny (SA Szczecin 05.10.2017); dodać termin |
| **Zakaz bez wynagrodzenia (po ustaniu)** | Zakaz obowiązuje po zakończeniu umowy, 0 zł kompensacji | ISTOTNE | Osłabia egzekwowalność; zaproponować rekompensatę |
| **Kara umowna > 24x stawki miesięcznej** | Nieproporcjonalna kara za naruszenie zakazu | ISTOTNE | Ryzyko miarkowania (art. 484 § 2 KC); negocjować w dół |
| **IP obejmujące wcześniejsze prace** | „Wszelkie prawa do utworów stworzonych w czasie obowiązywania, w tym wcześniej rozpoczęte" | **KRYTYCZNE** | Ograniczyć do deliverables z umowy; wyłączyć pre-existing IP |
| **Jednostronne wypowiedzenie** | Zleceniodawca — natychmiast; JDG — 3 miesiące | ISTOTNE | Wyrównać okresy wypowiedzenia |
| **Brak określenia zakresu usług** | „Usługi zgodnie z bieżącymi ustaleniami" | ISTOTNE | Ryzyko braku essentialia negotii; dookreślić przedmiot |
| **Stałe godziny + stałe miejsce** | „09:00–17:00 w biurze Zleceniodawcy" | ISTOTNE | Wskaźnik pozornego stosunku pracy |
| **Kontrola metodologii** | „Zgodnie z wewnętrznymi procedurami Zleceniodawcy" | ISTOTNE | Wskaźnik podporządkowania |
| **Brak limitu odpowiedzialności** | Nieograniczona odpowiedzialność JDG | ISTOTNE | Zaproponować cap (np. 12x stawki miesięcznej) |
| **Automatyczne przedłużenie bez opt-out** | Milczące przedłużenie po upływie terminu | POŻĄDANE | Dodać okres na zgłoszenie nieprzedłużenia |
| **Obowiązek informowania o klientach** | „Zleceniobiorca poinformuje o każdej innej współpracy" | ISTOTNE | Ogranicza swobodę JDG; wskaźnik kontroli |

## Obowiązkowe elementy umowy B2B

| Element | Uwagi |
|---|---|
| **Dane stron** | JDG: imię i nazwisko, firma (CEIDG), NIP, REGON, adres; sp. z o.o. / S.A.: pełna nazwa, KRS, NIP, REGON, adres, osoby reprezentujące |
| **Przedmiot umowy** | Konkretny zakres usług (PKD, opis techniczny, technology stack); unikać ogólników „usługi IT" |
| **Wynagrodzenie** | Stawka (godzinowa / miesięczna / projektowa), waluta, VAT (wliczony / niewliczony), termin płatności, forma (przelew na rachunek z białej listy > 15 000 zł) |
| **Termin** | Data początkowa, końcowa, warunki przedłużenia, okresy wypowiedzenia |
| **Raportowanie / odbiór** | Jak raportowane godziny / deliverables, kto akceptuje, termin akceptacji, milcząca akceptacja |
| **IP** | Przeniesienie / licencja; pola eksploatacji (art. 50 ustawy o prawie autorskim); pre-existing IP; forma pisemna (art. 53) |
| **Poufność** | Zakres, czas obowiązywania, zwrot materiałów |
| **Zakaz konkurencji** | Jeżeli zawarty — z elementami testu ważności (pkt 4 powyżej) |
| **Kary umowne** | Tylko za zobowiązania niepieniężne; kwoty; klauzula miarkowania |
| **Odpowiedzialność** | Limity (cap), wyłączenia, ubezpieczenie OC działalności |
| **Rozwiązanie** | Wypowiedzenie (obie strony), skutek natychmiastowy, rozliczenie prac w toku |
| **RODO** | Umowa powierzenia przetwarzania (art. 28 RODO) jeżeli dane osobowe |
| **Podpisy** | Forma: pisemna / elektroniczna (art. 78¹ KC) / dokumentowa (art. 77² KC) |

## Szablon audytu

```
AUDYT UMOWY O ŚWIADCZENIE USŁUG (B2B)
Klient: [Zleceniobiorca (JDG) / Zleceniodawca]
Kontrahent: [nazwa, KRS/NIP]
Data projektu: [___]
Data audytu: [___]

I. WERYFIKACJA KONTRAHENTA
   - CEIDG / KRS — status: [OK / uwagi]
   - Biała lista VAT — status: [OK / nieaktywny]
   - Inne: [...]

II. ANALIZA KLAUZUL KRYTYCZNYCH
   - Zakaz konkurencji — [obecny / brak; jeśli obecny — wynik testu ważności z sekcji 4]
   - Wyłączność — [obecna / brak; jeśli obecna — ocena ryzyka pozorności]
   - Kary umowne — [proporcjonalne / nadmierne; kwota vs. stawka miesięczna]
   - IP — [klarowne / nadmiernie szerokie; pola eksploatacji wymienione?]

III. ZNALEZISKA NA PROJEKCIE UMOWY
   [lista ustaleń wg klasyfikacji: KRYTYCZNE / ISTOTNE / POŻĄDANE]

IV. OCENA RYZYKA POZORNEGO STOSUNKU PRACY
   [TAK / NIE — z uzasadnieniem; liczba spełnionych wskaźników z pkt 5]

V. ZALECENIE
   [podpisywać / nie podpisywać / warunkowo — pod warunkiem poprawek]
```

## Kiedy ten skill uzupełniany jest agentem / innym skillem

- Dla pełnego sporządzania umowy B2B — agent `pl:contract-drafter` (tryb sporządzania).
- Dla weryfikacji kontrahenta (reprezentacja, upadłość, VAT) — skill `pl:searching-krs`.
- Dla wymogów RODO / umowy powierzenia — skill `pl:applying-rodo`.
- Dla podejrzenia pozornego stosunku pracy — agent `pl:labor-drafter` (powództwo o ustalenie, art. 189 KPC + art. 22 § 1¹ KP).
- Dla windykacji niezapłaconych faktur B2B — agent `pl:debt-collector`.
- Dla sporu sądowego na tle umowy — agent `pl:claim-drafter`.
