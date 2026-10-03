---
name: bozza-memo-disciplinare
title: Bozza memo disciplinare
description: Bozza memo disciplinare interno, contestazione o promemoria pre-licenziamento. Struttura in fatto/diritto/rischi. Nessuna consulenza legale.
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/lavoro/skills/bozza-memo-disciplinare
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: employment
language: en
---

# Bozza memo disciplinare

> **Bozza — non consulenza legale.**

## Tipi documento

| Tipo | Destinatario | Obiettivo |
| --- | --- | --- |
| Contestazione | Dipendente | Formalizzare addebiti |
| Memo interno | Management / HR | Decisione sanzione |
| Promemoria pre-licenziamento | Legale / socio | Go/no-go licenziamento |

## Struttura completa

### 1. Sintesi esecutiva (max 10 righe)

### 2. Cronologia fatti

Tabella data / evento / fonte prova.

### 3. Quadro normativo

- st.lav., CCNL, regolamento aziendale `[da verificare]`
- Procedimento rispettato sì/no

### 4. Valutazione proporzionalità

| Sanzione proposta | Alternativa meno grave | Motivazione scelta |
| --- | --- | --- |

### 5. Rischi contenzioso

- art. 18, reintegra, danni `[da verificare]`
- Reputazione interna

### 6. Raccomandazioni

Opzioni numerate; nessuna decisione automatica.

### 7. Allegati

Elenco documenti alla cartella disciplinare.

## Collegamenti

- Da `/lavoro:indagine-interna-disciplinare`
- Verso `/lavoro:revisione-licenziamento` se esito = licenziamento

## Appendice — Conservazione

Promemoria: conservare cartella disciplinare secondo policy HR e privacy `[da verificare]`.

## Appendice — Distribuzione

| Destinatario | Versione |
| --- | --- |
| Legale | Completa con rischi |
| HR | Senza strategia contenzioso dettagliata |
| Management | Solo sintesi esecutiva |

## Divieti

- Non inviare a dipendente senza revisione legale/HR

## Appendice — Coordinamento e chiusura

### Skill correlati

Usare insieme agli altri plugin del marketplace `pixari-italian-legal-skills` per profilo completo.

### Verifica output

Ogni sezione normativa senza fonte utente deve contenere `[da verificare]`.

### Revisione

Nessun documento va inviato a controparte, Garante, giudice o dipendente senza revisione umana.

### Test senza dati reali

Fascicoli in `testatti/` — solo personaggi inventati.

### Domande finali all'utente

- Documenti mancanti?
- Scadenza operativa?
- Chi approva in studio (socio, DPO, HR)?
- Output tecnico o per cliente?
- Follow-up skill consigliato?
