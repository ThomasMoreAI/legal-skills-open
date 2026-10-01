---
name: privacy-vendor-review-clemensjl
title: Third-party vendor and integration review (GDPR / ePrivacy)
description: Use when a third-party service, SDK, script, API or dependency is about to be added to a product, when an existing integration needs a data-protection sign-off, or when someone asks whether a vendor is "GDPR compliant". Also use when a sub-processor list changes, when a vendor announces a new region or a new owner, when an AI or LLM API is wired into a product, and before any launch that ships a tag, pixel, embed or telemetry SDK.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/privacy-vendor-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
sources:
- title: Ai Vendors
  path: references/ai-vendors.md
- title: Artefacts
  path: references/artefacts.md
- title: Checklist
  path: references/checklist.md
- title: Data Inventory
  path: references/data-inventory.md
- title: Device Access
  path: references/device-access.md
- title: Dpia
  path: references/dpia.md
- title: Enforcement
  path: references/enforcement.md
- title: Intake
  path: references/intake.md
- title: Processor Contract
  path: references/processor-contract.md
- title: Role Determination
  path: references/role-determination.md
- title: Transfers
  path: references/transfers.md
- title: Vendors Saas
  path: references/vendors-saas.md
- title: Vendors
  path: references/vendors.md
---

# Third-party vendor and integration review (GDPR / ePrivacy)

Assessment of an external service before it enters a product, and the internal records that assessment must produce. Governing texts: Regulation (EU) 2016/679 (GDPR), in particular Art 4(7)/(8), Art 26, Art 28, Art 30, Art 35 and Chapter V; Directive 2002/58/EC (ePrivacy) Art 5(3) as transposed nationally; Commission Implementing Decision (EU) 2021/914 (SCCs); Regulation (EU) 2024/1689 (AI Act) where the vendor is an AI system or GPAI model.

**Core principle:** "Is this vendor GDPR compliant?" has no answer. Compliance is a property of a deployment, not of a company — the controller carries accountability under Art 5(2) GDPR and cannot inherit it from a vendor badge. Six questions are answerable, and every one of them produces a document:

1. **What personal data does this integration actually transmit?** — verified on the wire, not from the vendor's marketing page.
2. **Is the vendor a processor, an independent controller, or a joint controller for that flow?** — per flow, not per company.
3. **Is there an Art 28 contract in force that covers it?** — in force, not merely published.
4. **Which Chapter V mechanism carries the data out of the EEA?** — including the sub-processor layer.
5. **Does it store or access anything on the user's device, and does it fire before consent?**
6. **What does each answer oblige you to write down?** — ROPA entry, notice paragraph, consent category, sub-processor entry, retention statement, DPIA trigger.

## Limits

This skill produces internal assessment records and draft artefacts, not legal advice.

- A DPO, privacy counsel or the competent supervisory authority signs off on: joint-controller arrangements under Art 26, any transfer where the vendor cannot name a valid mechanism, special-category data under Art 9, children's data, and any DPIA that ends in a residual high risk (Art 36 prior consultation).
- Every produced artefact carries `<!-- DRAFT – not legally approved -->` until that sign-off is confirmed. Never remove the marker silently.
- Every entry in `references/vendors.md`, `references/vendors-saas.md` and `references/ai-vendors.md` is a **dated snapshot**. Vendor terms change without notice. Re-verify against the vendor's live legal page before relying on any line, and re-date it. A snapshot older than the current quarter is a lead, not a finding.

**Boundary.** This skill assesses integrations and writes internal documentation. The published privacy notice, imprint, terms and cookie-policy *text* belongs to the `legal-*` skills; here you produce the factual paragraph content those texts consume.

## Workflow

1. **Intake.** Answer `references/intake.md` first. Unanswered items become `[[MISSING: …]]`; never guess an integration's behaviour.
2. **Observe the flow.** `references/data-inventory.md` — capture what the integration actually sends before reading any vendor claim.
3. **Work the six questions in order**, reading the matching reference file before writing anything. Question 2 decides which contract exists at all; question 5 decides whether the integration may load at page load.
4. **Produce the artefacts** from `references/artefacts.md`.
5. **Run `references/checklist.md`.** Report findings with the article and the location, not as reassurance.
6. **Decide.** Approve with artefacts attached, or reject with the single blocking finding named and the nearest compliant alternative.

**Output shape.** Four parts, in this order:

1. the artefacts (ROPA entry, notice paragraph, consent category, sub-processor entry, retention statement) with the draft marker, or the rejection with its blocking finding
2. the `[[MISSING: …]]` list the user must supply
3. adjacent open items, one sentence each
4. the sign-off note

Reference file names never appear in the delivered output.

## Decision matrix

