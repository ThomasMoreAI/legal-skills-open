---
name: draft-sow-extension-sboghossian
title: Draft — SOW Variants
description: Use when drafting a variant of a standard Statement of Work — specifically a time-and-materials SOW, a fixed-fee SOW, an outcome-based (KPI-tied) SOW, or a hybrid fee structure. Builds on the base SOW framework with variant-specific clauses for fee mechanics, cap provisions, KPI definitions, and mixed-fee allocation. Use alongside the base draft-sow skill; this skill provides the variant-specific additions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-sow-extension
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Draft — SOW Variants

This skill provides the fee-structure-specific provisions to be used within or alongside the base [[draft-sow]] framework. Each variant has different risk allocation between Client and Provider, and each requires different drafting discipline to avoid disputes.

## When to use this

- When the parties have chosen a fee structure other than a simple lump sum
- When an AFA (Alternative Fee Arrangement) is being implemented (see also [[efirm-finance-afa-quote-builder]])
- When the base [[draft-sow]] template needs adaptation for a specific fee model

## Variant 1 — Time-and-Materials (T&M) SOW

### When to use T&M
T&M is appropriate when scope is not fully defined at the start, when the Client needs flexibility to redirect work, or when the engagement involves research and exploratory work (due diligence, litigation strategy, open-ended consulting).

### Fee clause for T&M
```
Fees: Provider will invoice Client monthly based on actual hours worked by
role, at the following rates:
  [Role]      [Rate per hour]
  [Role]      [Rate per hour]

All time entries recorded in increments of [0.1 hour / 15 minutes].
Expenses: reimbursed at cost with prior approval for amounts exceeding [X].

Estimate: Provider estimates the total fees under this SOW will be
approximately [low] to [high]. Provider will notify Client in writing when
80% of the upper estimate has been consumed; no additional fees will be
incurred above [hard cap] without Client's written authorization.
```

### Critical T&M provisions
- **Monthly cap**: set a per-month hard cap even if the total is uncapped; prevents surprise invoices
- **80% notice obligation**: Provider must warn Client before consuming the full budget — without this, the Client receives an invoice for double the estimate
- **Activity reporting**: T&M invoices must include a time log (date, timekeeper, description, hours); vague entries (e.g., "review file — 3.0 hours") are grounds for challenge
- **Change directive**: Client may redirect scope in a T&M SOW by written direction; redirect does not require a formal Change Order (unlike fixed-fee where any change is a Change Order)

---

## Variant 2 — Fixed-Fee SOW

