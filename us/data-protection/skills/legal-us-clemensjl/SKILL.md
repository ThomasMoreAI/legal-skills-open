---
name: legal-us-clemensjl
title: US website and app compliance
description: Use when writing, reviewing, or fixing legally required texts and disclosures for a US website, webshop, app, or newsletter — privacy policy, notice at collection, Do Not Sell or Share link, terms of service, subscription and auto-renewal disclosures, email and SMS consent, DMCA agent, accessibility — or when asked whether a US online presence is legally compliant. Also use when an EU, UK or German legal template is about to be reused for the United States, when a business starts collecting personal data from US residents, when it starts selling to a new state, or before a site goes live.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/legal-us
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: data-protection
language: en
sources:
- title: Accessibility
  path: references/accessibility.md
- title: Advertising And Reviews
  path: references/advertising-and-reviews.md
- title: California Ccpa
  path: references/california-ccpa.md
- title: Checklist
  path: references/checklist.md
- title: Children And Teens
  path: references/children-and-teens.md
- title: Email And Sms
  path: references/email-and-sms.md
- title: Health And Biometrics
  path: references/health-and-biometrics.md
- title: Intake
  path: references/intake.md
- title: Opt Outs And Gpc
  path: references/opt-outs-and-gpc.md
- title: Privacy Policy
  path: references/privacy-policy.md
- title: Sales Returns And Sectoral
  path: references/sales-returns-and-sectoral.md
- title: State Privacy Scope
  path: references/state-privacy-scope.md
- title: Subscriptions And Auto Renewal
  path: references/subscriptions-and-auto-renewal.md
- title: Terms And Platform
  path: references/terms-and-platform.md
- title: Tracking And Wiretapping
  path: references/tracking-and-wiretapping.md
---

# US website and app compliance

Required texts and disclosures for US websites, webshops, apps and newsletters. The sources are the state comprehensive privacy statutes, the FTC Act (15 U.S.C. § 45) and the FTC's trade regulation rules, sectoral federal statutes (COPPA, HIPAA, GLBA, FERPA, VPPA, FCRA, CAN-SPAM, TCPA, ROSCA, DMCA), state wiretap and biometric statutes, and the ADA. Nothing in this area is codified in one place, and several well-known rules were struck down by courts in 2025 and 2026.

**Core principle:** there is no US privacy law. There are roughly twenty state comprehensive statutes, a stack of sectoral federal ones, and the FTC Act — and **which of them bite is decided by where the customers live and by volume and revenue thresholds, not by where the company sits.** Some states have no revenue threshold at all: Texas applies to any non-small business that processes or sells the personal data of Texans (Tex. Bus. & Com. Code § 541.002). A single "US privacy policy" copied from a template therefore fails in one of two ways — it **over-promises**, creating FTC Act § 5 liability for a commitment the business does not actually honour, or it **omits** a state's mandatory disclosure. Threshold analysis comes before drafting, always.

## Not legal advice

This skill produces drafts and findings, not legal advice. Before launch:

- **Get a lawyer** where there is a private right of action or a per-violation penalty: biometric processing (Illinois BIPA), consumer health data (Washington MHMD), video plus advertising pixels (VPPA), marketing SMS (TCPA), children under 13 (COPPA), any arbitration clause, and any data breach.
- Free first-line sources, all official: **Federal Trade Commission business guidance** (ftc.gov/business-guidance), **California Privacy Protection Agency** (cppa.ca.gov), **California Attorney General privacy unit** (oag.ca.gov/privacy/ccpa), **Colorado Attorney General's recognised universal opt-out list** (coag.gov/uoom), **U.S. Copyright Office DMCA Designated Agent Directory** (copyright.gov/dmca-directory), **DOJ ADA Information Line** (ada.gov, 800-514-0301). For any other state, the attorney general's office via **naag.org/find-my-ag**.
- Every generated text carries a visible `<!-- DRAFT – NOT LEGALLY APPROVED -->` HTML comment until the user confirms legal sign-off. Never remove the marker silently.

Never omit this section from the output and never soften it.

## Workflow

