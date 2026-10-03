---
name: parere-legale
title: Workflow Parere Legale
description: Redazione parere legale strutturato con citazioni normative verificate e giurisprudenza. Usa quando l'utente chiede un parere, un'opinione legale o un'analisi giuridica su una questione.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/parere-legale
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: litigation
language: it
---

# Workflow Parere Legale

Segui questi step nell'ordine. Usa i tool MCP di Legal IT.

## Step 1 — Analisi del quesito
Identifica:
- **Questione giuridica** principale
- **Norme potenzialmente applicabili** (codice civile, leggi speciali, regolamenti UE)
- **Parti coinvolte** e loro posizioni
- **Fatti rilevanti**

## Step 2 — Verifica normativa
Per OGNI norma che intendi citare nel parere:
1. Chiama `legal-it:cite_law` con il riferimento (es. "art. X legge Y") per ottenere il testo vigente
2. Se serve approfondimento dottrinale: chiama `legal-it:cerca_brocardi`

MAI citare una norma a memoria. Ogni citazione deve avere un `legal-it:cite_law` corrispondente.

## Step 3 — Ricerca giurisprudenziale
Per le questioni controverse o con orientamenti divergenti:
1. Chiama `legal-it:cerca_giurisprudenza` con il tema specifico per trovare le sentenze rilevanti
2. Per le top 2-3 sentenze piu pertinenti: chiama `legal-it:leggi_sentenza` con numero e anno per il testo integrale
3. Identifica l'orientamento prevalente (consolidato, in evoluzione, contrasto)

## Step 4 — Redazione del parere
Struttura il parere nelle seguenti sezioni:

### FATTO
Riassumi i fatti rilevanti come esposti dal cliente.

### DIRITTO
Esponi il quadro normativo applicabile, citando:
- Articoli di legge (con testo recuperato da `legal-it:cite_law`)
- Principi giurisprudenziali (con numero e anno delle sentenze)
- Dottrina rilevante (se emersa da `legal-it:cerca_brocardi`)

### ANALISI
Applica il diritto ai fatti:
- Sussunzione dei fatti nelle fattispecie normative
- Valutazione dei pro e contro per le diverse tesi
- Rischi e incertezze

### CONCLUSIONI
- Risposta al quesito in termini chiari
- Raccomandazioni operative
- Eventuali azioni da intraprendere con tempistiche

## Note
- Ogni norma citata DEVE avere un `legal-it:cite_law` nel transcript
- Ogni sentenza citata DEVE essere stata letta con `legal-it:leggi_sentenza`
- Segnalare chiaramente quando un'interpretazione è controversa
- Distinguere tra orientamento consolidato e orientamento minoritario
