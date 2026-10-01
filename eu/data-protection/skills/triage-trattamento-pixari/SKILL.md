---
name: triage-trattamento-pixari
title: Triage trattamento
description: 'Valutazione preliminare nuovo trattamento: base giuridica, rischio, necessità DPIA (art. 35), LIA, proceed/hold. Matrice rischio in bozza. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/privacy-gdpr/skills/triage-trattamento
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: it
---

# Triage trattamento

> **Bozza — non consulenza legale.** Non sostituisce DPIA formale né consultazione Garante ove obbligatoria.

## Step 1 — Scheda trattamento

Compila con l'utente:

| Campo | Valore |
| --- | --- |
| Finalità | |
| Titolare | |
| Categorie interessati | |
| Categorie dati (ordinari / particolari / giudiziari) | |
| Base giuridica proposta | `[da verificare]` art. 6 / 9 |
| Conservazione | |
| Destinatari / responsabili | |
| Trasferimenti extra-SEE | |
| Profilazione / decisioni automatizzate | |
| Sicurezza (misure note) | |

## Step 2 — Base giuridica

Per ogni finalità, verifica coerenza base / dati / trasparenza (art. 5, 6, 13–14) `[da verificare]`.

**Flag alta** se: dati particolari senza art. 9; larga scala; minori; monitoraggio sistematico pubblico.

## Step 3 — DPIA necessaria? (art. 35)

Checklist indicativa (non esaustiva):

- [ ] Valutazione sistematica e globale (profilazione su larga scala)
- [ ] Trattamento su larga scala di categorie particolari o dati penali
- [ ] Monitoraggio sistematico area accessibile al pubblico
- [ ] Liste Garante / EDPB art. 35(4) `[da verificare]`
- [ ] Tecnologie nuove (biometria, AI scoring, …)

**Esito:** `DPIA obbligatoria` | `DPIA consigliata` | `DPIA non richiesta` — con motivazione breve.

Se obbligatoria → invoca `/privacy-gdpr:generazione-dpia`.

## Step 4 — LIA (interesse legittimo)

Se base = art. 6(1)(f):

1. Finalità legittima
2. Necessità
3. Bilanciamento (test a tre stadi) — documentare in bozza `[da verificare]`

## Step 5 — Matrice rischio (output)

| Area | Rischio | Mitigazione proposta |
| --- | --- | --- |
| Trasparenza | basso/medio/alto | |
| Sicurezza | | |
| Diritti interessati | | |
| Trasferimenti | | |

## Step 6 — Decisione

- **Proceed** — con condizioni (informativa, contratto, TOM)
- **Hold** — attendere DPIA / parere DPO / consultazione art. 36 `[da verificare]`
- **Reject** — trattamento non proporzionato (motivare)

## Escalation

- Trattamento ad alto rischio residuo dopo mitigazioni
- Settori regolati (sanità, credito, telecom) — norme settoriali `[da verificare]`

## Appendice — Esempi tipologia (orientamento, non tassativo)

| Trattamento | DPIA indicativa | Note |
| --- | --- | --- |
| CRM B2B clienti | Consigliata se profilazione | Base contratto/legittimo interesse |
| Videosorveglianza dipendenti | Obbligatoria `[da verificare]` | LIA + sindacale |
| AI scoring candidati | Alta | Art. 22, bias, trasparenza |
| Newsletter B2C | Bassa se opt-in chiaro | ePrivacy cookie `[da verificare]` |
| Backup cloud UE | Media | Sub-responsabile + SCC |

## Appendice — Domande rapide all'utente

1. Volume interessati stimato?
2. Dati particolari coinvolti?
3. Decisioni automatizzate con effetti giuridici?
4. Trasferimenti fuori SEE?
5. Esiste registro trattamenti aggiornato?

## Output file

Salva bozza `triage_[nome]_bozza.md` con matrice rischio e decisione proceed/hold.

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
