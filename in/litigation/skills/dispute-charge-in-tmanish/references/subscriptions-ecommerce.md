# Subscription, Auto-Debit, and E-Commerce Refund Disputes (India)

The "I cancelled but got billed," "the free trial charged me," and "the seller won't refund" family, plus the auto-debit angle that's specific to India's payment rules.

## The India-specific lever: recurring-payment rules

RBI's framework for recurring card payments (e-mandates) requires **additional factor authentication when a mandate is set up**, a **pre-debit notification** to the customer before each charge above the small-value threshold, and, critically, an **easy way for the customer to modify or cancel the mandate**. Two consequences worth using:
- A recurring card charge the person never consciously authorized as a mandate, or that arrived with no pre-debit notification, is on weak ground, say so in the complaint.
- **The person can kill the mandate at the bank/card level**, not just with the merchant. Banks and card issuers provide a mandate-management facility (in the app or net banking, e.g. via the SiHub/mandate dashboard) where recurring authorizations can be viewed and cancelled. For UPI Autopay, mandates are cancellable directly in the UPI app. This is the "stop the bleeding" move: cancel the mandate at the payment level first, then fight about the refund.

## The facts that win these

- **The cancellation evidence**, confirmation email, screenshot, ticket number, and the date. "I cancelled on [date] (reference #X) and was charged on [date] anyway" is close to unbeatable.
- **The mandate trail**, was a recurring mandate ever properly set up with authentication? Did pre-debit notifications arrive? Absence is leverage.
- **The free-trial conversion**, if the conversion to paid wasn't clearly disclosed and consented to, say so specifically.

## Two-track strategy

Run both at once:
1. **The merchant/platform**, a dated written demand for the refund of the specific charge, citing the cancellation evidence, with a deadline, sent to the platform's **grievance officer** (see below).
2. **The payment lever in parallel**, cancel the mandate at the bank/app level, then raise a **chargeback** with the issuing bank for the charge taken after cancellation (read `cards-chargeback.md`). For a UPI Autopay debit after cancellation, dispute it through the app and the bank (read `upi-digital-payments.md`).

## E-commerce platforms: the grievance officer route

Under India's e-commerce consumer-protection rules, e-commerce entities must operate a **grievance redressal mechanism** with a named **grievance officer**, acknowledge complaints quickly (within about 48 hours) and redress them within about a month. The practical use:
- Address the written complaint to the **grievance officer** by name/designation (every compliant platform lists one, usually in the footer or "contact us" page) rather than generic support, it lands in the accountable channel.
- Cite the acknowledgment/redressal obligation and demand the ticket number.
- Platforms are also barred from unfair practices like refusing to take back defective goods or refusing refunds where due, for a defective or wrong item, pair this with the Consumer Protection Act framing (read `consumer-commissions.md`).

## Language to include (merchant/platform message)

- "I'm requesting a refund of ₹[amount] charged on [date], [transaction/order ID]. I cancelled this [subscription/order] on [date] (reference #[X]), so this charge should not have been taken."
- Where it fits: "No valid recurring mandate with my authentication exists for this charge / no pre-debit notification was received, as required for recurring card payments."
- "Please refund ₹[amount] to my original payment method within [7–15 days] and confirm the [subscription/mandate] is fully cancelled with no further charges."
- Escalation line: "Failing which, I will raise a chargeback with my bank, register the grievance with the National Consumer Helpline (1915), and file before the District Consumer Commission through e-Daakhil."

## Escalation

- **Chargeback / mandate cancellation** at the bank, usually the fastest actual recovery.
- **National Consumer Helpline (1915)**, free, registers the grievance against the company; many major platforms respond through NCH's convergence program.
- **Consumer commission via e-Daakhil** (read `consumer-commissions.md`), refund plus compensation for the harassment; filing where the person lives, no fee up to ₹5 lakh.
- **RBI Ombudsman** if the bank mishandles the mandate cancellation or chargeback (read `banking-ombudsman.md`).
