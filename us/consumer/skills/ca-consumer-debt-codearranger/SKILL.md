---
name: ca-consumer-debt-codearranger
title: California Consumer-Debt Defense
description: Use this skill for California consumer-debt defense — debt-buyer suits, original-creditor collection cases, and matters involving FDCPA, Regulation F, California Rosenthal Act, CDCLA licensing, FDBPA chain of title, or California UCL. Triggers include "California debt-buyer defense", "I was sued on a credit card in California", "collection agency sued me", "Rosenthal Act", "FDBPA chain of title", "unlicensed debt collector California", "validation notice", "time-barred debt California", "chain of title California debt", "business records California debt", "Rosenthal counterclaim", "consumer debt attorney fees". Subject-matter bundle covering FDCPA / Reg F / Rosenthal Act / CDCLA / FDBPA / UCL substantive law, chain-of-title doctrine, and discovery banks (RFPs, RFAs, interrogatories) for debt-defense litigation.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-consumer-debt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: consumer
language: en
sources:
- title: Ca Statutes Of Limitations
  path: references/ca-statutes-of-limitations.md
- title: Cdcla
  path: references/cdcla.md
- title: Chain Of Title
  path: references/chain-of-title.md
- title: Evidence Debt Buyer
  path: references/evidence-debt-buyer.md
- title: Fact Patterns
  path: references/fact-patterns.md
- title: Fdcpa
  path: references/fdcpa.md
- title: Fees Consumer Debt
  path: references/fees-consumer-debt.md
- title: Interrogatories Debt Buyer
  path: references/interrogatories-debt-buyer.md
- title: Key Cases
  path: references/key-cases.md
- title: Meet And Confer Debt Buyer
  path: references/meet-and-confer-debt-buyer.md
- title: Online Sources Consumer Debt
  path: references/online-sources-consumer-debt.md
- title: Recent Decisions
  path: references/recent-decisions.md
- title: Reg F
  path: references/reg-f.md
- title: Rfa Debt Buyer
  path: references/rfa-debt-buyer.md
- title: Rfp Debt Buyer
  path: references/rfp-debt-buyer.md
- title: Rosenthal Act
  path: references/rosenthal-act.md
- title: Ucc Article 9
  path: references/ucc-article-9.md
---

# California Consumer-Debt Defense

This skill is the **subject-matter bundle** for California
consumer-debt litigation: debt-buyer cases, original-creditor
collection actions, and any matter turning on FDCPA / Reg F /
Rosenthal Act / CDCLA / FDBPA / UCL.

It assumes the procedural framework is already in place via the
matter-neutral skills. This skill adds:

- **Substantive law**: FDCPA, Reg F, Rosenthal Act, CDCLA,
  FDBPA, UCL
- **Chain-of-title doctrine**: what a California debt-buyer
  plaintiff must prove to recover; FDBPA heightened pleading
  requirements
- **Evidence patterns**: Cal. Evid. Code § 1271 business-records
  foundation; Cal. Evid. Code § 1561 custodian declarations;
  Secondary Evidence Rule (§ 1521)
- **Fact-pattern triage**: 5 common California debt-defense
  scenarios and the matching defenses / counterclaims
- **Discovery banks**: pre-built RFPs, RFAs, and specially
  prepared interrogatories (up to 35 without declaration under
  CCP § 2030.030(a)) targeting the weak spots of a debt-buyer's
  case
- **Example filings**: synthetic answers, declarations, motions,
  and orders for a California debt-buyer-defense fact pattern

> **NOT LEGAL ADVICE.** Consumer-debt defense is fact-specific
> and outcome-dependent. This skill provides a procedural and
> substantive framework — not strategic advice for any specific
> case.

## Five common California debt-defense fact patterns

### Pattern 1: Debt-buyer suit on credit-card debt — FDBPA applies

Defendant receives a summons and complaint. The plaintiff
(e.g., LVNV Funding, Midland Funding, Cavalry SPV, Portfolio
Recovery Associates) alleges defendant owes a charged-off
credit-card account originally with Bank of America, Capital
One, or a similar original creditor. The plaintiff is a debt
buyer — it did not extend the credit.

