# What Counts as "Cash" for Form 8300

The §6050I definition of "cash" is **wider** than ordinary English. This is the single most-misunderstood rule on the form. Use this reference whenever a user describes a payment instrument that isn't pure currency.

## Statutory and regulatory basis

- **IRC §6050I(d)** — "cash" includes foreign currency; "to the extent provided in regulations prescribed by the Secretary, any monetary instrument (whether or not in bearer form) with a face amount of not more than $10,000"; and any digital asset (paragraph (3), added by the Infrastructure Investment and Jobs Act). A check drawn on the writer's own account is excluded.
- **26 CFR §1.6050I-1(c)(1)(ii)(B)** — extends "cash" to include cashier's checks, bank drafts, traveler's checks, and money orders **with face amounts of $10,000 or less** when received in a "designated reporting transaction" or in a transaction where the recipient knows the instrument is being used to avoid reporting.

## What IS cash for Form 8300

| Instrument | Counts as cash? | Conditions |
|------------|-----------------|------------|
| US currency (paper bills) | Yes | Always |
| US coin | Yes | Always |
| Foreign currency | Yes | Report the U.S. dollar equivalent at a fair market rate of exchange available to the public |
| Cashier's check, face ≤ $10,000 | Yes | Only in designated reporting transactions OR if recipient knows of structuring |
| Money order, face ≤ $10,000 | Yes | Same condition |
| Bank draft, face ≤ $10,000 | Yes | Same condition |
| Traveler's check, face ≤ $10,000 | Yes | Same condition |

## What is NOT cash for Form 8300

| Instrument | Counts as cash? | Why |
|------------|-----------------|-----|
| Personal check (any amount) | **No** | A check drawn on the payer's own account is excluded by §6050I(d) and the Form 8300 instructions |
| Wire transfer | **No** | Bank reports to FinCEN under separate BSA rules |
| ACH transfer | **No** | Same as wire |
| Credit card payment | **No** | Card network and issuer track these |
| Debit card payment | **No** | Same as credit card |
| Cashier's check, face > $10,000 | **No** | Outside the definition; if bought with currency, the issuing bank must file its own currency transaction report (Pub 1544) |
| Money order, face > $10,000 | **No** | Same |
| Bank draft or traveler's check, face > $10,000 | **No** | Same |
| Cashier's check, bank draft, traveler's check, or money order that is the proceeds of a bank loan, or a payment on certain promissory notes, installment sales contracts, or down payment plans | **No** | Exceptions in 26 CFR §1.6050I-1(c)(1)(iv)–(vi) and Pub 1544 |
| Digital assets (BTC, ETH, stablecoins) | **Not counted for now** | IRC §6050I(d)(3) adds digital assets to "cash" for returns required to be filed after December 31, 2023, but IRS Announcement 2024-4 says businesses do not have to include digital assets when testing the $10,000 threshold until Treasury and the IRS issue regulations. Verify current status before applying. |
| Promissory notes | **No** | Not a monetary instrument under the regulation |
| Goods bartered in trade | **No** | Not currency or a monetary instrument |

## Designated reporting transactions

A "designated reporting transaction" is a retail sale of any of the following — and is the trigger that converts sub-$10K monetary instruments into "cash" under §6050I:

1. **Consumer durable** — an item of tangible personal property of a type suitable under ordinary usage for personal consumption or use, reasonably expected to be useful for at least 1 year, and with a sales price of more than $10,000. Examples: cars, motorcycles, boats, jewelry, watches. A $20,000 automobile is a consumer durable even if sold for business use; a $20,000 dump truck or factory machine is not (26 CFR §1.6050I-1(c)(2)).
2. **Collectible** — items described in IRC §408(m)(2)(A)–(D): any work of art, rug or antique, metal or gem, stamp or coin (26 CFR §1.6050I-1(c)(3)).
3. **Travel or entertainment activity** — an item of travel or entertainment pertaining to a single trip or event, where the combined sales price of all items for that trip or event sold in the same or related transactions exceeds $10,000. Examples: cruises, foreign tour packages, charter flights.

Key tests for the designated-reporting-transaction status:

- The sale must be a **retail sale**: any sale (whether or not for resale) made in the course of a trade or business that principally consists of making sales to ultimate consumers (Form 8300 instructions, Definitions). Receipt of funds by a broker or other intermediary in connection with a retail sale also counts.
- A consumer durable or travel/entertainment item must have a sales price exceeding $10,000

## The cashier's-check trap

The most common 8300 misclassification:

**Wrong:** "The customer paid for the $14,000 used motorcycle with three $5,000 money orders. Each money order is under $10,000 so I don't have to file."

**Right:** Each individual money order is under $10,000, but the motorcycle is a consumer durable (designated reporting transaction). Under 26 CFR §1.6050I-1(c)(1)(ii)(B), the money orders ARE cash for §6050I purposes. The aggregate $15,000 ($5,000 × 3) crosses $10,000. File Form 8300.

By contrast:

**Right:** "The customer paid for the $14,000 used motorcycle with one cashier's check for $14,000."

The cashier's check exceeds $10,000 face, so it is not cash for Form 8300 (Pub 1544 explains that the issuing bank must report it if it was bought with currency). The dealer does **not** file Form 8300.

## Mixed payments

When a buyer pays with a mix of currency and instruments, evaluate each component separately and sum only the components that meet the §6050I definition of cash.

**Example.** A buyer pays $8,000 in $100 bills + $5,000 personal check + $3,000 cashier's check (face) for a $16,000 used car.

- Currency: $8,000 — IS cash
- Personal check: $5,000 — NOT cash
- Cashier's check $3,000: face ≤ $10,000, used in a consumer-durable retail sale (designated reporting transaction) — IS cash

Cash for §6050I = $8,000 + $3,000 = $11,000. Threshold crossed. **File Form 8300.**

## Foreign currency conversion

Show foreign currency in U.S. dollar equivalent at a fair market rate of exchange available to the public (Form 8300 instructions, item 32). Document the rate and its source. Enter the USD equivalent on item 32b with the country, and include it in the item 29 total.

## When in doubt

If the §6050I status of an instrument is unclear:

1. Consult the IRS Form 8300 Instructions (Rev. December 2023) and Pub 1544 (Rev. September 2014)
2. For unusual cases (e.g., crypto, prepaid debit cards, prepaid gift cards), check whether Treasury has issued guidance or a pending Notice of Proposed Rulemaking
3. When the answer is genuinely ambiguous and the dollar amount is high, ask the user to consult a CPA or BSA specialist; the instructions allow a voluntary Form 8300 for a suspicious transaction even at $10,000 or less. Failing to file when it was required is the costly direction.
