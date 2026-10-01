---
name: saas-legal-generator-briansunter
title: SaaS Legal Drafting Assistant
description: Create an attorney-review-ready SaaS legal drafting package from an evidence-based data and product inventory. Use whenever the user needs a privacy notice, terms of service, cookie notice, acceptable use policy, DPA, CCPA/CPRA notice, vendor disclosure, or a gap analysis of existing legal pages. This skill flags issues and drafts language for review.
author: briansunter
author_url: https://github.com/briansunter/kungfu/tree/master/skills/saas-legal-generator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# SaaS Legal Drafting Assistant

Generate tailored drafts and an issue list for professional review. Laws,
thresholds, contracts, and enforcement guidance change; use current official
sources for the selected jurisdiction.

## Hard Rules

- Never describe generated documents as “legally compliant,” “complete,” or
  universally required.
- Use current official legal and regulatory sources for every selected
  jurisdiction.
- Do not infer legal entity name, address, governing law, dispute forum, age
  eligibility, retention period, lawful basis, data sale/sharing, or contact
  details.
- Distinguish the service’s role as controller/business, processor/service
  provider, or both by processing activity.
- The published notice must match actual code, vendors, contracts, and
  operations. Policy text cannot repair a noncompliant product flow.
- Do not deploy nonessential cookies or tracking merely because a banner exists.
  Where consent is required, block the relevant technology until valid choice is
  obtained and preserve withdrawal.
- Do not add a California “Do Not Sell or Share” link or claim CCPA
  applicability without assessing coverage and practices. Covered businesses
  must also process applicable opt-out preference signals such as Global Privacy
  Control.
- Require qualified counsel review for launch, material data changes, regulated
  data, children, biometrics, AI profiling, international transfers, enterprise
  DPAs, or disputes.

## Start With a Legal Data Map

Inspect the repository, infrastructure, website, app stores, analytics, payment,
email, support, and auth integrations. Then confirm:

- legal entity, trade names, addresses, and contacts;
- service, users, countries, and age restrictions;
- data categories, sources, purposes, and recipients;
- processing roles and lawful bases where relevant;
- cookies, pixels, SDKs, local storage, and consent behavior;
- vendors/subprocessors and processing locations;
- retention rules and deletion mechanics;
- user rights request, appeal, verification, and opt-out workflows;
- security controls and incident process;
- billing, renewals, refunds, trials, and cancellation;
- user content, IP licenses, acceptable use, suspension, and termination;
- governing law, dispute approach, and contract hierarchy;
- regulated data or sector-specific requirements.

Label each item `Verified in product`, `User confirmed`, `Assumption`, or
`Unknown`.

## Determine Scope Before Drafting

Create a jurisdiction/obligation matrix rather than automatically adding every
law:

| Question | Evidence needed |
| --- | --- |
| Which privacy laws may apply? | Entity, location, targeting, thresholds, data practices |
| Is consent required for a technology? | Purpose, device access, jurisdiction, exemption |
| Is the company selling/sharing data? | Contract and data-flow analysis, not marketing labels |
| Is a DPA needed? | Controller/processor relationship and customer contract |
| Are transfer terms needed? | Origin, destination, mechanism, vendor contracts |
| Are children involved? | Actual audience, age gates, knowledge, and product design |
| Are accessibility/local-language duties relevant? | Market and service context |

Escalate uncertain threshold or conflict-of-law questions to counsel instead of
guessing.

## Drafting Workflow

### 1. Create the Configuration

Use [`example_config.json`](example_config.json) as a starting point. Preserve
unknown fields as explicit placeholders; do not silently choose defaults with
legal effect.

### 2. Generate a Baseline

```bash
cd skills/saas-legal-generator
bun run scripts/index.ts
# or
bun run scripts/index.ts config.json
```

[`scripts/index.ts`](scripts/index.ts) accelerates assembly. Its output is a
draft that must be compared with the data map and current law.

### 3. Tailor the Documents

Select only applicable documents:

- [Global privacy policy](templates/privacy-policy-global.md)
- [SaaS terms of service](templates/terms-of-service-saas.md)
- [Cookie policy](templates/cookie-policy.md)
- [Acceptable use policy](templates/acceptable-use-policy.md)
- [Data processing agreement](templates/data-processing-agreement.md)
- [CCPA/CPRA opt-out notice](templates/ccpa-opt-out-link.md)

For each clause attach its source: product behavior, contract term, business
decision, or legal requirement. Do not leave broad “may collect anything”
language when actual practices can be stated precisely.

### 4. Validate Product-to-Policy Consistency

Check:

- every SDK/vendor appears in the relevant disclosure and contract inventory;
- consent and preference changes actually alter data collection;
- deletion/export/request workflows work end to end;
- retention periods match jobs, backups, legal holds, and vendor deletion;
- trial, renewal, refund, and cancellation flows match the terms;
- links are visible before account creation and purchase where appropriate;
- material changes have a notice/versioning plan;
- no critical placeholders remain.

A passive “by continuing you agree” banner is not a valid default for
nonessential cookies where affirmative consent is required.

### 5. Produce Counsel Review Materials

Return both redlines and a concise issue list:

- high-risk unresolved decisions;
- assumptions that counsel must confirm;
- clause alternatives and business trade-offs;
- evidence/source behind each material statement;
- product changes required beyond documents;
- owner and review date;
- change log and effective-date plan.

## Output Contract

Return:

1. scope;
2. verified legal/data inventory;
3. jurisdiction and obligation matrix;
4. missing decisions and counsel triggers;
5. selected draft documents;
6. product-to-policy gap report;
7. implementation checklist for consent, rights, retention, and links;
8. placeholder report and attorney review packet.

Generated examples may be stored in `output/`, but must not be treated as
production-ready.

## Sources

- [General Data Protection Regulation |
  EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [Guidelines 05/2020 on Consent | European Data Protection
  Board](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en)
- [Cookies and Similar Technologies | UK Information Commissioner's
  Office](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/guidance-on-the-use-of-cookies-and-similar-technologies/)
- [California Consumer Privacy Act | California Department of
  Justice](https://oag.ca.gov/privacy/ccpa)
- [Global Privacy Control | California Department of
  Justice](https://oag.ca.gov/privacy/ccpa/gpc)
- [PIPEDA | Office of the Privacy Commissioner of
  Canada](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/)
- [LGPD | Brazil National Data Protection
  Authority](https://www.gov.br/anpd/pt-br)
