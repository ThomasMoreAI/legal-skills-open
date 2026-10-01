# Selling online: returns, pricing, and sector-specific regimes

Status as at 2026-08-05.

## There is no US right of withdrawal

This is the single most damaging assumption imported from EU law. **No federal statute gives a consumer the right to cancel an ordinary online purchase.** There is no equivalent to the 14-day withdrawal right in Art 9 of Directive 2011/83/EU. Return rights in the United States are **contractual** — they exist because the seller published a return policy, and they extend exactly as far as that policy says.

The rule that agents mistake for a cooling-off right is the **FTC Cooling-Off Rule, 16 CFR Part 429** ("Rule Concerning Cooling-Off Period for Sales Made at Homes or at Certain Other Locations"). Its scope is narrow and physical:

- It applies to a sale, lease or rental of consumer goods or services in which the seller **personally solicits** the sale and the buyer's agreement is made at a place **other than the seller's place of business** — with a purchase price of **$25 or more at the buyer's residence** and **$130 or more at other locations** (16 CFR § 429.0(a)).
- The buyer gets three business days to cancel, and the seller must furnish a completed cancellation form.
- § 429.0(a) expressly excludes transactions "conducted and consummated entirely by mail or telephone; and without any other contact between the buyer and the seller … prior to delivery", along with sales following a visit to a fixed retail establishment, emergency repairs with a signed waiver, real property, insurance and securities.

It is a door-to-door and temporary-location rule. It does not create a return right for e-commerce, and saying it does is a material misstatement.

## Return policy disclosure duties

Because the right is contractual, the disclosure of the policy is where the law bites.

- **California, Cal. Civ. Code § 1723** — every retail seller whose policy is **not** to give a full cash or credit refund, or an equal exchange, for at least seven days after purchase with proof of purchase, must conspicuously display that policy: on signs at each cash register and sales counter, at each public entrance, on tags attached to each item, **or on the retail seller's order forms**. The display must state whether a cash refund, store credit or exchange is given, the time period, the merchandise covered, and any other conditions. A seller that fails to display is liable to a buyer who returns or attempts to return the goods within 30 days of purchase. Certain categories (perishables, custom goods and others listed in the section) are excluded.
- Several other states impose parallel posting or disclosure duties, and a number require the policy to be presented before the purchase is completed. `[[UNVERIFIED: the current list of states with mandatory return-policy disclosure statutes and their citations — verify against each target state's code before listing them in client-facing text]]`
- **Independently of any state statute, an unclear or unhonoured return policy is a deceptive practice under 15 U.S.C. § 45.** Publish the policy, place it before the point of purchase, and honour it exactly as written.

## What a US checkout must actually disclose

There is no FAGG-style catalogue of pre-contractual information. The operative constraints are FTC Act § 5 (nothing misleading, nothing material omitted), state consumer protection statutes ("little FTC Acts", most with private rights of action and fee shifting), and — for anything recurring — ROSCA and the state automatic renewal laws in `subscriptions-and-auto-renewal.md`.

The practical minimum before the buyer commits:

- Total price, with all mandatory fees included or itemised and unavoidable-fee totals shown up front. Drip pricing and mandatory fees revealed only at the last step are an active FTC and state AG enforcement target.
- Whether sales tax is added at checkout — US prices are conventionally quoted **exclusive** of sales tax, unlike EU practice, and stating a tax-inclusive price where tax varies by destination creates its own problem.
- Shipping cost and delivery window. Under the **FTC Mail, Internet or Telephone Order Merchandise Rule, 16 CFR Part 435**, a seller must have a reasonable basis to expect it can ship within the time stated, or within 30 days if no time is stated, and must offer the buyer a delay option or a prompt refund if it cannot.
- The return policy, before payment.
- For subscriptions: the recurring amount, the interval, the renewal terms and the cancellation method, presented before consent is taken.

## Template — return policy block

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h2>Returns and Refunds</h2>
<p>
  You may return [[ELIGIBLE ITEMS]] within [[NUMBER]] days of
  [[delivery / purchase]] for a [[full refund / store credit / exchange]],
  provided [[CONDITION, e.g. the item is unused and in its original
  packaging]].
</p>
<p>
  Items that cannot be returned: [[LIST — e.g. custom-made goods, perishable
  goods, digital downloads once accessed. State the actual exclusions; do not
  copy a list from another seller.]]
</p>
<p>
  To start a return, [[PROCESS]]. Return shipping is paid by
  [[the customer / us]]. Refunds are issued to the original payment method
  within [[NUMBER]] business days of our receiving the returned item.
