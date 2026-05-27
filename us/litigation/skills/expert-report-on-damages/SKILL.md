---
name: expert-report-on-damages
title: Expert Report on Damages
description: Generates a structured expert report on economic damages for U.S. commercial litigation. Produces Daubert-ready, FRE 702-compliant analyses covering lost profits, disgorgement, diminution in value, or reasonable royalty with full FRCP 26(a)(2)(B) disclosure. Use when the user needs a damages expert report, economic loss calculation, damages rebuttal, forensic accounting analysis, or expert disclosure for commercial disputes during discovery, pre-trial, or trial.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/expert-report-on-damages
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis]
---

# Expert Report on Damages

Produces a Daubert-compliant expert damages report for U.S. commercial litigation with defensible methodology, transparent calculations, and full FRCP 26(a)(2)(B) disclosure.

## Prerequisites

1. **Case materials** — pleadings defining damages scope, interrogatory responses, deposition transcripts
2. **Financial records** — income statements, balance sheets, tax returns, sales records, general ledger (3–5 years pre-wrongdoing minimum)
3. **Contracts** — governing relationship, damages caps, limitations of liability
4. **Expert CV** — credentials, certifications, prior testimony list
5. **Industry data** — benchmarks, comparable company data, economic studies
6. **Discovery status** — identify gaps upfront; missing records require disclosed limitations or range opinions

## Report Structure

### 1. Title Page & Engagement Scope

- Retaining party, engagement date, specific questions presented
- Compensation statement: fees not contingent on outcome or amount
- Scope boundaries — what was and was not examined

### 2. Expert Qualifications (FRE 702 / Daubert)

| Element | Required Detail |
|---|---|
| Education | Degrees, institutions, dates |
| Certifications | CPA, CFE, CFA, ABV, CVA as applicable |
| Experience | Years in damages/forensic/valuation; matter types |
| Prior testimony | Case count, deposition vs. trial, jurisdictions |
| Publications | Peer-reviewed articles, conference papers, committee service |

### 3. Materials Reviewed

Itemized list of all documents, data, and testimony considered. Every item traceable to source.

### 4. Assumptions & Limitations

| # | Assumption / Limitation | Basis for Reasonableness |
|---|---|---|
| 1 | Accuracy of financial statements | Third-party preparation; management representations |
| 2 | Continuation of pre-breach trends | Historical performance data |
| 3 | [Case-specific] | [Support] |

Flag unavailable records, incomplete discovery, or destroyed documents. Explain how each gap affects certainty or requires a range opinion.

### 5. Factual Background

Objective chronological narrative from case documents covering:
- Parties, business relationship, contract terms, economic significance
- Alleged wrongful conduct: start date, duration, specific acts/omissions
- Damages accrual period with key milestone dates
- Industry/market context: growth rates, competitive dynamics, regulatory changes
- Alternative causes considered: management decisions, market downturns, competitor actions, unrelated operational issues

### 6. Methodology

#### Damages Type Selection

| Type | When Applicable |
|---|---|
| Lost profits ("but for") | Lost revenue/income from breach or tort |
| Diminution in value | Permanent impairment to asset or business value |
| Disgorgement | Defendant's profits from wrongful conduct |
| Reasonable royalty | IP infringement; licensing disputes |
| Cost to cure | Remediation for defective performance |

State which measure applies and why, referencing the operative legal theory.

#### Daubert Reliability Factors

Address each for every methodology chosen:

1. **Testability** — can be tested or falsified
2. **Peer review** — published in recognized literature or professional standards
3. **Error rate** — known/potential rate disclosed
4. **Standards** — governed by AICPA, NACVA, or equivalent [VERIFY current editions]
5. **General acceptance** — accepted in forensic accounting/economics community

#### Lost Profits Framework

1. Establish pre-wrongdoing baseline: gross, operating, and net margins over 3–5 historical periods
2. Project "but for" revenues using trend analysis, regression, or market-based projections
3. Subtract actual results during damages period
4. Adjust for mitigation efforts, avoided costs, contingency discounts, tax effects

#### Diminution in Value Framework

Apply valuation approaches consistently pre- and post-event:

