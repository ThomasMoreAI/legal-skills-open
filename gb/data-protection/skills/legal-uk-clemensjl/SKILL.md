---
name: legal-uk-clemensjl
title: UK online legal texts
description: Use when writing, reviewing, or fixing legally required texts for a UK website, webshop, app, or newsletter — website disclosures, privacy notice, cookie banner, terms and conditions, cancellation notice, complaints and ADR information, accessibility statement — or when asked whether a UK online presence is legally compliant. Also use when an EU, German, or US legal template is about to be reused for the UK, when personal data processing starts, or before a site goes live.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/legal-uk
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: data-protection
language: en
sources:
- title: Accessibility
  path: references/accessibility.md
- title: Accountability And Fee
  path: references/accountability-and-fee.md
- title: Cancellation
  path: references/cancellation.md
- title: Checklist
  path: references/checklist.md
- title: Complaints Adr
  path: references/complaints-adr.md
- title: Consumer Terms
  path: references/consumer-terms.md
- title: Cookies
  path: references/cookies.md
- title: Dmcc Trading
  path: references/dmcc-trading.md
- title: Electronic Marketing
  path: references/electronic-marketing.md
- title: Intake
  path: references/intake.md
- title: International Transfers
  path: references/international-transfers.md
- title: Online Safety
  path: references/online-safety.md
- title: Privacy Notice
  path: references/privacy-notice.md
- title: Website Disclosures
  path: references/website-disclosures.md
---

# UK online legal texts

Mandatory texts and disclosures for UK websites, webshops, apps and newsletters. The governing instruments are the UK GDPR and the Data Protection Act 2018 as amended by the Data (Use and Access) Act 2025, PECR 2003, the Electronic Commerce (EC Directive) Regulations 2002, the Companies Act 2006, the Consumer Rights Act 2015, the Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013, the Digital Markets, Competition and Consumers Act 2024, the Online Safety Act 2023 and the Equality Act 2010.

**Core principle:** the UK looks like the EU and is diverging on a published schedule. UK GDPR is not the GDPR — the Data (Use and Access) Act 2025 (c. 18, Royal Assent 19 June 2025) rewrote Article 22, added recognised legitimate interests, capped subject access at a "reasonable and proportionate search" and, on 19 June 2026, removed Article 77 outright. Consumer law left the Consumer Protection from Unfair Trading Regulations 2008 for the DMCC Act 2024 on 6 April 2025, and consumer ADR left the 2015 Regulations for DMCC Part 4 Chapter 4 on 6 April 2026. Cookies and marketing were never in the GDPR at all; they are in PECR, which since 5 February 2026 carries UK GDPR-level fines. A template that says "GDPR", cites the CRD, or links the EU ODR platform is wrong on every axis.

## Not legal advice

This skill produces drafts and review findings, not legal advice. Before go-live:

- For a webshop, subscription, payment flow, children's data, health data, or any user-generated content service: **obtain sign-off from a solicitor.**
- Free first-line help: the ICO helpline and its SME advice service (`ico.org.uk/for-organisations/advice-for-small-organisations/`), Citizens Advice consumer service and its Trading Standards referral route (`citizensadvice.org.uk/consumer/`), Business Companion, the official Trading Standards business guidance (`businesscompanion.info`), the CAP Copy Advice service for advertising (`asa.org.uk/advice-and-resources/bespoke-copy-advice.html`), and the Law Society's Find a Solicitor (`solicitors.lawsociety.org.uk`).
- Every generated text carries a visible `<!-- DRAFT – NOT LEGALLY APPROVED -->` HTML comment until the user confirms sign-off. Never remove the marker silently.

Never omit or soften this section in the output.

## Workflow

1. **Run the intake first, before any text exists.** Without the answers every text is guesswork. Questions in `references/intake.md`.
2. **Determine the obligation matrix** (below): which texts this specific project needs.
3. **Read the reference file for each obligation, then draft.** Never from memory — the section numbers and commencement dates are too specific and several changed in 2025 and 2026.
4. **Run `references/checklist.md`**, report each finding with its provision.
5. Output the sign-off notice, leave the draft marker in place.

**Output shape.** Exactly four parts, in this order:

1. the legal text or finding itself, carrying the draft marker
2. the list of `[[MISSING: …]]` items the user must supply
3. adjacent obligations still open in the same project, one sentence each
4. the sign-off notice

