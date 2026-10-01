---
name: legal-au-clemensjl
title: Legal texts for Australia
description: Use when writing, reviewing, or fixing legally required texts for an Australian website, webshop, app, or newsletter — privacy policy, collection notice, terms of service, returns and warranty policy, marketing consent, accessibility statement — or when asked whether an Australian online presence is compliant. Also use when an EU/GDPR or US legal template is about to be reused for Australia, when collection of personal information starts, or before a site goes live.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/legal-au
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: data-protection
language: en
sources:
- title: Accessibility
  path: references/accessibility.md
- title: Business Identification
  path: references/business-identification.md
- title: Checklist
  path: references/checklist.md
- title: Collection Notice
  path: references/collection-notice.md
- title: Consumer Guarantees
  path: references/consumer-guarantees.md
- title: Cookies And Tracking
  path: references/cookies-and-tracking.md
- title: Data Breach
  path: references/data-breach.md
- title: Intake
  path: references/intake.md
- title: Marketing Email
  path: references/marketing-email.md
- title: Online Safety
  path: references/online-safety.md
- title: Pricing And Claims
  path: references/pricing-and-claims.md
- title: Privacy Policy
  path: references/privacy-policy.md
- title: Privacy Scope
  path: references/privacy-scope.md
- title: Terms Of Service
  path: references/terms-of-service.md
---

# Legal texts for Australia

Mandatory disclosures and consumer-facing legal texts for Australian websites, webshops, apps and newsletters. The governing instruments are the Privacy Act 1988 (Cth) with the 13 Australian Privacy Principles (APPs) in Schedule 1, the Australian Consumer Law (ACL, Schedule 2 to the Competition and Consumer Act 2010 (Cth)) with the Competition and Consumer Regulations 2010, the Spam Act 2003 (Cth), the Do Not Call Register Act 2006 (Cth), the Corporations Act 2001 (Cth), the Online Safety Act 2021 (Cth) and the Disability Discrimination Act 1992 (Cth). Status as at 2026-08-05.

**Core principle.** Australian law breaks EU-built and US-built templates in opposite directions. There is **no general cooling-off right for online purchases** — instead the ACL gives non-excludable consumer guarantees (ACL s 64), so a returns policy that says "no refunds", "store credit only" or "no returns on sale items" is itself a contravention, while an imported "14-day right of withdrawal" invents a right that does not exist and, once published, binds the business contractually. In the other direction there is **no cookie consent requirement at all** — no ePrivacy equivalent — but APP 5 still requires a collection notice at the point of collection, which a consent banner does not satisfy. A template built from GDPR or CAN-SPAM material gets both ends wrong.

## Not legal advice

This skill produces drafts and review findings, not legal advice. Before go-live:

- Webshop, subscription, payment handling, children's data, health information, or platform operation with user-generated content: **obtain sign-off from an Australian lawyer.**
- First-line help without cost: the Office of the Australian Information Commissioner ([oaic.gov.au](https://www.oaic.gov.au)) for privacy; the ACCC ([accc.gov.au](https://www.accc.gov.au)) and your state or territory fair trading / consumer affairs office for consumer law; ASIC ([asic.gov.au](https://www.asic.gov.au)) for company and business name questions; ACMA ([acma.gov.au](https://www.acma.gov.au)) for spam and telemarketing; the eSafety Commissioner ([esafety.gov.au](https://www.esafety.gov.au)) for online safety; the Australian Human Rights Commission ([humanrights.gov.au](https://humanrights.gov.au)) for accessibility. Free legal advice runs through state and territory Legal Aid commissions and Law Society solicitor referral schemes. Legislation itself is at [legislation.gov.au](https://www.legislation.gov.au).
- Every generated text carries a visible `<!-- DRAFT – NOT LEGALLY APPROVED -->` HTML comment until legal sign-off is confirmed. Never remove the marker silently.

Never omit this section from the output and never soften it.

## Workflow

1. **Run the intake first, before any text exists.** Without the answers every text is guesswork. Questions in `references/intake.md`.
2. **Determine the obligation matrix** (below): which texts this specific project actually needs.
3. **Read the matching reference file before drafting each text.** Never from memory — the provisions are too specific and several changed in 2025 and 2026.
4. **Run `references/checklist.md`** and report each finding with its provision and location.
5. Emit the sign-off notice and leave the draft marker in place.

**Output shape.** The output has exactly four parts, in this order:

1. the legal text or finding itself, with the draft marker
2. the list of `[[MISSING: …]]` items the user must supply
3. adjacent obligations still open in the same project, one sentence each
4. the sign-off notice

The provision sits next to the statement it supports. Reference file names and paths belong in none of the four parts — they are working material, not deliverables.

## Obligation matrix

| Situation | Required text and its provision | Reference |
|---|---|---|
| Any entity that is an APP entity and collects personal information | APP privacy policy (APP 1.3, contents in APP 1.4) | `privacy-policy.md` |
| Any form, account signup, checkout, cookie, analytics, or log that collects personal information | APP 5 collection notice at or before collection | `collection-notice.md` |
| Turnover at or under $3m, or unsure whether the Privacy Act applies | Written scope assessment against Privacy Act s 6D and its exceptions | `privacy-scope.md` |
| Personal information held in any form | Data breach response plan; NDB scheme obligations (Privacy Act Part IIIC) | `data-breach.md` |
| Selling goods or services to consumers | Returns and remedies policy consistent with the consumer guarantees (ACL Part 3-2 Div 1, s 64) | `consumer-guarantees.md` |
| Offering a manufacturer or supplier warranty | Warranty against defects with the prescribed wording (Competition and Consumer Regulations 2010 reg 90) | `consumer-guarantees.md` |
| Any website, app or account-based service | Terms of service, with liability limits that survive s 64 and s 64A and unfair contract terms review (ACL ss 23–28) | `terms-of-service.md` |
| Any price, discount, claim or subscription shown to consumers | Single-price display (ACL s 48), no misleading conduct (s 18) or false representations (s 29) | `pricing-and-claims.md` |
| Newsletter, SMS, push or instant messaging marketing | Consent, sender identification, unsubscribe (Spam Act 2003 ss 16, 17, 18) | `marketing-email.md` |
| Telemarketing to Australian numbers | Do Not Call Register washing (Do Not Call Register Act 2006) | `marketing-email.md` |
| Company, registered business name, or invoicing | ABN/ACN and name disclosure (Corporations Act 2001 s 153; A New Tax System (Australian Business Number) Act 1999) | `business-identification.md` |
| User-generated content, comments, forums, marketplace, or a service minors can reach | Online Safety Act 2021 exposure, industry codes, and Part 4A social media minimum age | `online-safety.md` |
| Any public-facing digital service | Accessibility duty under Disability Discrimination Act 1992 s 24; WCAG conformance target | `accessibility.md` |
| Analytics, pixels, session replay, advertising tags, embeds | Not a consent question — an APP 3/APP 5/APP 6 question | `cookies-and-tracking.md` |

## Hard rules

- **There is no general cooling-off right for online purchases.** Cooling-off in the ACL attaches to unsolicited consumer agreements — telemarketing and door-to-door sales — where the consumer has 10 business days from the day after signing or receiving the agreement (ACL ss 76, 82), extended to 3 months if the seller broke the sales rules. Never present a change-of-mind return window as a legal requirement. If the business offers one, label it a voluntary policy that sits on top of the consumer guarantees.
- **Never write "no refunds", "store credit only", or "no returns on sale items".** The consumer guarantees cannot be excluded, restricted or modified (ACL s 64), and telling a consumer otherwise is a false or misleading representation about the existence or effect of a guarantee, right or remedy under ACL s 29 — a civil penalty provision.
- **Prescribed warranty wording is reproduced verbatim or not at all.** If any warranty against defects is given, Competition and Consumer Regulations 2010 reg 90 requires the exact mandatory text (different wording for goods, for services, and for goods and services together). Copy it from `consumer-guarantees.md`. Paraphrasing it is itself the breach.
- **No cookie consent obligation exists in Australian law.** There is no ePrivacy equivalent and no consent requirement for storing or reading information on a device. Installing a GDPR consent banner is not compliance and does not discharge anything. What is required is an APP 5 collection notice at or before collection and an APP 1.4 privacy policy.
- **The APP 5 collection notice is not the privacy policy.** APP 5.2 lists ten matters that must be brought to the individual's attention at or before collection, or as soon as practicable after. A link labelled "Privacy Policy" is not a notice. Only the access/correction and complaints matters (APP 5.2(g), (h)) may be satisfied by pointing at the policy.
- **Check the small business exemption before writing a privacy chapter, and check every carve-out first.** Privacy Act s 6D exempts operators with annual turnover of $3,000,000 or less, but health service providers, businesses that trade in personal information, Commonwealth contracted service providers, credit reporting bodies, residential tenancy database operators, AML/CTF reporting entities, CDR accredited entities, related bodies corporate of covered entities and opt-in entities are all pulled back in. Exempt from the Privacy Act never means exempt from the Spam Act, the ACL or the Online Safety Act.
- **The Privacy Act has no general right to erasure.** There is no equivalent of GDPR Art 17. APP 11.2 requires an entity to destroy or de-identify personal information once it is no longer needed for a permitted purpose — the entity's own assessment, not a right exercisable on request. Individuals have access (APP 12) and correction (APP 13). Never promise a deletion right that does not exist; once published, the promise binds.
- **There is no 72-hour breach deadline.** Under the Notifiable Data Breaches scheme an entity that suspects an eligible data breach has a maximum of 30 calendar days to complete a reasonable and expeditious assessment (Privacy Act s 26WH(2)), and must then notify the Commissioner and affected individuals as soon as practicable (ss 26WK, 26WL). The 72-hour rule is GDPR Art 33 and does not apply.
- **Electronic marketing is opt-in.** Spam Act 2003 s 16 prohibits sending a commercial electronic message without consent; s 17 requires accurate sender identification; s 18 requires a functional unsubscribe facility, and an unsubscribe request must be honoured within 5 business days. CAN-SPAM's send-until-they-object logic is a contravention in Australia.
- **Consumer prices are a single total price.** ACL s 48 requires the total price, as a single figure including GST and every other tax, duty, fee, levy and mandatory charge, to be displayed at least as prominently as any component of it. From 1 July 2027 mandatory per-transaction fees must additionally be disclosed upfront under the drip pricing provisions of the Competition and Consumer Amendment (Unfair Trading Practices) Act 2026.
- **Never invent business facts.** ABN, ACN, registered business name, registered office, trading name, insurer, licence number, turnover band: if not supplied, it becomes `[[MISSING: ABN]]` in the text and in the report back to the user. Never fill in a plausible-looking value.

## False friends

Imported assumptions that read as plausible and are wrong here. If one appears in an existing text, it is removed and replaced with the Australian position — if there is one.

| Imported assumption | Position in Australia |
|---|---|
| Cookie banner required (ePrivacy Directive Art 5(3), TTDSG, TKG) | No equivalent. Nothing in Australian law requires consent to set cookies. APP 5 notice and APP 1 policy instead. |
| Lawful basis for processing (GDPR Art 6) | The APPs have no lawful-basis structure. Collection is governed by APP 3, use and disclosure by APP 6. Consent is required only for sensitive information (APP 3.3), some direct marketing (APP 7) and the APP 8.2(b) cross-border exception. |
| Data protection officer required (GDPR Art 37) | No statutory DPO. APP 1.2 requires practices, procedures and systems; who owns them is the entity's choice. |
| 72-hour breach notification (GDPR Art 33) | 30 days maximum to assess (Privacy Act s 26WH(2)), then notify as soon as practicable (ss 26WK, 26WL). |
| Right to erasure (GDPR Art 17) | Does not exist. APP 11.2 destruction when no longer needed; APP 12 access; APP 13 correction. |
| Subject access response within one month | APP 12.4: agencies 30 days; organisations within a reasonable period. |
| 14-day right of withdrawal (Consumer Rights Directive Art 9) | No cooling-off for online purchases. Cooling-off applies to unsolicited consumer agreements only (ACL ss 76, 82). |
| Two-year statutory warranty (Sale of Goods Directive Art 10) | No fixed period. The guarantee of acceptable quality lasts as long as is reasonable for goods of that kind and price. |
| Standard contractual clauses for transfers (GDPR Art 46) | No approved clause set. APP 8.1 requires reasonable steps, normally an enforceable contract, and Privacy Act s 16C makes the discloser liable for the overseas recipient's acts anyway. |
| Age of consent 16 (GDPR Art 8) | The Privacy Act sets no age. Capacity is assessed individually. Separately, the Online Safety Act Part 4A social media minimum age of 16 is an obligation on platforms, not a consent rule for websites. |
| CAN-SPAM: mail until they opt out | Spam Act 2003 s 16 is opt-in. Inferred consent is narrow and is not "they gave us their email". |
| CCPA "Do Not Sell My Personal Information" link | No sale opt-out regime. Disclosure for a benefit is instead one of the things that strips a small business of the s 6D exemption. |
| Link to the EU ODR platform / EU dispute resolution | No Australian counterpart, and the EU platform itself shut down on 20.07.2025. Point to the relevant state or territory fair trading body and tribunal instead. |
| Impressum / legal notice page (§ 5 TMG, § 5 ECG) | No Australian imprint law. Disclosure duties are narrower and sit in Corporations Act s 153 and tax invoice rules. |
| WCAG mandated by statute (European Accessibility Act) | No Australian equivalent for the private sector. The duty comes from Disability Discrimination Act 1992 s 24 as unlawful discrimination, not from a conformance standard. |
| "We are in Australia so the GDPR does not apply" | The reverse trap. GDPR Art 3(2) catches an Australian business that offers goods or services to people in the EU or monitors their behaviour, regardless of where it sits. |

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| Cookie banner shipped as the privacy compliance measure | Solves a problem Australia does not have and leaves APP 5 unmet |
| Privacy policy linked in the footer and treated as the collection notice | Two separate obligations (APP 1.4 and APP 5.2) |
| Privacy policy that lists GDPR lawful bases | Signals a copied EU template; the APPs do not work that way |
| "You may request deletion of your data at any time" | No such right; publishing it creates a contractual promise you must honour |
| "Refunds only with receipt, within 14 days, unopened" | Purports to exclude the consumer guarantees (ACL s 64) and misstates rights (s 29) |
| Warranty text paraphrased or shortened | Reg 90 prescribes the exact wording |
| Business chooses repair when the failure is major | For a major failure the consumer chooses refund, replacement or compensation |
| Price shown excluding GST or booking fees, total revealed at checkout | Breaches the single-price rule (ACL s 48) |
| Pre-ticked marketing checkbox at checkout | Not consent under the Spam Act; also an unfair trading practice risk from 1 July 2027 |
| Unsubscribe requiring login or account creation | Contravenes Spam Act s 18 |
| Terms with a blanket "we exclude all liability" | Void against the consumer guarantees and a candidate unfair contract term (ACL ss 23–28, penalty-backed since 9 November 2023) |
| Accessibility ignored because "there is no Australian WCAG law" | Disability Discrimination Act 1992 s 24 makes an inaccessible service unlawful discrimination regardless |

## Reference files

Each contains the statutory basis with a status date, the mandatory content points, a template with `[[PLACEHOLDER]]` slots, and checkpoints.

- `references/intake.md` — questions to answer before the first text is written
- `references/privacy-scope.md` — APP entity status, Privacy Act s 6D small business exemption and its carve-outs, extraterritorial reach, GDPR overlap
- `references/privacy-policy.md` — APP 1.3/1.4 policy contents, APP 6, APP 7, APP 8, APP 12/13, the APP 1.7–1.9 automated decision-making disclosures due 10 December 2026
- `references/collection-notice.md` — APP 5.2 matters, placement, forms, accounts, checkout, template notices
- `references/data-breach.md` — Notifiable Data Breaches scheme, assessment, notification, response plan
- `references/consumer-guarantees.md` — ACL guarantees, major and minor failure, remedies, returns policy, reg 90 prescribed warranty wording
- `references/terms-of-service.md` — website and app terms, liability limits under s 64/s 64A, unfair contract terms, jurisdiction
- `references/pricing-and-claims.md` — single price s 48, misleading conduct s 18, false representations s 29, GST, subscriptions and drip pricing from 1 July 2027
- `references/marketing-email.md` — Spam Act consent, identification, unsubscribe; Do Not Call Register; testimonials and endorsements
- `references/business-identification.md` — ABN, ACN, registered business names, Corporations Act s 153, tax invoices, what belongs on a website
- `references/online-safety.md` — Online Safety Act, industry codes, Basic Online Safety Expectations, Part 4A social media minimum age, moderation and reporting
- `references/accessibility.md` — Disability Discrimination Act 1992, AHRC guidance, WCAG target, government Digital Service Standard, accessibility statement
- `references/cookies-and-tracking.md` — why there is no consent rule, what the APPs require of analytics, pixels and embeds
- `references/checklist.md` — pre-launch checklist with provisions and a finding format