1. **Run the intake before writing anything.** Questions in `references/intake.md`. Without the state footprint, the consumer counts and the revenue figures, every text is a guess.
2. **Determine the obligation set** from the matrix below and from `references/state-privacy-scope.md`. Write the applicability determination down; it is the deliverable's foundation and the first thing a regulator asks for.
3. **Read the relevant reference file before drafting.** Never from memory — the section numbers and the compliance dates are too specific, and several changed in the last eighteen months.
4. **Run `references/checklist.md`** and report each finding with its norm and its location.
5. Issue the approval notice and leave the draft marker in place.

**Output shape.** Exactly four parts, in this order:

1. the legal text or the finding, with the draft marker
2. the list of `[[MISSING: …]]` items the user must supply
3. adjacent obligations still open in the same project, one sentence each
4. the approval notice

The norm sits next to the statement it supports. Reference file names and paths belong in none of the four parts — they are working material, not deliverable.

## Obligation matrix

| Situation | Required texts, with the norm | Reference |
|---|---|---|
| Any commercial site collecting personal information from Californians or Delawareans — no threshold | Conspicuously posted privacy policy with a Do Not Track disclosure (CalOPPA, Cal. Bus. & Prof. Code § 22575; 6 Del. C. § 1205C) | `california-ccpa.md`, `state-privacy-scope.md` |
| Business over a state comprehensive privacy law threshold | Privacy notice with that state's mandatory content, rights mechanism, appeal route | `state-privacy-scope.md`, `privacy-policy.md` |
| CCPA applies | Notice at collection (§ 1798.100(a)), "Do Not Sell or Share" link and sensitive-information limitation link (§ 1798.135), 12-month lookback (§ 1798.130(a)(5)) | `california-ccpa.md` |
| Any sale, share or targeted advertising | Working opt-out plus honouring of opt-out preference signals | `opt-outs-and-gpc.md` |
| Third-party analytics, pixels, session replay or chat | Consent gating and a consent record — driven by state wiretap exposure, not by a cookie statute | `tracking-and-wiretapping.md` |
| Video content plus an advertising pixel | Standalone VPPA consent (18 U.S.C. § 2710(b)(2)(B)) | `tracking-and-wiretapping.md` |
| Service directed to children under 13, or actual knowledge of under-13 users | COPPA notice, verifiable parental consent, separate consent for third-party disclosure (16 CFR Part 312) | `children-and-teens.md` |
| Consumer health data, or biometric identifiers | Separate Washington health data policy (RCW 19.373.020); BIPA § 15(a)–(b) notice, release and retention schedule | `health-and-biometrics.md` |
| Email marketing | Physical postal address, opt-out honoured in 10 business days (15 U.S.C. § 7704) | `email-and-sms.md` |
| SMS marketing | Prior express written consent (47 CFR § 64.1200(f)(9)), quiet hours, revocation handling | `email-and-sms.md` |
| Subscription, free trial or auto-renewal | ROSCA disclosures and simple cancellation (15 U.S.C. § 8403) plus the state ARLs | `subscriptions-and-auto-renewal.md` |
| Reviews, testimonials, influencers, endorsements | 16 CFR Part 465 compliance and Part 255 disclosures | `advertising-and-reviews.md` |
| Any contract term worth relying on | Clickwrap acceptance, arbitration clause, acceptance records | `terms-and-platform.md` |
| User-generated content hosted | DMCA agent registration and three-year renewal (17 U.S.C. § 512(c)(2); 37 CFR § 201.38) | `terms-and-platform.md` |
| Goods or services sold online | Return policy disclosure, total price, shipping timeframe (16 CFR Part 435) | `sales-returns-and-sectoral.md` |
| Financial, edtech or screening products | GLBA Safeguards, FERPA contract terms, FCRA disclosures | `sales-returns-and-sectoral.md` |
| Any consumer-facing site | ADA Title III exposure; WCAG 2.1 AA as the working standard | `accessibility.md` |

## Hard rules

