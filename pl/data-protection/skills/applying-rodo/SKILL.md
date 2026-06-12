---
name: applying-rodo
title: applying-rodo
description: Use when drafting or reviewing RODO documents — mapping GDPR articles to obligations, legal basis (art. 6/9), klauzule informacyjne (art. 13–14), umowa powierzenia (art. 28), naruszenia (art. 33–34), DPIA (art. 35), wnioski osób (art. 15–22). RODO (2016/679) + UODO z 10.05.2018
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/skills/pl/law-pl-applying-rodo
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: data-protection
language: pl
---

# applying-rodo

RODO (GDPR) — rozporządzenie 2016/679 — jest stosowane bezpośrednio w Polsce. Ustawa z 10.05.2018 o ochronie danych osobowych (UODO) jest aktem uzupełniającym, głównie w zakresie wymaganym przez sam RODO (np. art. 8 ust. 1 — wiek zgody dzieci dla usług społeczeństwa informacyjnego, art. 88 — dane w kontekście zatrudnienia).

## Kluczowe URL

| Źródło | URL |
|---|---|
| RODO (tekst skonsolidowany) | https://eur-lex.europa.eu/eli/reg/2016/679/oj/pol |
| UODO (tekst jednolity) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20180001000 |
| PUODO | https://uodo.gov.pl |
| EDPB (wytyczne) | https://edpb.europa.eu |
| SCC (Rozp. 2021/914) | https://eur-lex.europa.eu/eli/reg_impl/2021/914/oj |
| Wykaz decyzji o adekwatności | https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en |

## Podstawy prawne — szybki wybór (art. 6 RODO)

| Sytuacja | Podstawa | Art. |
|---|---|---|
| Przetwarzanie na podstawie umowy z klientem (dostawa, usługa) | b) — wykonanie umowy | art. 6 ust. 1 lit. b |
| Czynności przed zawarciem umowy na żądanie osoby (np. wyliczenie oferty) | b) — czynności przed zawarciem umowy | art. 6 ust. 1 lit. b |
| Wystawienie faktury, księgowość, podatki | c) — obowiązek prawny | art. 6 ust. 1 lit. c + ustawa o VAT / CIT / PIT |
| ZUS, kadry, wynagrodzenia | c) | art. 6 ust. 1 lit. c + KP + ustawa o systemie ubezpieczeń społecznych |
| Marketing dotychczasowych klientów (własne produkty podobne) | f) — uzasadniony interes | art. 6 ust. 1 lit. f |
| Marketing nowych klientów (elektroniczny — e-mail, SMS) | a) — zgoda + ePrivacy (art. 10 ustawy o świadczeniu usług drogą elektroniczną, art. 172 Prawa telekomunikacyjnego) | art. 6 ust. 1 lit. a |
| Dochodzenie roszczeń, odpowiedzialność, ochrona prawna | f) | art. 6 ust. 1 lit. f |
| Monitoring wizyjny w zakładzie pracy | f) + KP art. 22² | art. 6 ust. 1 lit. f |
| Profilowanie kredytowe | b) lub c) (Prawo bankowe) | art. 6 ust. 1 lit. b / c |
| Dane zdrowotne pacjenta | h) z art. 9 ust. 2 — cele zdrowotne + art. 9 ust. 3 | art. 9 ust. 2 lit. h + art. 9 ust. 3 |

**Zasada:** wybierać **najniższą ingerencyjną** podstawę. Zgoda — tylko dla tego, gdzie inne podstawy nie pasują; zgoda wymaga dobrowolności (nie wymuszona, możliwa do odwołania).

## Art. 9 — dane szczególnych kategorii

Dane ujawniające:
- Pochodzenie rasowe / etniczne.
- Poglądy polityczne, przekonania religijne / światopoglądowe.
- Członkostwo związkowe.
- **Dane genetyczne, biometryczne** (w celu jednoznacznej identyfikacji).
- **Dane o zdrowiu, seksualności, orientacji seksualnej**.

**Podstawy art. 9 ust. 2:**
- a) wyraźna zgoda.
- b) obowiązki prawne z zakresu prawa pracy, zabezpieczenia społecznego.
- c) żywotne interesy osoby niezdolnej do wyrażenia zgody.
- d) podmioty nienastawione na zysk (polityczne, światopoglądowe, religijne, związki zawodowe).
- e) oczywiście upublicznione przez osobę.
- f) dochodzenie roszczeń przed sądem.
- g) ważne interesy publiczne.
- h) cele zdrowotne (diagnoza, opieka, leczenie, zarządzanie systemami zdrowia).
- i) zdrowie publiczne, transgraniczne zagrożenia.
- j) cele archiwalne, naukowe, historyczne, statystyczne.

## Prawa osoby — terminy i zakres

