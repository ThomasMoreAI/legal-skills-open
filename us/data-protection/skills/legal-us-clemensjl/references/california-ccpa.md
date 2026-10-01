# California — CCPA/CPRA and the California-only extras

Status as at 2026-08-05.

California is not just the largest state privacy regime; it is structurally different from the other state comprehensive laws, and several of its requirements exist nowhere else. A privacy programme built to the Virginia model and relabelled for California is missing mandatory elements. Statute: Cal. Civ. Code §§ 1798.100–1798.199.100. Regulations: 11 CCR § 7001 et seq., approved by the Office of Administrative Law on 29 March 2023. Enforced by the **California Privacy Protection Agency** and the **Attorney General**; the only private right of action is the data-breach action at § 1798.150.

## Who is a "business" — Cal. Civ. Code § 1798.140(d)

A for-profit entity that does business in California, determines the purposes and means of processing, collects consumers' personal information, and meets **any one** of:

1. annual gross revenues in excess of the statutory **$25,000,000** in the preceding calendar year, "as adjusted pursuant to subdivision (d) of Section 1798.199.95" — **the operative figure is $26,625,000**, effective 01.01.2025 (CPPA inflation-adjustment page, read 05.08.2026). Never apply the bare $25 million; it has not been the live threshold since the end of 2024;
2. alone or in combination, annually **buys, sells or shares the personal information of 100,000 or more consumers or households**;
3. derives **50 percent or more** of annual revenues from selling or sharing consumers' personal information.

Note what is different from other states: a **revenue-only** trigger with no volume element (a large company with one Californian customer is a business), a threshold counting **households** as well as consumers, and no exclusion for data processed solely to complete a transaction. Entities sharing common branding with a business, and joint ventures at specified ownership levels, are swept in.

## The two links — § 1798.135

This is the requirement no other state shares, and it is the most visible compliance artefact on a US site.

- **"Do Not Sell or Share My Personal Information"** — a clear and conspicuous link on the homepage. The wording is prescribed. "Your Privacy Choices" alone is not the statutory title, although the regulations recognise an opt-out icon used **with** a compliant link.
- **"Limit the Use of My Sensitive Personal Information"** — a second link, required where sensitive personal information is used or disclosed beyond the purposes permitted by § 1798.121.
- § 1798.135(a)(3) permits **a single, clearly labeled link** enabling the consumer to exercise both rights.
- § 1798.135(b) permits a business to comply **instead** by honouring an **opt-out preference signal** sent with the consumer's consent by a platform, technology or mechanism, in the manner set out in the regulations. A business that goes this route still needs the mechanism to work — see `opt-outs-and-gpc.md`.

The links must be reachable from the homepage and must work without an account, without a login, and without a consent banner in the way.

## Notice at collection — § 1798.100(a)

At or before the point of collection, the business must inform the consumer of the categories of personal information to be collected, the purposes for each category, whether it is sold or shared, and the retention period for each category or the criteria used to determine it. This is a **separate artefact from the privacy policy**, delivered at the point of collection — on the form, at the signup screen, in the app permission flow, and via a link on the homepage for passive collection. Regulations at 11 CCR § 7012 prescribe its content and placement. Most sites have a privacy policy and no notice at collection; that is a violation of § 1798.100(a), not a formatting preference.

## The 12-month lookback — § 1798.130(a)(5)

The privacy policy must:

- describe the categories of personal information collected about consumers **in the preceding 12 months**;
- separately list the categories **sold or shared** in the preceding 12 months, and the categories **disclosed for a business purpose**;
- describe consumers' rights and how to exercise them;
- be **updated at least once every 12 months**.

A policy with no date, or dated more than twelve months ago, is facially non-compliant. Put a "last updated" date on it and diarise the review.

## Request handling — § 1798.130(a)(1)–(2)

- **Two or more designated methods** for submitting requests, including a **toll-free telephone number**. A business that operates exclusively online and has a direct relationship with the consumer may provide only an email address.
- Respond within **45 days** of a verifiable consumer request, extendable once by a further 45 days where reasonably necessary, with notice of the extension given within the first 45 days.
- The right to correct, the right to know, the right to delete, the right to opt out of sale/sharing, the right to limit use of sensitive personal information, and the right against retaliation for exercising rights.

## CPPA regulations on ADMT, risk assessments and cybersecurity audits

The CPPA package "CCPA Updates, Insurance, Cybersecurity Audits, Risk Assessments, and Automated Decisionmaking Technology (ADMT) Regulations" was adopted by the Board on **24 July 2025**, approved by the Office of Administrative Law on **22 September 2025**, and took **effect on 1 January 2026**. These are the most consequential additions to the California regime since the CPRA, and they carry **phased compliance dates rather than a single switch-on** — the effective date of the regulations is not the date the substantive duties bite.

