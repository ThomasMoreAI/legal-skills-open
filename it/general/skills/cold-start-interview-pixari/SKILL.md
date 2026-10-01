---
name: cold-start-interview-pixari
title: Cold-start — profilo studio
description: 'Intervista cold-start completa per profilo studio in CLAUDE.md: organizzazione, materie, riti, citazioni, playbook, strumenti, escalation. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-italiano-hub/skills/cold-start-interview
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: it
---

# Cold-start — profilo studio

> **Configurazione — non consulenza legale.** Alla fine: `/diritto-italiano-hub:avvertenze-legali`.

## Obiettivo

Produrre un `CLAUDE.md` **operativo** per tutti i plugin (hub + civile + lavoro + privacy).

## Fase 1 — Identità

1. Nome studio / reparto legale / impresa
2. Ruolo utente (partner, associate, legale interno, praticante)
3. Lingua output (italiano tecnico / misto cliente)
4. Materie principali (ordine priorità)
5. Materie **escluse** (non dare consulenza)

## Fase 2 — Riti e competenze

| Rito | Frequenza | Note |
| --- | --- | --- |
| Civile ordinario | | |
| Giudizio del lavoro | | |
| Cautelare / esecutivo | | |
| TAR / amministrativo | | |
| Arbitrato | | |

Fori abituali `[da verificare]`.

## Fase 3 — Stile e citazioni

- Formato Cass. preferito
- Database (DeJure, Lexis, Italiagov, …) — solo nomi
- Politica `[da verificare]`: sempre se non da tool utente?
- Lingua citazioni UE (IT/EN)

## Fase 4 — Playbook e rischio

- Path playbook interno (senza contenuti riservati in chat)
- Soglie escalation socio / DPO / esterno
- Clausole red lines contrattuali (sintesi)
- Template memo/atto preferiti

## Fase 5 — Strumenti e dati

- PCT / gestionale fascicoli
- Policy AI studio (se nota)
- Divieto upload dati reali in Issue/PR — conferma comprensione

## Fase 6 — Plugin verticali

Suggerisci cold-start dedicati se materia attiva:

| Materia | Skill |
| --- | --- |
| Privacy | `/privacy-gdpr:cold-start-privacy` |
| Lavoro | `/lavoro:cold-start-lavoro` |
| Civile | `/diritto-civile:cold-start-civile` |

## Output — struttura `CLAUDE.md`

```markdown
## Identità
## Materie e riti
## Stile citazioni e fonti
## Playbook e red lines
## Escalation
## Strumenti
## Plugin collegati
## Note sessione
```

Scrivi file su `diritto-italiano-hub/CLAUDE.md` o path indicato.

## Chiusura

- Ricorda revisione periodica (semestrale)
- Proponi `/diritto-italiano-hub:fascicolo-mandato` per primo mandato test in `testatti/`

## Divieti

- Non memorizzare password o dati clienti reali nel file

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
