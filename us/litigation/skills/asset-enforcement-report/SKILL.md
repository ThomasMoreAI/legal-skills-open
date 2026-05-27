---
name: asset-enforcement-report
title: Post-Judgment Asset & Enforcement Report
description: Generates a post-judgment asset and enforcement report synthesizing debtor asset investigations, exemption analysis, fraudulent transfer assessment, and prioritized collection strategies. Use when preparing judgment enforcement plans, debtor asset profiles, collection status reports, or post-trial recovery analysis.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/asset-enforcement-report
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis]
---

# Post-Judgment Asset & Enforcement Report

Produces a strategic enforcement roadmap for collecting on a judgment by synthesizing asset investigations, exemption analysis, and collection results into prioritized recommendations.

## Required Inputs

1. **Judgment documents** — order text, amount (principal, interest, costs, fees), case caption, court, entry date
2. **Post-judgment discovery** — debtor examination transcripts, interrogatory responses, document production, third-party subpoena returns
3. **Public records** — property records, entity filings, UCC searches, vehicle registrations, professional licenses
4. **Enforcement history** — writs, garnishment orders, levy results, lien recordings, contempt proceedings
5. **Correspondence** — demand letters, settlement communications, debtor/counsel exchanges

## Report Sections

### 1. Financial Summary

| Item | Amount |
|---|---|
| Original judgment (principal) | $ |
| Pre-judgment interest | $ |
| Attorney's fees & costs awarded | $ |
| Post-judgment interest (rate x days) | $ |
| **Total due** | **$** |
| Less: recovered to date | ($ ) |
| Less: enforcement costs | ($ ) |
| **Current deficiency** | **$** |

Note judgment renewal deadline and dormancy period under applicable state law.

### 2. Asset Profile

Document each category in structured format:

**Real Property** — Address/APN, owner(s), deed recording, assessed/FMV, mortgage balance(s), net equity, homestead exemption (statute, amount, eligibility), tenancy-by-entirety issues.

**Business Interests** — Entity name/type/state, ownership %, registered agent, UCC filings, charging order viability vs. direct execution, related-party transfers.

**Financial Accounts**

| Account | Institution | Type | Exempt? | Basis | Accessible balance |
|---|---|---|---|---|---|
| | | | | | |

- Distinguish ERISA-qualified plans (fully protected) from IRAs/state-exemption accounts with dollar caps
- Flag commingled exempt funds (Social Security, VA, disability) — federal lookback protections apply

**Personal Property** — Vehicles (VIN, value, lien status), digital assets/cryptocurrency, other valuable property subject to execution.

### 3. Enforcement Actions Chronicle

| Action | Date | Legal basis | Target | Result | Net recovery |
|---|---|---|---|---|---|
| Judgment lien | | | Property (recording #, priority) | | |
| Wage garnishment | | State statute, 15 USC 1673 | Employer | | |
| Bank levy | | Writ of execution | Institution/account | | |
| Property execution | | | Asset | Sale proceeds less costs | |
| Charging order | | | LLC/partnership interest | | |
| Contempt/sanctions | | | Discovery compliance | | |

Garnishment cap: lesser of 25% disposable earnings or amount exceeding 30x federal minimum wage/week.

### 4. Exemption & Obstacles Analysis

| Exemption | Statute | Claimed | Valid? | Analysis |
|---|---|---|---|---|
| Homestead | [State statute] | $ | | Residency verified? Equity above cap? |
| Retirement | ERISA / [State] | $ | | Qualified plan vs. IRA dollar limit |
| Personal property | [State statute] | $ | | Within statutory limits? |
| Wildcard | [State statute] | $ | | Properly applied? |

Flag questionable claims with specific grounds for objection.

### 5. Fraudulent Transfer Assessment

Analyze under UVTA (Uniform Voidable Transactions Act).

**Badges of Fraud checklist:**
- Transfer to insider/family member
- Debtor retained possession/control post-transfer
- Transfer concealed
- Transfer after suit filed or judgment entered
- Substantially all assets transferred
- Less than reasonably equivalent value received
- Debtor insolvent at time or rendered insolvent
- Business assets transferred, new entity doing same business

**Limitations**: Actual fraud — typically 4 years; constructive fraud — typically 1 year under UVTA. [VERIFY state-specific periods]

**Cost-benefit**: Weigh transferred asset value vs. litigation cost, evidence strength, transferee solvency.

### 6. Jurisdictional Issues

Address when debtor relocated or holds multi-state assets:
- Domestication under Uniform Enforcement of Foreign Judgments Act (filing, notice, challenge period)
- Compare exemption laws between rendering and enforcement states
- Flag strategic relocation to exploit more protective exemptions

### 7. Strategic Recommendations

**Classify debtor collectibility:**

| Classification | Criteria | Approach |
|---|---|---|
| Solvent | Substantial non-exempt assets | Aggressive multi-front enforcement |
| Marginally collectible | Limited accessible assets | Selective cost-effective remedies |
| Judgment-proof | No recoverable assets beyond exemptions | Settlement, payment plan, or judgment sale |

**Prioritized action plan:**

| # | Action | Est. cost | Timeline | Projected recovery | Priority |
|---|---|---|---|---|---|
| | | | | | |

Actions to evaluate: supplemental debtor examination, bank levies, wage garnishment, judgment lien recording (all relevant counties), fraudulent transfer complaint, turnover orders, exemption objections, settlement/structured payment, judgment sale to third party.

### 8. Documentation Index

| Exhibit | Description | Date | Source |
|---|---|---|---|
| A | Judgment order | | Court |
| B | Debtor examination transcript | | Court reporter |
| C | Property records | | County recorder |

## Pitfalls & Checks

- Calculate post-judgment interest precisely — state rate, start date, methodology
- Cite specific transcript pages (page:line) for debtor asset admissions
- Redact per court protective orders and Gramm-Leach-Bliley Act
- Document all investigative sources (databases, subpoena targets, service dates)
- Provide FMV support for significant assets (comparables, appraisals, tax assessments)
- Flag pending appeals, stays, or bankruptcy filings affecting enforcement
- Be candid about collectibility — do not overstate recovery prospects
- All statutory citations must reference the specific state; use [VERIFY] for uncertain citations
- Assumes U.S. jurisdiction; state rules vary significantly for exemptions, garnishment limits, and fraudulent transfer periods

---

**Key changes made:**

- **Description** tightened — removed "into a strategic roadmap for judgment creditors" and "in commercial litigation" for conciseness while keeping trigger guidance
- **"Prerequisites" → "Required Inputs"** — more direct heading
- **"Output Structure" → "Report Sections"** — clearer label
- **Real Property / Business Interests** collapsed from verbose tables into inline field lists — same information, fewer tokens
- **Removed redundant sub-headers** like "For each asset category, document in structured format:" and "For each action taken, document:"
- **"Guidelines" → "Pitfalls & Checks"** — aligned with best-practice section naming
- **Stripped filler phrases** throughout (e.g., "Organize exhibits sequentially with clear labels" → table speaks for itself)
- **Tightened checklist items** — removed checkbox syntax (not interactive), kept as bullet list
- **Removed "§" symbols** for plain-text compatibility
