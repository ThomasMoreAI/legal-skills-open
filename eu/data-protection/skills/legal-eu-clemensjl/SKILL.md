---
name: legal-eu-clemensjl
title: EU baseline for online legal texts
description: Use when writing, reviewing, or fixing the EU-law layer of legally required texts for a website, webshop, app, platform, or newsletter reaching the European Union — privacy notice, cookie banner and consent flow, distance-selling information, withdrawal instructions, conformity and guarantee wording, DSA notice-and-action, AI transparency, accessibility information — or when asked whether an online product is EU-compliant. Also use when a template cites an EU directive article at a consumer, when a US or single-member-state template is about to be reused across the EU, when personal data processing starts, or before an EU-facing product goes live.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/legal-eu
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
sources:
- title: Accessibility
  path: references/accessibility.md
- title: Ai Act
  path: references/ai-act.md
- title: Checklist
  path: references/checklist.md
- title: Conformity
  path: references/conformity.md
- title: Consent Cookies
  path: references/consent-cookies.md
- title: Consumer Distance
  path: references/consumer-distance.md
- title: Dsa
  path: references/dsa.md
- title: Gdpr Internal
  path: references/gdpr-internal.md
- title: Gdpr Notice
  path: references/gdpr-notice.md
- title: Gdpr Transfers
  path: references/gdpr-transfers.md
- title: Intake
  path: references/intake.md
- title: National Layer
  path: references/national-layer.md
- title: Other Instruments
  path: references/other-instruments.md
- title: Unfair Terms Practices
  path: references/unfair-terms-practices.md
- title: Withdrawal
  path: references/withdrawal.md
---

# EU baseline for online legal texts

The EU-level layer that applies in every member state. Grounded in the GDPR, the ePrivacy Directive, the DSA, the Consumer Rights Directive as amended by the Omnibus and the distance-financial-services and green-transition directives, the Digital Content and Sale of Goods Directives, the Unfair Contract Terms and Unfair Commercial Practices Directives, the EAA, the AI Act, the GPSR, P2B, the Data Act, the CRA and NIS2. This skill is the baseline a national skill sits on top of. It covers no member state's implementing act — it only flags where one is required.

**Core principle:** an EU **Regulation** applies directly and identically in every member state; an EU **Directive** does not. The Consumer Rights Directive, the Digital Content and Sale of Goods Directives, the ePrivacy Directive, the EAA and NIS2 reach a user only through a national transposing act that differs in periods, thresholds, wording and remedies — and a directive has no horizontal direct effect between private parties (Art 288 TFEU; **Case C-91/92 Faccini Dori**). A template that cites a directive article at a consumer is citing an instrument that does not bind the consumer or the trader. Cite the national statute, or describe the right without a citation.

## Not legal advice

This skill produces drafts and findings, not legal advice. Before go-live:

- Webshop, subscription, payment processing, children's data, health data, biometrics, platform operation, or any high-risk AI use: **obtain sign-off from a qualified lawyer in the relevant member state.**
- Free first-line help: the national supervisory authority via the EDPB members list (edpb.europa.eu/about-edpb/our-members_en), the **European Consumer Centres Network** (eccnet.eu) for cross-border consumer questions, the **Enterprise Europe Network** (een.ec.europa.eu) for SMEs, and **Your Europe Business** (europa.eu/youreurope/business) for the official cross-border summaries.
- Every generated text carries a visible `<!-- DRAFT – NOT LEGALLY APPROVED -->` HTML comment until the user confirms legal sign-off. Never remove the marker silently.

Never omit or soften this section in the output.

## Workflow

1. **Run the intake first.** No text before the answers. Questions in `references/intake.md`. Question 1 decides which national skill has to run afterwards.
2. **Determine the obligation matrix** below: which texts this specific project needs.
3. **Read the reference file for each obligation before drafting.** Never from memory — the article numbers are too specific and several changed in 2025 and 2026.
4. **Run `references/checklist.md`**, reporting each finding with its instrument and article.
5. **Report every national dependency as an explicit gap**, using `references/national-layer.md`.
6. Output the approval notice; leave the draft marker in place.

**Shape of the output.** Exactly four parts, in this order:

