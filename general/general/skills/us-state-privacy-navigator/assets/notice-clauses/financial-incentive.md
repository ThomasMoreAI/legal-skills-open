# Model Clause — Notice of Financial Incentive (CA-specific; partial relevance elsewhere)

> **Use note.** California requires a "Notice of Financial Incentive" when a business offers a price or service difference in exchange for the collection, sale, sharing, or retention of PI (Cal. Civ. Code § 1798.125; CCPA Regs § 7016). Common triggers: loyalty programs that offer a discount in exchange for email signup; "give us your email and get 10% off" prompts; subscription tiers that offer "free with ads" vs. "paid ad-free."
>
> Colorado has loyalty-program-specific requirements under CPA Rules § 6.04. Other states do not have a directly equivalent regime, though the underlying transparency principles apply.
>
> **Never paste verbatim.** Tune to actual program economics and PI categories.

---

## Notice of Financial Incentive (California)

**Effective: [Date — AD format]**

This Notice of Financial Incentive describes the [Loyalty Program / Email Subscription / Discount Program] offered by [Company Name] ("we," "us," or "our") and how it relates to the collection, use, sale, or sharing of your personal information. This Notice is provided pursuant to California Civil Code § 1798.125 and CCPA Regulations § 7016.

### What we offer

When you [participate in / join / sign up for] [Program Name], you receive:

- [Specific benefit, e.g., a 10% discount on your first order]
- [Specific benefit, e.g., 1 point per dollar spent, redeemable for $5 reward at 500 points]
- [Specific benefit, e.g., access to members-only sales]

### What we collect and how we use it

In exchange for the benefits above, you provide us with the following categories of personal information:

| Category | Examples | How we use it |
|---|---|---|
| **Identifiers** | [Email address; first/last name; phone number] | [Account creation; sending program communications; identifying you at checkout] |
| **Customer records** | [Purchase history; product preferences] | [Personalizing offers; calculating point balance; recommending products] |
| **Internet/network activity** | [Browsing history on our properties; email open/click tracking] | [Measuring program engagement; optimizing offer relevance] |
| **Inferences** | [Preferences derived from purchase and browsing history] | [Personalizing the program experience] |

### Material terms

- **Joining is free.** You do not pay anything to join the Program.
- **You may withdraw at any time.** To withdraw, [unsubscribe link / contact path]. Upon withdrawal, you forfeit unredeemed program benefits unless [exception].
- **Effect of opt-out of sale or sharing.** If you opt out of the sale or sharing of your personal information, you can still participate in the Program. We will not condition program participation on your decision regarding sale or sharing.

### How we calculate the value of your personal information

The CCPA permits a price or service difference if it is reasonably related to the value of the consumer's data to the business. We have estimated that the value of your participation in the Program — including the personal information you provide — is approximately **$[X] per year per participant**, calculated using the following methodology:

[Describe the actual methodology. Examples that have been used by sophisticated programs:]

- **Expense methodology**: the marginal expense of administering the Program (technology, operations, fulfillment) divided by the number of active participants. Result: $[X] per participant.
- **Revenue-uplift methodology**: the difference in average annual revenue from a participant vs. a non-participant of similar profile. Result: $[X] per participant.
- **Direct-cost methodology**: the average value of the discounts and rewards distributed per participant per year. Result: $[X] per participant.

We have determined that the benefits we provide to participants ($[X] in discounts/rewards per year) are reasonably related to the value of the personal information collected through the Program ($[X] per year).

### Right of non-discrimination

We do not discriminate against you for exercising your privacy rights. Specifically:
- You may request access to, deletion of, or correction of your personal information without losing program benefits.
- You may opt out of sale or sharing of your personal information without losing program benefits.
- You may withdraw consent for sensitive personal information processing without losing program benefits, except as the withdrawal directly affects the specific feature for which the sensitive information is necessary.

### How to withdraw

To withdraw from the Program: [step-by-step].

To exercise your privacy rights generally: [link to Privacy Choices page].

To contact us: [privacy@example.com] | [toll-free phone].

---

## Colorado-Specific Loyalty Program Notice (CPA Rules § 6.04)

**Use when**: the controller offers a loyalty program AND is subject to Colorado CPA AND the program involves processing of PD beyond what is needed to fulfill the program benefit.

> ## Colorado Residents — Loyalty Program Information
>
> Our [Loyalty Program] processes your personal data to provide loyalty benefits. Beyond what is necessary to provide those benefits, we [also use program data for [marketing personalization, analytics, etc.]]. You may participate in the Loyalty Program without consenting to those additional uses.
>
> **What we process to deliver the loyalty benefit (no consent required):**
> - [Identifiers]
> - [Purchase history]
>
> **What we process beyond delivering the loyalty benefit (consent required):**
> - [Inferred preferences for non-program marketing]
> - [Cross-context behavioral advertising data, if applicable]
>
> If you do not consent to the additional uses, we will still provide the loyalty benefits associated with the program. To withhold or withdraw consent, [contact / settings].

---

## Implementation notes (delete from production)

1. **Trigger analysis.** Determine whether the program actually triggers the financial-incentive notice. A discount offered to all customers without conditioning on PI (e.g., "10% off for everyone today") is not a financial incentive. A discount conditioned on email signup or program enrollment is.
2. **Value calculation methodology.** This is an art rather than a science. Document the methodology and supporting calculation. Be prepared to defend it. AG enforcement has scrutinized hand-waving "negligible value" claims.
3. **Non-discrimination.** Programs that effectively penalize consumers who exercise privacy rights are non-compliant. Audit the consumer-experience differences between a program participant who opts out of sale and one who does not.
4. **Subscription "free with ads" tiers.** These can be treated as financial incentives if the "free" tier is conditioned on enabling certain data collection or sharing. Apply the financial-incentive framework if so.
5. **Multi-state coverage.** California's framework is the most prescriptive. CO has its own loyalty rules. Other states do not have a direct equivalent but transparency obligations apply.
6. **Documentation.** Retain the financial-incentive analysis and value calculation as part of the privacy program. AG inquiries often request this.
