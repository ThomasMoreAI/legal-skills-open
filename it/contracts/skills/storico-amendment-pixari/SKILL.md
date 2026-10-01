---
name: storico-amendment-pixari
title: Storico amendment contratto
description: Ricostruisce storico amendment / versioni contratto, conflitti tra allegati. EN amendment-history. Nessuna consulenza legale.
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-civile/skills/storico-amendment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: contracts
language: it
---

# Storico amendment contratto

> **Bozza — non consulenza legale.**

## Input

- Versioni contratto (date, autore bozza)
- Email/PEC negoziazione
- Ordine di precedenza clausole

## Workflow

1. Timeline versioni (tabella data / file / modifiche principali)
2. Matrice diff concettuale (non sostituisce diff legale automatizzato cieco)
3. **Conflitti** tra clausola master e allegato successivo
4. Clausole ancora vigenti vs superate
5. Raccomandazione: quale versione firmare / integrare

## Output

`storico_amendment_<nome>.md` + elenco punti aperti negoziazione.

## Collegamento

`/diritto-civile:fascicolo-civile` per matter strutturato.

## Divieti

- Non inventare versioni non fornite
