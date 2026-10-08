---
name: az-consumer-debt-codearranger
title: Arizona Consumer-Debt Defense
description: 'Use when defending an Arizona consumer against a debt-collection lawsuit (typically by debt buyer or collection agency, usually in Justice Court). Triggers: "sued for a debt Arizona", "debt collector Arizona", "Arizona Consumer Fraud Act", "debt buyer Arizona", "time-barred debt Arizona Mertola", "credit card statute of limitations Arizona", "FDCPA Arizona", "Arizona collection agency license", "Justice Court debt Arizona", "chain of title Arizona debt", "default judgment Arizona debt". Subject-matter bundle covering federal FDCPA / Regulation F layer, Arizona Consumer Fraud Act, DIFI collection-agency licensing (A.R.S. Title 32), chain-of-title under Arizona UCC Article 9, statute-of-limitations framework including *Mertola* credit-card acceleration rule, two-way attorney-fee exposure (A.R.S. § 12-341.01), Justice Court forum.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-consumer-debt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: consumer
language: en
---

# Arizona Consumer-Debt Defense

> **NOT LEGAL ADVICE.** This subject-matter bundle describes a procedural and substantive framework
> for Arizona consumer-debt cases, not legal advice and not strategic advice for any specific case.
> Outcomes are fact-specific; the choice of defenses, claims, motions, and discovery belongs to the
> litigant (and any counsel the litigant retains). Statute numbers, dollar thresholds, and day counts
> change — verify every citation against the current Arizona Revised Statutes (azleg.gov), the
> Arizona Rules of Civil Procedure, and the Justice Court Rules of Civil Procedure before filing,
> and consult a licensed Arizona attorney.

Use this bundle when an Arizona consumer has been sued by a **debt collector** — typically a **debt
buyer** (Midland Credit Management, Portfolio Recovery Associates, LVNV Funding, Cavalry SPV,
Jefferson Capital, etc.) or a **collection agency** acting for an original creditor. The dominant
forum is the **Justice Court**; see "Forum" below.

## The Arizona consumer-debt landscape

Arizona layers a federal regime over an Arizona-specific one. Unlike some states, Arizona has **no
standalone consumer-collection-practices act** modeled on the FDCPA; abusive collection conduct is
reached instead through the **Arizona Consumer Fraud Act (ACFA)** and the **collection-agency
licensing** regime, alongside the federal FDCPA.

**Federal layer.** **FDCPA**, 15 U.S.C. §§ 1692–1692p — the workhorse for debt-buyer defense and
counterclaims; reaches **third-party** collectors and debt buyers, generally **not** original
creditors. **Regulation F**, 12 C.F.R. pt. 1006 — the CFPB rule implementing the FDCPA (eff. Nov. 30,
2021; call-frequency, validation-notice content, time/place rules). Federal text lives in the shared
corpus; cross-reference `../az-law-references/references/federal-debt-laws/` (symlinked into
`claude-legal-federal-laws`).

**Arizona layer.** **ACFA** — A.R.S. § 44-1521 et seq. (deceptive/unfair practices; private right of
action). **Collection-agency licensing** — A.R.S. Title 32, Chapter 9, § 32-1001 et seq.
(administered by the Arizona Department of Insurance and Financial Institutions, **DIFI**).
**Arizona UCC Article 9** — A.R.S. § 47-9101 et seq. (assignments / chain of title). **Limitations**
— A.R.S. §§ 12-541 to 12-548. **Attorney fees in contract actions** — A.R.S. § 12-341.01 (two-way).

## The Arizona Consumer Fraud Act (ACFA) — reaching abusive collection conduct

The **ACFA**, A.R.S. § 44-1521 et seq., prohibits any "deception, deceptive or unfair act or
practice, fraud, false pretense, false promise, misrepresentation, or concealment, suppression or
omission of any material fact" in connection with the sale or advertisement of merchandise (A.R.S.
§ 44-1522). Arizona courts recognize an **implied private right of action** under the ACFA.

- **Reaching collection conduct.** A collector that misrepresents the amount, character, or legal
  status of a debt; threatens action it cannot or will not take; or sues on a time-barred debt may
  commit a deceptive/unfair act actionable under the ACFA. Map each misrepresentation to a specific
  factual element (the false statement, materiality, reliance/injury). Framing matters: the ACFA is
  the Arizona vehicle for the deceptive-practices theory the FDCPA also supplies federally.