**Key California distinction — FDBPA (Cal. Civ. Code,
§§ 1788.50 et seq.)**: Since January 1, 2014, a debt-buyer
plaintiff must comply with heightened pleading and
documentation requirements:

- Civ. Code, § 1788.58 requires the complaint to allege:
  - The name of the original creditor
  - The account number (at least the last 4 digits)
  - The date of charge-off
  - The balance at charge-off
  - The date of last payment
  - A statement that the complaint is filed within the SOL
  - The chain of title from original creditor to plaintiff
- Civ. Code, § 1788.60 requires pre-suit written notice to
  debtor; failure is an affirmative defense
- Civ. Code, § 1788.62 provides that noncompliance is a
  complete defense and entitles defendant to attorney's fees

**Defenses commonly raised in this pattern**:

- **FDBPA non-compliance** — Complaint lacks required § 1788.58
  allegations; defendant can demurrer or seek judgment
- **Lack of standing** — Plaintiff cannot prove every link in
  the chain of title from original creditor to itself
- **Statute of limitations** — CCP § 337 (4-year SOL on written
  contract); date of last payment triggers the clock
- **CDCLA non-licensure** — Check the DFPI website; collector
  or buyer without a license is violating Fin. Code § 100001
  and the UCL
- **Cal. Evid. Code § 1271 foundation** — Plaintiff cannot
  authenticate the original creditor's records through its own
  custodian

**Counterclaims commonly considered in this pattern**:

- **FDCPA** (§§ 1692e, 1692f, 1692g) — false representations,
  unfair practices, failure to provide validation
- **Rosenthal Act** (Civ. Code, § 1788.17) — incorporates FDCPA
  standards; also applies to original creditors
- **UCL** (Bus. & Prof. Code, § 17200) — borrows FDCPA / FDBPA
  violations as the "unlawful" prong
- **FDBPA private right of action** (Civ. Code, § 1788.62)

### Pattern 2: Debt-buyer suit on medical debt

Defendant is sued on a medical bill sold to a debt buyer.
Medical debt cases carry special rules:

**Federal rules on medical debt and credit reporting**:
- CFPB Reg V (12 CFR pt 1022) prohibits most medical debt from
  appearing on consumer credit reports for one year after the
  obligation is established, and removes such debts under
  $500 entirely for NCAP compliance
- HIPAA (45 CFR pts 160, 164): PHI cannot be disclosed without
  patient authorization; debt buyers relying on PHI to sue
  face authentication problems and possible HIPAA exposure

**California-specific**:
- The Confidentiality of Medical Information Act (Cal. Civ.
  Code, §§ 56-56.37) parallels HIPAA at the state level
- California hospitals and providers are subject to stricter
  charity care and billing requirements (Health & Safety Code,
  § 127400 et seq.)
- No balance billing for emergency services (Health & Safety
  Code, § 1317.2)

**Defenses**:
- Authentication: PHI in medical records cannot be used as
  evidence without proper HIPAA authorization — challenge
  foundation at every turn
- FDBPA compliance required same as any other debt-buyer suit
- CMIA (Civ. Code, § 56.36) — private right of action for
  unauthorized release of medical information
- Potential invalidity of the underlying debt (billing errors
  are common; itemized billing statement required)

### Pattern 3: Out-of-statute lawsuit (zombie debt)

Plaintiff files suit on a debt past the applicable California
SOL. Common when debt buyers hold old pools.

**California SOLs** (see `references/ca-statutes-of-limitations.md`):
- Written contract: CCP § 337 — 4 years
- Oral contract: CCP § 339 — 2 years
- Open book account: CCP § 337(a) — 4 years from last entry
- Sale of goods (UCC Art. 2): Cal. Comm. Code, § 2725 — 4 years

**Defenses**:
- **Statute of limitations**: plead as an affirmative defense
  under CCP § 437c or demurrer; burden shifts to plaintiff
  to show revival
- **Revival doctrine**: CCP § 360 — written acknowledgment or
  partial payment restarts the clock; oral promises do NOT
  revive; partial payment must be unambiguously referable to
  the specific debt
