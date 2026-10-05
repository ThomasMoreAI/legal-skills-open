---
name: form-8300-jupid-tax
title: Form 8300 — Report of Cash Payments Over $10,000 Received in a Trade or Business
description: 'Use this skill when a trade or business has received more than $10,000 in cash from one buyer in a single transaction or related transactions, and must file Form 8300 with IRS + FinCEN within 15 days. Triggers: "received over $10,000 cash", "Form 8300 filing", "report cash payment to IRS", "BSA E-Filing", "do I have to report cash", "customer paid cash".


  Do NOT use for: bank deposits over $10K (banks file CTR — different form), suspicious activity reports (SAR — banks only), individual non-business cash receipts (gifts, inheritances).'
author: jupid-tax
author_url: https://github.com/jupid-tax/jupid-skills/tree/main/forms/form-8300
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
sources:
- title: Aggregation Rules
  path: references/aggregation-rules.md
- title: Bsa E Filing
  path: references/bsa-e-filing.md
- title: Cash Definition
  path: references/cash-definition.md
- title: Common Mistakes
  path: references/common-mistakes.md
- title: Customer Notification
  path: references/customer-notification.md
- title: Penalties
  path: references/penalties.md
---

# Form 8300 — Report of Cash Payments Over $10,000 Received in a Trade or Business

This skill produces an audit-grade draft of Form 8300 from the user's transaction facts. It walks through the cash definition, applies the aggregation rules, fills Parts I–IV, validates the result, and emits a deliverable the user can transcribe into the FinCEN BSA E-Filing System with confidence.

The form itself is short (two pages, four parts). The judgment is in *whether the threshold was actually crossed* and *what counts as cash*. This skill optimizes for the latter — the agent should ask, not guess.