1. the legal text or finding itself, with the draft marker
2. the list of `[[MISSING: …]]` items the user must supply, including every national-layer gap
3. adjacent obligations open in the same project, one sentence each
4. the approval notice

The instrument and article sit next to the statement they support. Reference-file names and paths appear in none of the four parts — they are working material, not part of the delivery.

## Obligation matrix

| Situation | Required at EU level | Reference |
|---|---|---|
| Any processing of personal data, including server logs | Privacy notice under Art 13/14 GDPR | `gdpr-notice.md` |
| Any processing of personal data | Records, processor contracts, breach procedure, DPIA screening, DPO test (internal, not published) | `gdpr-internal.md` |
| Any recipient outside the EEA, including remote access | Chapter V transfer basis per recipient | `gdpr-transfers.md` |
| Any storage on or read from the user's device beyond strict necessity | Consent before access, Art 5(3) Dir 2002/58/EC | `consent-cookies.md` |
| Email or SMS marketing | Prior consent or Art 13(2) soft opt-in, all three conditions | `consent-cookies.md` |
| Selling to consumers at a distance | Precontractual information, order button, marketplace disclosures, price-reduction rules | `consumer-distance.md` |
| Selling to consumers at a distance | Withdrawal instruction, model form, **Art 11a withdrawal function** | `withdrawal.md` |
| Selling goods, digital content or digital services | Conformity, update duty, guarantee wording | `conformity.md` |
| Any standard terms, any consumer-facing interface | Unfair-terms and unfair-practices screening, dark patterns | `unfair-terms-practices.md` |
| Hosting third-party content, forum, comments, reviews, marketplace | DSA points of contact, notice and action, statement of reasons, trader traceability | `dsa.md` |
| Any AI system, chatbot or generative feature | Art 50 transparency, AI literacy, prohibited-practice and high-risk screening | `ai-act.md` |
| B2C e-commerce service, not a microenterprise | Annex V accessibility information in the terms | `accessibility.md` |
| Physical products, business users, connected products, cloud, regulated sectors | GPSR, CRA, P2B, Data Act, NIS2 scope tests; **ODR shutdown** | `other-instruments.md` |
| Any project touching a single member state | The national layer that this skill deliberately omits | `national-layer.md` |

## Hard rules

- **Never cite a directive article at a consumer.** Art 288 TFEU: a directive binds the member state, not the private party. **Case C-91/92 Faccini Dori** refused horizontal direct effect. "Under Art 9 of Directive 2011/83/EU you may withdraw within 14 days" is wrong on the instrument and possibly wrong on the period. Cite the national provision or state the right plainly.
- **The ODR platform is dead.** Regulation (EU) 2024/3228 repealed Regulation (EU) No 524/2013 with effect from **20.07.2025**; complaint submission stopped 20.03.2025 and all data was deleted by 20.07.2025. The Art 14 duty to link to it fell away with it. Any ODR link is a dead link and a false statement about a redress route. Remove it from footers, terms, order emails and shop-system defaults; never add it back.
- **No terminal-equipment access before consent.** Art 5(3) Directive 2002/58/EC covers cookies, `localStorage`, `sessionStorage`, IndexedDB, pixels, beacons, cache- and URL-based tracking, fingerprinting and IoT reporting — **regardless of whether personal data is involved** (EDPB Guidelines 2/2023 v2.0, 16.10.2024). Reject must sit on the first banner layer, visually equivalent to Accept. No pre-ticked boxes, no default-on sliders.
- **The digital consent age is not 16 across the EU.** Art 8(1) GDPR sets 16 as the default and expressly allows member states to go down to **13**. Verified spread: 13 in Belgium, Finland, Portugal and Sweden; 14 in Austria, Italy and Spain; 15 in Czechia, Denmark and France; 16 in Germany, Ireland, the Netherlands and Poland. Thirteen member states remain unverified. Never state a single EU-wide age; state the member state's figure with its statute, or report it as missing. See the table in `gdpr-notice.md`.
- **The order button carries the national statutory wording.** Art 8(2) Directive 2011/83/EU requires "order with obligation to pay" **or a corresponding unambiguous formulation**, and each member state enacted its own. The sanction is not a fine: **"If the trader has not complied with this subparagraph, the consumer shall not be bound by the contract or order."** Never translate the English phrase and treat it as compliant.
- **A withdrawal function is mandatory on online interfaces since 19.06.2026.** Art 11a of Directive 2011/83/EU, inserted by Directive (EU) 2023/2673: a continuously available "withdraw from contract here" function, a separate "confirm withdrawal" step, and a durable-medium acknowledgement with date and time. Recital 37 extends it beyond financial services to all distance contracts with a withdrawal right. It is not the German-style contract-cancellation button.
- **The AI Act high-risk dates moved.** Regulation (EU) 2026/1744 (Digital Omnibus on AI), in force 27.07.2026, pushed Annex III standalone high-risk systems to **02.12.2027** and Annex I product-embedded systems to **02.08.2028**. Art 50 transparency still applies from **02.08.2026**. Any plan still keyed to 02.08.2026 for high-risk is wrong.
- **Do not draft to unadopted law.** The ePrivacy Regulation proposal was **withdrawn** (OJ notice 06.10.2025) — Directive 2002/58/EC stays. The Digital Omnibus Regulation COM(2025) 837, which would amend the GDPR and repeal P2B, is at European Parliament committee stage and **is not law**. Only the AI omnibus was adopted.
- **Never invent facts about the business.** Legal name, registered office, register number, VAT number, supervisory authority, representative, responsible person, retention periods, processor list: if unknown it becomes `[[MISSING: …]]` in the text and in the report, never a plausible-looking value.
- **Every national dependency is reported, never defaulted.** Withdrawal period, guarantee period, burden-of-proof period, order-button wording, consent age, supervisory authority, consent lifetime: each is `[[MISSING: … — <member state>]]` until the national skill supplies it.

