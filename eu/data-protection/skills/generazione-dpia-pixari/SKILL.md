---
name: generazione-dpia-pixari
title: Generazione DPIA (bozza)
description: 'Bozza struttura DPIA (art. 35 GDPR) allineata a prassi Garante/EDPB: descrizione, necessità, rischi, misure, consultazione. Non sostituisce il DPO. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/privacy-gdpr/skills/generazione-dpia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: it
---

# Generazione DPIA (bozza)

> **Bozza — non consulenza legale.** La DPIA deve essere approvata dal titolare/DPO; consultazione Garante se art. 36 `[da verificare]`.

## Prerequisiti

- Output di `/privacy-gdpr:triage-trattamento` o scheda trattamento equivalente
- `CLAUDE.md` → sistemi e misure già note

## Struttura documento (sezioni)

### 1. Executive summary

- Trattamento, titolare, DPO
- Esito preliminare: rischio residuo basso/medio/alto (bozza)
- Raccomandazione proceed/hold

### 2. Descrizione del trattamento

- Finalità, natura, ambito, contesto
- Flusso dati (diagramma testuale)
- Interessati e volumi stimati
- Periodo di conservazione

### 3. Necessità e proporzionalità

- Base giuridica
- LIA se applicabile (sintesi)
- Alternative considerate

### 4. Valutazione rischi per diritti e libertà

| Rischio | Probabilità | Gravità | Rischio iniziale |
| --- | --- | --- | --- |
| Accesso non autorizzato | | | |
| Perdita integrità | | | |
| … | | | |

### 5. Misure di mitigazione (art. 32)

- Tecniche (cifratura, pseudonimizzazione, access control)
- Organizzative (formazione, policy, incident response)
- Residuo post-mitigazione

### 6. Consultazione stakeholder

- Parere DPO (spazio)
- Interessati / rappresentanti se previsto `[da verificare]`

### 7. Consultazione Garante (art. 36)

- Check: rischio alto residuo non mitigabile?
- Bozza richiesta se sì `[da verificare]`

### 8. Revisione e approvazione

- Data, versione, firmatari
- Calendario riesame

## Output

File markdown bozza `DPIA_[nome]_bozza.md` — tutte le affermazioni normative con `[da verificare]` se non da fonte utente.

## Divieti

- Non certificare conformità
- Non omettere rischi noti dall'utente

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