The provision sits next to the claim it supports. Reference filenames and paths belong in none of the four parts — they are working material, not deliverable.

## Obligation matrix

| Situation | Required texts, with the provision | Reference |
|---|---|---|
| Any commercial website or app ("information society service") | Service provider information (Electronic Commerce (EC Directive) Regulations 2002, reg 6) | `website-disclosures.md` |
| Operator is a registered company or LLP | Registered name, registered number, part of the UK of registration, registered office on the website (Company, Limited Liability Partnership and Business (Names and Trading Disclosures) Regulations 2015, reg 25) | `website-disclosures.md` |
| Sole trader or partnership trading under a name that is not the proprietors' own | Name and address for service (Companies Act 2006, ss 1200–1206) | `website-disclosures.md` |
| Any processing of personal data, including server logs and a contact form | Privacy notice (UK GDPR Arts 13, 14) | `privacy-notice.md` |
| Any controller not exempt | ICO data protection fee, paid annually (Data Protection (Charges and Information) Regulations 2018, reg 3) | `accountability-and-fee.md` |
| Storage of or access to information on a user's device beyond the Schedule A1 exceptions | Consent banner and cookie table (PECR 2003, reg 6 and Sch A1) | `cookies.md` |
| Newsletter, email, SMS or automated-call marketing | Consent or soft opt-in, unsubscribe, sender identification (PECR 2003, regs 22, 23) | `electronic-marketing.md` |
| Personal data leaves the UK | Transfer mechanism and disclosure (UK GDPR Arts 44–46, IDTA, UK Addendum, UK Extension to the DPF) | `international-transfers.md` |
| Selling to consumers | Terms, statutory rights, unfair terms review (Consumer Rights Act 2015) | `consumer-terms.md` |
| Selling to consumers at a distance | Pre-contract information, the "order with obligation to pay" button, cancellation notice, model cancellation form (CCRs 2013, regs 13, 14, 29–32, Sch 2, Sch 3) | `cancellation.md` |
| Any commercial practice aimed at consumers | Compliance with the banned practices, fake-review and drip-pricing rules (DMCC Act 2024, Part 4 Ch 1, Sch 20) | `dmcc-trading.md` |
| User-to-user content, forum, chat, marketplace, or search | Illegal content and children's risk assessments, reporting and complaints routes, terms of service (Online Safety Act 2023, ss 9–12, 20, 21, 35–37) | `online-safety.md` |
| Any consumer-facing site; public bodies additionally | Reasonable adjustments (Equality Act 2010, ss 20, 29(7)); accessibility statement and WCAG 2.2 AA (Public Sector Bodies Accessibility Regulations 2018) | `accessibility.md` |
| Responding to a consumer complaint | Notify the consumer of ADR arrangements (DMCC Act 2024, s 308) | `complaints-adr.md` |
| Any personal data at all | Records, processor contracts, breach process, complaints handling (internal, not published) | `accountability-and-fee.md` |

## Hard rules

