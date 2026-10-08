# Debt-Buyer Fact Patterns — Pattern Recognition Guide

Most debt-buyer complaints fit one of a small number of recurring
patterns. Recognizing the pattern points to the defenses that
commonly fit, the discovery typically served first, and the
procedural pressure points in this kind of case.

> **NOT LEGAL ADVICE.** This catalog is a drafting and triage aid,
> not legal advice. The defenses and counterclaims listed below
> are options the rules make available for the pattern — not a
> recommendation that any particular litigant pursue any
> particular option. The choice of pleading, motion, defense, and
> discovery belongs to the litigant (and any counsel the litigant
> retains). For procedural order, see `wa-first-30-days`.

---

## Pattern 1: Generic pool-schedule / redacted bill of sale

### Indicators

- Complaint attaches a "bill of sale" referring to "Schedule A" or
  "Pool Register" but no Schedule A is attached
- Attached schedule is heavily redacted — dollar totals visible,
  account numbers blacked out
- The transfer is described as "all charged-off accounts" from a
  date range

### Defenses commonly raised in this pattern

1. **UCC 9A-108 insufficiency** — the description does not
   objectively identify *Defendant's* account (see
   `ucc-article-9.md`)
2. **Standing** — CR 17(a); plaintiff is not the real party in
   interest because no assignment of *this* account is shown
3. **ER 1002 best evidence** — where is the unredacted schedule?
4. **FDCPA § 1692e(2)(A)** — misrepresenting the character of the
   debt (claiming ownership without proof of assignment)

### First-wave discovery

- RFP the **unredacted** Schedule A showing Defendant's account
- RFP all intermediate bills of sale and their schedules
- RFA: admit that the bill of sale does not identify Defendant's
  account by number in the four corners of the document

### Expected plaintiff response

- Refusal to produce the unredacted schedule citing
  confidentiality
- Production of a different document ("certificate of indebtedness")
  purporting to be authenticated, but which itself is a buyer-side
  declaration with no originator attestation

### Motion pathway

- Motion to compel production of unredacted schedules
- If plaintiff does not produce, MSJ on standing and on
  ER 803(a)(6) foundation failure

---

## Pattern 2: Missing monthly statements

### Indicators

- Complaint alleges a charge-off balance but attaches only a single
  "final statement" or "summary"
- No month-by-month account history produced
- Originator name appears only in the affidavit, not on statements

### Defenses commonly raised in this pattern

1. **ER 803(a)(6) foundation** — the affidavit is from a buyer-side
   custodian who never worked at the originator
2. **Calculation** — plaintiff cannot show how the balance was
   computed; challenge the principal/interest/fee breakdown
3. **FDCPA § 1692f(1)** — attempting to collect an amount not
   "expressly authorized" when unable to show the contract basis for
   each charge
4. **Account-stated defense rebutted** — if plaintiff pivots to
   account stated, no evidence of Defendant's acquiescence in a
   specific balance

### First-wave discovery

- RFP **every** monthly statement from account inception to
  charge-off
- IROG: breakdown of balance into principal, interest, fees, with
  calculation methodology and references to the controlling
  cardholder agreement
- RFA: admit plaintiff does not possess all monthly statements for
  the account

### Motion pathway

- SJ on inability to show the contract terms / calculations
- Alternative: partial SJ limiting balance to principal, striking
  interest and fees

---

## Pattern 3: No original cardholder agreement

### Indicators

- Complaint alleges written-contract basis for the 6-year SOL but
  attaches only a generic "sample" cardholder agreement
- Or attaches a cardholder agreement from a different year than
  account opening
- Originator refused to supply the original to the buyer (common)

### Defenses commonly raised in this pattern

1. **ER 1002 best evidence** — original required unless
   unavailability affirmatively shown
2. **SOL recharacterization** — if no written contract, the claim
   is account-stated under RCW 4.16.080(3) (**3-year** SOL, not 6);
   many buyer claims become time-barred under this
3. **FDCPA § 1692e(8)** — communicating or threatening to
   communicate information known or should be known to be false
   (claiming a written-contract basis when the contract is not in
   possession)
4. **ER 803(a)(6) + 901** — the "sample" cannot be authenticated as
   Defendant's agreement

### First-wave discovery

- RFP: the *signed or accepted* cardholder agreement bearing
  Defendant's account number or signature
- RFP: all cardholder agreements in effect for Defendant's account
  between origination and charge-off (agreements change over time)
- RFA: admit plaintiff does not possess the cardholder agreement
  in force at origination of Defendant's account
- RFA: admit plaintiff does not possess any cardholder agreement
  bearing Defendant's signature

### Motion pathway

- SJ on SOL recharacterization (3-year bar)
- Motion in limine excluding the "sample" cardholder agreement

---

## Pattern 4: Affidavit from remote custodian with template language

### Indicators

- Affidavit executed by someone at the debt buyer, not the
  originator
