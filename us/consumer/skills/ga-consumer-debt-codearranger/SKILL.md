---
name: ga-consumer-debt-codearranger
title: Georgia Consumer-Debt Defense
description: 'Use this skill for Georgia consumer-debt defense — debt-buyer suits, original-creditor collection cases, and any matter turning on FDCPA, Regulation F, FCRA, TILA, the Georgia Fair Business Practices Act (FBPA), chain-of-title / standing, or the business-records foundation a debt buyer needs to win. Triggers: "Midland Credit sued me in Georgia", "Georgia debt buyer lawsuit", "Portfolio Recovery sued me Georgia", "LVNV Funding Georgia", "I was sued on a credit card in Georgia", "answer a State Court debt complaint", "Magistrate Court debt lawsuit Georgia", "FBPA", "credit card statute of limitations Georgia", "time-barred debt Georgia", "chain of title Georgia debt", "set aside default judgment debt Georgia", "FDCPA counterclaim Georgia". Subject- matter bundle covering FDCPA / Reg F / FBPA substantive law, chain-of-title and standing doctrine, the debt-buyer business- records battleground, affirmative defenses, discovery banks, and counterclaims for Georgia debt-defense litigation.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-consumer-debt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: consumer
language: en
---

# Georgia Consumer-Debt Defense

This skill is the **subject-matter bundle** for Georgia
consumer-debt litigation: debt-buyer cases, original-creditor
collection actions, and any matter turning on FDCPA / Reg F /
FCRA / TILA and the Georgia Fair Business Practices Act (FBPA).

It assumes the procedural framework is already in place via the
matter-neutral skills. This skill adds the substantive law,
the standing and evidence doctrine, a fact-pattern triage, an
affirmative-defenses catalog, discovery banks, and the
counterclaim package.

> **NOT LEGAL ADVICE.** This subject-matter bundle describes
> a procedural and substantive framework for Georgia cases in
> this area, not legal advice and not strategic advice for
> any specific case. Outcomes are fact-specific; the choice
> of defenses, claims, motions, and discovery belongs to the
> litigant (and any counsel the litigant retains). Verify
> every rule, deadline, and citation against current law
> before filing.

## The Georgia consumer-debt landscape

Georgia's framework is **federal-first**. Unlike many states,
Georgia has **no mini-FDCPA** and the Georgia Department of
Banking and Finance does **not** license or regulate third-party
debt collectors or debt buyers. There is therefore **no
"unlicensed-collector" defense** of the kind that exists in
licensing states. The practical consequence is that the
**federal statutes are the primary tools**, and the Georgia Fair
Business Practices Act is the state-law overlay.

### Federal layer — the primary tools

- **FDCPA** (Fair Debt Collection Practices Act), 15 U.S.C.
  § 1692 et seq. — applies to **debt collectors** (including
  most debt buyers) collecting **consumer** debt; does not, as
  a general matter, reach original creditors collecting their
  own debt (15 U.S.C. § 1692a(6)).
- **Regulation F** (12 C.F.R. pt. 1006), effective November 30,
  2021 — the CFPB's FDCPA-implementing regulation; codifies the
  call-frequency safe harbor, the model validation notice, and
  the time-barred-debt litigation prohibition.
- **FCRA** (Fair Credit Reporting Act), 15 U.S.C. § 1681 et seq.
  — furnisher and credit-reporting obligations; identity-theft
  blocks.
- **TILA** (Truth in Lending Act), 15 U.S.C. § 1601 et seq. —
  disclosure obligations on the underlying credit account.

### Georgia state layer

- **Georgia Fair Business Practices Act (FBPA)**, O.C.G.A.
  § 10-1-390 et seq. — the state-law vehicle for collection
  misconduct, since Georgia has no mini-FDCPA. See the dedicated
  section below.
- **Installment Loan Act** (the Georgia Industrial Loan Act),
  O.C.G.A. Title 7, Ch. 3 (§ 7-3-1 et seq.) — the **only**
  licensing regime relevant here, and it reaches only **small-
  loan lenders** making consumer loans at or below a statutory
  threshold (currently **$3,000** — verify the exact figure
  against current law, as the cap is amended from time to time),
  **not** third-party collectors or debt buyers. A loan made by
  an unlicensed lender subject to the Act is **void**, with
  forfeiture of principal, interest, and charges under O.C.G.A.
  § 7-3-29. This matters only where the original obligation is a
  small-dollar installment loan from a lender that should have
  been licensed — it is not a general debt-buyer defense.

