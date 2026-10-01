---
name: novita-consob-capazme
title: Novita CONSOB
description: Riepilogo delle ultime delibere e provvedimenti CONSOB con sintesi orientamenti per tipologia o argomento. Usa quando l'utente chiede le ultime novita CONSOB, delibere recenti, aggiornamenti sui mercati finanziari o provvedimenti recenti dell'autorita di vigilanza.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/novita-consob
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: securities
language: it
---

# Novita CONSOB

Ultime delibere con sintesi orientamenti.

## Workflow

### 1. Ultime delibere

Chiama `legal-it:ultime_delibere_consob` con eventuali filtri (tipologia, argomento).

### 2. Approfondimento

Per le 2-3 delibere piu rilevanti: `legal-it:leggi_delibera_consob` con numero.

### 3. Quadro normativo

Per le norme richiamate: `legal-it:cite_law`.

## Output atteso

### Panoramica
Tendenze emergenti dai provvedimenti recenti.

### Per ciascuna delibera letta:
- **Oggetto**
- **Norme di riferimento**
- **Decisione/Sanzione**
- **Rilevanza pratica**

### Tendenze e indicazioni
Sintesi orientamenti dalle delibere piu recenti.
