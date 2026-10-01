---
name: quantificazione-danni-capazme
title: Quantificazione Danni
description: Quantifica danni biologici, patrimoniali o morali con personalizzazione e attualizzazione monetaria. Usa quando l'utente chiede di calcolare un risarcimento, quantificare danni da invalidita, danno emergente, lucro cessante o danno morale/esistenziale.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/quantificazione-danni
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: personal-injury
language: it
---

# Quantificazione Danni

Calcolo base, personalizzazione e attualizzazione.

## Workflow

### 1. Calcolo base

**Biologico** (percentuale invalidita):
- <= 9%: `legal-it:danno_biologico_micro` (tabelle art. 139 CdA)
- > 9%: `legal-it:danno_biologico_macro` (tabelle Milano)

**Patrimoniale** (importo):
- Danno emergente + lucro cessante
- `legal-it:interessi_legali` dalla data evento

**Morale/esistenziale**:
- `legal-it:danno_non_patrimoniale` come base

### 2. Personalizzazione

Criteri Cass. SS.UU. 26972/2008: sofferenza soggettiva, vita di relazione, specificita del caso.

### 3. Attualizzazione

1. `legal-it:rivalutazione_monetaria` dalla data evento
2. `legal-it:interessi_legali` sulla somma rivalutata
