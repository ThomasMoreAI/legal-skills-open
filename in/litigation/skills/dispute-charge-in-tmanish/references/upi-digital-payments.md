# UPI & Digital Payment Disputes (India)

UPI disputes are their own category because the flows and remedies differ from cards. Three distinct situations arrive under "UPI problem", identify which one it is before writing anything, because the mechanism is different for each.

## Situation 1: Transaction failed but money was debited

The most common case, and the one with the sharpest rule. Under RBI's framework harmonizing turnaround times for failed transactions, a failed UPI transaction where the account was debited but the beneficiary wasn't credited must be **auto-reversed by the bank, generally within one day (T+1)** of the transaction. If the reversal is delayed beyond the prescribed time, the bank owes the customer **compensation of ₹100 per day of delay**, automatically, without the customer having to claim it. (Similar timelines exist for other channels; for a failed ATM withdrawal where cash wasn't dispensed, reversal is due within about five days, with the same ₹100/day compensation beyond it.)

The letter should: identify the transaction (date, time, amount, **UPI transaction ID / UTR**, get this from the app), state it failed but was debited, cite the auto-reversal requirement and the ₹100/day compensation for the delay already accrued, and set the demand.

## Situation 2: Fraudulent UPI transaction (money taken without authorization)

This is an **unauthorized electronic transaction**, the RBI zero-liability framework applies in full, including the 3-working-day clock and the 10-day provisional credit. **Read `unauthorized-transactions.md` and lead with that.** Two UPI-specific additions:
- Report to the cyber fraud helpline **1930** immediately, for in-flight fraud, fast reporting can freeze the money before it's withdrawn.
- Also flag/report the fraud in the UPI app itself (raise a dispute against the transaction) so it enters the payment-system dispute track in parallel.

Note honestly: where the person **themselves transferred money to a scammer** (tricked into paying, e.g. a fake seller or "refund" scam), the zero-liability framework is weaker, that transaction was technically initiated by them. It's still worth reporting immediately (1930 can freeze funds in transit), disputing in the app, and complaining to the bank, but set expectations accordingly and don't promise the RBI tiers apply cleanly.

## Situation 3: Money sent to the wrong UPI ID / wrong number

There is **no automatic right of reversal**, the money has landed in a real (wrong) person's account, and banks can't simply claw it back without the recipient's consent. Be honest about this. The practical sequence:
1. **Immediately** raise it with the UPI app's support and the person's own bank, quoting the transaction ID, speed matters because recovery is easiest before the recipient spends it.
2. The bank/NPCI process contacts the beneficiary's bank, which asks the recipient to consent to a reversal.
3. If the recipient refuses to return clearly mistaken money, the person's remedies move to the legal track, a written demand to the recipient (if identifiable), a police complaint, and civil recovery. For meaningful amounts, say plainly this may need legal help.

## The escalation ladder for UPI disputes

1. **Raise the dispute in the UPI app** (Google Pay / PhonePe / Paytm / BHIM etc.), get the dispute/ticket number.
2. **Complain in writing to the person's own bank** (the account that was debited), banks own the reversal obligation; quote the app ticket and the UTR.
3. If unresolved, escalate through **NPCI's dispute redressal mechanism** (NPCI has an online complaint route for UPI).
4. If still unresolved or the bank stalls ~30 days: the **RBI Ombudsman** (read `banking-ombudsman.md`), digital-payment complaints are squarely within its remit.

## Language to include (failed-but-debited letter)

- "On [date] at [time], UPI transaction [ID/UTR] of ₹[amount] to [payee] **failed but my account was debited**. The amount has not been reversed."
- "Under RBI's directions on turnaround time for failed transactions, this should have been auto-reversed within one day, and **compensation of ₹100 per day** is payable for the delay beyond that, now [N] days."
- "Please reverse ₹[amount] plus the compensation accrued, and provide the complaint reference number in writing. Failing resolution, I will escalate to NPCI and the RBI Ombudsman."
