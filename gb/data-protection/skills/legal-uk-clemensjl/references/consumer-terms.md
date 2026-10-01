# Consumer terms and statutory rights

The Consumer Rights Act 2015 (c. 15) supplies the rights. Terms and conditions cannot reduce them, and a term that tries to is not binding. Status as at 2026-08-05: Part 1 and Part 2 in force.

Structure: Part 1 Chapter 2 goods (ss 3–32), Chapter 3 digital content (ss 33–47), Chapter 4 services (ss 48–57), Chapter 5 general (ss 58–60); Part 2 unfair terms (ss 61–76).

## Goods — ss 9–11 and the remedies

Every contract to supply goods to a consumer is treated as including terms that the goods are:

- of satisfactory quality (s 9) — the standard a reasonable person would consider satisfactory, taking account of description, price and all other relevant circumstances, including fitness for all purposes for which goods of that kind are usually supplied, appearance and finish, freedom from minor defects, safety and durability
- fit for a particular purpose made known to the trader (s 10)
- as described (s 11), including matching any pre-contract information given under the CCRs 2013

Remedies, ss 19–24:

| Remedy | Section | Timing |
|---|---|---|
| Short-term right to reject and get a refund | s 20, with the time limit in s 22 | 30 days from ownership, delivery and (where relevant) installation |
| Repair or replacement | s 23 | Within a reasonable time and without significant inconvenience |
| Price reduction or final right to reject | s 24 | After one failed repair or replacement |

A deduction for use may only be made on a final rejection, and not within the first six months except for motor vehicles (s 24(8)–(10)). Where a fault appears within six months of delivery it is taken to have been present at delivery unless the trader proves otherwise (s 19(14)–(15)).

## Digital content — ss 34–36 and 42–45

The same three implied terms apply to digital content: satisfactory quality (s 34), fit for particular purpose (s 35), as described (s 36). Remedies under s 42: repair or replacement, then price reduction. There is no short-term right to reject for digital content. Section 46 gives a right to compensation where digital content damages a device or other digital content and the trader failed to exercise reasonable care and skill.

There is no UK equivalent of the EU Digital Content Directive's ongoing update obligation as a standalone statutory duty; supply of updates is dealt with through the quality and description terms and through what the contract promises.

## Services — ss 49–52

Implied terms: performed with reasonable care and skill (s 49); information said by the trader about the service or the trader, on which the consumer relies, is binding (s 50); a reasonable price where none is fixed (s 51); performance within a reasonable time where none is fixed (s 52). Remedies under ss 55–56: repeat performance, then price reduction.

## Non-excludability

Sections 31 (goods), 47 (digital content) and 57 (services) make terms void to the extent they exclude or restrict liability under the implied terms, or restrict the remedies. Section 57(1) also prohibits excluding liability for failure to perform with reasonable care and skill. Section 65 makes void any term excluding liability for death or personal injury from negligence.

## Unfair terms — Part 2

Section 62: an unfair term of a consumer contract is not binding on the consumer; the same applies to consumer notices. A term is unfair if, contrary to the requirement of good faith, it causes a significant imbalance in the parties' rights and obligations to the detriment of the consumer. Section 68 requires written terms to be transparent — expressed in plain and intelligible language and legible. Section 69 resolves ambiguity in the consumer's favour.

Schedule 2 lists terms that may be regarded as unfair. The ones that appear most often in copied templates:

- excluding or limiting liability for the trader's breach
- allowing the trader to alter the terms, the service or the price unilaterally without a valid reason and without a right to exit
- binding the consumer while the trader's own performance is discretionary
- requiring a consumer who fails to perform to pay a disproportionately high sum
- excluding or hindering the consumer's right to take legal action, in particular by requiring arbitration not covered by legal provisions
- automatic extension of a fixed-term contract where the deadline for objecting is unreasonably early

Section 64 exempts the main subject matter and the price from the fairness assessment only if the term is transparent and prominent.

## Template skeleton

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h1>Terms and conditions</h1>

<h2>1. Who we are</h2>
<p>[[registered name, number, part of the UK, registered office, email — see website-disclosures.md]]</p>

<h2>2. These terms</h2>
<p>Which contracts they apply to, and that nothing in them affects the customer's statutory rights.</p>

<h2>3. How the contract is formed</h2>
<p>Order, acknowledgement, acceptance, and the point at which the contract comes into existence.</p>

<h2>4. Price and payment</h2>
<p>Total price including taxes, all compulsory charges shown up front, delivery charges, payment methods, when payment is taken.</p>

<h2>5. Delivery or performance</h2>
<p>Timescales, delivery restrictions, what happens if delivery fails, risk and ownership.</p>

<h2>6. Your right to cancel</h2>
<p>[[see cancellation.md — 14 days, model cancellation form]]</p>

<h2>7. Your statutory rights</h2>
<p>
  Goods must be of satisfactory quality, fit for purpose and as described (Consumer Rights Act 2015,
  sections 9 to 11). Digital content must meet the same standards (sections 34 to 36). Services must
  be performed with reasonable care and skill (section 49). Nothing in these terms affects those
  rights. [[If a commercial guarantee is offered, describe it here and state that it is in addition to,
  and does not affect, these rights.]]
</p>

<h2>8. Our liability</h2>
<p>[[no exclusion of liability for death or personal injury from negligence (s 65), for fraud, or under the implied terms (ss 31, 47, 57)]]</p>

<h2>9. Complaints</h2>
<p>[[see complaints-adr.md]]</p>

<h2>10. Governing law</h2>
<p>
  These terms are governed by the law of [[England and Wales / Scotland / Northern Ireland]].
  [[Consumers keep the protection of the mandatory rules of the country where they live.]]
</p>
```

## Checkpoints

- [ ] Statutory rights described using the CRA 2015 sections, not called a "warranty"
- [ ] No exclusion or restriction of the implied terms (ss 31, 47, 57) or of liability for death or personal injury (s 65)
- [ ] Short-term right to reject stated as 30 days for goods (s 22), and not offered for digital content where it does not exist
- [ ] Six-month reversed burden of proof not contradicted by a "faults must be reported within 14 days" clause
- [ ] Unilateral variation clauses have a valid stated reason and a right to exit (Sch 2)
- [ ] No compulsory arbitration or class-action waiver against consumers (Sch 2, s 62)
- [ ] Terms are plain, legible and available before the order (s 68)
- [ ] Price and main subject matter transparent and prominent if reliance is placed on s 64
- [ ] Any commercial guarantee stated as additional to statutory rights
- [ ] Governing law clause names a UK jurisdiction, not a foreign one, and does not strip mandatory consumer protection
- [ ] No US-style limitation-of-liability boilerplate, no "AS IS" disclaimer against consumers
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
