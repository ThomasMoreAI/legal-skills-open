---
name: oh-discovery-codearranger
title: Ohio Discovery
description: Use for Ohio discovery practice — interrogatories, RFPs, RFAs, depositions, meet-and-confer, motions to compel. Triggers include 'Ohio Civ. R. 33 interrogatories', 'Ohio Civ. R. 34 production', 'Ohio Civ. R. 36 admissions', 'Ohio Civ. R. 30 deposition', 'Ohio motion to compel Civ. R. 37', 'Ohio meet and confer'. Covers the Ohio Civ. R. discovery framework (closely tracks FRCP), the 40-interrogatory presumptive cap, the chain-of-title-targeted RFPs for consumer-debt defense, deposition mechanics under Civ. R. 30, and Civ. R. 37 motion-to-compel practice.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Ohio Discovery

> **NOT LEGAL ADVICE.** Discovery deadlines are tracked in
> each court's case-management order. Verify per-court Loc.
> R. before relying on Civ. R. baseline timing.

## Scope of discovery (Civ. R. 26)

Ohio Civ. R. 26(B)(1) allows discovery into any matter
"not privileged, which is relevant to the subject matter
involved in the pending action." Closely parallels FRCP
26(b)(1), though Ohio has **not** adopted the federal
"proportionality" amendment.

## Discovery devices

### Interrogatories — Civ. R. 33

- **40-question presumptive cap** under Civ. R. 33(A)(1)
  (counted across subparts; the cap is per side, not per
  responding party)
- **28 days to respond** under Civ. R. 33(A)(3)
- Available to any party as of right; no court order
  required

### Requests for Production — Civ. R. 34

- No statewide cap on number of RFPs
- **28 days to respond** under Civ. R. 34(B)
- Document and ESI both within scope

### Requests for Admission — Civ. R. 36

- No statewide cap
- **28 days to respond** under Civ. R. 36(A)
- **Failure to respond = deemed admission** — frequently a
  trap for pro se litigants
- Withdrawn / amended admissions require court order

### Depositions — Civ. R. 30 / 31

- **No state-wide limit** on number of depositions per side
  (unlike FRCP 30's 10-deposition cap)
- Notice + subpoena duces tecum for non-party records
- Civ. R. 30(D) procedure: 30-day notice; objections
  noted on the record

## Meet-and-confer

Ohio does NOT have a statewide good-faith conferral rule
analogous to NY's 22 NYCRR § 202.20-f or FRCP 37(a)(1).
However, **most Common Pleas local rules require
meet-and-confer before a motion to compel** — verify Loc.
R. of the assigned court.

Common Pleas courts that explicitly require meet-and-confer
include Cuyahoga (Loc. R. 21.4), Franklin (Loc. R. 21),
Hamilton (Loc. R. 18). Most others require it implicitly via
case-management orders.

Best practice for pro-se filers: document the conferral
attempt in writing (email or letter) and append to the
motion to compel.

## Motion to compel — Civ. R. 37

- Civ. R. 37(A) — motion to compel a response
- Civ. R. 37(B) — sanctions for failure to comply
- Civ. R. 37(D) — sanctions for failure to appear at
  deposition
- **Attorney's fees recoverable** to the prevailing movant
  under Civ. R. 37(A)(4) absent substantial justification
  for the discovery violation

## Chain-of-title-targeted RFPs (consumer-debt)

For consumer-debt defense — see `oh-consumer-debt` for the
full RFP catalog. Quick reference:

- The original signed account agreement
- Each assignment / bill-of-sale document showing transfer
  from original creditor to plaintiff
- The data file establishing this specific account is in the
  transferred pool
- Account statements showing the alleged balance + payment
  history

## Composition with other oh- skills

- `oh-deadlines` — Civ. R. 6 time computation for the 28-day
  response window
- `oh-first-30-days` — preliminary discovery requests with
  Answer
- `oh-draft-motion` — Civ. R. 37 motion to compel scaffolder
- `oh-consumer-debt` — debt-buyer-specific discovery
