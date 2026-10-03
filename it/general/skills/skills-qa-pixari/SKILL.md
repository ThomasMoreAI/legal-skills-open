---
name: skills-qa-pixari
title: QA skill — checklist v0.2
description: 'QA per SKILL.md v0.2: disclaimer, rito, citazioni, lunghezza minima workflow, testatti, invocabilità. Usare prima di PR. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-italiano-hub/skills/skills-qa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: en
---

# QA skill — checklist v0.2

## Obbligatorio — ogni skill workflow

- [ ] Frontmatter: `name`, `description` (≤1024 char), "Nessuna consulenza legale"
- [ ] `argument-hint` se skill accetta parametri
- [ ] Box disclaimer **nel corpo** (prime 10 righe)
- [ ] Nessuna promessa di parere vincolante / validità definitiva

## Profondità v0.2 (skill pratica)

- [ ] Skill **core** (non template): **≥100 righe** corpo markdown
- [ ] Almeno uno step numerato o tabella workflow
- [ ] Sezione **Output** esplicita
- [ ] Sezione **Divieti** o equivalente
- [ ] Escalation quando rischio alto

## Diritto italiano

- [ ] Rito indicato (civile, lavoro, privacy, …)
- [ ] Norme con estremi + `[da verificare]` dove non verificato
- [ ] No BGB / US brief structure
- [ ] No sentenze inventate

## Cross-plugin

- [ ] Rimandi corretti (`/plugin:skill` con nome plugin v0.2)
- [ ] Privacy in contratti → `privacy-gdpr:revisione-dpa`
- [ ] Rinomina v0.1 aggiornata in README/TROUBLESHOOTING

## Contributi

- [ ] Solo esempi `testatti/` fittizi
- [ ] Coerenza `AVVERTENZE.md`, `NOTICE`, `CONTRIBUTING.md` (min 100 righe nuovi skill)

## Test

- [ ] Percorso test in QUICKSTART o README plugin
- [ ] Output inizia con disclaimer bozza
- [ ] `claude plugin validate` su marketplace

## Esito report

```
Esito: OK | DA CORREGGERE
Skill: <nome>
Punti: ...
```

## Riferimento

Usa `skill-template` per nuovi skill; non invocabile come workflow.

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
## Appendice — Domande di chiusura all'utente

1. Ci sono documenti mancanti da caricare?
2. Quale scadenza operativa deve rispettare lo studio?
3. Serve bozza in italiano tecnico o nota per cliente?
4. Chi approva internamente (socio, DPO, HR)?
5. Eventuali vincoli segreto professionale o NDA con terzi?
6. Preferenza: tabella issue o memo narrativo?
7. Follow-up skill da eseguire dopo questo output?
8. Conferma che nessun dato reale finirà in repo pubblico?