- **Borrowing statute**: CCP § 361 applies the shorter of
  California's SOL or the SOL of the state where the
  cause of action arose

**Counterclaims**:
- **FDCPA** (§ 1692e(2), § 1692e(5), § 1692f(1)) — collecting
  on time-barred debt is misleading and unfair
- **Reg F § 1006.26(b)** — debt collector must not bring legal
  action on time-barred debt
- **Rosenthal Act** (Civ. Code, § 1788.17) — incorporates
  FDCPA standards
- **UCL** (Bus. & Prof. Code, § 17200) — predicate "unlawful"
  act is the FDCPA / Rosenthal violation

### Pattern 4: Identity theft / mistaken identity defense

Defendant is sued on a debt that is not theirs — account
opened by another person in defendant's name, or wrong "John
Doe" sued.

**California Identity Theft Victims Privacy and Protection Act**
(Cal. Civ. Code, § 1798.93):

- Defendant can seek a court declaration that the debt is
  the result of identity theft (§ 1798.93(a))
- Defendant must file a written claim with creditor and
  provide a police report (§ 1798.93(b))
- If creditor continues collection after notice, liable for
  actual damages, $30,000 minimum statutory, punitive damages,
  and attorney's fees (§ 1798.93(c)(2))

**Federal layer**:
- FCRA (15 U.S.C. § 1681c-2) — block of information resulting
  from identity theft on credit report
- FDCPA § 1692g — defendant can dispute validity within 30 days;
  debt collector must cease collection and verify

**Defenses and counterclaims**:
- **Civ. Code, § 1798.93 declaration** — file motion for
  declaration that the debt is fraudulent
- **FDCPA counterclaim** — collection after dispute is a
  separate violation
- **Rosenthal Act counterclaim**
- **UCL / UDAP** — fraudulent and unfair business practice

### Pattern 5: Original creditor lawsuit

Plaintiff is the original creditor — the bank or company that
actually extended credit. The FDCPA does not apply (original
creditors are not "debt collectors" under 15 U.S.C. § 1692a(6)).
But the **Rosenthal Act applies** — it covers first-party
creditors.

**Defenses**:
- **Account stated / objection**: defendant timely disputed
  the account
- **Statute of limitations**: CCP § 337 (4 years on written
  contract)
- **Unauthorized charges**: identity theft, fraud, or
  unauthorized use
- **Failure of consideration**: goods or services not received
- **Statute of frauds** (Civ. Code, § 1624) — certain agreements
  must be in writing

**Counterclaims**:
- **Rosenthal Act** (Civ. Code, §§ 1788-1788.33) — applies to
  first-party creditors collecting in California; § 1788.17
  incorporates FDCPA standards
- **UCL** (Bus. & Prof. Code, § 17200) — false/unfair conduct
  in collection
- **FCRA** (15 U.S.C. § 1681s-2) — if original creditor made
  false credit-reporting entries

## Substantive law — quick reference

### FDCPA (15 U.S.C. § 1692 et seq.)

The federal Fair Debt Collection Practices Act. Applies to
**debt collectors** (not original creditors, generally)
collecting **consumer** debt.

| Section | Subject |
|---------|---------|
| § 1692c | Communication restrictions |
| § 1692d | Harassment / abuse |
| § 1692e | False or misleading representations |
| § 1692f | Unfair practices |
| § 1692g | Validation notices |
| § 1692k | Civil liability ($1,000 statutory + actual + fees) |
| § 1692k(d) | 1-year SOL |

See `references/fdcpa.md` for the full annotated FDCPA.

### Regulation F (12 CFR pt 1006)

The CFPB's implementing regulation, effective November 30,
2021. Key provisions:

| Section | Subject |
|---------|---------|
| § 1006.6 | Communication with consumers |
| § 1006.14(b) | Call-frequency safe harbor (7-in-7) |
| § 1006.18 | False or misleading representations |
| § 1006.22 | Unfair or unconscionable practices |
| § 1006.26 | Time-barred debt |
| § 1006.30 | First-communication notice |
| § 1006.34 | Validation information |
| § 1006.38 | Disputes |

