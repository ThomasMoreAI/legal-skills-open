---
name: verdict-judgment-summary
title: Verdict/Judgment Summary
description: Produces structured post-trial verdict and judgment analysis memoranda for commercial litigation. Triggers when summarizing a jury verdict, bench trial decision, post-trial motion assessment, or appellate viability review. Covers liability determinations, damages breakdowns, critical rulings, and post-trial strategy.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/verdict-judgment-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, summarization, summary]
---

# Verdict/Judgment Summary

Produces an internal strategic memorandum analyzing a completed trial outcome, assessing post-trial options, and charting next steps.

## Prerequisites

Gather before starting — flag any missing items:

1. **Verdict form or written judgment** — exact findings, conclusions, awards
2. **Trial transcripts** — key rulings and testimony (full or partial)
3. **Trial team notes** — observation memos, jury reaction notes
4. **Docket entries** — MIL orders, evidentiary rulings, jury instruction disputes
5. **Comparable verdict research** — jurisdiction-specific damage benchmarks

## Quick Start

1. Extract all findings and awards from the official verdict/judgment
2. Map each claim to its outcome with exact verdict-form language
3. Tabulate damages by category with evidentiary basis
4. Catalog outcome-affecting rulings and preservation status
5. Assess post-trial motions and appellate viability
6. Compile deadlines and recommendations with cost-benefit analysis

## Output Structure

### 1. Executive Summary (3 paragraphs max)

| Element | Content |
|---|---|
| Prevailing party | Which party prevailed on which claims |
| Financial outcome | Total award, net result after offsets |
| Bottom line | One-sentence strategic takeaway |

### 2. Liability Determinations

Per claim tried:

- Outcome (sustained/defeated)
- Exact verdict form or judgment language
- Fault allocation among parties (comparative negligence/multiple defendants)
- Special interrogatory answers revealing jury reasoning
- Claims with liability but no damages — analyze why

### 3. Damages Breakdown

| Category | Amount | Basis |
|---|---|---|
| Economic (wages, medical, property) | $ | |
| Non-economic (pain/suffering, emotional distress, consortium) | $ | |
| Punitive | $ | Malice/fraud/oppression findings; ratio to compensatory |
| Statutory caps or remittitur | $ | Legal basis |
| **Total** | **$** | |

### 4. Critical Trial Rulings

Per outcome-affecting ruling:

| Ruling | Court's Reasoning | Standard | Preserved? | Appellate Impact |
|---|---|---|---|---|
| MIL on [topic] | | | Y/N | |
| Expert exclusion | | | Y/N | |
| Jury instruction refusal | | | Y/N | |
| Directed verdict denial | | | Y/N | |

Flag rulings deviating from jurisdiction precedent or involving novel statutory interpretation.

### 5. Post-Trial Motion Assessment

**JMOL / JNOV (FRCP 50(b) or state equivalent):**
- Could a reasonable jury have reached this verdict?
- Legally inconsistent findings?
- Success likelihood: High / Moderate / Low

**New Trial (FRCP 59 or state equivalent):**
- Prejudicial evidentiary errors?
- Improper jury arguments?
- Procedural irregularities affecting substantial rights?
- Success likelihood: High / Moderate / Low

**Remittitur / Additur:**
- Award outside range supported by evidence?
- Comparable verdict benchmarks in jurisdiction
- Alternative damage figure with evidentiary support

For each motion assess: legal merit, judge's tendencies, practical likelihood of relief.

### 6. Appellate Viability

| Issue | Standard of Review | Preserved? | Precedent Conflict? | Reversal Probability |
|---|---|---|---|---|
| | De novo / Substantial evidence / Abuse of discretion | Y/N | | High / Moderate / Low |

- Unpreserved issues: assess plain error or fundamental rights alternatives
- Recent appellate decisions on similar questions in jurisdiction
- Candidly assess genuine reversal prospect vs. delay

### 7. Recommendations and Deadlines

| Action | Deadline | Recommendation |
|---|---|---|
| JMOL/JNOV motion | 28 days federal / jurisdiction-specific | File / Do not file |
| New trial motion | 28 days federal / jurisdiction-specific | File / Do not file |
| Notice of appeal | 30 days federal / jurisdiction-specific | File / Do not file |
| Settlement outreach | [date] | Pursue / Hold |
| Client communication | [date] | Talking points |

Include cost-benefit analysis: post-trial expense vs. financial stakes, client risk tolerance, business objectives, reputational and precedential impact.

## Pitfalls and Checks

- **Cross-reference everything** — verify every figure, date, and finding against official judgment before finalizing
- **Analyze, don't describe** — explain *why* the verdict emerged (trial dynamics, credibility, evidence strength), not just what happened
- **Stay candid** — flag weaknesses even in favorable verdicts; maintain objectivity regardless of outcome
- **Deadline vigilance** — post-trial deadlines are jurisdictional and non-negotiable; always VERIFY for specific jurisdiction
- **Accessible executive summary** — must be comprehensible to attorneys who did not attend trial and non-lawyer clients
- **Prediction divergence** — where outcome differs from pre-trial assessment, analyze contributing factors
