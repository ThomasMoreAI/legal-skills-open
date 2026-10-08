---
name: tn-general-sessions-codearranger
title: Tennessee General Sessions Court
description: 'Use for Tennessee civil cases in General Sessions Court — limited-jurisdiction, high-volume, informal forum (dominant consumer-debt and eviction forum). Covers $25,000 civil monetary cap with unlimited detainer (eviction) jurisdiction; civil-warrant pleading model (informal, not formal Tenn. R. Civ. P. 10 captioned complaint); informal procedure (TRCP do not apply except as specifically made applicable); no formal discovery as of right; 10-day de novo appeal to Circuit Court (§ 27-5-108) where full formal procedure applies. For General Sessions appearance: no written answer needed; testimony at hearing suffices. Debt-buyer documentation requirement (§ 20-6-104) applies to defaults. Layer on top of `tn-statewide-format`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-general-sessions
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Tennessee General Sessions Court

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. General
> Sessions deadlines are short and unforgiving — verify every date and
> every local-rule requirement against the current statute and the
> court's own rules before acting.

Use this skill in addition to `tn-statewide-format` whenever a civil
case is in a **General Sessions Court**. General Sessions is the
limited-jurisdiction trial court that exists in every Tennessee
county. It is the **dominant consumer-debt and eviction forum** —
high volume, informal procedure, and very short appeal windows.

## Jurisdiction and monetary cap

- **Civil monetary cap: $25,000** (T.C.A. § 16-15-501). Claims above
  the cap belong in Circuit or Chancery Court. Verify the current
  figure before relying on it.
- **Attorney's fees and costs are generally excluded** from the cap
  computation — verify against the current statute.
- **EXCEPTION — unlimited jurisdiction in forcible entry and detainer
  (eviction).** General Sessions hears **detainer warrants** without
  regard to the monetary cap (the value of the property/possession is
  not capped). See `tn-landlord-tenant`.

## Informal procedure — the Rules of Civil Procedure generally do NOT apply

General Sessions practice is **informal**. The **Tennessee Rules of
Civil Procedure do not apply** in General Sessions **except as they
are specifically made applicable** by statute or rule. Practical
consequences:

- **Suit is commenced by a "civil warrant"** — a short summons-style
  form that names the parties, states the nature and amount of the
  claim in summary terms, and sets a return/appearance date — **not**
  a formal Rule 10 captioned complaint with numbered paragraphs. The
  civil-warrant form supplies the caption fields.
- **No formal discovery as of right.** There is no entitlement to
  Rule 33 interrogatories, Rule 34 requests for production, Rule 36
  requests for admission, or depositions in General Sessions; any
  discovery is at the court's discretion or by agreement. Build the
  defense around documents the defendant already holds and around
  what the plaintiff must prove at the appearance.
- **Pleadings are minimal.** A defendant ordinarily need not file a
  written answer; appearing on the return date and contesting the
  claim is the norm. Confirm the local practice — some courts request
  a brief written response and some require a written answer for
  certain case types.

Because the procedure is informal, the formal-pleading machinery in
`tn-statewide-format` (Rule 10 numbered paragraphs, Rule 56 summary
judgment) applies fully only **after** a de novo appeal lands the case
in Circuit Court (below). Use `tn-statewide-format` for any written
filing the General Sessions clerk does accept (e.g., a written motion
or a notice), and for the caption/format conventions.

## Consumer-debt and debt-buyer practice

General Sessions is where most consumer-debt collection suits are
filed. Two Tennessee features matter at the appearance:

- **Sworn-account device — T.C.A. § 24-5-107.** A plaintiff suing on
  an account may file a sworn affidavit of the account; this is an
  evidentiary/procedural device that can shift the burden to the
  defendant to **deny the account under oath**. It is **not** a
  separate statute of limitations. If the defendant fails to deny
  under oath, the sworn account may be taken as proved — so respond
  on the record.
- **Debt-buyer documentation before default — T.C.A. § 20-6-104**
  (added 2024). Before entering a **default judgment** for a
  **"subsequent creditor" / debt-buyer** plaintiff, the court must be
  presented with documentation sufficient to show (1) the plaintiff's
  **authority to collect the debt** and (2) **at least one document
  showing the debt's existence**, irrespective of any affidavit. This
  does **not** apply to original creditors/lienholders. Verify the
  current text and any threshold before relying on it.

See `tn-consumer-debt` for the full debt-defense framework (FDCPA,
the Tennessee Collection Service Act at T.C.A. Title 62 ch. 20,
statutes of limitation, and chain-of-title challenges).

## Eviction (detainer warrants)

Forcible entry and detainer (FED) actions are filed in General
Sessions under **T.C.A. § 29-18-101 et seq.** as a **detainer
warrant**. Possession remedies are governed by the FED statute,
including the possession-bond provisions at **§ 29-18-130(b)**. See
`tn-landlord-tenant` for notice requirements (including the 14-day
nonpayment notice under the URLTA at T.C.A. § 66-28-505 in
URLTA-covered counties) and the detainer-warrant defense framework.

## De novo appeal to Circuit Court — 10 days, jurisdictional

A General Sessions civil judgment is appealed to **Circuit Court for a
trial de novo**:

- **Deadline: 10 days from entry of the General Sessions judgment**
  (T.C.A. § 27-5-108). This 10-day period is uniform statewide and is
  **jurisdictional** — missing it forfeits the appeal. Verify the
  current statute and how the court computes the 10 days (and whether
  Tenn. R. Civ. P. 6 time-computation applies to the appeal step).
- The appeal produces a **trial de novo** — the case is tried anew in
  Circuit Court under the **full** Tennessee Rules of Civil
  Procedure. The General Sessions record/result does not bind the
  Circuit Court.
- **Detainer (eviction) appeals** follow the same 10-day de novo route
  under § 27-5-108; the possession-bond provisions of
  § 29-18-130(b) interact with the appeal — and Tennessee case law has
  held that a tenant's appeal is not automatically dismissed solely
  for failure to post the possessory bond. Verify current authority.

Once in Circuit Court on de novo appeal, switch to
`tn-statewide-format` and `tn-first-30-days` for formal pleading and
motion practice; the informal General Sessions regime no longer
applies.

## Caption / civil-warrant form

For documents the General Sessions clerk accepts, use the court
identifier line:

```
   IN THE GENERAL SESSIONS COURT FOR [COUNTY] COUNTY, TENNESSEE
```

But remember the **case is commenced by the clerk-issued civil
warrant**, not a captioned complaint; the warrant supplies the docket
number and the parties. For a written motion or notice filed in the
case, follow the caption conventions in `tn-statewide-format`.

## Composition

- For statewide format: `tn-statewide-format`
- For consumer-debt defense: `tn-consumer-debt`
- For eviction / detainer defense: `tn-landlord-tenant`
- For the post-appeal Circuit Court pleading: `tn-first-30-days`
- For deadline computation: `tn-deadlines`
- For pro se conventions: `tn-pro-se`
- For the controlling county's local practice: `tn-davidson`,
  `tn-shelby`, `tn-knox`, `tn-hamilton`, `tn-county-courts`

## References

- `tn-law-references` — T.C.A. (incl. § 16-15-501, § 27-5-108,
  § 29-18-101 et seq., § 24-5-107, § 20-6-104), Tenn. R. Civ. P.,
  Tenn. R. Evid., and local-rules corpus
