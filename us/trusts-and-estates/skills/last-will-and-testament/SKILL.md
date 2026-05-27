---
name: last-will-and-testament
title: Last Will and Testament
description: 'Drafts and structures U.S. Last Will and Testament documents. Trigger when the user needs to draft, revise, or review a will covering executor/guardian appointments, specific or residuary distributions, contingency planning, or execution-ready attestation and self-proving packaging. Applies to keywords: last will, testament, probate, executor, guardian, residuary, revocation, no-contest, ademption, predeceased beneficiary, elective share.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/last-will-and-testament
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [agreement, drafting, transactional]
---

# Last Will and Testament

Draft a probate-ready testament mapping client intent to enforceable will language under the applicable state's formalities.

## Quick Start

1. Confirm testator identity, capacity, age, and domicile state.
2. Collect family map (spouse, children, adopted/step, minors, excluded persons).
3. Identify prior wills/codicils, trusts, POA, marriage agreements, beneficiary designations.
4. Gather asset/liability inventory (real estate, business interests, personalty, digital assets, debts).
5. Select fiduciaries: executor + alternate; guardian(s) for minors (person and estate if split).
6. Confirm state execution rules: witness count, disqualifications, notarization, self-proving standard [VERIFY].
7. Map risk preferences: spendthrift concerns, anti-lapse treatment, common-disaster clauses, contest exposure.
8. Decide revocation strategy and compatibility with non-probate plans (trusts, TOD/POD, joint tenancies).

## Core Workflow

### Step 1 — Intake Validation

| Area | Collect | Pitfall |
|---|---|---|
| Identity | Full legal names, addresses, domicile | Misspelled names, outdated details |
| Family | All children + minor care needs; step/adopted distinctions | Predeceased-child or future-child disputes |
| Fiduciaries | Executor + alternate; guardian of person/estate | No backup executor |
| Property | Specific gifts list + residue universe | Omitted assets causing intestacy spillover |
| Contingencies | Death-before-testator branches, survivorship periods | Gifts failing under predecease or simultaneous death |
| Tax/Costs | Debt, tax, admin-payment sequence | Hidden tax liabilities, creditor disputes |
| Non-Probate | Trust triggers, account beneficiary tags, ownership structures | Conflicting transfers or partial revocations |

### Step 2 — Draft Will Sections

| Section | Must Include | Notes |
|---|---|---|
| Revocation | Revokes all prior wills/codicils | Single clear supersession sentence |
| Funeral/Legacy | Optional memorial choices | Non-binding where desired |
| Executor | Appointment + alternates, authority scope, bond election | Broad statutory powers or explicit limits |
| Guardianship | Guardian of person/estate + alternates | Reasoned notes only if strategically useful |
| Debts & Expenses | Funeral, just debts, admin costs ordering | Align with state default rules |
| Specific Bequests | Itemized gifts with contingencies | Anti-ademption fallback where useful |
| Residuary Clause | Full residual distribution, percentages/classes | Fallback for predeceasing takers required |
| Per Stirpes/Capita | Choice and default mechanics | Plain-language explanation in parent clause |
| Distribution Protections | No-contest clause (jurisdictional check), survivorship period | Many states restrict [VERIFY] |
| Executor Powers | Sale, investment, retention, settlement authority | Preserve liquidity options |
| Finalization | Signature block, witnesses, notary, self-proving affidavit | Match state witness count/order [VERIFY] |

### Step 3 — Assemble Execution Package

Produce the will in numbered-clause order:

1. Revocation
2. Executor and Personal Representative
3. Guardianship of Minors
4. Payment of Expenses, Debts, and Taxes
5. Specific Bequests
6. Residual Estate
7. Contingent Distribution Scheme
8. Powers of Executor
9. Final Provisions
10. Signature, Attestation, Self-Proving Affidavit

### Step 4 — Compliance Checklist

Before finalizing, verify each item:

- [ ] All required fields populated (no `[TBD]` placeholders)
- [ ] Testator capacity language present
- [ ] Alternate fiduciary and guardian provisions included
- [ ] No-contest clause screened for state enforceability [VERIFY]
- [ ] Survivorship and per stirpes/per capita logic consistent
- [ ] State-specific execution formalities mapped [VERIFY]
- [ ] Self-proving block aligned to state statute [VERIFY]
- [ ] Revocation clause does not conflict with prior instruments
- [ ] Non-probate documents cross-referenced consistently

## Formatting Rules

- Numbered clause order throughout.
- All legal names as `[full legal name]`.
- Complex bequests in two-column format: beneficiary / gift.
- Uncertain legal assumptions flagged in a dedicated section.
- Clean signature block with witness and notary placeholders.

## Pitfalls

- **No-contest clauses**: Do not include by default in uncertain states; validate enforceability first [VERIFY].
- **Tax guidance**: Identify assumptions and election impacts only — never give tax avoidance assurances.
- **Elective share / pretermitted heir / community property**: Flag for attorney review when these materially alter distribution.
- **Non-probate conflicts**: Cross-check trusts, joint property, and beneficiary designations against will provisions.
- **Contingencies**: Always add branches for predeceased or disabled beneficiaries with alternate fiduciary/guardian chains.
