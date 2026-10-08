---
name: tn-consumer-debt-codearranger
title: Tennessee Consumer-Debt Defense
description: Subject-matter bundle for defending a Tennessee consumer against debt-collection suits (typically in General Sessions Court). Covers federal FDCPA / Regulation F / FCRA layer; Tennessee Consumer Protection Act (§ 47-18-101 et seq.) with Pursell B2B-collection-conduct limit; Tennessee Collection Service Act (Title 62, Ch. 20) licensing; 2024 § 20-6-104 pre- default-judgment documentation requirement for debt-buyer plaintiffs; chain- of-title under Tennessee UCC Article 9; SOL framework (6-year open-account / 4-year goods); sworn-account device (§ 24-5-107); General Sessions $25k civil cap with unlimited detainer jurisdiction; 10-day de novo appeal to Circuit (§ 27-5-108) where formal discovery applies; 5-pattern fact-pattern triage (stale debt, original creditor's contract, medical debt, default judgment already entered, FDCPA counterclaim).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-consumer-debt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: consumer
language: en
---

# Tennessee Consumer-Debt Defense

> **NOT LEGAL ADVICE.** This skill provides drafting and analytical
> support for defending consumer-debt suits in Tennessee. Statute
> numbers, dollar thresholds, and day counts change — verify every
> citation against the current Tenn. Code Ann. and consult a licensed
> Tennessee attorney about your specific case.

Use this subject-matter bundle when a Tennessee consumer has been
sued by a **debt collector** — typically a **debt buyer** (Midland
Credit Management, Portfolio Recovery Associates, Cavalry SPV, LVNV
Funding, Unifin, etc.) or a **collection agency** acting for an
original creditor. The dominant forum is **General Sessions Court**;
see the "Forum" section below for the strategy that flows from that.

## The Tennessee consumer-debt landscape

Tennessee layers a federal regime over a Tennessee-specific one. A
critical point at the outset: in Tennessee, the **FDCPA and the
Tennessee Collection Service Act** — not the Tennessee Consumer
Protection Act — are the **primary debt-collection regimes**, for
the reasons explained under "The TCPA and its limits" below.

### Federal layer

- **FDCPA** (Fair Debt Collection Practices Act), 15 U.S.C.
  §§ 1692-1692p — the workhorse for debt-buyer defense and
  counterclaims
- **Regulation F**, 12 C.F.R. pt. 1006 — the CFPB regulation
  interpreting and implementing the FDCPA (effective Nov. 30, 2021;
  call-frequency, validation-notice, and time/place rules)
- **FCRA** (Fair Credit Reporting Act), 15 U.S.C. §§ 1681 et seq. —
  furnisher / re-aging / dispute issues when the debt is also being
  reported

### Tennessee layer

- **Tennessee Collection Service Act (TCSA)** — Tenn. Code Ann.
  Title 62, Ch. 20 (§§ 62-20-101 to -124), administered by the
  **Tennessee Collection Service Board** (Dept. of Commerce &
  Insurance). Licensing requirement at § 62-20-105.
- **Tennessee Consumer Protection Act (TCPA)** — Tenn. Code Ann.
  § 47-18-101 et seq. Treble damages and discretionary fees for
  willful/knowing violations (§ 47-18-109), but with an important
  limit in the collection context (below).
- **New pre-default-judgment documentation statute** — Tenn. Code
  Ann. § 20-6-104 (2024 Tenn. Acts ch. 914, eff. July 1, 2024).
  Feature this prominently in any debt-buyer case.
- **Tennessee UCC Article 9** — governs the assignments that make up
  a debt buyer's chain of title.

## Forum — why General Sessions changes everything

Most Tennessee consumer-debt suits are filed in **General Sessions
Court**, a court of limited jurisdiction:

- **Civil jurisdiction cap = $25,000** (Tenn. Code Ann. § 16-15-501;
  attorney's fees and costs are excluded from the cap — verify the
  current figure).
- **Informal procedure — no formal discovery as of right.** The
  Tennessee Rules of Civil Procedure generally do **not** apply in
  General Sessions except where specifically made applicable, so a
  defendant cannot serve interrogatories / RFPs as of right there.
- **De novo appeal to Circuit Court within 10 days** of entry of the
  General Sessions judgment (Tenn. Code Ann. § 27-5-108). On a de
  novo appeal the case is tried **afresh in Circuit Court under the
  full Tennessee Rules of Civil Procedure — and formal discovery DOES
  apply.**

**Strategic consequence:** the single most powerful procedural lever
in many Tennessee debt-buyer cases is the **10-day de novo appeal**.
A timely de novo appeal to Circuit moves the case into a forum where
the consumer can take **discovery** of the chain of title and the
account documentation — the records the debt buyer often cannot
produce. Calendar the 10-day clock under § 27-5-108 immediately
(see `tn-deadlines` and `tn-post-judgment`); it is short and
non-forgiving.

## The new § 20-6-104 documentation requirement (2024)

**Tenn. Code Ann. § 20-6-104** (added by 2024 Tenn. Acts ch. 914,
effective July 1, 2024) is the most significant recent development in
Tennessee debt-buyer defense. Before a court may enter **any default
judgment** in favor of a **debt-buyer / "subsequent creditor"**
plaintiff, the plaintiff must present:

1. **Documentation showing the plaintiff's authority to collect the
   debt** (i.e., the chain of assignment from the original creditor),
   **irrespective of any affidavit**; AND
2. **At least one document showing the debt's existence** (e.g., an
   account statement or the underlying agreement).