`[[UNVERIFIED: each individual compliance deadline inside the package — the ADMT compliance date, the risk-assessment conduct and first-submission dates, and the cybersecurity audit phase-in by revenue band. Read the approved regulation text linked from cppa.ca.gov/regulations before stating any of them. The draft and final texts differ, so a remembered date is likely wrong.]]`

Substantively, the package requires: pre-use notice and an opt-out where ADMT is used for a significant decision; risk assessments before initiating processing that presents a significant risk to consumers' privacy, retained and summarised to the Agency on a schedule; and independent annual cybersecurity audits for businesses whose processing presents significant risk, phased in by size.

## CalOPPA — Cal. Bus. & Prof. Code § 22575 et seq.

Still in force, and independent of the CCPA. It applies to any operator of a commercial website or online service that collects personally identifiable information about California consumers — with **no revenue or volume threshold at all**. It requires a **conspicuously posted privacy policy** that identifies the categories of PII collected and the categories of third parties with whom it is shared, describes the process for reviewing and requesting changes, describes how changes to the policy are notified, and states the effective date. It also requires disclosure of **how the operator responds to Do Not Track signals** and whether third parties may collect PII across sites over time.

The Do Not Track disclosure duty is the oddity: CalOPPA does not require honouring DNT, only disclosing the response to it. A truthful "we do not respond to Do Not Track signals" satisfies it. Omitting the disclosure entirely does not. A small business below every CCPA threshold still owes CalOPPA a privacy policy.

## Delete Act and the data broker registry

Businesses meeting the statutory definition of a **data broker** must register annually with the CPPA between **1 and 31 January**, reporting on the prior calendar year. The Agency's **Delete Request and Opt-out Platform (DROP)** went live for consumer requests on **1 January 2026**, and registered data brokers are required to begin **processing deletion requests submitted through DROP from 1 August 2026**. This applies only to data brokers — businesses that knowingly collect and sell personal information about consumers with whom they have no direct relationship. `[[UNVERIFIED: the Civil Code section numbers of the Delete Act and the required frequency of DROP access]]`

## The money figures — all inflation-adjusted, none are the statutory numbers

CPPA inflation-adjustment page, read 05.08.2026. All effective **01.01.2025**, all adjusted from the figures written into the statute:

| Item | Statutory | Operative |
|---|---|---|
| Revenue threshold, § 1798.140(d)(1)(A) | $25,000,000 | **$26,625,000** |
| Private-right-of-action statutory damages per consumer per incident, § 1798.150(a)(1)(A) | $100–$750 | **$107–$799** |
| Administrative fine per violation, § 1798.155 | $2,500 | **$2,663** |
| Administrative fine per **intentional** violation, or violation involving a minor under 16 | $7,500 | **$7,988** |
| Civil penalty per violation / per intentional violation, § 1798.199.90 | $2,500 / $7,500 | **$2,663 / $7,988** |

Adjustment runs in **January of every odd-numbered year**, off the California CPI (All Items, All Urban Consumers) change over the preceding two years. **Next adjustment: January 2027.** Any figure in this file, or in a client-facing text, is stale from that date — diary it.

Quoting the statutory numbers rather than the adjusted ones is a live error in most published US privacy summaries; it understates exposure by roughly 6.5 %.

## Checkpoints

- [ ] Applicability against § 1798.140(d) documented, including the current inflation-adjusted revenue figure ($26,625,000 until January 2027)
- [ ] "Do Not Sell or Share My Personal Information" link present on the homepage, or a compliant single combined link
- [ ] "Limit the Use of My Sensitive Personal Information" link present where sensitive PI is used beyond § 1798.121 purposes
- [ ] Both links functional without login and not blocked by a consent banner
- [ ] Notice at collection delivered at or before the point of collection, separate from the privacy policy (§ 1798.100(a); 11 CCR § 7012)
- [ ] Retention period or criteria stated for each category
- [ ] Privacy policy lists categories collected, sold or shared, and disclosed for a business purpose, each over the preceding 12 months
- [ ] Privacy policy carries a last-updated date within the last 12 months
- [ ] Two request channels, including a toll-free number unless the online-only exception applies
- [ ] 45-day response process with the extension notice built
- [ ] Opt-out preference signal honoured (see `opt-outs-and-gpc.md`)
- [ ] CalOPPA Do Not Track disclosure present and truthful
- [ ] ADMT, risk assessment and cybersecurity audit obligations checked against the current CPPA regulation deadlines — not against a remembered date
- [ ] Data broker status assessed; if a data broker, registration and DROP processing in place
