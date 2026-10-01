---
name: fascicolo-mandato-pixari
title: Fascicolo mandato
description: 'Workspace mandato: struttura cartelle, naming, privilege note, indice allegati. Cross-materia (civile, lavoro, privacy). Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-italiano-hub/skills/fascicolo-mandato
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: it
---

# Fascicolo mandato

> **Bozza — non consulenza legale.** Non sostituisce PCT/gestionale dello studio.

## Intake

| Campo | Valore |
| --- | --- |
| Slug | `mandato_<cliente>_<anno>` (no dati sensibili in slug pubblico) |
| Cliente (interno) | codice o iniziali |
| Materia | |
| Avvocato responsabile | |
| Privilegio | promemoria art. 622 c.p. `[da verificare]` |

## Struttura cartella standard

```
mandato_<slug>/
  00_meta.md          # anagrafica, contatti, confini mandato
  01_timeline.md      # cronologia (aggiornare con skill verticali)
  02_documenti/       # PDF, email export
  03_bozze/           # output AI da revisionare
  04_note_interne/    # strategia, non per cliente
  README_fascicolo.md # indice e stato
```

## File `00_meta.md` template

- Parti, oggetto, valore controversia indicativo
- Foro / rito
- Scadenze note `[da verificare]`
- **Non** incollare dati personali non necessari

## Privilege e riservatezza

- Etichetta bozze: `PRIVILEGIATO — BOZZA`
- Non condividere cartella con tool non approvati dallo studio
- Export AI: policy interna

## Integrazione skill

| Materia | Skill fascicolo specifico |
| --- | --- |
| Lavoro | `/lavoro:fascicolo-lavoro` |
| Civile cronologia | `/diritto-civile:cronologia-contenzioso` |
| Privacy DSAR | cartella `dsar/` sotto fascicolo |

## Aggiornamento

Ad ogni sessione: data, skill usato, file prodotto in `03_bozze/`.

## Test

Usa sottocartelle in `testatti/` senza copiare dati reali.

## Divieti

- Non caricare segreti industriali cliente in repo git pubblico

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
