---
name: data-breach-capazme
title: Data Breach
description: Gestione data breach GDPR con valutazione rischio, notifica al Garante entro 72h e stima sanzioni. Usa quando l'utente segnala una violazione di dati personali, chiede come gestire un data breach o deve notificare al Garante.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/data-breach
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: it
---

# Data Breach

Valutazione rischio, notifica Garante, stima sanzioni.

## Workflow

### 1. Raccolta dati incidente

Identificare: tipo violazione (confidenzialita/integrita/disponibilita), numero interessati, categorie dati, causa, data scoperta.

### 2. Valutazione rischio

Chiama `legal-it:valutazione_data_breach`:
- Livello rischio per interessati
- Obbligo notifica Garante (art. 33 GDPR)
- Obbligo comunicazione interessati (art. 34 GDPR)

### 3. Notifica al Garante

Se necessaria: chiama `legal-it:genera_notifica_data_breach`.

**SCADENZA**: 72 ore dalla scoperta.

### 4. Stima sanzioni

Chiama `legal-it:calcolo_sanzione_gdpr` con criteri art. 83(2) GDPR.

### 5. Piano d'azione

1. Contenere la violazione
2. Documentare nel registro violazioni (art. 33(5))
3. Notificare al Garante (se rischio non improbabile)
4. Comunicare agli interessati (se rischio elevato)
5. Misure correttive
