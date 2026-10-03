---
name: personalizzazione-playbook
title: Personalizzazione playbook
description: 'Aggiorna CLAUDE.md (hub o plugin) da feedback utente: red lines, stile, escalation. Equivalente customize lite. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-italiano-hub/skills/personalizzazione-playbook
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: en
---

# Personalizzazione playbook

> **Bozza — non consulenza legale.** Solo configurazione studio, non parere sul caso.

## Selezione file

| Argomento | Path |
| --- | --- |
| hub | `diritto-italiano-hub/CLAUDE.md` |
| privacy | `privacy-gdpr/CLAUDE.md` |
| lavoro | `lavoro/CLAUDE.md` |
| civile | `diritto-civile/CLAUDE.md` |

## Processo

1. Leggi file intero
2. Applica **solo** modifiche richieste dall'utente
3. Mantieni sezioni non toccate
4. Aggiungi in fondo: `Ultimo aggiornamento: YYYY-MM-DD — via personalizzazione-playbook`
5. Se modifica impatta più plugin, elenca cold-start da rifare

## Esempi modifiche tipiche

| Richiesta utente | Sezione target |
| --- | --- |
| "Foro Torino" | Foro / competenza |
| "Escalation DPO su ogni DSAR" | Escalation privacy |
| "Tono formale verso cliente" | Stile |
| "CCNL Commercio" | CCNL lavoro |

## Output

- Diff testuale (prima/dopo per sezione)
- File aggiornato
- Reminder revisione socio se policy strutturale

## Appendice — Rollback

Se l'utente chiede annullamento, ripristinare da git/versione precedente del `CLAUDE.md` — non tenere versioni concorrenti.

## Appendice — Esempi diff (fittizi)

| Prima | Dopo |
| --- | --- |
| Foro: (da compilare) | Foro: Milano `[da verificare]` |
| Escalation: generica | Escalation: socio entro 48h su penale >25% |

## Appendice — Validazione post-modifica

Dopo ogni aggiornamento, suggerire all'utente di eseguire uno skill di prova:

- Hub → `/diritto-italiano-hub:metodo-giuridico` su quesito fittizio
- Privacy → `/privacy-gdpr:triage-trattamento`
- Lavoro → `/lavoro:qa-rapida-lavoro`
- Civile → `/diritto-civile:revisione-contratto-b2b` su testatto

## Divieti

- Non inserire PII terzi
- Non risolvere controversia nel playbook

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