- **Statute of limitations on the ACFA claim.** The implied private ACFA action is generally governed
  by the **1-year** limitations period of **A.R.S. § 12-541** (actions on a statutory liability).
  **Verify the current period and accrual rule** against azleg.gov and Arizona case law before
  pleading — this is drift-prone and the period is short.
- **Remedies / fees.** Confirm the current remedies framework (actual damages; the availability and
  source of any attorney-fee or punitive recovery) before relying on it. Do not assume FDCPA-style
  statutory damages — the ACFA's remedial structure is its own.

## Collection-agency licensing — A.R.S. Title 32, Chapter 9 (DIFI)

Arizona **licenses collection agencies** under **A.R.S. § 32-1001 et seq.**, administered by **DIFI**
(the Department of Insurance and Financial Institutions, successor to the former Department of
Financial Institutions). A "collection agency" broadly includes a person engaged in collecting or
soliciting claims owed or asserted to be owed to another; a **debt buyer** collecting on purchased
accounts is generally acting as a collection agency for licensing purposes — confirm against the
current statutory definition and any debt-buyer-specific provisions.

- **Check the license.** Look up the plaintiff (and any servicer) on the DIFI licensee search before
  responding. An out-of-state debt buyer suing in Arizona without a license is a recurring pattern.
- **Licensing as a pressure point — not an automatic win.** Operating **unlicensed** violates the Act
  and exposes the collector to statutory penalties and an unfair-practice theory. Whether the lack of
  a license **voids** the debt, strips the plaintiff of **capacity to sue**, or merely supplies a
  regulatory violation is **not automatic** — verify current Arizona authority before arguing the
  suit or any resulting judgment is void. Treat lack of license as **evidence of an unfair practice
  and a settlement lever**, not a guaranteed merits defense.

## Statutes of limitations on the debt

Point to the corpus (`references/az-statutes-of-limitations.md` and the `az-statutes-debt` corpus)
for the authoritative, current counts — these are drift-prone. The headline framework:

| Claim | SOL | Citation |
|---|---|---|
| **Written contract** (signed-agreement debt) **or credit card** | **6 years** | A.R.S. § 12-548 |
| **Open account / stated account** | **3 years** | A.R.S. § 12-543 |
| **Oral / unwritten-contract debt** | **3 years** | A.R.S. § 12-543 |

- A.R.S. § 12-548(A) supplies the **6-year** period for debt evidenced by or founded on **(1) a
  written contract executed in this state** or **(2) a credit card** (as defined in A.R.S. § 13-2101) —
  so most credit-card debt has a direct statutory 6-year peg under § 12-548(A)(2), independent of the
  "written contract" question. The **3-year** period of A.R.S. § 12-543 governs **debt not evidenced
  by a writing** and **stated or open accounts**. (§ 12-544's 4-year period covers merchant mutual
  accounts, out-of-state instruments/judgments, etc.; sale-of-goods contracts run under A.R.S.
  § 47-2725 per § 12-544(4).) Whether a given account is a "credit card / written contract" or an
  "open account" can still be contested — pin down the account documents.
- **The *Mertola* credit-card acceleration rule — CRITICAL.** In ***Mertola, LLC v. Santos***, 244
  Ariz. 488, 422 P.3d 1028 (2018) (No. CV-17-0109-PR, July 27, 2018), the **Arizona Supreme Court**
  held that where a credit-card agreement contains an **optional-acceleration clause** (giving the
  creditor the option to declare the entire balance immediately due upon default), a **single cause
  of action** for the **entire debt** accrues — and the limitations clock starts on the **whole
  balance** — upon **default**, i.e., as of the **first uncured missed minimum payment**, **regardless
  of whether or when the creditor actually exercises** its option to accelerate. The Court expressly
  **rejected** the argument that accrual waits for the creditor's act of acceleration, adopting a
  **bright-line rule** so a creditor cannot extend the limitations period indefinitely by declining to
  accelerate. The claim is **not** treated as a series of installment claims each with its own clock.
  (A debtor's **cure** — the creditor's acceptance of arrearages bringing the account current — voids
  the cause of action and starts a fresh six-year period on any later default; a partial payment that
  does not cure does **not** reset the clock.) **Practical effect:** the SOL window for many
  credit-card claims is **shorter** than a payment-by-payment theory would suggest, and a suit filed
  more than the limitations period after the first uncured default may be **time-barred in full**. Pin
  down the date of the first missed payment; **verify the holding and cite against azleg.gov /
  CourtListener** before relying on it.