> **No collector licensing in Georgia.** Do not draft a defense
> or counterclaim premised on the debt buyer or collection
> agency being "unlicensed." Georgia does not license them.
> Run the case on the FDCPA, Reg F, the FBPA, standing/chain of
> title, the statute of limitations, and the business-records
> foundation instead.

## The FBPA — Georgia's state-law overlay

The **Fair Business Practices Act**, O.C.G.A. § 10-1-390 et seq.
(Title 10, Ch. 1, Art. 15, Part 2), prohibits unfair and
deceptive acts and practices in consumer transactions. Because
Georgia has no mini-FDCPA, the FBPA is the principal **state**
vehicle for FDCPA-type collection misconduct.

- **Purpose** — O.C.G.A. § 10-1-391.
- **Prohibition** — O.C.G.A. § 10-1-393(a): "unfair or deceptive
  acts or practices in the conduct of consumer transactions and
  consumer acts or practices in trade or commerce." FDCPA-type
  abuses (false representations about the amount or legal status
  of a debt, threats, deceptive dunning) can violate this
  section.
- **Consumer-marketplace limit** — the FBPA reaches conduct in
  the **consumer marketplace**; private, isolated, non-merchant
  transactions fall outside the Act. The collection of a
  consumer credit-card or consumer-loan debt is squarely within
  the marketplace the Act protects.

### The mandatory 30-day pre-suit written demand — flag this quirk

> **FBPA QUIRK — the § 10-1-399(b) demand is a statutory
> prerequisite.** Before filing an FBPA claim, the claimant must
> serve a **written demand for relief** on the prospective
> respondent **at least 30 days before** filing suit, identifying
> the claimant, reasonably describing the unfair/deceptive act,
> and the injury suffered (O.C.G.A. § 10-1-399(b)). Plan for this
> when raising the FBPA as a counterclaim — see the counterclaim
> section. Two further points: (1) the 30-day demand does **not
> toll** the FBPA limitations period (O.C.G.A. § 10-1-401), so
> the demand and the 2-year clock must be tracked separately; and
> (2) the demand requirement does not apply where the respondent
> has no place of business or assets in Georgia. A respondent's
> good-faith settlement tender in response to the demand can cap
> the recovery, so document the demand and any response carefully.

### FBPA remedies

- **Actual damages** — O.C.G.A. § 10-1-399(a).
- **Treble damages** — O.C.G.A. § 10-1-399(c): available for an
  **intentional** violation.
- **Attorney's fees and expenses of litigation** — O.C.G.A.
  § 10-1-399(d).
- **Injunctive relief** — O.C.G.A. § 10-1-399(a).
- **Statute of limitations** — O.C.G.A. § 10-1-401: **2 years**.

See `references/ga-fbpa.md` for the annotated statute and
`references/ga-installment-loan-act.md` for the small-loan regime.

## Fact-pattern triage

Most Georgia consumer-debt cases fall into one of these patterns.
The defense strategy varies by pattern. Deeper analysis lives in
the references.

### Pattern 1 — Stale credit-card debt by an out-of-state debt buyer

A debt buyer (e.g., Midland Credit Management, Portfolio Recovery
Associates, Cavalry SPV, LVNV Funding) sues a Georgia consumer —
typically in **State Court** or, for smaller amounts, **Magistrate
Court** — on a charged-off credit-card account where the last
payment was years ago.

- **SOL** — credit-card debt is governed by the **6-year
  written-contract** limitation, O.C.G.A. § 9-3-24 (see the
  counterintuitive-SOL section below). Verify the date of last
  payment / default; the clock runs from there.
- **Standing / chain of title** — the debt was originated by the
  bank, sold (often through several buyers), and the plaintiff is
  the assignee. Each transfer must be proven. Demand the bill of
  sale, assignment, and **account-level data** tying the
  plaintiff to *this* account (see *Nyankojo*, below).
- **No licensing defense** — do not plead unlicensed collection;
  Georgia does not license debt buyers.

### Pattern 2 — Debt buyer suing on the original creditor's agreement

Same as Pattern 1, but the plaintiff attaches the **original
creditor's cardmember agreement** to the complaint to establish a
written contract (and thus the 6-year SOL).

