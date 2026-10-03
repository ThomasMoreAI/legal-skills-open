---
name: redazione-contratto
title: Redazione Contratto
description: Supporto alla redazione contrattuale con verifica normativa, clausole tipo e compliance GDPR. Usa quando l'utente chiede di redigere, revisionare, analizzare un contratto, verificare clausole o predisporre un accordo.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/redazione-contratto
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: litigation
language: it
---

# Redazione Contratto

Schema clausole con fondamento normativo e compliance GDPR.

## Workflow

### 1. Quadro normativo

Chiama `legal-it:cite_law` per le norme del tipo contrattuale:
- Norme generali (artt. 1321-1469 c.c.)
- Norme specifiche del tipo (es. locazione artt. 1571 ss.)
- Legislazione speciale (Cod. Consumo per B2C)

Per orientamenti: `legal-it:cerca_brocardi` sulle norme chiave.

### 2. Clausole essenziali

Sulla base del quadro normativo:
- Elementi essenziali (art. 1325 c.c.)
- Clausole specifiche del tipo
- Garanzie e limitazione responsabilita
- Clausole risolutive e penali
- Foro e legge applicabile

### 3. Compliance GDPR (se dati personali)

Se il contratto prevede trattamento dati:
1. `legal-it:analisi_base_giuridica` per la base giuridica
2. `legal-it:genera_dpa` se una parte e responsabile del trattamento (art. 28)

### 4. Verifica vessatorieta (B2C)

Per contratti con consumatori: verificare clausole vessatorie (artt. 33-38 Cod. Consumo).

## Output

Schema clausole con: titolo, contenuto, fondamento normativo, note operative.

**Non redigere un contratto completo** — fornire schema e clausole chiave con fondamento normativo.