- Language is highly templated ("I have reviewed the records," "the
  records are maintained in the ordinary course," "the balance is
  true and correct")
- No explanation of **how** the custodian has personal knowledge
  of the originator's recordkeeping

### Defenses commonly raised in this pattern

1. **ER 602 lack of personal knowledge**
2. **ER 803(a)(6) foundation** failure — the custodian did not
   make the records and has no knowledge of how they were made
3. **ER 901** — cannot authenticate records originating from an
   unrelated entity
4. **CR 56(e)** / **CRLJ 56(e)** — SJ affidavit must be made on
   personal knowledge; this one is not

### First-wave discovery

- Deposition of the affiant (cost-effective even for pro se if the
  plaintiff is pressing hard)
- IROG: identify the affiant's employment history, specifically any
  time worked at the originator, training on originator's systems,
  or integration of originator's records into the buyer's systems
- RFP: the affiant's employment records and training records that
  support the claimed knowledge

### Motion pathway

- Motion to strike the affidavit (CR 56(e) / CRLJ 56(e))
- If stricken, SJ on inability to carry foundation burden

---

## Pattern 5: Account-stated vs. written-contract pleading confusion

### Indicators

- Complaint alternately describes the claim as "breach of a written
  contract" (6-year SOL, RCW 4.16.040) and as "account stated" or
  "open account" (3-year SOL, RCW 4.16.080)
- The real claim is account-stated but plaintiff wants the longer
  SOL

### Defenses commonly raised in this pattern

1. **SOL** — if the debt is account-stated, 3 years from default
2. **Inconsistent pleading** — CR 12(f) strike
3. **Failure to state a claim** — ambiguity on the theory pleaded
4. **Judicial admission** — pin plaintiff in discovery to one
   theory, then attack that theory

### First-wave discovery

- IROG: state precisely the legal theory (written contract, account
  stated, open account, or other) and identify the document that is
  the "contract" if the theory is written-contract
- RFA: admit the claim is pleaded on an account-stated basis

### Motion pathway

- MTD under CRLJ 12(b)(6) for failure to state a claim (if the
  theory is not pleaded with particularity)
- MSJ on SOL once the theory is pinned to account-stated

---

## Pattern 6: Time-barred suit

### Indicators

- Date of last payment or charge-off is more than 6 years before
  filing (written-contract claim) or 3 years (account-stated /
  oral)
- Partial payments made without written acknowledgment after the
  SOL would have tolled
- Complaint obscures the date of default

### Defenses commonly raised in this pattern

1. **SOL** — RCW 4.16.040 (6-yr) or RCW 4.16.080 (3-yr), depending
   on theory (see Pattern 5)
2. **Reg F § 1006.26** — prohibits suit on time-barred debt;
   filing the suit is itself an FDCPA / Reg F violation
3. **FDCPA § 1692e(2)(A), (5)** — deceptive representation that a
   lawsuit on a time-barred debt can be pursued
4. **CPA per se via RCW 19.16.250(21)** — threatening or taking
   legal action on a debt where the action is time-barred

### First-wave discovery

- RFP: all documents evidencing the date of Defendant's first
  default / last unpaid payment
- RFA: admit that the last payment on the account was made more
  than 6 years before the filing of the Complaint
- RFA: admit no written acknowledgment of the debt was signed by
  Defendant within 6 years preceding filing

### Motion pathway

- MSJ on SOL
- Counterclaim: FDCPA + Reg F + CPA per se (RCW 19.16.440 bridge)
- Request fees under 4.84.330 (reciprocal), RCW 19.16.450, RCW
  19.86.090, 15 U.S.C. § 1692k

---

## Pattern 7: Unlicensed collection agency / out-of-state debt buyer

### Indicators

- Plaintiff is incorporated out-of-state
- Check the Washington Department of Licensing — not listed as a
  licensed collection agency
- Plaintiff is suing in its own name but acquired the debt for
  collection

### Defenses commonly raised in this pattern

1. **RCW 19.16.110** — licensing requirement violated
2. **RCW 19.16.440** — per se CPA violation
3. **Dismissal** as an unlicensed plaintiff cannot bring suit to
   enforce collection of a debt (*Evergreen Collectors v. Holt* and
   *Gray v. Suttell*)
4. **FDCPA § 1692e** — deceptive implication of lawful collection
   authority

### First-wave discovery

- IROG: state all state license numbers plaintiff holds authorizing
  collection, by state
- RFP: copies of plaintiff's Washington collection agency license
- Public-record check: search DOL.wa.gov directly

### Motion pathway

- MTD on standing / capacity to sue
- Counterclaim: per se CPA via RCW 19.16.440 + attorney fees under
  RCW 19.16.450

---

## Pattern 8: Originator → DBA → Buyer (naming-churn obscuring the chain)

### Indicators

- Bill of sale shows a transfer from "Bank A, N.A." but the
  cardholder agreement is from "Bank A (Delaware)"
- Bank mergers, renaming, or "doing business as" variations between
  issuer, assignor of the pool, and the pool purchaser
- Chain: Bank → Servicer → Trust → Buyer 1 → Buyer 2 → Plaintiff

### Defenses commonly raised in this pattern

1. **Chain-of-title gaps** — every naming discrepancy is a gap to
   prove up
2. **Successor-in-interest evidence required** — merger
   documents, trust agreements, servicing agreements
3. **ER 901 authentication** — each document requires its own
   foundation

### First-wave discovery

- RFP: every document showing that "Bank A, N.A." and "Bank A
  (Delaware)" are the same entity or that one is the legal
  successor of the other (merger certificate, SEC filing, OCC
  notice of consolidation)
- IROG: identify each entity that ever held legal or equitable
  title to Defendant's account, with dates of acquisition and
  transfer
- RFP: trust indentures and pooling/servicing agreements where the
  debt was held by a trust

### Motion pathway

- MSJ on chain of title — identify the missing link; plaintiff
  cannot cure at the pleading stage with declarations alone
- Discovery sanctions if the documents cannot be produced

---

## Pattern 9: Default-judgment trap

### Indicators

- Service of process was by abode or substitute service
- Defendant did not receive actual notice
- Default judgment entered
- Discovery of the judgment comes later (credit pull, garnishment)

### Defenses commonly raised in this pattern

1. **CR 60(b) motion to vacate** (superior) / **CRLJ 60(b)**
   (district) — within **one year** for (b)(1)-(3) grounds, or a
   reasonable time for (b)(4)-(11)
2. **Service defect** — improper service voids the judgment
   independent of the merits
3. **Meritorious defense** — all the above patterns become
   available once the judgment is vacated

### First-wave action

- Immediate motion to vacate under CR 60 (see
  `wa-post-judgment` skill)
- Simultaneously: answer with all defenses and counterclaims
  preserved in case the vacation is granted

### Motion pathway

- Motion to vacate + response/answer conditional on vacation +
  request for stay of any enforcement (garnishment, levy)

---

## Pattern 10: Zombie debt / revived in buyer's records

### Indicators

- The account was charged off many years ago
- A more recent "reporting date" appears on credit bureau records
  (the buyer re-aged the trade line)
- The buyer sends a new collection letter offering "settlement" on
  a debt already time-barred

### Defenses commonly raised in this pattern

1. **SOL** — as in Pattern 6
2. **FCRA re-aging violation** — if the trade line's first-
   delinquency date was reset, pair with FCRA claim (15 U.S.C.
   § 1681s-2)
3. **Reg F § 1006.26** — time-barred debt
4. **Reg F § 1006.30** — no credit reporting before first contact

### First-wave discovery

- RFP: credit-bureau reports furnished by plaintiff and its
  predecessors
- RFP: the "date of first delinquency" furnished to each bureau
- IROG: identify who calculated and furnished the DOFD

### Motion pathway

- Counterclaim: FDCPA + Reg F + FCRA + CPA per se
- SJ defensively on the underlying collection claim

---

## Cross-pattern matrix

| Pattern | Main RCW | Main Rule | FDCPA Section | Main Case |
|---------|----------|-----------|---------------|-----------|
| 1 Redacted schedule | RCW 62A.9A-108 | ER 1002 | § 1692e(2)(A) | *Kulas* |
| 2 Missing statements | RCW 4.16.040/.080 | ER 803(a)(6) | § 1692f(1) | *Discover v. Bridges* |
| 3 No cardholder agreement | RCW 4.16 | ER 1002 | § 1692e(8) | *Ziegler* |
| 4 Remote custodian | RCW 19.16.250 | ER 602, 803(a)(6) | § 1692e | *Iverson* |
| 5 Pleading confusion | RCW 4.16.080(3) | CR 12(b)(6), 12(f) | § 1692e(2) | — |
| 6 Time-barred | RCW 4.16 | CR 56 | § 1692e(2), (5) | *Rotkiske* |
| 7 Unlicensed | RCW 19.16.110 | CR 12(b) | § 1692e | *Gray v. Suttell* |
| 8 Naming churn | RCW 62A.9A | ER 901, 1002 | § 1692e | *Kulas* |
| 9 Default trap | — | CR 60(b) | — | *Morin v. Burris* |
| 10 Zombie / re-age | RCW 4.16, 19.86 | — | § 1692e; FCRA | — |

## Intake questions

When a user describes their case, ask:

- When did you open the account? (Pattern 3)
- When was your last payment? (Pattern 6)
- Did you receive a letter from the plaintiff before the lawsuit?
  (Patterns 6, 10)
- How were you served — in person, at home, left at the door?
  (Pattern 9)
- What's attached to the complaint — a bill of sale, a cardholder
  agreement, monthly statements, an affidavit? (Patterns 1, 2, 3, 4)
- Who is the plaintiff — the original bank or a debt buyer?
  (Patterns 4, 7, 8)
- Is the plaintiff licensed in Washington? (Pattern 7 — check DOL)
- Are you already in collections with the credit bureaus?
  (Pattern 10)

## Notes

- **Patterns overlap** — most cases match 2–4 of these. Order
  defenses by leverage, not by match order
- **Discovery first**, motions second — the patterns above are
  designed to surface evidence that supports the motion
- **Document the plaintiff's every concession** — misnamed parties,
  admitted redactions, missing statements — in a running chronology
  so the motion record is complete