See `references/reg-f.md` for the full annotated Reg F.

### Rosenthal Fair Debt Collection Practices Act
(Cal. Civ. Code, §§ 1788–1788.33)

California's primary consumer-debt statute. **Key California
distinctions**:

- **Applies to original creditors** (first-party collectors)
  as well as third-party debt collectors — this is a major
  expansion over FDCPA, which covers only third-party collectors
- **§ 1788.17** incorporates FDCPA § 1692c through § 1692j
  directly into California law; every FDCPA violation is also
  a Rosenthal Act violation in California
- **§ 1788.30** damages: actual damages + statutory damages
  of $100 to $1,000 per violation + attorney's fees for
  prevailing consumer
- **§ 1788.30(f)** — 1-year SOL from the violation
- **§ 1788.13** — prohibited false/misleading statements
  (similar to FDCPA § 1692e)
- **§ 1788.11** — prohibited harassment (similar to FDCPA § 1692d)
- **§ 1788.15** — communication restrictions (similar to
  FDCPA § 1692c)

See `references/rosenthal-act.md` for the full annotated statute.

### California Debt Collection Licensing Act (CDCLA)
(Cal. Fin. Code, §§ 100000–100027, effective January 1, 2022)

Requires that **both debt collectors AND debt buyers** obtain
a license from the DFPI (Department of Financial Protection
and Innovation) before collecting debts in California.

- **Fin. Code, § 100001** — "debt collector" defined broadly;
  includes debt buyers
- **Fin. Code, § 100002** — license required before engaging
  in debt-collection activity
- **Fin. Code, § 100006** — DFPI can revoke/suspend license
- **Non-licensure consequences**:
  - Affirmative defense to collection suit
  - Violation of Cal. Bus. & Prof. Code, § 17200 (UCL)
  - DFPI enforcement action
- **DFPI license lookup**: https://dfpi.ca.gov/consumers/
  check-your-financial-company/

Check the DFPI database at the outset of every case.

See `references/cdcla.md` for the full annotated statute.

### Fair Debt Buying Practices Act (FDBPA)
(Cal. Civ. Code, §§ 1788.50–1788.64, effective January 1, 2014)

Governs **debt buyers** — entities that purchase charged-off
consumer debt for collection purposes. Not applicable to
original creditors.

**Key sections**:

- **Civ. Code, § 1788.52** — before debt buyer can collect,
  it must have documented proof of chain of title, balance
  itemization, and the original account number
- **Civ. Code, § 1788.54** — communications to debtor must
  include specific disclosures; failure to provide is a
  violation
- **Civ. Code, § 1788.56** — debt buyer must provide debtor
  with documentation of debt within 30 days of written request
- **Civ. Code, § 1788.58** — complaint requirements:
  - Name of original creditor
  - Last 4 digits of account number
  - Date of charge-off
  - Balance at charge-off
  - Date of last payment
  - Statement that action is timely
  - Chain of ownership from original creditor to plaintiff
- **Civ. Code, § 1788.60** — pre-suit written notice required
- **Civ. Code, § 1788.62** — noncompliance is a complete defense;
  prevailing debtor entitled to costs and attorney's fees
- **Civ. Code, § 1788.64** — action for injunctive relief by
  AG or DA

See `references/chain-of-title.md` for the chain-of-title
doctrine analysis.

### UCL (Cal. Bus. & Prof. Code, § 17200 et seq.)

The Unfair Competition Law. Provides three prongs:

- **Unlawful**: borrows violations of any other law as the
  predicate — FDCPA violations, Rosenthal Act violations,
  FDBPA violations, and CDCLA non-licensure all qualify
- **Unfair**: conduct substantially injurious to consumers;
  balancing test under *Cel-Tech Communications, Inc. v.
  Los Angeles Cellular Telephone Co.* (1999) 20 Cal.4th 163
- **Fraudulent**: conduct likely to deceive a reasonable consumer

**Remedies**:
- Injunctive relief (Bus. & Prof. Code, § 17203)
- Restitution (§ 17203)
- Civil penalty of $2,500 per violation for AG enforcement
  (§ 17206)
