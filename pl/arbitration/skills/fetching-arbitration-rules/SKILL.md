---
name: fetching-arbitration-rules
title: fetching-arbitration-rules
description: Use when retrieving arbitration institutional rules (SAKIG przy KIG, Sąd Arbitrażowy Lewiatan, ICC, LCIA, SCC, SIAC, HKIAC, VIAC, UNCITRAL) — fetching current version, verifying redaction applicable to the date of arbitration agreement, constructing URLs for official rule texts
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/plugins/pl/skills/fetching-arbitration-rules
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: arbitration
language: pl
---

# fetching-arbitration-rules

Regulaminy sądów arbitrażowych i instytucji administrujących są okresowo nowelizowane (ICC — 2012/2017/2021; LCIA — 1998/2014/2020; SCC — 2017/2023; SIAC — 2013/2016/2025; HKIAC — 2013/2018/2024; SAKIG — 2015/2025). Różne wersje odmiennie regulują konsolidację, emergency arbitrator, expedited procedure, early dismissal, third-party funding — cytowanie bez wskazania roku redakcji nie ma wartości dowodowej. W sprawach z polskim elementem najczęściej w grze są: SAKIG przy KIG, Sąd Arbitrażowy Lewiatan, a spośród zagranicznych — ICC, LCIA, SCC, VIAC; dla ad hoc — UNCITRAL Arbitration Rules.

## URL patterns (zweryfikowano 2026-04-20)

| Instytucja | Obowiązujący regulamin | URL | Data redakcji |
|---|---|---|---|
| Sąd Arbitrażowy przy KIG (SAKIG) | Regulamin SAKIG | `https://sakig.pl/regulamin/` | Weryfikować aktualną edycję na stronie SAKIG |
| Sąd Arbitrażowy Lewiatan | Regulamin SA Lewiatan | `https://sadarbitrazowy.org.pl/regulamin/` | Weryfikować na stronie Konfederacji Lewiatan |
| Sąd Arbitrażowy przy SIDiR (FIDIC-adjacent) | Regulamin SA SIDiR | `https://sidir.pl/sad-arbitrazowy/` | Weryfikować na stronie SIDiR |
| ICC | 2021 ICC Rules of Arbitration | `https://iccwbo.org/dispute-resolution/dispute-resolution-services/arbitration/rules-procedure/2021-arbitration-rules/` | 01.01.2021 |
| LCIA | 2020 LCIA Arbitration Rules | `https://www.lcia.org/Dispute_Resolution_Services/lcia-arbitration-rules-2020.aspx` | 01.10.2020 |
| SCC Arbitration Institute | 2023 SCC Arbitration Rules | `https://sccarbitrationinstitute.se/en/scc-arbitration-rules-english-2023/` | 01.01.2023 |
| SIAC | SIAC Rules 2025 (7th edition) | `https://siac.org.sg/siac-rules-2025` | 01.01.2025 |
| HKIAC | 2024 HKIAC Administered Arbitration Rules | `https://hkiac.org/arbitration/rules-and-practice-notes/2024-administered-arbitration-rules/` | 01.06.2024 |
| VIAC | Vienna Rules (obowiązująca od 01.01.2025) | `https://www.viac.eu/en/arbitration-basics/arbitration-rules/` | 01.07.2021 (oryginał); obowiązująca — 01.01.2025 |
| UNCITRAL | UNCITRAL Arbitration Rules (1976 / 2010 / 2013 / 2021 Expedited) | `https://uncitral.un.org/en/texts/arbitration/contractualtexts/arbitration` | 2013 (podstawowy); 2021 (Expedited) |
| ICSID | ICSID Arbitration Rules 2022 | `https://icsid.worldbank.org/rules-regulations/convention/rules-procedure-arbitration-proceedings-arbitration-rules` | 01.07.2022 |

## Workflow