- **Standing** — the cardmember agreement is the *original
  creditor's* contract. Attaching it does not, by itself, prove
  the plaintiff **owns** this account. The plaintiff still must
  prove an unbroken assignment chain.
- **Evidence** — the original creditor's records are the
  plaintiff's, only by way of a hearsay exception; the plaintiff's
  own custodian generally cannot lay the foundation for records it
  did not create (see the evidence section).

### Pattern 3 — Collection lawsuit on a medical debt

A collection agency or buyer sues on a medical bill.

- **Itemization / billing accuracy** — medical bills frequently
  contain errors; demand an itemized statement and challenge the
  amount.
- **Credit-reporting limits** — under Reg V / NCAP rules, much
  medical debt is restricted from appearing on consumer credit
  reports; FCRA furnisher accuracy obligations apply.
- **Foundation** — the same business-records and chain-of-title
  problems apply; medical providers' records used by a buyer are
  third-party records requiring proper foundation.

### Pattern 4 — Default judgment already entered

The consumer was sued, often never properly served, and a default
judgment was entered — frequently discovered only when a
garnishment lands.

- **Open default as of right** — O.C.G.A. § 9-11-55(a): a default
  may be opened **as a matter of right within 15 days** of the
  default on payment of costs.
- **After 15 days** — O.C.G.A. § 9-11-55(b): the default may be
  opened only on a showing of **providential cause, excusable
  neglect, or a proper case**, plus the four statutory
  conditions (motion under oath, a meritorious defense, an offer
  to plead instanter, and announcing ready to proceed). The
  "proper case" prong does not require a reasonable explanation
  for the default — *Bowen v. Savoy*, 308 Ga. 204, 839 S.E.2d 546
  (2020) (verify pincite).
- **Meritorious defense** — the chain-of-title, SOL, and
  foundation defenses below supply the meritorious-defense
  showing.
- Coordinate with `ga-post-judgment` for the set-aside motion and
  any garnishment traverse.

### Pattern 5 — FDCPA / FBPA counterclaim

The consumer was sued and the collector's conduct (false
representations about the amount or legal status of the debt,
suing on time-barred debt, harassment, validation failures)
supports affirmative claims.

- **FDCPA counterclaim** — 1-year SOL from the violation
  (15 U.S.C. § 1692k(d)); statutory damages up to $1,000 plus
  actual damages and mandatory fees.
- **FBPA counterclaim** — 2-year SOL (O.C.G.A. § 10-1-401), but
  **serve the § 10-1-399(b) 30-day written demand first**; treble
  damages for intentional violations and attorney's fees on top
  of actual damages.

## Statute of limitations — the counterintuitive part

> **Credit-card debt in Georgia is a 6-year, written-contract
> matter — not a 4-year open account.** This surprises many pro
> se litigants. Because using the card constitutes acceptance of
> the written cardmember agreement, a credit-card claim is a
> **written contract** governed by the **6-year** limitation of
> **O.C.G.A. § 9-3-24** — *Hill v. American Express*, 289 Ga.
> App. 576, 657 S.E.2d 547 (2008), and *Phoenix Recovery Group
> v. Mehta* (Ga. App. 2008). (Secondary sources conflate the
> reporter pincites; verify against the official report.)

| Claim | SOL | Authority |
|---|---|---|
| Written / simple contract (incl. credit card) | 6 years | O.C.G.A. § 9-3-24 |
| Open account / oral / implied contract | 4 years | O.C.G.A. § 9-3-25 |
| Catch-all contract | 4 years | O.C.G.A. § 9-3-26 |
| FDCPA claim | 1 year (from violation) | 15 U.S.C. § 1692k(d) |
| FBPA claim | 2 years | O.C.G.A. § 10-1-401 |

**The 4-year escape hatch is also a proof defect.** The 4-year
open-account limitation (O.C.G.A. § 9-3-25) applies only where
the plaintiff **cannot produce the written cardmember
agreement** and is therefore left pleading an open account or
account stated. When that happens, the same evidentiary gap that
shortens the SOL to 4 years is **also a foundation/proof defect**
— the plaintiff has no written contract to anchor the claim or to
prove its terms. Press both points together.

**Revival.** A new promise must be **in writing** to revive a
barred debt (O.C.G.A. § 9-3-110); a **part payment** entered on
written evidence of the debt operates as a new promise from which
the period runs anew (O.C.G.A. § 9-3-112). Debt buyers sometimes
solicit a small payment to restart the clock — scrutinize whether
any payment was unambiguously referable to *this* debt and
whether the writing requirements are met.