| Situation | What applies | Reference |
|---|---|---|
| New SDK, script, tag, embed or API added to a product | Full six-question review | `intake.md`, `data-inventory.md` |
| Vendor claims "we are just a processor" | Art 4(7)/(8), Art 26, Art 28 role test | `role-determination.md` |
| Ad platform, pixel, conversion API, social embed | Joint controllership under Art 26, Fashion ID line | `role-determination.md`, `enforcement.md` |
| Payment provider, fraud/AML tooling, KYC | Split roles: processor for payment execution, independent controller for fraud and legal duties | `role-determination.md` |
| Contract review before signature | Art 28(3) checklist, Art 28(2)/(4) sub-processor chain | `processor-contract.md` |
| Any data reaching a non-EEA entity, including remote support access | Chapter V mechanism, TIA, supplementary measures | `transfers.md` |
| Vendor is US-based | DPF entity lookup, SCC module choice, FISA 702 exposure | `transfers.md`, `enforcement.md` |
| Anything that sets cookies, writes localStorage, reads IndexedDB or fingerprints | ePrivacy Art 5(3), consent gating, CMP category | `device-access.md` |
| Analytics, session replay, heatmaps, error telemetry | Art 5(3) plus role test plus retention | `device-access.md`, `vendors.md` |
| Newsletter or transactional e-mail tooling | Open- and click-tracking pixels are an Art 5(3) event in the recipient's mail client | `enforcement.md`, `vendors-saas.md` |
| Named vendor already reviewed before | Dated snapshot, must be re-verified | `vendors.md`, `vendors-saas.md` |
| LLM / AI API, AI feature, model provider | Training defaults, retention, ZDR, AI Act Art 50 | `ai-vendors.md` |
| Large-scale, novel, monitoring or profiling integration | Art 35 trigger test, national blacklist | `dpia.md` |
| Producing the records after approval | Art 30(1), Art 13(1)(e)/(f), retention | `artefacts.md` |
| Pre-launch or pre-signature gate | Findings list with article and location | `checklist.md` |

## Hard rules

- **"GDPR compliant" is not a finding.** Art 5(2) puts accountability on the controller. A vendor's ISO 27001, SOC 2, TISAX or self-declared "GDPR ready" badge says nothing about Art 28, Art 30 or Chapter V for *your* deployment. Record the six answers, not the badge.
- **ePrivacy Art 5(3) does not care whether it is personal data.** Art 5(3) Directive 2002/58/EC covers "the storing of information, or the gaining of access to information already stored" on a subscriber's or user's terminal equipment. EDPB Guidelines 2/2023 on the technical scope of Art 5(3), Version 2.0, adopted 07.10.2024, confirm the threshold is *information*, not personal data, and analyse URL and pixel tracking, local processing, IP-only tracking, IoT reporting and unique identifiers. "No cookies, only localStorage", "only a fingerprint" and "only a tracking pixel" are all inside the rule.
- **Check the DPF entity, not the brand.** EU-US Data Privacy Framework participation attaches to a named legal entity with a scope (HR data / non-HR data) and a status. Verify the exact contracting entity on `dataprivacyframework.gov/list` and record the certification status and date. A parent company's certification does not cover a subsidiary that is not listed.
- **A third-party tag is *your* transfer.** EDPB Guidelines 05/2021 v2.0 (14.02.2023): personal data disclosed via cookies is "not considered as being disclosed directly by the data subject, but rather as a transmission by the operator of the website that the data subject is visiting". The site operator is the exporter for every third-country script its page loads — the visitor's browser making the request does not shift that.
- **An EU region does not end the transfer question.** Remote access from a third country — support, on-call engineering, a US-based sub-processor — is a transfer under Chapter V (EDPB Guidelines 05/2021 on the interplay of Art 3 and Chapter V). Ask where support sits and where sub-processors sit, not only where the bucket sits.
- **A published DPA is not a DPA in force.** Art 28(9) requires the contract in writing, including electronic form. Determine whether the master terms incorporate the addendum by reference automatically or whether an acceptance step exists in the dashboard. If an acceptance step exists and was never performed, the processing has no Art 28 basis — that is a blocking finding, not a to-do.
- **A vendor that reserves its own use rights is not your processor for that use.** Art 28(3)(a) requires processing only on documented instructions. Terms permitting the vendor to use the data for its own product improvement, benchmarking, model training or ad measurement describe an independent controller (or joint controller) for that purpose, which needs its own legal basis and its own notice paragraph.
- **Never write a retention period you cannot point at a setting for.** If the vendor's dashboard has no retention control and the terms name no period, the answer is `[[MISSING: retention period — no vendor setting found]]`, not "as long as necessary".
- **Never invent the user's stack.** Contracting entity, region setting, plan tier, signed DPA date, consent-manager category and legal basis are facts about the user's deployment. Unknown values become `[[MISSING: …]]` in the artefact and in the report.
- **The vendor reference files expire.** Treat every line in `vendors.md` and `ai-vendors.md` as valid only for the date stamped on it. Re-check the vendor's own page before approving.

