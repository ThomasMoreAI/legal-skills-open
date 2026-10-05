# CHANGELOG - subappalto-contratti-pubblici-dlgs36

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #265)
- Prima versione della skill di supporto alla **disciplina del subappalto** nei **contratti
  pubblici**, ai sensi dell'**art. 119 del D.Lgs. 31 marzo 2023, n. 36** (Codice dei contratti
  pubblici), nell'area `appalti-opere-pubbliche`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 31 marzo 2023, n. 36** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 8d14a74fbded95d0255f100c23197e61ac5803156320fd5a3b5f142c17e83bc9
    (codice 23G00044). Art. 119 via `caricaArticolo` (versione 2, idGruppo 18).
  - Trascrizione verbatim in `references/fonti/dlgs-36-2023-art119.md`: art. 119 per intero
    (commi 1-20).
- Estratto operativo `references/estratti/subappalto-checklist.md`.
- Due task: `qualifica-subappalto.md` e `imposta-autorizzazione-subappalto.md`.
- Due esempi: nolo a caldo sotto soglia (non-subappalto da comunicare); subappalto di
  lavorazioni con pagamento diretto a PMI.

### Contenuto ancorato al testo
- Nozione e soglie (c. 2: > 2% / > 100.000 euro / manodopera > 50%), attivita' non
  configuranti subappalto (c. 3), condizioni (c. 4), trasmissione 20 giorni prima (c. 5),
  responsabilita' solidale (c. 6-7), pagamento diretto (c. 11), tutele e CCNL (c. 12),
  autorizzazione a 30 giorni con silenzio-assenso e termini dimezzati sotto soglia (c. 16),
  subappalto a cascata (c. 17).

### Scope e limiti
- Non rilascia l'autorizzazione, non verifica i requisiti del subappaltatore, non sostituisce
  la stazione appaltante ne' il RUP. Non riproduce gli articoli richiamati dall'art. 119
  (artt. 100, 103, 11, 120, allegato II.2-bis, cause di esclusione) ne' la fase di gara.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 36/2023 pinnato (nuovo
  hash) e verificare le modifiche dei decreti correttivi (es. D.Lgs. 209/2024) segnalate dai
  doppi tondi `(( ))` nel testo.
- Validazione Livello 2 con esperto di contrattualistica pubblica / RUP.
