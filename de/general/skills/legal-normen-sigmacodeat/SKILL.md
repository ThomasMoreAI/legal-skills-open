---
name: legal-normen-sigmacodeat
title: Legal-Normen Skill
description: 'Searches and interprets legal norms (statutes, regulations, ordinances)

  for a given legal question. Finds relevant provisions, interprets them

  in context, and cross-references with case law. Supports DE, AT, CH, EU.'
author: Sigmacodeat
author_url: https://github.com/Sigmacodeat/Sigmabrain/tree/main/server/skills/legal-normen
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: en
---

# Legal-Normen Skill

## When To Use

- The user asks about a specific statute or provision
- The user needs to know which law applies to a situation
- The user wants interpretation of a legal norm

## Protocol

### Step 1 — Identify the Legal Question

Determine:
- Subject matter
- Jurisdiction
- Time period (for temporal applicability)

### Step 2 — Search the Brain

Search for relevant norms in the brain:
```
gbrain search "<legal-question>" --type statute
```

Also check law-corpus:
```
gbrain search "<keyword>" law-corpus/<jurisdiction>
```

### Step 3 — Find Relevant Provisions

Extract:
- Applicable statute
- Relevant sections/paragraphs
- Temporal scope
- Material scope

### Step 4 — Interpret in Context

Apply standard interpretation methods:
1. **Grammatical** — literal meaning of the text
2. **Systematic** — position within the legal system
3. **Teleological** — purpose and intent
4. **Historical** — legislative history

### Step 5 — Cross-Reference Case Law

Search for relevant court decisions:
```
gbrain search "<provision>" --type court_decision
```

## Output Format

```
## Relevante Normen — [Legal Question]

### Anwendbare Vorschrift
**Gesetz:** [Name]
**Paragraph:** [Section]
**Wortlaut:**
> [Text]

### Auslegung
- **Grammatisch:** [Interpretation]
- **Systematisch:** [Interpretation]
- **Teleologisch:** [Interpretation]

### Rechtsprechung
| Gericht | Datum | Entscheidung |
|---|---|---|
| [Court] | [Date] | [Holding] |

### Ergebnis
[Conclusion]
```

## Anti-patterns

- Never ignore temporal applicability
- Never omit contradictory provisions
- Never present one-sided interpretation
- Always cite the exact provision

## Contract

1. Each returned norm cites its exact § and statute acronym from the brain corpus.
2. If a norm is not in the corpus, that is stated rather than guessed.
3. The output supports legal work; it is not legal advice.

## Anti-Patterns

- ❌ Paraphrasing a norm as if quoting it — quote the § text or cite the source.
- ❌ Returning a § number without the statute or the version stamp.
- ❌ Inventing a norm that is not in the indexed corpus.

## Output Format

Per norm: § + statute · the norm text (or a faithful summary with source) · relevance
to the query — with the brain source for each entry.
