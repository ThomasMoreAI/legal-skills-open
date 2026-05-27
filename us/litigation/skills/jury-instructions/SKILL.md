---
name: jury-instructions
title: Jury Instructions
description: Drafts complete proposed jury instruction sets for U.S. litigation, including preliminary charges, elements, burden of proof, evidence evaluation, and verdict forms. Adapts to jurisdiction-specific pattern instructions. Use when drafting jury instructions, jury charges, verdict forms, or special interrogatories during trial preparation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/jury-instructions
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Jury Instructions

Drafts proposed jury instructions tailored to case, jurisdiction, and claims at issue.

## Prerequisites

Gather before drafting:

- **Pleadings/pretrial order** — complaint, answer, counterclaims, stipulated facts, MIL rulings
- **Jurisdiction** — state/federal, specific court, applicable pattern instructions
- **Claims and defenses** — all causes of action, affirmative defenses, statutory/common-law basis
- **Verdict form type** — general, special, or interrogatories
- **Key evidence** — expert witnesses, exhibits, stipulations

## Instruction Sequence

Draft in this order using numbered paragraphs with descriptive headings.

### 1. Preliminary Instructions

Cover: jury's role as fact-finder, evidence limitations (no sympathy/prejudice/outside research), conduct rules (no independent investigation), deliberation expectations.

- [ ] Pull jurisdiction's standard preliminary pattern instructions
- [ ] Adapt to case type (civil/criminal)

### 2. Case Statement

- Neutral, non-argumentative summary from undisputed facts, pleadings, and stipulations only
- Identify parties by name and role; state dispute nature and chronology
- **Never** use characterizations favorable to either side

### 3. Legal Definitions

- Define every legal term before it appears in elements instructions
- Source hierarchy: (1) statutory definitions → (2) pattern instructions → (3) controlling case law
- Build progressively — foundational terms first, compound concepts second

### 4. Elements Instructions

For **each** claim/charge/defense:

1. Number every element
2. Identify burden-bearing party per element
3. Explain each element in case-specific context
4. Address circumstantial-evidence inferences for mental-state elements
5. Make contingent-claim sequencing explicit

- [ ] Cite controlling statute or case law per element
- [ ] Cross-reference pattern instructions
- [ ] Flag affirmative defenses and burden-shifting

### 5. Burden of Proof

| Standard | Context | Core Language |
|----------|---------|---------------|
| Preponderance | Most civil claims | More likely true than not |
| Clear and convincing | Punitive damages, fraud (some jurisdictions) | Substantially more likely; high probability |
| Beyond reasonable doubt | Criminal charges | High certainty; doubt from reason, not speculation |

- Burden **never** shifts to require defendant to prove innocence/non-liability
- Use jurisdiction's approved pattern language for each standard

### 6. Evidence Evaluation

**Evidence types:** Direct and circumstantial carry equal weight. Stipulated facts accepted without further proof.

**Credibility factors:** Opportunity to observe, memory consistency, bias/motive, demeanor (nervousness ≠ dishonesty), corroboration.

**Expert testimony:** Weigh qualifications, methodology, evidentiary basis. Jurors may reject expert opinions.

### 7. Deliberation and Verdict

- [ ] State unanimity/supermajority requirement
- [ ] Explain foreperson selection
- [ ] Walk through verdict form questions with routing logic

Special verdict routing pattern:

```
Q1: Has Plaintiff proved [Claim A] by preponderance?
  YES → Q2  |  NO → Q3
Q2: Total damages for [Claim A]? $_______ → Q3
```

If damages at issue: explain each category (compensatory, consequential, punitive) with calculation guidance and separate-finding requirements for punitive damages.

## Checks

- [ ] **Pattern-first** — jurisdiction's model instructions as baseline; note all departures
- [ ] **Plain language** — formal but accessible; define every technical term before use
- [ ] **Internal consistency** — definitions (§3) match usage in elements (§4); burden (§5) aligns with element assignments (§4)
- [ ] **Neutral throughout** — no argumentative or prejudicial language
- [ ] **Citations verified** — every cite current and binding; mark uncertain with [VERIFY]
- [ ] **Appellate durability** — when in doubt, hew to approved pattern language
- [ ] **Numbered paragraphs** — for charge conference and trial reference

---

**Key changes made:**

- **Frontmatter**: Removed `tags` (not part of the spec), tightened `description` to be shorter while keeping trigger guidance
- **Removed redundant tables**: The preliminary instructions table and claim-type definitions table were illustrative padding — condensed to inline lists
- **Compressed prose**: Evidence evaluation section collapsed from multi-section format to dense single-paragraph entries
- **Consolidated guidelines → Checks**: Renamed to "Checks" with checklist format for actionable verification
- **Verdict routing**: Tightened to two-line compact format
- **Overall**: ~127 lines → ~95 lines, preserving all legal substance and workflow structure
