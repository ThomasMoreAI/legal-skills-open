---
name: metodo-giuridico
title: Metodo giuridico (Italia)
description: 'Metodo giuridico italiano completo per atti, pareri, note cliente: qualificazione, norma, subsunzione, prove, conclusioni. Integra fascicolo e citazioni. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-italiano-hub/skills/metodo-giuridico
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: en
---

# Metodo giuridico (Italia)

> **Bozza — non consulenza legale.** Apri con `/diritto-italiano-hub:avvertenze-legali`.

## Setup

1. Leggi `diritto-italiano-hub/CLAUDE.md` e `CLAUDE.md` del plugin verticale se attivo
2. Carica fascicolo se esiste (`/diritto-italiano-hub:fascicolo-mandato`)
3. Dichiara **rito** e **tipo documento**

## Fase 1 — Qualificazione

- Fatto rilevante (solo da documenti utente)
- Quesito giuridico e confini mandato
- Domande all'utente (max 5 puntati) se dati mancanti
- Profili giuridici concorrenti (es. contratto + 231 `[da verificare]`)

## Fase 2 — Norma

- Gerarchia: Cost., legge, d.lgs., reg. UE, contratto
- Specialità / posteriorità — segnala conflitto, non risolvere in autonomia
- Per norma: estremi + data vigore + `[da verificare]`
- Applica `/diritto-italiano-hub:citazione-italiana`

## Fase 3 — Subsunzione

Per ogni elemento:

| Elemento | Fatto provato / da provare | Norma | Pro / contro |
| --- | --- | --- | --- |

## Fase 4 — Prova e processo

- Onere della prova
- Eccezioni preliminari se atto di parte `[da verificare]`
- Prescrizione/decadenza — calcolo provvisorio
- CTU / consulenza tecnica se utile

## Fase 5 — Conclusioni (bozza)

- Petitum o raccomandazioni operative
- Alternative (transazione, mediazione)
- Rischi e next steps

## Formati output

### Atto di parte (civile ordinario)

1. Intestazione tribunale / parti / difensori
2. In fatto (cronologia se disponibile)
3. In diritto (per capo)
4. Conclusioni e richiesta istruttoria
5. Allegati e prova

### Parere interno

Quesito → Fatto → Diritto → Rischi → Opzioni

### Nota cliente

Linguaggio accessibile + disclaimer; poi `/diritto-civile:sintesi-cliente-stakeholder` se serve executive summary

## Integrazione verticali

| Materia | Skill specialistico |
| --- | --- |
| Civile | `/diritto-civile:subsunzione-civile` |
| Lavoro | `/lavoro:revisione-licenziamento` |
| Privacy | `/privacy-gdpr:risposta-diritti-interessato` |

## Appendice — Matter workspace (EN matter-workspace)

Prima di analisi su mandato reale:

1. `/diritto-italiano-hub:fascicolo-mandato` o fascicolo verticale (`fascicolo-privacy`, `fascicolo-civile`, `fascicolo-lavoro`)
2. Carica solo documenti del matter attivo
3. Registra in `matter.md` skill invocati e output in `bozze/`

## Appendice — Esempio mini-output (parere)

```markdown
> Bozza — non consulenza legale.

## Quesito
…

## Fatto (da documenti utente)
…

## Diritto
- art. … c.c. [da verificare]

## Rischi
…

## Opzioni
1. …
```

## Appendice — Escalation hub

| Trigger | Azione |
| --- | --- |
| Penale / criminale | Altro difensore |
| Cross-border | Verifica foro e legge applicabile |
| Urgenza cautelare | `/contenzioso-civile:triage-ricorso-cautelare` se installato |

## Divieti

- Struttura US brief / BGB non adattato
- Conclusioni come sentenza definitiva
- Consulenza al cittadino senza avvocato

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
