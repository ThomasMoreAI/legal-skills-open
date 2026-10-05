---
name: modifiche-varianti-contratti-pubblici-dlgs36-morellid
title: Modifiche del contratto e varianti in corso d'opera (D.Lgs. 36/2023 art. 120)
description: Supporto documentale alla modifica dei contratti pubblici in corso di esecuzione e alle varianti in corso d'opera secondo il Codice dei contratti pubblici (D.Lgs. 31 marzo 2023, n. 36), art. 120. Use when an engineer, RUP, or economic operator must frame a change to a public contract or a variation order (variante in corso d'opera) under Italian D.Lgs. 36/2023 art. 120; it is a documentary aid and does NOT approve the change, does NOT reproduce the referenced annexes, and does NOT replace the contracting authority, the RUP, or ANAC.
author: morellid
author_url: https://github.com/morellid/skill-per-ingegneri/tree/main/skills/modifiche-varianti-contratti-pubblici-dlgs36
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: government-contracts
language: it
tags: [varianti-in-corso-d-opera, modifica-contratto, dlgs-36-2023, contratti-pubblici, quinto-d-obbligo]
sources:
- title: Modifiche Varianti Checklist
  path: references/estratti/modifiche-varianti-checklist.md
- title: Dlgs 36 2023 Art120
  path: references/fonti/dlgs-36-2023-art120.md
---

# Modifiche del contratto e varianti in corso d'opera (D.Lgs. 36/2023 art. 120)

## Quando usare questa skill

Usala quando un **ingegnere, RUP, operatore di stazione appaltante o operatore economico** deve
inquadrare una **modifica di un contratto pubblico in corso di esecuzione** o una **variante in
corso d'opera**, secondo l'**art. 120 del Codice dei contratti pubblici** (D.Lgs. 31 marzo 2023,
n. 36):

- stabilire se la modifica e' **ammessa senza nuova procedura** (casi del comma 1);
- verificare **limiti economici** e distinguere **sostanziale/non sostanziale**;
- inquadrare **rinegoziazione**, **quinto d'obbligo**, **proroghe**, **autorizzazione del RUP** e
  **oneri verso l'ANAC**.

Per il **subappalto** usa `subappalto-contratti-pubblici-dlgs36` (art. 119); per la fase di
**gara** usa `bandi-tipo-anac-checker`, `oepv-valutatore-offerte-tecniche` e
`specifiche-tecniche-ict-appalti-dlgs36`.

## Casi di modifica senza nuova procedura (comma 1)

- **a) Clausole di revisione/opzione**: previste in **clausole chiare, precise e inequivocabili**
  dei documenti di gara (anche opzioni), a prescindere dal valore.
- **b) Prestazioni supplementari**: non previste, quando il cambio di contraente sia
  **impraticabile** o comporti **notevoli disagi/incremento dei costi**.
- **c) Varianti in corso d'opera**: per **circostanze imprevedibili** (nuove disposizioni;
  **eventi naturali straordinari/forza maggiore**; **rinvenimenti**; **difficolta' geologiche/
  idriche** non prevedibili con le conoscenze consolidate al momento della progettazione).
- **d) Sostituzione del contraente**: per clausole chiare; **morte/insolvenza/ristrutturazioni**
  societarie con operatore idoneo; subentro della stazione appaltante verso i subappaltatori.

Per **a) e c)** struttura del contratto e operazione economica devono restare **inalterate**.

## Limiti economici (commi 2-4)

- **b) e c)**: aumento di prezzo **non oltre il 50%** del valore iniziale; per **piu' modifiche
  successive** il limite si applica **a ciascuna** (senza eludere il codice).
- **Sotto soglia** (c. 3): modifiche consentite se **sotto entrambi** la **soglia dell'art. 14**
  e il **10%** (servizi/forniture) o **15%** (lavori) del valore iniziale.

## Sostanziale o non sostanziale (commi 5-7)

- **Non sostanziali**: sempre consentite (c. 5). Il **c. 7** elenca modifiche progettuali non
  sostanziali (risparmi in compensazione; soluzioni equivalenti/migliorative; interventi del
  direttore dei lavori finanziati nel quadro economico).
