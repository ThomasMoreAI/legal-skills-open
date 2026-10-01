---
name: monitoraggio-informativa-pixari
title: Monitoraggio informativa
description: 'Revisione periodica informativa privacy / policy interne: completezza art. 13-14, coerenza con trattamenti attuali, azioni aggiornamento. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/privacy-gdpr/skills/monitoraggio-informativa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: it
---

# Monitoraggio informativa

> **Bozza — non consulenza legale.** Verificare modifiche normative e provvedimenti Garante `[da verificare]`.

## Quando usare

- Revisione annuale / semestrale policy privacy
- Dopo nuovo trattamento o cambio fornitore cloud
- Pre-lancio campagna marketing o nuovo modulo dati

## Step 1 — Inventario trattamenti collegati

Allinea informativa a registro trattamenti (se fornito):

| Trattamento in policy | In registro? | Coerente? |
| --- | --- | --- |
| | | |

## Step 2 — Checklist art. 13-14 (sintesi)

- [ ] Identità e contatti titolare / DPO
- [ ] Finalità e base giuridica per ciascuna
- [ ] Legittimo interesse (se usato) — sintesi LIA `[da verificare]`
- [ ] Destinatari / categorie responsabili
- [ ] Trasferimenti extra-SEE e garanzie
- [ ] Periodo conservazione o criteri
- [ ] Diritti e modalità esercizio
- [ ] Reclamo Garante
- [ ] Obbligo/dispensa conferimento
- [ ] Processi automatizzati / profilazione

## Step 3 — Coerenza operativa

- Cookie banner / preference center allineati?
- Form raccolta dati citano finalità corrette?
- Link informativa raggiungibile pre-conferimento?

## Step 4 — Output

| Elemento | Stato | Azione |
| --- | --- | --- |
| … | OK / Gap | Aggiornare sezione X |

**Prossima revisione suggerita:** data + trigger (nuovo fornitore, breach, …)

## Divieti

- Non pubblicare informativa aggiornata senza approvazione DPO

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

## Appendice — Errori comuni (privacy)

- Rispondere al DSAR senza mappare tutti i sistemi
- Confondere titolare e responsabile nella lettera
- Omettere verifica identità su richieste di cancellazione
- Trasferimenti USA senza SCC/TIA documentati nel DPA
- DPIA copiata da template senza rischi specifici del trattamento
## Appendice — Domande di chiusura all'utente

1. Ci sono documenti mancanti da caricare?
2. Quale scadenza operativa deve rispettare lo studio?
3. Serve bozza in italiano tecnico o nota per cliente?
4. Chi approva internamente (socio, DPO, HR)?
5. Eventuali vincoli segreto professionale o NDA con terzi?
6. Preferenza: tabella issue o memo narrativo?
7. Follow-up skill da eseguire dopo questo output?
8. Conferma che nessun dato reale finirà in repo pubblico?
