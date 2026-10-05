---
name: compila-quadro-730-gsaccardi
title: Compila Quadro 730
description: 'Guide the user through filling in any quadro (section) of the Italian Modello 730 precompilato. Covers all main quadri: A (terreni), B (fabbricati), C (lavoro dipendente), D (lavoro autonomo), E (oneri detraibili/deducibili), F (acconti/crediti/ritenute), G (crediti d''imposta), H (coniuge), M (imposte sostitutive), and more. Use this skill when a user asks how to fill in a specific section of the 730, what data goes where, or needs step-by-step guidance for a quadro they are unsure about.'
author: gsaccardi
author_url: https://github.com/gsaccardi/dichiarino-mcp/tree/main/skills/compila-quadro-730
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: tax
language: en
sources:
- title: Quadri
  path: references/QUADRI.md
---

# Compila Quadro 730

Step-by-step guide for filling in any section (quadro) of the **Modello 730 Precompilato**.

## When to activate

Activate when the user asks:
- "Come compilo il quadro C?"
- "Dove inserisco gli interessi sul mutuo?"
- "Ho un affitto: quale quadro devo usare?"
- "Cosa va nel rigo E8/E10?"

---

## Quick quadro reference

| Quadro | Contenuto | Fonte dati principale |
|--------|-----------|----------------------|
| **A** | Terreni | Visura catastale, contratti d'affitto |
| **B** | Fabbricati / abitazione | Visura, IMU, contratti |
| **C** | Lavoro dipendente / pensione | Certificazione Unica (CU) |
| **D** | Lavoro autonomo / altri redditi | Fatture, CU autonomi |
| **E** | Oneri detraibili e deducibili | Scontrini, fatture, ricevute |
| **F** | Acconti, ritenute, eccedenze | CU, F24, dichiarazione precedente |
| **G** | Crediti d'imposta | Comunicazioni Agenzia Entrate |
| **H** | Dati del coniuge (dichiarazione congiunta) | Dati anagrafici coniuge |
| **I** | Abitazione principale (deduzione IMU) | F24 IMU |
| **L** | Frontalieri e lavoratori all'estero | CU, contratto estero |
| **M** | Imposte sostitutive (opzione cedolare secca) | Contratto d'affitto |
| **T** | Plusvalenze da cessione partecipazioni | Estratti conto broker |
| **W** | Investimenti esteri / monitoraggio fiscale | Documenti patrimoniali esteri |

---

## Step-by-step instructions

### 1 - Identify the quadro

Ask the user which quadro they need help with, or infer it from context.

### 2 - Use Dichiarino MCP (if available)

```
guida_compilazione_quadro(nome_quadro="C")
→ Returns: campi, istruzioni, note, documenti_necessari
```

Also useful:
```
lista_documenti_spesa(tipo_spesa="interessi_mutuo")
→ Returns required documents for each expense type
```

### 3 - Guide the user field by field

For each rigo (row) of the quadro:
1. State the **rigo number** and its label
2. Explain **what data to enter** and from which document
3. Note any **limits, codes, or checkboxes**
4. Flag **common mistakes**

### 4 - Detailed guidance per quadro

See [references/QUADRI.md](references/QUADRI.md) for field-by-field breakdown of the most common quadri.

---

## Common scenarios

**Scenario A - Lavoratore dipendente standard**
- Quadro C: copy from CU boxes 1, 21, 22, 23, 24 → righi C1, C9, C10
- Quadro F: ritenute already pre-filled; verify rigo F2 matches CU box 21

**Scenario B - Affitto con cedolare secca**
- Quadro B: insert immobile, check "cedolare secca" flag, enter canone
- Quadro M: confirm aliquota (21% ordinaria, 10% concordato)

**Scenario C - Interessi mutuo prima casa**
- Quadro E, rigo E7: insert interessi passivi (max €4.000), rate 19%
- Documents: attestato interessi banca, atto di mutuo, rogito

**Scenario D - Spese sanitarie**
- Quadro E, righi E1–E3: sum all spese sanitarie; franchigia €129,11 applies
- Only deduct the excess: if total = €500 → deduct 19% × (500 − 129.11)

---

## Edge cases

- **Pre-filled data incorrect**: guide user to modify the field and add a note
- **Multiple CUs** (two employers in same year): sum righi C1 values, attach both CUs
- **Reddito estero**: declare in Quadro C with foreign tax credit in Quadro G
- **Immobile inagibile**: Quadro B with 50% rendita catastale reduction, insert code "2"
