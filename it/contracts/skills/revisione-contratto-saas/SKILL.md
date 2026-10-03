---
name: revisione-contratto-saas
title: Revisione contratto SaaS
description: 'Revisione MSA/licenza SaaS B2B: SLA uptime, dati, subfornitura cloud, exit, limitazione responsabilità. Italia / UE. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-civile/skills/revisione-contratto-saas
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: contracts
language: en
---

# Revisione contratto SaaS

> **Bozza — non consulenza legale.**

## Setup

- Ruolo: cliente SaaS vs fornitore
- `CLAUDE.md` playbook + allegati SLA / DPA

## Matrice SLA

| Metrica | Contratto | Gap | Severity |
| --- | --- | --- | --- |
| Uptime % | | | |
| Esclusioni manutenzione | | | |
| Service credit / penale | | | |
| RTO/RPO backup | | | |
| Support tiers (P1/P2) | | | |

## Dati e portabilità

| Tema | Verifica |
| --- | --- |
| Titolarità dati cliente | |
| Export format (API, CSV) | |
| Cancellazione post-termine | |
| Sub-processors list + notice | |
| Localizzazione dati (UE) | |

## Sicurezza

- Standard dichiarati (ISO 27001, SOC2) — richiedere report **all'utente**, non inventare
- Incident notification → link `/privacy-gdpr:violazione-dati`
- Vulnerability / patch policy

## Commerciali

| Clausola | Nota |
| --- | --- |
| Fee / ramp / true-up | |
| Rinnovo tacito | |
| Price increase cap | |
| Affiliates / group use | |
| Change of control | |

## Limitazione responsabilità

- Esclusione danni indiretti
- Cap annuo (fee 12 mesi?)
- Carve-out: IP breach, dati, dolo

## Privacy obbligatoria

`/privacy-gdpr:revisione-dpa` sullo stesso pacchetto se trattamento dati personali.

## Output

Tabella issue + executive summary + email negoziazione bozza (5 bullet).

## Appendice — Exit e vendor lock-in

| Tema | Domande |
| --- | --- |
| Migrazione dati | Costi, assistenza, tempi |
| Codice custom | Proprietà e portabilità |
| SLA post-terminazione | Accesso read-only |
| Reference customer | Solo se utente fornisce |

## Divieti

- Non attestare certificazioni SOC2 senza documento

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
