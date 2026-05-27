---
name: change-in-control-agreement
title: Change in Control Agreement
description: Drafts U.S. executive Change in Control Agreements with double-trigger severance, equity acceleration, and 280G/409A compliance. Use when drafting or negotiating CIC agreements, change in control protections, executive severance in M&A, or golden parachute provisions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/change-in-control-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Change in Control Agreement

Drafts a tax-compliant U.S. executive CIC agreement with double-trigger structure, precise statutory definitions, severance benefits, and parachute payment protections.

## Quick Start

Gather before drafting:

1. **Executive** — name, title, base salary, target bonus, outstanding equity (type, vesting, performance metrics)
2. **Company** — legal name, state of incorporation, entity type, public/private status
3. **Existing agreements** — employment agreement, equity plan docs, prior CIC/severance agreements
4. **Deal terms** — severance multiple, protection period, 280G treatment, benefits continuation period
5. **Benchmarking** (if available) — peer agreements, proxy disclosures, comp committee guidelines

## Core Workflow

```
- [ ] Collect executive profile, company info, and existing agreements
- [ ] Define key terms (Change in Control, Cause, Good Reason, Qualifying Termination)
- [ ] Set severance benefits (cash, equity acceleration, COBRA, pro-rated bonus)
- [ ] Configure 280G approach (No Gross-Up / Best Net / Full Gross-Up)
- [ ] Add 409A compliance provisions (separation from service, specified employee delay)
- [ ] Draft release conditions (OWBPA-compliant consideration + revocation periods)
- [ ] Include general provisions (governing law, dispute resolution, successor assignment)
- [ ] Verify all placeholders resolved and cross-references consistent
```

## Article Specifications

### Article I — Definitions

- **Change in Control**: define ownership threshold, merger/consolidation test, and all-or-substantially-all-assets sale test. Include board-turnover test only if needed by the deal context.
- **Cause**: include felony/plea trigger, willful failure after written notice plus cure period, materially injurious conduct, fiduciary-duty breach, and material policy violation with cure where applicable.
- **Good Reason**: include material duty diminution, compensation reduction not broadly applied, and relocation threshold. Include notice/cure/election windows.
- **Qualifying Termination**: without Cause or for Good Reason during the protection period.
- **Protection Period**: usually 12-24 months post-CIC; include pre-CIC tail only if requested.

### Article II — Severance Benefits

- **Cash severance**: set multiple against base salary plus target annual bonus.
- **Pro-rated bonus**: specify target vs actual metric and payment timing.
- **Equity acceleration**: define covered award types and performance-award vesting level.
- **Exercise window**: specify post-termination option/SAR exercise period.
- **Benefits continuation**: define COBRA or equivalent duration and end conditions.
- **Mitigation/offset**: state whether mitigation is required and whether outside earnings offset benefits.

### Article III — Conditions to Benefits

- **Release requirement**: include execution and non-revocation condition with OWBPA-compliant timelines.
- **Release scope and carve-outs**: list included claims and preserved rights.
- **Property return and transition cooperation**: include practical handoff obligations and expense reimbursement terms.

### Article IV — Section 280G/4999

- Select one approach: **No Gross-Up**, **Best Net (cutback)**, or **Full Gross-Up**.
- If cutback applies, define reduction order (for example, cash first, then equity; 409A-covered amounts first).
- Specify independent calculator (accounting firm or tax counsel), allocation process, and finality standard.

### Article V — Section 409A

- Treat each installment/payment as a separate payment for 409A purposes.
- Tie payment triggers to 409A separation-from-service definitions.
- Include specified-employee delay mechanics for applicable public-company executives.
- Include reimbursement timing/non-liquidation guardrails and a compliant savings clause.

### Article VI — General Provisions

- Governing law and venue/dispute-resolution path.
- Successor assumption requirements and assignment limits.
- Supersession hierarchy against prior CIC/severance arrangements.
- Amendment/waiver formalities, severability, notice mechanics, and permitted offset language.

## Key Placeholders

| Placeholder | Market Range |
|---|---|
| `[SEVERANCE MULTIPLE]` | CEO: 2x–3x; C-suite/SVP: 1.5x–2x; other senior: 1x–1.5x |
| `[PROTECTION PERIOD]` | 12–24 months post-CIC |
| `[PRE-CIC TAIL]` | 3–6 months (if included) |
| `[BENEFITS CONTINUATION]` | 12–24 months |
| `[280G APPROACH]` | No Gross-Up / Best Net / Full Gross-Up |
| `[PERFORMANCE VEST LEVEL]` | Target / Maximum / Actual through CIC date |
| `[EXERCISE EXTENSION]` | 12–24 months post-termination |
| `[RELOCATION THRESHOLD]` | 35–50 miles |
| `[GOOD REASON NOTICE]` | 60–90 days; cure 30 days; election 30–60 days |

## Pitfalls

- **Single trigger** — avoid for public companies; ISS/Glass Lewis routinely vote against single-trigger equity acceleration
- **280G modeling** — run parachute calculations before selecting approach; full gross-up is rarely defensible in new agreements
- **409A** — treat each payment as separate; do not rely on short-term deferral exemption for CIC-contingent amounts; use Day-60 payment with two-tax-year rule; apply specified-employee 6-month delay for public company executives
- **OWBPA** — strictly observe 21-day (under 40) or 45/60-day (40+) consideration periods plus 7-day revocation; non-compliance invalidates ADEA release
- **Equity plan override** — confirm acceleration and extended exercise provisions expressly supersede conflicting plan/award terms; some plans require separate committee action
- **Pre-CIC tail** — limit to terminations "at the request of" or "in connection with" the contemplated transaction; avoid overbroad language
- **State law** — CA, NY, and others restrict non-competes; review local WARN, mini-COBRA, and wage payment requirements separately
