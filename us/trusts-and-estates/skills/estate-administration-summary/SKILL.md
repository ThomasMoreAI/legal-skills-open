---
name: estate-administration-summary
title: Estate Administration Summary
description: Generates a structured U.S. estate administration/probate status summary covering decedent identifiers, asset inventory, creditor claims, distributions, tax compliance, disputes, and next steps with source citations. Trigger on requests for estate administration summary, probate status report, executor update, estate progress report, inventory and appraisal summary, creditor claims status, or distribution schedule summary.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/estate-administration-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [summarization, summary, transactional]
---

# Estate Administration Summary

Structured snapshot of probate/estate administration status: actions completed, outstanding issues, and remaining work.

## Quick Start

1. Collect governing instruments (will, codicils, trust, intestacy determination), probate case data, asset inventory with appraisals, creditor records, beneficiary roster, tax filings, and any litigation filings.
2. Walk through each output section in order.
3. Cite every factual statement (document name + date + page/paragraph). Mark missing or uncertain facts `UNKNOWN` and list them in Open Questions.

## Output Sections

### 1) Matter Header

Field | Value | Source
--- | --- | ---
Decedent (full name) | |
Date of death | |
Domicile at death | |
Jurisdiction / court | |
Case number | |
Personal representative / executor | |
Relationship to decedent | |
Appointment date | |
Governing instrument | will / trust / intestacy |
Bond required? | yes / no / unknown |
Status as of | YYYY-MM-DD |

### 2) Estate Snapshot

- Gross estate value (as of date):
- Known liabilities (as of date):
- Cash on hand / reserves:
- Distributions to date (total):
- Anticipated remaining duration:

### 3) Assets & Valuation

Asset | Category | Ownership/Title | Value (date) | Status | Beneficiary/Plan | Issues | Source
--- | --- | --- | --- | --- | --- | --- | ---
 | | | | retained/sold | | |

### 4) Creditor Claims

Statutory claims deadline: [date] — Source: [cite]

Creditor | Amount Claimed | Priority Class | Status | Resolution Date | Notes | Source
--- | --- | --- | --- | --- | --- | ---
 | | | approved/rejected/paid/pending | | |

### 5) Distributions

Recipient | Relationship | Asset/Cash | Value | Date | Authority | Source
--- | --- | --- | --- | --- | --- | ---
 | | | | | order/consent |

### 6) Tax Compliance

- [ ] Final individual return (Form 1040) — date:
- [ ] Fiduciary returns (Form 1041 / state) — periods:
- [ ] Estate tax return required? (Form 706 / state) — basis:
- [ ] Taxes paid / liabilities outstanding:
- [ ] Audits, notices, or disputes:

### 7) Disputes / Litigation

Issue | Parties | Procedural Status | Next Deadline | Impact on Administration | Source
--- | --- | --- | --- | --- | ---
 | | | | |

### 8) Administration Timeline

Date | Event | Source
--- | --- | ---
 | |

### 9) Beneficiary Communications & Accountings

- Beneficiaries notified (date/method):
- Missing, minor, or incapacitated beneficiaries:
- Accountings delivered or filed (type/date):
- Objections or concerns raised:

### 10) Remaining Tasks & Forecast

Task | Dependency | Target Date | Risk/Notes | Source
--- | --- | --- | --- | ---
 | | | |

### 11) Open Questions / Missing Docs

- [List each unknown, missing document, or unresolved issue]

## Pitfalls & Checks

- **No legal opinions.** Use neutral, factual language throughout.
- **"As of" qualifiers.** Every amount and date must state its reference date and cite the source.
- **Do not infer deadlines or priority rules.** If not documented, mark `UNKNOWN` and flag as state-specific.
- **Conflicting data.** Only reconcile when the source hierarchy is explicit; otherwise present both values and note the conflict.
- **Redact PII.** Mask SSNs, full account numbers, and other sensitive identifiers.
- **Unverified citations.** Tag with `[VERIFY]`.
- **Jurisdiction terminology.** Use probate terms consistent with the governing state's courts.
