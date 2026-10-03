---
name: escalation-clausole
title: Escalation clausole
description: Flag clausole ad alto rischio per escalation interna (socio, DPO, assicurazione). EN escalation-flagger. Nessuna consulenza legale.
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-civile/skills/escalation-clausole
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: contracts
language: it
---

# Escalation clausole

> **Bozza — non consulenza legale.**

## Trigger automatici (bozza)

| Clausola | Severity | Escalation a |
| --- | --- | --- |
| Penale > soglia playbook | alta | socio |
| Cap responsabilità < fee annua | alta | socio |
| Foro estero non accettabile | alta | legale |
| Dati personali senza DPA | alta | DPO |
| Arbitrato ICC senza review | media | socio |
| Change of control | media | legale M&A |

## Output

Email/memo interno: "non firmare senza X" + clausole citate.

## Divieti

- Non sostituire approval committee
