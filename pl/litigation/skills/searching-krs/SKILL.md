---
name: searching-krs
title: searching-krs
description: Use when identifying Polish legal entities, verifying reprezentację (zarząd, pełnomocnictwa), adresy do doręczeń, postępowania upadłościowe / restrukturyzacyjne, sprawozdania finansowe — KRS dla spółek i stowarzyszeń, CEIDG dla JDG, KRD / BIG InfoMonitor, MSiG
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/plugins/pl/skills/searching-krs
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: litigation
language: pl
---

# searching-krs

Każdy pozew przeciwko osobie prawnej wymaga prawidłowego oznaczenia. Brak KRS / NIP, nieaktualny adres, błędne osoby reprezentujące — podstawa do zwrotu pozwu (art. 130 KPC) albo do nieważności postępowania. Ten skill wskazuje, gdzie szukać i czego używać w pozwach.

## Rejestry krajowe — przegląd

| Rejestr | Zakres | URL | Charakter |
|---|---|---|---|
| **KRS** (Krajowy Rejestr Sądowy) | Spółki handlowe, stowarzyszenia, fundacje, spółdzielnie, inne jednostki organizacyjne | `https://ekrs.ms.gov.pl` | Publiczny, bezpłatny |
| **CEIDG** (Centralna Ewidencja i Informacja o Działalności Gospodarczej) | Osoby fizyczne prowadzące działalność gospodarczą | `https://aplikacja.ceidg.gov.pl` | Publiczny, bezpłatny |
| **MSiG** (Monitor Sądowy i Gospodarczy) | Ogłoszenia sądowe i gospodarcze — upadłości, restrukturyzacje, likwidacje, wezwania wierzycieli | `https://ems.ms.gov.pl/msig` | Publiczny, bezpłatny |
| **KRD / BIG InfoMonitor / ERIF** | Dłużnicy (wpisywani przez wierzycieli); firmy i konsumenci | `https://krd.pl`, `https://big.pl`, `https://erif.pl` | Dostęp płatny; BIK dla kredytowej historii |
| **VAT-owcy** — biała lista | NIP czynnych podatników, rachunki bankowe | `https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka` | Publiczny, bezpłatny |
| **Rejestr Dłużników Alimentacyjnych** | Dłużnicy alimentacyjni > 6 miesięcy | `https://ekrd.pl` (MOPS) | Dostęp przez jednostki uprawnione |
| **REGON** | Baza statystyczna GUS | `https://wyszukiwarkaregon.stat.gov.pl` | Publiczny, bezpłatny |

## KRS — szczegółowo

### Typy wpisów

| Dział KRS | Przeznaczenie |
|---|---|
| Rejestr Przedsiębiorców | Spółki handlowe (z o.o., akcyjna, osobowe, europejskie), spółdzielnie, przedsiębiorstwa państwowe, oddziały zagranicznych przedsiębiorstw |
| Rejestr Stowarzyszeń i innych organizacji społecznych | Stowarzyszenia, fundacje, kluby sportowe, OPP |
| Rejestr Dłużników Niewypłacalnych | Wpisy o zaległościach (dodatkowy rejestr) |

### Informacje dostępne — bezpłatnie

- **Nazwa / firma.**
- **NIP / REGON / KRS.**
- **Siedziba i adres.**
- **Kapitał zakładowy** (dla spółek kapitałowych).
- **Dane wspólników** (dla sp. z o.o., komandytowej, jawnej).
- **Akcjonariusze** (dla S.A. — tylko posiadacze ≥ 5%).
- **Skład zarządu** — imiona, nazwiska, PESEL.
- **Prokurenci** (prokura łączna / samoistna).
- **Rada nadzorcza** (dla spółek).
- **Sposób reprezentacji** — kluczowe dla pozwów.
- **Otwarte postępowania** — upadłość, restrukturyzacja, likwidacja.
- **Sprawozdania finansowe** (w ostatnich latach wymagane elektronicznie).

### Wyszukiwanie

**Po nazwie:** `https://ekrs.ms.gov.pl/web/wyszukiwarka-krs/`.

**Po KRS:** wprowadzić 10-cyfrowy numer.

**Odpis aktualny** (bezpłatny PDF) — kliknąć „Pobierz odpis aktualny"; zawiera bieżący stan.

