# Selling into the EU from Switzerland

Most Swiss shops sell into the EU. When they do, a second, stricter body of law applies to that part of the business in parallel with Swiss law. This file states the parallel duties compactly; it does not replace EU-specific advice. Status as at 2026-08-05.

## When EU law bites

Two different tests, often confused.

- **Data protection.** Art. 3(2) GDPR: the Regulation applies to processing of personal data of data subjects **who are in the Union** by a controller or processor not established in the Union, where the processing relates to (a) the offering of goods or services to such data subjects, irrespective of whether payment is required, or (b) the monitoring of their behaviour as far as it takes place within the Union.
- **Contract law.** Art. 6(1) Rome I (Regulation (EC) No 593/2008): a consumer contract is governed by the law of the consumer's habitual residence where the professional pursues its activities in that country, or **by any means directs such activities** to that country, and the contract falls within the scope of those activities. Art. 6(2): a choice of law is permitted but **may not deprive the consumer of the protection of the mandatory provisions** that would apply absent the choice.

So a choice of Swiss law in the AGB does not remove EU consumer protection from a German or French consumer whom the shop targeted. Evidence of targeting: language versions, currency, delivery zones, EU top-level domains, EU telephone numbers, EU-directed advertising.

**Jurisdiction.** Switzerland and the EU are both parties to the Lugano Convention of 2007. Its protective jurisdiction rules for consumer contracts allow a consumer to sue in their own domicile and require the trader to sue there, and they limit the effect of jurisdiction clauses agreed before the dispute arises. Check the Convention text before drafting a jurisdiction clause for an EU-facing shop.

## Which act bites on which trigger

| Trigger | EU act | Practical consequence |
|---|---|---|
| Personal data of people in the EU, offering or monitoring | GDPR Art. 3(2) | Full GDPR on top of the DSG, Art. 27 representative, consent banner |
| Consumer contract directed at an EU country | Rome I Art. 6, Directive 2011/83/EU | Mandatory consumer protection of the consumer's residence, 14-day withdrawal right |
| Goods sold to EU consumers | Directives (EU) 2019/770 and 2019/771 | Conformity regime that cannot be contracted out of |
| Consumer products placed on the EU market | Regulation (EU) 2023/988 | EU-established responsible person under Art. 16 |
| E-commerce service to EU consumers | Directive (EU) 2019/882 | Accessibility of the EU-facing offering from 28 June 2025 |
| Intermediary service with EU users | Regulation (EU) 2022/2065 | DSA machinery and an EU legal representative |
| Intermediation service used by EU-established business users to reach EU consumers | Regulation (EU) 2019/1150 | P2B transparency, ranking disclosure and redress duties in the platform terms, irrespective of where the provider is established |

Deciding "we do not target the EU" is a legitimate answer, but it has to be implemented: no EU delivery zones, no EUR pricing, no EU-language versions aimed at EU customers, no EU-targeted advertising. A disclaimer alone does not undo evidence of targeting.

## GDPR

Where Art. 3(2) GDPR applies, the full Regulation applies to that processing, on top of the DSG. The practical deltas against a Swiss-only setup:

| Duty | What changes |
|---|---|
| Legal basis | Every processing needs an Art. 6 GDPR basis, stated in the notice (Art. 13(1)(c)) |
| Consent for cookies | Prior, informed, freely given, unambiguous consent for non-essential cookies under the national ePrivacy implementations; reject as easy as accept; nothing fires before the decision; consent logged |
| Representative | Art. 27 GDPR: a representative in a Member State where the data subjects are, designated in writing, unless the Art. 27(2)(a) exemption applies |
| Breach notification | Art. 33 GDPR: 72 hours to the supervisory authority unless the breach is unlikely to result in a risk — a different trigger and a hard deadline compared with Art. 24 DSG |
| Records | Art. 30 GDPR with its own exemption logic, which is not the Art. 24 DSV exemption |
| Rights | Arts. 15–22 GDPR, including the standalone right to object under Art. 21 and erasure under Art. 17 |
| Sanctions | Administrative fines against the undertaking under Art. 83 GDPR, in addition to Swiss criminal fines against individuals |

