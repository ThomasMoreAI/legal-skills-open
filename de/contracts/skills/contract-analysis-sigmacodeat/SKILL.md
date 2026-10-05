---
name: contract-analysis-sigmacodeat
title: Contract Analysis Skill
description: 'Analyzes contracts (Verträge) for risks, unusual clauses, missing provisions,

  and enforceability issues under DE/AT/CH/EU law. Input: contract text or

  brain slug. Output: clause-by-clause risk matrix, red flags, recommended

  changes, and an overall risk score (low/medium/high/critical).

  Marks all conclusions as requiring attorney review.'
author: Sigmacodeat
author_url: https://github.com/Sigmacodeat/Sigmabrain/tree/main/server/skills/contract-analysis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: en
---

# Contract Analysis Skill

> **Warning:** AI-generated contract analysis. Attorney review required before reliance.
> **Chains with:** [legal-subsumption](../legal-subsumption/SKILL.md) for specific clause issues.

## Contract

This skill guarantees:
1. Every flagged clause cites the contract section by number/heading
2. Risk ratings are justified with the applicable legal standard
3. Missing standard clauses are identified explicitly
4. AGB-Recht (§§ 305–310 BGB) and DSGVO implications are checked automatically

## Protocol

### Step 1 — Load Contract

If brain slug provided: `gbrain get_page <slug>`
If text provided directly: use as-is

Identify:
- **Contract type**: Kaufvertrag / Dienstvertrag / Werkvertrag / Mietvertrag / NDA / GmbH-Vertrag / Arbeitsvertrag / Lizenzvertrag / Sonstige
- **Parties**: Vertragsparteien, Rollen
- **Governing law**: Rechtswahlklausel (default: DE if not stated)
- **Language**: DE / EN / Bilingual

### Step 2 — Risk Scan

Search brain for known problem clauses:
```
gbrain search "problematische Klausel [contract_type] AGB unwirksam § 307 BGB"
gbrain search "[contract_type] Muster Checkliste Pflichtklauseln"
```

### Step 3 — Clause-by-Clause Analysis

For each material clause, assess:

| Dimension | Question |
|---|---|
| Wirksamkeit | Ist die Klausel wirksam? (§§ 305–310 BGB, § 879 ABGB) |
| Vollständigkeit | Fehlen Standardregelungen? |
| Haftung | Ist die Haftung ausgewogen? |
| Laufzeit/Kündigung | Sind Fristen angemessen? |
| Datenschutz | DSGVO-Konformität (Art. 28, 32, 37 DSGVO)? |
| Gerichtsstand | Ist der Gerichtsstand wirksam vereinbart? |

### Step 4 — Output Format

```markdown
## Vertragsanalyse — [Vertragsbezeichnung] — [Datum]

### Übersicht
- **Vertragstyp:** [Typ]
- **Parteien:** [A] ↔ [B]
- **Anwendbares Recht:** [Jurisdiktion]
- **Gesamtrisiko:** 🟢 Niedrig / 🟡 Mittel / 🔴 Hoch / 🚨 Kritisch

### Klauselmatrix

| Klausel | Bewertung | Risiko | Empfehlung |
|---------|-----------|--------|------------|
| § 1 Vertragsgegenstand | [Text-Zusammenfassung] | 🟢/🟡/🔴 | [Änderungsvorschlag] |
| § 3 Haftung | [Text-Zusammenfassung] | 🔴 | [Konkreter Änderungsvorschlag] |
| ... | | | |

### 🚨 Rote Flaggen (sofort klären)
1. [Klausel X]: [Problem] — [Rechtliche Grundlage]
2. ...

### ⚠️ Fehlende Standardklauseln
- [ ] Höhere Gewalt (force majeure)
- [ ] Schriftformklausel (§ 127 BGB)
- [ ] Salvatorische Klausel
- [ ] [weitere fehlende Klauseln]

### 📋 Empfohlene Änderungen
[Nummerierte Liste mit konkreten Textvorschlägen]

### Nächste Schritte
- [ ] Anwaltliche Überprüfung (insbesondere: [Klauseln])
- [ ] Nachverhandlung: [Punkte]
- [ ] Vor Unterzeichnung klären: [Fragen]

---
⚠️ KI-generierte Analyse. Kein Ersatz für Rechtsberatung.
```

### Step 5 — File Results

```
gbrain put_page \
  --slug "legal/contracts/analysis-[contract-slug]-[date]" \
  --type "legal_document" \
  --metadata '{"document_type": "contract_analysis", "risk_level": "[low|medium|high|critical]"}'
```

## Common Red Flag Patterns

- **Totalausschluss der Haftung**: oft unwirksam (§ 309 Nr. 7 BGB)
- **Einseitige Änderungsvorbehalte**: § 308 Nr. 4 BGB — nur bei berechtigtem Interesse
- **Überraschende Klauseln**: § 305c BGB — werden nicht Vertragsbestandteil
- **Datenweitergabe ohne Rechtsgrundlage**: Art. 6 DSGVO fehlt
- **Gerichtsstand nur für eine Partei günstig**: § 38 ZPO — nur zwischen Kaufleuten
- **Überlange Laufzeiten bei AGB**: § 309 Nr. 9 BGB

## Anti-Patterns

- ❌ Declaring a clause "safe" or "unenforceable" as binding legal advice — flag risks, recommend review.
- ❌ Reviewing only the clauses present while ignoring missing market-standard protections.
- ❌ Losing the source reference for a flagged clause (every finding cites its location).

## Output Format

A clause-by-clause risk report: each finding with severity (low / medium / high),
the clause location, the risk rationale, and a suggested redline — marked as an
AI-assisted analysis requiring legal review.
