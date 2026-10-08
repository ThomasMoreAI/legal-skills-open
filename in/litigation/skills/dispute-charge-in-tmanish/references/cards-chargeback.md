# Card Disputes & Chargebacks (India)

For wrong or disputed **merchant charges** on credit and debit cards, duplicates, charges after cancellation, goods not received, amounts different from what was agreed. (For transactions the person never made at all, that's fraud, read `unauthorized-transactions.md` first; the RBI zero-liability clock dominates.)

## The mechanism: chargeback through the issuing bank

Indian card transactions run on the same card networks (Visa, Mastercard, RuPay, Amex), and the **chargeback**, the issuing bank reversing the charge through the network, is the working lever for merchant disputes. It isn't a statutory right, but it's an established process every issuer operates, and network rules give the person a genuine dispute path when the merchant won't cooperate.

Grounds that typically support a chargeback:
- **Duplicate billing**, charged twice for one purchase
- **Charged after cancellation**, subscription or order cancelled, charge taken anyway
- **Goods/services not received**, paid, never delivered
- **Amount mismatch**, billed more than the agreed price
- **Refund promised but never processed**, merchant issued a refund confirmation that never landed
- **Merchant ceased operations** before delivering

## Timing

Chargeback windows are set by the card networks and are **limited, typically in the range of 60–120 days** from the transaction or expected delivery date, varying by network and dispute type. Don't quote an exact figure as universal; the safe instruction is **raise it promptly, and if weeks have already passed, raise it now**. The person raises it with their **issuing bank** (the bank that issued the card), not the merchant's bank.

## The process

1. **Contact the merchant first, in writing, with a deadline**, most networks expect an attempted resolution, and it builds the record. Keep the refusal or silence as evidence.
2. **Raise the dispute with the issuing bank**, via the app (most Indian banks have a "dispute transaction" or "raise chargeback" flow), net banking, or the bank's grievance email. State the ground, attach evidence (order confirmation, cancellation proof, merchant correspondence), and **get the dispute reference number**.
3. The bank raises the chargeback through the network; the merchant can contest, so documentation decides it.
4. Billing disputes on credit cards also sit within RBI's card rules, a cardholder can dispute a billing entry, and the bank must address it through its grievance process; if it doesn't, that failure feeds the Ombudsman escalation.

While a credit-card amount is under genuine dispute, the person should say so in writing and ask the bank to note the dispute on the account, and should keep paying the undisputed balance so the dispute doesn't turn into a delinquency problem.

## Language to include (to the issuing bank)

- "I am disputing the following transaction and request a **chargeback**."
- Transaction: date, amount, merchant as it appears, card last 4 digits.
- The ground: duplicate / charged after cancellation on [date] (proof attached) / goods not received by [expected date] / amount differs from agreed ₹[X].
- "I contacted the merchant on [date]; [they refused / did not respond]. Correspondence attached."
- "Please register this dispute, provide the reference number in writing, and confirm the timeline. Failing resolution, I will escalate to your nodal officer and the RBI Ombudsman."

## Escalation

- Bank stalls or rejects unreasonably → the bank's **grievance redressal cell / nodal officer** in writing, then the **RBI Ombudsman** after ~30 days (read `banking-ombudsman.md`).
- The underlying merchant dispute (defective goods, service deficiency, seller refusing a lawful refund) can go to the **consumer commission** in parallel (read `consumer-commissions.md`), the chargeback recovers the money; the commission adds compensation and pressure.
