# Distance selling: information, order button, cancellation

The Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013 (SI 2013/3134). Status as at 2026-08-05: in force, revised text current to August 2026. The term is "the right to cancel", not "the right of withdrawal" and not "the right to a refund".

Two provisions of the DMCC Act 2024 (inserting regs 7(4A) and 27(3A)) are recorded on legislation.gov.uk as outstanding changes not yet applied to the text — they relate to the interaction with the DMCC subscription regime, which is not in force (see `dmcc-trading.md`).

## Pre-contract information — reg 13 and Schedule 2

For a distance contract the trader must give or make available the Schedule 2 information in a clear and comprehensible manner before the consumer is bound. It includes the main characteristics, the trader's identity and geographical address, the total price inclusive of taxes and all delivery and additional charges, arrangements for payment and delivery, the complaint handling policy, the existence of the statutory conformity obligation, the duration of the contract and how to terminate it, and — paragraph (l) — the conditions, time limit and procedures for exercising the right to cancel together with the model cancellation form in Schedule 3 Part B.

The information forms part of the contract (reg 13(5)) and cannot be altered without express agreement.

## The order button — reg 14

Status as at 2026-08-05: in force.

Reg 14(2): where the contract places the consumer under an obligation to pay, the trader must make the consumer aware, in a clear and prominent manner and directly before the consumer places the order, of the information in Schedule 2 paragraphs (a), (f), (g), (h), (s) and (t).

Reg 14(3): the trader must ensure the consumer explicitly acknowledges that the order implies an obligation to pay.

Reg 14(4): if placing the order entails activating a button or similar function, the trader must ensure it is labelled in an easily legible manner only with the words "order with obligation to pay" or a corresponding unambiguous formulation indicating that placing the order entails an obligation to pay the trader.

Reg 14(5): if the trader does not comply with reg 14(3) or (4), the consumer is not bound by the contract or order.

"Buy now", "Submit", "Continue", "Complete order" and "Place order" do not indicate a payment obligation. "Pay now", "Buy now — pay £X" and "Order with obligation to pay" do. The order summary must sit directly above the button.

Reg 14(6): trading websites must indicate clearly and legibly, at the latest at the beginning of the ordering process, whether any delivery restrictions apply and which means of payment are accepted.

## The right to cancel — regs 27–38

**Reg 29:** the consumer may cancel a distance or off-premises contract at any time in the cancellation period without giving any reason and without incurring any liability, except as provided in regs 34(3), 34(9), 35(5) and 36(4).

**Reg 30 — normal cancellation period, 14 days:**

| Contract type | Period ends 14 days after |
|---|---|
| Service contract, and digital content not on a tangible medium | the day the contract is entered into |
| Sales contract, single delivery | the day the goods come into the physical possession of the consumer or a person identified by them |
| Multiple goods in one order, delivered separately | the day the last of the goods is received |
| Goods in multiple lots or pieces | the day the last lot or piece is received |
| Regular delivery over a defined period | the day the first of the goods is received |

**Reg 31 — extension for breach of the information duty.** If the trader does not provide the information on the right to cancel required by Schedule 2 paragraph (l): if the trader supplies it within 12 months of the day the 14-day period began, the cancellation period ends 14 days after the consumer receives it; otherwise it ends 12 months after the day it would have ended under reg 30.

**Reg 28 — contracts and situations where the right does not apply**, including goods made to the consumer's specifications or clearly personalised; goods liable to deteriorate or expire rapidly; sealed goods not suitable for return for health protection or hygiene reasons once unsealed; sealed audio, video recordings or software once unsealed; goods inseparably mixed after delivery; newspapers, periodicals and magazines other than subscriptions; contracts concluded at public auction; accommodation, transport of goods, vehicle rental, catering and leisure services for a specified date or period; and urgent repair or maintenance visits specifically requested by the consumer.

**Reg 37 — digital content supplied before the end of the cancellation period.** The consumer loses the right to cancel only if they gave express consent to supply beginning before the end of the period and acknowledged that the right to cancel would be lost. Both must be captured; two separate, unticked confirmations with a timestamp.