</p>
<p>
  For [[SUBSCRIPTION / DIGITAL PRODUCT]] purchases, see [[LINK]].
</p>
<p>This policy was last updated on [[DATE]].</p>
```

The policy must be linked from the product page and from the checkout page, not only from the footer. Whatever it says is the contract, and the FTC and state attorneys general treat departures from it as deception under 15 U.S.C. § 45.

## Sector-specific regimes that catch ordinary sites

### GLBA and the FTC Safeguards Rule — 16 CFR Part 314

"Financial institution" for FTC purposes is far broader than banks: mortgage brokers, motor vehicle dealers, payday lenders, tax preparers, collection agencies, and businesses that act as "finders" bringing together buyers and sellers of financial products. A comprehensive written information security programme is required, with a designated qualified individual, risk assessment, access controls, encryption, MFA, vendor oversight and an incident response plan.

**§ 314.4(j)**, effective **13 May 2024**, requires notification to the FTC as soon as possible and **no later than 30 days after discovery** of a notification event — unauthorised acquisition of unencrypted customer information of **at least 500 consumers**. Encrypted information counts as unencrypted if the key was also accessed.

The GLBA Privacy Rule (Regulation P, 12 CFR Part 1016) governs the initial and annual privacy notices and the opt-out for sharing with non-affiliated third parties. GLBA-regulated data is exempt or partially exempt from most state comprehensive privacy laws — check the exemption in each state, because some exempt the **entity** and some only exempt the **data**.

### FERPA — 20 U.S.C. § 1232g, 34 CFR Part 99

Binds educational agencies and institutions receiving Department of Education funds, not vendors directly. An edtech vendor is pulled in through the **school official exception**, 34 CFR § 99.31(a)(1)(i)(B): an outside contractor, consultant, volunteer or provider of outsourced services may be treated as a school official if it performs an institutional service the institution would otherwise use employees for, **is under the direct control of the institution with respect to the use and maintenance of education records**, and is subject to the redisclosure limits of § 99.33(a). In practice this means the contract dictates the vendor's obligations — no advertising use, no redisclosure, and deletion on termination. State student-privacy statutes (notably California's SOPIPA) impose direct duties on operators and are often stricter.

### FCRA — 15 U.S.C. § 1681

Two ways an ordinary business is caught. As a **user of consumer reports** — running background checks on applicants, tenant screening, or any eligibility decision using a third-party report — the business must provide a **standalone written disclosure and obtain authorisation** under § 1681b(b)(2); the disclosure must consist solely of that disclosure, and burying it in an application form or adding a liability release defeats it. Adverse action then requires a pre-adverse-action notice with a copy of the report and the summary of rights, followed by an adverse action notice under § 1681m. As a **consumer reporting agency** — assembling or evaluating consumer information for the purpose of furnishing reports to third parties for eligibility decisions — the business takes on the full accuracy, dispute and permissible-purpose regime. Tenant screening, gig-worker vetting and "people search" products have all been treated as consumer reporting.

### Telemarketing Sales Rule — 16 CFR Part 310

Applies to telemarketing calls, including calls the seller makes to follow up on an online form fill, and to inbound calls responding to certain solicitations. It requires prescribed disclosures before the customer consents to pay, prohibits misrepresentations, restricts calling hours, requires compliance with the Do Not Call registry and the seller's internal list, and imposes recordkeeping duties. It sits alongside, not instead of, the TCPA — see `email-and-sms.md`.

## Checkpoints

- [ ] No text anywhere claims a statutory right to cancel, a cooling-off period, or a 14-day return window as a matter of law
- [ ] Return policy published, linked before payment, and honoured exactly as written
- [ ] California Civ. Code § 1723 display requirement satisfied if the policy is less generous than a 7-day full refund or exchange
- [ ] Total price including all mandatory fees shown before the buyer commits; no fees disclosed only at the final step
- [ ] Shipping timeframe stated with a reasonable basis, and the 16 CFR Part 435 delay/refund process implemented
- [ ] If any financial product, lending, tax or payment facilitation activity: Safeguards Rule programme in place and the § 314.4(j) 30-day FTC notification path documented
- [ ] If edtech: contracts satisfy 34 CFR § 99.31(a)(1)(i)(B), and no advertising use of student data
- [ ] If background or tenant screening: standalone § 1681b(b)(2) disclosure, and the two-step adverse action process implemented
- [ ] If outbound calls follow online submissions: TSR disclosures, calling hours, and Do Not Call scrubbing in place
