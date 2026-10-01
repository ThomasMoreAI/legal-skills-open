---
name: confronto-norme-capazme
title: Confronto Norme
description: Confronta due o piu norme evidenziando differenze, sovrapposizioni, criteri di prevalenza e coordinamento. Usa quando l'utente chiede di confrontare articoli, verificare quale norma prevale, risolvere un conflitto normativo o capire il rapporto tra due disposizioni.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/confronto-norme
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: it
---

# Confronto Norme

Differenze, sovrapposizioni, prevalenza e coordinamento.

## Workflow

### 1. Recupero testi

Chiama `legal-it:cite_law` per ciascuna norma. Per annotazioni: `legal-it:cerca_brocardi`.

### 2. Analisi comparativa

Confronta su: ambito oggettivo, soggettivo, presupposti, effetti, sanzioni.

### 3. Rapporto tra le norme

- **Specialita** (lex specialis)
- **Successione** (lex posterior)
- **Gerarchia** (rango)
- **Concorso** (applicazione contemporanea)
- **Complementarieta**

### 4. Giurisprudenza sul coordinamento

Dalle annotazioni, individua pronunce sul rapporto tra le norme.
