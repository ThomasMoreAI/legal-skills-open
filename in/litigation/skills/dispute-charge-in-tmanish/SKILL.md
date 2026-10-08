---
name: dispute-charge-in-tmanish
title: Dispute a Charge (India)
description: Write effective letters and complaints to dispute a wrong charge, bill, fee, failed transaction, or denied refund in India and actually get money back, using Indian consumer-protection mechanisms (RBI rules, Consumer Protection Act 2019, banking ombudsman). Use whenever someone in India wants help disputing a charge, fighting a fee, getting a refund, reversing a UPI or card transaction, reporting fraud on their account, challenging a bill, complaining about an e-commerce seller, or escalating after a company or bank said no. Trigger even without the word "dispute"; phrases like "they charged me twice," "I want my money back," "money got debited but the transaction failed," "UPI fraud," "I was billed after cancelling," "the seller refuses to refund," or "how do I fight this charge" all mean this skill should be used. This is the India-specific edition; use it when the person is in India or dealing with an Indian bank, merchant, or platform.
author: tmanish
author_url: https://github.com/tmanish/dispute-charge/tree/main/dispute-charge-in
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: litigation
language: en
sources:
- title: Banking Ombudsman
  path: references/banking-ombudsman.md
- title: Cards Chargeback
  path: references/cards-chargeback.md
- title: Consumer Commissions
  path: references/consumer-commissions.md
- title: Subscriptions Ecommerce
  path: references/subscriptions-ecommerce.md
- title: Unauthorized Transactions
  path: references/unauthorized-transactions.md
- title: Upi Digital Payments
  path: references/upi-digital-payments.md
---

# Dispute a Charge (India)

People lose real money to wrong charges, failed-but-debited transactions, fraud, and refused refunds, not because they lack a case, but because the complaint they send is a polite request instead of one that invokes an actual obligation. India's framework is stronger than most people realize: RBI rules put banks on hard clocks with real penalties, and the Consumer Protection Act 2019 gives consumers a genuinely accessible tribunal system. This skill puts those to work.

The goal of every output is a message that does four things a generic complaint doesn't: states the specific facts cleanly, names the mechanism that obligates a response (the RBI circular, the chargeback, the Consumer Protection Act), sets a deadline, and makes the next escalation visible, the RBI Ombudsman, the consumer commission, e-Daakhil, so the recipient knows ignoring it has a cost.

## The two clocks that decide everything

Two timing rules dominate Indian disputes, and the person's position often depends on acting inside them:

1. **Fraud/unauthorized transactions: the 3-working-day rule.** Under RBI's customer-protection framework, reporting an unauthorized electronic transaction within **3 working days of the bank's alert** generally means **zero liability**, the bank must reverse the full amount. Days 4–7 cap liability at ₹5,000–₹25,000 depending on account type; beyond 7 days it's the bank's board policy. If someone mentions fraud, the very first output should be: report to the bank NOW, in writing, then the letter. Read `references/unauthorized-transactions.md`.
2. **Everything else: build the written record early.** Escalation to the RBI Ombudsman requires having complained to the bank first (and giving it ~30 days); consumer commission cases are built on the documented trail. The letter isn't just persuasion, it's the foundation of the escalation.

## The one rule that matters most

**Get the facts before writing.** A vague complaint gets a form reply; a specific one gets resolved. If key facts are missing, ask efficiently, in one batch:
- **What** was charged/debited, **how much**, **exact date and time** (for UPI/digital, the transaction ID / UTR number is gold)
- **Who** charged it (merchant/bank as it appears) and **how it was paid** (credit card, debit card, UPI, net banking, wallet, this decides the mechanism)
- **Why it's wrong** (unauthorized/fraud, failed but debited, duplicate, cancelled but charged, item not delivered, defective, service deficient)
- **What they've already done** (called the bank? complaint/reference number? been refused? first contact?)
- **What outcome they want** (reversal, refund, replacement, compensation)

If some facts are missing but the person wants speed, write with bracketed placeholders like `[transaction ID]`, except for fraud, where the report-immediately instruction comes first regardless.

## Pick the right mechanism

| If the situation is... | Read this file |
|---|---|
| Fraud / a transaction the person never made (card, UPI, net banking, wallet) | `references/unauthorized-transactions.md` |
| A UPI or digital payment that failed but money was debited, or a wrong UPI transfer | `references/upi-digital-payments.md` |
| A wrong or disputed **card** charge from a merchant (duplicate, cancelled, not received) | `references/cards-chargeback.md` |
| A bank won't fix it, is stalling, or levied a wrong fee/charge | `references/banking-ombudsman.md` |
| Defective goods, deficient service, or an e-commerce seller refusing a refund | `references/consumer-commissions.md` |
| A subscription, auto-debit, or "I cancelled but got billed" | `references/subscriptions-ecommerce.md` |

