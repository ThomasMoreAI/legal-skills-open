---
name: expert-witness-report-analysis
title: Expert Witness Report Analysis
description: Critiques opposing expert witness reports for admissibility challenges, disclosure deficiencies, and cross-examination vulnerabilities. Triggers when the user provides an expert report for analysis, needs Daubert/Frye assessment, requests a motion to exclude or limit expert testimony, or prepares deposition or trial cross-examination of an opposing expert.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/expert-witness-report-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, memo]
---

# Expert Witness Report Analysis

Produces a litigation-ready memorandum assessing an opposing expert's report for admissibility, methodology flaws, and impeachment opportunities under Daubert or Frye.

## Prerequisites

Collect before starting:

1. **Expert report** — full text with all opinions and basis statements
2. **Expert CV** — credentials, publications, prior testimony history
3. **Underlying data/exhibits** — materials the expert relied upon
4. **Case file materials** — pleadings, discovery, relevant fact record
5. **Jurisdiction** — federal (Daubert) vs. state (Frye or hybrid)
6. **Deposition transcripts** (if available) — for prior inconsistent statements

## Workflow

### Step 1: Extract and Catalog Opinions

Number each opinion verbatim with report page citations. For each, record the factual predicates claimed, methodological steps, and expressed certainty level.

### Step 2: Assess Qualifications

Extract credentials against this checklist:

- Degrees, licenses, board certifications (verify currency)
- Publications and peer-reviewed work
- Prior testimony history — frequency, plaintiff vs. defendant ratio
- Litigation income percentage vs. professional practice
- Prior exclusions, judicial criticism, sanctions, retractions

Map each opinion to the expertise it requires. Flag gaps under FRE 702.

### Step 3: Check FRCP 26(a)(2) Disclosure Completeness

Flag any missing or incomplete required elements:

- Complete statement of all opinions
- Basis and reasons for each opinion
- Facts or data considered
- Exhibits to be used
- Qualifications (CV)
- Cases with testimony in past 4 years
- Compensation statement

Missing elements are independent grounds for exclusion under FRCP 37(c)(1).

### Step 4: Analyze Methodology

Trace each analytical chain: raw data → intermediate steps → final opinion.

Assess per step: claimed method, standard practice, departures, and justification.

**Red flags:**
- Litigation-only method not used in regular practice
- Cherry-picked data or ignored contradicting information
- Unsupported assumptions or no independent testing
- Failure to test alternative hypotheses
- Backward reasoning from conclusion to data
- Internal inconsistencies between report sections

### Step 5: Evaluate Admissibility

**Daubert** (*Daubert v. Merrell Dow*, 509 U.S. 579 (1993); *Kumho Tire v. Carmichael*, 526 U.S. 137 (1999)) — assess each factor:

| Factor | Assessment |
|---|---|
| Testability | Satisfies / Fails / Partial |
| Peer review | Satisfies / Fails / Partial |
| Error rate | Satisfies / Fails / Partial |
| General acceptance | Satisfies / Fails / Partial |
| Fit to case facts | Satisfies / Fails / Partial |

**Frye** (*Frye v. United States*, 293 F. 1013 (D.C. Cir. 1923)) — identify the relevant scientific community, document general acceptance evidence, flag controversy or rejection.

Cite analogous case law where experts with similar deficiencies were excluded or admitted. State motion recommendation: exclude, limit, or reserve for cross.

### Step 6: Draft Cross-Examination Outline

Structure each theme as: Lock in → Establish standards → Expose deviation → Force concession.

Common themes:
- **Credentials gap** — establish field, narrow to sub-discipline, obtain admission of no training/publications, confront with opinion scope
- **Ignored contrary data** — establish duty to consider all information, identify what existed, confirm non-review, force choice (ignorance vs. deliberate omission)
- **Litigation-only methodology** — obtain method description, confirm no publications or non-litigation use, introduce authoritative contrary standard

Include impeachment sequences for prior inconsistent publications, depositions, or testimony in other cases.

### Step 7: Formulate Recommendations

- **Rebuttal expert** — required or optional; specify needed qualifications
- **Additional discovery** — depose expert, obtain working files/drafts/counsel communications, third-party discovery to verify assumptions
- **If testimony admitted** — cross themes, limiting instruction requests, closing argument framing on weight vs. credibility

## Output Format

Structure the memorandum as:

1. **Executive summary** (≤2 pages) — expert identity, numbered key opinions, admissibility recommendation, top 3-5 challenges with strategic impact
2. **Qualifications assessment** with credentials-to-opinion gap table
3. **Disclosure deficiency analysis**
4. **Methodology analysis** with step-by-step assessment table
5. **Opinion-by-opinion analysis** — factual predicates, method, logic gaps, certainty assessment, vulnerability summary
6. **Admissibility assessment** with Daubert/Frye evaluation and analogous case law
7. **Cross-examination outline**
8. **Recommendations**

## Pitfalls and Checks

- Cite every assertion to the report, CV, or case record with page/paragraph references
- Tag `[VERIFY]` on any case citation or statutory reference requiring confirmation
- Distinguish challenges to entire testimony vs. specific opinions — tailor motion scope
- Note jurisdiction-specific layers (e.g., affidavit-of-merit statutes in medical malpractice) beyond Daubert/Frye
- Distinguish Daubert's flexible reliability inquiry from Frye's binary general-acceptance test
- Maintain objective tone — acknowledge sound work rather than manufacturing weak challenges
- Mark every page Attorney-Client Privileged / Work Product