The Swiss adequacy status under EU law and the Swiss adequacy list in Anhang 1 DSV both govern transfers. Neither removes the GDPR's applicability to a Swiss controller under Art. 3(2).

## Consumer Rights Directive: the withdrawal right returns

Directive 2011/83/EU, Art. 9(1): save where the exceptions in Art. 16 apply, the consumer has **14 days** to withdraw from a distance or off-premises contract, without giving any reason and without incurring costs beyond those in Arts. 13(2) and 14. Art. 6 sets the pre-contractual information duties for distance contracts, including the conditions, period and procedure for exercising withdrawal, and the model withdrawal form.

This is the mirror image of the Swiss position. A shop serving both markets needs **two** sets of terms, or one set that grants the EU standard to everyone. Granting the 14-day right to all customers is the simplest safe design; splitting by delivery address is defensible but must be implemented consistently in the checkout, the confirmation email and the terms.

The Sale of Goods Directive (EU) 2019/771 and the Digital Content Directive (EU) 2019/770 replace the OR warranty regime for EU consumers, with a two-year conformity period, a repair-or-replacement hierarchy, a reversed burden of proof for the first year at minimum, and — unlike Art. 199 OR — no possibility of contracting out.

## Product safety: GPSR

Regulation (EU) 2023/988 applies from **13 December 2024**. Art. 16(1): a product covered by the Regulation may not be placed on the market unless there is an **economic operator established in the Union** responsible for the tasks in Art. 4(3) of Regulation (EU) 2019/1020. Art. 16(2) adds ongoing checks on technical documentation and on the labelling and traceability requirements of Art. 9(5)–(7).

For a Swiss seller shipping consumer products to EU customers this means an EU-established responsible person must exist and must be identifiable on the product, its packaging, the parcel or an accompanying document, and the online offer must carry the traceability and safety information the Regulation requires. No Swiss-law equivalent exists.

## Accessibility: EAA

Directive (EU) 2019/882 applies from **28 June 2025** (Art. 31(2)) and covers e-commerce services. Microenterprises providing services are exempt under Art. 4(5); the definition in Art. 3(23) is fewer than 10 persons and turnover or balance sheet total not exceeding EUR 2 million. Transitional arrangements run to 28 June 2030 under Art. 32(1). See `barrierefreiheit.md`.

## Platform duties: DSA

Regulation (EU) 2022/2065 applies to intermediary services offered to recipients in the Union irrespective of where the provider is established. A Swiss platform with EU users therefore needs the DSA machinery for that service — points of contact, a legal representative in the Union, notice-and-action, statements of reasons, terms transparency, and the marketplace trader-traceability duties where applicable. None of this is required by Swiss law for the Swiss-facing service.

## Tax and customs

Cross-border VAT, import one-stop-shop registration and customs formalities are outside the scope of a legal-text skill, but they change the price the customer sees and therefore the price-display obligations. Where a Swiss shop delivers DDP into the EU, the displayed price and the terms must state who bears import VAT and duties. Flag this to the client as a separate workstream rather than drafting around it.

## Checkpoints

- [ ] Targeting of EU consumers decided explicitly and documented, with the evidence
- [ ] If targeted: Art. 3(2) GDPR applied, Art. 27 GDPR representative appointed or the exemption documented
- [ ] Consent banner meets the EU standard for EU visitors
- [ ] Privacy notice states a legal basis per processing for EU-facing processing
- [ ] Breach process covers both the 72-hour GDPR deadline and the Art. 24 DSG standard
- [ ] 14-day withdrawal right granted to EU consumers, with model withdrawal form and correct start of the period
- [ ] Terms do not purport to remove EU consumer protection by a choice of Swiss law
- [ ] Jurisdiction clause checked against the Lugano Convention's consumer rules
- [ ] EU responsible person under Art. 16 GPSR identified and named on the offer
- [ ] EAA conformity of the EU-facing shop planned, or microenterprise exemption documented
- [ ] DSA duties assessed if the service is an intermediary service with EU users
- [ ] Import VAT and duties position stated where the shop delivers into the EU
