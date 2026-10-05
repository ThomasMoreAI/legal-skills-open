# CHANGELOG - accertamento-tecnico-preventivo-cpc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #269)
- Prima versione della skill di supporto all'**istruzione preventiva** nel processo civile
  (accertamento tecnico preventivo e consulenza tecnica preventiva conciliativa), ai sensi
  degli **artt. 696 e 696-bis del Codice di procedura civile**, nell'area `forense`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **Codice di procedura civile (R.D. 1443/1940)** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 7a53e745448ed3657d629b49a9f4c2e18eb08bfaa19f55e815e046793788c655
    (codice 040U1443). Artt. 696 e 696-bis via `caricaArticolo` (idGruppo=118).
  - Trascrizione verbatim in `references/fonti/cpc-696-696bis.md`: art. 696 e art. 696-bis
    per intero (testo aggiornato alla riforma Cartabia, D.Lgs. 149/2022).
- Estratto operativo `references/estratti/atp-checklist.md`.
- Due task: `scegli-strumento-preventivo.md` e `imposta-procedimento-atp.md`.
- Due esempi: infiltrazioni (ATP conservativo art. 696); difetti in appalto privato (696-bis
  conciliativo).

### Contenuto ancorato al testo
- Art. 696: presupposto di urgenza, estensione a cause e danni (c. 2), nomina CTU (c. 3),
  sospensione fino al deposito CTU non oltre 6 mesi (c. 4), definizione e liquidazione (c. 5).
- Art. 696-bis: richiesta anche fuori urgenza per crediti da inadempimento/fatto illecito,
  tentativo di conciliazione, verbale con efficacia di titolo esecutivo esente da imposta di
  registro, acquisizione della relazione nel merito, richiamo artt. 191-197.

### Scope e limiti
- Non instaura il procedimento, non redige il ricorso ne' la relazione di merito, non fornisce
  il contenuto tecnico della consulenza (cfr. `relazione-peritale-ctu-cpc`). Non riproduce gli
  articoli richiamati (692-695, 191-197). Non sostituisce giudice, avvocato ne' CTU.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del c.p.c. pinnato (nuovo hash) e
  verificare le modifiche (riforma Cartabia e successive) segnalate dai doppi tondi `(( ))`.
- Validazione Livello 2 con avvocato/magistrato o CTU esperto di istruzione preventiva.
