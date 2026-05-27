---
name: construction-case-summary
title: Construction Law Case Summary
description: Produces structured U.S. construction law case summaries with timelines, holdings, damages, and risk takeaways. Triggers on construction case summaries, defect analyses, payment dispute summaries, bond or mechanic's lien reviews, OSHA violation briefs, or construction precedent digests.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/construction-case-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: construction
language: en
tags: [analysis, litigation, summarization, summary]
---

# Construction Law Case Summary

Structured, citation-anchored summary of a construction law decision for precedent and risk analysis.

## Quick Start

Gather before drafting:
- Full case materials with record/opinion citations
- Jurisdiction, court level, procedural posture, published/precedential status
- Referenced project documents (contract, specs, change orders, bond, lien filings, safety reports)
- Party list with roles (owner, GC, subs, design professionals, insurers)

## Workflow

1. Run intake checklist; flag missing inputs.
2. Populate Case Metadata and Parties tables.
3. Build dated timeline with source cites.
4. Apply relevant module(s): Contract Breach, Defects, Safety/OSHA.
5. Extract holdings and reasoning with pinpoint cites.
6. Record damages/relief and practical takeaways.
7. For multiple cases, synthesize majority/minority rules by jurisdiction.

## Intake Checklist

- [ ] Court, jurisdiction, decision date
- [ ] Case caption and citation
- [ ] Procedural posture and standard of review
- [ ] Contract/bond/lien documents and key clauses
- [ ] Defect discovery timeline
- [ ] Injury/OSHA event details
- [ ] Damages claimed/awarded
- [ ] Published vs unpublished status

## Output Tables

**Case Metadata**

| Field | Entry |
|---|---|
| Caption | |
| Citation | |
| Court | |
| Decision Date | |
| Jurisdiction | |
| Procedural Posture | |
| Standard of Review | |
| Published / Precedential | |
| Outcome | |

**Parties and Roles**

| Party | Role | Key Obligations / Exposure |
|---|---|---|
| | | |

**Timeline**

| Date | Event | Source Cite |
|---|---|---|
| | | |

## Summary Template

- **Dispute type(s):** …
- **Project type / delivery method:** …
- **Key facts:** …
- **Legal issues:** …
- **Holdings:** …
- **Court's reasoning:** …
- **Damages / relief:** …
- **Practical impact:** …

## Modules

### Contract Breach

| Element | Notes |
|---|---|
| Contract form (written/oral) | |
| Clauses at issue (scope, notice, payment, change orders, force majeure) | |
| Breach theory and defenses (substantial performance, impossibility, waiver) | |
| Payment disputes (prompt payment, retainage) | |
| Performance/payment bond issues | |
| Mechanic's lien posture and deadlines | |
| Economic loss doctrine application | |

### Construction Defects

| Element | Notes |
|---|---|
| Defect type (structural, design, materials, workmanship) | |
| Patent vs latent classification | |
| Statute of limitations / repose analysis | |
| Expert testimony and code/standard references | |
| Warranty claims (express/implied) | |
| Fault allocation among participants | |
| Damages theory (repair, diminution, consequential) | |

### Worker Safety / OSHA

| Element | Notes |
|---|---|
| OSHA standard(s) cited | |
| Violation classification and penalties | |
| GC vs sub safety responsibility | |
| Workers' comp exclusivity impact | |
| Third-party liability or indemnity | |
| Willful or criminal findings | |

## Holdings and Damages

**Holdings / Rule Synthesis**

| Issue | Holding | Rule/Standard | Cite |
|---|---|---|---|
| | | | |

**Damages / Relief**

| Category | Claimed | Awarded | Notes |
|---|---|---|---|
| | | | |

**Practical Takeaways**

- [ ] Contract drafting or notice practices affected
- [ ] Documentation practices that controlled outcome
- [ ] Insurance coverage or bond implications
- [ ] Safety compliance or supervision adjustments

## Pitfalls

- Use exact citations for facts and holdings; never paraphrase without a cite.
- Distinguish holding from dicta; label dissent/concurrence explicitly.
- Flag uncertain statutes or regulatory citations with `[VERIFY]`.
- Note jurisdiction-specific doctrines (anti-indemnity, prompt payment, lien law) and state variance.
- State limitation if decision is unpublished or nonprecedential.
- Never invent facts, timelines, or code/OSHA provisions.
