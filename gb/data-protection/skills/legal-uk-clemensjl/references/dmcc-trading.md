# Unfair commercial practices — DMCC Act 2024

The Digital Markets, Competition and Consumers Act 2024 (c. 13), Part 4 Chapter 1, replaced the Consumer Protection from Unfair Trading Regulations 2008 on 6 April 2025 (Commencement No. 2 Regulations 2025). CPUT 2008 is revoked and survives only for conduct before that date. Any citation of CPUT for current conduct is wrong.

Status as at 2026-08-05: Part 4 Chapter 1 (ss 225–230) and Schedule 20 in force since 6 April 2025; Chapter 2 (subscription contracts, ss 253–281) not in force; Chapter 4 (ADR, ss 291–310) in force since 6 April 2026.

## The prohibition

- **s 225** — unfair commercial practices are prohibited
- **s 226** — misleading actions: false or deceptive information, including about the main characteristics, price, and the trader's own status
- **s 227** — misleading omissions: omitting material information the average consumer needs to take an informed transactional decision, or providing it in an unclear, unintelligible, ambiguous or untimely manner
- **s 228** — aggressive practices: harassment, coercion or undue influence
- **s 229** — contravention of the requirements of professional diligence
- **s 230** — omission of material information from an invitation to purchase
- **Schedule 20** — 32 practices unfair in all circumstances, with no need to show any effect on the consumer

The test changed from CPUT: a practice is unfair where it is likely to cause the average consumer to take a transactional decision they would not otherwise have taken.

## Drip pricing — s 230

An invitation to purchase must include, among other things, the total price of the product or, where it cannot reasonably be calculated in advance, the manner in which it will be calculated. Section 230 defines the total price as including any fees, taxes, charges or other payments the consumer will necessarily incur if they buy. Freight, delivery or postal charges not included in the total price must be stated separately. Omission includes providing the information in an unclear or untimely manner, or where the consumer is unlikely to notice it.

Consequences for a checkout flow: compulsory booking fees, service fees, mandatory insurance and unavoidable card surcharges belong in the headline price, not on the final screen. Genuinely optional extras and charges that vary with a choice the consumer has not yet made can be presented separately, but must be prominent and given in good time.

## Fake and manipulated reviews — Schedule 20 paragraph 13

Status as at 2026-08-05: in force since 6 April 2025. Paragraph 13 covers, in all circumstances:

- submitting or commissioning a fake consumer review, or one that conceals that it was incentivised
- publishing consumer reviews, or consumer review information, in a misleading way — including presenting positive reviews selectively over negative ones, or omitting relevant context about how reviews were obtained
- failing to take reasonable and proportionate steps to prevent and remove fake reviews, concealed incentivised reviews, and misleading review information
- offering services that facilitate any of the above

Paragraph 12 separately bans using editorial content in the media to promote a product where the trader has paid for it without making that clear. Paragraph 4 bans falsely claiming approval or endorsement.

Practical consequences: an incentivised review must be labelled as incentivised at the point it is displayed; review filtering that suppresses negative reviews is a banned practice; and an operator hosting reviews owes an active duty to police them, not merely to refrain from writing them.

## Subscription contracts — not in force

Part 4 Chapter 2 (ss 253–281) creates a full subscription regime: pre-contract information, reminder notices before auto-renewal, end-of-contract notices, cooling-off periods on renewal with proportionate refunds, and a prohibition on cancellation arrangements that are disproportionately difficult.

None of it is in force. The Department for Business and Trade published its consultation response on 2 April 2026 and put commencement at spring 2027, after a first delay from an earlier target. The regime depends on secondary legislation that has not been made.

Rules for drafting: describe the regime as forthcoming, dated as an expectation and not a commitment, and never write a clause that asserts a current statutory duty to send renewal reminders or grant renewal cooling-off periods. Existing subscription obligations come from elsewhere — the CCRs 2013 information duties, the CRA 2015 unfair terms rules on automatic extension (Sch 2), and s 227 DMCC on misleading omissions about renewal and cancellation.

## Enforcement

Since 6 April 2025 the CMA can enforce consumer law directly, by administrative decision, without going to court. It can issue provisional and final infringement notices, give directions including enhanced consumer measures and redress, and impose penalties of up to the higher of 10% of global turnover or £300,000 for a business, and up to £300,000 for an individual. Separate penalties apply for breaching directions or undertakings. Trading Standards services and sector regulators retain their own enforcement routes.

The CMA opened its first tranche of eight direct enforcement investigations on 18 November 2025, focused on online pricing practices including drip pricing and pressure selling.

Sections 232–235 give consumers private rights of redress — the right to unwind, a discount, and damages — for misleading and aggressive practices. These sit alongside the Consumer Rights Act 2015 remedies rather than replacing them, so a single defective transaction can generate both a CRA claim and a DMCC redress claim.

## Templates

Reviews policy, published wherever reviews are displayed:

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>How we handle reviews</h2>
<p>
  Reviews on this site come from [[who can leave a review: verified purchasers only / anyone with an
  account / imported from [[platform]]]].
</p>
<p>
  [[If incentives are used:]] We [[offer [[incentive]] for leaving a review]]. Reviews written after an
  incentive was offered are labelled "Incentivised" wherever they appear.
  [[If no incentives are used:]] We do not offer anything in exchange for reviews.
</p>
<p>
  Reviews are shown [[default ordering]]. You can sort and filter them yourself.
  We do not delete a review because it is negative. We remove reviews that
  [[criteria: abusive, off-topic, identifiable as fake]], and we check for fake reviews by
  [[method]].
</p>
<p>The overall rating shown is [[how it is calculated, and which reviews it includes]].</p>
```

Price display block for a product or booking page:

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<p class="price">
  <strong>[[total price including VAT and all compulsory fees]]</strong>
  <span>Includes [[named compulsory fees: booking fee, service charge, mandatory insurance]].</span>
  <span>Delivery: [[amount]] [[or: calculated at checkout, from [[amount]]]].</span>
  <span>[[Optional extras are listed separately and are not included in this price.]]</span>
</p>
```

Neither block is a statutory form. They exist because ss 227 and 230 are drafted as omissions tests, so the compliant version of a page is the one that states the facts a consumer needs before deciding.

## Checkpoints

- [ ] No citation of the Consumer Protection from Unfair Trading Regulations 2008 for post-6 April 2025 conduct
- [ ] Headline price includes every charge the consumer will necessarily incur (s 230)
- [ ] Delivery and postal charges stated separately and prominently where not in the total price
- [ ] No compulsory fee first revealed at the final checkout step
- [ ] Countdown timers, "only 2 left" and "12 people viewing" claims are true and evidenced (ss 226, 228, Sch 20)
- [ ] Reference-price and "was/now" claims evidenced by genuine prior selling prices
- [ ] Incentivised reviews labelled as incentivised where they are displayed (Sch 20 para 13)
- [ ] No suppression or reordering of reviews that misrepresents the overall picture
- [ ] Documented process for detecting and removing fake reviews, proportionate to the volume hosted
- [ ] Paid editorial and influencer content disclosed (Sch 20 para 12, CAP Code rule 2.4)
- [ ] Environmental and "sustainable" claims substantiated and specific (s 226)
- [ ] No subscription clause asserting a DMCC duty that is not yet in force
- [ ] Renewal, price-change and cancellation terms reviewed against CRA 2015 Sch 2 and s 227 DMCC