## False friends

Assumptions imported from a single member state or from outside the EU that do not hold at EU level.

| Imported assumption | Position at EU level |
|---|---|
| "§ 5 TMG / § 5 DDG governs the imprint" (Germany) | No single EU imprint provision. Art 5 of Directive 2000/31/EC sets the minimum; the operative rules are national and stack differently per member state |
| "§ 312k BGB cancellation button" (Germany) | Not an EU rule. What EU law now requires is the **Art 11a CRD withdrawal function** — a different thing: exercising withdrawal, not terminating a continuing contract |
| "Widerrufsrecht" as the universal term | The EU term is withdrawal; each member state has its own statutory word, and Austria's is *Rücktritt*, not *Widerruf* |
| "20 employees triggers a DPO" (Germany, § 38 BDSG) | Art 37(1) GDPR has no headcount threshold. Headcount rules are national law under Art 37(4) |
| "Consent age is 16 everywhere" | Art 8(1) default is 16 with an express option down to 13. Ten of the fourteen verified member states deviate; only Germany, Ireland, the Netherlands and Poland sit at 16 |
| "Two years' guarantee across the EU, one year's reversed burden of proof" | Art 10(3)/(5) and Art 11(2) of Dir (EU) 2019/771 are member-state options. Both figures vary |
| "Link the EU ODR platform in the footer" | Repealed; the platform ceased operating 20.07.2025 |
| "CCPA-style notice at collection is enough" (US) | Arts 13/14 GDPR require purpose, **legal basis per processing**, recipients, retention, transfers and the full rights list, before or at collection |
| "Legitimate interest covers analytics cookies" (US/UK habit) | Art 5(3) ePrivacy requires **consent** for the device access itself; the EDPB Cookie Banner Taskforce ruled out legitimate interest for placement, and a missing consent cannot be rescued downstream |
| "We are not established in the EU, so the GDPR does not apply" | Art 3(2) catches offering goods or services to, or monitoring the behaviour of, data subjects in the Union, and Art 27 then requires an EU representative |
| "The DSA is only for big tech" | Chapter III Sections 1 and 2 bind every intermediary and hosting provider with **no size exemption**. Only Sections 3 and 4 have micro/small reliefs, and they are three separate provisions — Arts 19, 29 and 15(2) |
| "The AI Act only matters for high-risk systems" | Art 4 AI literacy binds every provider and deployer, and Art 50 transparency binds chatbots and generative features from 02.08.2026 |
| "EN 301 549 gives us presumption of conformity under the EAA" | No harmonised standard is cited in the OJ under Directive (EU) 2019/882. EN 301 549 V3.2.1 is harmonised only under the public-sector Directive (EU) 2016/2102 |
| "We need a public accessibility statement with a feedback and enforcement link" | That is Directive (EU) 2016/2102, public sector. A private e-commerce service owes the **EAA Annex V** information in its terms and conditions |

