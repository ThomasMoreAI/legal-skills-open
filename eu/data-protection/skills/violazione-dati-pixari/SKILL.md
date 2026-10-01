---
name: violazione-dati-pixari
title: Violazione dati personali
description: 'Workflow violazione dati personali: valutazione rischio, notifica Garante art. 33 (72h), comunicazione interessati art. 34, registro violazioni. Bozza documenti. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/privacy-gdpr/skills/violazione-dati
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: it
---

# Violazione dati personali

> **Bozza — non consulenza legale.** Termini e obblighi su testo vigente `[da verificare]`. Attivare incident response IT e DPO immediatamente.

## Step 1 — Intake incidente

| Campo | Dettaglio |
| --- | --- |
| Data/ora scoperta | |
| Data/ora violazione (stimata) | |
| Descrizione | |
| Categorie dati | |
| N. interessati stimati | |
| Cause / vettore | |
| Misure contenimento già adottate | |

## Step 2 — Valutazione rischio (art. 33-34)

Valuta probabilità e gravità per diritti e libertà:

- Dati particolari / finanziari / credenziali?
- Identificabilità diretta?
- Misure crittografiche efficaci?
- Durata esposizione

**Esito bozza:**

- Notifica Garante: **sì / no / incerto** — motivare
- Comunicazione interessati: **sì / no** — motivare art. 34 `[da verificare]`

## Step 3 — Notifica autorità (art. 33) — bozza

Se notifica richiesta, struttura:

1. Natura violazione
2. DPO contatto
3. Conseguenze probabili
4. Misure proposte/adottate

**Timeline:** documentare conteggio 72h da consapevolezza `[da verificare]`.

## Step 4 — Comunicazione interessati (art. 34) — bozza

Linguaggio chiaro: cosa successo, DPO, misure, raccomandazioni (es. cambio password).

## Step 5 — Registro violazioni (art. 33(5))

Voce registro:

| ID | Data | Fatto | Dati | Esito notifica | Azioni correttive |
| --- | --- | --- | --- | --- | --- |

## Step 6 — Follow-up

- Root cause analysis
- Aggiornamento DPIA / TOM
- Valutazione sanzioni / contenzioso `[da verificare]`
- Coordinamento con responsabili art. 28 (notifica titolare se sub-responsabile)

## Escalation

- Violazione su larga scala, ransomware con exfiltrazione, dati sanitari
- Segnalazioni media / reclami multipli

## Testatto

Usa `testatti/privacy-fittizio/03_nota_violazione_interna.md` per simulazione.

## Divieti

- Non ritardare contenimento tecnico per attendere bozza
- Non ammettere colpa in bozze esterne senza revisione legale

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
