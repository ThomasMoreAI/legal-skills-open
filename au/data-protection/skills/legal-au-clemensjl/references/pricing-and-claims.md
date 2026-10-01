# Pricing, claims and representations

The provisions that generate most ACCC enforcement against websites. Australian Consumer Law, Schedule 2 to the Competition and Consumer Act 2010 (Cth). Status as at 2026-08-05.

## Misleading or deceptive conduct — ACL s 18

A person must not, in trade or commerce, engage in conduct that is misleading or deceptive or likely to mislead or deceive. No intention is required, no consumer needs to have been misled, and it cannot be contracted out of. Silence can mislead where a reasonable person would expect disclosure. Section 18 does not itself attract a civil pecuniary penalty; the remedies are injunctions, damages, corrective advertising and compensation orders.

## False or misleading representations — ACL s 29

Section 29 lists specific false or misleading representations in connection with the supply or promotion of goods or services, including representations about standard, quality, value, grade, composition, style or model; about price; about testimonials; about the need for goods or services; and **about the existence, exclusion or effect of any condition, warranty, guarantee, right or remedy**. Unlike s 18, s 29 is a civil penalty provision and also a criminal offence provision under the parallel Part 4-1 offences.

**Maximum civil penalties.** For conduct on or after **28 March 2026** the fixed component for a body corporate is **$100,000,000**, following the Treasury Laws Amendment (Doubling Penalties for ACCC Enforcement) Act 2026 (No. 19, 2026, assented 27 March 2026). The maximum is the greatest of that fixed amount, three times the value of the benefit reasonably attributable to the conduct, or — where the benefit cannot be determined — 30% of adjusted turnover during the breach turnover period. For an individual the ACCC states a maximum of $2,500,000. (Source: ACCC, "Fines and penalties".)

## Single price — ACL s 48

Where a business represents part of the price of goods or services to a consumer, it must also specify, **as a single figure, the total price**, displayed **at least as prominently** as the component. The single price must include every tax, duty, fee, levy and additional charge that is quantifiable at the time — GST, airport taxes, mandatory booking or card fees, compulsory levies. It is unlawful to represent a component as the total price.

Practical consequences for a website:

- Prices to consumers are GST-inclusive. Displaying ex-GST prices to consumers with "+ GST" alongside breaches the rule unless the GST-inclusive total is at least as prominent and adjacent.
- A "from $X" price with mandatory fees added at checkout is drip pricing.
- Where the GST-exclusive price and the GST amount are shown separately, both must be close to, and no more prominent than, the GST-inclusive total.
- Optional extras genuinely chosen by the customer are not part of the single price. Delivery charges may be excluded from the single price if they cannot be quantified up front, but must still be disclosed; a delivery charge that is known must be disclosed prominently before the customer commits.
- Business-to-business pricing may be shown ex-GST, but the audience has to be genuinely business.

## "Was/now" and discount claims

A "was $X, now $Y" claim represents that the goods were previously sold at $X for a reasonable period immediately before the sale, in reasonable volumes. Keep the price history that proves it. Strike-through pricing, "RRP" claims and "up to 70% off" claims are all representations under s 29 and s 18. There is no Australian equivalent of the EU price-indication rule requiring the lowest price of the previous 30 days — but the underlying claim still has to be true, and the ACCC treats permanent "sales" as misleading.

## Unfair trading practices — from 1 July 2027

The **Competition and Consumer Amendment (Unfair Trading Practices) Act 2026** passed both Houses on 2 July 2026, received Royal Assent on 6 July 2026 and **commences 1 July 2027** (Treasury media release, 1 April 2026; parliamentary record). It amends the ACL to add:

- a general, principles-based prohibition on unfair trading conduct — conduct that manipulates a consumer or unreasonably distorts the consumer's decision-making environment and causes or is likely to cause detriment;
- a targeted drip pricing provision requiring mandatory per-transaction fees to be disclosed upfront and prominently;
- a subscription contract regime requiring disclosure of key terms before sign-up, reminders at critical points, and removal of unreasonable barriers to cancelling.

[[UNVERIFIED: the new section numbers reported by practitioner sources — a general prohibition at ACL s 28B, drip pricing at s 48A and subscriptions at ss 48B to 48H — were not confirmed against legislation.gov.au in this session. Cite the Act and the commencement date, not the section numbers, until confirmed.]]

Design decisions taken now that will fail in 2027: pre-ticked add-ons, cancel-by-phone-only subscriptions, countdown timers that reset, confirmshaming, and hidden mandatory fees. Fix them now — most are already exposed under ss 18, 29 and 48.

## Testimonials, reviews and endorsements

- A testimonial that was not given, or that has been edited so it no longer reflects what was said, is a false representation under s 29.
- Incentivised, solicited-only-from-happy-customers, or selectively filtered reviews are misleading under s 18. If reviews are moderated, disclose the moderation policy.
- Paid endorsements and affiliate content must be disclosed clearly and in the same medium; "#ad" buried in a hashtag block is not clear disclosure.
- Claims about products with a specific standard — organic, Australian Made, carbon neutral, hypoallergenic — need substantiation held before publication. The ACCC has published guidance on environmental and sustainability claims. [[UNVERIFIED: the title and date of the current ACCC greenwashing guidance were not checked in this session]]

## Scams Prevention Framework

The scams framework introduced by the Treasury Laws Amendment (Scams Prevention Framework) Act 2025 imposes obligations only on entities in **designated regulated sectors** — banking, telecommunications and digital platform services — designated by instrument (Competition and Consumer (Scams Prevention Framework—Regulated Sectors) Designation 2026, on the Federal Register of Legislation). An ordinary retail website is not caught. Check the designation before assuming otherwise.

## Template — pricing disclosures

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Prices</h2>
<p>All prices are shown in Australian dollars and include GST and all compulsory fees.
   [[Delivery charges are shown before you confirm your order / Delivery is $X per order.]]
   [[If any mandatory fee cannot be quantified up front, state what it is and how it is
   calculated.]]</p>

<h2>Discounts</h2>
<p>[[Where a "was" price is shown, it is the price at which we offered the item for sale
   for at least [[period]] immediately before this promotion.]]</p>

<h2>Subscriptions</h2>
<p>[[Term, renewal price, renewal date, how far in advance we remind you, and the
   cancellation route — which must be no harder than signing up.]]</p>
```

## Checkpoints

- [ ] Every consumer-facing price is a GST-inclusive single figure at least as prominent as any component
- [ ] Mandatory fees are in the headline price, not added at checkout
- [ ] Delivery charges disclosed before the customer commits
- [ ] "Was/now", "RRP" and percentage-off claims backed by price history held on file
- [ ] No permanent sale
- [ ] Countdown timers, stock counters and "X people viewing" reflect reality
- [ ] Testimonials are genuine, unedited in substance, and attributable
- [ ] Review collection and moderation practices disclosed
- [ ] Paid and affiliate content disclosed clearly in the same medium
- [ ] Environmental, origin and health claims substantiated before publication
- [ ] Subscription flows audited against the 1 July 2027 regime now, not in 2027
- [ ] Every `[[…]]` resolved or reported as `[[MISSING: …]]`
