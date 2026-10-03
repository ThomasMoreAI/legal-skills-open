---
name: verifica-prescrizione
title: Verifica Prescrizione
description: Verifica la prescrizione di un diritto civile o di un reato penale con calcolo termine, analisi cause di sospensione/interruzione e stato attuale. Usa quando l'utente chiede se un diritto e prescritto, i termini di prescrizione, o la decadenza di un'azione.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/verifica-prescrizione
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: litigation
language: en
---

# Verifica Prescrizione

Calcolo termine prescrizione civile o penale.

## Workflow

### Civile

Chiama `legal-it:prescrizione_diritti`:
- **10 anni**: ordinaria (tipo_diritto='ordinaria', art. 2946 c.c.)
- **5 anni**: risarcimento danni (tipo_diritto='risarcimento_danni', art. 2947 c.c.)
- **2 anni**: danno da circolazione veicoli / RCA (tipo_diritto='risarcimento_rca', art. 2947 c.2 c.c.)

Verifica sospensione (artt. 2941-2942) e interruzione (art. 2943).

### Penale

Chiama `legal-it:prescrizione_reato`:
- Termine = massimo edittale (min 6 anni delitto, 4 contravvenzione)
- Sospensione (art. 159 c.p.) e interruzione (art. 160 c.p.)
- Riforma Cartabia: improcedibilita in appello/cassazione

## Output: stato PRESCRITTA / NON PRESCRITTA / IN SCADENZA con data esatta.
