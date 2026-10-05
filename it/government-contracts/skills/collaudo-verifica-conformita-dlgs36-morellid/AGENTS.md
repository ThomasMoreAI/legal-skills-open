# AGENTS.md - collaudo-verifica-conformita-dlgs36

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **collaudo dei lavori** e alla **verifica di conformita'** di
servizi e forniture nei contratti pubblici, secondo il **D.Lgs. 36/2023, art. 116**.
Target: ingegneri/architetti (RUP, collaudatori, DL/DEC), stazioni appaltanti,
operatori economici.

**È una skill documentale**: inquadra funzione, termini, collaudatori e incompatibilita';
**non redige** il certificato di collaudo/CRE, **non riproduce** l'allegato II.14, non
nomina i collaudatori, non sostituisce la stazione appaltante, il RUP o l'organo di
collaudo.

## Nota sull'area

Area **appalti-opere-pubbliche**. Copre la **fase di chiusura** del contratto
(collaudo/verifica di conformita'): complementare alle altre skill D.Lgs. 36
(`subappalto-contratti-pubblici-dlgs36`, `modifiche-varianti-contratti-pubblici-dlgs36`,
`garanzie-appalti-pubblici-dlgs36`, `oepv-valutatore-offerte-tecniche`,
`specifiche-tecniche-ict-appalti-dlgs36`). Distinta dal **collaudo statico** strutturale
(DPR 380 art. 67), coperto da `denuncia-opere-strutturali-l1086`.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-36-2023-art-116**: D.Lgs. 36/2023, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `0e9a1938...`; codice 23G00044; stesso indice delle altre
  skill D.Lgs. 36). Art. 116 versione 2, idGruppo 18, flagTipoArticolo 0, caricato via
  `caricaArticolo` e trascritto verbatim.

Trascrizione in `references/fonti/dlgs-36-2023-art-116.md`; estratto operativo in
`references/estratti/collaudo-verifica-checklist.md`.

## Punti chiave (verificati sul testo)

- **c. 1**: collaudo (lavori) / verifica di conformita' (servizi/forniture); funzione di
  certificare caratteristiche tecniche/economiche/qualitative, obiettivi, tempi.
- **c. 2**: termine 6 mesi (fino 1 anno per particolare complessita', all. II.14;
  riducibile); certificato provvisorio -> definitivo dopo 2 anni; approvazione tacita.
- **c. 3**: responsabilita' dell'appaltatore per vizi/difformita' (anche riconoscibili)
  denunciati prima del carattere definitivo, salvo art. 1669 c.c.
- **cc. 4/4-bis/4-ter**: 1-3 collaudatori (requisiti, indipendenza, PA/non PA);
  collaudatore statico; segreteria tecnica.
- **c. 5**: verifica di conformita' da RUP o direttore dell'esecuzione; verificatori
  diversi per elevato contenuto tecnologico.
- **c. 6**: incompatibilita' (a-e): magistrati/avvocati Stato, dipendenti PA in conflitto
  (art. 16), rapporti nel triennio con OE, chi ha svolto controllo/progettazione/
  direzione, chi ha partecipato alla gara.
- **cc. 7-11**: rinvio all'allegato II.14 (modalita', CRE); modalita'/tempi verifica nel
  capitolato; documenti finali (piano di manutenzione, BIM art. 43); accertamenti di
  laboratorio non soggetti a ribasso (costi all. II.15).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il certificato di collaudo/verifica o il **CRE**; non riprodurre gli
  allegati II.14/II.15.
- Non **inventare** termini/numeri: usare 6 mesi/1 anno, 2 anni, 1-3 collaudatori come da
  art. 116.
- Non confondere con il **collaudo statico** (DPR 380 art. 67).

### Cosa fare
- **Distinguere** collaudo/verifica, **inquadrare** termini, certificato, collaudatori e
  incompatibilita', con rinvio all'allegato II.14 e agli organi competenti.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 36/2023 pinnato a nuovo `!vig=` (nuovo hash)
e rileggere l'art. 116 (testo tra `(( ))`, es. correttivo D.Lgs. 209/2024).

## Validatori

- Non ancora assegnato (Livello 2 con RUP / collaudatore / esperto di contratti pubblici).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`inquadra-collaudo-termini.md`, `verifica-collaudatori-incompatibilita.md`)
- Esempi: 2 (termini e certificato di collaudo - cc. 1-3; nomina collaudatore e incompatibilita' - cc. 4-6)
