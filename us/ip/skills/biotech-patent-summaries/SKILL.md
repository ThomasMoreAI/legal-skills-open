---
name: biotech-patent-summaries
title: Biotechnology Patent Summaries
description: Summarizes biotech patent families and disputes into litigation-ready intelligence briefs. Trigger when the user provides patent applications, issued patents, PTAB filings, prosecution histories, licensing materials, or litigation documents in biotechnology domains and requests a summary, risk assessment, or FTO analysis.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/biotech-patent-summaries
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
tags: [analysis, litigation, summarization, transactional]
---

# Biotechnology Patent Summaries

Produce a source-grounded intelligence brief on biotech patents and disputes for litigation, portfolio, and executive decisions.

## Quick Start

1. Collect inputs: patent corpus, dispute materials, parties/products map, jurisdiction scope, and clear objective (litigation exposure, licensing, design-around, or FTO).
2. Run the core workflow below.
3. Deliver the output template with uncertainty tags on every analytical assertion.

## Core Workflow

1. **Ingest & normalize** — Gather patent identity, claim sets, prosecution history, and dispute metadata. Normalize dates to ISO format. Define technical terms on first use.
2. **Extract & map claims** — Identify independent claims first, quote critical language verbatim, then map dependents and fallback embodiments.
3. **Analyze validity/infringement** — Test enforceability vectors:
   - §101 eligibility (methods, diagnostics, natural products)
   - §102/103 novelty and obviousness
   - §112 enablement/written description (especially genus claims over biological matter)
4. **Assess procedural & business impact** — Quantify litigation risk (timeline, injunction exposure, claim-construction volatility), cross-jurisdiction differences, and commercial consequences.
5. **Compile deliverable** — Fill the output template; tag every item as confirmed fact, party argument, or analytical assessment.

## Input Capture

| Bucket | Key Fields |
|---|---|
| Patent identity | Patent/app no., family ID, filing/priority/grant dates, assignee |
| Technical scope | Mechanism, target, platform, key molecules/processes |
| Claim set | Independent/dependent claims, types, limitations, embodiments |
| Status | Pending/granted/abandoned, IPR/opposition posture, deadlines |
| Dispute metadata | Court/tribunal, parties, accused products, allegations |
| Procedural calendar | Hearings, motions, claim construction, trial dates (with certainty rating) |
| Strategic posture | Commercial significance, exclusivity, competitor landscape, remedies sought |

## Output Template

```
# [Matter Title]
Current through: [DATE]

## 1) Executive Summary
Three short paragraphs: patent landscape, key legal issues, action recommendations.

## 2) Patent/Dispute Snapshot
| Field | Value |
|---|---|
| Identifier | |
| Jurisdiction(s) | |
| Parties | |
| Status | |
| Urgency | |

## 3) Claim & Scope Analysis
| Claim # | Text excerpt | Breadth | FTO relevance | Risk flags |
|---|---|---|---|---|

## 4) Validity & Prior-Art Assessment
| Ground | Basis | Record support | Counterargument strength | Probability |
|---|---|---|---|---|

## 5) Infringement Analysis
| Accused product/method | Claim-mapped match | Defense argument space | Exposure |
|---|---|---|---|

## 6) Dispute Timeline
| Date | Event | Forum | Strategic effect |
|---|---|---|---|

## 7) Strategic Recommendations
- [ ] Litigation strategy
- [ ] Licensing / settlement
- [ ] Design-around / alternative pathway
- [ ] Portfolio filing or challenge
- [ ] Regulatory and exclusivity coordination

## 8) Uncertainty Register
Confirmed facts | Documented allegations | Analytical assumptions | Open gaps
```

## Deliverable Rules

- **Citation discipline** — Cite patent numbers, claim/paragraph refs, docket entries; no uncited assertions.
- **Scope discipline** — Label each statement as fact, party argument, or analysis.
- **Technical precision** — Keep scientific language exact; do not oversimplify in ways that change meaning.
- **Jurisdiction tags** — Label every legal standard by jurisdiction and confidence level.
- **Currency** — State explicit "current through" date and stop-line assumptions.

## Pitfalls & Checks

- No legal advice; provide neutral counsel-grade analysis only.
- Default to US jurisdiction unless explicitly labeled otherwise.
- Do not overstate claim scope where specification support is thin.
- Flag missing records as "needs confirmation" — never infer.
- [VERIFY] Confirm current case law before finalizing eligibility/invalidation analysis, especially for biotech diagnostic and sequence-related claims.
- [VERIFY] Cross-check AIA first-inventor-to-file effects, PGR/IPR timing windows, and equitable doctrines for US patents.
- For biologics, evaluate regulatory exclusivities (orphan, pediatric, biologics data exclusivity) alongside patent rights.