### When to use fixed fee
Fixed fee is appropriate when scope is tightly defined, deliverables are clear, and the Provider can price the risk of scope. It transfers scope-risk to the Provider (if it takes longer, they absorb it) and budget-risk to the Client (they know exactly what they're paying, but scope is tightly controlled).

### Fee clause for fixed fee
```
Fees: Provider will perform all services under this SOW for a fixed fee
of [Amount] ("Fixed Fee"), invoiced as follows:

  Milestone         Amount     Invoice trigger
  ─────────────     ──────     ──────────────────────────
  [Milestone 1]     [X]%       Delivery of [deliverable D1]
  [Milestone 2]     [X]%       Client acceptance of [D2]
  [Final]           [X]%       Final delivery and go-live

The Fixed Fee is inclusive of all costs except: [list exclusions —
third-party fees, travel if applicable].
```

### Critical fixed-fee provisions
- **Change Order process**: any change to scope requires a written Change Order signed by both parties before additional work commences; Provider is not obligated to perform out-of-scope work
- **Assumed inputs**: list the Client inputs and assumptions on which the Fixed Fee is based (if a key assumption is wrong, the Fixed Fee may be adjusted)
- **Scope creep protection**: include a "change control" clause — if Client requests work outside the SOW scope, Provider provides an estimate, parties agree on the Change Order, then work proceeds; no informal verbal directives
- **Completion definition**: define "completion" precisely — it is when the deliverables are accepted, not when the Provider considers the work done

### Change Order template (for fixed-fee SOW)
```
CHANGE ORDER NO. [X] to SOW No. [Y]

Description of change: [precise description of additional work]
Reason for change: [Client-initiated scope expansion / corrected assumption]
Impact on timeline: [extend milestone M3 by X days]
Additional fee: [Amount] (or credit [Amount] if scope is reduced)
Payment: invoiced on [completion of changed deliverable / milestone trigger]

Agreed and signed: [Provider] [Client] [Date]
```

---

## Variant 3 — Outcome-Based / KPI-Tied SOW

### When to use outcome-based
Outcome-based fees tie payment to the achievement of measurable results — cost savings achieved, deals closed, regulatory approvals obtained, number of successfully completed transactions. Common in management consulting, litigation (contingency), and legal process outsourcing where Client wants aligned incentives.

### Fee clause for outcome-based
```
Fees: Provider's compensation under this SOW is tied to the following
Key Performance Indicators ("KPIs"):

  KPI                     Measurement        Target      Fee at target
  ─────────────────────   ──────────────     ─────────   ─────────────
  [KPI 1 — e.g., cost     Difference         [X]% cost   [Amount / %]
   savings on contracts]   between            reduction
                           pre- and
                           post-negotiation
                           contract values

  [KPI 2]                 [Method]           [Target]    [Fee]

Measurement: KPIs will be calculated by [agreed methodology] within
[30] days of [trigger event / period end].
Disputes on KPI calculation: [dispute resolution mechanism — expert
determination is recommended].
```

### Critical outcome-based provisions
- **KPI definition precision**: ambiguous KPIs are litigated, not paid; define every variable in the formula (what counts as a "contract," what is the comparison baseline, what is included and excluded)
- **Anti-manipulation covenant**: Client shall not take actions designed to artificially depress KPI performance (e.g., redirecting work away from Provider during the measurement period)
- **Audit rights**: Provider should have the right to audit Client's records to verify KPI calculation; Client should have the right to audit Provider's methodology
- **Minimum base fee**: consider a small base fee to cover Provider's costs during the engagement, even if KPI targets are not met; pure contingency with no base fee may be prohibited in some jurisdictions (e.g., Lebanon: contingency as sole compensation is not permitted for lawyers)
- **Cap on outcome fee**: set a cap on the total outcome fee to limit windfall scenarios

### Jurisdiction notes for outcome-based fees
| Jurisdiction | Rule |
|---|---|
| Lebanon | Contingency as the sole fee is not permitted for lawyers; honoraires de résultat (success bonus on top of base) is permitted |
| France | Pacte de quota litis (agreement on contingency as sole fee) is prohibited; success bonus on top of base (honoraires de résultat) is permitted |
| KSA | Contingency fees for lawyers are permitted subject to a reasonableness standard; court can adjust |
| UAE | Contingency fees for lawyers are permitted; courts can adjust |
| UK | Conditional Fee Agreements (CFAs) and Damages-Based Agreements (DBAs) are regulated |
| US | Contingency fees common in personal injury, employment; state-by-state regulations apply |

---

## Variant 4 — Hybrid SOW (Fixed Base + Variable Outcome)

### When to use hybrid
The hybrid structure provides a fixed base fee covering the Provider's cost floor and a variable component tied to outcomes. This balances the Provider's need for cost certainty with the Client's desire for performance alignment.

### Fee clause for hybrid
```
Fees: Provider's compensation under this SOW consists of:

(a) Base Fee: [Amount], invoiced [on milestone triggers per the table
    in Section 4]; and

(b) Performance Fee: up to [Amount / X%] of [defined outcome base],
    calculated as follows: [formula]; measurement as set out in the
    KPI schedule attached as Schedule [X].

Total maximum fee: [Base Fee + maximum Performance Fee cap] = [Amount].
```

---

## Comparing the Variants

| Dimension | T&M | Fixed fee | Outcome-based | Hybrid |
|---|---|---|---|---|
| Who bears scope risk | Client | Provider | Shared | Shared |
| Who bears execution risk | Client | Provider | Provider | Provider |
| Budget certainty for Client | Low | High | Moderate (if base + cap) | High (if capped) |
| Alignment of incentives | Low | Moderate | High | High |
| Administrative burden | High (time tracking) | Low (milestone tracking) | High (KPI measurement) | Medium |
| Appropriate when | Scope undefined | Scope tight | Outcomes measurable | Both parties want alignment with cost floor |

## Related skills

- [[draft-sow]]
- [[draft-msa]]
- [[draft-sla]]
- [[efirm-finance-afa-quote-builder]]
