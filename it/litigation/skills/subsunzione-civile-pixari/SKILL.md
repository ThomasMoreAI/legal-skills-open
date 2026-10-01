---
name: subsunzione-civile-pixari
title: Subsunzione civile
description: 'Subsunzione civile completa: qualificazione, norma, prove, eccezioni, conclusioni bozza comparsa/parere. Rito civile ordinario default. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-civile/skills/subsunzione-civile
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: litigation
language: it
---

# Subsunzione civile

> **Bozza — non consulenza legale.** Usa `/diritto-italiano-hub:metodo-giuridico` e `citazione-italiana`.

## Input

- Fatto, documenti, data vigore
- Tipo output: parere, nota cliente, **bozza comparsa** (cenni), atto cautelare `[da verificare]` se indicato

## Step 1 — Qualificazione

- Rapporto giuridico (contratto, extracontratto, responsabilità precontrattuale, …)
- Eventuali profili concorrenti
- Domande all'utente se dati mancanti

## Step 2 — Norma

- c.c. e leggi speciali
- Consumatore: d.lgs. 206/2005 `[da verificare]`
- Per ogni norma: estremi + vigore `[da verificare]`

## Step 3 — Subsunzione per elemento

| Elemento | Fatto | Norma | Pro/contro |
| --- | --- | --- | --- |
| | | | |

Esempi tipici (adattare al caso):

- Inadempimento / mora — art. 1218, 1453 ss. c.c. `[da verificare]`
- Risarcimento — danno, nesso, causalità
- Nullità / annullabilità

## Step 4 — Eccezioni processuali

Se output = atto:

- Competenza, litispendenza, continenza `[da verificare]`
- Prescrizione / decadenza — calcolo provvisorio
- Onere prova

## Step 5 — Conclusioni (bozza)

- Petitum / richieste
- Rischi probatori
- Passi (CTU, consulenza tecnica, mediazione)

## Rito

Default: **civile ordinario** (c.p.c.). Cautelare / esecutivo solo se richiesto.

## Output format

| Tipo | Sezioni |
| --- | --- |
| Parere | Quesito, fatto, diritto, rischio, opzioni |
| Comparsa bozza | Intestazione, fatto, diritto, conclusioni, prova |
| Nota cliente | Linguaggio semplificato + disclaimer |

## Divieti

- Non citare Cass. senza fonte utente
- Non copiare articoli interi da memoria modello

## Appendice — Checklist finale sessione

- [ ] Output inizia con disclaimer bozza / non consulenza
- [ ] Norme e sentenze non verificate: `[da verificare]`
- [ ] Escalation documentata se applicabile
- [ ] Prossimi passi con responsabile (legale, DPO, HR)
- [ ] Nessun dato reale di mandato in Issue/PR pubbliche

## Appendice — Workflow collegati

| Esigenza | Comando |
| --- | --- |
| Profilo studio | `/diritto-italiano-hub:cold-start-interview` |
| Metodo e citazioni | `/diritto-italiano-hub:metodo-giuridico`, `citazione-italiana` |
| Avvertenze | `/diritto-italiano-hub:avvertenze-legali` |
| Fascicolo | `/diritto-italiano-hub:fascicolo-mandato` |

## Appendice — Fonti (non in repo)

Verificare su: Normattiva, EUR-Lex, garanteprivacy.it, database giuridici dello studio.

## Appendice — Test

Fascicoli fittizi in `testatti/` — personaggi inventati.

## Appendice — Revisione umana

Ogni bozza richiede revisione da professionista abilitato prima di invio, deposito o firma.
