---
name: prenuptial-agreement
title: Prenuptial / Postnuptial Agreement
description: Drafts enforceable prenuptial and postnuptial agreements for US jurisdictions with financial disclosure schedules, property classification, spousal support provisions, estate waivers, and procedural fairness safeguards. Ensures compliance with UPAA/UPMAA frameworks. Use when drafting prenuptial agreements, postnuptial agreements, marital property agreements, premarital contracts, or antenuptial agreements.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/prenuptial-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Prenuptial / Postnuptial Agreement

Drafts an enforceable marital agreement with financial disclosure, property classification, support provisions, and procedural safeguards tailored to the governing US jurisdiction.

## Quick Start

Gather before drafting:

1. **Agreement type** — prenuptial (pre-marriage) or postnuptial (during marriage)
2. **Governing jurisdiction** — state of execution and residence of each party
3. **Applicable framework** — UPAA, UPMAA, or state-specific statute
4. **Financial disclosures** — asset inventories, account statements, business valuations, income documentation for both parties
5. **Existing documents** — prior marital agreements, estate plans, business operating agreements

## Core Workflow

### 1. Jurisdictional Analysis

Determine before drafting:

| Factor | Options |
|---|---|
| Framework | UPAA / UPMAA / state-specific statute |
| Disclosure standard | Full & fair / reasonable / statutory schedule |
| Spousal support waiver | Permitted / limited / unconscionability review at enforcement |
| Waiting period | State-required minimum before wedding (e.g., 30 days) |
| Independent counsel | Required / recommended / waivable |
| Execution formalities | Notarization, witnesses, self-proving affidavit |

### 2. Financial Disclosure Schedules (Exhibits A / B)

Each party discloses under sworn representation:

- Real property — legal descriptions, FMV, encumbrances
- Financial accounts — institution, type, approximate balance
- Retirement accounts — plan type, vested amount, beneficiary
- Business interests — entity, ownership %, valuation methodology
- Intellectual property — description, estimated value
- Vehicles and tangible personal property above threshold
- All liabilities — secured, unsecured, contingent, tax
- Income from all sources — employment, business, investment, rental
- Monthly expenses and regular financial obligations

State that material misrepresentation or concealment may render agreement voidable.

### 3. Property Classification

- **Separate property** — pre-marital assets (reference disclosure schedules), gifts, inheritances received individually
- **Marital property** — assets acquired through earnings/joint effort during marriage
- **Appreciation** — passive (remains separate) vs. active from marital effort (specify treatment)
- **Commingling** — when separate property loses character; tracing methodology
- **Marital residence** — ownership classification, occupancy rights, buyout options, refinancing obligations
- **Business interests** — remains separate; specify compensation for marital contribution (percentage interest / formula payment / explicit waiver)

### 4. Debt Allocation

- **Pre-marital debts**: sole responsibility of incurring party; cross-indemnification and hold-harmless
- **Marital debts**: by incurring party / equal division / proportional to income
- **Joint debts**: primary responsibility and contribution obligations
- **New debt controls**: spousal consent threshold above $[amount]; prohibition on pledging other party's separate property
- **Tax liabilities**: joint return allocation, separate business income liability, audit procedures
- **Dissolution**: assumption/indemnification, refinancing deadlines, asset sale waterfall

### 5. Spousal Support

**Full waiver** — include this language:

> Each party forever and irrevocably waives any right to seek temporary or permanent spousal support, maintenance, or alimony regardless of marriage duration, circumstances of dissolution, financial condition, or changed circumstances.

Require acknowledgments that each party understands the waiver's significance, has evaluated earning capacity, has considered self-sufficiency, and consents voluntarily.

**Limited support** — specify triggering conditions, duration caps, amount caps, termination events, and modifiability.

**Jurisdiction check**: if state requires independent counsel for support waivers or applies unconscionability review at enforcement, add safeguards and fairness-at-enforcement language.

### 6. Estate and Death Provisions

- Waiver of elective share / statutory spousal share / community property rights (if agreed)
- Life insurance: minimum coverage, ownership, beneficiary designation, survival post-divorce
- Retirement accounts: waiver of survivor benefits, QDRO rights, ERISA protections
- Estate planning coordination: agreement supersedes contrary will/trust provisions
- Prior-relationship children: carve-outs protecting inheritance rights
- Delineation of assets subject to agreement vs. freely disposable by will/trust

### 7. Procedural Fairness Recitals

Include all of the following:

- [ ] Each party advised of right to independent counsel
- [ ] Adequate opportunity to retain and consult separate attorneys
- [ ] If represented: attorney acknowledgment confirming review, explanation, voluntary consent
- [ ] If counsel waived: knowing and voluntary waiver after explanation of significance
- [ ] Prenuptial timing: executed ≥30 days before wedding (or per jurisdiction)
- [ ] No duress, coercion, fraud, or undue influence
- [ ] Complete financial disclosures provided and reviewed
- [ ] Adequate time to review, consider, and negotiate terms
- [ ] If sophistication disparity: extended review period, mandatory counsel, explicit acknowledgments

### 8. Modification, Sunset, and Review

- Amendments require writing, both signatures, same execution formalities as original
- Sunset clause (optional): automatic termination after [X] years or specified event; specify fallback regime
- Periodic review every [X] years or upon significant life changes
- No oral modifications; no waiver by course of conduct

### 9. Dispute Resolution and General Provisions

- **Governing law**: [State] without conflict-of-law principles
- **Venue**: [County/District]
- **Process**: Mandatory mediation → litigation (or binding arbitration)
- **Fees**: prevailing party / proportional to resources / each bears own
- **Severability**: invalid provisions severed; remainder enforceable; reform to intent
- Integration/merger clause; confidentiality; notice provisions
- Binding on heirs, executors, administrators, assigns
- Covenant to execute additional instruments (deeds, beneficiary designations, QDROs)

### 10. Execution Block

| Element | Required? |
|---|---|
| Party signatures with printed name and date | Always |
| Witness attestation (2 disinterested witnesses) | Check jurisdiction |
| Notarial acknowledgment with commission expiration, county, seal | Check jurisdiction |
| Attorney certificates of independent legal advice | Check jurisdiction |
| Self-proving affidavit | If permitted |

## Pitfalls and Checks

- Verify UPAA vs. UPMAA vs. independent framework before drafting — controls disclosure requirements, support waiver enforceability, and execution formalities
- Confirm execution timing satisfies any state-mandated waiting period before the wedding
- Never draft spousal support waivers without checking whether jurisdiction applies unconscionability review at enforcement (not just execution)
- Flag potentially unenforceable provisions with `[JURISDICTION NOTE]`
- Mark uncertain statutory citations with `[VERIFY]`
- If either party lacks independent counsel, strengthen procedural safeguards and include explicit waiver-of-counsel acknowledgments
- Financial disclosures must use approximate balances, not vague ranges
- Address ERISA preemption when waiving retirement account survivor benefits
- Include execution instructions: signing sequence, number of copies, documents executed simultaneously
