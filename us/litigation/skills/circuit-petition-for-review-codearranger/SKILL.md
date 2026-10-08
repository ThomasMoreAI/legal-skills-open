---
name: circuit-petition-for-review-codearranger
title: Immigration — Circuit Petition for Review (PFR)
description: 'Use this skill to file a petition for review (PFR) of a final removal order in a U.S. Court of Appeals under INA § 242 / 8 U.S.C. § 1252 — judicial review of a removal order (filed with the circuit court, NOT EOIR). Triggers: "petition for review", "court of appeals immigration", "PFR", "INA 242", "30 days to petition for review", "stay of removal", "exhaustion immigration appeal", "judicial review removal order", "federal court immigration appeal". Drafts PFR caption scaffold, filing checklist (venue, exhaustion, certified record), stay-of-removal motion outline. Flags the **30-day deadline is jurisdictional and uncurable** (INA § 242(b)(1)). Composes with bia-appeals, immigration-deadlines, and immigration-fact-check.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-immigration-laws/skills/circuit-petition-for-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Immigration — Circuit Petition for Review (PFR)

> **NOT LEGAL ADVICE.** This skill produces drafting aids, checklists, and document
> scaffolds — **not legal advice**, and no attorney-client relationship is created.
> **The 30-day deadline to file a petition for review is JURISDICTIONAL — it cannot be
> tolled, extended, or excused, and missing it is uncurable.** A petition for review is
> federal appellate litigation on a closed administrative record; **strongly consider
> retaining a licensed attorney experienced in circuit immigration practice** before
> proceeding. Verify every date and citation against current law.

## What a petition for review is — and is not

A petition for review (PFR) is the **sole and exclusive means** of obtaining judicial review
of a **final order of removal** (8 U.S.C. § 1252(a)(5)). It is filed in a **U.S. Court of
Appeals (a circuit court) — not with EOIR, the immigration court, or the BIA.** The "final
order" is almost always the **BIA's decision** dismissing the appeal (or the IJ's order if no
BIA appeal was taken and none is available).

The PFR document itself is **short**: a notice naming the petitioner, identifying the order
under review (with a copy of the order attached — § 1252(c)), and stating the court. The
**merits are argued later**, in an opening brief decided **only on the administrative record**
the agency already made (§ 1252(b)(4)(A)); the court does not take new evidence and reverses
fact findings only if "any reasonable adjudicator would be compelled" to the contrary
(§ 1252(b)(4)(B)).

## Deadline, venue, and exhaustion — the three jurisdictional gates

| Gate | Rule | Authority |
|---|---|---|
| **Deadline** | **File no later than 30 days after the date of the final order of removal** (usually the BIA decision). **Jurisdictional — no tolling, no extension, no good-cause cure.** | § 1252(b)(1) |
| **Venue** | File in the circuit covering the place where **the immigration judge completed the proceedings** — not where the petitioner now lives. | § 1252(b)(2) |
| **Exhaustion** | The court may review **only** if the petitioner **exhausted all administrative remedies available as of right** — i.e., raised the issue to the BIA. Issues not presented to the Board are generally unreviewable. | § 1252(d)(1) |

Compute the 30 days against the date stamped on the final order, count calendar days, and
confirm the circuit with `immigration-deadlines`. A motion to reopen or reconsider at the BIA
**does not** restart this clock; if a PFR and a reopen/reconsider motion are both pending, the
court consolidates them (§ 1252(b)(6)) — see `eoir-motions-to-reopen-reconsider`.

## Scope of review — the § 1252(a)(2) bars and the (a)(2)(D) exception

Congress stripped circuit jurisdiction over two large categories of removal orders:

- **Criminal-offense bar — § 1252(a)(2)(C).** No jurisdiction to review a final removal order
  against a noncitizen removable for certain crimes (offenses under § 1182(a)(2) or
  § 1227(a)(2)(A)(iii), (B), (C), (D), and the stacked-CIMT clause).
