---
name: revisione-licenziamento-pixari
title: Revisione licenziamento
description: 'Revisione approfondita licenziamento: qualificazione (giusta causa, giustificato motivo), procedimento, art. 18, impugnazione, prove. Output memo e checklist rischi. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/lavoro/skills/revisione-licenziamento
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: employment
language: it
---

# Revisione licenziamento

> **Bozza — non consulenza legale.** Verificare CCNL, norme vigenti e giurisprudenza `[da verificare]`.

## Carica contesto

1. `CLAUDE.md` → CCNL, soglie art. 18, foro
2. Documenti: lettera, contratto, timeline, disciplinari
3. Fascicolo test: `testatti/licenziamento-fittizio/`

## Step 1 — Qualificazione rapporto

| Elemento | Valore |
| --- | --- |
| Data assunzione | |
| Qualifica / livello CCNL | |
| Periodo prova | esaurito sì/no |
| Part-time / somministrazione | |
| Tutele rinforzate (dirigenti, rappresentanti) | `[da verificare]` |

## Step 2 — Tipologia licenziamento

| Tipo | Elementi da verificare |
| --- | --- |
| Giusta causa | Grave inadempimento, contestazione, proporzionalità `[da verificare]` |
| Giustificato motivo oggettivo | Ragioni economiche/organizzative, criteri, riallocazione `[da verificare]` |
| Giustificato motivo soggettivo | Performance, assenze, procedimento |
| Disciplinare / contrattuale | CCNL, regolamento aziendale |

**Output bozza:** qualificazione proposta + grado di confidenza (alta/media/bassa).

## Step 3 — Procedimento

- [ ] Contestazione fatti e termini per difese `[da verificare]`
- [ ] Audizione / contraddittorio se dovuto
- [ ] Consultazione sindacale / procedura collettiva se applicabile `[da verificare]`
- [ ] Art. 18 — autorizzazione/licenziamento nullo se soglie superate `[da verificare]`
- [ ] Tutele COVID / settoriali eventuali `[da verificare]`

## Step 4 — Forma e contenuto lettera

- Motivazione sufficiente per il tipo scelto?
- Data efficacia, preavviso/indennità sostitutiva `[da verificare]`
- TFR e documenti fine rapporto
- Clausole post-contrattuali (non concorrenza) — validità `[da verificare]`

## Step 5 — Termini impugnazione

Calcolo **provvisorio** — obbligo verifica su fonti:

- Decorrenza da comunicazione / consegna
- Rito: giudizio del lavoro `[da verificare]`
- Prescrizione azioni

## Step 6 — Prove e rischi

| Rischio | Livello | Mitigazione bozza |
| --- | --- | --- |
| Insufficienza motivazione | | |
| Vizio procedimento art. 18 | | |
| Discriminazione / riparatoria | | |
| Reintegra / indennità sostitutiva | | `[da verificare]` |

## Step 7 — Output

1. **Memo interno** (2–4 pagine): fatto, diritto, rischi, opzioni (confermare, transazione, contenzioso)
2. **Tabella documenti** mancanti
3. **Checklist rapida** se serve follow-up → `/lavoro:checklist-licenziamento`

## Escalation

- Licenziamenti collettivi, crisi, illeciti penali
- Lavoratori con tutele speciali
- Accertamento INPS/INAIL connesso

## Appendice — Tabella documenti da richiedere

| Documento | Perché |
| --- | --- |
| Contratto e integrazioni | Qualifica, livello |
| Ultime 12 buste paga | Retribuzione, assenze |
| Cartellino / presenze | Contestazioni assenza |
| Procedimenti disciplinari precedenti | Proporzionalità |
| Email/PEC HR rilevanti | Contestazioni |
| Organigramma | LMO se applicabile `[da verificare]` |

## Appendice — Memo struttura (estratto)

```markdown
## Sintesi
## Fatto (cronologia)
## Qualificazione licenziamento
## Procedimento
## Art. 18 / tutele
## Termini
## Rischi e quantum indicativo [da verificare]
## Raccomandazioni
```

## Appendice — EN termination-review parity (checklist estesa)

| Area EN | Copertura IT skill |
| --- | --- |
| High-risk flags | art. 18, tutele, gravidanza/maternità `[da verificare]` |
| Documentation | cartella disciplinare completa |
| Alternatives | transazione, concordato, rientro |
| Client communication | memo per HR vs lettera dipendente |

## Appendice — Comunicazione datore (bozza bullet)

- Conferma motivazione scelta e coerenza con precedenti disciplinari
- Verifica assistenza legale interna/esterna
- Piano comunicazione uscita e accesso sistemi post-licenziamento

## Appendice — Post-licenziamento

| Task | Owner |
| --- | --- |
| TFR e documenti cessazione | HR |
| Comunicazioni INPS | `[da verificare]` |
| DSAR dipendente | `/privacy-gdpr:risposta-diritti-interessato` |
| Fascicolo chiusura | `/lavoro:fascicolo-lavoro` |

## Divieti

- Non consigliare al dipendente azioni senza avvocato
- Non citare numeri sentenza senza fonte utente

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