Often two apply (a fraudulent card charge → unauthorized-transactions for the RBI clock *and* cards-chargeback for the network dispute; a seller refusing a refund on a card purchase → consumer-commissions *and* cards-chargeback). Read both and combine, the RBI/bank mechanism usually recovers the money fastest, while the Consumer Protection Act route adds compensation and real pressure.

## Structure of an effective dispute letter

Keep it tight, one page. Long letters read as emotional; short letters read as serious.

```
[Your name]
[Address / registered mobile / email]
[Account or card last 4 digits / transaction ID / order number]
[Date]

To: [Bank grievance cell / merchant / platform grievance officer]

Re: [Dispute / refund demand / unauthorized transaction report], ₹[amount] dated [date]

[1. The claim, in one or two sentences. What was charged/debited, when, and
what you want. Exact amount, date, transaction/reference ID.]

[2. The facts, in plain chronological order, order/transaction details,
cancellation dates, prior complaint numbers, evidence.]

[3. The mechanism. The rule that applies and what it obligates. E.g. "Under
RBI's circular on limiting customer liability in unauthorized electronic
banking transactions, I reported within 3 working days and my liability
is zero; please reverse the full amount."]

[4. The ask + deadline, exactly what you want and by when.]

[5. The escalation, stated calmly, the RBI Ombudsman, the consumer
commission via e-Daakhil, the National Consumer Helpline (1915).]

[Signature]
```

## Tone: calm, specific, slightly formal

- **No insults, no capitals, no emotional escalation**, anger gives the recipient a reason to dismiss you.
- **No over-explaining or pleading.** State the fact: "This debit is unauthorized." / "This charge is incorrect."
- **Cite specifics relentlessly**, dates, amounts, transaction IDs, complaint reference numbers. In India, the complaint reference number is the currency of escalation; always tell the person to demand one and record it.
- **One clear ask**, stated plainly and once.
- **Name the deadline and the next step.** A letter that says "failing which I will escalate to the RBI Ombudsman / file before the consumer commission" cannot simply be filed away.

## How to deliver the output

Default to a ready-to-send message the person can copy, most Indian disputes start via the bank's app or email, the merchant's support email, or a platform's grievance form. Email to the bank's or platform's **official registered grievance email creates a timestamped record**, prefer it over (or in addition to) phone calls, and tell the person to keep every acknowledgment. For bank matters, route to the bank's **grievance redressal cell / nodal officer** (listed on every bank's website), not just frontline support.

## What this skill does not do

- It does not invent rules or numbers. The RBI liability tiers, commission jurisdiction limits, and timelines in the reference files are the verified backbone; where a detail isn't certain (bank-specific policies, state-specific practice), describe the mechanism generically rather than asserting specifics.
- It does not assume the law is frozen. RBI circulars and consumer rules change; if the dispute hinges on a specific rule or a very recent regulation you're not fully certain is current, verify with a quick web search (if available) before citing it, and if you can't verify, describe the mechanism generically.
- It does not apply Indian law to non-Indian situations. If it becomes clear the person is not in India and isn't dealing with an Indian bank/merchant, don't cite RBI rules or the Consumer Protection Act. Fall back to the universal structure, exact facts, the contract/policy terms, one clear ask, a deadline, visible escalation, plus the card chargeback, and point them to their own country's consumer authority.
- It does not give formal legal advice or guarantee outcomes. For high-value or complex matters (large sums, insurance disputes, real estate, anything heading to litigation), say plainly the letter is a strong first step but the person may want a consumer lawyer or the appropriate forum, and point them there.
- It does not help fabricate facts. The strategy depends on a truthful, documented account. Filing a false complaint or a false fraud report is itself an offense, redirect to disputes the person actually has grounds for.

## Quick reference: the highest-impact India moves

1. **For fraud: report within 3 working days, in writing**, this single act can take liability to zero. Everything else comes second.
2. **Name the exact transaction**, date, amount, transaction ID/UTR. Vagueness is the #1 reason disputes fail.
3. **Get and quote the complaint reference number** at every step, it's what makes escalation stick.
4. **Use the bank-first-then-Ombudsman rhythm**, complain to the bank's grievance cell in writing; if unresolved in ~30 days or the reply is unsatisfactory, escalate free of charge to the RBI Ombudsman.
5. **Remember the consumer commission is genuinely accessible**, file where *you* live, online via e-Daakhil, no fee up to ₹5 lakh, and compensation is on the table. Naming it in the letter is real pressure. Keep it to one page and zero emotion.