**Companion guide for end users:** [Form 8300 (2026): Reporting Cash Over $10,000 in Business](https://jupid.com/blog/form-8300-cash-payments-over-10000-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 8300, "8300", "BSA E-Filing", "FinCEN cash report", or §6050I
- The user describes a customer paying their business more than $10,000 in cash, in a single transaction OR a series of related transactions
- The user runs one of the high-frequency 8300 trades — used/new car dealer, jeweler, attorney, real estate broker, contractor, bail bondsman, art dealer, pawnbroker, boat/RV/aircraft dealer, wedding venue/caterer — and asks about cash compliance
- The user asks "do I have to report this cash" or "what do I file when someone pays cash"
- The user describes a customer paying with multiple money orders or cashier's checks for a consumer durable, collectible, or travel/entertainment

Do **not** engage this skill when:

- The user is a bank or financial institution → they file FinCEN Currency Transaction Reports (CTR / FinCEN Form 104), not Form 8300
- The user is a casino → they file FinCEN Form 8852, not Form 8300
- The user wants to file a Suspicious Activity Report (SAR) → that is a separate FinCEN form, only filed by financial institutions and limited other categories
- The user received cash as a gift, inheritance, or personal transaction outside a trade or business → §6050I does not apply
- The user is making a personal cash deposit at their bank → the bank handles CTR reporting; the depositor files nothing

If the user's situation is ambiguous (e.g., a sole proprietor who occasionally takes cash but isn't sure their activity rises to a "trade or business"), ask before proceeding. The IRS reads "trade or business" expansively — operating regularly with a profit motive almost always qualifies.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **The transaction trigger.** What did the customer pay, when, in what form (currency / cashier's check / money order / mixed)? Was it one payment or multiple?
2. **Buyer identity.** Full legal name, current mailing address, date of birth, occupation, and TIN (SSN or ITIN). For a non-resident with no TIN, capture passport details and country of issuance.
3. **Government-issued ID.** Type (driver's license, passport, state ID, alien registration), document number, issuing state/country. The agent should confirm the user has a photocopy or scan stored.
4. **Person on whose behalf** (if different from the buyer in the room). If an employee is paying on behalf of a company, or one spouse is paying for the other, Part II applies. Ask explicitly: "Is the person who handed you the cash buying for themselves, or for someone else?"
5. **Transaction details.** Date cash was received (or date the threshold was crossed for aggregated payments). Total cash amount. Amount in $100 bills or higher denominations. Item or service description (VIN for vehicles, matter description for legal services, project description for contractors).
6. **Filing business identity.** Business legal name, EIN, address, nature of business, and the name of the individual employee who handled the transaction.
7. **Aggregation history.** Has this same buyer paid the business cash before in the past 12 months? If so, total amount and dates of prior payments. The 12-month look-back is required to determine whether the threshold was crossed on this payment or earlier.
8. **BSA E-Filing account status.** Does the business already have a registered BSA E-Filing account with a Supervisory User? If not, registration is a prerequisite — see [`filing.md`](./filing.md).

For payment-method edge cases, additionally ask:

- If a cashier's check or money order was used: face amount of each instrument and whether the transaction was a "designated reporting transaction" (sale of consumer durable, collectible, or travel/entertainment). See [`references/cash-definition.md`](./references/cash-definition.md).
- If the buyer paid in foreign currency: the USD equivalent at the date of receipt.
- If the buyer paid using a mix of cash and other instruments: a breakdown of every component.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm the cash threshold actually triggered

Apply the §6050I cash definition strictly. **Personal checks, wire transfers, ACH, credit cards, and debit cards are NOT cash for Form 8300 purposes.** A customer paying you $50,000 by personal check triggers no 8300 obligation.

What IS cash:

- US currency and coins
- Foreign currency (convert to USD at the date of receipt)
- Cashier's checks, money orders, traveler's checks, and bank drafts **with face amounts of $10,000 or less** AND received in either (a) a designated reporting transaction (consumer durable / collectible / travel-or-entertainment retail sale) or (b) a transaction where the recipient knows the payer is structuring to evade reporting

Cashier's checks, money orders, and bank drafts with face amounts **over $10,000** are NOT cash for Form 8300 — the issuing bank already filed a CTR when the customer purchased the instrument.

If the cash definition is not met, stop. Do not file an 8300.

Full reference: [`references/cash-definition.md`](./references/cash-definition.md).

### Step 2 — Apply the aggregation rules

Sum all cash payments from the same buyer to the same business across:

- A single transaction
- Multiple payments for a single transaction (installments)
- A series of connected transactions within 12 months that the recipient knows or has reason to know are connected

If the cumulative cash exceeds $10,000 on the *current* payment, the 15-day clock starts on the date of the current payment.

If the cumulative was *already* over $10,000 from prior reportable filings within the last 12 months, a new 8300 is triggered when *additional* cash from the same buyer itself crosses $10,000.

Full reference: [`references/aggregation-rules.md`](./references/aggregation-rules.md).

### Step 3 — Confirm the 15-day deadline date

Filing deadline = the **15th day after** the date of receipt (or the date the threshold was crossed for aggregated payments). If the 15th day falls on a weekend or federal holiday, the deadline rolls to the next business day. State the deadline date explicitly in the deliverable.

### Step 4 — Collect Part I (and Part II) identification data

For Part I (the person from whom cash was received):

- Last name, first name, middle initial
- TIN (SSN or ITIN; for non-resident with neither, capture passport country and number in the alien-ID fields)
- Address (number, street, apt/suite, city, state, ZIP)
- Date of birth
- Occupation, profession, or business
- Government-issued ID document — type, number, issuing authority

For Part II (the principal on whose behalf the transaction was conducted), if applicable: same fields. If the Part I person is buying for themselves, Part II is left blank or marked "same as Part I."

If multiple individuals delivered cash for a single transaction (e.g., joint buyers of a vehicle), Part I has space for only one — file an additional Form 8300 or attach a written statement listing the others. Ask the user which individuals were physically present.

### Step 5 — Fill Part III (Description of Transaction and Method of Payment)

- Date cash received (or the date of the payment that crossed the threshold)
- Total cash received in USD
- Total amount in $100 bills or higher denominations (counted separately to flag potential structuring)
- Whether more than one payment is being reported
- Identification of the payment instrument(s): currency / foreign currency / cashier's check / money order / bank draft / traveler's check; for monetary instruments, capture issuer and serial number
- Type of transaction: personal property purchased / real property purchased / personal services / business services / intangible property / debt obligation / exchange of cash / escrow or trust / bail received / other
- Specific description: free-text describing the item or service (VIN, legal matter, project, etc.)

### Step 6 — Fill Part IV (Business That Received Cash)

- Business name (legal entity name)
- EIN
- Business address
- Nature of business (use NAICS-style description: "Used motor vehicle dealer", "Law firm — family law", etc.)
- Name of individual employee who handled the cash receipt
- Phone number
- Signature and date (digital for e-filing)

### Step 7 — Run validation checks

See **Validation** below. Run every check. Don't skip checks even if the math looks clean.

### Step 8 — Produce the deliverable

See **Output format** below.

### Step 9 — Schedule the customer notification

The customer notification under IRC §6722 is due **January 31 of the year following the filing year**. Always include this in the deliverable as a scheduled follow-up. The notification is a separate, independently penalized obligation. Reference: [`references/customer-notification.md`](./references/customer-notification.md).

### Step 10 — Hand off downstream

State the next steps the user must take:

- **File via BSA E-Filing within 15 days** — see [`filing.md`](./filing.md) for the field-by-field flow
- **Save the BSA tracking ID** displayed on submission — required record retention
- **Photocopy the customer's ID** if not already on file (5-year retention)
- **Schedule customer notification for January 31 of next year**
- **Retain all 8300 records, supporting documents, and notification proof for 5 years**

### Step 11 — File the return (optional, if the user wants the agent to file)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- BSA E-Filing System login flow and field-by-field mapping
- Hardship-waiver path for paper filing
- Submission state machine (Submitted → Acknowledged → Tracking ID issued)
- Security rules — never email or text the 8300 with SSN visible; encrypt at rest

If the user only wants a draft and will file themselves, skip this step.

---

## Critical ask-don't-guess rules

These rules exist because the wrong default looks like a working answer until the IRS audit reveals the misclassification.

1. **If the user mentions a "money order" or "cashier's check," ASK whether the face amount of the single instrument is over or under $10,000, AND whether the underlying transaction is a designated reporting transaction (consumer durable, collectible, or travel/entertainment).** A money order or cashier's check with face <$10,000 is *only* "cash" under §6050I if the transaction is a designated reporting transaction or the recipient knows the buyer is structuring. A cashier's check with face >$10,000 is never "cash" for Form 8300 (the bank already filed a CTR).
2. **If the user describes multiple payments from the same buyer, ASK for the cumulative cash total within the past 12 months.** The aggregation rule only triggers once cumulative cash exceeds $10,000. Don't assume a single $11,000 deposit is the trigger if the buyer also paid $5,000 cash three months ago.
3. **NEVER assume "cash" includes a personal check.** Personal checks are explicitly excluded from the §6050I definition regardless of amount. A $50,000 personal check is not reportable on Form 8300 (the bank may report on suspicious-activity grounds, but that is a separate filing the bank initiates).
4. **NEVER assume the buyer in the room is the principal.** If the cash was delivered by an employee, agent, attorney, or relative, Part II applies — ask explicitly who the goods or services are for.
5. **If the user has not registered a BSA E-Filing account, do not skip ahead to filing instructions.** Registration is a prerequisite and takes its own time. Surface this gap before producing the field-by-field draft.
6. **If the user wants to file on paper to avoid e-filing setup, ASK whether they have an active hardship waiver from FinCEN under 31 CFR §1010.306(e).** Without a waiver, paper filing has been non-compliant since January 1, 2024 and itself triggers a penalty.

---

## Line-by-line guidance

### Header (top of form)

- **Box 1a (multiple parties)** — Check if more than one person handed cash for this transaction. Required when joint buyers paid together.
- **Box 1b (suspicious transaction)** — Check if the business has reason to suspect the cash payment is part of structuring or other illicit activity. Checking this box does not change the filing deadline but flags the report for FinCEN attention.
- **Amendment box** — Check only if amending a previously filed 8300. Reference the BSA tracking ID of the original.

### Part I — Identity of Individual From Whom the Cash Was Received

| Field | What to enter | Source from user |
|-------|---------------|------------------|
| Last name | Buyer's legal last name | Government ID |
| First name | Buyer's legal first name | Government ID |
| M.I. | Middle initial if any | Government ID |
| TIN | SSN (9 digits) or ITIN | Bill of sale or buyer-provided |
| Address | Number, street, apt/suite | Government ID |
| City, state, ZIP | | Government ID |
| Country (if non-US) | | Passport |
| DOB | MM/DD/YYYY | Government ID |
| Occupation | Buyer's profession | Bill of sale or buyer-stated |
| ID type/number | "Driver's license" / "Passport" / etc., document number, issuing state or country | Photocopy on file |

If the buyer refuses to provide a TIN, the form still must be filed with the TIN field left blank — but the business must indicate why on Box 1c and is exposed to a separate "missing TIN" penalty under §6722. Ask the user whether the TIN was actually obtained or refused.

### Part II — Person on Whose Behalf This Transaction Was Conducted

Same field set as Part I. Used only when the Part I person is acting for someone else. Common cases:

- An employee of a corporation paying for goods purchased by the corporation (Part II = the corporation)
- A relative paying on behalf of another household member
- An attorney paying on behalf of a client (e.g., bail or settlement disbursement)

If Part II applies, the agent should also ask whether the principal in Part II has a TIN — this is required.

### Part III — Description of Transaction and Method of Payment

| Field | What to enter |
|-------|---------------|
| 27 — Date cash received | Date of payment (or date threshold crossed for aggregated cases) |
| 28 — Total cash received | Sum in USD |
| 29 — Total in $100s or higher | Subset of Line 28 paid in $100 bills, $500s, or larger denominations (rare) |
| 30 — More than one cash transaction | Yes if reporting multiple payments aggregating to >$10K; otherwise No |
| 31 — Identification of payment | Currency / foreign currency / cashier's check / money order / bank draft / traveler's check (with issuer and serial number for non-currency) |
| 32 — Type of transaction | Check exactly one box from the predefined list |
| 33 — Specific description | Free text — VIN, item, matter description |

### Part IV — Business That Received Cash

| Field | What to enter |
|-------|---------------|
| 34 — Business name | Legal name of the entity |
| 35 — EIN | 9 digits |
| 36 — Address | Business address |
| 37 — Nature of business | Plain-language description |
| 38 — Individual who handled | Name of the employee or owner who took the cash |
| 39 — Title | Their title |
| 40 — Date signed | Date the form is signed |
| 41 — Phone | Business phone |

For e-filing, the signature is captured digitally inside the BSA E-Filing System.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Threshold and definition checks

- [ ] Total cash (Line 28) is **strictly greater than** $10,000. Exactly $10,000 does not trigger 8300 — the statute reads "more than $10,000."
- [ ] Every payment instrument counted toward the total fits the §6050I "cash" definition. Personal checks, wires, ACH, credit/debit cards excluded.
- [ ] If any cashier's check or money order is included, the underlying transaction is a designated reporting transaction OR the business knows the buyer is structuring. If neither, the instrument is not cash and should be removed from the total.
- [ ] If multiple payments are aggregated, all payments are from the same buyer to the same business within 12 months.

### Identification checks

- [ ] Buyer's TIN is present, OR Box 1c is checked indicating refusal/missing TIN with a reason captured.
- [ ] Date of birth is present and in MM/DD/YYYY format.
- [ ] At least one government-issued ID type, number, and issuing authority captured.
- [ ] If multiple buyers physically delivered cash, Box 1a is checked AND additional names are listed (additional 8300 or attached statement).
- [ ] If the Part I person is paying on behalf of someone else, Part II is filled with the principal's identity AND TIN.

### Deadline check

- [ ] 15-day deadline calculated from the date in Line 27. Deadline rolls forward if it falls on a weekend or federal holiday.
- [ ] Deadline is in the future at time of draft. If it is already past, surface this loudly — the filing is late and a penalty has accrued.

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Line 29 (high-denomination bills) is $0 but Line 28 is large — possibly an oversight; ask user to confirm the denomination breakdown.
- [ ] Line 28 is suspiciously round and close to threshold (e.g., $10,001) — could be structuring; consider whether Box 1b should be checked.
- [ ] Buyer's address is a PO Box — IRS prefers a residential or business address; capture both if available.
- [ ] Buyer refused to provide a TIN — this is reportable but raises an audit flag; document the refusal.
- [ ] The transaction is the third or fourth 8300 from the same buyer in 12 months — pattern that may warrant Box 1b (suspicious transaction).

### Cross-form checks

- [ ] Customer notification scheduled for January 31 of the year following filing.
- [ ] BSA E-Filing account exists OR registration step added to the deliverable.
- [ ] Document retention plan in place — bill of sale, ID copies, BSA tracking ID, notification proof — 5-year retention.

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe into the BSA E-Filing System. Format:

```markdown
# Form 8300 — DRAFT for filing year YYYY

## Filing context
- Date cash received: MM/DD/YYYY
- 15-day filing deadline: MM/DD/YYYY (state weekend/holiday rollover if any)
- BSA E-Filing account status: <registered / needs registration>

## Header boxes
1a. Multiple parties: <Yes / No>
1b. Suspicious transaction: <Yes / No>
Amendment to prior 8300: <Yes / No>  (if Yes, prior BSA tracking ID: ...)

## Part I — Identity of Individual From Whom Cash Was Received
Last name:        <name>
First name:       <name>
M.I.:             <initial>
TIN (SSN/ITIN):   <xxx-xx-xxxx>
Address:          <street, city, state, ZIP>
Country:          <if non-US>
DOB:              MM/DD/YYYY
Occupation:       <profession>
ID type:          <Driver's license / Passport / etc.>
ID number:        <document number>
Issuing authority: <state or country>

## Part II — Person on Whose Behalf
<filled if applicable, otherwise "N/A — Part I person is the principal">

## Part III — Description of Transaction
27. Date cash received:                  MM/DD/YYYY
28. Total cash received:                 $X,XXX
29. Amount in $100 bills or higher:      $X,XXX
30. More than one cash transaction:      Yes | No
31. Method of payment:
    - Currency: $X,XXX
    - Foreign currency: $X,XXX (USD equivalent)
    - Cashier's check: <issuer, serial #, amount>
    - Money order: <issuer, serial #, amount>
    - Bank draft: <issuer, serial #, amount>
    - Traveler's check: <issuer, serial #, amount>
32. Type of transaction: <one of the predefined boxes>
33. Specific description: <free text>

## Part IV — Business That Received Cash
34. Business name:                       <legal name>
35. EIN:                                 XX-XXXXXXX
36. Address:                             <street, city, state, ZIP>
37. Nature of business:                  <description>
38. Individual who handled:              <name>
39. Title:                               <title>
40. Date signed:                         MM/DD/YYYY
41. Phone:                               (XXX) XXX-XXXX

## Required follow-ups
- [ ] File via FinCEN BSA E-Filing System (https://bsaefiling.fincen.treas.gov/) by MM/DD/YYYY
- [ ] Capture and save BSA tracking ID
- [ ] Save PDF copy with customer file (5-year retention)
- [ ] Send customer notification by January 31, YYYY (year after filing)
- [ ] Retain ID copies, bill of sale, and BSA tracking ID for 5 years

## Validation summary
- Threshold: passed | <list failures>
- Identification: passed | <list failures>
- Deadline: <date>; status: future | past
- Sanity warnings: <list any warnings raised>

## Sources cited in this draft
- IRC §6050I (cash receipts in trade or business)
- 31 USC §5331 (BSA cash reporting)
- 26 CFR §1.6050I-1 (regulatory definitions)
- 26 CFR §301.6011-2 (mandatory e-filing effective Jan 1, 2024)
- IRS Form 8300 (current revision)
- IRS Publication 1544
- Rev. Proc. <year> (current penalty inflation adjustments)
```

The draft is **not** the filed form. The user (or the agent, with explicit authorization) still has to enter it into BSA E-Filing. The deliverable's value is that every field is computed, every rule applied, and the customer-notification follow-up is scheduled before it falls through the cracks.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/cash-definition.md`](./references/cash-definition.md) — IRC §6050I "cash" definition, designated reporting transactions, what counts and what doesn't
- [`references/aggregation-rules.md`](./references/aggregation-rules.md) — Single vs. related transactions, 12-month look-back, installment payment timing
- [`references/customer-notification.md`](./references/customer-notification.md) — January 31 deadline, Pub 1544 model letter, §6722 penalty exposure
- [`references/penalties.md`](./references/penalties.md) — $310 base, intentional disregard tiers, criminal exposure for structuring
- [`references/bsa-e-filing.md`](./references/bsa-e-filing.md) — FinCEN BSA E-Filing System overview, account registration, BSA tracking IDs
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Frequent 8300 filer errors with fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for the BSA E-Filing System, field-by-field map, hardship-waiver path

## Examples

End-to-end worked Form 8300s. Use these as patterns when the user's situation is similar.

- [`examples/car-dealer-single-transaction.md`](./examples/car-dealer-single-transaction.md) — Used car dealer Hector receives $14,500 cash for a single vehicle sale
- [`examples/service-business-aggregating-payments.md`](./examples/service-business-aggregating-payments.md) — Contractor receives multiple cash deposits aggregating to $11,000 across a project
- [`examples/attorney-receiving-retainer.md`](./examples/attorney-receiving-retainer.md) — Attorney receives a $25,000 cash retainer delivered by a third party on behalf of a client

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS and FinCEN sites for the year being filed — penalty amounts adjust annually under inflation Rev. Procs.

- [Form 8300 (2026): Reporting Cash Over $10,000 in Business](https://jupid.com/blog/form-8300-cash-payments-over-10000-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 8300 (latest)](https://www.irs.gov/pub/irs-pdf/f8300.pdf) — the form itself
- [Instructions for Form 8300 (latest)](https://www.irs.gov/pub/irs-pdf/i8300.pdf) — line-by-line IRS guidance
- [About Form 8300](https://www.irs.gov/forms-pubs/about-form-8300) — IRS landing page with current revisions
- [Publication 1544](https://www.irs.gov/pub/irs-pdf/p1544.pdf) — Reporting Cash Payments of Over $10,000
- [FinCEN BSA E-Filing System](https://bsaefiling.fincen.treas.gov/) — mandatory filing channel since 2024
- [FinCEN Form 8300 guidance](https://www.fincen.gov/resources/statutes-regulations/guidance/form-8300-information-trades-businesses)
- IRC §6050I (information reporting on cash transactions in a trade or business)
- 31 USC §5331 (BSA reporting of cash receipts in nonfinancial trades or businesses)
- IRC §6721 (failure-to-file information return penalties)
- IRC §6722 (failure to furnish payee statement — covers customer notification)
- 26 CFR §1.6050I-1 (Treasury Regulations defining cash, related transactions, designated reporting transactions)
- 26 CFR §301.6011-2 (mandatory e-filing of information returns, effective Jan 1, 2024)
- 31 CFR §1010.306(e) (FinCEN hardship-waiver standard for paper filing)
- 31 CFR Chapter X (FinCEN BSA regulations)
- Rev. Proc. 2024-40 — inflation-adjusted penalty amounts for tax year 2025; verify the current-year Rev. Proc. before filing

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS and FinCEN forms, publications, and regulations. It is not tax or legal advice. It does not establish a CPA-client or attorney-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that high-volume cash businesses or unusual fact patterns warrant a licensed tax professional or AML/BSA compliance specialist's review.