- **SOL is an affirmative defense** that must be **pleaded** (Ariz. R. Civ. P. 8(c)) or it is waived
  — raise it expressly in the answer. It is also a **summary-judgment ground** under **Ariz. R. Civ.
  P. 56**; a time-barred debt is a strong Rule 56 motion candidate once the account dates are fixed.

## Chain of title / standing — Arizona UCC Article 9

A debt buyer must trace ownership from the original creditor through every intermediate buyer to
itself under **Arizona UCC Article 9** (A.R.S. § 47-9101 et seq.), with a **Bill of Sale** for each
transfer, an **Assignment** specifically identifying **this** account (account number), and
**account-level data** matching this consumer's account. A bill of sale referencing "an attached
portfolio" without the attachment, or "all accounts sold on [date]" without tying to **this**
account, is **insufficient**. Standing turns on whether the plaintiff can prove it owns this
specific account.

**Business-records foundation.** To admit the account records and the assignment, the plaintiff must
lay a foundation under **Ariz. R. Evid. 803(6)** (records of a regularly conducted activity, via a
custodian or qualified witness) and **Ariz. R. Evid. 902(11)** (self-authenticating certified
business records in lieu of a live custodian). Recurring theme: the debt buyer's affiant has **no
personal knowledge** of the *original creditor's* record-keeping and cannot lay an 803(6) foundation
for another entity's records. Probe the affiant's basis of knowledge.

## Attorney fees — A.R.S. § 12-341.01 cuts both ways

In a contested **action arising out of contract**, **A.R.S. § 12-341.01** provides that the court
**may** award the **successful party** reasonable attorney fees. This is a **two-way** statute and a
critical risk consideration:

- A consumer who **defeats** the suit (e.g., wins on SOL or no-chain-of-title) may apply for fees as
  the successful party.
- But a consumer who **loses** — including by failing to appear and suffering a **default judgment**
  — may be ordered to pay the **creditor's** reasonable fees on top of the debt and costs. The award
  is **discretionary** (the court weighs the fee factors), not automatic, but the exposure is real.
  Factor this two-way risk into any decision to litigate vs. settle, and into the decision **never to
  ignore** a complaint (default exposes the consumer to fees). **Verify the current statute and
  fee-award standard** before advising on exposure.

## Forum — most consumer-debt suits are in Justice Court

Most Arizona consumer-debt suits are filed in the **Justice Court**, a court of limited civil
jurisdiction (claims up to the statutory jurisdictional cap — **verify the current figure**), under
the **Justice Court Rules of Civil Procedure (JCRCP)** rather than the Arizona Rules of Civil
Procedure. Larger claims go to **Superior Court**. The **answer deadline** runs under the JCRCP (the
period depends on the manner of service — **confirm the current days**); miss it and the plaintiff
can take a **default** and then a **default judgment** (with potential § 12-341.01 fee exposure). See
`az-justice-courts` for the JCRCP mechanics, `az-superior-courts` for Superior Court practice,
`az-first-30-days` for the answer, and `az-post-judgment` for setting aside a default.

## The five fact patterns

**Pattern 1 — Debt buyer with no chain of title.** Demand the Article 9 bills of sale and
account-specific assignments tying **this** account to the plaintiff (A.R.S. § 47-9101 et seq.);
challenge the affiant's Ariz. R. Evid. 803(6)/902(11) basis of knowledge; check the plaintiff's DIFI
collection-agency license (A.R.S. § 32-1001 et seq.).

**Pattern 2 — Time-barred debt (Mertola).** Pin the date of the **first uncured missed payment**.
Under ***Mertola, LLC v. Santos***, 244 Ariz. 488 (2018), a credit-card account with an
optional-acceleration clause accrues a **single** cause of action for the **whole balance** upon
default — as of the first uncured missed payment, **regardless of whether/when the creditor
accelerates** — so a suit filed more than the applicable period (written contract / credit card
**6 years**, A.R.S. § 12-548; open account **3 years**, A.R.S. § 12-543) after that date may be
**time-barred in full**. Plead SOL (Ariz. R. Civ. P. 8(c)) and move under **Rule 56**.

**Pattern 3 — FDCPA validation / dispute violation.** Consumer disputed or never received a
compliant validation notice. FDCPA §§ 1692g (validation), 1692e (false/misleading), 1692f (unfair);
Reg F validation-notice content (12 C.F.R. pt. 1006). Pair with an **ACFA** deceptive-practice
theory (A.R.S. § 44-1522) where the conduct is also a misrepresentation.

