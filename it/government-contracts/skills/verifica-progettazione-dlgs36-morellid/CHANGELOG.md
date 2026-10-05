# CHANGELOG - verifica-progettazione-dlgs36

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #362)
- Prima versione della skill di supporto al **RUP**, al **soggetto verificatore** e al **progettista**
  per la **verifica della progettazione** e la **validazione** del progetto a base di gara, ai sensi del
  **D.Lgs. 31 marzo 2023, n. 36, art. 42**, nell'area `appalti-opere-pubbliche`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 36/2023** - indice Normattiva pinnato `!vig=2026-07-17` SHA256:
    0e9a193836e379cb33cb6daf1a5a988c608eb9559d84b91a841d9ed9791a62af (codice 23G00044, idGruppo 5).
    Art. 42 (versione 1) via `caricaArticolo` (formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-36-2023-art-42.md` (art. 42, commi 1-5).
- Estratto operativo `references/estratti/verifica-progettazione-checklist.md`.
- Due task: `inquadra-verifica-progetto.md` e `inquadra-validazione-effetti.md`.
- Due esempi: appalto integrato (tempi di verifica di PFTE/esecutivo, soggetti e incompatibilita');
  verifica positiva (assolvimento sismico, Archivio OO.PP., validazione).

### Contenuto ancorato al testo
- Oggetto della verifica - rispondenza al documento d'indirizzo e conformita' alla normativa - e tempi
  in relazione al livello, con regole per affidamento congiunto e PPP (c. 1); ruolo del RUP e
  incompatibilita' con progettazione, coordinamento sicurezza, direzione lavori e collaudo (c. 2);
  effetti della verifica positiva - assolvimento di deposito/autorizzazione sismica e denuncia al genio
  civile, deposito nell'Archivio informatico nazionale delle opere pubbliche (c. 3); validazione come
  atto formale del RUP con riferimento al rapporto e alle controdeduzioni, estremi nel bando/lettera
  d'invito (c. 4); rinvio all'Allegato I.7 per contenuti, modalita' e soggetti e oneri nelle risorse
  dell'opera (c. 5).

### Scope e limiti
- Non esegue la verifica ne' redige il rapporto o l'atto di validazione, non riproduce l'Allegato I.7
  (soglie di importo e soggetti verificatori) ne' gli obblighi sismici del DPR 380. Non sostituisce il
  RUP, il soggetto verificatore ne' il progettista.

### Note di sviluppo
- Distinta da `collaudo-verifica-conformita-dlgs36` (verifica in esecuzione) e `pfte-allegato-i7-checker`
  (contenuti PFTE). Verificare periodicamente l'aggiornamento dell'art. 42 (es. correttivo D.Lgs.
  209/2024) e dell'Allegato I.7. Validazione Livello 2 con RUP/esperto di verifica progetti.
