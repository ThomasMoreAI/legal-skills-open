# Advertising, reviews, endorsements and dark patterns

Status as at 2026-08-05.

There is no US pre-approval regime for advertising and no mandatory disclosure catalogue. The governing instrument is a two-sentence prohibition, applied case by case, backed by a rule with civil penalties for the review-and-testimonial subset.

## FTC Act § 5 — 15 U.S.C. § 45

**§ 45(a)(1):** "Unfair methods of competition in or affecting commerce, and unfair or deceptive acts or practices in or affecting commerce, are hereby declared unlawful."

**Deception** is not codified. It comes from the FTC's 1983 Policy Statement on Deception: a representation, omission or practice that is **likely to mislead a consumer acting reasonably under the circumstances**, and that is **material**. There is no intent requirement and no requirement that anyone was actually misled.

**Unfairness** is codified at **§ 45(n)**: the Commission may not declare an act unfair "unless the act or practice causes or is likely to cause **substantial injury to consumers which is not reasonably avoidable by consumers themselves and not outweighed by countervailing benefits to consumers or to competition**."

Two consequences that matter more than they look:

- **Every voluntary statement in a privacy policy becomes enforceable.** A policy promising "we never sell your data" while an advertising pixel is live is a § 5 deception. Over-promising in a copied template is the most common way a US company creates liability it did not have.
- **Every state has a "little FTC Act"** — a UDAP statute mirroring § 5. Most carry a private right of action, many with statutory damages and fee shifting. The FTC is not the only, or usually the first, enforcer.

## Rule on the Use of Consumer Reviews and Testimonials — 16 CFR Part 465

Published 22 August 2024 (89 Fed. Reg. 68034), **effective 21 October 2024**, in force. This is a § 18 trade regulation rule, so violations trigger civil penalties under 15 U.S.C. § 45(m)(1)(A) — **per violation**, which in review cases can mean per fake review.

| Section | Prohibits |
|---|---|
| § 465.2 | Fake or false consumer reviews, consumer testimonials, or celebrity testimonials — including reviews by people who do not exist, who did not use the product, or who materially misrepresent their experience |
| § 465.3 | **[Reserved]** — the proposed provision on reusing and repurposing reviews was not adopted |
| § 465.4 | Buying positive or negative consumer reviews — providing compensation conditioned on the review expressing a particular sentiment |
| § 465.5 | Insider consumer reviews and testimonials without clear and conspicuous disclosure of the connection (officers, managers, employees, their relatives, and solicitation of these) |
| § 465.6 | Company-controlled review websites or entities presented as independent |
| § 465.7 | Review suppression — using unfounded or groundless legal threats, physical threats, intimidation, or public false accusations to prevent or remove a negative review; and misrepresenting that the reviews on a site represent all or most reviews when negative ones have been suppressed |
| § 465.8 | Misuse of fake indicators of social media influence — buying or selling fake followers, views or engagement |

Note the section numbering carefully: § 465.3 is reserved, so buying reviews is **§ 465.4**, not § 465.3. Getting these numbers wrong is the giveaway of an unverified citation.

Practical consequences for a normal site: incentivised reviews are permitted only if the incentive is not conditioned on sentiment and the incentive is disclosed; employee reviews must be labelled; a review widget that filters out one- and two-star reviews while implying completeness violates § 465.7; and a "verified reviews" badge must be true.

## Endorsement Guides — 16 CFR Part 255

Revised at 88 Fed. Reg. 48102, 26 July 2023. Sections: § 255.0 purpose and definitions, § 255.1 general considerations, § 255.2 consumer endorsements, § 255.3 expert endorsements, § 255.4 endorsements by organizations, § 255.5 disclosure of material connections, § 255.6 endorsements directed to children.

Core duty (§ 255.5): where a **material connection** exists between endorser and advertiser — one the audience would not reasonably expect and that would affect the weight or credibility given to the endorsement — it must be **clearly and conspicuously disclosed**. Material connections include payment, free or discounted product, affiliate commission, employment, a family or business relationship, and contest entry.

