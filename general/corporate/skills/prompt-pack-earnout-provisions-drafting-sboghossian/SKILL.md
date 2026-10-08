---
name: prompt-pack-earnout-provisions-drafting-sboghossian
title: Earnout Provisions Drafting
description: Use when drafting earnout provisions for an M&A agreement — covering performance metrics, measurement periods, accounting principles, operating covenants, adjustment mechanisms, and dispute resolution procedures. Earnouts bridge valuation gaps between buyer and seller and are common in technology, healthcare, and services deals. Applies across jurisdictions with particular attention to MENA (UAE, KSA, DIFC, ADGM), UK, EU, and US deals. Trigger when the acquisition agreement needs post-closing contingent consideration provisions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-earnout-provisions-drafting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Earnout Provisions Drafting

## When to use this

Use this skill when drafting the earnout section of an M&A agreement (SPA, APA, or merger agreement). Earnouts allow part of the purchase price to be contingent on the target's post-closing performance, bridging the valuation gap when buyer and seller disagree on what the business is worth. They are common in:

- Technology acquisitions (key metric: ARR, MRR, or active users)
- Healthcare and pharma (key metric: regulatory approval milestones, revenue)
- Professional services (key metric: revenue retention from key clients)
- Startups and growth companies with forward-looking valuations

Earnouts are also among the most litigated provisions in M&A — the drafting must be precise.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Maximum earnout amount | The ceiling of contingent consideration | Ask |
| Earnout metrics | Revenue, EBITDA, gross profit, ARR, milestone-based — must be defined precisely | Ask in detail |
| Measurement period(s) | Annual, quarterly, multi-year — and the exact start/end dates | Ask |
| Accounting principles | IFRS, US GAAP, local GAAP — and which party's auditors apply | Ask |
| Operating covenant obligations on buyer post-closing | What the buyer must/must not do to avoid manipulating the earnout | Critical; ask |
| Dispute resolution mechanism for earnout disputes | Accountant expert, arbitration, courts | Ask |

## Optional inputs