- Attorney's fees only via § 1021.5 private-attorney-general
  theory (not automatically available under UCL itself)

**Standing**: "Any person who has suffered injury in fact and
has lost money or property" — *Kwikset Corp. v. Superior Court*
(2011) 51 Cal.4th 310.

### Chain of title

A California debt-buyer plaintiff must prove every link in the
chain from original creditor to itself. FDBPA § 1788.58
expressly requires this in the complaint. Typical chain:

```
Original Creditor (Bank of America)
       ↓ Bulk Sale Agreement, Bill of Sale, Assignment Schedule
First Debt Buyer (e.g., Asset Acceptance / Sherman)
       ↓ Bulk Sale Agreement, Bill of Sale, Assignment Schedule
Second Debt Buyer (e.g., LVNV Funding / Encore Capital)
       ↓ Possible additional transfers
Current Plaintiff (e.g., Midland Funding, LLC)
```

Each link requires:

- **Bill of Sale** — the document evidencing each transfer
- **Assignment Schedule** — the inventory listing the specific
  accounts assigned, identified by account number and balance
- **Authentication** — under Cal. Evid. Code § 1271 and § 1561,
  the records must be authenticated by a custodian with
  personal knowledge of the originating entity's business
  practices

See `references/chain-of-title.md` for the full doctrine and
`references/evidence-debt-buyer.md` for the evidentiary analysis.

### California statutes of limitations

| Claim | SOL | Statute |
|-------|-----|---------|
| Written contract | 4 years | CCP § 337 |
| Oral contract | 2 years | CCP § 339 |
| Open book account | 4 years | CCP § 337(a) |
| Sale of goods (UCC Art. 2) | 4 years | Cal. Comm. Code, § 2725 |
| Negotiable instrument (UCC Art. 3) | 6 years | Cal. Comm. Code, § 3118 |
| FDCPA claim | 1 year | 15 U.S.C. § 1692k(d) |
| Rosenthal Act claim | 1 year | Civ. Code, § 1788.30(f) |
| FDBPA claim | 4 years | Civ. Code, § 1788.62 (see ref.) |
| UCL claim | 4 years | Bus. & Prof. Code, § 17208 |

**Revival**: CCP § 360 — written acknowledgment or partial
payment referrable to the specific debt restarts the clock.
Oral promises or ambiguous payments do NOT revive.

**Borrowing statute**: CCP § 361 — California applies the
shorter of California's SOL or the SOL of the state where
the cause of action arose.

See `references/ca-statutes-of-limitations.md` for full analysis.

## Key California-specific defenses

### CDCLA non-licensure

Check the DFPI licensee database before answering. If the
plaintiff (debt buyer or collection agency) lacks a valid
DFPI license, this is:

1. An affirmative defense — plaintiff lacks legal authority
   to collect
2. A UCL "unlawful" prong violation — unlicensed activity
   is an unfair business practice
3. Potentially a Fin. Code § 100018 violation with DFPI
   enforcement consequences

**Pleading**: "As a [Nth] affirmative defense, Plaintiff
was not licensed by the California Department of Financial
Protection and Innovation as required by Cal. Fin. Code,
§ 100002, and therefore lacks the legal authority to collect
debts or maintain this action in California."

### FDBPA pleading deficiencies

If the complaint was filed by a debt buyer and fails to
allege any element required by Civ. Code, § 1788.58:

- **Demurrer under CCP § 430.10(e)** — failure to state
  facts sufficient to constitute a cause of action
- **Motion for judgment on the pleadings (CCP § 438)** —
  if deficiency is not cured

### Rosenthal Act violations

Particularly useful when:

- The original creditor (not just a debt buyer) is engaging
  in abusive collection conduct
- The collector has made false representations about the
  amount, legal status, or nature of the debt
- The collector failed to provide a validation notice

Damages: Civ. Code, § 1788.30 — actual damages + $100–$1,000
statutory per violation + attorney's fees.

### UCL "unlawful" prong via FDCPA