| Prawo | Art. RODO | Termin |
|---|---|---|
| Dostęp do danych + kopia | 15 | 1 miesiąc (max 2 miesiące w skomplikowanych) |
| Sprostowanie | 16 | 1 miesiąc |
| Usunięcie („zapomnienie") | 17 | 1 miesiąc |
| Ograniczenie przetwarzania | 18 | 1 miesiąc |
| Przenoszenie danych | 20 | 1 miesiąc |
| Sprzeciw (art. 6 lit. e/f) | 21 | 1 miesiąc; zaprzestać, chyba że nadrzędne uzasadnione podstawy |
| Sprzeciw (marketing) | 21 ust. 3 | Natychmiast, bez wyważania |
| Niepodleganie decyzji zautomatyzowanej | 22 | Co do zasady — nie mieć takiej decyzji |

**Forma odpowiedzi:** pisemna (e-mail dopuszczalny), zrozumiała, bezpłatna. Żądanie nieuzasadnione / powtarzające się — administrator może odmówić lub naliczyć opłatę.

## Klauzula informacyjna — checklist (art. 13 lub 14)

| Element | Art. 13 (dane od osoby) | Art. 14 (inne źródła) |
|---|---|---|
| Administrator | ✓ | ✓ |
| IOD (jeśli wyznaczony) | ✓ | ✓ |
| Cele + podstawa | ✓ | ✓ |
| Uzasadniony interes (jeśli podstawa f) | ✓ | ✓ |
| Odbiorcy | ✓ | ✓ |
| Transfer do państw 3. | ✓ | ✓ |
| Okres przechowywania | ✓ | ✓ |
| Prawa | ✓ | ✓ |
| Prawo wycofania zgody (jeśli zgoda) | ✓ | ✓ |
| Prawo skargi do PUODO | ✓ | ✓ |
| Obowiązkowy / dobrowolny charakter podania | ✓ | — |
| Zautomatyzowane decyzje | ✓ | ✓ |
| **Źródło danych** | — | ✓ (jeśli nie z publicznego źródła) |
| Termin przekazania informacji | Przy zbieraniu | W 1 miesiącu od pozyskania, max przy pierwszym kontakcie, max przy ujawnieniu innemu odbiorcy |

## Umowa powierzenia (art. 28) — elementy obowiązkowe

1. Przedmiot, czas, charakter, cel, rodzaj danych, kategorie osób.
2. Obowiązki procesora (art. 28 ust. 3 lit. a-h):
   - a) Przetwarzanie wyłącznie na udokumentowane polecenie administratora.
   - b) Tajemnica.
   - c) Środki bezpieczeństwa (art. 32).
   - d) Subprocesorzy — warunki.
   - e) Pomoc w prawach osób (art. 15-22).
   - f) Pomoc w obowiązkach administratora (art. 32-36).
   - g) Zwrot / usunięcie danych po zakończeniu.
   - h) Udostępnianie informacji + umożliwienie audytów.
3. Prawa administratora (inspekcje, audyty).
4. Odpowiedzialność.
5. Warunki rozwiązania.

## DPIA — kiedy jest obowiązkowa (art. 35 ust. 3)

- Systematyczna, kompleksowa ocena osobowa + decyzje (profilowanie z konsekwencjami).
- Duża skala przetwarzania danych szczególnych (art. 9) lub danych karnych (art. 10).
- Systematyczny monitoring na dużą skalę miejsc publicznych.
- **Komunikat PUODO z 17.06.2019** — lista operacji wymagających DPIA (np. duża skala danych zdrowotnych, geolokalizacji, biometrii).

## Naruszenia — 3 kroki

1. **Stwierdzenie** — rejestr wewnętrzny (art. 33 ust. 5 RODO) — wszystkie naruszenia, niezależnie od ryzyka.
2. **Ocena ryzyka:**
   - Mało prawdopodobne → bez zgłoszenia PUODO.
   - Ryzyko → zgłoszenie do PUODO w 72 h (art. 33).
   - Wysokie ryzyko → dodatkowo zawiadomienie osób (art. 34).
3. **Zgłoszenie:**
   - Formularz na uodo.gov.pl (lub e-PUAP).
   - Treść: charakter, kategorie osób, liczba, konsekwencje, środki zaradcze.

**72 godziny** — od stwierdzenia. Po 72 h można, z uzasadnieniem opóźnienia.

## Transfery — decyzja o adekwatności lub SCC

**Państwa z decyzją adekwatności** (stan na 2026-04):
- UK (Decyzja 2021/1772; weryfikować termin obowiązywania i ewentualne przedłużenia).
- Szwajcaria, Japonia, Izrael, Korea Płd., Kanada (prywatny sektor), Argentyna, Nowa Zelandia, Andora, Urugwaj, Wyspa Man, Guernsey, Jersey, Wyspy Owcze.
- **USA** — EU-US Data Privacy Framework (Decyzja 2023/1795 z 10.07.2023). Firmy certyfikowane — transfer dopuszczalny bez dodatkowych zabezpieczeń.

