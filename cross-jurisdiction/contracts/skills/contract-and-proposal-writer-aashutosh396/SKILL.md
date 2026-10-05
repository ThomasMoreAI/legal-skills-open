---
name: contract-and-proposal-writer-aashutosh396
title: Contract & Proposal Writer
description: Use when drafting a freelance contract, client proposal, SOW, NDA, or MSA — generates jurisdiction-aware (US/EU/UK/DACH) business documents with key-clause options and pandoc docx conversion. Starting points, not a substitute for legal counsel.
author: aashutosh396
author_url: https://github.com/aashutosh396/mindpalace/tree/main/mindpalace/skills/global/documents/contract-and-proposal-writer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: contracts
language: en
tags: [contract, proposal, sow, nda, msa, dpa, gdpr, jurisdiction, freelance, pandoc]
---

# Contract & Proposal Writer

Generate professional, jurisdiction-aware business documents: freelance/dev contracts, proposals, SOWs, NDAs, MSAs. Markdown output → docx via pandoc. Covers US (Delaware), EU (GDPR), UK, DACH (German law). **Not legal advice** — strong starting points; review with an attorney for high-value/complex work.

## Workflow
1. **Gather requirements:** document type; jurisdiction; engagement type (fixed/hourly/retainer); parties (names, roles, addresses); scope (1-3 sentences); total value or rate; dates/duration; special requirements (IP assignment, white-label, subcontractors).
2. **Select template** (dev fixed, consulting retainer, SaaS partnership, NDA mutual/one-way, SOW).
3. **Generate & fill** all `[BRACKETED]` placeholders; flag missing data as "REQUIRED".
4. **Convert to docx:** `pandoc contract.md -o contract.docx --reference-doc=company-template.docx --number-sections -V geometry:margin=1in`.

## Key clause options
| Clause | Options |
|---|---|
| Payment | Net-30, milestone-based, monthly retainer |
| IP ownership | Work-for-hire (US), assignment (EU/UK), license-back |
| Liability cap | 1x contract value (standard), 3x (high-risk) |
| Termination | For cause (14-day cure), convenience (30/60/90-day notice) |
| Confidentiality | 2-5 year term, perpetual for trade secrets |
| Warranty | "As-is" disclaimer, limited 30/90-day fix warranty |
| Dispute resolution | Arbitration (AAA/ICC/LCIA/DIS), courts (per jurisdiction) |

## Jurisdiction notes
- **US (Delaware):** work-for-hire doctrine (Copyright Act §101); AAA arbitration; non-competes enforceable with reasonable scope.
- **EU (GDPR):** DPA required if processing personal data; IP assignment may need a separate written deed; ICC/local-chamber arbitration.
- **UK:** English law; Patents Act 1977 / CDPA 1988; LCIA; UK GDPR.
- **DACH:** BGB governs; written-form requirement (§126 BGB — include a Schriftformklausel); author retains moral rights, must explicitly transfer Nutzungsrechte; non-competes max 2 years with compensation (§74 HGB); DSGVO mandatory; statutory notice periods.

## GDPR DPA (Art. 28) — clause block for EU/DACH
Include subject matter, data-subject categories, personal-data categories, processing duration, processor obligations (process only on documented instructions, confidentiality, Art. 32 measures, assist with data-subject requests, no sub-processors without consent, delete/return on termination), sub-processor list, and cross-border transfer mechanism (SCCs / adequacy / BCRs).

## Common pitfalls
Missing IP-assignment language (work-for-hire alone insufficient in EU/DACH); vague acceptance criteria; no change-order process (scope creep kills fixed-price); jurisdiction mismatch; missing liability cap; oral amendments. Prefer milestone payments over net-30 for >$10K; add force majeure for >3-month engagements; specify return/destruction of confidential materials in NDAs; version-control templates and review annually.
