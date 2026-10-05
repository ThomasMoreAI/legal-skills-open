---
name: legal-beweislage-sigmacodeat
title: Legal-Beweislage Skill
description: 'Analyzes evidence in a legal case: evaluates strengths and weaknesses,

  identifies gaps, assesses admissibility, and recommends evidence

  gathering. Produces an evidence board summary with weighted items

  and source verification.'
author: Sigmacodeat
author_url: https://github.com/Sigmacodeat/Sigmabrain/tree/main/server/skills/legal-beweislage
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: en
---

# Legal-Beweislage Skill

## When To Use

- The user asks about evidence in a case
- The user wants to know what evidence is missing
- The user needs an evidence strength assessment
- Before filing, to verify proof completeness

## Protocol

### Step 1 — Load Case Evidence

Search the brain for the case and extract the `evidence` frontmatter array:
```
gbrain search "<case>" --type legal-case
```

### Step 2 — Categorize Evidence

Group by type:
- **Documentary**: Contracts, emails, invoices, reports
- **Testimonial**: Witness statements, expert opinions
- **Physical**: Objects, photos, videos
- **Digital**: Server logs, metadata, blockchain records
- **Circumstantial**: Indirect evidence establishing facts

### Step 3 — Evaluate Each Item

| Criterion | Weight |
|---|---|
| Relevance | High |
| Authenticity | High |
| Admissibility | High |
| Corroboration | Medium |
| Chain of custody | High (for physical) |

Score each item 0-1 and flag gaps.

### Step 4 — Identify Gaps

Common gaps:
- Missing documentary evidence (no written contract)
- Witness unavailable (moved, died, hostile)
- Chain of custody broken
- Digital evidence without hash verification
- Hearsay without exception

### Step 5 — Recommend Actions

1. **Gather** — obtain missing documents
2. **Preserve** — secure digital evidence
3. **Corroborate** — find supporting evidence
4. **Challenge** — prepare to exclude opponent's weak evidence

## Output Format

```
## Beweislage — [Case Title]

### Beweismittel-Übersicht

| # | Typ | Beschreibung | Stärke | Status |
|---|---|---|---|---|
| 1 | Dokument | [Desc] | ★★★★☆ | ✅ Vorhanden |
| 2 | Zeuge | [Desc] | ★★☆☆☆ | ⚠️ Unvollständig |

### Beweislücken
1. [Gap] — [Severity]
2. [Gap] — [Severity]

### Empfohlene Maßnahmen
1. [Action]
2. [Action]

### Gesamtbewertung
[Summary]
```

## Anti-patterns

- Never ignore chain-of-custody issues
- Never overstate weak evidence
- Never omit contradictory evidence
- Always flag authentication issues

## Contract

1. Each asserted fact is mapped to its evidence (or marked as unsupported) with the source.
2. The burden of proof (Beweislast) per claim element is stated.
3. The assessment supports, never replaces, the lawyer's evidentiary judgment.

## Anti-Patterns

- ❌ Treating an unsupported assertion as proven.
- ❌ Losing the link between a fact and its evidence document.
- ❌ Assigning the Beweislast without naming the norm it follows from.

## Output Format

A Beweislage matrix: claim element · burden of proof · supporting evidence (with source)
· strength (stark / mittel / schwach / fehlt) · gaps — marked as AI-assisted, lawyer to verify.
