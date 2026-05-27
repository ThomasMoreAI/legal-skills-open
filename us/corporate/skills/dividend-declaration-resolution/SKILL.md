---
name: dividend-declaration-resolution
title: Dividend Declaration Resolution
description: Drafts a board of directors resolution authorizing a cash, stock, or property dividend to shareholders. Enforces solvency testing (equity and balance sheet), WHEREAS/RESOLVED clause structure, critical date triad (declaration/record/payment), officer authorization, and Secretary certification under Delaware DGCL §170 or equivalent state statute. Use when documenting board approval of a dividend distribution or when corporate governance records require a formal profit-distribution authorization.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/dividend-declaration-resolution
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [drafting]
---

# Dividend Declaration Resolution

Drafts a board-adopted resolution authorizing a dividend distribution, functioning as a binding corporate record and evidentiary foundation for fiduciary compliance.

## Quick Start

Collect these inputs before drafting:

1. **Articles of incorporation** — legal name, authorized stock classes, preferred dividend preferences, cumulation rights
2. **Bylaws** — quorum requirements, notice provisions, officer authority
3. **Financial statements** — balance sheet and income statement within 90 days; retained earnings balance
4. **Loan agreements** — dividend restrictions, maintenance covenants, lender consent requirements
5. **Prior resolutions** (if any) — format consistency, accumulated preferred dividends paid
6. **Dividend parameters** — type (cash/stock/property), amount per share, proposed record date, proposed payment date

## Output Structure

### 1. Header Block

- Corporation legal name, document title ("Resolution of the Board of Directors Authorizing Declaration of [Type] Dividend")
- Meeting type (regular/special), date, location/remote platform, time

### 2. Meeting Mechanics

| Item | Required Content |
|---|---|
| Notice | Proper notice per bylaw § ___ confirmed; waiver if applicable |
| Quorum | Quorum present per bylaw § ___ and [State] Corp. Law § ___ |
| Directors present | Full names |
| Directors absent | Names; whether excused |
| Presiding officer | Name and title |

### 3. WHEREAS Recitals

Draft numbered recitals in this order:

| # | Recital | Key Content |
|---|---------|-------------|
| 1 | Financial review | Board reviewed financials as of [date]; retained earnings of $[X] |
| 2 | Statutory authority | Dividend pursuant to [Del. DGCL §170 / [State] [Cite]] [VERIFY for non-DE] |
| 3 | Equity solvency | Corporation able to pay debts as they become due |
| 4 | Balance sheet solvency | Assets exceed liabilities after giving effect to dividend |
| 5 | Business judgment | Dividend in best interests considering capital needs and prospects |
| 6 | Preferred satisfaction | Accumulated preferred dividends paid/current [omit if no preferred] |
| 7 | Third-party compliance | Loan covenants satisfied / lender consent obtained [omit if N/A] |

### 4. RESOLVED Clauses

| # | Resolution | Key Language |
|---|-----------|-------------|
| 1 | **Dividend Declaration** | Declare [cash] dividend of $[X.XX] per share on [Class] stock, par value $[X.XX], totaling ~$[aggregate] based on [X,XXX,XXX] shares outstanding |
| 2 | **Critical Dates** | Declaration Date: date of meeting; Record Date: 10–30 days post-declaration; Payment Date: 2–4 weeks post-record |
| 3 | **Eligible Shares** | Payable to holders of record of [Class] shares at Record Date; treasury shares and forfeiture shares excluded |
| 4 | **Officer Authorization** | CEO, CFO, Secretary authorized to: (a) instruct transfer agent; (b) make accounting entries; (c) file regulatory notifications; (d) execute implementing documents. Ministerial changes permitted if non-material |

### 5. Vote Record

- Count and names: in favor, against, abstaining (with conflict disclosures)
- Resolution declared ADOPTED or FAILED
- Document conflict-of-interest disclosures and recusals by name

### 6. Secretary Certification and Signature Block

- Secretary certifies resolution duly adopted at properly noticed meeting with quorum present throughout
- Signature lines: Corporate Secretary (name, date), Chairperson of the Board (name, date)
- Corporate seal placement

## Guidelines

- **Both solvency tests are mandatory** — omitting either equity or balance sheet test creates fiduciary exposure
- **Delaware §170** [VERIFY] — applies to DE-incorporated entities; confirm equivalent statute for other jurisdictions before citing
- **Preferred stock priority** — verify cumulative vs. non-cumulative in articles; accumulated arrears must clear before common dividend if cumulative
- **Lender covenants** — check all credit agreements for dividend blockers and basket limitations before finalizing
- **Record date window** — Delaware requires record date no more than 60 days before payment [VERIFY]; NYSE/Nasdaq listed companies have additional exchange notice requirements
- **Treasury shares** — exclude from eligibility and aggregate calculation
- **Stock dividends** — may require shareholder approval if altering capital structure; confirm under governing state law and articles
- **Retention** — file executed resolution in corporate minute book per applicable state record-keeping statute

## Troubleshooting

- **Missing solvency recital** — if either equity or balance sheet solvency language is absent, the resolution is incomplete; add the missing recital before finalization
- **Non-Delaware jurisdiction** — do not default to DGCL citations; insert `[VERIFY: STATE STATUTE]` and confirm the governing state's dividend authority provision
- **Preferred stock arrears unknown** — if cumulation status or arrears balance is unavailable, flag with `[VERIFY: PREFERRED DIVIDEND STATUS]` rather than omitting the recital
- **Covenant conflict** — if loan agreement review is incomplete, insert `[VERIFY: LENDER CONSENT REQUIRED]` in the third-party compliance recital
- **Record date exceeds statutory window** — if proposed record date is more than 60 days before payment, adjust dates or confirm state law permits the gap