**Status distinction that matters.** Part 255 comprises administrative interpretations — **guides, not legislative rules.** They are not independently enforceable and carry no direct civil penalties. Liability runs through § 5, or through Part 465 where the same conduct also breaches that rule. Part 465 exists precisely because the Guides never had a penalty hook. Do not describe the Endorsement Guides as a rule with penalties.

Disclosure mechanics that survive scrutiny: the disclosure appears in the endorsement itself, above the fold, in the same medium and language, unavoidable without clicking "more", and in plain words ("Paid partnership with X", "X sent me this free"). Platform disclosure tools alone are treated as insufficient. "#ad" buried in a block of hashtags is not clear and conspicuous. Both the brand and the influencer can be liable, and the brand is expected to have a written policy, to train endorsers, and to monitor.

## Made in USA Labeling Rule — 16 CFR Part 323

Published 14 July 2021 (86 Fed. Reg. 37022), **effective 13 August 2021**. § 323.2 makes it an unfair or deceptive act to label a product Made in the United States unless three cumulative conditions hold: "the final assembly or processing of the product occurs in the United States, all significant processing that goes into the product occurs in the United States, and **all or virtually all** ingredients or components of the product are made and sourced in the United States." It applies to labels and, under § 323.3, to mail order advertising including online. Enacted under 15 U.S.C. § 45a, so civil penalties under § 45(m)(1)(A) apply.

Qualified claims ("Assembled in USA from imported components", "70% US content") are permitted if accurate and non-misleading.

## Dark patterns

**There is no FTC dark-patterns rule.** The nearest thing was the negative option rule, which was vacated — see `subscriptions-and-auto-renewal.md`. What exists is § 5 case-by-case enforcement, ROSCA for online negative options, state UDAP statutes, and state statutory definitions. California defines a dark pattern at Cal. Civ. Code § 1798.140(*l*) as "a user interface designed or manipulated with the substantial effect of subverting or impairing user autonomy, decisionmaking, or choice", and under the CCPA regulations an interface that is a dark pattern **does not produce valid consent** — that is the concrete legal consequence, not a fine.

Patterns that draw enforcement: drip pricing and mandatory fees revealed at the last step; pre-checked add-ons; confirmshaming; asymmetric consent buttons; cancellation flows longer than signup flows; countdown timers that reset; "only 2 left" scarcity claims that are false.

## Pricing and comparison claims

- A "was $X, now $Y" reference price must be a genuine former price at which the product was offered in good faith for a reasonable period.
- "Free" offers require clear and conspicuous disclosure of the conditions, and the price of the item that must be purchased must not be inflated to cover the free one.
- Mandatory fees should be included in the advertised price or disclosed up front; several states have enacted junk-fee statutes requiring the total price to be the advertised price. `[[UNVERIFIED: the current list of state junk-fee/all-in pricing statutes and their effective dates — verify per target state]]`

## Checkpoints

- [ ] Every claim on the site traced to substantiation held before the claim was published
- [ ] Privacy policy and marketing copy checked against actual data practices — no promise the business does not keep
- [ ] Reviews: no fabricated, purchased-for-sentiment, or undisclosed insider reviews (16 CFR §§ 465.2, 465.4, 465.5)
- [ ] Review display not filtered to suppress negatives while implying completeness (§ 465.7)
- [ ] No legal threats used against reviewers (§ 465.7)
- [ ] No purchased followers or engagement (§ 465.8)
- [ ] Incentivised reviews: incentive disclosed and not conditioned on sentiment
- [ ] Influencer and affiliate disclosures in the endorsement itself, above the fold, in plain words (16 CFR § 255.5)
- [ ] Written endorser policy exists and endorsers are monitored
- [ ] Any "Made in USA" claim tested against all three conditions of 16 CFR § 323.2
- [ ] Reference prices are genuine former prices
- [ ] Total price with mandatory fees shown before the final step
- [ ] Consent interfaces reviewed against the dark-pattern definition — asymmetric buttons invalidate the consent they collect
