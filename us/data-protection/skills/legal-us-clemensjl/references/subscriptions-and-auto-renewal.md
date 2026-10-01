# Subscriptions, free trials and auto-renewal

Status as at 2026-08-05.

**The FTC "Click-to-Cancel" Rule is vacated. Do not cite it, and do not tell a client the obligations disappeared with it.** Both errors are made constantly, in opposite directions. The federal rule is gone; the substance survives through ROSCA, FTC Act § 5, and a state patchwork that is in several respects stricter than the vacated rule.

## What happened to the federal rule

The FTC's amended Negative Option Rule (16 CFR Part 425), adopted 15 November 2024 (89 Fed. Reg. 90476), was **vacated in its entirety** by the Eighth Circuit in *Custom Communications, Inc. v. FTC*, No. 24-3137 (8th Cir., 8 July 2025). The ground was procedural: the FTC skipped the preliminary regulatory analysis required by 15 U.S.C. § 57b-3(b)(1) after its own ALJ found the rule would exceed the $100 million threshold. The court declined to apply the rule's own severability clause: "vacatur of the entire Rule is appropriate." The compliance date had been deferred to 14 July 2025 — the rule was struck six days before it would have bitten, and **never took effect**.

What is left of Part 425 is the **1973 Prenotification Negative Option Plans rule** (§ 425.1), which reaches only book-of-the-month-club style prenotification plans. It does not reach continuity plans, automatic renewals or free-to-pay conversions.

The FTC published an **ANPRM on 13 March 2026** (Matter No. P064202) asking whether and how to re-regulate; comments closed 13 April 2026. `[[UNVERIFIED: any NPRM or final rule issued after 13 April 2026 — check federalregister.gov before advising]]`

## What actually binds — ROSCA, 15 U.S.C. § 8403

The Restore Online Shoppers' Confidence Act is untouched and is the operative federal law for any negative-option sale made **online**. It is unlawful to charge for goods or services sold through a negative-option feature on the internet unless the seller:

1. "provides text that clearly and conspicuously discloses all material terms of the transaction **before obtaining the consumer's billing information**";
2. "obtains a consumer's **express informed consent** before charging the consumer's credit card, debit card, bank account, or other financial account";
3. "provides **simple mechanisms** for a consumer to stop recurring charges".

ROSCA is enforced as an FTC Act violation, with civil penalties and consumer redress. The FTC's 2021 Enforcement Policy Statement Regarding Negative Option Marketing (86 Fed. Reg. 60822) remains the agency's stated approach.

## The state patchwork — this is where the real requirements live

Design to the strictest state in the customer footprint, not to the federal floor. Verified examples:

| State | Statute | Distinctive requirements |
|---|---|---|
| California | Bus. & Prof. Code §§ 17600–17606, as amended by AB 2863 (Ch. 515, approved 24 Sept 2024) | Applies to contracts **entered into, amended or extended on or after 1 July 2025** — it sweeps in legacy subscriptions. Express affirmative consent to the renewal terms **separately** from the rest of the transaction (§ 17602(a)(4)); retainable post-purchase acknowledgment with cancellation instructions (§ 17602(a)(3)); if enrolment was online, a prominent link or button permitting **immediate** termination without obstruction (§ 17602(d)); cancellation by the same medium used to enrol (§ 17602(f)); annual reminder notice (§ 17602(h)); consent records retained at least 3 years or 1 year after termination, whichever is longer. Free-to-pay conversions are expressly covered (§ 17601). |
| New York | Gen. Bus. Law § 527-a | Clear and conspicuous material terms before consent; affirmative agreement; cancellation "at any time using a simple cancellation mechanism" matching the medium of consent; written confirmation after consent; advance renewal notice **15–45 days** for terms of a year or more renewing for six months or more; trial notice **3–21 days** before the first charge for trials over a month; price increases need fresh consent or a 14-day cancellation window with pro-rata refund. |
| Colorado | C.R.S. § 6-1-732 | "A simple, cost-effective, timely, easy-to-use, and readily accessible mechanism" for cancellation — a **one-step online link**. Reminder **25–40 days before each automatic renewal**, not only annual ones. This is the tightest reminder cadence of the group. |
| Illinois | Automatic Contract Renewal Act, 815 ILCS 601/10 | Online enrolment ⇒ the consumer "must be allowed to terminate… **exclusively online**". Trials of 15+ days: notice at least 3 days before the cancellation deadline. Contracts of 12+ months: written notice 30–60 days before the cancellation deadline. |
| Virginia | Va. Code § 59.1-207.46 | Cancellation mechanism "at least as simple as" the enrolment method, available through all enrolment channels; **no forced live-agent interaction unless enrolment required one**. Free trials over 30 days: notice within 30 days of trial end. Renewals extending beyond 12 months: notice 30–60 days before the cancellation deadline. |