| Approach | Techniques | Key Inputs |
|---|---|---|
| Market | Comparable company, precedent transactions | Revenue/EBITDA multiples |
| Income | DCF, capitalization of earnings | Discount rate, growth rate, normalized earnings |
| Cost | Replacement/reproduction cost | Asset inventory, depreciation |

Diminution = Pre-event value minus Post-event value. Use same methodology for both dates.

### 7. Damages Calculations

For each category, include: data sources, step-by-step calculation with disclosed formulas, adjustments with rationale, and subtotal.

Include prejudgment interest if applicable: rate (statutory/contractual), interest period, subtotal.

State total damages. All numbers must trace to source documents or disclosed assumptions.

- Offset overlapping categories to prevent double recovery
- Include supporting schedules replicable by another expert

#### Sensitivity Analysis

| Key Assumption | Low | Base | High |
|---|---|---|---|
| Revenue growth rate | X−2% | X% | X+2% |
| Profit margin | X−1% | X% | X+1% |
| Discount rate | X+1% | X% | X−1% |
| **Total Damages** | **$___** | **$___** | **$___** |

### 8. Opinions & Conclusions

State each opinion to "a reasonable degree of [economic/financial] certainty" per jurisdiction convention:

> **Opinion 1:** [Figure or range] for [category], based on [methodology].
> **Opinion 2:** Under alternative scenario [X], damages are [Y].

Identify factors that could cause actual damages to differ. Confine opinions to expertise area and available evidence.

### 9. Exhibits & Appendices

- [ ] Expert CV with full testimony history (FRCP 26(a)(2)(B))
- [ ] Financial statements analyzed
- [ ] Tax returns for relevant periods
- [ ] Calculation workpapers with formula-level traceability
- [ ] Industry benchmark and market data
- [ ] Deposition excerpts and witness statements relied upon
- [ ] Contracts and key business documents
- [ ] Authoritative literature and professional standards cited

## Compliance Checklist

- [ ] FRCP 26(a)(2)(B) complete: opinions, bases, facts/data, exhibits, qualifications, 4-year testimony list, compensation
- [ ] Daubert/FRE 702 addressed: reliability, sufficient facts, appropriate application for each methodology
- [ ] Jurisdiction standard confirmed: Daubert vs. Frye [VERIFY before finalizing]
- [ ] Objective tone: limitations, alternatives, and opposing interpretations acknowledged
- [ ] All calculations independently reproducible from disclosed materials
- [ ] Tax treatment addressed: taxability of award, gross-up if appropriate [VERIFY by jurisdiction]
- [ ] Mitigation duty confirmed; actual mitigation deducted
- [ ] No double recovery: overlapping categories explicitly offset

## Troubleshooting

**Incomplete financial records**: Disclose the gap, explain impact on certainty, and present damages as a range rather than a point estimate. Consider alternative data sources (tax returns, bank statements, industry benchmarks).

**Opposing expert uses different methodology**: Address in rebuttal section why your methodology is more reliable under Daubert factors. Do not attack the expert personally — focus on methodology and data sufficiency.

**Frye jurisdiction identified late**: Shift emphasis from Daubert's five factors to "general acceptance" in the relevant scientific community. Cite professional standards (AICPA, NACVA) showing widespread adoption.

**Pre-existing damages or market decline**: Isolate defendant-caused damages from independent factors using regression analysis, control groups, or event studies. Document the separation methodology explicitly.

**Court excludes a damages category**: Structure calculations modularly so excluded categories can be removed without invalidating the remainder.

---

Key changes from the original:

- **Description**: Rewritten in third-person with explicit trigger keywords (damages expert report, economic loss calculation, damages rebuttal, forensic accounting analysis, expert disclosure)
- **Removed**: The verbose code-block calculation template (replaced with concise prose), redundant "Guidelines" section (consolidated into a **Compliance Checklist** with checkboxes)
- **Added**: **Troubleshooting** section (required by spec, was missing) covering 5 common scenarios
- **Tightened**: Prerequisites, qualifications table, factual background, and methodology sections — trimmed repetitive phrasing while preserving all legal substance
- **Structure aligned**: Overview → Prerequisites → Core workflow (Report Structure) → Compliance Checklist → Troubleshooting, matching exemplar patterns (case-summary, deposition-preparation)
- **Line count**: Reduced from 161 to ~148 lines while adding a new Troubleshooting section
