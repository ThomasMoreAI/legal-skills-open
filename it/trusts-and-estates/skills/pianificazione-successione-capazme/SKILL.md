---
name: pianificazione-successione-capazme
title: Pianificazione Successione
description: Pianifica una successione ereditaria con calcolo quote legittime, imposte di successione, franchigie e adempimenti. Usa quando l'utente chiede di calcolare quote ereditarie, imposte successione, eredita, testamento, franchigia o donazione.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/pianificazione-successione
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: trusts-and-estates
language: it
---

# Pianificazione Successione

Quote ereditarie, imposte e adempimenti.

## Workflow

### 1. Quote ereditarie

Chiama `legal-it:calcolo_eredita` con massa_ereditaria (valore totale dell'asse in €) ed eredi (dict: {'coniuge': bool, 'figli': int, 'ascendenti': bool, 'fratelli': int}).

### 2. Imposte di successione

Chiama `legal-it:imposte_successione` con valore_beni, parentela (uno tra 'coniuge_linea_retta', 'fratelli_sorelle', 'parenti_fino_4_grado_affini_fino_3', 'altri'), immobili (bool), prima_casa (bool).
- Aliquota per grado di parentela
- Franchigia (1M coniuge/figli, 100K fratelli)
- Imposte ipotecaria (2%) e catastale (1%) se immobili

### 3. Imposte compravendita (se immobili da vendere)

Chiama `legal-it:imposte_compravendita`.

## Adempimenti da indicare

- Dichiarazione successione: entro 12 mesi
- Voltura catastale: entro 30 giorni
- Accettazione eredita: con beneficio d'inventario se opportuno