Every FDCPA violation in California is also a Rosenthal Act
violation (§ 1788.17) AND a UCL "unlawful" prong violation.
Triple-count these violations.

Advantage of UCL over standalone FDCPA: UCL has a 4-year SOL
(Bus. & Prof. Code, § 17208) versus FDCPA's 1-year SOL.

## Attorney's fees — defendant's recovery paths

When the consumer-defendant prevails:

### Path 1: FDCPA § 1692k(a)(3)

Mandatory one-way fee-shifting — consumer who prevails on
an FDCPA counterclaim recovers reasonable attorney's fees
and costs.

### Path 2: Rosenthal Act — Civ. Code, § 1788.30(c)

Successful action against a debt collector under the Rosenthal
Act entitles the consumer to reasonable attorney's fees.

### Path 3: Civ. Code, § 1717 — contract reciprocity

Most cardholder agreements contain a fee clause (e.g.,
"You shall pay our attorney's fees if we sue to collect").
Civ. Code, § 1717 makes such clauses reciprocal — the
prevailing party (including the consumer) recovers fees.

### Path 4: CCP § 1021.5 — private attorney general

When the consumer's action enforces an important right
affecting the public interest:

- FDCPA / Rosenthal / FDBPA / CDCLA enforcement qualifies
  in many cases
- Consumer need not be the only beneficiary
- Financial burden on consumer relative to stake must be
  disproportionate

### Path 5: FDBPA — Civ. Code, § 1788.62

When the debt buyer fails to comply with FDBPA, the prevailing
consumer recovers costs and attorney's fees.

### Path 6: Civ. Code, § 1788.30 Rosenthal statutory damages

$100 to $1,000 per violation. Not a fee-shifting provision —
this is substantive statutory damages recoverable even without
attorney representation.

See `references/fees-consumer-debt.md` for full analysis and
procedural mechanics.

## Discovery banks (subject-matter-specific)

Pre-built discovery banks for California debt-defense practice.
These compose with the procedural framework in `ca-discovery`:

- **`references/rfp-debt-buyer.md`** — First Requests for
  Production targeting chain of title, original-creditor
  records, plaintiff's records, CDCLA licensure, FDBPA
  compliance, communications, and collection history
- **`references/rfa-debt-buyer.md`** — Requests for Admission
  locking in foundational facts (plaintiff's corporate form,
  DFPI license status, chain of title, charge-off date,
  authentication capacity)
- **`references/interrogatories-debt-buyer.md`** — Up to 35
  specially prepared interrogatories under CCP § 2030.030(a)
  covering chain of title, pre-suit contact, balance arithmetic,
  debtor identification, account opening, charge-off, and
  underlying contract
- **`references/meet-and-confer-debt-buyer.md`** — California
  M&C templates per CCP § 2031.310(b)(2) (RFPs), § 2030.300(b)
  (interrogatories), and § 2033.290(b) (RFAs); 45-day deadline
  to move to compel applies to most discovery

## Evidence patterns

The Cal. Evid. Code § 1271 business-records foundation question
is the critical evidentiary battleground. The plaintiff's
typical declaration:

> "I am the custodian of records for [Plaintiff Debt Buyer].
> Plaintiff maintains records of accounts in the ordinary
> course of business. Account number ending XXXX was assigned
> to Plaintiff on [date] by [Original Creditor]. Plaintiff's
> records show a balance of $[amount] owing on the account.
> True and correct copies are attached."

This declaration typically **fails** as foundation because:

1. The declarant is the **debt buyer's** custodian, not the
   original creditor's custodian
2. The original creditor's records are hearsay — the declarant
   cannot attest that they were made in the original creditor's
   regular course of business
3. The "remote custodian" doctrine — the debt buyer cannot
   speak to the trustworthiness of records it did not create
4. Cal. Evid. Code § 1561 requires the custodian to provide
   a declaration with specific elements; a conclusory declaration
   fails

Note the California Secondary Evidence Rule: Cal. Evid. Code
§ 1521 allows secondary evidence of the content of a writing
if the original is lost, stolen, or in the opposing party's
control — but this applies to the content of documents, not
to the foundation for hearsay exceptions.

