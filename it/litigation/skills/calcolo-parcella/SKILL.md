---
name: calcolo-parcella
title: Calcolo Parcella
description: Calcola la parcella dell'avvocato per attivita civile, penale o stragiudiziale secondo il D.M. 55/2014 con nota spese completa. Usa quando l'utente chiede compenso avvocato, notula, preventivo legale, parcella professionale o fattura per prestazione legale.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/calcolo-parcella
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: litigation
language: it
---

# Calcolo Parcella

Compenso avvocato D.M. 55/2014 con nota spese.

## Workflow

### 1. Calcolo compenso

| Tipo | Tool |
|------|------|
| Civile | `legal-it:parcella_avvocato_civile` |
| Penale | `legal-it:parcella_avvocato_penale` |
| Stragiudiziale | `legal-it:parcella_stragiudiziale` |
| Vol. giurisdizione | `legal-it:parcella_volontaria_giurisdizione` |

### 2. Nota spese

Chiama `legal-it:nota_spese` per il prospetto: compenso per fase, spese generali (15%), CPA (4%), IVA (22%).

## Output atteso

| Fase | Minimo | Medio | Massimo |
|------|--------|-------|---------|
| Studio | ... | ... | ... |
| Introduttiva | ... | ... | ... |
| Istruttoria | ... | ... | ... |
| Decisionale | ... | ... | ... |
| **Totale** | **...** | **...** | **...** |
