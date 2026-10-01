---
name: revisione-contratto-b2b-pixari
title: Revisione contratto B2B
description: 'Revisione approfondita contratto B2B italiano: commessa, SLA, penale, limitazione responsabilità, foro, 1341-1342, IP, recesso, DPA. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-civile/skills/revisione-contratto-b2b
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: commercial
language: it
---

# Revisione contratto B2B

> **Bozza — non consulenza legale.** Verificare norme vigenti e CCNL/settore se applicabile.

## Setup

1. Leggi `CLAUDE.md` → foro, red lines, playbook
2. Ruolo cliente: **committente** o **prestatore** (cambia priorità negoziale)
3. Allegati: condizioni generali, SLA, DPA privacy

## Step 1 — Struttura contratto

| Documento | Coerenza con master |
| --- | --- |
| Contratto principale | |
| Allegati (CGC, SLA, listini) | |
| Ordini / SOW | |
| DPA / privacy | → `/privacy-gdpr:revisione-dpa` |

## Step 2 — Clausole economiche

| Clausola | Analisi |
| --- | --- |
| Oggetto / prestazioni | Ambiguità, deliverable |
| Corrispettivo / indicizzazione | IVA, revisione prezzi |
| Pagamento | Termini, mora, sospensione |
| Durata / rinnovo | Tacito rinnovo, exit |
| Garanzie | Conformità, difetti nascosti `[da verificare]` |

## Step 3 — Inadempimento e exit

- Risoluzione art. 1453 ss. c.c. `[da verificare]`
- Clausola risolutiva espressa — trigger chiari
- Recesso convenzionale / preavviso
- **Penale** — art. 1384 c.c., cap, cumulo con danni `[da verificare]`
- **Limitazione responsabilità** — esclusioni dolo/colpa grave, indiretti, massimali

## Step 4 — Foro e ADR

- Foro esclusivo / derogabile
- Arbitrato CAM / istituzionale `[da verificare]`
- Mediazione obbligatoria d.lgs. 28/2010 se controversia civile `[da verificare]`

## Step 5 — Condizioni generali (1341-1342 c.c.)

- [ ] Clausole vessatorie individuate `[da verificare]`
- [ ] Doppia sottoscrizione specifica per: penale, foro, limitazione, recesso, …
- [ ] Trasparenza B2B vs B2C (d.lgs. 206/2005 se consumatore involontario)

## Step 6 — IP e riservatezza

- Titolarità sviluppi / licenza d'uso
- Marchi, open source compliance (bozza checklist)
- NDA incorporata o separata

## Step 7 — Altri rischi

| Tema | Flag |
| --- | --- |
| Subfornitura / change of control | |
| Force majeure | |
| Anticorruzione / 231 | `[da verificare]` |
| Legge applicabile (se cross-border) | |

## Output obbligatorio

### Tabella issue

| ID | Clausola | Rischio | Severity | Suggerimento bozza | Norma `[da verificare]` |
| --- | --- | --- | --- | --- | --- |

### Executive summary

- Top 5 punti negoziali
- Firmabile sì/no condizionato
- Approvazioni interne (socio, DPO)

## Appendice A — Clausole tipo commessa IT

| Clausola | Domande al committente | Red flag |
| --- | --- | --- |
| Accettazione deliverable | Chi valida? UAT? | Accettazione tacita troppo breve |
| Change request | Prezzo e tempi CR | CR gratis illimitate |
| Proprietà codice | Custom vs framework | Licenza perpetua non esclusiva |
| Escrow source code | Se fornitore insolvente | Assente su mission-critical |
| Service credit | Solo penale o anche SLA | Cap penale basso vs danni reali |

## Appendice B — 1341-1342 workflow

1. Elencare clausole che richiedono **approvazione specifica** `[da verificare]`
2. Verificare doppia firma su foglio separato o box in calce
3. Se controparte è PMI: valutare vessatorietà B2B `[da verificare]`
4. Documentare in tabella issue ID `1341-01`, `1341-02`, …

## Appendice C — Esempio riga tabella issue

| ID | Clausola | Rischio | Severity | Suggerimento | Norma |
| --- | --- | --- | --- | --- | --- |
| C-01 | Penale 30% | Disproporzionata | alta | Ridurre a 15% o cap | art. 1384 c.c. `[da verificare]` |
| C-02 | Foro esclusivo Tokyo | Inefficace/assente tutela | alta | Foro Milano o arbitrato IT | `[da verificare]` |

## Appendice D — Coordinamento privacy

Se trattamento dati personali nel contratto:

1. Flag in tabella issue → `PRIV-01`
2. Eseguire `/privacy-gdpr:revisione-dpa` sullo stesso pacchetto
3. Verificare informativa art. 13 verso dipendenti controparte se accesso a sistemi

## Appendice E — Post-review

- [ ] Bozza email negoziazione (opzionale, 5 bullet)
- [ ] Lista allegati da richiedere (bilanci, polizze, certificazioni)
- [ ] Scadenza proposta firma

## Appendice — Vendor review (EN vendor-agreement-review)

| Tema fornitore/acquirente | Domanda chiave |
| --- | --- |
| SLAs consegna | Penali, cap |
| Acceptance testing | UAT, rejection |
| Indemnity IP | Titolarità custom |
| Insurance | RCT, cyber se dati |
| Change of control | Consenso |

Per contratti pura fornitura → `/diritto-civile:revisione-fornitore`.

## Appendice — Negoziazione (email bozza)

```markdown
Oggetto: Commenti bozza [contratto] — [data]
- C-01: [clausola] — proposta: …
- C-02: …
Si richiede call per punti ad alta severity.
```

## Appendice — Matter

Apri `/diritto-civile:fascicolo-civile` prima di revisioni multi-round.

## Divieti

- Non certificare validità contratto
- Non omettere 1341-1342 su CGC ricevute

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
