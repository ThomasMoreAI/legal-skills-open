---
name: written-consent-in-lieu-of-meeting
title: Written Consent in Lieu of Meeting
description: Drafts U.S. corporate written-consent instruments (board, shareholder, member) as substitutes for formal meetings. Triggers when counsel requests board consent, shareholder written consent, unanimous consent, consent-in-lieu approvals, or "action without meeting" for contracts, financing, equity issuance, officer delegation, or governing-document amendments. Produces jurisdiction-aware approval records with threshold validation and execution mechanics.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/written-consent-in-lieu-of-meeting
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting]
---

# Written Consent in Lieu of Meeting

Drafts a written-consent instrument authorizing entity action without a meeting, preserving corporate-record integrity and enforceability.

## Quick Start

1. Collect entity type, legal name, and jurisdiction of formation.
2. Obtain governing documents (charter, bylaws, operating agreement) — especially consent-specific provisions.
3. Identify the action, approval class (board vs. shareholder/member), and required threshold.
4. Draft consent with proper recitals, resolutions, and signature blocks.
5. Validate threshold math and statutory alignment before output.

**Hard stop:** If jurisdiction or entity type is missing, request before drafting.

## Intake Checklist

| Field | Source |
|---|---|
| Entity legal name | Charter / certificate of formation |
| Jurisdiction | Formation docs |
| Governing authority | Bylaws / operating agreement |
| Action type | User request + transaction docs |
| Required threshold | Governing docs + statute |
| Signatory list + interests | Board list, cap table, membership ledger |
| Effective date rule | Governing docs + statute `[VERIFY]` |
| Filing destination | Secretary / record-retention policy |

## Workflow

### 1. Legal Framework Check

- Classify as board or shareholder/member consent.
- Confirm written-consent authorization statute:
  - DE corp board: DGCL §141(f) `[VERIFY]`
  - DE stockholder: DGCL §228 `[VERIFY]`
  - LLC: state LLC statute equivalent `[VERIFY]`
- Check governing-doc overrides: notice windows, class protections, unanimity, special-purpose approvals.
- Confirm the action is not statutorily excluded from written consent in the jurisdiction.

### 2. Draft Structure

```
WRITTEN CONSENT OF THE [BOARD OF DIRECTORS / SHAREHOLDERS]
OF [ENTITY NAME] IN LIEU OF [SPECIAL/ANNUAL] MEETING

[Effective Date]

The undersigned [directors/shareholders/members] of [ENTITY], pursuant to
[GOVERNING STATUTE] and [GOVERNING DOCUMENT], hereby consent to the
following resolutions:

WHEREAS [fact and authority recitals];
WHEREAS [threshold and compliance recitals];

RESOLVED, THAT [resolution with complete action language].
```

### 3. Resolution Content by Action Type

| Action | Required elements |
|---|---|
| Contract authorization | Agreement title/date, key terms, parties, permitted modifications, authority granted |
| Financing | Max principal, rate/maturity/conditions, collateral, lender, covenant linkage |
| Equity issuance | Security type/class/number, recipient, price/valuation, restrictions, ROFR/preemptive compliance |
| Asset disposition | Target asset, consideration, authority conditions, delegated approval, filing steps |
| Officer delegation | Officer identity, authority scope, caps, signature limits, duration |
| Governing-doc amendment | Exact section text or exhibit, vote threshold, procedural prerequisites, filing |

### 4. Signature and Recordkeeping

- Signature block per required signatory: signature, printed name, title, date.
- Shareholder/member lines must state class, shares/membership %, and percentage of outstanding.
- Include consent execution statement confirming threshold met.
- Optional secretary certificate: filed date, record location, effectiveness status.

### 5. Quality Gate

1. **Authority** — statute + governing docs align with consent mechanism used.
2. **Threshold math** — interest percentages exactly satisfy required vote.
3. **Consistency** — recitals match resolutions on facts, parties, and scope.
4. **Completeness** — output missing-items list if any material fact is unknown; never finalize silently.

## Pitfalls

- Never assume e-signature validity — confirm governing docs and jurisdiction permit it.
- Do not over-broaden delegation authority; no open-ended grants.
- Preserve minority-rights protections and class-vote mechanics from governing documents.
- Keep recital and resolution scope tightly limited to the approved action.
- Include conditions precedent and third-party approvals in resolutions, not commentary.
- Mark any unconfirmed statutory citation with `[VERIFY]`.
