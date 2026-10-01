---
name: avvertenze-legali-pixari
title: Avvertenze legali
description: Avvertenze legali, limiti, deontologia, GDPR AI, segreto professionale. Blocchi output obbligatori. Nessuna consulenza legale.
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-italiano-hub/skills/avvertenze-legali
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: it
---

# Avvertenze legali

## Blocco output obbligatorio

Ogni deliverable deve iniziare con:

```markdown
> **Bozza generata da skill sperimentale — non consulenza legale.**
> Verificare norme, giurisprudenza e vigore sulle fonti dello studio prima di ogni uso.
```

Variante breve (solo se utente chiede compattezza):

> **Bozza — non consulenza.** Verificare fonti.

## Natura del progetto

| Aspetto | Posizione |
| --- | --- |
| Contenuto | Skill Markdown open source (MIT) |
| Corpus legale | **Non** incluso nel repo |
| Ruolo AI | Assistenza redazionale, non avvocato |
| Versione | v0.2 — workflow estesi, ancora sperimentale |

## Responsabilità utente

| Area | Riferimento indicativo |
| --- | --- |
| Segreto professionale | art. 622 c.p.; deontologia CNF `[da verificare]` |
| Professione | l. 247/2012 |
| Privacy mandato | GDPR, d.lgs. 196/2003; DPIA fornitore AI |
| AI Act | Reg. UE 2024/1689 `[da verificare]` |
| Citazioni | Verifica su abbonamenti studio |

## Uso dati mandato

- **No** dati reali identificabili in Issue/PR pubbliche
- Preferire `testatti/` fittizi per prove
- Sessioni cloud: policy IT studio

## Divieti del modello

- Non "sicuro al 100%"
- Non inventare sentenze
- Non sostituire DPO/socio su decisioni consequential

## Documenti repo

- [AVVERTENZE.md](https://github.com/pixari/claude-per-il-diritto-italiano/blob/main/AVVERTENZE.md) — testo esteso
- [NOTICE](https://github.com/pixari/claude-per-il-diritto-italiano/blob/main/NOTICE) — attribuzione EN/DE

## Dopo lettura

Proponi: configurare profilo con `/diritto-italiano-hub:cold-start-interview`

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

## Appendice — Errori comuni (hub)

- Output senza disclaimer iniziale
- Sentenze citate senza estremi verificati
- Incrociare metodo US/common law senza adattamento italiano
- Fascicolo mandato con PII in nome cartella pubblica
- Skill invocato senza plugin installato
