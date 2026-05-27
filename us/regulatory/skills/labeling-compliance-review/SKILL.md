---
name: labeling-compliance-review
title: FDA Labeling Compliance Review
description: Conducts FDA labeling compliance reviews for drugs, foods, dietary supplements, and medical devices. Analyzes principal display panels and information panels against FDCA, 21 CFR, and FDA guidance to identify misbranding risks, claims violations, and mandatory disclosure gaps. Use when reviewing product labels, auditing FDA compliance, assessing labeling risk, or preparing for FDA submission.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/labeling-compliance-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# FDA Labeling Compliance Review

Structured compliance assessment of FDA-regulated product labeling. Identifies misbranding risks and regulatory gaps with cited corrective recommendations.

## Prerequisites

Gather before starting:

1. **Label files** — images or PDFs of all panels (PDP, information, back/side)
2. **Product classification** — drug (OTC/Rx), food, dietary supplement, device, or cosmetic
3. **Intended use statement** — as marketed and as labeled
4. **Claims substantiation** (if applicable) — scientific support for health, structure/function, or nutrient content claims
5. **Prior FDA correspondence** (if any) — warning letters, 510(k) clearance, labeling supplements

## Quick Start

1. Classify the product and identify controlling CFR parts
2. Review PDP for identity, net quantity, and prohibited claims
3. Review information panel against product-specific checklist
4. Evaluate each claim for type, permissibility, and required disclaimers
5. Check mandatory warnings and statements
6. Produce findings table with severity, citation, and corrective action

## Core Workflow

### Step 1: Product Identification

| Field | Detail |
|---|---|
| Product name (as labeled) | Include trademarked elements |
| Product classification | Drug / Food / Dietary Supplement / Device / Cosmetic |
| Intended use | Conditions, target population, route/method |
| Applicable framework | Controlling CFR parts (e.g., 21 CFR 101 for food, 21 CFR 201 for drugs) |

### Step 2: Principal Display Panel (PDP)

Evaluate each element against product-specific requirements:

| Element | Requirement | Citation |
|---|---|---|
| Statement of identity | Common/usual name or standard of identity | 21 CFR 101.3 (food) / 201.10 (drug) |
| Net quantity of contents | Lower 30% of PDP, minimum type size per area | 21 CFR 101.105 / 201.51 |
| Established drug name | Prominent, ≥½ size of proprietary name | 21 CFR 201.10(g) |
| Prohibited terms/imagery | No unapproved therapeutic claims, no misleading vignettes | FDCA §403(a) / §502(a) |
| Type size & prominence | Meets minimum ratios; not obscured by design | 21 CFR 101.15 / 201.15 |

Mark each: Compliant / Non-Compliant / N/A. Add notes for any deficiency.

### Step 3: Information Panel

Apply the checklist matching the product classification:

**Foods — Nutrition Facts:**
- [ ] Correct format (21 CFR 101.9)
- [ ] Serving size per RACC (21 CFR 101.12)
- [ ] All mandatory nutrients in prescribed order
- [ ] Current daily value percentages
- [ ] Type size ≥ 6 pt (≥ 8 pt for heading)
- [ ] Ingredients in descending order of predominance (21 CFR 101.4)
- [ ] Allergen declaration per FALCPA — "Contains:" or parenthetical (21 CFR 101.4(d))

**OTC Drugs — Drug Facts:**
- [ ] Standardized format (21 CFR 201.66)
- [ ] Headings in order: Active ingredient → Purpose → Uses → Warnings → Directions → Other information → Inactive ingredients
- [ ] Minimum 6 pt type
- [ ] All required warning subheadings present
- [ ] Adequate directions for use (21 CFR 201.5)

**Dietary Supplements — Supplement Facts:**
- [ ] Format per 21 CFR 101.36
- [ ] All dietary ingredients with amounts and %DV
- [ ] "Other ingredients" below panel
- [ ] § 403(s) disclaimer present

