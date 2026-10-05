# Form 8300 Penalties

Penalty exposure on Form 8300 has three layers: civil failure-to-file (negligent), civil intentional disregard, and criminal. The civil amounts adjust annually under inflation Rev. Procs.; the criminal exposure is statutory and does not adjust.

## Civil penalties — failure to file (IRC §6721)

The §6721 penalty applies to failure to file an information return (which includes Form 8300) on time, file in the required electronic format, or include all required information.

### Tiers (penalty per failure, current inflation-adjusted amounts)

Verify the current-year amounts in the most recent Rev. Proc. before quoting to the user. As of Rev. Proc. 2024-40 (tax year 2025):

| Tier | When | Penalty per failure |
|------|------|---------------------|
| First tier | Filed within 30 days of the deadline | $60 |
| Second tier | Filed after 30 days but by August 1 | $130 |
| Third tier | Filed after August 1 or not filed | **$330** (verify current year — described in the blog as $310; rates have moved) |
| Intentional disregard | Knowing failure to file | Greater of $660 per failure or 10% of the cash amount required to be reported (up to $134,800 per failure as of 2025; verify) |

The blog companion uses $310 as a rounded current figure; the agent should always cite the current Rev. Proc. amount when producing a deliverable.

### Aggregate caps

Negligent-failure penalties are subject to annual caps that scale with business size; intentional-disregard penalties have no cap. For a single $10K cash receipt event, the cap is rarely a concern — the per-failure number drives the analysis.

## Civil penalties — failure to furnish payee statement (IRC §6722)

§6722 applies to failure to furnish the customer notification due by January 31 of the year following the filing.

| Tier | When | Penalty per recipient |
|------|------|------------------------|
| First tier | Furnished within 30 days of January 31 | $60 |
| Second tier | Furnished after 30 days but by August 1 | $130 |
| Third tier | Furnished after August 1 or not at all | $330 (verify current year) |
| Intentional disregard | Knowing failure to furnish | Greater of $660 per statement or 10% of the aggregate amount required to be reported, no cap |

§6722 is **independent of** §6721 — a business that filed the 8300 timely but missed the customer notification still owes §6722.

## Doubling for the same event

The §6721 + §6722 stack means a single missed transaction can cost roughly **2× the per-failure amount** before any intentional-disregard finding. For a single $14,500 transaction with both filings missed:

- §6721: $330 (negligent third tier)
- §6722: $330 (negligent third tier)
- Total civil: ~$660 baseline

Under intentional disregard, the greater-of formula means a $14,500 reportable cash amount yields a per-failure penalty of $660 (greater than 10% of $14,500 = $1,450 — wait, recheck: greater of $660 OR 10% of cash = $1,450 → $1,450 per failure). Stacked across §6721 and §6722, the same transaction can produce $2,900+ in intentional-disregard exposure.

## Criminal penalties

Form 8300 sits at the intersection of tax law and the Bank Secrecy Act. Knowing willful violations carry criminal exposure under both regimes.

### IRC §7203 — willful failure to file

A willful failure to file Form 8300 (or to supply information required by §6050I) is a **misdemeanor**, punishable by:

- Up to $25,000 fine ($100,000 for a corporation)
- Up to 1 year imprisonment
- Both, plus prosecution costs

### IRC §7206 — false or fraudulent return

A willful filing of a false or fraudulent Form 8300 is a **felony**, punishable by:

- Up to $100,000 fine ($500,000 for a corporation)
- Up to 3 years imprisonment
- Both, plus prosecution costs

### 31 USC §5324 — structuring

Structuring transactions to evade the §6050I reporting requirement is a separate criminal offense under 31 USC §5324(b). Penalties:

- Up to $250,000 fine ($500,000 for a corporation)
- Up to 5 years imprisonment
- Up to 10 years imprisonment if combined with another violation or part of a pattern of illegal activity > $100,000 in any 12-month period

Structuring includes both the buyer breaking up payments to keep each below $10,000 AND the recipient agreeing to accept smaller payments to avoid filing. **The recipient business can be prosecuted for participating in structuring**, even if the recipient did not initiate it.

### Patriot Act and BSA layered exposure

Because §5331 incorporates Form 8300 into the BSA, knowing failures to file can also implicate broader BSA criminal provisions (31 USC §5322), with additional fines up to $250,000 and 5 years per violation, doubled under aggravated patterns.

## Reasonable cause defense

§6724 provides a "reasonable cause" defense to the §6721 and §6722 civil penalties. The standard is high — the filer must show that the failure was due to reasonable cause and not willful neglect, AND that the failure was corrected within a reasonable time after discovery.

What counts as reasonable cause:

- Documented serious illness or natural disaster preventing timely filing
- Reliance on bad advice from a tax professional, where the professional was given complete and accurate information
- Inability to obtain the customer's TIN despite documented good-faith efforts (refused TIN should be filed with TIN blank and the refusal documented)

What does NOT count as reasonable cause:

- "I forgot"
- "My accountant didn't tell me about it"
- "The customer didn't want to give their information"
- "I didn't know cash included money orders"

## Penalty mitigation in practice

If a filer discovers a missed 8300:

1. **File the late report immediately.** Each day of delay can move the penalty into a higher tier.
2. **Document the discovery and correction** — when did you realize the gap, what did you do, on what date.
3. **Consider a voluntary disclosure** to the IRS Small Business / Self-Employed division if multiple filings were missed. Voluntary disclosure does not eliminate civil penalties but may reduce them and reduces criminal exposure.
4. **Engage a CPA or tax attorney** if the missed filings span multiple years or involve large amounts. Self-prepared late filings can compound exposure.
5. **Send the customer notifications** for any 8300s filed late, even retroactively — separate §6722 failure stacks otherwise.

## Pattern enforcement

The IRS's most common 8300 enforcement case is not a single missed filing but a **pattern of missed filings** discovered through a single audit:

- A used-car dealer takes 8 cash transactions over $10K in a year, files none. Audit reveals the pattern through customer-side records.
- Per-failure penalty under intentional disregard at $1,450+ × 8 = $11,600 minimum, often higher
- §6722 stacking adds equivalent customer-notification penalties
- Criminal referral becomes likely once a deliberate pattern is established

The risk profile changes sharply at "third or fourth missed filing in a 12-month period." The agent should flag this clearly to any user describing a backlog.

## When the agent should escalate

If the user describes:

- Three or more missed 8300s
- An audit letter or IRS notice referencing 8300 compliance
- Cash transactions over $30,000 with deliberate structuring
- Any criminal investigation contact

Stop the workflow and recommend: "This is beyond the scope of a self-filing tool. Engage a tax attorney or AML/BSA compliance specialist before responding to the IRS or filing additional reports."