**Regs 34–35 — reimbursement.** Refund without undue delay and in any event within 14 days; for sales contracts, from the day the goods are received back or the consumer supplies evidence of return, whichever is earlier. Standard delivery cost is refunded; the extra cost of an enhanced delivery option chosen by the consumer is not. Return costs fall on the consumer only if the trader told them so before the contract.

## Templates

Cancellation notice:

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Your right to cancel</h2>
<p>
  You have the right to cancel this contract within 14 days without giving any reason.
  The cancellation period will expire after 14 days from [[the day on which you acquire, or a third
  party other than the carrier and indicated by you acquires, physical possession of the goods /
  the day of the conclusion of the contract]].
</p>
<p>
  To exercise the right to cancel, you must inform us —
  [[registered name]], [[address]], [[email]], [[telephone]] —
  of your decision to cancel this contract by a clear statement (for example a letter sent by post
  or email). You may use the model cancellation form below, but it is not obligatory.
  To meet the cancellation deadline it is sufficient for you to send your communication concerning
  your exercise of the right to cancel before the cancellation period has expired.
</p>
<p>
  If you cancel this contract, we will reimburse to you all payments received from you, including
  the costs of delivery (except for the supplementary costs arising if you chose a type of delivery
  other than the least expensive type of standard delivery offered by us). We will make the
  reimbursement without undue delay, and not later than 14 days after
  [[the day we receive back from you any goods supplied, or you supply evidence of having sent them
  back, whichever is earliest / the day we are informed about your decision to cancel]].
  We will make the reimbursement using the same means of payment as you used for the initial
  transaction, unless you have expressly agreed otherwise; you will not incur any fees as a result.
</p>
<p>[[Goods only:]] You must send back the goods without undue delay and in any event not later than
  14 days from the day on which you communicate your cancellation to us.
  [[You will have to bear the direct cost of returning the goods. / We will collect the goods at our cost.]]
</p>
```

Model cancellation form, Schedule 3 Part B CCRs 2013. The authoritative wording is published on legislation.gov.uk as images; reproduce it from the instrument itself and verify before publication.

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h3>Model cancellation form</h3>
<p>(Complete and return this form only if you wish to withdraw from the contract.)</p>
<p>
  To [[trader's name, geographical address, and where available fax number and email address]]:<br><br>
  I/We [*] hereby give notice that I/We [*] cancel my/our [*] contract of sale of the following
  goods [*]/for the supply of the following service [*],<br><br>
  Ordered on [*]/received on [*],<br>
  Name of consumer(s),<br>
  Address of consumer(s),<br>
  Signature of consumer(s) (only if this form is notified on paper),<br>
  Date<br><br>
  [*] Delete as appropriate
</p>
```

The form must be supplied with the pre-contract information and be downloadable or printable. A cancellation web form may be offered in addition (reg 32(3)), with acknowledgement of receipt on a durable medium, but it does not replace the model form.

## Checkpoints

- [ ] The word used throughout is "cancel", never "withdraw"
- [ ] Order button labelled "order with obligation to pay" or an equally unambiguous payment wording (reg 14(4))
- [ ] Order summary with total price directly above the button (reg 14(2))
- [ ] Delivery restrictions and accepted payment means stated at the start of the ordering process (reg 14(6))
- [ ] All Schedule 2 information given before the consumer is bound (reg 13)
- [ ] Cancellation period start correctly matched to the contract type (reg 30)
- [ ] Model cancellation form from Schedule 3 Part B provided and saveable
- [ ] Order confirmation supplied on a durable medium including the cancellation information (reg 16)
- [ ] Digital content immediate access: express consent and acknowledgement of loss of the right captured as two separate unticked confirmations with a timestamp (reg 37)
- [ ] Exclusions claimed only where reg 28 actually applies — no invented "unopened packaging only" or "no returns on sale items"
- [ ] Return costs disclosed before contract if the consumer is to bear them (reg 35(5))
- [ ] Refund within 14 days, same payment method, delivery cost included at the standard rate (reg 34)
- [ ] No claim that the DMCC subscription cancellation rules apply — they are not in force
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
