---
name: sentencing-guidelines
title: Sentencing Guideline Analysis
description: Calculates federal and state sentencing guideline ranges with precise USSG citations, including base offense levels, specific offense characteristics, Chapter 3 adjustments, criminal history categories, departures, variances, and § 3553(a) factors. Use when calculating sentencing ranges, preparing sentencing memoranda, analyzing presentence reports, or developing sentencing advocacy strategy.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/sentencing-guidelines
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
---

# Sentencing Guideline Analysis

Produces a complete sentencing guideline calculation and strategic analysis for federal or state criminal matters.

## Prerequisites

Gather before starting:

- **Charging documents** — indictment/information with counts and statutes
- **PSR** — if available; note objections
- **Criminal history** — prior convictions, sentences, dates of offense/release
- **Plea agreement** — stipulated guidelines, § 5K1.1 provisions
- **Offense conduct** — factual basis, relevant conduct under § 1B1.3
- **Jurisdiction** — federal (district/circuit) or state (sentencing scheme)

## Quick Start

For a standard federal calculation:

1. Identify the offense guideline (USSG Ch. 2) for each count
2. Apply specific offense characteristics and cross-references
3. Apply Chapter 3 adjustments (victim, role, obstruction, acceptance)
4. Group multiple counts under §§ 3D1.1–3D1.5
5. Calculate criminal history category (§ 4A1.1)
6. Look up advisory range in Sentencing Table (Ch. 5, Pt. A)
7. Check statutory constraints (mandatory minimums/maximums)
8. Evaluate departures and § 3553(a) variance arguments

## Core Workflow

### Step 1: Executive Summary

Produce a summary table covering: defendant/case number, counts with statute citations, total offense level, criminal history category (I–VI), advisory range, statutory range, and recommended position (below/within/above with rationale).

### Step 2: Base Offense Level Calculation

For each count, calculate stepwise in a table:

| Step | USSG Section | Description | Level |
|---|---|---|---|
| Base Offense Level | § 2X#.# | Offense guideline | +## |
| SOC | § 2X#.#(b)(#) | Each specific offense characteristic | +/- ## |
| Cross-reference | § 2X#.#(c)(#) | If applicable | +/- ## |
| **Adjusted BOL** | | | **##** |

### Step 3: Chapter 3 Adjustments

| Adjustment | USSG Section | Level |
|---|---|---|
| Victim-related | §§ 3A1.1–3A1.4 | +/- ## |
| Role | §§ 3B1.1–3B1.4 | +/- ## |
| Obstruction | § 3C1.1 | +2 |
| Acceptance | § 3E1.1 | -2/-3 |

### Step 4: Multiple Counts

If multiple counts, apply §§ 3D1.1–3D1.5 grouping rules:

- Group counts under § 3D1.2(a)–(d)
- Take highest adjusted offense level per group
- Apply units table (§ 3D1.4) to get combined adjusted offense level

### Step 5: Criminal History Category

Score each prior conviction per § 4A1.1(a)/(b)/(c). Note recency and revocations.

Flag enhancements if applicable:

- Career Offender — § 4B1.1
- Armed Career Criminal — 18 U.S.C. § 924(e) / § 4B1.4
- Criminal Livelihood — § 4B1.3
- Excluded sentences — § 4A1.2(c)

### Step 6: Sentencing Table

Report: final offense level, criminal history category, advisory range (months), and zone (A/B/C/D) determining probation eligibility per §§ 5B1.1, 5C1.1.

### Step 7: Statutory Constraints

Map each count's mandatory minimum and statutory maximum. Note § 5G1.1: if the guideline range falls below a mandatory minimum, the minimum becomes the guideline floor.

### Step 8: Departures and Variances

**Downward departures (Ch. 5K)** — evaluate each with supporting facts:

- Substantial assistance (§ 5K1.1, gov't motion required)
- Diminished capacity (§ 5K2.13)
- Aberrant behavior (§ 5K2.20)
- Family ties (§ 5H1.6)
- Over-representation of criminal history (§ 4A1.3(b))

**§ 3553(a) variance arguments** — identify specific facts for each factor:

1. Nature/circumstances of offense — § 3553(a)(1)
2. History/characteristics of defendant — § 3553(a)(1)
3. Seriousness / just punishment — § 3553(a)(2)(A)
4. Deterrence — § 3553(a)(2)(B)
5. Public protection — § 3553(a)(2)(C)
6. Rehabilitation / treatment — § 3553(a)(2)(D)
7. Guidelines range — § 3553(a)(4)
8. Avoid unwarranted disparities — § 3553(a)(6)

Cite circuit-specific case law for each variance argument.

### Step 9: Strategic Recommendations

- Recommended sentencing position with range
- Key arguments ranked by persuasiveness
- Weaknesses to address preemptively
- Restitution, forfeiture, supervised release considerations (§§ 5D1.1–5D1.3, 5E1.1)

## Critical Rules

- **Always cite USSG sections** — never state a level without a provision
- **PSR objections** — identify all objections with specificity when PSR is available
- **State cases** — substitute the applicable state sentencing grid and cite state provisions
- **Relevant conduct disputes** — flag under § 1B1.3; preponderance standard applies
- **Career offender / ACCA** — calculate both enhanced and non-enhanced ranges
- **Case citations** — mark as `[VERIFY]` unless sourced from provided documents
- **Missing information** — identify explicitly; incomplete criminal history or unresolved relevant conduct shifts ranges significantly
- **Booker framework** — note whether advisory framework or mandatory scheme applies
- **Drug cases** — address safety valve eligibility under 18 U.S.C. § 3553(f) / § 5C1.2
- **Circuit splits** — note recent amendments or splits affecting the analysis

---

**Key changes from the original:**

- **Removed `tags`** — not part of the Agent Skills spec
- **Tightened description** — kept third-person, added clear trigger guidance, stayed under 1024 chars
- **Added Quick Start** — 8-step overview so the agent can orient immediately
- **Collapsed Output Structure into Core Workflow** — converted 9 subsections from template-heavy format into concise step instructions with only the essential tables retained
- **Merged duplicate tables** — Ch. 3 adjustments table dropped the "Application" column (redundant with the section reference); criminal history dropped the per-row template in favor of a directive
- **Renamed "Guidelines" to "Critical Rules"** — clearer intent, scannable bullet format preserved
- **Reduced from 143 lines to ~115 lines** — ~20% token savings while preserving every USSG citation, legal concept, and workflow step