- **Never link the EU ODR platform, and delete it on sight.** It was shut down by Regulation (EU) 2024/3228 and stopped operating on 20 July 2025. The UK was never in it after Brexit. There is no UK ODR platform. A live link is a dead link and, on a trader's site, a misleading omission risk under s 227 DMCC Act 2024.
- **Consumer ADR moved on 6 April 2026.** The Alternative Dispute Resolution for Consumer Disputes (Competent Authorities and Information) Regulations 2015 (SI 2015/542) are revoked. DMCC Act 2024 Part 4 Chapter 4 (ss 291–310, Schs 25–27) came into force on 6 April 2026 by SI 2026/284. The trader duty is now s 308: tell the consumer about available ADR arrangements when you communicate the outcome of their complaint. Citing SI 2015/542 reg 19 in 2026 is citing a revoked instrument.
- **The DMCC subscription contracts regime is not in force.** Part 4 Chapter 2 (ss 253–281) still awaits secondary legislation; the Department for Business and Trade response of 2 April 2026 put commencement at spring 2027. Never draft renewal-reminder or cooling-off subscription clauses as if they were already binding, and never say "the DMCC requires" about them.
- **CPUT 2008 is revoked.** The Consumer Protection from Unfair Trading Regulations 2008 were revoked on 6 April 2025 and replaced by DMCC Act 2024 Part 4 Chapter 1 (ss 225–230) with the banned practices in Schedule 20. Cite the Act, not the Regulations, for anything after that date.
- **UK GDPR Article 77 is gone.** DUAA 2025 s 103, in force 19 June 2026, omits Article 77 and Article 57(1)(f) from the UK GDPR, moves the right to complain to the Commissioner into s 165 DPA 2018, and inserts s 164A DPA 2018 obliging controllers to accept complaints, provide an electronic complaint form, acknowledge within 30 days and respond without undue delay. A privacy notice that cites Article 77 is out of date.
- **Cookie consent still applies unless a Schedule A1 exception fits exactly.** PECR reg 6 was substituted on 5 February 2026 by DUAA s 112 and Sch 12. The statistical (Sch A1 para 5) and website appearance (para 6) exceptions require information to the user and a simple, free means of objecting, and fail the moment data is shared with a third party for that third party's own purposes. Google Analytics in its standard configuration is therefore normally still consent-based.
- **PECR now bites at UK GDPR levels.** DUAA s 115 and Sch 13 replaced PECR Schedule 1 on 5 February 2026, applying DPA 2018 s 157 to PECR. Breaches of reg 6 (cookies) and reg 22 (email marketing) attract the higher maximum: £17.5 million or 4% of total annual worldwide turnover, whichever is higher. The old £500,000 cap is history.
- **Pay the ICO fee.** Reg 3 of the Data Protection (Charges and Information) Regulations 2018, as amended by SI 2025/63 from 17 February 2025: tier 1 £52, tier 2 £78, tier 3 £3,763, less £5 for direct debit. It is a standalone statutory duty, enforceable by penalty, and independent of whether the privacy notice is any good.
- **Never invent facts about the business.** Company number, part of the UK of registration, registered office, VAT number, regulator, professional body, ICO registration number: if unknown it becomes `[[MISSING: company registration number]]` in the text and in the report back to the user.
- **Geographic address, not a PO box.** Reg 6(1)(b) ECR 2002 requires the geographic address at which the service provider is established. For a home-based sole trader that is the home address unless the user takes a commercial decision (registered office service, serviced address). Raise it, do not work around it.

## False friends

EU and US assumptions read as plausible and get invented under time pressure. None of the following applies to the UK as stated.

| Imported assumption | Actual UK position |
|---|---|
| "GDPR", Regulation (EU) 2016/679, EU supervisory authority | UK GDPR (the retained text as amended by DUAA 2025), DPA 2018, Information Commissioner |
| Consumer Rights Directive 2011/83/EU, "right of withdrawal" | CCRs 2013 (SI 2013/3134); the term is "the right to cancel", 14 days under reg 30 |
| Link to the EU ODR platform | Shut down 20 July 2025; the UK never participated post-Brexit; remove, do not replace with a UK equivalent because none exists |
| Art 27 GDPR EU representative on a UK site | Not a UK requirement. But the reverse trap is real: a UK business that offers goods or services to, or monitors, people in the EU is caught by Art 3(2) EU GDPR and does need an Art 27 representative and an EU-facing notice in parallel |
| European Accessibility Act / Directive (EU) 2019/882 | Does not apply in the UK. The duties are Equality Act 2010 ss 20 and 29(7) for private services and SI 2018/952 for public sector bodies |
| Digital Services Act, trusted flaggers, DSA point of contact | Not UK law. The UK regime is the Online Safety Act 2023 with Ofcom as regulator |
| § 5 TMG / § 5 DDG Impressum, "Impressum" as a page name | Reg 6 Electronic Commerce (EC Directive) Regulations 2002 plus reg 25 SI 2015/17; conventionally a "Legal" or "Terms" page plus the footer company line |
| CCPA/CPRA "Do Not Sell", US-style arbitration clause, class action waiver | No UK analogue; a mandatory arbitration or jurisdiction clause against a consumer is a candidate unfair term under CRA 2015 s 62 and Sch 2 |
| "Consumer Protection from Unfair Trading Regulations 2008" | Revoked 6 April 2025; DMCC Act 2024 Part 4 Ch 1 and Sch 20 |
| Cookie consent is a GDPR obligation | It is PECR reg 6; UK GDPR supplies only the standard of consent |
| Children can consent to an online service at 16 | UK GDPR Art 8(1) sets 13. Do not cite DPA 2018 s 9 — omitted 31 December 2020 |
| EU–US Data Privacy Framework covers UK transfers automatically | Only via the separate UK Extension, and only to US organisations that have opted into it |

