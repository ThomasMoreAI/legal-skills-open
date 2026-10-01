---
name: qualificazione-rapporto-pixari
title: Qualificazione rapporto di lavoro
description: Qualificazione rapporto di lavoro vs collaborazione autonoma / parasubordinazione. Ispirato EN worker-classification. Nessuna consulenza legale.
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/lavoro/skills/qualificazione-rapporto
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: employment
language: it
---

# Qualificazione rapporto di lavoro

> **Bozza — non consulenza legale.** Rischio accertamento INPS/Agenzia Entrate `[da verificare]`.

## Input

- Descrizione incarico (compiti, orari, subordinazione, strumenti)
- Parte che chiede: datore vs consulente
- CCNL di riferimento se noto

## Matrice indicatori (bozza)

| Indicatore | Lavoro subordinato | Autonomo |
| --- | --- | --- |
| Orario/luogo imposti | alto | basso |
| Subordinazione gerarchica | alto | basso |
| Strumenti del committente | alto | basso |
| Rischio economico | basso | alto |
| Incarico a persone giuridiche | | spesso autonomo |

## Profili IT tipici

| Profilo | Note |
| --- | --- |
| Dipendente tempo indeterminato/determinato | Contratto + INPS |
| Collaborazione coordinata e continuativa | art. 409 c.p.c. `[da verificare]` — non confondere con lavoro |
| Partita IVA / P.IVA progetto | Contratto d'opera / servizi |
| Somministrazione | Agenzia licenziata |

## Output

1. **Qualificazione proposta** (confidenza alta/media/bassa)
2. **Rischi** (contributi, sanzioni, requalifica)
3. **Documenti suggeriti** (contratto, assicurazione, DURC, …)
4. **Passi** — legale del lavoro / consulente fiscale

## Rimandi

- Assunzione → `/lavoro:hiring-review-lavoro`
- Contenzioso → `/lavoro:revisione-licenziamento`

## Divieti

- Non certificare assenza di rischio accertamento
