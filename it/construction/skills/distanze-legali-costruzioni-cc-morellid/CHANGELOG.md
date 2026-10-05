# CHANGELOG - distanze-legali-costruzioni-cc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #261)
- Prima versione della skill di supporto alle **distanze legali nelle costruzioni** e alla
  disciplina delle **luci e vedute** del **Codice civile** (artt. 873-907), nell'area
  `edilizia-urbanistica-catasto`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **Codice civile (R.D. 16 marzo 1942, n. 262)** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 390892173cda82d76151571464a5288deca18ecf1fc1d56c6eebb3753e788cf5 (codice 042U0262).
    Artt. 873, 877, 878, 879, 889, 890, 892, 905, 906, 907 (testo vigente) via `caricaArticolo`,
    trascritti verbatim in `references/fonti/cc-distanze-873-907.md`.
- Estratto operativo `references/estratti/distanze-costruzioni-checklist.md`.
- Due task: `verifica-distanze-costruzioni.md` e `verifica-luci-vedute.md`.
- Due esempi: nuova costruzione presso il confine (art. 873 + coordinamento DM 1444/1968); finestra
  e vedute (artt. 905-907).

### Contenuto ancorato al testo
- Distanza 3 m tra costruzioni (art. 873), muro di cinta (art. 878), aderenza/confine (art. 877),
  esenzioni (art. 879); pozzi 2 m e tubi 1 m (art. 889), depositi nocivi/pericolosi (art. 890);
  alberi 3/1,5/0,5 m con eccezioni (art. 892); vedute dirette 1,5 m (art. 905), oblique 0,75 m
  (art. 906), costruzioni a 3 m dalle vedute acquisite (art. 907).

### Scope e limiti
- Le distanze civilistiche sono **minimi derogabili in aumento** dai regolamenti locali e vanno
  coordinate con il **DM 1444/1968 art. 9** (distanze tra pareti finestrate), non riprodotto. La
  skill non risolve il caso concreto, non misura in sito e non sostituisce il tecnico/consulente
  legale (servitu', usucapione della veduta, comunione del muro, prevenzione).

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del Codice civile pinnato (nuovo hash) e
  rileggere gli articoli; verificare il coordinamento con il DM 1444/1968 e la giurisprudenza.
- Validazione Livello 2 con avvocato civilista / CTU esperto di distanze.