Key points:

- It applies to **subsequent creditors / debt buyers**, NOT to
  **original creditors / lienholders**. Identify which the plaintiff
  is at the outset.
- It is a **default-judgment** gate. Even a defendant who never
  appears benefits — but a defendant who does appear can hold the
  plaintiff to this proof and argue it has not satisfied the standard.
- It is **on top of** the ordinary evidentiary foundation
  requirements (below); satisfying an affidavit does not satisfy
  § 20-6-104.

Verify the exact current text and any implementing case law before
relying — this is a brand-new statute.

## The TCPA and its limits — read this before pleading a TCPA claim

The **Tennessee Consumer Protection Act** (Tenn. Code Ann.
§ 47-18-101 et seq.) is a powerful statute on paper:

- **Treble damages** for a **willful or knowing** violation, plus
  **discretionary attorney's fees** (Tenn. Code Ann. § 47-18-109).
- **SOL**: one year from discovery, with a **five-year repose**
  (Tenn. Code Ann. § 47-18-110).

**BUT** — and this is critical — under ***Pursell v. First American
National Bank*, 937 S.W.2d 838 (Tenn. 1996)** and its progeny, the
TCPA **generally does NOT reach the act of collecting a debt or
enforcing a security interest**. *Pursell* held that a repossession
was not "trade or commerce" within the TCPA, and courts have extended
the reasoning to foreclosure and collection conduct. The analysis is
**fact-specific**: **deceptive practices in the underlying consumer
transaction** (the original sale, financing, or solicitation) can
still be actionable under the TCPA. So:

- Do **not** reflexively plead a TCPA claim for ordinary collection
  conduct — it is likely to be dismissed under *Pursell*.
- The **FDCPA** (federal) and the **TCSA** (state collection-licensing
  regime) are the right vehicles for collection-conduct claims.
- Reserve the TCPA for deception in the **underlying transaction**,
  and confirm there is no intervening authority before making any
  categorical statement.

## The Tennessee Collection Service Act (TCSA)

The TCSA, Tenn. Code Ann. Title 62, Ch. 20 (§§ 62-20-101 to -124),
licenses and regulates collection-service businesses through the
**Tennessee Collection Service Board**:

- **Licensing requirement** — Tenn. Code Ann. § 62-20-105: no person
  may operate a collection-service business in Tennessee without a
  valid collection-service license. Check the Board's licensee roster
  for the plaintiff / its servicer.
- **IMPORTANT LIMIT on the "unlicensed = void" theory** — § 62-20-105
  also provides that a debt collected by **voluntary payment or final
  judgment may NOT be set aside solely because the collector lacked a
  license**. So "the collector is unlicensed, therefore the judgment
  is void" is **not** a winning argument by itself; lack of license is
  better used as evidence of an unfair practice and as a pressure
  point, not as an automatic defense to the judgment.
- See also **§ 62-20-124** on conditions for assignment of accounts
  and for commencing litigation (verify current text and scope).

## Statutes of limitations on the debt

| Claim | SOL | Citation |
|---|---|---|
| **Written contract / open account** (incl. most credit-card debt) | **6 years** | Tenn. Code Ann. § 28-3-109 |
| **Sale of goods (UCC)** | **4 years** | Tenn. Code Ann. § 47-2-725 |
| **Sworn account** | *evidentiary device — NOT a separate SOL* | Tenn. Code Ann. § 24-5-107 |

Notes:

- The **6-year** period at § 28-3-109 covers written contracts and
  open accounts, which captures **most credit-card debt**. The clock
  runs from breach, or for open/revolving accounts commonly from the
  **date of last payment / last activity** (fact-dependent — verify
  the account history).
