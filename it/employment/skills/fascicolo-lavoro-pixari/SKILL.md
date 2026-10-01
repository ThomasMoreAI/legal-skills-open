---
name: fascicolo-lavoro-pixari
title: Fascicolo lavoro
description: 'Intake e organizzazione fascicolo lavoro: timeline, allegati, ruolo cliente, prossimi atti. Integra testatti licenziamento. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/lavoro/skills/fascicolo-lavoro
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: employment
language: it
---

# Fascicolo lavoro

> **Bozza — non consulenza legale.** Matter workspace EN `matter-workspace`.

## Path persistente (doc)

`~/.claude/plugins/config/pixari-italian-legal-skills/lavoro/matters/<slug>/`

Cross-hub: `/diritto-italiano-hub:fascicolo-mandato`.

## Intake

| Campo | Valore |
| --- | --- |
| Cliente / parte rappresentata | datore / lavoratore |
| Dipendente (se applicabile) | |
| CCNL | |
| Fase | pre-contenzioso / impugnazione / cassazione `[da verificare]` |
| Foro | |

## Struttura cartella suggerita

```
fascicolo_<slug>/
  00_anagrafica.md
  01_timeline.md
  02_contratto_e_documenti/
  03_licenziamento_o_disciplina/
  04_contenzioso/
  05_comunicazioni_cliente/
  bozze/
```

## Timeline

Genera o aggiorna `01_timeline.md` da documenti caricati (date, evento, fonte).

## Prossimi passi (bozza)

| Priorità | Azione | Skill |
| --- | --- | --- |
| | Revisione licenziamento | `/lavoro:revisione-licenziamento` |
| | Checklist termini | `/lavoro:checklist-licenziamento` |

## Testatto

Carica `testatti/licenziamento-fittizio/` per prova end-to-end.

## Privacy

Dati dipendenti — limitare export; seguire policy studio.

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

## Appendice — Errori comuni (lavoro)

- Licenziamento senza precedente contestazione quando richiesta
- Ignorare soglie art. 18 e procedimento `[da verificare]`
- Calcolo termini impugnazione senza data certa comunicazione
- Uso di email informali come prova senza contesto
- Clausole non concorrenza non proporzionate al CCNL
## Appendice — Domande di chiusura all'utente

1. Ci sono documenti mancanti da caricare?
2. Quale scadenza operativa deve rispettare lo studio?
3. Serve bozza in italiano tecnico o nota per cliente?
4. Chi approva internamente (socio, DPO, HR)?
5. Eventuali vincoli segreto professionale o NDA con terzi?
6. Preferenza: tabella issue o memo narrativo?
7. Follow-up skill da eseguire dopo questo output?
8. Conferma che nessun dato reale finirà in repo pubblico?
