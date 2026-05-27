---
name: expert-report-class-damages
title: Expert Report on Class Damages
description: Drafts a litigation-ready expert report on class-wide damages for class action proceedings. Structures analysis to satisfy Daubert/FRE 702 admissibility and FRCP 23(b)(3) predominance. Use when retaining or preparing a damages expert for class certification, merits, or trial phases.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/expert-report-class-damages
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, drafting]
---

# Expert Report on Class Damages

Produces a court-ready expert damages report demonstrating class-wide measurability of harm under a common methodology, structured to survive Daubert challenge and support FRCP 23(b)(3) certification.

## Prerequisites

1. **Class definition and complaint** — allegations, liability theories, relief sought
2. **Engagement scope** — retention letter specifying opinions requested and exclusions
3. **Damages evidence** — transaction records, financial statements, pricing data, surveys, or defendant-produced databases
4. **Expert CV** — credentials, publications, prior testimony history
5. **Opposing expert reports** (if any) — to distinguish competing methodologies
6. **Legal authorities** — jurisdiction's Daubert/Frye standard; prior rulings on proposed methodology

## Quick Start

1. Gather prerequisites above
2. Confirm jurisdiction's admissibility standard (Daubert, Frye, or Sargon)
3. Select primary damages methodology from the methodology table below
4. Walk through each output section in order
5. Run the compliance checklist before finalizing

## Output Sections

### 1. Title Page

| Field | Content |
|---|---|
| Court & case caption | Full court name, case number, parties |
| Expert identity | Name, title, firm/institution |
| Retaining party | Plaintiff / Defendant / Neutral |
| Report date | Date of signing |
| Confidentiality designation | Per applicable protective order |

### 2. Introduction & Engagement Scope

- Identify the putative class, claims, and relief sought
- State questions addressed:
  - Can damages be measured class-wide using common evidence?
  - What is the aggregate class-wide damages amount?
  - Do individual damages issues predominate over common ones?
- Explicitly state what is **not** in scope (liability, causation, individual allocation) to limit deposition exposure

### 3. Expert Qualifications

Tie credentials directly to the methodology used — generic backgrounds invite Daubert attack.

| Category | Detail |
|---|---|
| Education | Degree, institution, year |
| Relevant experience | Industry, sector, years |
| Publications | Those bearing on methodology or damages field |
| Prior testimony | Number of matters, courts, subject areas |
| Specific expertise | Why qualified for *this* methodology |

### 4. Methodology & Economic Framework

**Select and justify the primary methodology:**

| Methodology | Best For | Key Requirements |
|---|---|---|
| Regression analysis | Price-fixing, overcharge | Sufficient transaction data; control variables |
| Before-and-after | Market disruption, fraud | Clean pre-period baseline; comparable windows |
| Yardstick / benchmark | Product liability, consumer harm | Comparable unaffected market or product |
| Lost profits (but-for) | Breach, interference | Reliable projections; defensible counterfactual |

**Must include:**
- Cite academic literature and FJC *Reference Manual on Scientific Evidence* (3d ed.)
- Address prior court acceptance in similar cases
- Explain why rejected alternatives are less reliable
- Demonstrate common proof: damages calculable without individualized inquiries

### 5. Data Sources & Assumptions

For each data source, document:

| Element | Description |
|---|---|
| Origin | Who produced it, how obtained |
| Processing | Cleaning, normalization, exclusions |
| Reliability | Suitability for analysis; completeness concerns |
| Limitations | Known gaps; defendant data issues |

**Material assumptions:** state each explicitly, cite supporting basis, and perform sensitivity analysis showing damages remain robust across reasonable variations.

### 6. Damages Analysis & Calculations

Present step-by-step:

1. **Class size** — method for identifying affected members
2. **Per-member harm** — average injury and distribution across subgroups
3. **Aggregate damages** — formula, inputs, result

For each step: show formula, data inputs with source citations, and output value.

- Use tables/charts for judge/jury accessibility
- Calculate each measure separately (compensatory, restitutionary, disgorgement) — explain overlaps to avoid double-counting
- Address mitigation, offsets, or benefits reducing net damages
- Present sensitivity ranges for uncertain point estimates

### 7. Conclusions

- State aggregate damages with confidence level
- If range: identify variation drivers
- Tie each conclusion to methodology and data
- Acknowledge modeling uncertainties — avoid false precision
- Confirm damages provable to reasonable certainty under applicable standard

### 8. Appendices

| Appendix | Contents |
|---|---|
| A | Expert CV |
| B | Materials considered (complete list) |
| C | Calculation workpapers |
| D | Data tables and source extracts |
| E | Demonstrative exhibits |
| F | Bibliography |
| G | Model/software documentation (if proprietary tools) |

## Compliance Checklist

- [ ] **Daubert**: methodology is testable, peer-reviewed where possible, has known error rate, and is generally accepted — address all four factors [VERIFY circuit's Daubert formulation]
- [ ] **FRCP 23(b)(3)**: common questions predominate; model does not require individualized mini-trials
- [ ] **FRE 702**: opinions based on sufficient facts, reliable methodology, reliably applied to facts
- [ ] **Scope discipline**: no opinions beyond engagement scope
- [ ] **Data provenance**: chain of custody documented for all data relied upon
- [ ] **Replication**: methodology sufficiently documented for opposing expert to replicate
- [ ] **Jurisdiction**: confirm controlling admissibility standard — Daubert, Frye, *Sargon* (CA), or other [VERIFY by jurisdiction]
