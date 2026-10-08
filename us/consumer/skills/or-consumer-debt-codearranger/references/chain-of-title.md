# Chain of Title — Debt-Buyer Cases (Oregon)

A debt buyer must prove it owns the alleged debt to recover.
This requires proving every transfer from the original creditor
to the debt buyer — the **chain of title**. Chain of title is
the principal evidentiary battleground in debt-defense
litigation in Oregon and nationwide.

## The typical chain

```
Original Creditor (Bank of America)
                ↓
                ↓  Bulk Sale Agreement (master agreement
                ↓  governing the pool sale)
                ↓
                ↓  Bill of Sale (transfer document)
                ↓
                ↓  Assignment Schedule (list of specific
                ↓  accounts assigned, identified by account
                ↓  number and balance)
                ↓
First Debt Buyer (Sherman Acquisition / CACH / etc.)
                ↓
                ↓  Same documents for the resale
                ↓
Second Debt Buyer (Velocity Investments / LVNV / etc.)
                ↓
                ↓  Sometimes additional resales
                ↓
Current Plaintiff (e.g., LVNV Funding, LLC)
```

For the current plaintiff to prove standing, **every link**
must be authenticated. Defects in any link defeat the chain.

## Required documents per link

### 1. Bulk Sale Agreement (master)

The master contract between buyer and seller. Typically:

- Many pages of boilerplate
- Defines the scope of the sale (which accounts; which
  warranties)
- Specifies that account-specific details are in the
  Assignment Schedule

The Bulk Sale Agreement alone is insufficient — it shows the
seller's intent to sell some accounts, but not specifically
the defendant's account.

### 2. Bill of Sale

The transfer document. Typically:

- One page
- Brief: "Seller transfers all right, title, and interest in
  the accounts listed on Schedule A to Buyer"
- Signed by an officer of seller and buyer

The Bill of Sale also is insufficient alone — it requires the
Assignment Schedule to identify the specific accounts.

### 3. Assignment Schedule

The list of accounts. Typically:

- A multi-page document or spreadsheet
- Identifies each account by:
  - Account number (often partial or redacted)
  - Original cardholder name
  - Date of last activity / charge-off
  - Balance at charge-off

Debt buyers often produce only **redacted** assignment
schedules — with the defendant's row visible but the other
rows blacked out. This is **inadequate** authentication
because:

- The redaction hides the schedule's structure
- The court cannot verify the schedule actually existed at the
  time of the alleged transfer
- The defendant cannot evaluate the accuracy of the data row
  for their own account

### 4. Cardholder Agreement (original)

The contract between the original cardholder (defendant) and
the original creditor. Establishes:

- The terms of the credit relationship
- Whether the account was a personal or business account
- The applicable interest rate
- The fees structure
- Any arbitration clause
- The chosen governing law

Cardholder agreements are typically **NOT** in the debt
buyer's possession. The defendant should specifically request
this document; the debt buyer's failure to produce it goes to
both standing AND foundation under OEC 803(6).

### 5. Monthly Statements

Showing the account history — purchases, payments, interest,
fees. Establishes:

- The accuracy of the alleged balance
- Whether the defendant disputed any charges
- The dates of charges (relevant for SOL analysis)
- Whether interest accrued post-charge-off (which may not be
  authorized by contract — § 1692f(1))

Monthly statements are also typically NOT in the debt buyer's
possession.

## Common chain-of-title failures

### Failure 1: Missing the cardholder agreement

The debt buyer cannot produce the original cardholder agreement
because the seller did not transfer it as part of the sale. The
seller's records show only summary information, not the actual
contract terms.

**Implication**: Without the contract, the debt buyer cannot
prove:

- The terms governing interest, fees, and arbitration
- Whether the alleged debt is a contract debt or open account
  (affecting SOL analysis)
- Whether the defendant signed for personal or business
  purposes (affecting consumer-statute coverage)

### Failure 2: Redacted assignment schedule

The debt buyer produces an assignment schedule with only the
defendant's row visible. The remainder is redacted.