- **Scope before drafting.** Determine and record which state laws apply, using each state's own threshold. Never assume a threshold exists: **Tex. Bus. & Com. Code § 541.002** and **Neb. Rev. Stat. § 87-1103** have **no consumer-number and no revenue threshold** — both reach any entity that processes or sells personal data of state residents and is not a small business under the federal SBA standards. "We are too small for state privacy laws" is almost always wrong.
- **Never write "we do not sell your personal information" without checking the network tab.** Under the state definitions, disclosing personal information to an advertising platform for cross-context behavioural advertising is a sale or a share whether or not money moves. A false statement is a deceptive practice under **15 U.S.C. § 45** and under every state UDAP statute. Verify against a live capture, not against the client's belief.
- **The FTC "Click-to-Cancel" Rule is vacated.** *Custom Communications, Inc. v. FTC*, No. 24-3137 (8th Cir., 8 July 2025) vacated 16 CFR Part 425 in its entirety for failure to prepare the regulatory analysis required by 15 U.S.C. § 57b-3(b)(1); it never took effect. Never cite it as a live obligation — and never tell a client the duty disappeared, because **ROSCA, 15 U.S.C. § 8403**, and the state auto-renewal laws impose materially the same requirements.
- **The FCC one-to-one consent rule is vacated.** *Insurance Marketing Coalition Ltd. v. FCC*, No. 24-10277 (11th Cir., 24 January 2025). Do not cite it. The **prior express written consent** requirement of 47 CFR § 64.1200(f)(9) for marketing robotexts is untouched and still binds.
- **Email is opt-out, SMS is opt-in.** CAN-SPAM requires no consent but mandates a valid physical postal address in every commercial message and an opt-out honoured within **10 business days** (15 U.S.C. § 7704(a)(3)–(5)). A first marketing text without prior express written consent is a **$500-to-$1,500-per-message** exposure with a private right of action (47 U.S.C. § 227(b)(3)).
- **The CCPA notice at collection is a separate artefact from the privacy policy.** Cal. Civ. Code § 1798.100(a) requires it at or before the point of collection. A site with a privacy policy and no notice at collection is non-compliant.
- **Register the DMCA agent and diarise the renewal.** Any site storing material at the direction of users needs a designation filed electronically with the Copyright Office, and **37 CFR § 201.38(c)(4)** expires it three years after registration. An expired designation means no § 512 safe harbour. This is cheap, mandatory, and almost always missed.
- **Never invent facts about the business.** Legal entity name, street address, state of formation, registration numbers, designated agent, revenue and consumer counts: if unknown it becomes `[[MISSING: …]]` in the text and in the report back to the user. Never plausibly filled in.
- **Never state a compliance date from memory.** COPPA Rule dates, the CPPA's ADMT and risk-assessment deadlines, DOJ's ADA Title II dates and the TCPA revocation waiver have all moved. Verify against the agency's own site, or mark `[[UNVERIFIED: …]]`.

## False friends — EU assumptions that do not transfer