The common pattern across every state ARL:

1. Clear and conspicuous disclosure of the renewal terms **before** purchase, adjacent to the consent action.
2. **Affirmative consent to the renewal terms specifically**, not bundled into acceptance of the terms of service.
3. A retainable **post-purchase acknowledgment** containing the terms and the cancellation instructions.
4. **Cancellation at parity with enrolment.** Signed up online, cancels online, in the same number of steps.
5. **Renewal and trial reminders**, on cadences that differ per state.

`[[UNVERIFIED: whether Delaware has a standalone auto-renewal statute — do not assert one]]`

## Template — enrolment disclosure block

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<section aria-label="Subscription terms">
  <h3>Subscription terms</h3>
  <p>
    [[PLAN NAME]] renews automatically every [[INTERVAL]] at
    [[AMOUNT]] plus applicable taxes until you cancel.
    [[IF TRIAL: Your free trial lasts [[LENGTH]]. On [[DATE]] we will charge
    [[AMOUNT]] to the payment method you provide unless you cancel before
    that date.]]
    You can cancel at any time at [[CANCELLATION URL]] — the same place you
    signed up, in one step, without contacting us.
  </p>
  <label>
    <input type="checkbox" name="arl_consent" value="1">
    I agree to these automatic renewal terms.
  </label>
</section>
```

The checkbox must be separate from any terms-of-service acceptance checkbox and must not be pre-ticked. Record the display text version, timestamp and user identifier.

## Cancellation flow rules

- The cancellation route must be reachable from the account area without a search, and must terminate the subscription **in that flow**. A form that generates a ticket is not a cancellation mechanism.
- Retention offers may be presented, but the consumer must be able to decline in one action and complete the cancellation. An offer that must be declined three times is a dark pattern and an FTC Act § 5 target.
- Do not require a phone call, a live chat, or a mailed letter where enrolment was a click.
- Send a cancellation confirmation and stop billing at the end of the paid period.

## Checkpoints

- [ ] No text or code anywhere refers to the FTC "Click-to-Cancel" Rule or 16 CFR Part 425 as a live obligation
- [ ] All material terms disclosed before billing information is collected (15 U.S.C. § 8403(1))
- [ ] Separate, unchecked affirmative consent to the renewal terms, distinct from terms-of-service acceptance
- [ ] Post-purchase acknowledgment sent in a retainable form, containing cancellation instructions
- [ ] Online cancellation available in the same place as enrolment, completing in the flow, no live-agent requirement
- [ ] Retention offers declinable in one action
- [ ] Reminder notices scheduled to the strictest cadence in the customer footprint (Colorado's 25–40 days before **each** renewal is usually the binding constraint)
- [ ] Free-to-pay conversion notices scheduled (Illinois 3 days for 15+ day trials; New York 3–21 days; Virginia within 30 days of a 30+ day trial ending)
- [ ] Consent records retained for at least 3 years, or 1 year after termination, whichever is longer (Cal. Bus. & Prof. Code § 17602)
- [ ] Legacy subscriptions reviewed: California's amendments apply to contracts amended or extended on or after 1 July 2025
