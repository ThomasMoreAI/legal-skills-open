---
name: succession-planning-summary
title: Succession Planning Summary
description: Synthesizes wills, trusts, beneficiary designations, powers of attorney, and healthcare directives into a unified estate succession reference document. Covers asset distribution maps, trust structures, fiduciary appointments, special provisions, and administration timelines. Use when onboarding to an estate matter, preparing executor guides, summarizing estate plans, or bridging complex instruments with practical implementation steps.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/succession-planning-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: trusts-and-estates
language: en
tags: [summarization, summary, transactional]
---

# Succession Planning Summary

Produces a single reference document that consolidates all estate planning instruments for executors, trustees, and beneficiaries.

**Header disclaimer**: This summary does not replace legal counsel. Mark unverified or ambiguous provisions with `[REQUIRES LEGAL REVIEW]`.

## Prerequisites

1. **Estate planning instruments** — wills, codicils, trust agreements, beneficiary designation forms
2. **Fiduciary documents** — powers of attorney, healthcare directives/proxies
3. **Asset inventory** — real property, financial accounts, business interests, significant personal property
4. **Amendments or restatements** — with dates, to establish document priority

## Quick Start

1. Collect all instruments and confirm which is most recent for each category
2. Build the executive overview table (plan structure, beneficiaries, fiduciaries)
3. Map every asset to its transfer mechanism (probate, trust, or beneficiary designation)
4. Document each trust, fiduciary appointment, and special provision
5. Draft the administration timeline with statutory deadlines
6. Flag gaps, conflicts, and time-sensitive items

## Output Structure

### 1. Executive Overview

| Element | Content |
|---|---|
| Plan structure | Revocable trust-centered, will-based, or hybrid |
| Primary beneficiaries | Named individuals/entities with relationship |
| Major asset categories | Real property, financial, business, personal property |
| Distribution philosophy | Equal split, needs-based, conditional, phased |
| Key fiduciaries | Executor, trustee(s), guardian(s) |

### 2. Asset Distribution Map

Organize by transfer mechanism. Use this table for each asset:

| Asset | Transfer Mechanism | Primary Beneficiary | Contingent Beneficiary | Conditions |
|---|---|---|---|---|
| {asset} | probate / trust / beneficiary designation | {name, %} | {name, %} | {if any} |

**Probate assets**: specific bequests, percentage/residuary allocations, contingent chains.
**Non-probate transfers**: beneficiary designations (retirement, life insurance, POD/TOD), joint tenancy, trust-funded assets.

### 3. Trust Structures

For each trust:

| Field | Detail |
|---|---|
| Name & type | e.g., Revocable Living Trust, ILIT, SNT, CRUT |
| Trustee / Successor | Names, order of succession |
| Purpose | Asset protection, tax planning, special needs, charitable |
| Funding source | Pour-over will, direct transfer, beneficiary designation |
| Distribution standard | HEMS, discretionary, mandatory income, unitrust % |
| Distribution timing | Age-based, milestone-based, immediate, staggered |
| Termination trigger | Age attainment, death, purpose fulfilled |

Note trust-to-trust relationships and pour-over provisions.

### 4. Fiduciary Appointments

| Role | Primary | Successor(s) | Scope / Limitations |
|---|---|---|---|
| Executor / Personal Rep. | | | |
| Trustee (per trust) | | | |
| Guardian (minor children) | | | |
| POA — Financial | | | Durable? Springing? |
| POA — Healthcare / Proxy | | | |
| Trust Protector | | | Modification powers? |

### 5. Special Provisions

Flag each that applies:

- Conditions precedent (age, sobriety, education milestones)
- Tangible personal property memoranda
- Business succession (buy-sell, management transition)
- Charitable giving (outright, CRT, private foundation, DAF)
- Tax planning structures (A/B trust, QTIP, GRAT, dynasty trust)
- Spendthrift / asset protection clauses
- In terrorem (no-contest) clauses
- Digital asset provisions

### 6. Administration Timeline

| Phase | Actions | Deadline |
|---|---|---|
| Immediate (0–30 days) | Secure assets, locate documents, notify institutions, file death certificate | — |
| Short-term (1–6 months) | Open probate if required, file inventory, notify beneficiaries, apply for EIN | Creditor period varies by state |
| Mid-term (6–12 months) | Asset valuation, Form 706 decision (9 mo + 6-mo extension), disclaimer deadline (9 mo) | IRC § 2518 |
| Distribution | Satisfy debts/taxes, fund sub-trusts, make bequests, distribute residuary | After creditor period closes |
| Closing | Final accounting, beneficiary receipts, petition to close | — |

### 7. Gaps, Conflicts & Action Items

Flag each:

- Assets not addressed by any instrument
- Contradictions between documents (e.g., will vs. beneficiary designation)
- Outdated designations (pre-divorce, deceased beneficiaries)
- Missing referenced documents (e.g., personal property memorandum)
- State-specific issues requiring local counsel
- Time-sensitive elections or disclaimers at risk

## Guidelines

- Define legal terms in plain language parenthetically on first use
- Cross-reference related provisions across instruments (pour-over will → trust, designation → trust sub-account)
- Beneficiary designations generally control over will/trust provisions — flag conflicts for attorney review
- Include a table of contents for estates with 3+ trusts or 10+ distinct assets
- Attribute every statement to its source document and date
