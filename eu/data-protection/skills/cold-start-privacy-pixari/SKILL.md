---
name: cold-start-privacy-pixari
title: Cold-start privacy
description: 'Intervista cold-start per profilo privacy: ruoli GDPR, sistemi, processo DSAR, template informativa/DPA. Scrive privacy-gdpr/CLAUDE.md. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/privacy-gdpr/skills/cold-start-privacy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: it
sources:
- title: Template Claude Privacy
  path: references/template-claude-privacy.md
---

# Cold-start privacy

> **Bozza — non consulenza legale.** Configurazione operativa; non sostituisce registro trattamenti né DPIA.

## Obiettivo

Popolare `CLAUDE.md` del plugin con informazioni **utilizzabili** da tutti gli skill privacy (DSAR, DPA, DPIA, violazioni).

## Intervista (chiedi in sequenza)

### 1. Contesto organizzazione

- Settore e dimensione (PMI, gruppo, PA `[da verificare]`)
- Ruolo utente: titolare, responsabile, DPO interno/esterno, legale
- Paesi / sedi con dipendenti o clienti

### 2. Ruoli GDPR tipici

- Chi è titolare per trattamenti principali (HR, clienti, marketing, sito)?
- Responsabili critici già noti (cloud, payroll, CRM)?
- DPO nominato? Contatto

### 3. Sistemi (per DSAR)

Elenco **ogni** repository dati personali:

| Sistema | Titolare/Resp. | Tipi dati | Note accesso DSAR |
| --- | --- | --- | --- |
| | | | |

### 4. Processo DSAR

- Canale ricezione (PEC, email dedicata, form)
- Verifica identità standard
- SLA interno (giorni) — confrontare con art. 12 `[da verificare]`
- Chi approva risposta (DPO, legale, HR)

### 5. Playbook contrattuale

- DPA tipo: allegato standard sì/no
- Red lines (audit illimitato, trasferimenti, sub-responsabile)
- Clausole SCC / cloud accettate

### 6. Documenti da caricare (opzionale)

- Bozza informativa privacy
- Template DPA
- Ultima risposta DSAR anonimizzata (per stile)

## Output — aggiorna `CLAUDE.md`

Scrivi o aggiorna le sezioni:

```markdown
## Ruoli e contatti
## Registro sistemi (DSAR)
## Processo DSAR
## Playbook DPA
## Escalation
## Fonti verifica
```

Usa `skills/cold-start-privacy/references/template-claude-privacy.md` come guida struttura.

## Dopo il cold-start

Suggerisci all'utente:

1. `/privacy-gdpr:risposta-diritti-interessato` con testatto `testatti/privacy-fittizio/`
2. `/privacy-gdpr:revisione-dpa` su DPA fittizio
3. `/privacy-gdpr:triage-trattamento` per nuovo trattamento

## Appendice — Domande opzionali avanzate

- Registro trattamenti: tool (Excel, OneTrust, …)?
- Cookie / marketing: gestione consenso?
- Whistleblowing hotline: trattamento segnalazioni?
- Imprese gruppo: joint controllership art. 26?
- Settore PA: codice PA `[da verificare]`?

## Appendice — Template file da creare

Dopo cold-start, suggerisci cartella `references/` con:

- `informativa_sito_bozza.md` (solo struttura)
- `dpa_template_bozza.md` (solo titoli clausole art. 28)

## Divieti

- Non inventare sistemi o contatti DPO
- Non memorizzare dati reali di interessati nell'intervista

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
