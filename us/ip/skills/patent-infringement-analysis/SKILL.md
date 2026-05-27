---
name: patent-infringement-analysis
title: Patent Infringement Analysis
description: Generates a structured patent infringement analysis mapping claims to accused product features via claim charts. Covers Phillips claim construction, literal infringement, doctrine of equivalents, validity defenses, damages, and strategic recommendations. Use when analyzing patent infringement, preparing claim charts, evaluating IP litigation risk, or assessing licensing and design-around options.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/patent-infringement-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# Patent Infringement Analysis

Produces a report evaluating whether an accused product or process infringes asserted patent claims, for litigation counsel, in-house teams, or technical experts.

## Prerequisites

Gather before starting:

1. **Asserted patent(s)** — specification, claims, file history, prosecution docs, amendments, office action responses
2. **Accused product/process** — specs, manuals, marketing materials, drawings, schematics, source code, reverse engineering reports
3. **Prior art** — patents, publications, technical standards relevant to the technology
4. **Asserted claims identified** — which independent and dependent claims are at issue

## Report Structure

### 1. Executive Summary

| Element | Content |
|---|---|
| Overall conclusion | Qualified: "strong likelihood," "probable," "unlikely," or "no infringement" |
| Per-claim assessment | Bottom-line for each independent claim and key dependents |
| Recommendations | Cease / license / litigate / design-around / post-grant proceedings |
| Critical risks | Willfulness exposure, SOL deadlines, related litigation |
| Key uncertainties | Ambiguous terms, missing technical info, unsettled legal questions |

### 2. Patent Overview

- **Bibliographic data** — number, title, dates (issue/filing/priority), inventors, assignee, family
- **Technical field** — problem, inventive concept, advantages over prior art
- **Prosecution highlights** — amendments, narrowing arguments, disclaimer/estoppel, canceled claims
- **Asserted claims** — dependency relationships, selection rationale
- **Patent status** — litigation history, post-grant proceedings, terminal disclaimers

### 3. Claim Construction

Apply **Phillips v. AWH Corp.** framework for each disputed term:

| Source | Analysis |
|---|---|
| Claim language | Ordinary meaning to POSITA; context from surrounding claims |
| Specification | Definitions, "as used herein," lexicography, consistent usage |
| Prosecution history | Amendments, distinguishing arguments, disclaimer/estoppel |
| Claim differentiation | Presume different claims have different scope |
| Extrinsic evidence | Expert testimony, dictionaries — less weight than intrinsic |

Output as:

| Claim Term | Proposed Construction | Support (col:ln or prosecution doc + page) |
|---|---|---|

Flag ambiguous terms with alternative constructions and outcome impact. For **§ 112(f) means-plus-function** limitations: identify function → corresponding structure in spec → equivalents.

### 4. Accused Product Description

- Product name, model, purpose, high-level operation
- Feature-by-feature description paralleling claim structure
- Cite evidence precisely: document title, page/section, figure, code file:line
- Note versions/configurations analyzed
- Flag non-observable features and information gaps needing discovery

### 5. Element-by-Element Infringement Analysis

For each asserted claim, produce a **claim chart**:

| # | Claim Limitation (as construed) | Accused Feature (with evidence) | Literal? | DOE? |
|---|---|---|---|---|

**Literal infringement**: Apply all-elements rule. Cite specific evidence for each correspondence. Explain *why* each feature meets the limitation — no conclusory statements.

**Doctrine of equivalents** (where not literally met): Apply function-way-result or insubstantial differences test. Check DOE limitations:

| Limitation | Test |
|---|---|
| Prosecution history estoppel | Amendment-based narrowing? Festo presumption of surrender |
| Vitiation | Would DOE eliminate the limitation? |
| Dedication to public | Disclosed but not claimed? Johnson & Johnston |
| All-limitations rule | Apply per-element, not to invention as a whole |

**Infringement theories** (as applicable):
- **Direct** (§ 271(a)) — single entity performs all limitations
- **Inducement** (§ 271(b)) — knowledge + specific intent + active inducement
- **Contributory** (§ 271(c)) — material component + no substantial non-infringing uses + knowledge

State per-claim infringement likelihood with qualification and basis.

### 6. Validity Considerations

Presumed valid (§ 282). Invalidity: clear and convincing (litigation) or preponderance (PTAB).

| Defense | Framework |
|---|---|
| Anticipation (§ 102) | Single reference with every limitation; element-by-element; check statutory bars |
| Obviousness (§ 103) | Graham factors; secondary considerations (commercial success, long-felt need, failure of others, copying) |
| Eligibility (§ 101) | Alice/Mayo two-step: abstract idea/natural phenomenon → inventive concept |
| § 112 defenses | Written description, enablement, definiteness |

Flag uncited prior art not before the examiner — these are strong IPR candidates.

### 7. Defenses, Risks, and Strategy

**Equitable defenses**: Laches, equitable estoppel, implied license, exhaustion/first sale, inequitable conduct.

**Damages**:

| Factor | Framework |
|---|---|
| Lost profits | Panduit four-factor test |
| Reasonable royalty | Georgia-Pacific factors; hypothetical negotiation |
| Apportionment | Entire market value rule; isolate patented feature value |
| Marking (§ 287) | Product marking status; pre-notice damages exposure |
| Enhanced damages | Willfulness risk; opinion of counsel value |

**Strategy**: Evaluate litigation cost/timeline, design-around feasibility, licensing range from comparables, IPR timing (one-year post-complaint deadline), venue under TC Heartland, and business impact.

### 8. Conclusion and Recommendations

- Synthesize per-claim likelihood integrating construction + analysis + validity
- Candid strengths/weaknesses assessment
- Prioritized next steps by urgency and cost
- Information gaps requiring investigation
- Time-sensitive actions: preservation, opinion of counsel, IPR deadlines

## Checks

- Maintain neutral, analytical tone — acknowledge both strengths and weaknesses
- Cite precisely: patent col:ln, prosecution doc date + page, product doc + section, cases in Bluebook
- Use `[VERIFY]` for any citation not confirmed from source materials
- Distinguish known evidence from areas needing further investigation
- Qualify all assessments based on evidence strength — never overstate
- For means-plus-function claims, always identify structure + equivalents (narrower scope than general DOE)
- Flag willfulness risk early when accused infringer has knowledge of patent
