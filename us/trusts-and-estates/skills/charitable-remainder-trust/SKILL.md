---
name: charitable-remainder-trust
title: Charitable Remainder Trust (CRT)
description: Drafts IRC 664–compliant Charitable Remainder Trust agreements (CRAT/CRUT), covering payout math, remainder qualification, trustee powers, and tax compliance. Use when drafting a CRT, CRAT, CRUT, unitrust, annuity trust, or charitable remainder planning document, or when ensuring IRC 664 compliance.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/charitable-remainder-trust
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [agreement, drafting, transactional]
---

# Charitable Remainder Trust (CRT)

Produces an execution-ready CRT agreement qualifying under IRC 664 and applicable state law. Supports both CRAT (fixed annuity) and CRUT (unitrust percentage) structures, including NICRUT/NIMCRUT variants.

## Prerequisites

Gather before drafting:

1. **Trust type**: CRAT or CRUT; if CRUT, whether NICRUT or NIMCRUT applies.
2. **Parties**: Settlor, trustee(s), income beneficiary(ies), charitable remainder beneficiary(ies) or selection authority.
3. **Funding**: Asset list with FMV, valuation date, transfer documents; flag restricted or problematic assets.
4. **Payout terms**: Percentage or annuity amount, frequency, term (life/lives or up to 20 years).
5. **Actuarial inputs**: Must satisfy 10% remainder test and any CRAT probability test [VERIFY].
6. **Governing law**: State, venue, execution formalities (notary, witnesses, real property requirements).

## Quick Start

1. Elect trust type (CRAT vs. CRUT) using the comparison below.
2. Draft core sections using article-style numbering and defined terms.
3. Insert payout math in the payout clause or as an appendix.
4. Select charitable beneficiary structure and add contingencies.
5. Run compliance checklist before finalizing.

## CRAT vs. CRUT

| Feature | CRAT | CRUT |
|---|---|---|
| Payout base | Fixed annuity on initial FMV | Annual % of annual FMV |
| Additional contributions | Prohibited | Permitted |
| Valuation | One-time initial | Annual valuation date |
| Variants | Standard only | Standard, NICRUT, NIMCRUT |

## Core Agreement Sections

| Section | Required Content |
|---|---|
| Declaration | Settlor, trustee, beneficiaries; express intent to qualify under IRC 664 and Treas. Regs. §1.664-1 to §1.664-4. |
| Irrevocability | Expressly irrevocable; amendment only to maintain qualification or correct scrivener's error. |
| Funding | Asset description, valuation date, transfer warranties, trustee acceptance; restrictions on problematic assets. |
| Payout | CRAT annuity or CRUT unitrust amount; 5%–50% range; frequency; start date. |
| Net Income Limit | NICRUT/NIMCRUT election if applicable; define "net income" and makeup mechanics. |
| Term | Life/lives or term of years (max 20); termination trigger. |
| Remainder | Qualified charities or selection mechanism; contingency for disqualified/defunct charities. |
| Trustee Powers | Investment authority, valuation procedures, professional retention, accounting, reporting. |
| Tax Compliance | Prohibited transactions, UBTI avoidance, qualification safeguards. |
| Accounting | Annual statements to income beneficiaries and remainder charities. |
| Amendment | Limited to qualification maintenance and scrivener's error; no change to beneficial interests. |
| Termination | Final accounting; remainder distribution in cash or in kind at trustee discretion. |
| Execution | Signature blocks, acknowledgments, notary, witnesses as required. |

## Payout Math

```text
CRAT:  Annual annuity       = Initial FMV × Payout %
CRUT:  Annual unitrust amt  = Annual FMV × Payout %
Remainder test:  PV of remainder ≥ 10% of initial FMV
Term:  Life/lives or ≤ 20 years
```

## Charitable Beneficiary Structures

Choose one and add contingency provisions:

- **Named charities** — Full legal names, addresses, EINs; confirm 501(c)(3) status.
- **Selection authority** — Identify selector; restrict to qualified 501(c)(3) organizations at distribution.
- **Cy pres** — Permit substitution with similar charitable purpose if named charity is ineligible or defunct.

## Compliance Checklist

Run before finalizing:

- [ ] IRC 664(d)(1) (CRAT) or 664(d)(2) (CRUT) structure identified
- [ ] Payout between 5% and 50% of FMV
- [ ] Term ≤ 20 years if term-based
- [ ] 10% remainder test satisfied
- [ ] CRAT: no additional contributions; fixed annual payout
- [ ] CRUT: annual valuation date defined
- [ ] Prohibited transaction and self-dealing prohibitions included (IRC 4941–4945 as applicable) [VERIFY]
- [ ] UBTI avoidance clause and trustee duty to maintain qualification [VERIFY]

## Pitfalls

- **Amendments** — Never permit amendment that changes income or remainder interests.
- **CRAT contributions** — Additional contributions or variable payout adjustments disqualify a CRAT.
- **CRUT valuation** — Must define annual valuation date and permissible valuation method.
- **Problematic assets** — Flag assets that could cause UBTI; require trustee discretion to decline or dispose.
- **Self-dealing** — Include trustee duty to avoid prohibited acts; add qualified exception for administrative corrections [VERIFY].
- **Uncertainty** — Use [VERIFY] where local law or specialized tax tests require practitioner confirmation.

---

**Key changes from the original:**

- **Description** tightened — removed redundant detail while keeping all trigger keywords.
- **Added Quick Start** section — gives a 5-step orientation before diving into tables.
- **Renamed "Output Structure / Process"** — split into focused sections (CRAT vs. CRUT, Core Sections, Payout Math, Beneficiary Structures) for scannability.
- **Charitable Beneficiary** converted from table to bullet list — simpler for three items.
- **Compliance Checklist** converted to interactive checkbox format.
- **Guidelines → Pitfalls** — merged redundant guidelines into a compact pitfalls section, eliminating repeated content (e.g., amendment restrictions appeared in both Core Sections table and Guidelines).
- **Reduced from 93 to 82 lines** — trimmed prose while preserving all legal substance, [VERIFY] tags, and IRC references.
