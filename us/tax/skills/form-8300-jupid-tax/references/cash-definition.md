# What Counts as "Cash" for Form 8300

The §6050I definition of "cash" is **wider** than ordinary English. This is the single most-misunderstood rule on the form. Use this reference whenever a user describes a payment instrument that isn't pure currency.

## Statutory and regulatory basis

- **IRC §6050I(d)** — defines "cash" as "United States and foreign coin and currency" plus, "to the extent provided in regulations prescribed by the Secretary, any monetary instrument."
- **26 CFR §1.6050I-1(c)(1)(ii)** — extends "cash" to include cashier's checks, bank drafts, traveler's checks, and money orders **with face amounts of $10,000 or less** when received in a "designated reporting transaction" or in a transaction where the recipient knows the payer is structuring to avoid reporting.

## What IS cash for Form 8300

| Instrument | Counts as cash? | Conditions |
|------------|-----------------|------------|
| US currency (paper bills) | Yes | Always |
| US coin | Yes | Always |
| Foreign currency | Yes | Convert to USD at date of receipt |
| Cashier's check, face ≤ $10,000 | Yes | Only in designated reporting transactions OR if recipient knows of structuring |
| Money order, face ≤ $10,000 | Yes | Same condition |
| Bank draft, face ≤ $10,000 | Yes | Same condition |
| Traveler's check, face ≤ $10,000 | Yes | Same condition |

## What is NOT cash for Form 8300

| Instrument | Counts as cash? | Why |
|------------|-----------------|-----|
| Personal check (any amount) | **No** | Bank already tracks via routine processes; not in §6050I definition |
| Wire transfer | **No** | Bank reports to FinCEN under separate BSA rules |
| ACH transfer | **No** | Same as wire |
| Credit card payment | **No** | Card network and issuer track these |
| Debit card payment | **No** | Same as credit card |
| Cashier's check, face > $10,000 | **No** | Issuing bank already filed a CTR when buyer purchased the instrument |
| Money order, face > $10,000 | **No** | Same — the bank that issued already reported |
| Bank draft, face > $10,000 | **No** | Same |
| Cryptocurrency (BTC, ETH, stablecoins) | **Currently no for §6050I purposes** | Treasury proposed rules in 2022 to extend reporting to digital assets, but as of 2026 no implementing regulation has been finalized. Verify current status before applying. |
| Promissory notes | **No** | Not a monetary instrument under the regulation |
| Goods bartered in trade | **No** | Not currency or a monetary instrument |

## Designated reporting transactions

A "designated reporting transaction" is a retail sale of any of the following — and is the trigger that converts sub-$10K monetary instruments into "cash" under §6050I:

1. **Consumer durable** — an item of tangible personal property generally suitable for personal use, expected to last at least one year, and with a sales price of more than $10,000. Examples: cars, motorcycles, boats, trailers, jewelry, watches, fine art.
2. **Collectible** — items defined in IRC §408(m)(2): art, antiques, metals or gems, stamps, coins, alcoholic beverages held as collectibles, and similar tangible personal property held for investment.
3. **Travel or entertainment activity** — a single trip or entertainment event with a sales price of more than $10,000. Examples: cruises, foreign tour packages, charter flights, concert tour packages.

Key tests for the designated-reporting-transaction status:

- The sale must be a **retail** sale to an **end-user** (not wholesale, not for resale)
- The item or activity must have a sales price exceeding $10,000

## The cashier's-check trap

The most common 8300 misclassification:

**Wrong:** "The customer paid for the $14,000 used motorcycle with three $5,000 money orders. Each money order is under $10,000 so I don't have to file."

**Right:** Each individual money order is under $10,000, but the motorcycle is a consumer durable (designated reporting transaction). Under 26 CFR §1.6050I-1(c)(1)(ii), the money orders ARE cash for §6050I purposes. The aggregate $15,000 ($5,000 × 3) crosses $10,000. File Form 8300.

By contrast:

**Right:** "The customer paid for the $14,000 used motorcycle with one cashier's check for $14,000."

The cashier's check exceeds $10,000 face. The bank that issued it already filed a CTR when the customer paid cash for it. The dealer does **not** file Form 8300.

## Mixed payments

When a buyer pays with a mix of currency and instruments, evaluate each component separately and sum only the components that meet the §6050I definition of cash.

**Example.** A buyer pays $8,000 in $100 bills + $5,000 personal check + $3,000 cashier's check (face) for a $16,000 used car.

- Currency: $8,000 — IS cash
- Personal check: $5,000 — NOT cash
- Cashier's check $3,000: face ≤ $10,000, used in a consumer-durable retail sale (designated reporting transaction) — IS cash

Cash for §6050I = $8,000 + $3,000 = $11,000. Threshold crossed. **File Form 8300.**

## Foreign currency conversion

Convert foreign currency to USD at the spot rate on the date of receipt. The Treasury reporting rate or the customer's bank conversion rate are both acceptable; document the rate used. Note the original foreign currency and the USD equivalent on Line 31.

## When in doubt

If the §6050I status of an instrument is unclear:

1. Consult the IRS Form 8300 Instructions and Pub 1544 for the current revision
2. For unusual cases (e.g., crypto, prepaid debit cards, prepaid gift cards), check whether Treasury has issued guidance or a pending Notice of Proposed Rulemaking
3. When the answer is genuinely ambiguous and the dollar amount is high, file the report. A "defensive" 8300 carries no penalty if the threshold turned out not to be crossed; failing to file when it was is the costly direction.