See `references/ga-statutes-of-limitations.md` for the full
analysis.

## Standing and chain of title

A Georgia debt-buyer plaintiff must prove an **unbroken chain of
assignment** from the original creditor to itself. This is the
single most productive defense in a debt-buyer case.

- ***Nyankojo v. North Star Capital Acquisition***, 298 Ga. App.
  6, 679 S.E.2d 57 (2009) — the go-to authority. The Court of
  Appeals reversed summary judgment because the plaintiff failed
  to prove the **unbroken chain of assignment** of the account to
  itself.
- ***Wirth v. CACH, LLC***, 300 Ga. App. 488, 685 S.E.2d 433
  (2009) — account-stated / business-records foundation in the
  debt-buyer setting.
- ***Rutledge v. Gemini Capital Group, LLC***, 327 Ga. App. 454,
  757 S.E.2d 893 (2014) — same battleground; proof of ownership
  and foundation.

What the plaintiff must actually produce for each link:

- **Bill of sale** — the document evidencing each transfer.
- **Assignment** — specifically identifying the accounts
  transferred.
- **Account-level data** — records tying *this consumer's*
  account (by account number and balance) to the bulk transfer.

A bill of sale that references "an attached schedule" without the
schedule, or that recites "all accounts sold on [date]" without
account-level data tying it to the defendant, does not prove
ownership of the specific account.

See `references/chain-of-title.md` for the doctrine and
`references/key-cases.md` for full holdings.

## Evidence — the debt-buyer business-records battleground

Georgia's Evidence Code (Title 24, modeled on the Federal Rules
of Evidence, effective January 1, 2013) makes the **business-
records foundation** the decisive evidentiary fight.

- **O.C.G.A. § 24-8-803(6)** — the business-records hearsay
  exception. The record must be (A) made at or near the time,
  (B) by or from a person with personal knowledge **and a
  business duty** to report, (C) kept in the course of a
  regularly conducted activity, and (D) made as a regular
  practice — shown through a custodian or other qualified witness
  **or** by certification under § 24-9-902(11)/(12); the court
  may exclude where the source or circumstances indicate a **lack
  of trustworthiness**.
- **O.C.G.A. § 24-9-902(11)** — self-authentication of certified
  domestic records of a regularly conducted activity (custodian
  certification, with written notice to adverse parties and an
  opportunity to inspect). § 24-9-902(12) covers foreign records
  under penalty of perjury.

The recurring debt-buyer problem: the plaintiff's custodian
attests to the **buyer's** records but tries to sweep in the
**original creditor's** records ("incorporated" or third-party
records). The contested issues are whether the original creditor's
records were made by someone with a **business duty to report**,
whether the buyer can speak to their trustworthiness at all, and
whether a conclusory custodian affidavit satisfies § 24-8-803(6).
Federal FRE 803(6) / 902(11) case law is persuasive on these
points.

See `references/evidence-debt-buyer.md` for objection language.

## Affirmative defenses — Georgia debt-buyer answer

In the answer, plead all that apply (coordinate with
`ga-first-30-days`):

1. **Failure to state a claim** — O.C.G.A. § 9-11-12(b)(6)
   (pleading inadequate to allege ownership or account terms).
2. **Statute of limitations** — O.C.G.A. § 9-3-24 / § 9-3-25
   (raise the 4-year open-account bar in the alternative when no
   written agreement is produced).
3. **Lack of standing** — plaintiff cannot prove ownership of
   this specific account (chain of title).
4. **Account stated** — no agreed accounting between *this*
   plaintiff and the defendant.
5. **Lack of privity** — no contract between plaintiff and
   defendant.
6. **Payment / accord and satisfaction.**
7. **Identity theft** (if applicable) — coordinate FCRA blocks.
8. **Discharge in bankruptcy** (if applicable).

See `references/affirmative-defenses.md` for the annotated
catalog.

## Discovery strategy

Georgia **allows written interrogatories** — capped at **50,
including subparts** (O.C.G.A. § 9-11-33). Build the discovery
plan around the plaintiff's weak spots:

1. **Requests for Admission** — lock in the elements: no written
   contract produced, no proof of assignment, no account-level
   data, plaintiff is not the original creditor.