1. **Ustalić instytucję.** Źródło — zapis na sąd polubowny w umowie, Request for Arbitration, odpowiedź, terms of reference albo zarządzenie proceduralne. Jeżeli zapis jest dwuznaczny (np. „Sąd Arbitrażowy przy Krajowej Izbie Gospodarczej" — bez doprecyzowania miasta; istnieją oddziały) — zweryfikować, która dokładnie organizacja administruje sprawę dzisiaj.
2. **Ustalić datę rozpoczęcia arbitrażu.** Wg większości regulaminów (ICC Art. 6(1), LCIA Art. 1, SIAC Rule 3, HKIAC Art. 4) obowiązuje wersja, która była w mocy na datę złożenia Request for Arbitration / Notice of Arbitration, jeżeli strony nie uzgodniły inaczej. To właśnie ta data, a nie data zapisu na sąd polubowny, decyduje o zastosowanej wersji.
3. **Zweryfikować przepisy przejściowe zapisu.** Niektóre zapisy fiksują konkretną wersję („w brzmieniu obowiązującym w dniu zawarcia Umowy" albo „z późniejszymi zmianami"); zapisana wersja ma pierwszeństwo przed domyślną.
4. **Fetch oficjalnej strony** przez WebFetch wg URL z tabeli. Sprawdzić w nagłówku strony lub preamble regulaminu: datę wejścia w życie, numer wersji, czy nie pojawiło się ogłoszenie o nowej wersji w przygotowaniu.
5. **Pobrać PDF regulaminu** z linku „Download" / „Rules (PDF)" na oficjalnej stronie — PDF jest authoritative text, wersja HTML często skrócona.
6. **Znaleźć konkretny artykuł/regułę** — wg numeru (Article / Rule / § / Paragraf). W SIAC i HKIAC numeracja — „Rule", w ICC/LCIA/SCC/VIAC — „Article", w SAKIG i Lewiatan — „§".
7. **Cytować** z obowiązkowym wskazaniem roku redakcji oraz, w razie potrzeby, daty weryfikacji.

## Wyszukiwanie wcześniejszych redakcji

- **ICC.** Archiwum poprzednich redakcji (1998, 2012, 2017) publikowane jest na iccwbo.org w dziale „Previous versions of the Arbitration Rules". W razie braku — przez `https://web.archive.org/web/*/iccwbo.org/*arbitration-rules*`.
- **LCIA.** 2014 LCIA Rules i 1998 LCIA Rules dostępne z działu „Historic LCIA Arbitration Rules" na lcia.org; PDF zwykle zachowane jako osobne dokumenty.
- **SCC.** Redakcje 2010 i 2017 — na sccarbitrationinstitute.se w dziale poprzednich wersji.
- **SIAC.** Redakcje 2013 i 2016 — na siac.org.sg w dziale Previous Rules; 6. edycja (2016) obowiązywała do 31.12.2024.
- **HKIAC.** 2013 i 2018 HKIAC Administered Arbitration Rules — na hkiac.org w dziale poprzednich redakcji.
- **VIAC.** Vienna Rules 2013, 2018, 2021 — na viac.eu; archiwalne redakcje PDF.
- **SAKIG.** Poprzednie redakcje — na sakig.pl, a dla starych (sprzed 2015 r.) — przez `https://web.archive.org/web/*/sakig.pl/*`. Weryfikować datę wejścia w życie tej konkretnej redakcji.
- **SA Lewiatan.** Poprzednie redakcje — na sadarbitrazowy.org.pl, w razie braku — web.archive.org.
- **UNCITRAL.** Oficjalne redakcje: 1976 (original), 2010 (revised), 2013 (z poprawkami pod Transparency Rules), 2021 (Expedited Rules jako uzupełnienie). Wszystkie dostępne na `uncitral.un.org` w dziale Arbitration.
- **Web Archive.** Dla każdej instytucji weryfikować datę cache (timestamp w URL archive.org) — tymczasowa redakcja może wyglądać jak finalna, jeżeli zrzut ekranu wykonano w okresie przejściowym.

## Format cytowania

Podstawowy szablon:

`<Artykuł/Article/Rule/§> <numer>(<ustęp>) of the <rok> <nazwa regulaminu> (URL, zweryfikowano <data>)`

Przykłady:

- § 19 Regulaminu Sądu Arbitrażowego przy KIG (w brzmieniu obowiązującym od [data]), `https://sakig.pl/regulamin/` (zweryfikowano 2026-04-20).
- § 4 Regulaminu Sądu Arbitrażowego Lewiatan (aktualne brzmienie).
- Art. 4(3) of the 2021 ICC Rules of Arbitration, `https://iccwbo.org/.../2021-arbitration-rules/`.
- Article 28 of the 2020 LCIA Arbitration Rules, `https://www.lcia.org/.../lcia-arbitration-rules-2020.aspx`.
- Article 8 of the 2023 SCC Arbitration Rules, `https://sccarbitrationinstitute.se/en/scc-arbitration-rules-english-2023/`.
- Rule 5 of the SIAC Rules 2025 (7th edition), `https://siac.org.sg/siac-rules-2025`.
- Article 28 of the 2024 HKIAC Administered Arbitration Rules, `https://hkiac.org/.../2024-administered-arbitration-rules/`.
- Article 45 of the Vienna Rules 2021 (as amended with effect from 01.01.2025), `https://www.viac.eu/en/arbitration-basics/arbitration-rules/`.
- Article 17 of the UNCITRAL Arbitration Rules (as revised in 2013), `https://uncitral.un.org/en/texts/arbitration/contractualtexts/arbitration`.

Dla dokumentów polskich — „§" / „art." / „ust." / „pkt"; dla angielskojęzycznych memorandów — „Article" / „Rule" / „§". Nazwa regulaminu — w języku dokumentu.

## Najczęstsze błędy

- **Cytat bez roku redakcji.** 2012 ICC Rules ≠ 2021 ICC Rules — różne zasady emergency arbitrator (pojawił się w 2012), konsolidacji (zaktualizowano w 2021, Art. 10), expedited procedure (wprowadzono w 2017, Art. 30 i Appendix VI), joinder of additional parties. Bez roku redakcji cytat nie ma wartości procesowej.
- **Poleganie na tabeli bez świeżej weryfikacji.** Tabela w tym skillu — punkt wyjścia; regulaminy są aktualizowane bez wcześniejszego ogłoszenia (SIAC przeszedł z 6. na 7. edycję od 01.01.2025; SCC zaktualizował regulamin w 2023; HKIAC — w 2024). Przed finalnym dokumentem — obowiązkowy WebFetch oficjalnej strony.
- **Mylenie UNCITRAL Rules z UNCITRAL Model Law on International Commercial Arbitration.** UNCITRAL Arbitration Rules — regulamin proceduralny dla ad hoc arbitrażu, stosowany za zgodą stron. UNCITRAL Model Law — wzór ustawodawstwa krajowego, zaimplementowany w KPC Część V (art. 1154–1217). Powoływanie się w memorandum procesowym na Model Law jako na Rules — rażący błąd.
- **Zastosowanie obecnego regulaminu do starego sporu.** Jeżeli Request for Arbitration złożony w 2018 r., dla ICC obowiązują 2017 Rules, nie 2021; dla LCIA — 2014 Rules, nie 2020; dla HKIAC — 2013 Rules, nie 2018 (jeżeli RfA przed 01.11.2018). Przejście na nową wersję bez zgody stron — podstawa do zaskarżenia wyroku.
- **Web Archive bez weryfikacji daty cache.** Timestamp w URL (`/web/20190315.../...`) pokazuje datę cache, a nie datę redakcji dokumentu. Czytać datę wejścia w życie na dole strony lub w preamble PDF, żeby nie wziąć tymczasowej redakcji (np. 2017 ICC Rules w cache 2019 r.) za redakcję obowiązującą w czasie sporu.
- **Używanie starego URL SAKIG (arbitraz.kig.pl).** Domena arbitraz.kig.pl przekierowuje do sakig.pl, ale oryginalne linki do dokumentów mogą wygasać. Sprawdzać zawsze sakig.pl jako źródło autorytatywne.
- **Mylenie SCC z innymi „SCC".** SCC Arbitration Institute w Sztokholmie (wcześniej — Arbitration Institute of the Stockholm Chamber of Commerce) — nie mylić ze Swiss Chambers' Arbitration Institution (SCAI, obecnie Swiss Arbitration Centre) ani z chińskim CIETAC. Własna strona — `sccarbitrationinstitute.se`.
- **Ignorowanie przepisów przejściowych w samym regulaminie.** Nowe redakcje zwykle zawierają osobny artykuł o stosowaniu w czasie (np. ICC 2021 Art. 6(1), SIAC 2025 Rule 1.3). Czytać go osobno — tam zapisane, kiedy stosuje się starą redakcję.
- **Mylenie SAKIG w Warszawie z Sądem Arbitrażowym przy Krajowej Izbie Gospodarczej w Krakowie lub Katowicach.** SAKIG w Warszawie (sakig.pl) — największy i domyślnie rozumiany. Regionalne izby mogą mieć własne sądy arbitrażowe — weryfikować konkretną klauzulę.
