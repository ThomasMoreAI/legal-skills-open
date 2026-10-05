---
name: commercial-lease-analyzer-onewave-ai
title: Commercial Lease Analyzer
description: Decode a commercial lease before signing or renewing -- true all-in occupancy cost (base rent plus NNN/CAM plus escalations), the clauses that hurt small tenants (personal guarantees, relocation, restoration), and the negotiation asks landlords routinely grant. The lease is most SMBs' biggest fixed cost and least-read document.
author: OneWave-AI
author_url: https://github.com/OneWave-AI/claude-skills/tree/main/commercial-lease-analyzer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Commercial Lease Analyzer

Commercial leases are written by landlords' attorneys for landlords, and small tenants sign them unread because the rent number looked fine. Read the whole thing, price the whole thing, and arm the tenant for the negotiation. Input: the lease or letter of intent (PDF/.docx), plus the renewal notice if that is the trigger. Analysis support for the tenant's decision and their attorney's review -- not legal advice.

## Workflow

1. **Price the true occupancy cost.** Base rent is the teaser; build the real number: NNN/CAM charges (taxes, insurance, common-area maintenance -- and whether CAM has a cap or is uncontrolled), escalations applied year by year (fixed %, CPI, or stepped), utilities responsibility, percentage rent if retail, and the amortized cost of any tenant-improvement obligations. Output the year-by-year total and the effective rate per square foot -- compare THAT to the market, not the base rent.
2. **Extract the clock terms.** Term, renewal options (and their pricing: fixed, capped, or "market rate" -- the last is a blank check without an arbitration mechanism), notice windows for renewal/termination, and holdover penalties. Feed the dates to `cowork-contract-renewal-radar` so the notice deadline never ambushes.
3. **Hunt the small-tenant traps,** quoting each clause verbatim with location: personal guarantee scope (full-term vs. burn-down as the business proves itself), relocation clause (landlord can move you -- who pays, and does the space have to be comparable), restoration/surrender obligations (returning the space to shell condition can cost tens of thousands), assignment/sublet restrictions (can you sell the business without landlord consent), exclusive-use absence (nothing stops the landlord leasing to your competitor next door), CAM audit rights (can you verify the charges), operating covenants, and default/cure windows.
4. **Grade and compare.** Each finding rated tenant-favorable / market-standard / landlord-favorable / red flag. If comparing spaces or renewal-vs-move, run steps 1-3 per option and lay the true costs and trap lists side by side, including moving and buildout costs in the move scenario.
5. **Build the ask list.** The negotiation memo: what to request ranked by value and by how routinely landlords grant it -- guarantee burn-down, CAM cap, renewal-rate cap or arbitration, restoration limited to alterations, exclusive-use for the tenant's category, free-rent months, TI allowance -- each with the specific clause edit it implies, ready for the attorney and the broker.

## Rules

- The effective all-in cost per year is the headline number of every analysis; base rent alone never gets quoted as "the cost."
- Verbatim quotes with section numbers for every flagged clause -- paraphrased lease analysis is how traps survive review.
- "Market rate" renewal language without a determination mechanism is always flagged; it is the most expensive vague phrase in small-business contracts.
- Silence is a finding: no exclusive-use, no CAM cap, and no cure period are reported as prominently as bad clauses.
- The math shows its work: escalation compounding and CAM estimates are shown year by year, with assumptions labeled.
- Attorney framing is built into the deliverable -- the ask list is prep for counsel and broker, not a substitute for them.

## Quick Commands

- "Analyze [lease]" -- full workflow
- "What will this space really cost?" -- step 1 only
- "Renewal vs. move: [lease] vs [new LOI]" -- side-by-side comparison
- "What do I ask for?" -- the negotiation memo
