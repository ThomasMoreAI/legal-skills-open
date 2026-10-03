---
name: mappatura-normativa
title: Mappatura Normativa
description: Costruisce la mappa normativa completa di un settore o attivita con fonti organizzate per livello gerarchico e matrice adempimenti. Usa quando l'utente chiede il quadro normativo completo di un settore, tutte le leggi applicabili a un'attivita, o una checklist di obblighi normativi.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/mappatura-normativa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: litigation
language: it
---

# Mappatura Normativa

Mappa completa delle fonti per settore/attivita, organizzata per gerarchia.

## Workflow

### 1. Fonti per livello

Per ogni livello, chiama `legal-it:cite_law` su ogni articolo fondamentale:
1. **Costituzione** — articoli rilevanti
2. **UE** — regolamenti e direttive con D.Lgs. di recepimento
3. **Nazionale** — codici, testi unici, leggi, D.Lgs.
4. **Secondarie** — D.M., autorita indipendenti, linee guida

### 2. Fonti autorita vigilanza

- Settori finanziari: `legal-it:cerca_delibere_consob`
- Privacy: `legal-it:cerca_provvedimenti_garante`

### 3. Matrice adempimenti

| Obbligo | Fonte | Soggetto | Termine | Sanzione |
|---------|-------|----------|---------|----------|
| ... | ... | ... | ... | ... |