**Pattern 4 — Wrong amount / wrong person.** Inflated balance (unauthorized fees/interest) or
mistaken identity / identity theft. **FDCPA** §§ 1692e(2)/1692f(1) (misrepresenting the amount;
collecting amounts not owed); **ACFA** § 44-1522 (deceptive statement of the debt's amount or legal
status); FCRA § 605B identity-theft block if applicable (see the shared `federal-debt-laws/` corpus).

**Pattern 5 — Unlicensed collector / debt buyer.** Plaintiff or servicer holds no Arizona DIFI
collection-agency license. **A.R.S. Title 32, Chapter 9** (§ 32-1001 et seq.) — operating without a
license violates the Act; use as **evidence of an unfair practice / settlement lever**, verifying
current Arizona authority before arguing the suit or judgment is void. Pair with **ACFA / FDCPA**
theories.

## Affirmative-defenses catalog

Plead all that apply in the answer (Ariz. R. Civ. P. 8(c) — defenses not pleaded may be waived):

1. **Statute of limitations** — written contract / credit card 6 years (A.R.S. § 12-548) or open
   account / unwritten-contract debt 3 years (A.R.S. § 12-543), as sharpened by *Mertola* for
   credit-card debt under an optional-acceleration clause; Rule 56 summary-judgment ground.
2. **Lack of standing / failure to prove assignment** — plaintiff cannot prove it owns this account
   (UCC Article 9).
3. **Failure to state a claim** — no chain of title or specific account terms.
4. **Lack of / failure of consideration.**
5. **Payment / accord and satisfaction / release / settlement.**
6. **Account stated** — no agreed accounting between this plaintiff and this defendant.
7. **Lack of capacity to sue** — unlicensed collection agency / debt buyer (A.R.S. § 32-1001 et
   seq.); assert with the verification caveat.
8. **Identity theft** (if applicable) — FCRA § 605B block.
9. **Discharge in bankruptcy** (if applicable).
10. **FDCPA / ACFA violation** (raised as a counterclaim; also a defense theme).

See `references/affirmative-defenses.md` for the annotated catalog.

## Discovery strategy

In Superior Court the Arizona Rules of Civil Procedure govern; in **Justice Court** the **JCRCP**
control and discovery is **more limited** (verify the venue's rules before serving). Tools:
**Requests for Admission** on the elements; **Interrogatories** on chain of title, custodian
identity, and account-level data; **Requests for Production** for bills of sale, assignments, the
original cardholder agreement, periodic statements, and electronic records; then **meet-and-confer**
and a **Motion to Compel**. The full RFP / RFA / interrogatory banks live in the references; see
`az-discovery` for mechanics.

## Composition

- Statewide format: `az-statewide-format`. Forums: `az-justice-courts` (dominant), `az-superior-courts`,
  `az-maricopa`, `az-pima`.
- Answer / first response: `az-first-30-days`, `az-draft-motion`. Declaration: `az-draft-declaration`.
- Proposed order: `az-draft-order`. Notice / motion: `az-draft-note`, `az-draft-motion`.
- Discovery / motion-to-compel: `az-discovery`. Set-aside / garnishment: `az-post-judgment`.
- Deadlines: `az-deadlines`. Pro se conventions: `az-pro-se`. QC: `az-quality-check`, `az-fact-check`.

## References

- `references/fdcpa.md`, `references/reg-f.md` — federal layer (see
  `../az-law-references/references/federal-debt-laws/`)
- `references/az-consumer-fraud-act.md` — ACFA (A.R.S. § 44-1521 et seq.; § 44-1522 practices;
  the § 12-541 1-year limitations question)
- `references/az-collection-agency-licensing.md` — A.R.S. Title 32, Ch. 9 (§ 32-1001 et seq.); DIFI
  licensure + licensee lookup
- `references/az-statutes-of-limitations.md` — A.R.S. §§ 12-541 / 12-543 / 12-544 / 12-548 +
  *Mertola, LLC v. Santos* acceleration rule
- `references/az-attorney-fees.md` — A.R.S. § 12-341.01 two-way contract-action fees
- `references/chain-of-title.md` — Arizona UCC Article 9 doctrine (A.R.S. § 47-9101 et seq.)
- `references/evidence-debt-buyer.md` — Ariz. R. Evid. 803(6) / 902(11) foundation
- `references/rfp-debt-buyer.md`, `references/rfa-debt-buyer.md`,
  `references/interrogatories-debt-buyer.md` — discovery banks
- `references/affirmative-defenses.md` — annotated catalog
- `references/online-sources-consumer-debt.md` — canonical URLs