- Earnout structure: cumulative vs. independent annual periods
- Catch-up provisions (shortfall in Year 1 can be made up in Year 2)
- Accelerated earnout triggers (change of control post-closing; seller's termination)
- Anti-embarrassment provisions (if buyer sells target within earnout period at a higher multiple, seller shares in excess value)
- Equity vs. cash payment of earnout
- Treatment of earnout on death or incapacity of the seller key person

## Document structure

### 1. Definitions

Define every term used in the earnout provisions with precision:
- **Earnout Consideration**: the contingent payment, expressed as a formula (e.g., 2x the amount by which EBITDA exceeds USD X)
- **Earnout Period**: specific start and end dates; fiscal year or calendar year
- **Earnout Metrics**: define the specific financial or operational metrics
  - If revenue: gross or net? exclude which items (returns, taxes, intercompany)?
  - If EBITDA: define adjustments (management fees, extraordinary items, buyer's shared services allocation?)
  - If ARR: which contracts qualify? minimum contract value? annual contracts only or monthly normalized?
- **Accounting Principles**: IFRS or US GAAP; consistently applied by whom; define what "consistently applied" means
- **Earnout Statement**: the document the buyer prepares at end of each period

### 2. Earnout Calculation

Specify the formula:

> "The Earnout Consideration for each Earnout Year shall be an amount equal to [formula], provided that the total Earnout Consideration payable in respect of all Earnout Years shall not exceed [maximum amount]."

- Tiered earnouts: "25% payable if EBITDA exceeds X; 50% if EBITDA exceeds Y; 100% if EBITDA exceeds Z"
- Binary milestone earnouts: "USD X payable on achievement of [regulatory approval / customer contract signature / product launch]"
- Hybrid: financial threshold + strategic milestone

### 3. Earnout Statement Process

1. Buyer prepares and delivers the Earnout Statement within [30–60] days after end of each Earnout Period
2. Statement must include the calculation in sufficient detail for the Seller to verify
3. Seller has [20–30] days to review; may deliver a Notice of Disagreement specifying items disputed
4. Parties negotiate resolution for [15–20] days after Notice of Disagreement
5. Unresolved disputes referred to an Independent Accountant (not buyer's or seller's auditors); decision is final and binding
6. Costs of Independent Accountant: borne by the party whose position is further from the final determination (or split equally)

### 4. Payment

- Payment due within [10–20] business days after Earnout Statement becomes final
- Set-off: buyer may set off against earnout only against finally determined (not disputed) indemnity claims
- Interest on late payment: [rate] from due date

### 5. Operating Covenants (Critical)

The most heavily negotiated section — the buyer's obligations to avoid "sandbagging" the earnout:

**Buyer must**:
- Operate the target in the ordinary course of business consistent with pre-closing practice
- Fund the business with adequate working capital
- Not divert revenue-generating opportunities away from the target
- Maintain the target's separate legal existence (if applicable)
- Not impose management fees, royalties, or charges on the target that reduce the earnout metric

**Buyer must not**:
- Merge the target into another group entity in a way that makes the earnout metric unmeasurable
- Materially change the accounting policies applied to the target without consent
- Change the target's fiscal year end
- Reduce pricing of target's products/services in a way that depresses the earnout metric

**Seller may request**:
- Periodic reporting rights (quarterly management accounts)
- Observer rights on the target's board during the earnout period
- Dispute rights if buyer takes actions that materially affect the earnout

### 6. Acceleration Events

Define circumstances in which the full earnout accelerates and becomes payable immediately:
- Buyer undergoes a change of control post-closing
- Buyer terminates the seller's employment or services agreement (if seller is also an employee) without cause
- Buyer materially breaches the operating covenant obligations
- Target is sold, wound up, or merged during the earnout period

### 7. Dispute Resolution

- Accountant expert determination is preferred for financial metric disputes (fast, binding, cost-efficient)
- Milestone disputes (was the milestone achieved?) may go to arbitration
- Specify the expert appointment mechanism: agreed list, or nominated by [ICAEW President / AICPA] if parties cannot agree within [10] days

## Jurisdictional notes

### Civil-law jurisdictions (UAE onshore, KSA, Lebanon, Egypt)

Civil-law courts may characterize earnout obligations as conditional obligations or contingent debts. Key considerations:
- The condition must be possible, legal, and clearly defined — vague metrics will not be enforced
- Court-appointed experts in civil-law systems may not apply the same accounting precision as Big-4 independent accountants in common-law systems; contract for independent accountant determination
- Penalty clause rules: in most MENA civil-law jurisdictions, courts can reduce penalties and damages to equitable levels; earnout provisions are not penalties but are sometimes treated analogously; use precise formula rather than penalty language

### DIFC / ADGM / UK (common law)

- Earnout obligations are enforceable as contractual debt obligations
- Operating covenants will be interpreted strictly; buyer must not take "unreasonable steps" to prevent earnout achievement (implied duty of good faith in DIFC law)
- Expert determination clauses are final and binding unless manifestly wrong (high bar to challenge)

### US

- Delaware courts apply strict construction to earnout provisions; ambiguity in metrics has historically been resolved against the party that drafted the contract
- Operating covenant disputes are a major source of post-closing M&A litigation
- Consider using financial metrics defined by reference to GAAP rather than IFRS for US deals

## Common mistakes

- **Vague metric definitions**: "Revenue" without defining inclusions/exclusions leads to the most earnout disputes. Every dollar in or out of the metric must be explicitly addressed.
- **No accounting principles specification**: If the buyer changes from IFRS to US GAAP post-closing, the earnout metric changes; pin down the exact accounting framework.
- **Insufficient operating covenants**: Buyers who divert business opportunities or charge management fees without covenants face no contractual liability; sellers need robust protections.
- **Set-off risk**: Allowing set-off against earnout for any disputed indemnity claim gives buyer an incentive to manufacture or over-claim indemnity claims to avoid paying the earnout.
- **No acceleration on buyer's change of control**: If the buyer is acquired post-closing, the earnout obligation may be assignable and the new owner may have no interest in achieving it.

## Related skills

- [[prompt-pack-disclosure-letter]]
- [[prompt-pack-escrow-agreement]]
- [[prompt-pack-due-diligence-report]]
- [[prompt-pack-investment-agreement-venture-capital]]
