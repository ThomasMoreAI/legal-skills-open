---
name: hiring-review-lavoro
title: Hiring review — lavoro
description: 'Revisione assunzione: contratto, periodo di prova, clausole restrittive, dati personali HR, CCNL. Bozza memo per HR/legale. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/lavoro/skills/hiring-review-lavoro
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: employment
language: en
---

# Hiring review — lavoro

> **Bozza — non consulenza legale.**

## Input

- Bozza contratto / lettera assunzione
- Job description, livello CCNL, inquadramento
- Policy assunzione interna se esiste

## Matrice clausole

| Clausola | Verifica | Severity |
| --- | --- | --- |
| Qualifica e livello CCNL | Mansioni coerenti | |
| Retribuzione e superminimo | Minimi CCNL `[da verificare]` | |
| Orario / ripartizione | Limiti orario | |
| Periodo di prova | Durata e recesso `[da verificare]` | |
| Sede e smart working | Accordi | |
| Non concorrenza / stabilità | Proporzionalità, compenso | |
| Proprietà risultati creativi | Se ruolo R&D | |
| Privacy dipendente | Informativa art. 13 | |
| TFR e welfare | | |
| Patto formativo / rimborso formazione | | |

## Dati personali HR

- Nuovo trattamento? → `/privacy-gdpr:triage-trattamento`
- Clauses conservazione documenti identità e visite mediche `[da verificare]`

## Documenti pre-assunzione

| Doc | Obbligatorietà `[da verificare]` |
| --- | --- |
| Idoneità sanitaria | |
| Casellario / certificazioni | |
| Patto non concorrenza firmato | |

## Output

- Tabella gap
- Memo "condizioni sospensive" se documenti mancanti
- Email bozza a HR con top 3 fix

## Appendice — Assunzione determinata / somministrazione

Se tipo non indeterminato: verificare cause e termini `[da verificare]` prima di approvare bozza.

## Appendice — Checklist pre-firma HR

- [ ] Informativa privacy firmata
- [ ] Documenti identità e codice fiscale
- [ ] Visita medica se dovuta
- [ ] Comunicazioni INPS/INAIL `[da verificare]`
- [ ] Accessi IT e badge

## Divieti

- Non garantire assenza contenzioso

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
