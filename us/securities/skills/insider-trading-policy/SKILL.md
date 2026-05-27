---
name: insider-trading-policy
title: Insider Trading Policy
description: 'Drafts a U.S. financial-services insider trading policy covering MNPI definitions, preclearance, blackout windows, 10b5-1 plan governance, restricted/watch lists, reporting, and enforcement. Use when creating or updating insider trading policies for broker-dealers, investment advisers, or investment companies. Triggers: insider trading policy, 10b5-1 plan, preclearance, restricted list, blackout period, Reg FD, MNPI.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/insider-trading-policy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
---

# Insider Trading Policy

Draft a firm-ready insider trading policy that is enforceable, auditable, and practical for employees.

## Quick Start

Gather before drafting:

1. Firm name, entity structure, regulatory status (BD, IA, IC, bank affiliate)
2. Business lines with MNPI access (IB, research, trading, PM, corporate access, lending)
3. Whether firm/parent is a public issuer and earnings cadence
4. Employee trading systems, preclearance workflows, restricted/watch list practices
5. Personal trading exceptions, OBA/board service approval process
6. Compliance contacts, hotline, and non-retaliation policy text

## Core Workflow

1. Populate variables and confirm applicable regulatory add-ons
2. Verify legal authorities and insert accurate citations
3. Draft sections in order below using defined terms consistently
4. Tailor controls to firm systems and risk profile
5. Add appendices for forms and quick reference

## Variables

```
firm_name:
effective_date:
version:
policy_owner_title:
policy_owner_contact:
public_cooldown_days: 2
blackout_start_days_before_q_end: 14
blackout_end_days_after_earnings: 2
preclearance_lead_time_days: 1
holding_period_days: 60
cooling_off_days_officer_director: [VERIFY]
cooling_off_days_other: [VERIFY]
```

## Authorities to Validate

| Authority | Applies to | Purpose |
|---|---|---|
| Exchange Act §10(b) / Rule 10b-5 [VERIFY] | All | Anti-fraud, insider trading prohibition |
| Rule 10b5-1 [VERIFY] | All | Affirmative defense, plan requirements |
| Regulation FD [VERIFY] | Issuers | Selective disclosure restrictions |
| Advisers Act Rule 204A-1 [VERIFY] | IAs | Code of ethics, personal trading |
| IC Act Rule 17j-1 [VERIFY] | ICs | Code of ethics, reporting |
| FINRA OBA/PST/outside accounts rules [VERIFY] | BDs | Supervisory procedures |

## Policy Sections

| # | Section | Required Content |
|---|---|---|
| 1 | Purpose and Scope | Covered persons/securities; possession standard; extraterritorial; personal/joint/trust/managed accounts |
| 2 | Definitions | MNPI, Material, Nonpublic, Public dissemination, Tipping, Beneficial ownership, Covered person |
| 3 | Core Prohibitions | No trading on MNPI; no tipping; no recommending/inducing; no third-party circumvention |
| 4 | Information Barriers | Physical/system controls; access logs; cross-wall bans; monitoring |
| 5 | Wall Crossing | Pre-approval; written notice; acknowledgment; trading freeze; documentation |
| 6 | Restricted List | Criteria; trading/research bans; additions/removals; distribution |
| 7 | Watch List | Monitoring scope; escalation triggers; no safe harbor |
| 8 | Preclearance | Who must preclear; request data; approval window; denial grounds; execution confirmation |
| 9 | Blackout Periods | If issuer: subject persons; timing; exceptions; earnings releases |
| 10 | 10b5-1 Plans | Eligibility; approval; cooling-off; modifications; overlapping plans; certifications |
| 11 | Personal Trading | Short sales, derivatives, margin, holding periods, speculative bans |
| 12 | Reporting | Initial holdings; quarterly transactions; annual certifications; duplicate statements |
| 13 | Outside Activities | Board service approval; conflicts; external MNPI reporting |
| 14 | Training | Annual; role-based frequency; case studies |
| 15 | Enforcement | Discipline range; zero-tolerance for intentional misconduct; regulator cooperation |
| 16 | Reporting and Non-Retaliation | Hotline; escalation; confidentiality; non-retaliation |
| 17 | Administration | Policy owner; amendments; annual review; version control |

## Key Definitions

| Term | Standard |
|---|---|
| Material | Reasonable investor would consider important or likely to affect price |
| Nonpublic | Not broadly disseminated; requires absorption period of `public_cooldown_days` |
| MNPI | Material and nonpublic information from any source |
| Possession standard | Trading while aware of MNPI prohibited regardless of use |
| Tipping | Disclosing MNPI outside authorized channels |
| Covered securities | Equity, debt, options, swaps, derivatives, ADRs, linked instruments |
| Covered persons | Employees, officers, directors, interns, contractors, consultants, temps |

## Core Prohibitions

- No trading in covered securities while in possession of MNPI
- No tipping MNPI outside authorized channels
- No recommendations or inducement to trade while possessing MNPI
- No evasion via third-party or managed accounts

## Controls Checklist

- [ ] Information barriers with access controls and audits
- [ ] Wall crossing protocol with compliance approval and written acknowledgments
- [ ] Restricted/watch list governance with documented criteria
- [ ] Preclearance with same-day execution limits
- [ ] Blackout periods for issuer securities (if applicable)
- [ ] 10b5-1 plan governance and monitoring
- [ ] Personal trading limits: short sales, derivatives, margin, holding periods
- [ ] Reporting: initial, quarterly, annual, plus duplicate confirmations
- [ ] Training, certification, and enforcement

## Template Blocks

**Policy Header**

```
Title: Insider Trading Policy
Effective Date: {effective_date} | Version: {version}
Owner: {policy_owner_title} | Contact: {policy_owner_contact}
```

**Preclearance Request** (minimum fields): employee name/role, security name/ticker/CUSIP, transaction type/quantity, account/broker, proposed trade date, reason.

**Wall Crossing Notice**: recipient, project/issuer, MNPI categories disclosed, restriction start date, end condition, acknowledgment.

**Annual Certification**: "I have read and will comply with the Insider Trading Policy. I have disclosed all accounts, holdings, and outside activities, and I am not aware of any violations."

## Pitfalls

- Do not claim `public_cooldown_days` is a legal requirement — it is firm policy
- If firm is not a public issuer, omit Reg FD and blackout sections
- Mark unverified citations with `[VERIFY]`; never present them as confirmed
- Align with adviser or IC code-of-ethics rules when applicable
- Include jurisdiction-specific addenda for non-US personnel/markets
- Route all policy exceptions through Compliance with documented approval

---

Key changes from the original:

- **Removed `tags`** — not part of the Agent Skills spec (only `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` are valid)
- **Restructured body** into Quick Start / Core Workflow / reference tables / Pitfalls pattern
- **Renamed "Prerequisites"** to "Quick Start" and "Guidelines" to "Pitfalls" for clarity
- **Compressed template blocks** — Preclearance Request, Wall Crossing Notice, and Annual Certification collapsed from multi-line code blocks to inline descriptions (saves ~30 lines)
- **Compressed Policy Header** template from 5 lines to 3
- **Tightened table cells** throughout — semicolons replace verbose phrases, abbreviations (BD, IA, IC, PM) used consistently
- **Removed the duplicate "(Financial Services)" subtitle** — redundant with description
- **Removed redundant "Output Structure / Process" heading** — merged into "Core Workflow"
- **Line count reduced** from 161 to ~120, well under the 500-line target
