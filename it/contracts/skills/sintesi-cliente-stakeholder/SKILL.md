---
name: sintesi-cliente-stakeholder
title: Sintesi cliente / stakeholder
description: Executive summary non tecnica da atti, bozze contratto o pareri per cliente/management. Linguaggio chiaro, rischi in plain language. Nessuna consulenza legale.
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-civile/skills/sintesi-cliente-stakeholder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: contracts
language: it
---

# Sintesi cliente / stakeholder

> **Bozza — non consulenza legale.** Non per invio esterno senza revisione avvocato.

## Input

- Documento sorgente (revisione contratto, subsunzione, cronologia)
- Destinatario: board, CEO, investitore, socio non legale

## Struttura (max 2 pagine)

### 1. In sintesi (3 bullet)

- Decisione richiesta
- Rischio principale in una frase
- Raccomandazione bozza

### 2. Contesto

Un paragrafo: chi, cosa, quando.

### 3. Cosa va bene / cosa preoccupa

| Tema | Valutazione qualitativa |
| --- | --- |
| | OK / Attenzione / Critico |

### 4. Rischi business

| Rischio | Probabilità | Impatto €/reputazione |
| --- | --- | --- |
| | bassa/media/alta | |

### 5. Prossimi passi

| Azione | Owner | Entro |
| --- | --- | --- |
| | | |

### 6. Disclaimer

Bozza AI; verifiche legali pendenti; non consulenza.

## Stile

- Evitare "art. 1453" senza spiegazione
- `[da verificare]` → "da confermare con il legale"
- Importi solo se nel sorgente

## Appendice — Tono per destinatario

| Destinatario | Tono |
| --- | --- |
| Board | Decisione + rischio € |
| CEO | 1 pagina max |
| Investitore | Focus deal-breaker |

## Appendice — Cosa omettere

- Citazioni estese di articoli
- Strategie processuali dettagliate
- Nomina controparti se non necessaria al decisore

## Divieti

- Non nascondere rischi alti
- Non promettere esito giudizio

## Appendice — Coordinamento e chiusura

### Skill correlati

Usare insieme agli altri plugin del marketplace `pixari-italian-legal-skills` per profilo completo.

### Verifica output

Ogni sezione normativa senza fonte utente deve contenere `[da verificare]`.

### Revisione

Nessun documento va inviato a controparte, Garante, giudice o dipendente senza revisione umana.

### Test senza dati reali

Fascicoli in `testatti/` — solo personaggi inventati.

### Domande finali all'utente

- Documenti mancanti?
- Scadenza operativa?
- Chi approva in studio (socio, DPO, HR)?
- Output tecnico o per cliente?
- Follow-up skill consigliato?
