---
name: atm-equity-distribution-agreement
title: ATM Equity Distribution Agreement
description: Drafts a market-standard At-The-Market (ATM) Equity Distribution Agreement for public issuers conducting continuous shelf offerings under Rule 415(a)(4). Use when establishing or renewing an ATM program under an effective Form S-3, drafting a sales agent agreement, or structuring a continuous equity offering program.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/atm-equity-distribution-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: capital-markets
language: en
tags: [agreement, corporate, drafting]
---

# ATM Equity Distribution Agreement

Generates an Equity Distribution Agreement for an ATM offering program compliant with Rule 415(a)(4), Regulation M, and applicable exchange listing rules.

## Prerequisites

Collect before drafting:

1. **Issuer** — legal name, state of incorporation, principal office
2. **Registration statement** — Form S-3 file number, effective date, maximum aggregate offering amount
3. **Securities** — class, par value, proposed ATM program maximum (must not exceed shelf availability)
4. **Agent(s)** — legal name(s), FINRA registration status, commission rate (market: 2–3%)
5. **Exchange** — principal listing market (NYSE/Nasdaq); 20%-cap shareholder approval status
6. **Existing arrangements** — prior ATM agreements, lock-ups, co-manager arrangements

## Document Structure

| Section | Key Contents |
|---|---|
| Parties & Recitals | Party names; shelf registration citation; Rule 415(a)(4) characterization |
| Definitions | Shares, Placement Notice, Floor Price, Commission, Applicable Time, VWAP, Issuance Cap, Suspension Notice |
| Agency Appointment | Non-exclusive; commercially reasonable efforts; not an underwriter; sub-agent consent |
| Sale Mechanics | Placement notice process; volume caps; daily confirmations; T+2 settlement; DTC delivery |
| Compensation | Commission % of gross proceeds; expense allocation; wire instructions |
| Reps & Warranties | Corporate, registration/disclosure, capitalization, financial, compliance, litigation |
| Issuer Covenants | Registration maintenance, reporting, notification, blackouts, due diligence access, ongoing deliverables |
| Indemnification | Mutual indemnification; defense procedures; contribution (cap = commissions received) |
| Conditions Precedent | Initial closing deliverables; per-placement conditions |
| Termination | Mutual notice; immediate triggers; automatic events; post-termination obligations |
| General Provisions | NY/DE governing law; jury waiver; notices; integration; severability; confidentiality |

## Sale Mechanics

**Placement Notice** — Issuer delivers written notice specifying max shares, floor price, and sales period. Agent sells on commercially reasonable efforts basis and provides daily confirmations (shares sold, gross/net proceeds, VWAP).

**Volume Limits** — Daily cap typically ≤ 25% of average daily trading volume. Program cap must not exceed shelf availability; track against exchange listing limits.

**Settlement** — T+2 via DTC through issuer's transfer agent.

**Mandatory Suspension Triggers:**
- Issuer possesses undisclosed MNPI
- Quarterly earnings blackout
- Registration statement not effective or stop order in effect/threatened
- Exchange trading halt

## Representations & Warranties

**Corporate** — Duly organized; full authority; agreement enforceable (subject to bankruptcy/equity carve-outs); no conflicts; no outstanding consents.

**Registration & Disclosure** — Registration statement effective, no stop order; compliant with Securities Act; no material misstatement/omission (10b-5 standard); Exchange Act filings current.

**Capitalization** — Accurate share counts; shares when issued will be validly issued, fully paid, non-assessable; no undisclosed preemptive rights; options/warrants/convertibles disclosed.

**Financial** — Financials present fairly per GAAP; no undisclosed MAC since most recent financials.

**Compliance & Litigation** — Material permits held; no undisclosed proceedings with potential MAE.

## Issuer Covenants

- Maintain registration statement effectiveness; provide agent advance copies of amendments
- Furnish all Exchange Act filings and material communications
- Immediately notify agent of any event causing prospectus misstatement/omission
- Suspend sales during MNPI possession and earnings blackouts
- Provide reasonable due diligence access
- Deliver quarterly (and on request): officer's certificate (CEO + CFO), counsel opinion, negative assurance letter, auditor comfort letter

## Indemnification & Contribution

- **Issuer → Agent**: Losses from misstatement/omission in registration statement, prospectus, or supplements (except agent-furnished information)
- **Agent → Issuer**: Losses from agent-furnished written information only
- **Defense**: Prompt notice; indemnitor may assume defense; no settlement without consent unless unconditional release with no fault admission
- **Contribution**: When indemnification unavailable; allocated by relative benefit and fault; agent cap = total commissions received

## Conditions Precedent

**Initial Closing** — Executed agreement; counsel opinion; negative assurance letter; comfort letter; officer's certificate; exchange listing approval; registration statement confirmed effective.

**Per-Placement** — Reps true in all material respects; covenants performed; no stop order; no MAC; shares not suspended/delisted; updated opinions and comfort letters as required.

## Termination

| Type | Terms |
|---|---|
| Mutual notice | 5–10 business days (allows pending transaction wind-down) |
| Agent immediate | Trading suspension; stop order; issuer MAC; material breach; market disruption |
| Automatic | All shares sold; registration expires; delisting; bankruptcy |
| Post-termination | Settle pending trades; pay commissions; final reconciliation; indemnification survives |

## Pitfalls & Verification

- **Rule 415(a)(4)**: Confirm all sales qualify as at-the-market (existing trading market, not fixed price); verify block transaction provisions preserve this characterization
- **Regulation M**: Address agent market activity restrictions during distribution periods [VERIFY current SEC guidance]
- **Exchange 20% Cap**: Confirm shareholder approval status (NYSE § 312 / Nasdaq Rule 5635) [VERIFY current rule text]
- **Form S-3 Eligibility**: Public float ≥ $75M; Baby Shelf Rule limits issuers with float < $75M to 1/3 of float per 12 months [VERIFY]
- **No Underwriter Characterization**: Agent must act on commercially reasonable efforts basis throughout — avoid Securities Act § 11 underwriter liability
- **Shelf Tracking**: Include mechanism to track shares sold against program maximum and remaining availability
- **FINRA**: Confirm registered broker-dealer status; Rule 5110 filing requirements may apply [VERIFY]
- **Concurrent Programs**: Track aggregate issuances across all ATM and equity programs against exchange caps
- **Governing Law**: Default NY; consider DE if charter-related issues are central
- **Survival**: Indemnification must expressly survive termination (statute of limitations period recommended)
