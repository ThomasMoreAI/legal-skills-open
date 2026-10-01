# Terms of service

Terms are a contract, not a disclosure. Nothing in Australian law requires a website to publish terms — but once published and incorporated, they bind, and the two provisions that decide whether they survive are ACL s 64 and the unfair contract terms regime in ACL Part 2-3 (ss 23–28). Status as at 2026-08-05.

## Incorporation

Terms bind only if the customer had reasonable notice of them before contracting.

- **Clickwrap** — an unticked checkbox next to a link, ticked before the order or account is created, with the version recorded against the account. This is what holds up.
- **Browsewrap** — a footer link with "by using this site you agree". Weak, and weaker still for onerous terms.
- Terms cannot be varied unilaterally without a mechanism, and a broad unilateral variation right is itself a candidate unfair term.
- Keep every version with a date. A dispute is about the terms in force on the day of the transaction.

## Unfair contract terms — ACL ss 23–28

Applies to **standard form contracts** with a **consumer** or a **small business**. Since **9 November 2023** proposing, applying or relying on an unfair term in such a contract is unlawful and attracts civil penalties; each unfair term is a separate contravention. A court may also declare a term void, vary the contract or grant an injunction.

Small business threshold from 9 November 2023: the business employs **fewer than 100 people** or has an **annual turnover under $10 million**. Under the ACL the monetary contract-value threshold was removed entirely; under the ASIC Act the regime applies to a small business contract only where the upfront price payable, excluding interest, is $5 million or less. (Sources: ACCC and ASIC guidance.)

A term is unfair if it would cause a significant imbalance in the parties' rights and obligations, is not reasonably necessary to protect the legitimate interests of the party advantaged by it, and would cause detriment to another party if applied or relied on. Terms defining the main subject matter, setting the upfront price, or required by law are excluded from review.

Terms that regularly fail:

- unilateral variation of price, service or terms without notice and without a right to exit
- automatic renewal with a long notice period or no reminder
- broad exclusions or caps on liability
- termination rights for one side only, or disproportionate termination fees
- unilateral determination of whether a breach has occurred
- limitation of the customer's right to sue, or forcing a foreign forum
- indemnities that make the customer liable for the business's own conduct
- terms permitting the business to assign the contract to anyone's detriment

Minor negotiated changes do not take a contract out of "standard form".

## Liability

**A blanket exclusion of liability is void to the extent it purports to exclude, restrict or modify the consumer guarantees (ACL s 64).** Write the carve-out explicitly rather than relying on a severance clause.

Where the goods or services are **not** of a kind ordinarily acquired for personal, domestic or household use or consumption, liability for breach of a guarantee may be limited to repair, replacement or resupply, or the cost of doing so, if that limitation is fair and reasonable (ACL s 64A). This is the only cap that works against the guarantees, and it does not work for consumer-grade products.

Misleading or deceptive conduct under ACL s 18 cannot be contracted out of at all. An entire-agreement or no-reliance clause does not defeat an s 18 claim.

A workable structure:

1. state that nothing in the terms excludes, restricts or modifies any guarantee, right or remedy under the ACL that cannot be excluded;
2. cap remaining liability, with the s 64A limitation stated where the supply is non-consumer-grade;
3. exclude indirect and consequential loss;
4. keep the cap proportionate to the fees paid — an unfairly low cap is itself a candidate unfair term.

## Jurisdiction and governing law

Choose the law and courts of an Australian state or territory, named. Foreign law and exclusive foreign jurisdiction clauses against Australian consumers are candidate unfair terms and do not displace the ACL, which applies to conduct in Australia and to conduct outside Australia by entities carrying on business in Australia.

Do not include an arbitration clause or class action waiver against consumers. Do not point consumers at the ACCC as a dispute resolution route — the ACCC does not resolve individual disputes. Point them at the relevant state or territory fair trading agency and the relevant civil and administrative tribunal.

There is no Australian equivalent of the EU ODR platform. If an existing text links to it, delete the link: the platform ceased operating on 20 July 2025.

## Template — skeleton

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<h1>Terms of Service</h1>
<p>These terms apply between you and [[legal entity name]] (ABN [[ABN]]) of
   [[address]]. Version [[n]], effective [[date]].</p>

<h2>1. Who we are and how to contact us</h2>
<h2>2. Your account</h2>
<h2>3. What we supply</h2>
<h2>4. Orders and acceptance</h2>
<p>[[When the contract is formed — on our acceptance, not on your order. Order
   confirmation wording must match.]]</p>
<h2>5. Prices and payment</h2>
<p>All prices are in Australian dollars and include GST unless stated. See our pricing
   page for delivery charges. [[If subscription: renewal term, renewal price, notice we
   give before renewal, and how to cancel — cancellation must not be harder than
   signing up.]]</p>
<h2>6. Delivery</h2>
<h2>7. Your consumer guarantees</h2>
<p>Our goods and services come with guarantees under the Australian Consumer Law that
   cannot be excluded. Nothing in these terms excludes, restricts or modifies any
   guarantee, right or remedy you have under the Australian Consumer Law that cannot
   lawfully be excluded, restricted or modified. See our returns policy at [[link]].</p>
<h2>8. Acceptable use</h2>
<h2>9. Your content</h2>
<p>[[Licence you take over user content — limited to what the service actually needs.
   A perpetual worldwide sublicensable licence over personal content is a candidate
   unfair term.]]</p>
<h2>10. Intellectual property</h2>
<h2>11. Suspension and termination</h2>
<p>[[Symmetrical where possible; notice period; what happens to prepaid amounts and to
   the customer's data on termination.]]</p>
<h2>12. Liability</h2>
<p>Nothing in these terms excludes, restricts or modifies the consumer guarantees. Subject
   to that, our liability [[cap]]. [[Where the supply is not of a kind ordinarily acquired
   for personal, domestic or household use, our liability for failure to comply with a
   guarantee is limited to (as applicable) repair, replacement or resupply of the goods or
   services, or payment of the cost of doing so.]]</p>
<h2>13. Privacy</h2>
<p>We handle personal information as described in our Privacy Policy at [[link]].</p>
<h2>14. Changes to these terms</h2>
<p>[[Notice period, how notified, and the customer's right to end the contract without
   penalty if they do not accept the change.]]</p>
<h2>15. Complaints and disputes</h2>
<p>[[Internal complaint route with a response time. Then the state or territory fair
   trading agency and tribunal. No ODR link. No mandatory arbitration.]]</p>
<h2>16. Governing law</h2>
<p>These terms are governed by the laws of [[state or territory]], and the courts of
   [[state or territory]] have non-exclusive jurisdiction.</p>
```

## Checkpoints

- [ ] Acceptance is an affirmative, unticked action recorded with the version and timestamp
- [ ] Every version retained with its effective dates
- [ ] Explicit statement that the consumer guarantees are not excluded, placed before the liability cap
- [ ] Liability cap does not purport to override the guarantees; s 64A limitation used only where the supply is genuinely non-consumer-grade
- [ ] No entire-agreement or no-reliance clause presented as defeating ACL s 18
- [ ] Terms reviewed line by line against the unfair contract terms criteria, with unilateral variation, auto-renewal, termination and indemnity clauses given specific attention
- [ ] Small business counterparties considered, not just consumers
- [ ] Governing law and forum are an Australian state or territory, named
- [ ] No mandatory arbitration or class action waiver against consumers
- [ ] No link to the EU ODR platform anywhere in the project
- [ ] Cancellation route for subscriptions no harder than signup
- [ ] Every `[[…]]` resolved or reported as `[[MISSING: …]]`
