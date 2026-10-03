---
name: cold-start-lavoro
title: Cold-start lavoro
description: 'Cold-start profilo diritto del lavoro: CCNL, dimensione impresa, art. 18, rito, template memo licenziamento. Scrive lavoro/CLAUDE.md. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/lavoro/skills/cold-start-lavoro
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: employment
language: en
---

# Cold-start lavoro

> **Bozza — non consulenza legale.**

## Intervista strutturata

### A — Organizzazione

| Domanda | Risposta (annotare) |
| --- | --- |
| Ragione sociale / gruppo | |
| Settore ATECO (sintesi) | |
| N. dipendenti per sede | |
| Rappresentanza sindacale interna? | |
| RSU / contrattazione integrativa | |

### B — CCNL e policy

| Domanda | Risposta |
| --- | --- |
| CCNL applicabile | |
| Integrative aziendali (path interno) | |
| Regolamento aziendale / disciplinare | |
| Smart working policy | |
| Whistleblowing / 231 collegato `[da verificare]` | |

### C — Soglie e tutele

| Domanda | Risposta |
| --- | --- |
| Soglie art. 18 st.lav. `[da verificare]` | |
| d.lgs. 23/2015 — rilevanza | |
| Tutele dirigenti / rappresentanti | |
| Lavoratori disabili / categorie protette | |

### D — Contenzioso

| Domanda | Risposta |
| --- | --- |
| Foro abituale | |
| Rito: giudizio del lavoro (default) | |
| Studio esterno per impugnazioni | |
| Template memo licenziamento (path) | |

### E — HR operativo

| Domanda | Risposta |
| --- | --- |
| Contatto legale HR | |
| Escalation socio (soglie) | |
| Privacy dipendenti → DPO | |

## Output — `lavoro/CLAUDE.md`

Compila sezioni:

```markdown
## Organizzazione
## CCNL e policy
## Soglie art. 18
## Rito e foro
## Playbook licenziamento
## Hiring standard
## Escalation
## Testatti
```

## Dopo cold-start — percorsi test

1. `testatti/licenziamento-fittizio/` + `/lavoro:revisione-licenziamento`
2. `/lavoro:checklist-licenziamento` per screening rapido
3. `/lavoro:hiring-review-lavoro` su contratto tipo

## Coordinamento hub

Se profilo studio assente: `/diritto-italiano-hub:cold-start-interview` prima.

## Divieti

- Non salvare nomi dipendenti reali in `CLAUDE.md` committato su repo pubblico

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
