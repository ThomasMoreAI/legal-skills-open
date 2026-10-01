---
name: revisione-msa-fornitore-pixari
title: Revisione MSA fornitore
description: Revisione MSA master + ordini (SaaS/fornitura). Unisce SaaS e vendor EN. Nessuna consulenza legale.
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-civile/skills/revisione-msa-fornitore
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: contracts
language: it
---

# Revisione MSA fornitore

> **Bozza — non consulenza legale.**

## Ordine precedenza

1. MSA master
2. SOW / ordini
3. DPA privacy
4. SLA allegato

## Workflow

1. `/diritto-civile:revisione-contratto-saas` su SLA e dati
2. `/diritto-civile:revisione-fornitore` su consegna/garanzie
3. `/privacy-gdpr:revisione-dpa` se dati
4. `/diritto-civile:escalation-clausole` su red flags

## Output

Tabella issue unificata per pacchetto commerciale.

## Divieti

- Non ignorare conflitto MSA vs ordine successivo