- The **4-year** UCC period at § 47-2-725 governs the **sale of
  goods** and can **displace** the 6-year contract period where the
  obligation is for goods. Identify the nature of the obligation.
- **Sworn account (§ 24-5-107)** is a **procedural / evidentiary
  device**, not a limitations period: a properly sworn account
  affidavit shifts the burden to the defendant to **deny the account
  under oath**. If the plaintiff relies on a sworn account, the
  defendant should verify-and-deny under oath to keep the account in
  dispute.

## Evidence foundation the plaintiff must satisfy

To prove the debt and the assignment, a debt-buyer plaintiff must lay
a business-records foundation:

- **Tenn. R. Evid. 803(6)** — business-records hearsay exception
  (records of regularly conducted activity, via a custodian or other
  qualified witness, or a self-authenticating certification).
- **Tenn. R. Evid. 902** — self-authentication (certified copies of
  business records). Note: the exact 902(11)-equivalent subsection
  numbering should be **verified** against the current rule.

A common defense theme: the debt buyer's affiant has **no personal
knowledge** of the *original creditor's* record-keeping and cannot
lay a 803(6) foundation for records created by a different entity.
Probe the affiant's basis of knowledge.

## The five fact patterns

Most Tennessee consumer-debt-buyer cases fall into one of five
patterns; the defense strategy varies by pattern.

### Pattern 1 — Stale credit-card debt by an out-of-state debt buyer

A debt buyer sues a Tennessee consumer in General Sessions on a
credit-card account whose last payment was 5-7+ years ago.

- **SOL**: the credit-card account is on or past the **6-year**
  § 28-3-109 line. Pin down the date of last payment/activity.
- **Chain of title**: originated by the issuing bank → sold to a
  Tier-1 buyer → resold → sued by a downstream buyer. Each transfer
  needs Article 9 documentation tying **this specific account** to
  the plaintiff.
- **§ 20-6-104**: if the plaintiff seeks a default, hold it to the
  authority-to-collect + at-least-one-document proof.

### Pattern 2 — Debt buyer suing on the original creditor's contract

Plaintiff attaches the **original creditor's** cardholder agreement
to its complaint but is **not** the original creditor.

- **Standing**: the cardholder agreement does not establish that
  **this** plaintiff owns **this** account.
- **Assignment**: demand the Article 9 bills of sale / assignments
  proving the chain of title to the plaintiff.

### Pattern 3 — Collection suit on a medical debt

A collection agency sues for a medical balance.

- **FCRA / accuracy** — dispute and accuracy issues if the balance is
  also being reported.
- **No Surprises Act** (federal, eff. 2022) — certain balance-billing
  may be unenforceable; verify applicability.
- **Foundation** — the agency must still prove the amount and its
  authority to collect.

### Pattern 4 — Default judgment already entered

Consumer was sued, often never properly served, and a judgment was
entered (frequently surfacing via garnishment).

- **10-day de novo appeal** to Circuit under § 27-5-108 if still
  within the window — the cleanest reset (see `tn-post-judgment`).
- **Tenn. R. Civ. P. 60.02** relief from final judgment (mistake,
  excusable neglect, newly discovered evidence, fraud, void, or
  satisfied) where the de novo window has closed; void-judgment
  grounds carry no fixed outer limit, while (1)/(2) grounds carry a
  reasonable-time / one-year limit. Pair with a **meritorious
  defense** (SOL, chain of title, FDCPA).
- For a debt-buyer default, also raise **§ 20-6-104** — the plaintiff
  may have obtained the default without the required documentation.

### Pattern 5 — Counterclaim under the FDCPA (and, narrowly, TCPA)

Consumer was sued; defenses plus a federal counterclaim:

- **FDCPA** — counterclaim for §§ 1692e (false/misleading
  representations), 1692f (unfair practices), or 1692g (validation)
  violations; 1-year SOL from the violation.
- **TCPA** — only where the deception lies in the **underlying
  consumer transaction** (mind *Pursell*); plead carefully.

## Affirmative-defenses catalog

Plead all that apply in the answer (in Circuit on de novo appeal; in
General Sessions, raise orally / by written notice as permitted):

1. **Failure to state a claim** — pleading does not allege the chain
   of title or specific account terms (Tenn. R. Civ. P. 12.02(6) in
   Circuit).
2. **Statute of limitations** — 6 years on contract/open account
   (Tenn. Code Ann. § 28-3-109) or 4 years on goods (§ 47-2-725).
3. **Lack of standing / failure to prove assignment** — plaintiff
   cannot prove it owns this specific account (Article 9).
4. **Lack of privity** between plaintiff and defendant.
5. **Account stated** — no agreed accounting between this plaintiff
   and this defendant.