**Medical Devices:**
- [ ] Adequate directions for use (21 CFR 801.5)
- [ ] Intended use and indications
- [ ] Contraindications, warnings, precautions
- [ ] UDI compliance if applicable (21 CFR 801.20)

### Step 4: Claims Compliance

For each claim on the label:

| Claim Text | Claim Type | Permissible? | Required Disclaimer | Substantiation | Citation |
|---|---|---|---|---|---|
| | Health / Qualified Health / Structure-Function / Nutrient Content / Therapeutic | Y/N | Disclaimer text | Adequate / Insufficient / Missing | |

**Key claim rules:**
- **Structure/function (supplements):** Must include "This statement has not been evaluated by the FDA..." disclaimer; must not imply disease treatment (21 CFR 101.93)
- **Health claims:** Must be authorized (21 CFR 101.70-83) or qualify as qualified health claim
- **Nutrient content:** Must meet defined criteria (21 CFR 101.13, 101.54-101.69)
- **Disease claims** on food/supplement → triggers unapproved new drug classification (FDCA § 201(g))

### Step 5: Warnings & Mandatory Statements

| Required Statement | Citation |
|---|---|
| Allergen declaration (FALCPA) | 21 CFR 101.4(d) |
| Pregnancy/nursing warning | 21 CFR 201.63 / 101.17(h) |
| Children's dosing/warning | Product-specific |
| Tamper-evident statement | 21 CFR 211.132 (drugs) |
| Storage conditions | 21 CFR 201.66(c)(8) |
| Manufacturer/distributor name & address | 21 CFR 101.5 / 201.1 |
| Prop 65 (if CA distribution) | CA Health & Safety Code § 25249.6 [VERIFY] |

Mark each: Present / Absent, and Correct Format / Deficient.

### Step 6: Compliance Conclusion

**Overall status:** Compliant / Non-Compliant / Conditionally Compliant

**Findings table:**

| # | Finding | Severity | Regulatory Basis | Recommended Correction | Priority |
|---|---|---|---|---|---|
| | | Critical / Major / Minor | CFR citation | Specific fix | Immediate / 30-day / Next revision |

**Severity levels:**
- **Critical** — product is misbranded; enforcement exposure (warning letter, seizure, injunction)
- **Major** — significant gap; likely flagged in FDA inspection
- **Minor** — technical deficiency; low enforcement risk

Include: risk assessment (enforcement exposure summary), and reviewer name, date, and label version examined.

## Common Pitfalls

- Always cite specific 21 CFR sections — never use generic "FDA requires" language
- Flag ambiguous classification (e.g., supplement vs. drug boundary) and note regulatory consequences of each
- If product is marketed for a disease condition but classified as supplement/food, flag unapproved new drug risk explicitly
- Mark unverifiable citations with `[VERIFY]`
- Do not assume state-level compliance — note that state laws (Prop 65, state food labeling) may add obligations
- For combination products or novel ingredients, recommend pre-market FDA consultation
- If label was subject to a prior warning letter, cross-check all cited deficiencies against current label

---

**Key changes from the original:**

- **Removed `tags`** — not part of the Agent Skills spec; only `name` and `description` are recognized frontmatter fields
- **Added Quick Start** — gives the agent a scannable 6-step overview before diving into detail
- **Restructured body as "Core Workflow"** — sequential numbered steps replace the nested "Output Structure" framing, aligning with the workflow/checklist pattern from best practices
- **Consolidated tables** — PDP table dropped the empty "Compliant?" and "Notes" columns (replaced with a single instruction line); Warnings table dropped "Present?" and "Correct Format?" columns for the same reason
- **Renamed "Guidelines" → "Common Pitfalls"** — matches the recommended skill body section naming
- **Tightened prose throughout** — removed redundant phrasing ("Produces a structured compliance assessment of…" became the concise overview), shortened prerequisite descriptions, compressed claim rules into a bulleted list with bold labels
- **Line count: 135 → 126** — modest reduction while adding the Quick Start section, staying well under the 500-line ceiling
