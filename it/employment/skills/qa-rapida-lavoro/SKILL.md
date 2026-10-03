---
name: qa-rapida-lavoro
title: Q&A rapida — lavoro
description: 'Q&A diritto del lavoro italiano: orario, ferie, trasferte, distacco, smart working, CCNL. Risposta breve con rimandi e verifica. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/lavoro/skills/qa-rapida-lavoro
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: employment
language: en
---

# Q&A rapida — lavoro

> **Bozza — non consulenza legale.** Verificare CCNL e norme vigenti `[da verificare]`.

## Aree coperte

| Area | Promemoria |
| --- | --- |
| Orario / straordinario | Limiti st.lav. + CCNL |
| Ferie e permessi | Maturation, proporzionali |
| Malattia / infortunio | INPS, job retention `[da verificare]` |
| Trasferte / distacco | Distacco art. 30 `[da verificare]` |
| Smart working | Accordo individuale/collective `[da verificare]` |
| Demansionamento / cambio mansione | |
| Rappresentanza sindacale | |

## Modalità risposta

1. Riformula in termini giuridici
2. Indica norme/CCNL **probabilmente** rilevanti con `[da verificare]`
3. Max 20 righe + passi successivi
4. Se serve atto → skill dedicata

## Rimandi

| Tema | Skill |
| --- | --- |
| Licenziamento | `/lavoro:revisione-licenziamento` |
| Assunzione | `/lavoro:hiring-review-lavoro` |
| Dati dipendente | `/privacy-gdpr:risposta-diritti-interessato` |

## Limiti

- Non calcolare termini senza date
- Non sostituire sindacato/avvocato per il dipendente

## Escalation

Contenzioso, licenziamenti collettivi, illeciti penali.

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
