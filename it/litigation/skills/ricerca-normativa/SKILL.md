---
name: ricerca-normativa
title: Ricerca Normativa
description: Ricerca normativa completa su un tema giuridico con tutte le fonti applicabili ordinate per gerarchia, giurisprudenza e quadro sanzionatorio. Usa quando l'utente chiede quali norme si applicano, il quadro normativo di un settore, le fonti di una materia o una ricerca legislativa.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/ricerca-normativa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: litigation
language: it
---

# Ricerca Normativa

Fonti primarie, norme collegate, giurisprudenza e sanzioni.

## Regola fondamentale

**Ogni norma citata DEVE essere verificata con `legal-it:cite_law`**. Mai citare a memoria.

## Workflow

### 1. Fonti primarie

Per ogni norma individuata, chiama `legal-it:cite_law`. Ordina per gerarchia:
1. Costituzione
2. Regolamenti UE
3. Direttive UE (+ D.Lgs. recepimento)
4. Leggi ordinarie / D.Lgs. / D.L.
5. D.M. e regolamenti
6. Circolari e prassi

### 2. Norme collegate

Per ogni norma primaria: attuazione, modifiche, abrogazioni, disposizioni transitorie.

### 3. Giurisprudenza

`legal-it:cerca_brocardi` per massime. `legal-it:cerca_giurisprudenza` per approfondimento.

### 4. Fonti autorita vigilanza

- Finanza/mercati: `legal-it:cerca_delibere_consob`
- Privacy: `legal-it:cerca_provvedimenti_garante`
