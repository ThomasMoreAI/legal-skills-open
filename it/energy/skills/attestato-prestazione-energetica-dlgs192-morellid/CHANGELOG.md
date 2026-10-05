# CHANGELOG - attestato-prestazione-energetica-dlgs192

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #274)
- Prima versione della skill di supporto agli **obblighi dell'attestato di prestazione
  energetica (APE)**, ai sensi degli **artt. 6 e 15 del D.Lgs. 19 agosto 2005, n. 192**,
  nell'area `energia-incentivi`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 19 agosto 2005, n. 192** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: d7a39f3b08f8f9ae71fdbe2737ae57953cc8beec2b8c18000b0c8b61614f21a8
    (codice 005G0219). Artt. 6 e 15 via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dlgs-192-2005-artt-6-15.md`: artt. 6 e 15 per
    intero (testo vigente, con i blocchi (( )) dei provvedimenti successivi).
- Estratto operativo `references/estratti/ape-checklist.md`.
- Due task: `verifica-obbligo-ape.md` e `inquadra-sanzioni-ape.md`.
- Due esempi: vendita di appartamento senza APE; annuncio immobiliare senza classe energetica.

### Contenuto ancorato al testo
- Art. 6: quando l'APE e' dovuto (c. 1-2), clausola/allegazione con sanzioni (c. 3), validita'
  10 anni e decadenza (c. 5), affissione edifici PA (c. 6-7), annuncio commerciale (c. 8),
  esonero se APE gia' valido (c. 10), contenuti e sistema informativo/catasto (c. 12).
- Art. 15: DSAN ex DPR 445/2000 (c. 1-2); professionista senza criteri 700-4200 (c. 3);
  mancata dotazione nuovi/vendita 3.000-18.000 (c. 7-8); locazione 300-1.800 (c. 9); annuncio
  senza parametri 500-3.000 (c. 10).

### Scope e limiti
- Non calcola, non redige e non certifica l'APE (tecnico abilitato). Non riproduce le
  metodologie/modelli (DM 26/6/2015 Linee guida APE; UNI/TS 11300): rinvio. Non applica le
  sanzioni (regioni/comuni). Non tratta i requisiti minimi (art. 3-4) ne' la relazione tecnica
  (art. 8) se non come richiamo.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 192/2005 pinnato (nuovo
  hash) e verificare le modifiche (L. 90/2013, D.Lgs. 48/2020; blocchi (( )), commi abrogati).
- Validazione Livello 2 con certificatore energetico / esperto EPBD.
