---
name: cronologia-contenzioso
title: Cronologia contenzioso (contrattualistica / pre-contenzioso)
description: 'Cronologia fatti e prove da fascicolo civile: timeline, gap probatori, allegati. Per contenzioso e pre-contenzioso. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-civile/skills/cronologia-contenzioso
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: contracts
language: en
---

# Cronologia contenzioso (contrattualistica / pre-contenzioso)

> **Bozza — non consulenza legale.** Per lite in corso o giudiziale → `/contenzioso-civile:cronologia-contenzioso`.

## Input richiesti

- Parti e ruolo processuale (attore/convenuto)
- Documenti con **data** verificabile
- Obiettivo: contenzioso, mediazione, parere

## Step 1 — Estrazione eventi

Per ogni documento:

1. Data (o intervallo)
2. Evento in una riga
3. Tipo: fatto / comunicazione / atto / prova
4. Fonte file
5. Rilevanza: alta/media/bassa

## Step 2 — Timeline markdown

```markdown
| Data | Evento | Tipo | Fonte | Rilevanza | Gap prova? |
```

Ordina cronologicamente; sega eventi **contestati** vs **pacifici**.

## Step 3 — Gap analysis

| Gap | Impatto | Azione suggerita |
| --- | --- | --- |
| Manca prova consegna diffida | | Richiedere ricevuta PEC |
| Data inizio inadempimento incerta | | |

## Step 4 — Prescrizione (bozza)

Ipotesi scadenze `[da verificare]` — **non** calcolo definitivo senza qualificazione da legale.

## Step 5 — Collegamenti

- Subsunzione → `/diritto-civile:subsunzione-civile`
- Sintesi management → `/diritto-civile:sintesi-cliente-stakeholder`

## Testatti

`testatti/contratto-b2b-fittizio/` + email PEC fittizia.

## Appendice — Export per comparsa

Dopo timeline, suggerire estratto **In fatto** per `/diritto-civile:subsunzione-civile` (solo fatti pacifici separati da contestati).

## Appendice — Legenda tipo evento

| Tipo | Simbolo suggerito in timeline |
| --- | --- |
| Fatto | F |
| Comunicazione | C |
| Atto processuale | A |
| Prova | P |

## Divieti

- Non inventare eventi o date

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
