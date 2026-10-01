---
name: indagine-interna-disciplinare-pixari
title: Indagine interna disciplinare
description: 'Indagine disciplinare interna: raccolta prove, contraddittorio, riservatezza, conservazione documenti. Bozza piano indagine e verbale. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/lavoro/skills/indagine-interna-disciplinare
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: employment
language: it
sources:
- title: Template Verbale Audizione
  path: references/template-verbale-audizione.md
---

# Indagine interna disciplinare

> **Bozza — non consulenza legale.** Rispettare privacy dipendenti e eventuali obblighi penali (non sostituire PM).

## Fase 1 — Avvio

- Fatto contestato e data
- Soggetti coinvolti (testimoni, responsabili)
- Sospensione cautelare? `[da verificare]` CCNL e proporzionalità
- Nomina incaricato indagine (neutrale)

## Fase 2 — Raccolta prove

| Fonte | Azione | Privacy |
| --- | --- | --- |
| Email aziendali | Export controllato | Policy IT |
| Videosorveglianza | Solo se base legale `[da verificare]` | |
| Testimoni | Verbale separato | |
| Registri accessi | | |

**Conservazione:** catena custodia semplificata; no alterazione.

## Fase 3 — Contraddittorio

- Comunicazione addebiti al lavoratore
- Termine per memorie difensive `[da verificare]`
- Eventuale assistenza sindacale/legale

## Fase 4 — Conclusione

- Relazione: fatto accertato / non provato / parziale
- Raccomandazione sanzione (richiamo, sospensione, licenziamento) — **bozza**
- Se licenziamento → `/lavoro:revisione-licenziamento`

## Output documenti

1. Piano indagine (timeline)
2. Bozza verbale audizione (template in references)
3. Relazione finale per HR

## Escalation

- Reati penali, molestie, whistleblowing → legale penale / 231 `[da verificare]`
- Dati particolari → DPO

## Divieti

- Non interrogare senza diritto di difesa dove dovuto

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
