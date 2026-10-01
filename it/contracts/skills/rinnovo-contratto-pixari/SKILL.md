---
name: rinnovo-contratto-pixari
title: Rinnovo contratto
description: Analisi rinnovo tacito / scadenza contratto, preavviso, rinegoziazione. EN renewal-tracker. Nessuna consulenza legale.
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-civile/skills/rinnovo-contratto
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: contracts
language: it
---

# Rinnovo contratto

> **Bozza — non consulenza legale.**

## Checklist

- [ ] Data scadenza / rinnovo tacito
- [ ] Preavviso richiesto (giorni)
- [ ] Indicizzazione prezzo al rinnovo
- [ ] Opt-out window
- [ ] Clausole sopravvivenza (confidenzialità, limitazione, foro)

## Output

Timeline azioni (alert T-90, T-60, T-30) + bozza lettera rinegoziazione.

## Divieti

- Non calcolare date senza testo contratto