See `references/evidence-debt-buyer.md` for the doctrine and
specific objection language.

## Key cases — California and 9th Circuit

### California appellate

- *Davidson v. Seterus, Inc.* (2018) 21 Cal.App.5th 283 —
  first-party collector + Rosenthal Act; broad application
  to original creditors acting through servicers
- *Komarova v. National Credit Acceptance, Inc.* (2009) 175
  Cal.App.4th 324 — broad construction of Rosenthal Act;
  no requirement that collector know the law is violated
- *Herr v. Nestlé USA, Inc.* (2003) 109 Cal.App.4th 779 —
  UCL "unlawful" prong incorporates violation of any statute
- *Kwikset Corp. v. Superior Court* (2011) 51 Cal.4th 310 —
  UCL standing; "injury in fact" + "lost money or property"

### 9th Circuit / federal

- *Henson v. Santander Consumer USA, Inc.*, 582 U.S. 79 (2017)
  — debt buyer collecting own debt generally not FDCPA "debt
  collector" under § 1692a(6) primary definition; but may
  qualify under "regularly collects" prong
- *Heintz v. Jenkins*, 514 U.S. 291 (1995) — attorneys
  engaged in debt collection are "debt collectors"
- *Rotkiske v. Klemm*, 589 U.S. 8 (2019) — FDCPA 1-year SOL
  runs from violation, not discovery (discovery rule generally
  inapplicable except through equitable tolling)

See `references/key-cases.md` for full citations and holdings.

## Companion procedural skills

This subject-matter bundle composes with:

- **`ca-statewide-format`** — CRC 2.100–2.119 formatting
- **The relevant court skill** — `ca-lasc` / `ca-sfsc` /
  `ca-county-courts`
- **`ca-pro-se`** — pro se conventions in California
- **`ca-law-references`** — citation conventions, online
  sources; California Style Manual
- **`ca-discovery`** — discovery framework; layer the
  debt-buyer-specific banks on top
- **`ca-first-30-days`** — initial response (demurrer,
  answer, affirmative defenses + counterclaims)
- **`ca-deadlines`** — SOL computation; CCP § 12a calendar
  computation
- **`ca-fact-check`** — citation verification against
  California statutes and cases
- **`ca-quality-check`** — format pass before filing
- **`ca-draft-*`** — drafting the specific filings
- **`ca-post-judgment`** — if default judgment already entered

## References

- `references/fdcpa.md` — FDCPA section-by-section
- `references/reg-f.md` — Regulation F annotated
- `references/rosenthal-act.md` — California Rosenthal Act
  (Civ. Code, §§ 1788–1788.33)
- `references/cdcla.md` — California Debt Collection Licensing
  Act (Fin. Code, §§ 100000 et seq.)
- `references/chain-of-title.md` — chain-of-title doctrine
  under California law and FDBPA
- `references/evidence-debt-buyer.md` — Cal. Evid. Code § 1271
  business-records foundation in debt-buyer cases
- `references/ca-statutes-of-limitations.md` — California SOLs
  for debt and consumer-protection claims
- `references/key-cases.md` — California and federal decisions
- `references/recent-decisions.md` — recent California
  appellate and 9th Circuit opinions (2020–2025)
- `references/fees-consumer-debt.md` — fee-shifting in
  California debt-defense cases
- `references/rfp-debt-buyer.md` — RFPs targeting chain
  of title and FDBPA compliance
- `references/rfa-debt-buyer.md` — RFAs locking in basics
- `references/interrogatories-debt-buyer.md` — up to 35
  specially prepared interrogatories
- `references/meet-and-confer-debt-buyer.md` — sample M&C
  correspondence
- `references/ucc-article-9.md` — UCC Article 9 (Cal. Comm.
  Code, §§ 9101–9809) on secured transactions and debt-buyer
  chain-of-title
- `references/online-sources-consumer-debt.md` — authoritative
  URLs for California debt-related research
- `references/fact-patterns.md` — five common debt-defense
  fact patterns with deeper analysis

**NOT LEGAL ADVICE.** Generated content is a drafting aid;
verify against current rules and case law before filing.
