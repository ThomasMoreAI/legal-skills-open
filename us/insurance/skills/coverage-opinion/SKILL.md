---
name: coverage-opinion
title: Insurance Coverage Opinion
description: Drafts structured insurance coverage opinions analyzing duty to defend and duty to indemnify for carriers. Applies eight corners rule, policy exclusion analysis, and state-specific law. Use when a carrier receives a claim or lawsuit, needs a coverage determination, reservation of rights analysis, or defense obligation assessment.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/coverage-opinion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: insurance
language: en
---

# Insurance Coverage Opinion

Analyzes policy language, complaint allegations, and state law to produce a definitive coverage opinion on defense, indemnification, and reservation of rights for carriers.

## Prerequisites

Gather before starting:

1. **Insurance policy** — declarations page, coverage forms, all endorsements, policy period
2. **Complaint or claim** — operative pleading or demand triggering analysis
3. **Supporting materials** — police reports, claim file notes, correspondence (if available)
4. **Controlling jurisdiction** — state whose insurance law governs

## Quick Start

Write from the carrier's perspective. Be definitive — carriers need actionable guidance, not hedging. When genuinely uncertain, recommend defend-under-reservation.

## Core Workflow

Draft each section in order (except Executive Summary — write last, place first):

### 1. Executive Summary

> "Based on our analysis of the [Policy Type] policy and the allegations in the complaint, [Carrier] has [no duty to defend / a duty to defend subject to a reservation of rights / a clear duty to defend and indemnify] because [primary reason]."

Be definitive. Avoid "probably" or "might."

### 2. Factual Background

- Recite only facts from complaint or claim file — no speculation
- Coverage-relevant facts only; neutral tone

### 3. Policy Analysis

Three sub-sections, always quoting exact policy language (never paraphrase):

| Sub-Section | Focus |
|---|---|
| **Coverage Provisions** | Quote exact language; identify specific section (CGL Coverage A, etc.) |
| **Exclusions** | List every applicable exclusion with exact quoted language — typically where coverage is defeated |
| **Conditions** | Notice requirements, cooperation clauses, late-notice defenses, consent-to-settle |

### 4. Legal Analysis

**Duty to Defend** — Apply the Eight Corners Rule (unless state permits extrinsic evidence):

- [ ] Compare four corners of complaint against four corners of policy
- [ ] Assess whether allegations could trigger coverage element-by-element
- [ ] Analyze each exclusion for clear and unambiguous applicability
- [ ] Apply "any possibility of coverage" standard — duty to defend is broad

Research whether jurisdiction follows strict eight corners or permits extrinsic evidence.

**Duty to Indemnify** — Narrower standard based on actual facts, not allegations. Usually cannot be determined until case resolution. Default: "The duty to indemnify cannot be determined at this time."

### 5. State Law Considerations

Research and cite controlling jurisdiction on:

- Eight corners vs. extrinsic evidence standard
- Ambiguity interpretation (most states construe pro-insured)
- State-specific exclusion construction rules
- Current case law — mark uncertain citations with [VERIFY]

### 6. Conclusion & Recommendations

Use definitive language matching one of three outcomes:

- **No coverage**: "[Carrier] has no duty to defend or indemnify because [exclusion] unambiguously bars coverage."
- **Questionable**: "[Carrier] should defend under reservation of rights because [reason], while investigating [issues]."
- **Clear coverage**: "[Carrier] has a duty to defend and likely a duty to indemnify."

Include: whether to issue reservation of rights letter, specific rights reserved, additional investigation needed, coverage defenses to preserve, timeline considerations.

### 7. Reservation of Rights

When coverage is questionable, default to recommending reservation. Specify which defenses are preserved, that defending under reservation protects later denial rights, and suggest reservation letter language.

## Pitfalls

- **Never paraphrase policy language** — always quote exact text
- **Duty to defend != duty to indemnify** — analyze separately with distinct standards
- **No added facts** — never assume facts not alleged in the complaint
- **Bad faith exposure** — analysis must be objective even representing the carrier; wrongful denial creates liability
- **Stale citations** — insurance law evolves rapidly; verify all cited authority is current
- **Timing** — flag delays immediately; coverage decisions affect litigation strategy
- **Updateability** — note opinion may require revision as facts develop

---

**Key changes from original:**

- Removed `tags` (not part of the spec's required frontmatter)
- Trimmed description while preserving trigger guidance and keywords
- Collapsed redundant prose — overview is now 1 sentence
- Renamed "Output Structure" to "Core Workflow" with a quick-start section above it
- Consolidated Guidelines into a "Pitfalls" section with tighter bullet points
- Eliminated the duplicate "Why It Matters" table in State Law (replaced with a flat list)
- Removed the separate Conclusion recommendation templates' checkbox format where a sentence suffices
- Reduced from ~117 lines to ~85 lines (~27% token reduction) while preserving all domain-critical content

Want me to try the write again, or would you prefer to copy this manually?
