# UCC Article 9 — Assignments of Accounts (RCW 62A.9A)

Washington's Uniform Commercial Code Article 9 governs secured
transactions and assignments of **accounts receivable** — the legal
category into which purchased consumer debts fall. Debt buyers acquire
accounts through bills of sale and pool-purchase agreements, both of
which are Article 9 transactions.

> **Pair with** `chain-of-title.md` for standing arguments, and
> `evidence-rules.md` for the evidentiary hurdles to admitting the
> bill of sale itself.

## Why Article 9 matters for debt-buyer defense

When a debt buyer sues on a credit-card account, it must prove it is
the owner of **that specific account**. Article 9 governs both:

1. **Whether the transfer validly occurred** (9-203 — attachment)
2. **Whether the buyer has rights enforceable against the account
   debtor** (9-406 — account debtor's rights)

If the pool-purchase documents fail to identify the specific account
with sufficient specificity, the chain of title breaks — even if there
is a bill of sale with a dollar figure attached to a schedule.

## Key RCW 62A.9A sections

### RCW 62A.9A-102 — Definitions

- **Account** (subsection (a)(2)) — a right to payment of a monetary
  obligation, for goods sold, services rendered, or *anything else*
  where the right to payment is not evidenced by an instrument. Credit-
  card receivables are accounts.
- **Assignment** — a transfer of the account. An "assignee" steps
  into the shoes of the assignor, subject to the account debtor's
  defenses.
- **Account debtor** (subsection (a)(3)) — the person obligated on the
  account. In debt cases, the defendant is the account debtor.

### RCW 62A.9A-109(a)(3) — Scope

Article 9 applies to "a sale of accounts ... or chattel paper."
Purchases of consumer debt portfolios are sales of accounts;
Article 9 applies.

### RCW 62A.9A-203 — Attachment and enforceability

A security interest (and, by RCW 62A.9A-109(a)(3), a sale of accounts)
attaches when:

1. **Value has been given**
2. The **debtor has rights** in the collateral
3. The debtor has **authenticated a security agreement** that
   provides a description of the collateral that **reasonably
   identifies** it

"Reasonably identifies" — 9A-108 — requires specific identification.
"All accounts" is sufficient between the original parties, but does
not survive scrutiny when the buyer must prove it bought *this*
account.

### RCW 62A.9A-108 — Sufficiency of description

Describes how collateral must be identified. Three methods:

1. Specific listing
2. Category
3. Any other method by which identity is **objectively determinable**

**A "schedule" attached to a bill of sale that lists accounts by
number satisfies this**. A bill of sale that says "all charged-off
accounts of [originator] from [date range]" — without an attached
account-level schedule — **does not**. Courts outside Washington
have split; Washington courts analyzing debt-buyer standing have
moved toward requiring account-level identification (see
`chain-of-title.md` and `recent-decisions.md`).

### RCW 62A.9A-404 — Rights acquired by assignee; defenses preserved

The assignee takes **subject to** all defenses the account debtor has
against the assignor that accrue before the account debtor receives
notice of the assignment. This is powerful for defendants:

- **FDCPA violations** by the original creditor are defenses
  against the buyer
- **Disputes over the balance** with the original creditor travel
  with the assignment
- **Defective billing** by the original creditor is not cured by
  the assignment

### RCW 62A.9A-406 — Notice and payment to assignee

Until the account debtor receives an **authenticated notification** of
the assignment that reasonably identifies the rights assigned, the
account debtor may continue to pay the assignor and discharge its
obligation.

This means: before a debt buyer can sue, it (or someone in the chain)
must have given the account debtor effective notice of the assignment.
In practice, the first "notice" is often the collection letter or the
lawsuit itself — which can be attacked on FDCPA grounds (§ 1692g
validation notice requirements) for the same deficiency.

## The debt-buyer chain in Article 9 terms

Typical chain:

```
    Original Creditor (e.g., a bank)
                 │
                 │  Bill of sale + pool schedule
                 ▼
         Debt Buyer #1 (wholesale, often bankrupt or dissolved)
                 │
                 │  Assignment + pool schedule
                 ▼
         Debt Buyer #2 (e.g., Velocity Investments)
                 │
                 │  (lawsuit)
                 ▼
          Account Debtor (Defendant)
```

For the buyer to win, each arrow requires:

1. A writing (bill of sale / assignment)
2. Identification of the specific account (9A-108 sufficiency)
3. Value given (9A-203)
4. Authenticated notification to the account debtor (9A-406) —
   which may be the collection letter

## Typical deficiencies to attack

### 1. The bill of sale is generic

Bills of sale often recite that the originator transfers "all right,
title and interest in the charged-off accounts identified on Schedule
A." If Schedule A is:

- **Missing** — the bill of sale conveys nothing specific
- **Redacted** — the defendant cannot verify their account is on it
- **A summary** with dollar totals but no account numbers — does
  not satisfy 9A-108

**Challenge**: move to compel production of the *unredacted* schedule
showing the defendant's account (via wa-discovery). If the buyer
cannot produce it, challenge standing.

### 2. One or more assignments in the chain are missing

Each transfer must be documented. A gap — "we bought it from X but
don't have the paperwork showing X owned it" — defeats the chain.
**Challenge**: request all intermediate assignments in discovery;
move to dismiss or for summary judgment if any link is missing.

### 3. The purchase agreement disclaims warranty of accuracy

Pool-purchase agreements routinely disclaim any warranty of:

- The validity of the debt
- The accuracy of the balance
- The identity of the account debtor
- The enforceability against the account debtor

These disclaimers are admissions against the buyer. Quote them in
the motion:

> Plaintiff concedes in § 4.2 of its purchase agreement that the
> accounts are sold "AS IS, WHERE IS, with no warranty as to
> collectibility, accuracy, or enforceability." Plaintiff thus
> accepted the transferred accounts subject to the account debtors'
> defenses — and cannot now claim entitlement to payment without
> proving those accounts against the defenses available.

### 4. No notice of assignment to the account debtor

Under 9A-406, the account debtor may pay the assignor (not the
assignee) until it receives authenticated notice of the assignment.
If the first "notice" is the lawsuit, the account debtor may
reasonably have continued to owe nothing to the buyer at the time
of suit.

Pair with **FDCPA § 1692g** — validation notice must be in writing
within 5 days of the initial communication. A debt buyer that sues
without having sent § 1692g notice has both an Article 9 and an
FDCPA problem.

## Discovery requests grounded in Article 9

(See `wa-discovery` for full discovery practice.)

### Requests for Production

1. The unredacted Schedule [A / 1 / Pool Register] referenced in
   each bill of sale or assignment identifying Defendant's account
   by account number
2. All documents evidencing payment of consideration (9A-203 value
   element) for the transfer of Defendant's account at each step in
   the chain
3. All assignment notices sent to Defendant pursuant to RCW 62A.9A-406
4. All pool-purchase agreements and related disclaimers, including
   disclaimers of warranty of accuracy or enforceability

### Requests for Admission

1. Admit that the bill of sale from [originator] to [first buyer]
   does not identify Defendant's account by account number in the
   four corners of the document
2. Admit that Plaintiff did not send Defendant an authenticated
   notification of assignment prior to filing suit
3. Admit that the purchase agreement contains a warranty disclaimer
   on collectibility or enforceability of the accounts purchased

## Sample argument pattern (SJ opposition)

```
Plaintiff's standing depends on an unbroken chain of Article 9
assignments, each satisfying RCW 62A.9A-203 (attachment), -108
(sufficiency of description), and -406 (notice). Plaintiff has
failed on all three:

1. **Attachment** (9A-203): no evidence of consideration paid for
   Defendant's specific account at the step from [Buyer 1] to
   Plaintiff.

2. **Description** (9A-108): the bill of sale attached as Exhibit
   [X] refers to "Schedule A," but no Schedule A has been produced
   identifying Defendant's account. A description that is
   determinable only by reference to a document not in evidence is
   not "objectively determinable" under 9A-108.

3. **Notice** (9A-406): no notice of assignment was sent to
   Defendant prior to the filing of this action. Defendant's
   obligations, if any, run to the original creditor under
   9A-406(a).

Plaintiff has not carried its burden. Summary judgment must be
denied and Plaintiff's claim dismissed for lack of standing.
```

## Relationship to ER 803(a)(6) and ER 901

Even a *perfect* Article 9 chain fails if the documents cannot be
admitted. The bill of sale and account-level schedule must also
clear:

- **ER 901** — authentication
- **ER 803(a)(6)** — business-records foundation

See `evidence-rules.md`. A remote custodian at the debt buyer cannot
authenticate records created by the originator; this is independent
of the Article 9 question.

## Leading cases (Washington and persuasive)

- *Discover Bank v. Bridges*, 154 Wn. App. 722, 226 P.3d 191 (2010)
  — chain-of-title foundation
- *Gray v. Suttell & Assocs.*, 123 F. Supp. 3d 1283 (E.D. Wash. 2015)
  — debt-buyer chain and RCW 19.16
- *CACH, LLC v. Kulas*, 21 A.3d 1015 (Me. 2011) — persuasive; bill of
  sale without account schedule insufficient
- *Unifund CCR Partners v. Youngman*, 932 N.E.2d 1253 (Ohio App.
  2010) — persuasive; specific account identification required
- *Palisades Collection, LLC v. Kalal*, 324 Wis. 2d 180, 781 N.W.2d
  503 (2010) — persuasive; similar standards

## Notes

- Article 9 arguments pair naturally with ER objections at SJ — the
  *Article 9 deficiency shows the buyer never acquired the account*;
  the *ER deficiency shows the buyer cannot prove it anyway*
- Washington case law is still developing on the intersection of
  Article 9 and debt-buyer practice — cite federal and out-of-state
  cases as persuasive where WA authority is thin
- **Always fetch** current text of 62A.9A-108, -203, -404, -406 from
  `https://app.leg.wa.gov/RCW/default.aspx?cite=62A.9A.[section]`
  before filing
