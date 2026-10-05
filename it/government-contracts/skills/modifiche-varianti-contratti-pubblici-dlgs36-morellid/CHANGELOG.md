# CHANGELOG - modifiche-varianti-contratti-pubblici-dlgs36

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #273)
- Prima versione della skill di supporto alla **modifica dei contratti pubblici in corso di
  esecuzione** e alle **varianti in corso d'opera**, ai sensi dell'**art. 120 del D.Lgs. 31
  marzo 2023, n. 36** (Codice dei contratti pubblici), nell'area `appalti-opere-pubbliche`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 31 marzo 2023, n. 36** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 8d14a74fbded95d0255f100c23197e61ac5803156320fd5a3b5f142c17e83bc9
    (codice 23G00044). Art. 120 via `caricaArticolo` (versione 2, idGruppo 18).
  - Trascrizione verbatim in `references/fonti/dlgs-36-2023-art120.md`: art. 120 per intero
    (commi 1-15-bis).
- Estratto operativo `references/estratti/modifiche-varianti-checklist.md`.
- Due task: `qualifica-modifica-contratto.md` e `imposta-variante-corso-opera.md`.
- Due esempi: rinvenimento imprevisto -> variante in corso d'opera (c. 1 lett. c); opzione di
  proroga prevista in gara (c. 10).

### Contenuto ancorato al testo
- Casi senza nuova procedura (c. 1 a-d), limiti 50% (c. 2) e sotto soglia 10%/15% (c. 3),
  modifica sostanziale (c. 6) e non sostanziale (c. 5, 7), rinegoziazione RUP entro 3 mesi
  (c. 8), quinto d'obbligo (c. 9), proroghe (c. 10-11), autorizzazione del RUP e avviso GUUE
  (c. 13-14), oneri di comunicazione/trasmissione all'ANAC e sanzioni ex art. 222 (c. 15),
  verifica errori/omissioni progettuali (c. 15-bis).

### Scope e limiti
- Non approva modifiche/varianti ne' ne attesta la legittimita'. Non riproduce gli allegati
  richiamati (II.14, II.16) ne' gli articoli collegati (art. 60, 14, 222, 41 c. 8-bis). Non
  tratta il subappalto (art. 119) ne' la fase di gara. Non sostituisce stazione appaltante,
  RUP ne' ANAC.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 36/2023 pinnato (nuovo
  hash) e verificare le modifiche dei decreti correttivi (es. D.Lgs. 209/2024) segnalate dai
  doppi tondi `(( ))` nel testo.
- Validazione Livello 2 con esperto di contrattualistica pubblica / RUP.