- **Discretionary-decision bar — § 1252(a)(2)(B).** No jurisdiction to review judgments
  granting or denying the listed discretionary relief (e.g., cancellation under § 1229b,
  voluntary departure under § 1229c, adjustment under § 1255, certain § 1182 waivers), or
  other decisions specified to be in the agency's discretion.

> **The key exception — § 1252(a)(2)(D).** Nothing in those bars precludes review of
> **constitutional claims or questions of law** raised in a petition for review to an
> appropriate court of appeals. A PFR that falls within a bar generally survives only if it is
> framed as a constitutional claim or a legal question (the application of law to settled
> facts can qualify). Frame the petition's issues accordingly and verify the controlling
> circuit construction via CourtListener (below) — do not rely on remembered case names.

## No automatic stay — you must MOVE for a stay of removal

> **Filing a petition for review does NOT stay removal.** Service of the petition does not stop
> the government from removing the petitioner while the case is pending **unless the court
> orders otherwise** (§ 1252(b)(3)(B)). To avoid removal during the appeal, the petitioner must
> file a **separate motion for a stay of removal** in the court of appeals and satisfy the
> stay standard (the *Nken*-type four-factor test — likelihood of success, irreparable harm,
> balance of equities, public interest). Some circuits operate a temporary administrative-stay
> practice on request; confirm the local rule and the government's forbearance policy. **Treat
> the stay motion as urgent and parallel to the PFR, not as something that happens later.**

## Artifacts this skill drafts

- **PFR caption / notice scaffold** — petitioner name(s) and A-number; respondent (the Attorney
  General / United States); the order under review and its date; the circuit; a statement that
  a copy of the order is attached (§ 1252(c)).
- **Filing checklist** — the 30-day deadline (computed and flagged jurisdictional); correct
  venue (circuit of the IJ's completed proceedings); exhaustion confirmation; copy of the final
  order attached; the certified **administrative record** (CAR) request/expectation; filing fee
  or fee-waiver motion; service on the respondent.
- **Stay-of-removal motion outline** — the four stay factors mapped to the record, an urgency
  banner, and a prompt to seek a temporary administrative stay where the circuit allows.
- **Exhaustion worksheet** — issue-by-issue: was it raised to the BIA? where in the record?
  flagging any issue at risk of being deemed unexhausted under § 1252(d)(1).

## Related authority

- **INA § 242 / 8 U.S.C. § 1252** (judicial review of orders of removal) —
  [`../../references/immigration-statutes/INA-II-immigration.md`](../../references/immigration-statutes/INA-II-immigration.md)
  (§ 1252; the INA ↔ 8 U.S.C. crosswalk is in that corpus's
  [README](../../references/immigration-statutes/README.md)).
- **Circuit immigration case law** (constructions of the (a)(2) bars, the (a)(2)(D) exception,
  exhaustion, and the stay standard) is **on-demand via CourtListener** — see
  [`../../references/legal-data-apis.md`](../../references/legal-data-apis.md) for the MCP
  `search` workflow and the per-circuit `court` ids (`ca1`–`ca11`; the Ninth, `ca9`, carries the
  largest immigration docket). **Do not invent case names** — pull and verify each cite, then
  confirm with `immigration-fact-check`.
- Canonical filing URLs and the PFR framework pointer —
  [`../../references/online-sources.md`](../../references/online-sources.md).

## Composition

- **`bia-appeals`** — establishes the final order that this PFR reviews; the BIA decision is the
  trigger for the 30-day clock.
- **`eoir-motions-to-reopen-reconsider`** — a parallel reopen/reconsider motion does **not**
  toll the PFR deadline; if both are pending the court consolidates (§ 1252(b)(6)).
- **`immigration-deadlines`** — compute and double-check the **jurisdictional 30-day** deadline
  and identify the correct circuit/venue.
- **`immigration-fact-check`** — verify every statutory and case citation in the PFR and the
  stay motion before filing.
