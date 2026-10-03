---
name: revisione-nda
title: Revisione NDA
description: 'Revisione NDA / accordo riservatezza B2B italiano: definizioni, scopo, durata, carve-out, legge applicabile, rimedi. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-civile/skills/revisione-nda
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: contracts
language: en
---

# Revisione NDA

> **Bozza — non consulenza legale.**

## Setup

- Ruolo: **divulgante** (proteggere info) vs **ricevente** (limitare obblighi)
- Contesto: M&A, partnership, commessa, hiring

## Step 1 — Definizioni

| Termine | OK? | Commento |
| --- | --- | --- |
| Informazioni riservate | | Ampiezza definizione |
| Esclusioni (pubblico dominio, sviluppo indipendente, legge) | | |
| Rappresentanti / advisor | | |

## Step 2 — Scopo e uso

- Uso limitato a finalità X (specifica)
- Divieto reverse engineering se pertinente
- Return/destruction a fine trattative

## Step 3 — Durata

- Durata accordo vs sopravvivenza obbligo riservatezza
- Coerenza con progetto (es. 2 anni valutazione + 5 sopravvivenza)

## Step 4 — Rimedi

- Penale: proporzionalità `[da verificare]`
- Injunction / rimedi equitativi
- Non competere con legge italiana imperativa

## Step 5 — Legge e foro

- Legge italiana preferita se entrambe parti IT
- Foro/arbitrato coerente con contratto definitivo futuro

## Step 6 — Trappole

| Clausola nascosta | Flag |
| --- | --- |
| Non-solicit dipendenti | |
| Non circumvention | |
| Esclusività trattativa | |

## Output

Tabella gap + 2-3 formulazioni alternative per punti **alta** severity.

## Testatto

`testatti/nda-fittizio/NDA_2026_Delta-Omega.md`

## Appendice — Confronto ruoli

| Aspetto | Divulgante vuole | Ricevente vuole |
| --- | --- | --- |
| Definizione | Ampia | Stretta |
| Durata | Lunga | Breve |
| Penale | Alta | Bassa/cap |
| Foro | Proprio | Neutro |

## Divieti

- Non dichiarare NDA "standard di mercato" senza confronto

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