6. **Failure of consideration / lack of consideration.**
7. **Payment / accord and satisfaction / settlement.**
8. **Failure to satisfy the sworn-account device** — account is
   denied under oath (Tenn. Code Ann. § 24-5-107).
9. **§ 20-6-104** — debt-buyer plaintiff lacks the required
   documentation (default-judgment context).
10. **Identity theft** (if applicable) — FCRA § 605B block.
11. **Discharge in bankruptcy** (if applicable).
12. **FDCPA violation** (raised as counterclaim, but note as a defense
    theme).

See `references/affirmative-defenses.md` for the annotated catalog.

## Chain of title — Tennessee UCC Article 9

A debt buyer must trace ownership from the original creditor through
every intermediate buyer to itself under Tennessee's enactment of UCC
Article 9, with:

- **Bill of Sale** for each transfer;
- **Assignment** specifically identifying the account (account number
  / unique identifier); and
- **Account-level data** matching this consumer's account.

A bill of sale that references "an attached portfolio" without
attaching it, or that says "all accounts sold on [date]" without
tying to this account, is **insufficient** to prove ownership. The
RFP bank in `references/rfp-debt-buyer.md` targets each link.

## Discovery strategy

Discovery is where Tennessee forum mechanics dominate:

- **In General Sessions** there is **no formal discovery as of
  right.** Use informal document requests, cross-examination at the
  hearing, and — most importantly — preserve the **de novo appeal**.
- **In Circuit** (on de novo appeal or original Circuit filing) the
  full Tennessee Rules of Civil Procedure apply:
  1. **First Set of Requests for Admission** (Tenn. R. Civ. P. 36) —
     admissions on the elements (no contract, no assignment, no
     statement of account).
  2. **First Set of Interrogatories** (Tenn. R. Civ. P. 33) — chain
     of title, custodian identity, account-level data. (No statewide
     numeric cap — check the venue's local rules.)
  3. **First Set of Requests for Production** (Tenn. R. Civ. P. 34) —
     bills of sale, assignments, original agreement, periodic
     statements, account-level data, electronic records.
  4. **Subpoena to the original creditor** verifying the chain.
  5. **Meet-and-confer**, then **Motion to Compel** under Tenn. R.
     Civ. P. 37.

The full RFP / RFA / interrogatory banks live in the references. See
`tn-discovery` for mechanics and `tn-general-sessions` for the
forum-specific limits.

## Composition

- For statewide format: `tn-statewide-format`
- For the dominant forum and de novo-appeal mechanics:
  `tn-general-sessions`
- For drafting the answer / first response: `tn-first-30-days`,
  `tn-draft-motion`
- For drafting the declaration: `tn-draft-declaration`
- For drafting the proposed order: `tn-draft-order`
- For drafting the notice / motion: `tn-draft-note`, `tn-draft-motion`
- For discovery and motion-to-compel mechanics: `tn-discovery`
- For setting aside a default / garnishment: `tn-post-judgment`
- For the 10-day appeal and other clocks: `tn-deadlines`
- For QC: `tn-quality-check`, `tn-fact-check`

## References

- `references/fdcpa.md` — FDCPA, 15 U.S.C. § 1692 et seq., annotated
- `references/reg-f.md` — Regulation F at 12 C.F.R. pt. 1006
- `references/fcra.md` — FCRA furnisher / accuracy issues
- `references/tn-collection-service-act.md` — TCSA, Tenn. Code Ann.
  Title 62, Ch. 20 (licensing under § 62-20-105; § 62-20-124)
- `references/tn-tcpa.md` — Tennessee Consumer Protection Act (Tenn.
  Code Ann. § 47-18-101 et seq.) and the *Pursell* limit
- `references/tn-section-20-6-104.md` — the 2024 debt-buyer
  documentation statute
- `references/tn-statutes-of-limitations.md` — § 28-3-109 / § 47-2-725
  / § 24-5-107 sworn account
- `references/chain-of-title.md` — Tennessee UCC Article 9 doctrine
- `references/evidence-debt-buyer.md` — Tenn. R. Evid. 803(6) / 902
  foundation
- `references/rfp-debt-buyer.md` — Request for Production bank
- `references/rfa-debt-buyer.md` — Request for Admission bank
- `references/interrogatories-debt-buyer.md` — Interrogatory bank
- `references/meet-and-confer-debt-buyer.md` — M&C letter templates
- `references/affirmative-defenses.md` — annotated catalog
- `references/key-cases.md` — Tennessee debt-buyer case law
- `references/online-sources-consumer-debt.md` — canonical URLs