**Implication**: The court cannot verify the schedule existed
at the time of the alleged transfer. The redaction itself is
evidence of poor record-keeping; a properly maintained
schedule would not require redaction (the other rows aren't
the defendant's privilege).

### Failure 3: Bill of Sale without specificity

The Bill of Sale references "the accounts listed on Schedule
A" but no Schedule A is produced, OR the Schedule A is
generic without account-level detail.

**Implication**: There is no transfer of the specific account
— only a generic transfer of "accounts" without
identification.

### Failure 4: Gap in the chain

The chain shows transfer from Original Creditor to Debt Buyer
A, then from Debt Buyer B to Plaintiff — but no document for
Debt Buyer A → B. The chain has a missing link.

**Implication**: Plaintiff cannot prove ownership traces back
to the original creditor.

### Failure 5: Defective authentication

The plaintiff offers the documents but cannot authenticate them
under OEC 803(6) / 902(11). The custodian who signs the
declaration is plaintiff's custodian, not the seller's — they
cannot attest to the seller's record-keeping practices.

## Discovery approach to chain of title

Defense discovery targets the documents listed above:

1. **Cardholder agreement** — RFP 1
2. **Monthly statements** for the 60-month period before
   charge-off — RFP 2
3. **Bill of Sale** for each transfer in the chain — RFP 3
4. **Assignment schedule** (unredacted) for each transfer
   — RFP 4
5. **Bulk Sale Agreement** for each transfer — RFP 5
6. **Account history** (post-charge-off; from each holder)
   — RFP 6
7. **Communications** between the holders regarding the
   account — RFP 7

If the plaintiff produces partial or no documents, motion to
compel under ORCP 46 A — see `or-discovery` and
`references/rfp-debt-buyer.md`.

## Strategic deployment

### Phase 1: Force production

The defendant's first discovery push targets every chain-of-
title document. If plaintiff produces nothing useful, the
motion-to-compel record builds.

### Phase 2: Authenticate or strike

Once any documents are produced, examine their authentication.
The OEC 803(6) / 902(11) foundation typically requires more
than the debt buyer can provide. See `evidence-debt-buyer.md`
for the foundation analysis.

### Phase 3: Summary judgment / motion in limine

If plaintiff cannot produce authenticated chain-of-title
documents:

- **Motion for summary judgment under ORCP 47** — plaintiff
  lacks evidence on an element (standing) of its claim
- **Motion in limine** to exclude the unauthenticated
  documents from trial

### Phase 4: Counterclaims

The course of conduct supports FDCPA, UTPA, and ORS 697
counterclaims:

- Filing suit without proof of ownership = false
  representation (§ 1692e, UTPA § 646.608(1)(s))
- Demanding payment without proof of standing = unfair
  practice (§ 1692f(1))

## Oregon-specific notes

### UCC Article 9 (ORS 79)

Some debt transfers involve **security interests** under UCC
Article 9 (ORS 79). When the debt is sold as a security
interest, the chain of title requires UCC filings and
perfection analysis. This is rare for credit-card debt but
common for auto loans and equipment finance.

See `references/ucc-article-9.md` for the doctrine.

### Mandatory arbitration

If the original cardholder agreement contains a mandatory
arbitration clause, plaintiff may seek to compel arbitration.
The defense to compel: the cardholder agreement is the
authority for arbitration, but plaintiff cannot produce the
agreement. No agreement → no arbitration. *See* AT&T Mobility
LLC v. Concepcion, 563 US 333 (2011) (federal arbitration
preemption — but Oregon courts apply traditional contract
formation analysis to determine whether the arbitration
agreement exists).

### Original-creditor cases

For original-creditor cases (where the plaintiff IS the
original creditor, not a debt buyer), chain of title is moot.
The original creditor doesn't need to prove transfer; they own
the debt by virtue of having created it. Focus shifts to:

- Account-stated objections
- Authentication of records
- Statute of limitations
- Fraudulent / unauthorized charges

## Sample chain-of-title argument (motion to compel)

```
III. STATEMENT OF ISSUES

     1. Whether Plaintiff, alleging it acquired Defendant's
        alleged account through an assignment from Bank of
        America, must produce the documents proving that
        chain of ownership.

     2. Whether ORCP 36 B(1) "possession, custody, or
        control" includes documents the debt buyer
        contractually has a right to obtain from the
        original creditor under the bulk sale agreement.

VI. ARGUMENT

    A.  Plaintiff cannot stand on the bare allegation of
        ownership.

        A plaintiff in a breach-of-contract claim must prove
        each element, including standing. The Complaint
        alleges Plaintiff "acquired the account through an
        assignment from Bank of America." (Compl. ¶ 4.)
        Plaintiff has produced no document evidencing that
        assignment. The Bill of Sale and Assignment
        Schedule are the foundational documents; their
        production is non-discretionary in a debt-buyer
        case.

    B.  Plaintiff's "not in possession" objection is
        invalid.

        Under ORCP 36 B(1), "possession, custody, or
        control" includes the legal right to obtain. The
        bulk sale agreement that Plaintiff entered into with
        Bank of America gives Plaintiff the contractual
        right to obtain account-specific documentation upon
        request. Plaintiff therefore has "control" of these
        documents.
```

## Cross-references

- `or-consumer-debt` SKILL — main bundle
- `references/evidence-debt-buyer.md` — OEC 803(6) / 902(11)
  foundation analysis
- `references/rfp-debt-buyer.md` — RFP bank targeting chain
  of title
- `references/ucc-article-9.md` — UCC Article 9 for secured
  transactions
- `references/key-cases.md` — Oregon and federal precedents
  on chain of title
