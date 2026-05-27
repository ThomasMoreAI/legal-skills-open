---
name: bankruptcy-proof-of-claim
title: Proof of Claim (Bankruptcy)
description: Drafts filing-ready proofs of claim for U.S. bankruptcy proceedings using Official Form B 410 under FRBP 3001. Handles secured, unsecured priority, and general unsecured claims with proper valuation, documentation, and bar date compliance. Use when a creditor needs to file or amend a proof of claim in a bankruptcy case.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/bankruptcy-proof-of-claim
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
tags: [drafting, litigation]
---

# Proof of Claim (Bankruptcy)

Prepares a complete proof of claim for filing with the U.S. Bankruptcy Court, compliant with FRBP 3001 and Official Form B 410.

## Prerequisites

1. **Case information** — debtor name, case number, court, chapter, bar date
2. **Creditor information** — legal name, address, authorized agent
3. **Claim basis** — contract, promissory note, invoice, judgment, statutory, tort
4. **Claim amount** — principal, interest (rate and calculation), fees, costs
5. **Security interest** (if secured) — collateral description, lien perfection documents, valuation
6. **Priority status** (if priority) — statutory basis under § 507(a)
7. **Supporting documents** — contracts, invoices, account statements, UCC filings, judgments

## Quick Start

1. Confirm bar date and calculate days remaining — this is jurisdictional
2. Gather all prerequisites above; request missing items before drafting
3. Calculate total claim as of petition date using the claim calculation table below
4. Draft Form B 410 Parts 1–4 per the output structure
5. Attach all supporting documentation per FRBP 3001(c)
6. Include signature block with penalty-of-perjury declaration

## Output Structure

### Part 1: Claim Information

| Field | Value |
|---|---|
| Debtor name and case number | [From case info] |
| Creditor name and mailing address | [From creditor info] |
| Claim amount as of petition date | [Calculated total] |
| Basis for claim | [Category and description] |
| Post-petition interest/charges | [Yes/No — note separately] |
| Subject to setoff | [Yes/No — describe if yes] |

### Part 2: Secured Claim

Complete only if claim is secured:

- **Collateral value** — real property, personal property, or other (state valuation basis)
- **Perfection basis** — mortgage, deed of trust, UCC filing, or judicial lien
- **Secured amount** — lesser of claim amount or collateral value per § 506(a)
- **Unsecured deficiency** — difference if undersecured
- Attach evidence of perfection

### Part 3: Priority Claim

Complete only if claiming priority under § 507(a):

| Priority Category | Statutory Basis |
|---|---|
| Domestic support obligations | § 507(a)(1) |
| Wages/salaries (180-day window, statutory cap) | § 507(a)(4) |
| Employee benefit plan contributions | § 507(a)(5) |
| Tax claims | § 507(a)(8) |

State the amount entitled to priority.

### Part 4: Supporting Documentation

Attach per FRBP 3001(c):

| Claim Type | Required Attachment |
|---|---|
| Based on a writing | The writing itself (contract, note, invoice) |
| Secured | Evidence of perfection (recorded mortgage, UCC filing) |
| Open-end / revolving credit | Account statement |
| Filed by assignee | Documentation of full assignment chain |

### Signature and Declaration

- Penalty-of-perjury declaration
- Authorized representative name and capacity
- Filing agent information (if applicable)

## Claim Calculation

All amounts calculated as of the petition date:

| Component | Amount | Basis |
|---|---|---|
| Principal | $ | Contract/invoice amount |
| Pre-petition interest | $ | Rate × period (cite contractual or statutory rate) |
| Late fees/charges | $ | Per contract terms |
| Attorney's fees | $ | If contractually authorized |
| **Total claim** | **$** | **Sum as of petition date** |

Post-petition amounts are noted separately — not included in the filed claim amount but may be recoverable for oversecured creditors under § 506(b).

## Guidelines

- **Bar date is jurisdictional** — a missed bar date typically results in claim disallowance
- **File even if disputed** — protect the creditor's position; amount can be resolved later
- **Petition date controls** — calculate all amounts as of that date, not the filing date
- **Secured claim bifurcation** — § 506(a) splits into secured (up to collateral value) and unsecured deficiency
- **Documentation is mandatory** — courts can reduce or disallow undocumented claims
- **Agent filings** — include power of attorney or written authorization
- **Amended claims** — permitted before distribution, but monitor all deadlines
- **Local rules** — check CM/ECF requirements for the specific court

## Troubleshooting

| Issue | Resolution |
|---|---|
| Bar date has passed | Check if cause exists for late filing (excusable neglect under FRBP 9006(b)(1)); file motion for leave immediately |
| Missing supporting documents | File claim with available documentation and supplement before objection deadline; note incomplete attachments |
| Uncertain claim amount | File with best estimate and mark as "estimated" on Form B 410; amend when exact figure is available |
| Secured claim without perfection evidence | File as general unsecured unless perfection can be documented; obtain and attach evidence before objection hearing |
| Claim objection received | Review objection basis, gather responsive evidence, and file response within the court's deadline |

---
