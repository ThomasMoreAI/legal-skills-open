# Common Form 8300 Mistakes

Patterns the agent should watch for. Each is a real failure mode the IRS encounters in 8300 audits.

## Mistake 1: Treating personal checks as cash

**Pattern:** A customer writes a $25,000 personal check for a kitchen remodel down payment, and the contractor panic-files Form 8300.

**Why it's wrong:** Personal checks are explicitly **not** "cash" under IRC §6050I and 26 CFR §1.6050I-1(c)(1)(ii). Bank instruments tied to the payer's own account do not trigger the 8300 obligation — the bank's routine reporting (via separate BSA channels) is the system's coverage.

**Fix:** Re-read the cash definition. Only US currency, foreign currency, and certain monetary instruments **with face ≤ $10,000** in designated reporting transactions count. Wire transfers, ACH, credit/debit cards, and cashier's checks > $10,000 are also outside the definition.

**Agent action:** When a user describes a "large check," ask the type — personal vs. cashier's vs. money order — before applying the §6050I rule.

---

## Mistake 2: Missing the 15-day deadline

**Pattern:** A car dealer takes a $14,000 cash payment on April 1, intends to file, then forgets until tax season the following year.

**Why it's costly:** §6721 third-tier penalty kicks in once the filing is past August 1 — in 2025 dollars, ~$330 per missed filing minimum. If the IRS finds a pattern of missed filings, intentional-disregard exposure starts at $660+ per failure or 10% of cash, whichever is greater.

**Fix:** File the same week cash is received, never wait. Build a calendar reminder triggered the moment cash crosses the threshold. The 15-day clock is calendar days, not business days, but if Day 15 falls on a weekend or federal holiday, it rolls to the next business day.

**Agent action:** When producing a draft, always state the explicit deadline date and flag it loudly if the user is already past it.

---

## Mistake 3: Forgetting the customer notification

**Pattern:** The 8300 gets filed in March 2026. The customer notification due January 31, 2027 doesn't.

**Why it's costly:** IRC §6722 imposes a separate negligent-failure penalty (~$330 per recipient under current Rev. Proc., higher for intentional disregard). The customer-notification penalty is independently auditable and is one of the most common second-level findings in 8300 enforcement.

**Fix:** Treat the customer notification as part of the 8300 workflow. The moment an 8300 is submitted, queue a January 15-of-next-year reminder.

**Agent action:** Every 8300 deliverable must include the scheduled customer notification with the exact January 31 deadline date for the relevant year. Don't bury it in a footnote.

---

## Mistake 4: Failing to aggregate related payments

**Pattern:** A customer pays a contractor $6,000 cash on March 1, then $5,500 cash on April 25 for the same kitchen remodel. The contractor files nothing because no single payment hit $10K.

**Why it's wrong:** 26 CFR §1.6050I-1(b)(2) defines "related transactions" expansively — payments connected by a common project, contract, or relationship aggregate. Cumulative cash crossed $10,000 on April 25, triggering a 15-day clock from that date.

**Fix:** Track cumulative cash payments per buyer over rolling 12 months. The moment cumulative cash exceeds $10K, the threshold is crossed.

**Agent action:** When a user describes multiple payments, always ask for the cumulative total and the relationship between payments. Don't assume each payment is independent.

---

## Mistake 5: The cashier's-check/money-order trap

**Pattern:** A buyer pays for a $14,500 used motorcycle with three $5,000 money orders. The dealer thinks "each one is under $10K, no 8300 required."

**Why it's wrong:** Under 26 CFR §1.6050I-1(c)(1)(ii), monetary instruments with face ≤ $10,000 ARE cash for §6050I purposes when received in a "designated reporting transaction." A consumer durable retail sale (the motorcycle) is a designated reporting transaction. Aggregate $15,000 — file Form 8300.

**Fix:** When a buyer pays with multiple monetary instruments each under $10K for a consumer durable, collectible, or travel/entertainment activity, treat them as cash.

**Agent action:** If the user mentions money orders or cashier's checks, always ask (a) the face amount of each instrument and (b) what was being purchased. If a designated reporting transaction is involved, the under-$10K instruments count as cash.

---

## Mistake 6: Filing under intent-of-the-rule rather than the rule

**Pattern:** A small jeweler thinks "the rule is meant to catch criminals; I sell to local customers I trust, so I don't need to file."

**Why it's wrong:** §6050I applies to any trade or business receiving more than $10,000 in cash, regardless of trust, relationship, or perceived risk. The IRS reads "trade or business" expansively. Non-filing because the recipient subjectively trusts the buyer is not a defense.

**Fix:** File when the threshold is met, full stop. The rule is mechanical, not judgmental.

**Agent action:** Never accept "but it's a regular customer / friend / family member" as a reason not to file. The 8300 obligation is independent of the relationship.

---

## Mistake 7: Skipping ID collection and TIN capture

**Pattern:** A customer pays $13,000 cash for jewelry, but is in a rush. The store agrees to "collect the ID later." The customer never returns to provide it.

**Why it's wrong:** Form 8300 requires Part I identification including TIN and ID details. Filing without them is incomplete; not filing because the data is incomplete is non-filing — both lead to penalties.

**Fix:** Collect at the moment of payment, before the customer leaves with the goods. If the customer refuses to provide a TIN, file the 8300 with the TIN blank AND check the appropriate box documenting the refusal AND retain notes of the refusal in the file.

**Agent action:** If the user describes accepting a >$10K cash payment without ID/TIN collection, flag this immediately and recommend retroactive contact to collect — late ID collection is much harder than at-the-counter, and the 15-day clock is still ticking.

---

## Mistake 8: Paper filing without a hardship waiver

**Pattern:** A small business owner downloads the Form 8300 PDF, fills it out, and mails it to the IRS in 2026 without ever registering on BSA E-Filing.

**Why it's wrong:** Effective January 1, 2024, paper filing is non-compliant for almost every 8300 filer (26 CFR §301.6011-2). Without an active hardship waiver under 31 CFR §1010.306(e), paper filing itself triggers a penalty even if the substance is correct.

**Fix:** Register on https://bsaefiling.fincen.treas.gov/ before any 8300 obligation arises. Keep the account active. File electronically.

**Agent action:** When a user mentions paper filing, ask whether they have an active FinCEN hardship waiver. If no, redirect to the BSA E-Filing registration step before producing a deliverable.
