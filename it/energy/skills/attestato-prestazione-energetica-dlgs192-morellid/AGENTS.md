# AGENTS.md - attestato-prestazione-energetica-dlgs192

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale agli **obblighi relativi all'attestato di prestazione energetica (APE)**:
quando e' dovuto e chi lo produce, dotazione e consegna, clausola nel contratto e allegazione,
annuncio commerciale, validita', affissione negli edifici pubblici e sanzioni, secondo gli
**artt. 6 e 15 del D.Lgs. 19 agosto 2005, n. 192**. Target: ingegneri, tecnici, proprietari,
agenzie.

**E' una skill documentale**: inquadra obblighi/soggetti/sanzioni; **non calcola, non redige e
non certifica** l'APE, non applica le sanzioni.

## Nota sull'area e sulla complementarita'

Area **energia-incentivi**. Complementare e distinta da `trasmittanza-termica-opache-dm2015`
(involucro), `diagnosi-energetica-dlgs102` (diagnosi imprese) e
`esercizio-controllo-impianti-termici-dpr74` (esercizio impianti): questa copre l'**APE**
(dotazione/obblighi/sanzioni), non il calcolo energetico.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-192-2005-artt-6-15**: D.Lgs. 19 agosto 2005, n. 192, pagina indice Normattiva pinnata
  a `!vig=2026-07-16` (hash `d7a39f3b...`; codice 005G0219). Artt. 6 (idGruppo 1, v9) e 15
  (idGruppo 3, v4) caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/dlgs-192-2005-artt-6-15.md`; estratto operativo in
`references/estratti/ape-checklist.md`.

## Punti chiave (verificati sul testo)

- **Quando** (art. 6 c. 1-2): edifici costruiti/venduti/locati; nuovi/ristrutturazioni importanti
  **prima dell'agibilita'**; dotazione costruttore/proprietario; disponibilita' all'avvio
  trattative e consegna al termine; **15 giorni** per vendita/locazione prima della costruzione.
- **Clausola** (c. 3): allegazione dell'APE; sanzione **3.000-18.000** (singole locazioni
  **1.000-4.000**, meta' se <= 3 anni).
- **Validita' 10 anni** (c. 5); **affissione** edifici PA > 500 (poi 250) m² (c. 6-7); **annuncio**
  con indici e classe (c. 8).
- **Sanzioni** (art. 15): professionista **700-4200** (c. 3); mancata dotazione nuovi/vendita
  **3.000-18.000** (c. 7-8); locazione **300-1.800** (c. 9); annuncio **500-3.000** (c. 10).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare/redigere/certificare** l'APE ne' riprodurre le metodologie (DM 26/6/2015,
  UNI/TS 11300): rinviarvi.
- Non inventare **soglie/importi** non presenti nel testo: usare i valori verbatim degli artt. 6/15.
- Non applicare le sanzioni (competenza di regioni/comuni).

### Cosa fare
- Stabilire se l'APE e' **dovuto** (nuovo/vendita/locazione), **chi** lo produce, i **tempi** e
  gli **adempimenti** (dotazione, consegna, clausola, annuncio); individuare la **sanzione**.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 192/2005 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere artt. 6/15, verificando le modifiche (il decreto e' molto modificato; L. 90/2013,
D.Lgs. 48/2020; blocchi (( )) e commi abrogati).

## Validatori

- Non ancora assegnato (Livello 2 con certificatore energetico / esperto EPBD).

## Stato attuale

- Versione: 0.1.0-alpha (closes #274)
- Task files: 2 (`verifica-obbligo-ape.md`, `inquadra-sanzioni-ape.md`)
- Esempi: 2 (vendita di appartamento senza APE; annuncio immobiliare senza classe energetica)
