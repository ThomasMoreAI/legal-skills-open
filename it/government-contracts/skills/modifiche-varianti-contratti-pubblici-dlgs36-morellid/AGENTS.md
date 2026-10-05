# AGENTS.md - modifiche-varianti-contratti-pubblici-dlgs36

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **modifica dei contratti pubblici in corso di esecuzione** e alle
**varianti in corso d'opera**: casi ammessi senza nuova procedura, limiti economici, modifica
sostanziale/non sostanziale, quinto d'obbligo, proroghe, autorizzazione del RUP e oneri verso
l'ANAC, secondo l'**art. 120 del D.Lgs. 31 marzo 2023, n. 36**. Target: ingegneri, RUP, stazioni
appaltanti, operatori economici.

**E' una skill documentale**: inquadra casi/limiti/procedura; **non approva** modifiche/varianti,
non ne attesta la legittimita', non sostituisce stazione appaltante, RUP ne' ANAC.

## Nota sull'area e sulla complementarita'

Area **appalti-opere-pubbliche**. Complementare e distinta da `subappalto-contratti-pubblici-dlgs36`
(art. 119) e dalle skill di gara (`bandi-tipo-anac-checker`, `oepv-valutatore-offerte-tecniche`,
`specifiche-tecniche-ict-appalti-dlgs36`): questa copre le **modifiche/varianti** in fase esecutiva.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-36-2023-art120**: D.Lgs. 31 marzo 2023, n. 36, pagina indice Normattiva pinnata a
  `!vig=2026-07-16` (hash `8d14a74f...`; codice 23G00044). Art. 120 (versione 2, idGruppo 18)
  caricato via `caricaArticolo` e trascritto verbatim. Stesso atto dell'art. 119 (subappalto).

Trascrizione in `references/fonti/dlgs-36-2023-art120.md`; estratto operativo in
`references/estratti/modifiche-varianti-checklist.md`.

## Punti chiave (verificati sul testo)

- **Casi senza nuova procedura** (c. 1 a-d): clausole di revisione/opzione; supplementari;
  varianti per circostanze imprevedibili (disposizioni sopravvenute, forza maggiore,
  rinvenimenti, difficolta' geologiche/idriche); sostituzione del contraente.
- **Limiti**: **50%** per b)/c) (c. 2); sotto **soglia art. 14** e **10%/15%** (c. 3).
- **Sostanziale** (c. 6) vs **non sostanziale** (c. 5, 7).
- **Rinegoziazione** RUP entro **3 mesi** (c. 8); **quinto d'obbligo** (c. 9); **proroghe** (c. 10-11).
- **Autorizzazione del RUP** e **avviso GUUE** (c. 13-14); **oneri ANAC** e sanzioni art. 222 (c. 15).

## Convenzioni specifiche

### Cosa NON fare
- Non **approvare** modifiche/varianti ne' attestarne la legittimita'.
- Non riprodurre gli **allegati** (II.14, II.16) ne' gli articoli richiamati (60, 14, 222, 41 c. 8-bis).
- Non trattare il **subappalto** (art. 119) ne' la fase di gara.

### Cosa fare
- Qualificare la modifica (caso c. 1, limiti, sostanziale/no) e impostare il procedimento
  (quinto d'obbligo, autorizzazione RUP, avviso GUUE, oneri ANAC).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 36/2023 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere l'art. 120, verificando le modifiche dei **decreti correttivi** (es. D.Lgs. 209/2024)
segnalate dai doppi tondi `(( ))`.

## Validatori

- Non ancora assegnato (Livello 2 con esperto di contrattualistica pubblica / RUP).

## Stato attuale

- Versione: 0.1.0-alpha (closes #273)
- Task files: 2 (`qualifica-modifica-contratto.md`, `imposta-variante-corso-opera.md`)
- Esempi: 2 (rinvenimento archeologico -> variante lett. c; opzione di proroga prevista in gara)