**Odpis pełny** (płatny) — cała historia wpisów (dla badania dziejów spółki); 60 zł za odpis pełny.

### Sposób reprezentacji — kluczowe dla pozwu

W pozwie **oznaczyć pozwanego wg sposobu reprezentacji z KRS**:

Przykład: `[Nazwa spółki] sp. z o.o. z siedzibą w Warszawie (00-001), ul. [X] [nr], KRS: 0000XXXXXXX, NIP: XXXXXXXXXX, REGON: XXXXXXXXX, reprezentowana przez [imię i nazwisko członka zarządu], [funkcja] — zgodnie z [sposób: samodzielnie / łącznie z drugim członkiem zarządu / łącznie z prokurentem]`.

**Błędy najczęstsze:**
- Pozew „przeciwko ABC sp. z o.o." bez KRS — ryzyko zwrotu.
- Błędny KRS — zwrot.
- Podanie osób, które już nie są w zarządzie (zmiany KRS odbywają się na bieżąco — weryfikować dzień wniesienia pozwu, nie sporządzania projektu).

### Postępowania — ostrzeżenia

**Kolumna „Postępowania":**
- **Upadłość** — pozew trzeba skierować do syndyka; część roszczeń zgłasza się do masy upadłości (art. 236 Prawa upadłościowego).
- **Restrukturyzacja** — zależnie od trybu (sanacja, przyspieszone postępowanie układowe, postępowanie układowe, postępowanie o zatwierdzenie układu) — ograniczenia w dochodzeniu roszczeń.
- **Likwidacja** — likwidator reprezentuje spółkę.

**Zawsze weryfikować** przed pozwem.

## CEIDG — osoby fizyczne prowadzące działalność gospodarczą

**Dane:**
- Imię i nazwisko.
- NIP, REGON.
- Adres do doręczeń (może być inny niż miejsce zamieszkania).
- Adres wykonywania działalności.
- Data rozpoczęcia, zawieszenia, zakończenia.
- Przedmiot działalności (PKD).

**Wyszukiwanie:** `https://aplikacja.ceidg.gov.pl`.

**Uwaga:** w pozwie przeciwko osobie fizycznej prowadzącej działalność — pozew kieruje się do **osoby fizycznej**, z dodatkowym oznaczeniem działalności gospodarczej:

`[Imię Nazwisko], PESEL: [XXXXXXXXXXX], prowadzący działalność gospodarczą pod firmą „[nazwa firmy]", NIP: [XXXXXXXXXX], zamieszkały [adres zamieszkania lub adres do doręczeń z CEIDG]`.

## Biała lista VAT — weryfikacja rachunków bankowych

`https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka/`.

**Informacje:**
- Status podatnika VAT (czynny / zwolniony / wykreślony).
- Rachunki bankowe zgłoszone do urzędu skarbowego.

**Znaczenie:**
- Dla B2B — przelew na rachunek spoza białej listy przy płatności > 15 000 zł → sankcje podatkowe (brak kosztów uzyskania; solidarna odpowiedzialność za VAT).
- Dla pozwu — weryfikacja, czy pozwany przedsiębiorca jest aktywnym podatnikiem VAT (wpływa na dochodzone kwoty netto / brutto).

## MSiG — ogłoszenia

`https://ems.ms.gov.pl/msig`.

**Kluczowe ogłoszenia dla wierzyciela:**
- Ogłoszenie o upadłości → zgłoszenie wierzytelności w 30 dni od ogłoszenia.
- Ogłoszenie o otwarciu postępowania restrukturyzacyjnego.
- Likwidacja spółki → wezwanie wierzycieli do zgłoszenia wierzytelności w 3 miesięcy.

**Pełnotekstowe** — bezpłatnie.

**Archiwum** — sięga do 2000 r.

## KRD / BIG / ERIF — dłużnicy

**Zakres:** wpisy dłużników (konsumentów, przedsiębiorców) przez wierzycieli.

**Wpis** możliwy:
- Konsument — długi ≥ 200 zł, wymagalne ≥ 60 dni, po wezwaniu do zapłaty z min. 30-dniowym terminem i informacją o wpisie (art. 21 ustawy o BIG).
- Przedsiębiorca — długi ≥ 500 zł, te same wymogi.

**Wyszukiwarka**:
- **KRD** (krd.pl) — największy; płatny dostęp.
- **BIG InfoMonitor** (big.pl) — dostęp dla abonentów.
- **ERIF** (erif.pl) — trzeci.