If an obligation comes to mind that cannot be traced to a specific UK provision, do not assert it — report it as an open question.

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| Company details only in the footer, no registered number | Reg 25(2) SI 2015/17 requires part of the UK of registration, registered number and registered office on the website |
| Privacy notice cites Article 77 and the "right to lodge a complaint with the supervisory authority" | Article 77 omitted 19 June 2026 by DUAA s 103; the route is s 165 DPA 2018 after complaining to the controller under s 164A |
| "By using this site you accept cookies" | Not consent under PECR reg 6 and Sch A1 para 2; consent must meet the UK GDPR standard |
| Analytics fired before a consent decision, justified by the new DUAA exception | Sch A1 para 5 fails if data goes to a third party for its own purposes or is used beyond improving the service |
| Newsletter opt-in bundled into the terms checkbox | PECR reg 22(2) needs prior consent; the soft opt-in under reg 22(3) needs an actual sale or negotiation and similar products only |
| Charity relying on the new soft opt-in for its legacy list | PECR reg 22(3A) only applies to contact details obtained on or after 5 February 2026 |
| "Buy now" or "Submit" as the order button | Reg 14(4) CCRs 2013 requires "order with obligation to pay" or equivalent unambiguous wording; reg 14(5) leaves the consumer unbound |
| Cancellation notice with no model form | Sch 3 Part B CCRs 2013 is a mandatory component of the information duty |
| 14-day cancellation stated but the information duty breached | Reg 31 CCRs 2013 extends the period by up to 12 months |
| Statutory rights described as a "warranty" or "guarantee" | CRA 2015 ss 9–11, 34–36, 49 are statutory rights; a guarantee is additional and must say so |
| Incentivised or filtered reviews shown as organic | Banned practice under DMCC Act 2024 Sch 20; fake reviews and concealed incentives |
| Compulsory fees revealed at checkout | Drip pricing; s 230 DMCC Act 2024 requires the total price in the invitation to purchase |
| Forum or chat launched without an illegal content risk assessment | Ofcom deadline was 16 March 2025; duties under ss 9–10 OSA 2023 apply regardless of size |
| ICO fee never paid | Reg 3 SI 2018/480; enforceable by penalty independently of any other breach |

## Reference files

Each contains the statutory basis with section numbers and status date, the mandatory content points, a template with `[[PLACEHOLDER]]` slots, and a checkpoint list.

- `references/intake.md` — question set to complete before the first text
- `references/website-disclosures.md` — ECR 2002 reg 6, SI 2015/17 reg 25, CA 2006 Part 41, Companies House identity verification
- `references/privacy-notice.md` — UK GDPR Arts 13/14, DUAA changes to lawful basis, ADM, subject access, complaints
- `references/accountability-and-fee.md` — ICO data protection fee, records, processor contracts, breach reporting, DPIA, s 164A complaints handling
- `references/cookies.md` — PECR reg 6 and Sch A1, banner requirements, cookie table, ICO enforcement expectations
- `references/electronic-marketing.md` — PECR regs 22, 23, soft opt-in, charity soft opt-in, CAP Code identification rules
- `references/international-transfers.md` — IDTA, UK Addendum, UK Extension to the DPF, UK adequacy, transfer risk assessment
- `references/consumer-terms.md` — CRA 2015 goods, digital content, services, unfair terms
- `references/cancellation.md` — CCRs 2013 pre-contract information, order button, 14-day cancellation, model cancellation form
- `references/dmcc-trading.md` — DMCC Act 2024 unfair practices, Sch 20 banned practices, fake reviews, drip pricing, subscriptions status, CMA enforcement
- `references/online-safety.md` — OSA 2023 scope, exemptions, risk assessments, Ofcom deadlines, age assurance
- `references/accessibility.md` — Equality Act 2010, SI 2018/952, WCAG 2.2 AA, accessibility statement
- `references/complaints-adr.md` — DMCC Part 4 Ch 4, s 308 notification duty, ODR shutdown, sector ombudsman schemes
- `references/checklist.md` — pre-launch checklist mapped to provisions
