---
name: gap-normativo-privacy-pixari
title: Gap normativo privacy
description: Gap analysis tra documentazione interna (informativa, registro, policy) e requisiti richiesti dall'utente o da nuovo trattamento. Nessuna consulenza legale.
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/privacy-gdpr/skills/gap-normativo-privacy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: it
---

# Gap normativo privacy

> **Bozza — non consulenza legale.** Confrontare sempre con testi vigenti e linee Garante `[da verificare]`.

## Input

- Documenti interni forniti (informativa sito, policy HR, estratto registro trattamenti)
- Obiettivo: nuovo prodotto, audit interno, risposta a reclamo, due diligence

## Step 1 — Mappa requisiti applicabili

Da contesto utente, elenca ambiti:

| Ambito | Fonti da verificare |
| --- | --- |
| Trasparenza art. 13-14 | |
| Diritti art. 15-22 | |
| Sicurezza art. 32 | |
| Responsabile art. 28 | |
| Trasferimenti cap. V | |
| Cookie / ePrivacy | d.lgs. 196/2003 `[da verificare]` |
| Settore (se applicabile) | |

## Step 2 — Matrice gap

| Requisito | Stato doc interno | Gap | Priorità | Azione bozza |
| --- | --- | --- | --- | --- |
| Identità titolare | | | | |
| Finalità | | | | |
| Base giuridica | | | | |
| Conservazione | | | | |
| Diritti | | | | |
| DPO | | | | |
| Trasferimenti | | | | |

**Priorità:** P1 = blocco go-live; P2 = remediation 30gg; P3 = miglioramento.

## Step 3 — Piano remediation

Tabella azioni con owner (DPO, IT, legale) e scadenze indicative.

## Step 4 — Output

- Executive summary (1 pagina)
- Gap table completa
- Non elencare articoli senza `[da verificare]` se non confermati da fonte utente

## Collegamenti

- Nuovo trattamento → `/privacy-gdpr:triage-trattamento`
- Informativa sito → `/privacy-gdpr:monitoraggio-informativa`

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