**Użyteczność dla pozwu:** weryfikacja innych zaległości pozwanego; argumentacja dla zabezpieczenia (ryzyko niewypłacalności).

## BIK (Biuro Informacji Kredytowej)

`https://www.bik.pl`.

**Zakres:** historia kredytowa osób fizycznych i firm. Dostęp głównie dla banków; konsument może pobrać **raport BIK o sobie**.

**Dla pozwu:** osoba trzecia nie może żądać raportu cudzego; zwykle wnioskować o udostępnienie przez sąd.

## Księgi wieczyste (KW)

`https://ekw.ms.gov.pl`.

**Dla pozwów o nieruchomości** — weryfikacja:
- Właściciela (lub użytkownika wieczystego).
- Obciążeń (hipoteka, służebność, prawo dożywocia).
- Ostrzeżenia o niezgodności.

**Numer KW** — format: WAxx/xxxxxxxx/x (np. WA1M/00012345/6).

## Workflow — przed pozwem przeciwko osobie prawnej

1. **Sprawdzić KRS** — odpis aktualny (bezpłatny PDF).
2. **Zapisać:** pełna nazwa, adres siedziby, KRS, NIP, REGON.
3. **Zweryfikować sposób reprezentacji** — kto i jak podpisuje za spółkę.
4. **Sprawdzić postępowania** — upadłość / restrukturyzacja.
5. **Białe listy VAT** — dla B2B, zwłaszcza przy większych transakcjach.
6. **KRD / BIG** — dla oceny wypłacalności i argumentacji zabezpieczenia.
7. **MSiG** — archiwalnie, dla upadłości / restrukturyzacji.

## Workflow — przed pozwem przeciwko osobie fizycznej prowadzącej działalność

1. **CEIDG** — aktualne dane, adres do doręczeń.
2. **Biała lista VAT** — jeżeli B2B.
3. **KRD / BIG** — wpisy.
4. **Ewentualnie** — księgi wieczyste, jeżeli pozew o nieruchomość.

## Workflow — przed pozwem przeciwko zagranicznej osobie prawnej

1. **Oddziały zagranicznego przedsiębiorstwa** — zwykle w KRS.
2. **Zagraniczne rejestry** — zależnie od państwa:
   - Niemcy: Handelsregister (handelsregister.de).
   - Wielka Brytania: Companies House.
   - USA — rejestry stanowe.
   - UE: BRIS (Business Registers Interconnection System) — `https://e-justice.europa.eu`.
3. **Pozew** — wymaga tłumaczenia + doręczenia wg Rozporządzenia 2020/1784 (wewnątrz UE) lub Konwencji Haskiej 1965 (poza UE).

## Najczęstsze błędy

- **Pozew przeciwko „firmie" bez KRS.** Zwrot pozwu (art. 130 KPC).
- **Nieaktualne dane z KRS.** Zmiany w zarządzie — bieżące. Weryfikować na dzień wniesienia, nie sporządzania.
- **Pomijanie sposobu reprezentacji.** Pozew podpisany przez „niewłaściwą" osobę — pozwany zakwestionuje.
- **Pomijanie postępowań.** Pozew przeciwko spółce w upadłości → nieskuteczny; wierzytelność zgłaszać do syndyka.
- **Mylenie osoby fizycznej prowadzącej działalność ze spółką.** JDG to **osoba fizyczna**; pozew na `[imię nazwisko], prowadzący działalność...`, nie na firmę jako osobę prawną.
- **Pomijanie białej listy VAT.** Przelew na konto spoza listy (B2B > 15 000 zł) — sankcje + ryzyko odpowiedzialności solidarnej.
- **Błędny adres do doręczeń.** W KRS i CEIDG można zmienić adres do doręczeń; używać aktualnego.
- **Pomijanie spółki w organizacji.** Spółka w organizacji (przed wpisem do KRS) ma własną podmiotowość — oznaczenie bez KRS, z danymi wspólników.
- **Spółka cywilna.** **Nie jest osobą prawną** — pozew przeciwko wszystkim wspólnikom osobno.
- **Wspólnik spółki osobowej.** W sp. jawnej, komandytowej — wspólnicy odpowiadają solidarnie za zobowiązania spółki (art. 22 KSH) — można pozywać spółkę + wspólników.