2. **Interrogatories** — chain of title (each transferor/
   transferee and date), the custodian's basis of knowledge, and
   account-level data, within the 50-count cap.
3. **Requests for Production** — bills of sale, assignment
   agreements and schedules, the original cardmember agreement,
   periodic statements, and account-level / electronic records.
4. **Meet-and-confer** — formal letter when responses are
   deficient, then a motion to compel.

The full banks live in `references/rfa-debt-buyer.md`,
`references/interrogatories-debt-buyer.md`,
`references/rfp-debt-buyer.md`, and
`references/meet-and-confer-debt-buyer.md`. Compose with
`ga-discovery` for the procedural mechanics.

## Counterclaim package

Where the facts support it, raise:

- **FDCPA** — federal claim; **1-year SOL from the violation**
  (15 U.S.C. § 1692k(d)). Statutory damages up to $1,000 + actual
  + mandatory fees (§ 1692k(a)(3)). Reg F supplies the
  time-barred-debt-litigation theory.
- **FBPA** — state claim; **2-year SOL** (O.C.G.A. § 10-1-401).
  **First serve the § 10-1-399(b) 30-day written demand** —
  treble damages for intentional violations (§ 10-1-399(c)) and
  attorney's fees (§ 10-1-399(d)).

Because the § 10-1-399(b) demand is a prerequisite and the
demand does **not** toll the 2-year clock, raise the FBPA
counterclaim only after the demand is served (or, if the demand
is sent contemporaneously, plan the pleading sequence so the
30 days have run before the FBPA count is asserted). See
`references/fees-consumer-debt.md` for fee mechanics.

## Composition

This subject-matter bundle composes with:

- **`ga-statewide-format`** — O.C.G.A. § 9-11-10 + Uniform
  Superior Court Rules formatting baseline.
- **`ga-state-court`** — where most debt suits land.
- **`ga-magistrate`** — small-claims / lower-dollar debt suits.
- **`ga-first-30-days`** — answer, affirmative defenses, and
  counterclaims.
- **`ga-discovery`** — discovery framework; layer the debt-buyer
  banks on top (interrogatories allowed, 50-count cap).
- **`ga-draft-motion`** — motion drafting (e.g., to compel, for
  summary judgment, to set aside).
- **`ga-draft-declaration`** — supporting declarations/affidavits.
- **`ga-draft-order`** — proposed orders.
- **`ga-post-judgment`** — set aside a default judgment;
  garnishment traverse and exemptions.
- **`ga-deadlines`** — SOL and response-time computation.
- **`ga-fact-check`** — citation verification against Georgia
  statutes and cases.
- **`ga-quality-check`** — pre-filing format and content QC.

## References

- `references/fdcpa.md` — FDCPA § 1692 et seq. annotated
- `references/reg-f.md` — Regulation F (12 C.F.R. pt. 1006)
- `references/ga-fbpa.md` — Georgia Fair Business Practices Act
  (O.C.G.A. § 10-1-390 et seq.), incl. the § 10-1-399(b) demand
- `references/ga-installment-loan-act.md` — Georgia Installment
  Loan Act (O.C.G.A. Title 7, Ch. 3) small-loan regime
- `references/chain-of-title.md` — standing / assignment-chain
  doctrine under Georgia law
- `references/evidence-debt-buyer.md` — O.C.G.A. § 24-8-803(6) /
  § 24-9-902(11) business-records foundation
- `references/ga-statutes-of-limitations.md` — Georgia SOLs for
  debt and consumer-protection claims
- `references/key-cases.md` — *Nyankojo*, *Wirth*, *Rutledge*,
  *Hill*, *Phoenix Recovery*, *Bowen* and related decisions
- `references/affirmative-defenses.md` — annotated defense catalog
- `references/rfp-debt-buyer.md` — Requests for Production bank
- `references/rfa-debt-buyer.md` — Requests for Admission bank
- `references/interrogatories-debt-buyer.md` — interrogatory bank
  (50-count cap, O.C.G.A. § 9-11-33)
- `references/meet-and-confer-debt-buyer.md` — M&C letter templates
- `references/fees-consumer-debt.md` — fee-shifting and damages in
  Georgia debt-defense cases
- `references/online-sources-consumer-debt.md` — authoritative URLs
  for Georgia debt-related research

**NOT LEGAL ADVICE.** Generated content is a drafting aid;
verify against current rules and case law before filing.