If an obligation comes to mind that cannot be traced to a named EU instrument and article, it is not asserted — it is reported as an open question.

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| One legal basis stated for the whole website | Art 13(1)(c) GDPR requires the basis **per processing purpose** |
| Privacy notice lists services the site does not load, or omits ones it does | Checked against the network trace, not against intent |
| "This site uses cookies. OK" | Not a clear affirmative action under Art 4(11) GDPR |
| Google Fonts, Maps, YouTube, reCAPTCHA loaded before consent | Terminal-equipment access plus a third-country transfer before any basis exists |
| Order button labelled "Buy", "Submit" or "Continue" | Art 8(2) CRD — the consumer is not bound by the contract |
| Withdrawal instruction without the model form | Art 6(1)(h) CRD requires the Annex I(B) form to be supplied |
| No withdrawal function on the site | Art 11a CRD, mandatory since 19.06.2026 |
| "-40 %" computed against a list price | Art 6a Dir 98/6/EC and **Case C-330/23 Aldi Süd**, 26.09.2024 — the percentage must be computed against the 30-day low |
| Review badge without any verification step | Annex I point 23b UCPD, unfair in all circumstances |
| DSA cited as the fix for a misleading cookie banner | Art 25(2) DSA excludes practices covered by the UCPD or the GDPR |
| Chatbot with the AI disclosure only in the terms | Art 50(5) AI Act requires it at the first interaction |
| DPF named as the sole US transfer basis | Valid, but under appeal in **Case C-703/25 P**; always keep a fallback |
| Marketplace with no trader traceability | Art 30 DSA, subject only to the Art 29 micro/small exemption |
| Physical product sold with no EU responsible person | Art 16 GPSR — the product may not be placed on the market at all |

## Reference files

Each carries the instrument, the article numbers, a status date, the mandatory content, a template with `[[PLACEHOLDER]]` slots, and checkpoints.

- `references/intake.md` — questions to answer before the first text
- `references/national-layer.md` — per instrument, what a national skill must add on top
- `references/gdpr-notice.md` — Arts 12–22 GDPR, information duties, legal bases, special categories, child consent per member state
- `references/gdpr-internal.md` — Arts 27, 28, 30, 33–37 GDPR: representative, processor contracts, records, breach, DPIA, DPO
- `references/gdpr-transfers.md` — Chapter V, adequacy list, SCCs, the Data Privacy Framework and its appeal
- `references/consent-cookies.md` — Art 5(3) and Art 13 Dir 2002/58/EC, consent standard, banner design, pay-or-consent
- `references/consumer-distance.md` — Dir 2011/83/EU and the Omnibus: precontractual information, order button, marketplaces, price reductions, reviews
- `references/withdrawal.md` — periods, exceptions, effects, model form, the Art 11a withdrawal function
- `references/conformity.md` — Dir (EU) 2019/770 and 2019/771 as amended by the Repair Directive
- `references/unfair-terms-practices.md` — Dir 93/13/EEC and Dir 2005/29/EC, blacklists, dark patterns
- `references/dsa.md` — Reg (EU) 2022/2065 tiers, exemptions, notice and action, trader traceability
- `references/ai-act.md` — Reg (EU) 2024/1689 as amended by Reg (EU) 2026/1744, timeline, Art 50
- `references/accessibility.md` — Dir (EU) 2019/882, scope, microenterprise exemption, Annex V versus public-sector statements
- `references/other-instruments.md` — ODR shutdown and ADR, GPSR, CRA, P2B, Data Act, NIS2
- `references/checklist.md` — pre-launch checklist with instrument and article per item