| Assumption imported from EU or German law | Position in the United States |
|---|---|
| A GDPR-style consent banner is required before cookies (Art 5(3) ePrivacy Directive) | **No US statute requires prior consent for cookies.** Banners are deployed because of state wiretap class actions (Cal. Penal Code §§ 631, 638.51), the VPPA, and state opt-out duties. Design the banner as a script gate and a consent record, not as a cookie notice. |
| "Legitimate interests" as a lawful basis (Art 6(1)(f) GDPR) | No US privacy law has legal bases. Writing one into a US policy imports a framework no US regulator applies. |
| Controller and processor (Art 4 GDPR) | California says **business, service provider, contractor and third party** (Cal. Civ. Code § 1798.140); most other states say controller and processor — with definitions that do not match the GDPR ones. Use the vocabulary of the state that applies. |
| Right to be forgotten (Art 17 GDPR) | A **right to delete**, with statutory exceptions materially wider than Art 17. Do not use the EU phrase. |
| A Data Protection Officer is required (Art 37 GDPR) | No US law requires one. Naming a DPO creates an expectation the business is then held to. Several states instead require **data protection assessments** for higher-risk processing. |
| Consent before loading third-party fonts, maps or video | Not a statutory requirement. The exposure is wiretap and VPPA litigation, and the fix is the same script gate — but the legal reasoning, and therefore the record you must keep, is different. |
| 14-day right of withdrawal (Art 9 Directive 2011/83/EU) | **There is no federal cooling-off right for online purchases.** The FTC Cooling-Off Rule, 16 CFR Part 429, covers personally solicited sales at the buyer's home ($25+) and at temporary locations ($130+), and expressly excludes transactions conducted entirely by mail or telephone. Return rights are contractual. |
| Impressum / § 5 DDG provider identification | No equivalent. The nearest duties are the CAN-SPAM physical postal address, the CalOPPA privacy policy, and the DMCA agent contact block. |
| Age of digital consent is 16 (Art 8 GDPR) | **13** under COPPA, 15 U.S.C. § 6501. Between 13 and 18 there is no federal statute — only state law and FTC Act § 5. |
| One supervisory authority, one lead authority | The FTC, the CPPA, **fifty state attorneys general**, and private plaintiffs. There is no one-stop shop and no lead-authority mechanism. |
| An accessibility statement satisfies the accessibility duty (EAA) | No US statute requires an accessibility statement. ADA Title III is enforced by private suit, and an overstated statement is evidence against the business. |
| Reverse trap: US law is all that applies | **GDPR Art 3(2) still reaches a US company** that offers goods or services to people in the EU or monitors their behaviour, and an Art 27 representative may be required. Targeting the EU is a factual question about pricing, language, shipping and ad targeting — not about where the servers are. |

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| One "US privacy policy" applied to all states | Mandatory content differs per state; the union is the requirement |
| "We do not sell your data" with ad pixels live | Sale and share are defined to include this; the statement is a § 5 deception |
| Privacy policy but no notice at collection | Cal. Civ. Code § 1798.100(a) requires it at the point of collection |
| Consent banner but no GPC handling | The signal is a legal opt-out in several states; ignoring it violates the statute regardless of the banner |
| Citing NRS 603A.340 for Nevada's opt-out of sale | § 603A.340 is the notice duty; the opt-out is § 603A.345, and § 603A.346 for data brokers |
| Assuming every state's opt-out signal covers profiling | New Jersey and Nebraska limit it to targeted advertising and sale; a separate profiling opt-out is still required |
| Citing the FTC Click-to-Cancel Rule | Vacated 8 July 2025; ROSCA and state ARLs are the live obligations |
| Citing DOJ's ADA Title II rule at a private business | It binds state and local government only, and its dates were extended in April 2026 |
| "Compliant with GDPR and CCPA" badge | An enforceable representation under § 5 |
| Terms of service linked only in the footer | Browsewrap; no contract formed, so the arbitration clause and limitation of liability are worthless |
| UGC site with no DMCA agent, or a lapsed one | No § 512 safe harbour; direct copyright exposure |
| Subscription cancellable only by phone or email | Contrary to the state ARLs where enrolment was online |
| Marketing texts sent at 11 p.m. | 47 CFR § 64.1200(c)(1) quiet hours; an active class-action theory |
| Children's site running a third-party ad SDK on one consent | The amended COPPA Rule requires separate parental consent for third-party disclosure |
| Accessibility overlay treated as remediation | Does not prevent Title III suits and draws them |

## Reference files

Each contains the statutory basis with section numbers and a status date, the mandatory content points, a template with `[[PLACEHOLDER]]` slots, and checkpoints.

- `references/intake.md` — questions to answer before the first text exists
- `references/state-privacy-scope.md` — which state laws apply, with thresholds; the skill's spine
- `references/privacy-policy.md` — content, template, and the statements that must never appear
- `references/california-ccpa.md` — CCPA/CPRA, the two links, notice at collection, CPPA regulations, CalOPPA
- `references/opt-outs-and-gpc.md` — Global Privacy Control, universal opt-out mechanisms, building and testing them
- `references/tracking-and-wiretapping.md` — CIPA, state wiretap statutes, VPPA, why the banner exists
- `references/children-and-teens.md` — COPPA and the 2025 amendments, teen provisions, CAADCA status
- `references/health-and-biometrics.md` — HIPAA, My Health My Data, BIPA, Texas CUBI, FTC health breach rule
- `references/email-and-sms.md` — CAN-SPAM, TCPA, consent capture, revocation
- `references/subscriptions-and-auto-renewal.md` — ROSCA, the vacated federal rule, state auto-renewal laws
- `references/advertising-and-reviews.md` — FTC Act § 5, reviews rule, endorsement guides, Made in USA, dark patterns
- `references/terms-and-platform.md` — clickwrap, arbitration, Section 230, DMCA safe harbour
- `references/sales-returns-and-sectoral.md` — no cooling-off right, return disclosures, GLBA, FERPA, FCRA, TSR
- `references/accessibility.md` — ADA Title III, the circuit split, WCAG as the working standard
- `references/checklist.md` — pre-launch checklist with the norm against each item
