---
name: cold-start-civile
title: Cold-start civile
description: 'Cold-start profilo civile: contenzioso vs contratti, foro, 1341-1342, playbook clausole. Scrive diritto-civile/CLAUDE.md. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-civile/skills/cold-start-civile
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: contracts
language: en
---

# Cold-start civile

> **Bozza — non consulenza legale.**

## Intervista strutturata

### A — Profilo pratica

| Domanda | Risposta |
| --- | --- |
| % tempo contratti vs contenzioso | |
| Settori (IT, industriale, retail, …) | |
| Controparte tipo (PMI, corporate, PA) | |
| Lingua contratti (IT / EN) | |

### B — Foro e ADR

| Domanda | Risposta |
| --- | --- |
| Foro esclusivo preferito | |
| Arbitrato (CAM, ICC, …) | |
| Mediazione pre-azione `[da verificare]` | |

### C — Playbook negoziale

| Clausola | Red line interna |
| --- | --- |
| Penale max | |
| Cap responsabilità | |
| IP su sviluppi | |
| Recesso / preavviso | |
| SLA minime (se SaaS) | |

### D — 1341-1342 c.c.

| Domanda | Risposta |
| --- | --- |
| Processo doppia firma in studio | |
| Clausole sempre evidenziate | |
| Template foglio approvazione | |

### E — Privacy e dati

| Domanda | Risposta |
| --- | --- |
| DPA standard path | |
| Skill `/privacy-gdpr:revisione-dpa` su ogni commessa con dati | |

## Output — `diritto-civile/CLAUDE.md`

Sezioni: pratica, foro, playbook, 1341-1342, escalation, testatti.

## Percorsi test

| Fascicolo | Skill |
| --- | --- |
| `testatti/contratto-b2b-fittizio/` | `revisione-contratto-b2b` |
| `testatti/nda-fittizio/` | `revisione-nda` |

## Appendice — Esempio red lines compilate (fittizio)

| Clausola | Valore esempio |
| --- | --- |
| Penale max | 20% fee annua |
| Cap | 100% corrispettivo 12 mesi |
| Foro | Milano |

## Divieti

- Non inserire segreti commerciali cliente nel file profilo

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