## False friends

| Plausible wrong assumption | Actual position |
|---|---|
| "Vendor is SOC 2 / ISO 27001 certified, so we are covered" — security-questionnaire habit | Security certifications address Art 32 only. They say nothing about role, Art 28, Chapter V or Art 5(3). |
| "We signed SCCs, so the transfer is done" | Schrems II (CJEU 16.07.2020, C-311/18) requires a case-by-case assessment of the destination's law plus supplementary measures where needed. SCCs without a transfer impact assessment are an incomplete mechanism. |
| "They are DPF-certified, so no SCCs are needed" | Only for the listed entity, only while Active, and only within its certified data scope. Sub-processors outside the DPF still need their own mechanism. |
| "No cookies, so no consent banner" — from cookie-centric US guidance | Art 5(3) ePrivacy covers any storage or access on the device, cookies or not. |
| "IP anonymisation makes it non-personal" | The Austrian DSB rejected exactly this for Google Analytics (decision 2021-0.586.257, published 12.01.2022): the remaining identifiers still singled out the user. |
| "Consent Mode v2 solves Google Analytics" | Consent Mode changes what Google receives; it does not answer the Chapter V question and, in its default modelling configuration, still contacts Google endpoints. |
| "We have a BAA" / "they signed our CCPA service-provider addendum" — US import | Neither is an Art 28 GDPR contract. Art 28(3) requires the eight specific undertakings; a HIPAA BAA and a CCPA addendum contain none of them. |
| "Auftragsverarbeitung because we pay them" | The role follows who determines purposes and means (Art 4(7), EDPB Guidelines 07/2020 v2.0, 07.07.2021), not who invoices whom. |
| "The sub-processor list is our authorisation" | Art 28(2) requires prior specific or general written authorisation plus notice of changes plus a real objection right. A page that changes silently is none of those. |
| "The pixel is the ad platform's problem" | CJEU 29.07.2019, C-40/17 Fashion ID: the site operator is a joint controller for the collection and the transmission to the plugin provider, even without access to the data. |
| "US privacy risk is only GDPR" | CIPA §§ 631/638.51 pixel and session-replay claims are a separate, US-side reason to gate the same tags behind consent. |
| "An analytics or captcha tool is obviously our processor" | Not always, and it changes. Microsoft states Microsoft Clarity is GDPR-compliant **as a data controller**; Google's reCAPTCHA was an independent controller until **02.04.2026** and a processor after it. Read the vendor's own role statement and date it. |
| "It is open source / self-hosted, so no review" | Self-hosting removes the transfer and Art 28 questions, not the Art 5(3), Art 30 and notice questions. |

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| Reviewing the vendor instead of the integration | The same vendor can be a processor in one flow and an independent controller in another |
| Reading the vendor's privacy policy as the contract | The consumer privacy policy governs the vendor's own site, not your data. The DPA governs your data. |
| Recording "Google" as the recipient | Art 30(1)(d) needs the categories of recipients and, for transfers, the third country and the safeguard — plus which Google entity |
| Approving before observing the network traffic | Vendor documentation routinely understates what the default snippet loads |
| Consent category "necessary" for error telemetry | Error tracking is not strictly necessary to provide the service the user requested; it needs consent if it touches the device |
| Treating an embed as content rather than a processor question | YouTube, Maps, fonts and captchas all contact a third party from the user's browser |
| No sub-processor monitoring after approval | Art 28(2) objection rights are worthless if nobody reads the notification |
| Ignoring the vendor's own AI/product-improvement clause | Converts your processor into a controller for that purpose without you noticing |
| One DPIA per company rather than per processing | Art 35 attaches to processing operations, not to suppliers |
| Approval with no expiry | Terms, sub-processors and regions change; an undated approval is not evidence of accountability |

## Reference files

- `references/intake.md` — questions to answer before any assessment
- `references/data-inventory.md` — establishing what the integration actually transmits
- `references/role-determination.md` — controller / processor / joint controller test and the cases that break it
- `references/processor-contract.md` — Art 28(3) checklist, sub-processor chain, audit rights
- `references/transfers.md` — Chapter V, adequacy list, DPF, SCC modules, TIA, UK and Swiss variants
- `references/device-access.md` — ePrivacy Art 5(3), consent gating, CMP category assignment
- `references/artefacts.md` — ROPA entry, notice paragraph, retention statement, sub-processor entry
- `references/dpia.md` — Art 35 trigger test and national blacklists
- `references/vendors.md` — dated findings: infrastructure, analytics, payments, ad platforms
- `references/vendors-saas.md` — dated findings: email, support, embeds, forms, workplace tools
- `references/ai-vendors.md` — LLM and AI APIs: training defaults, retention, ZDR, AI Act
- `references/enforcement.md` — decisions and regulatory positions with citations
- `references/checklist.md` — pre-approval gate producing findings
