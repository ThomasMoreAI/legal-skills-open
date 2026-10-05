# Aggregation Rules: Single vs. Related Transactions

The $10,000 threshold is not always a single payment. The aggregation rules combine related payments into a single 8300 obligation. Use this reference whenever a customer has paid the business cash more than once.

## Statutory and regulatory basis

- **IRC §6050I(a)** — applies to "any person engaged in a trade or business … who, in the course of such trade or business, receives more than $10,000 in cash in 1 transaction (or 2 or more related transactions)."
- **26 CFR §1.6050I-1(b)(2)** — defines "related transactions" as "any transactions conducted between a payer (or its agent) and a recipient of cash in a 24-hour period," AND any transactions conducted within a longer period (typically up to 12 months) "if the recipient knows or has reason to know that each transaction is one of a series of connected transactions."

## The four aggregation scenarios

### Scenario 1 — Single transaction over $10,000

A buyer pays $14,500 cash for one item in one visit.

- **Threshold crossed:** at the moment of payment.
- **15-day clock starts:** date of receipt.
- **One Form 8300 filed.**

### Scenario 2 — Multiple payments for a single transaction (installments)

A buyer makes a $3,000 cash down payment, then $4,000 cash on day 60, then $4,500 cash on day 120 — all for the same item or service.

- **Threshold crossed:** on the third payment, when cumulative crosses $10,000 ($3,000 + $4,000 + $4,500 = $11,500 > $10,000).
- **15-day clock starts:** date of the payment that crosses the threshold (day 120 in this example).
- **One Form 8300 filed reporting the aggregate $11,500.**

If a fourth payment then comes in within the 12 months following the third — say another $5,000 cash — the obligation is to monitor whether *additional* cash from this buyer crosses $10,000 again. Until a new $10K aggregation triggers, no second 8300 is required.

### Scenario 3 — Series of connected transactions (24-hour rule)

A buyer makes multiple separate cash payments to the same recipient within a 24-hour period. Treasury Regulation §1.6050I-1(b)(2)(i) treats these as related transactions automatically — the recipient is presumed to know they're connected.

**Example.** A jewelry buyer pays $6,000 cash for a watch at 10am, then returns at 4pm and pays $5,500 cash for earrings. Both purchases are within 24 hours, both from the same recipient. Combined: $11,500. **File Form 8300.** The 15-day clock starts at the second payment.

### Scenario 4 — Series of connected transactions (longer than 24 hours)

For payments more than 24 hours apart, aggregation requires that the recipient "knows or has reason to know" the transactions are part of a connected series. The IRS interprets this expansively.

**Example.** A construction contractor takes a $4,500 cash deposit on March 1 for a kitchen remodel, then a $7,000 cash progress payment on April 15 for the same project. Both payments relate to the same job — the contractor has clear "reason to know" they are connected. Cumulative: $11,500. **File Form 8300 within 15 days of April 15.**

## The 12-month look-back

The IRS uses 12 months as a working window for "series of connected transactions" that aren't a single contractual project. Within 12 months, prior cash payments from the same buyer should be reviewed each time new cash comes in.

**Practical rule:** keep a per-buyer rolling sum of cash payments. When the rolling sum within 12 months exceeds $10,000, the threshold is crossed.

**Example.** A used-car dealer has the same buyer return repeatedly:

- Jan 15: cash deposit of $2,000 on a future vehicle purchase
- April 1: cash payment of $5,000 for accessories
- May 20: cash payment of $4,000 toward a different vehicle purchase

The dealer should aggregate these. By May 20, the cumulative cash from this buyer over 12 months = $11,000. **File Form 8300 within 15 days of May 20.**

If the three transactions are genuinely unrelated (different items, different occasions, no contractual link), the dealer may have a defense against aggregation. But the conservative posture is to aggregate when the same buyer crosses $10,000 cumulative cash.

## After the first 8300 is filed

Once an 8300 has been filed for a buyer, **subsequent cash payments from the same buyer that themselves total more than $10,000 within the next 12 months trigger a new 8300.** The clock resets after each filing.

**Example.** Hector files an 8300 on April 16 for Maria's $14,500 vehicle purchase. In June, Maria returns and pays $11,000 cash for a different car. A new, separate 8300 is required for the June transaction (15 days from receipt). The April filing does not "cover" June.

## When NOT to aggregate

Aggregation does not apply across these boundaries:

- **Different recipients.** Two different LLCs owned by the same person are separate recipients (unless they're a single legal entity); each tracks its own threshold.
- **Different payers.** If Maria pays $6,000 cash and her separate friend John (acting independently) pays $5,000 cash, these are not aggregated even if for related items.
- **Refunded transactions.** A cash payment that was fully refunded to the buyer in good faith is treated as not received for §6050I purposes — but document the refund carefully.

## Edge case: Part II (third-party payer)

If an employee, agent, or relative pays cash on behalf of someone else, aggregation runs against the **principal in Part II**, not the person handing over the cash. The recipient business should track totals against the principal whose name appears on Part II.

## Documentation requirements for aggregation

Whenever aggregation is the basis of the filing, retain:

- Receipts or records of every individual payment that was aggregated
- Notes connecting the payments (matter file, project name, vehicle VIN, customer ID)
- The date and amount when cumulative cash crossed $10,000 — this is the date you write on Line 27 of Form 8300

## When to ask the user

The agent should ask explicitly:

- "Has this same buyer paid your business cash before in the past 12 months?"
- "Are these payments connected — same project, same item, same matter — or independent?"
- "Did all payments come from the same buyer, or from different people on behalf of one principal?"

Don't assume aggregation when the user mentions only one transaction. But always ask, because most aggregation failures come from the recipient never having considered prior payments at all.