**Bez adekwatności** — SCC (Rozp. 2021/914). Po *Schrems II* (C-311/18) wymagany **TIA** (Transfer Impact Assessment):
1. Ocena prawa państwa docelowego (inwigilacja, dostęp władz).
2. Ocena, czy SCC + dodatkowe zabezpieczenia zapewnią ochronę równoważną.
3. Zawieszenie transferu, jeżeli nie.

## UODO — szczególne krajowe

- **Wiek zgody dzieci** (art. 4 UODO w zw. z art. 8 RODO): **16 lat** (Polska pierwotnie 16; zweryfikować aktualne brzmienie — przepisy zmieniano).
- **Zadośćuczynienie** (art. 92 UODO): roszczenie cywilne — sąd cywilny, od sprawcy naruszenia. Dochodzone obok / zamiast skargi do PUODO.
- **Kary** (art. 101-104 UODO): PUODO wydaje decyzję; skarga do WSA w Warszawie.
- **IOD** (art. 8-11 UODO): zgłoszenie do PUODO w 14 dni.
- **Prawo pracy** (KP art. 22¹-22⁴): dane osobowe pracownika ograniczone do wyliczonych w art. 22¹ KP; monitoring — art. 22² KP.

## Cytowanie

- **Artykuł RODO:** art. [nr] [ust. / lit.] rozp. 2016/679 (RODO).
- **Artykuł UODO:** art. [nr] ustawy z 10.05.2018 o ochronie danych osobowych.
- **Wyrok TSUE:** wyrok TSUE z [data] w sprawie C-[nr]/[rok] *[tytuł]*, ECLI:EU:C:[rok]:[nr].
- **Decyzja PUODO:** decyzja Prezesa UODO z [data], znak: [znak], dostępna: [URL na uodo.gov.pl].
- **Wytyczne EDPB:** Guidelines [nr]/[rok] on [temat], adopted on [data], [URL].

## Najczęstsze błędy

- **Zgoda na wszystko jako podstawa przetwarzania.** Zgoda musi być dobrowolna — w relacji klient / usługodawca zwykle jest; ale jeżeli usługa jest niemożliwa bez przetwarzania (np. faktura), podstawą jest **umowa / obowiązek prawny**, nie zgoda.
- **Pomijanie marketingu elektronicznego przez ePrivacy.** Dla e-mail marketingu — dwa poziomy: art. 10 ustawy o świadczeniu usług drogą elektroniczną (wymaga zgody) + art. 172 Prawa telekomunikacyjnego (wymaga zgody). RODO jest **dodatkowa**, nie zastępuje tych ustaw.
- **Klauzule informacyjne bez elementów obowiązkowych.** Pominięcie np. okresu przechowywania, kontaktu do IOD, prawa skargi do PUODO = naruszenie.
- **Brak umów powierzenia.** Każdy dostawca IT, księgowości, chmury, mailingu = powierzenie. Bez umowy — oba podmioty są administratorami = podwójna odpowiedzialność.
- **Traktowanie cookies wyłącznie jako RODO.** Prawo telekomunikacyjne art. 173 — zgoda na cookies analityczne / marketingowe (opt-in). Cookie banner z „akceptuj wszystkie" domyślnie = naruszenie.
- **Zgłoszenie naruszenia po 72 h bez uzasadnienia.** Spóźnienie = powód zaostrzenia kary (decyzja PUODO z 10.09.2019 przeciwko MorelePL — 2,8 mln zł).
- **DPIA pisana „na potem".** DPIA powinna poprzedzać przetwarzanie. Pisanie po fakcie = brak rozliczalności.
- **Transfer bez TIA.** SCC same w sobie nie wystarczą (*Schrems II*); bez TIA — ryzyko podniesienia zarzutu podczas kontroli PUODO.
- **Pomijanie obowiązku informacyjnego przy zbieraniu od osoby trzeciej** (art. 14). Np. zakup bazy kontaktów B2B — obowiązek informacyjny wobec każdej osoby w ciągu 1 miesiąca.
- **Niewystarczające zabezpieczenia techniczne (art. 32).** „Rozsądne" nie wystarczy — trzeba udokumentować ocenę ryzyk i dobrane środki (szyfrowanie, MFA, kopie zapasowe, DLP, audyty).
- **Mylenie administratora z procesorem.** Administrator **decyduje** o celach i sposobach przetwarzania; procesor — przetwarza na polecenie. Dostawca CRM = zwykle procesor. Dostawca marketingu masowego = czasem administrator (własna baza, własne cele). Błędna kwalifikacja = niepoprawne umowy.
