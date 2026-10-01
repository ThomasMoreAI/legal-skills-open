---
name: citazione-italiana-pixari
title: Citazione italiana
description: 'Regole citazione diritto italiano ed europeo: norme, Cass., merito, Corte cost., UE, Garante, AE. Tier [da verificare]. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-italiano-hub/skills/citazione-italiana
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: it
---

# Citazione italiana

## Principio

- **Mai** inventare estremi di sentenza o comma non verificato.
- Senza fonte live utente: **`[da verificare]`** (obbligatorio).

## Tier di verifica (per il revisore)

| Tag | Uso |
| --- | --- |
| `[da verificare]` | Tutto ciò che non viene da documento/tool utente |
| `[fonte utente]` | Estratto fornito dall'utente — rischio errore trascrizione |
| `[database]` | Se utente indica DeJure/Lexis con estremi |

## Norme italiane

Formato:

`art. X, comma Y, l. / d.lgs. / d.P.R. n. … del …`

- Data del **fatto** o del **quesito** per vigore
- Multivigenza / novella: segnala `[da verificare]`
- URN Normattiva quando utente fornisce link — non costruire URN inventati

## Unione europea

- Regolamento (UE) n. …/…
- Direttiva: recepimento italiano se rilevante
- CGUE: causa, data, estremi + `[da verificare]`

## Giurisprudenza

| Organo | Formato minimo |
| --- | --- |
| Cass. civ./pen./lav. | Sez., sent./ord., data, n. |
| Sezioni unite | Esplicitare |
| Merito | Trib./C.A., città, estremi |
| Corte cost. | sent./ord., data, n. |
| TAR / Cons. Stato | `[da verificare]` estremi |
| Giudice pace / UE | se applicabile |

## Prassi amministrative

- Garante privacy: provvedimenti e linee — `[da verificare]`
- Agenzia Entrate: circolari — orientamento, non legge
- CNF: deontologia

## Cosa non fare

- Non incollare articoli interi da memoria modello
- Non usare "è consolidato" senza fonte
- Non citare "Cass. recente" senza numero

## Checklist pre-consegna

- [ ] Ogni norma ha estremi e vigore?
- [ ] Ogni sentenza verificata o `[da verificare]`?
- [ ] Reg. UE con numero ufficiale?
- [ ] Disclaimer bozza presente?

## Applicazione

Esegui questa skill **prima** di consegnare output di `metodo-giuridico` o skill verticali.

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
