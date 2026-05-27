---
name: transfer-agent-agreement
title: Transfer Agent Agreement
description: 'Drafts U.S. transfer agent agreements between issuers and SEC-registered transfer agents covering appointment, stock ledger, transfer processing, Rule 17Ad compliance, fees, termination, and transition. Trigger on: transfer agent agreement, stock ledger, shareholder registry, TA-1, TA-2, 17Ad, appointing or renewing a transfer agent.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/transfer-agent-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
tags: [agreement, corporate, drafting, regulatory, transactional]
---

# Transfer Agent Agreement

Drafts the agreement governing appointment of a transfer agent, services scope, regulatory compliance, fees, and transition mechanics.

## Quick Start

1. Collect party details, securities description, and service scope.
2. Confirm transfer agent SEC registration status.
3. Draft sections per the checklist below.
4. Attach fee schedule and exhibits.

## Prerequisites

1. **Parties**: Issuer and transfer agent legal names, entity types, addresses, SEC registration number, authorized signatories.
2. **Securities**: Class/series, par value, CUSIP, legends, transfer restrictions.
3. **Issuer profile**: Public/private, SEC reporting status, exchange/DTC/FAST/DRS participation, approximate holder count.
4. **Service scope**: Book-entry vs certificated, paying agent duties, corporate action support, escheatment handling.
5. **Transfer rules**: Required documentation, medallion guarantees, legal opinion requirements, stop transfer list authority.
6. **Fees**: Retainer, per-transfer, per-certificate, onboarding, volume tiers, expense caps.
7. **Term**: Duration, renewal, termination notice periods, transition timeline.
8. **Other**: Data security/breach notification, dispute resolution, governing law, exhibits list.

## Section Checklist

| Section | Must Include |
|---|---|
| Parties/Recitals | Appointment basis, securities covered, authority references |
| Definitions | Issuer, Transfer Agent, Securities, Records, Authorized Representatives |
| Appointment | Exclusive/non-exclusive, scope, future issuances |
| Services | Stock ledger, transfers, certificates/book-entry, replacement, corporate actions |
| Compliance | SEC transfer agent rules [VERIFY], recordkeeping, safeguarding funds/securities |
| Transfer Restrictions | Legend removal process, legal opinion requirements, stop transfer list |
| Fees/Expenses | Fee schedule reference, billing cycle, expense approvals, fee adjustment mechanism |
| Term/Termination | Length, renewal, convenience, breach, regulatory loss, insolvency |
| Transition | Data delivery format, cooperation period, continuation services, return of property |
| Reps/Covenants | Authority, good standing, registration maintenance, system capability, insurance |
| Indemnity/Liability | Mutual indemnities, carve-outs for gross negligence/willful misconduct, cap, damages exclusion |
| Confidentiality | Definition, use limits, permitted disclosures, survival |
| Data Security | Safeguards, breach notice timing, subcontractor controls |
| Disputes | Governing law, venue/arbitration, fee shifting |
| Miscellaneous | Notices, assignment, force majeure, counterparts, survival |
| Exhibits | Fee schedule, SLAs, forms, authorized signers list |

## Transfer Processing Checklist

- Confirm authorized signers list and instruction channel.
- Require medallion signature guarantee for certificated transfers.
- Define acceptable legal opinions for legend removal.
- Maintain and honor stop transfer list.
- Set rejection notice timing, cure path, and routine transfer turnaround.

## Key Clauses

**Appointment.** Issuer appoints Transfer Agent as [exclusive/non-exclusive] transfer agent and registrar for the Securities. Transfer Agent accepts and will perform the Services in accordance with applicable law and this Agreement.

**Transfer Restrictions.** Transfer Agent will refuse any transfer that violates applicable securities laws, contractual restrictions, or Issuer instructions. Legend removal requires (a) Issuer written authorization and (b) legal opinion from counsel reasonably acceptable to Issuer, unless Issuer waives in writing.

**Transition Assistance.** Upon termination, Transfer Agent will deliver complete Records in a mutually agreed electronic format and provide transition services for [30/60] days. Issuer will pay all undisputed fees and reasonable transition expenses.

## Fee Schedule Template

| Item | Amount |
|---|---|
| Retainer | $[amount] per [month/year] |
| Per-transfer | $[amount] per transfer |
| Per-certificate issue | $[amount] |
| Replacement certificate | $[amount] |
| Onboarding/Conversion | $[amount] (one-time) |
| Expenses | At cost; pre-approval above $[threshold] |
| Billing | [monthly/quarterly], net [30] days |

## Guidelines

- Require covenant to maintain SEC registration; loss of registration triggers termination.
- Specify exclusive vs non-exclusive appointment and whether future issuances are covered.
- Match transfer restriction mechanics to issuer's actual legends and lockups — avoid generic language.
- Align recordkeeping duties with issuer's state corporate law stock ledger requirements.
- Keep indemnities mutual; exclude gross negligence and willful misconduct from indemnification.
- Cap liability only with carve-outs for confidentiality breaches, data breaches, and willful misconduct.
- **Public/DTC issuers**: Address DTC/FAST/DRS interfaces and corporate action timelines.
- **Private issuers**: Emphasize consent rights, ROFR/ROFO procedures, issuer approval steps.
- Use [VERIFY] on uncertain rule citations; confirm current SEC transfer agent rules before finalizing.
- Do not draft legal opinions — only specify when required and acceptable form.

## Troubleshooting

- **Missing SEC registration number**: Do not proceed without confirming registration on SEC EDGAR; flag with [VERIFY].
- **Unclear exclusivity**: Default to exclusive unless issuer confirms otherwise — non-exclusive appointments require additional coordination clauses.
- **Generic legend language**: Always request issuer's actual certificate legends and restriction agreements rather than using boilerplate.
- **Fee schedule gaps**: If fee details are incomplete, insert placeholders and flag each as [TO BE CONFIRMED] for client review.

---