- **Sostanziale** (c. 6): quando **altera considerevolmente** struttura/operazione economica; in
  ogni caso se ammetterebbe altri candidati/offerte, **cambia l'equilibrio economico** a favore
  dell'aggiudicatario, **estende notevolmente** l'ambito, o sostituisce il contraente fuori dai
  casi del c. 1 lett. d).

## Procedimento, quinto d'obbligo, proroghe (commi 8-14)

- **Rinegoziazione** (c. 8): il **RUP** formula la proposta di nuovo accordo entro **tre mesi**.
- **Quinto d'obbligo** (c. 9): se previsto in gara, variazioni fino al **quinto** dell'importo
  alle condizioni originarie; l'appaltatore **non** puo' chiedere la risoluzione.
- **Proroghe** (c. 10-11): opzione di proroga; **proroga tecnica** all'uscente solo per il tempo
  strettamente necessario e nei casi di pericolo/grave danno all'interesse pubblico.
- **Autorizzazione** (c. 13): modifiche/varianti **autorizzate dal RUP**; le modifiche
  progettuali del c. 7 **approvate** dalla stazione appaltante su proposta del RUP (all. II.14);
  **avviso in GUUE** per i casi b)/c) (c. 14).

## Oneri ANAC ed errori progettuali (commi 15, 15-bis)

- **ANAC** (c. 15): comunicazione/trasmissione a cura del RUP (all. II.14); l'ANAC che accerta
  l'**illegittimita'** della variante esercita i poteri dell'art. 222; l'inadempimento comporta
  le **sanzioni** dell'art. 222, c. 13.
- **Errori/omissioni progettuali** (c. 15-bis): verifica in contraddittorio con progettista e
  appaltatore.

## Cosa NON fa (limiti)

- **Non approva** modifiche o varianti e **non ne attesta** la legittimita'.
- **Non riproduce** gli **allegati** richiamati (II.14, II.16) ne' gli articoli collegati
  (art. 60 revisione prezzi, art. 14 soglie, art. 222 ANAC, art. 41 c. 8-bis).
- **Non sostituisce** la stazione appaltante, il RUP ne' l'ANAC; non tratta il **subappalto**
  (art. 119) ne' la fase di gara.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`qualifica-modifica-contratto`](tasks/qualifica-modifica-contratto.md) | Stabilisce se la modifica rientra in un caso del comma 1 (a-d), rispetta i limiti (50%, 10%/15%) ed e' sostanziale o meno |
| [`imposta-variante-corso-opera`](tasks/imposta-variante-corso-opera.md) | Imposta procedimento, quinto d'obbligo, autorizzazione del RUP, avviso GUUE e oneri di comunicazione all'ANAC |

## Riferimenti normativi

- **D.Lgs. 31 marzo 2023, n. 36** (Codice dei contratti pubblici) - **art. 120** (Modifica dei
  contratti in corso di esecuzione): casi senza nuova procedura (c. 1), limiti 50% e sotto soglia
  (c. 2-3), modifica sostanziale/non sostanziale (c. 5-7), rinegoziazione (c. 8), quinto
  d'obbligo (c. 9), proroghe (c. 10-11), autorizzazione del RUP e avviso GUUE (c. 13-14), oneri
  ANAC e sanzioni ex art. 222 (c. 15), errori progettuali (c. 15-bis).
- Articoli/allegati **richiamati** (non riprodotti): **art. 60** (revisione prezzi), **art. 14**
  (soglie), **art. 222** (poteri/sanzioni ANAC), **art. 41 c. 8-bis**, **allegati II.14 e II.16**.

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-36-2023-art120.md`,
`references/estratti/modifiche-varianti-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la qualificazione della modifica, l'approvazione della
variante e la valutazione di legittimita' restano responsabilita' dell'operatore economico,
della **stazione appaltante**, del **RUP** e - per i controlli - dell'**ANAC**, sul testo vigente
dell'art. 120 (il Codice e' soggetto a decreti correttivi). La skill **non sostituisce** tali
soggetti ne' la lettura dell'art. 120 e degli atti da esso richiamati.
