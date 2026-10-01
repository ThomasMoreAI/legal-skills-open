---
name: causa-civile-capazme
title: Causa Civile
description: Pianifica una causa civile con calcolo contributo unificato, scadenze processuali post-Cartabia, termini impugnazione e preventivo costi. Usa quando l'utente chiede di avviare una causa, calcolare costi giudiziali, verificare termini processuali o preparare un preventivo per il cliente.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/causa-civile
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: litigation
language: it
---

# Causa Civile

Pianificazione completa: costi, scadenze, preventivo.

## Workflow

### 1. Contributo unificato

Chiama `legal-it:contributo_unificato` con valore_causa, tipo_procedimento (es. cognizione, lavoro, monitorio) e grado (primo/appello/cassazione).

### 2. Scadenze processuali

Chiama `legal-it:scadenza_processuale` per i termini in base al rito:
- **Ordinario**: comparsa risposta (70gg), memorie art. 171-ter c.p.c.
- **Sommario**: costituzione resistente, mutamento rito
- **Lavoro**: ricorso, memoria difensiva

Sospensione feriale: 1-31 agosto.

### 3. Impugnazioni

Chiama `legal-it:scadenze_impugnazioni`:
- Primo -> appello: 30gg (breve) / 6 mesi (lungo)
- Appello -> cassazione: 60gg (breve) / 6 mesi (lungo)

### 4. Preventivo

Chiama `legal-it:preventivo_civile` con range compenso per fase.

## Note
- Mediazione obbligatoria (D.Lgs. 28/2010)
- Negoziazione assistita (D.L. 132/2014)
