---
name: draft-founders-agreement-sboghossian
title: Founders' Agreement
description: Use when drafting a founders' agreement covering equity, vesting, IP, roles, and exit mechanics between co-founders before or at incorporation. P0 corporate skill covering reverse vesting (4-year/1-year cliff), good-leaver/bad-leaver definitions, IP assignment retroactive to pre-incorporation work, reserved matters, drag-along/tag-along thresholds, buy-sell for deadlock, and governing law. Pairs with draft-shareholders-agreement for investor rounds.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-founders-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Founders' Agreement

## When to use this

A founders' agreement is the governing document for the relationship between co-founders of a company — before institutional investors arrive. It covers who owns what, under what conditions, and what happens when a founder leaves.

Use this skill when:
- Two or more founders are starting a company and need to document their equity split, roles, and departure terms before incorporating.
- A recently incorporated company has not yet adopted a formal founders' agreement and needs to regularize the cap table.
- A founder is departing and the team needs to apply the good-leaver/bad-leaver mechanics to unvested shares.
- An investor (or lead investor) is requiring a founders' agreement as a condition of a seed round.

**Why now, not later:** founders' disputes are among the most destructive events for a startup. The time to negotiate is before any party has power over the other. A founders' agreement completed at inception saves enormous friction if a founder departs, performance disappoints, or external investors arrive and ask hard questions about the cap table.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Founder names, roles, and current equity percentages | Defines the parties and baseline cap table | — |
| Company name and jurisdiction (or "to be incorporated") | Governs applicable law for IP assignment, vesting, and enforcement | — |
| Equity split rationale (capital, IP, sweat equity, past contributions) | Must be documented to withstand investor or judicial scrutiny | — |
| Vesting schedule (duration, cliff) | Investor-required; protects company and other founders from a departing founder retaining full equity | 4-year / 1-year cliff |
| IP brought to company by each founder (pre-existing) | Must be explicitly assigned; IP owned by a founder personally is not company IP | — |
| Decision-making structure (tie-break, supermajority items) | Prevents operational deadlock | CEO tie-break on day-to-day |
| Good-leaver / bad-leaver definitions | Determines treatment of unvested (and sometimes vested) shares on departure | — |

## Optional inputs
- Future financing: pre-emption rights, anti-dilution preferences
- Non-compete scope (during + post-departure)
- Geographic restrictions on the business during the term
- Founder salary during bootstrap phase
- Advisor or board-observer seat for departing founders

## Core clauses

### 1. Recitals
Brief statement of the company's purpose, the founders' roles to date, and the reason for this agreement (alignment; investor readiness; cap-table clarity).

### 2. Contribution and equity allocation
Document each founder's contribution:
| Founder | Cash | IP contributed | Time/skills contribution | Equity % |
|---|---|---|---|---|
| [Name] | [Amount] | [Description] | [Role / months] | [%] |

The equity split should be agreed upfront and not modifiable without supermajority approval. Document the rationale for the split — "equal split" is simple but often creates misalignment; contribution-weighted splits require more negotiation but often produce better outcomes.

### 3. Reverse vesting schedule

**The mechanism:** founders receive all their shares at incorporation (unlike employees who receive options). However, unvested shares are subject to repurchase by the company at par (or nominal value) if the founder departs before their shares have vested.

Standard: 4-year vesting; 12-month cliff.
- Before cliff: all shares unvested and repurchasable.
- At cliff: 25% of shares vest; the cliff tranche is not repurchasable.
- After cliff: 1/48 of total shares vests per month.
- At 4 years: 100% vested; no remaining repurchase right.

> "In the event of a Leaver Event occurring within the Vesting Period, the Company shall have the right, exercisable within [30] days of the Leaver Event, to repurchase the Unvested Shares from the Departing Founder at their Original Issue Price."

### 4. Cliff
State the cliff date explicitly: "No Shares shall be Vested prior to the first anniversary of the Vesting Commencement Date. On the first anniversary, 25% (one-quarter) of each Founder's Shares shall vest."

### 5. Acceleration provisions
Define the trigger events:
- **Single trigger** (change of control alone): unvested shares vest on closing. Useful if founders want full protection from an acquirer leaving them employed but not rewarded.
- **Double trigger** (change of control + involuntary termination within 12 months): more investor-friendly; prevents founders from "cashing out" simply by selling the company.

> "In the event of a Change of Control, [50% / 100%] of each Founder's then-Unvested Shares shall vest [immediately / upon Involuntary Termination within 12 months of the Change of Control]."

### 6. Good leaver / bad leaver

These definitions control what happens to vested shares — not just unvested:

**Good leaver:**
> Departure due to: (a) termination without cause; (b) resignation for good reason (material reduction in role, breach of this Agreement by Company); (c) death; (d) permanent disability. Treatment: vested shares kept; unvested shares repurchased at par.

**Bad leaver:**
> Departure due to: (a) termination for cause (fraud, gross misconduct, criminal conviction); (b) voluntary resignation before the Cliff Date; (c) material breach of this Agreement, the IP Assignment, or Non-Compete. Treatment: vested shares subject to company repurchase at par or cost (negotiate the price); unvested shares forfeited without payment.

The good/bad leaver mechanism must also address shares held by the departing founder's entity or trust if any founder holds shares through a vehicle.

### 7. IP assignment — retroactive and prospective

**This clause is foundational.** All IP created before incorporation that relates to the company's business must be assigned to the company at (or before) the company's formation.

> "Each Founder hereby assigns to the Company, with full title guarantee and free from any encumbrances, all Intellectual Property Rights in and to: (a) the works and inventions set out in Schedule [IP Schedule], created by the Founder before the date of this Agreement in connection with the Company's business; and (b) all future works and inventions created by the Founder in the course of their engagement with the Company."

IP Schedule: enumerate specific assets — code repositories, designs, brand assets, domain names, prototypes. Vague assignments are litigated routinely.

Address moral rights (relevant in civil-law jurisdictions: France, Lebanon, UAE, KSA): include a waiver of moral rights to the extent permitted by applicable law; in French law, a consent clause is more appropriate than a waiver.

### 8. Founder roles and responsibilities
- Designate roles: CEO, CTO, CFO, CPO, etc.
- Define decision-making authority by role.
- **CEO tie-breaker**: CEO has the deciding vote on day-to-day operational decisions (below the reserved-matters threshold) in the event of deadlock.
- Founders are expected to devote [full / [X%]] of their time to the company.

### 9. Reserved matters (supermajority)
The following decisions require [75% / unanimous] founder approval:
- Increasing or changing the option pool.
- Adding new founders or issuing shares to new founders.
- Major financing rounds (changing terms, dilution thresholds).
- Sale of the company or material asset sale.
- Change to the vesting schedule.
- Incurring debt above [USD X] threshold.
- Terminating a founder for cause.

The supermajority threshold prevents a majority founder from taking unilateral action on these matters.

### 10. Non-compete

During the company's existence and for [12] months post-departure:
- Founder shall not directly or indirectly engage in any business that competes with the Company's core products/services.
- Territory: [geographic scope — where the company actually operates].
- Scope must be limited to genuinely competitive activity; blanket non-competes are unenforceable in most jurisdictions.

Post-departure non-compete enforceability:
- **UAE**: enforceable up to 2 years (Cabinet Decision 1/2022 for employees; similar principles for founders).
- **KSA**: enforceable up to 2 years with reasonable scope.
- **France**: non-compete requires compensation to the founder (otherwise unenforceable as a restraint of trade).
- **US (California)**: post-employment non-compete clauses are largely unenforceable under California law; use non-solicitation of customers and employees instead.
- **UK**: enforceable if reasonable in scope, duration, and geographic reach.

### 11. Confidentiality
Standard mutual confidentiality; post-termination survival. Trade secrets survive indefinitely.

### 12. Exit mechanics

**Drag-along**: if founders holding [50% / 67% / 75%] wish to sell the company, they may require remaining founders to sell on the same terms. Threshold should be high enough to prevent a slim majority from forcing a sale against the wishes of a significant minority.

**Tag-along**: if any founder sells shares, remaining founders have the right to participate in the sale on the same terms on a pro-rata basis.

**ROFR**: before any founder transfers shares, the company and other founders have a right of first refusal at the offered price.

**Buy-sell (shotgun)**: in the event of irretrievable deadlock:
> "[Either / a majority of] Founders may invoke the buy-sell mechanism: the invoking party offers to buy all other Founders' shares at price P, or to sell all its shares to the other Founders at price P. The other Founders must elect within [30] days: sell to the invoking party, or buy the invoking party's shares at price P."

The buy-sell mechanism is coercive by design — set the price carefully or risk triggering it and being the one who must buy.

### 13. Spouse / family provision
Any transfer of shares (including by inheritance, divorce settlement, or trust arrangement) to a spouse or family member requires company and co-founder approval. This prevents unwanted third parties from becoming shareholders through relationship breakdown.

### 14. Governing law and jurisdiction
Match to the company's jurisdiction of incorporation or the intended holding company jurisdiction (often Cayman, DIFC, or Delaware for VC-backed companies; UAE mainland or KSA for MENA-focused growth companies).

## Jurisdictional notes

| Jurisdiction | Key considerations |
|---|---|
| **DIFC / ADGM** | Full common-law framework; standard Cayman/DIFC founders' agreements enforce cleanly; DIFC Courts / ADGM Courts enforce English-law drafting |
| **Cayman Islands** | VC-standard holding company jurisdiction; combined with DIFC/UAE operating subsidiary; reverse vesting mechanics enforced |
| **UAE mainland** | Company law (Federal Decree-Law 32/2021); unlimited share redemption is limited by corporate law — use option/buyback structures rather than automatic forfeiture |
| **KSA** | Saudi Company Law 2022 permits private JSC structures with vesting; confirm Sharia compliance for any buy-sell mechanism that could be characterized as gharar (speculative) |
| **Lebanon** | SAL (S.A.) mechanics; reverse vesting via company buyback of treasury shares; limited by capital reduction rules |
| **France** | Reverse vesting must comply with French company law; AGA or BSPCE structures preferred for tax efficiency; non-compete requires financial compensation |
| **US (Delaware)** | Most VC-standard founders' agreements are Delaware-law; Section 83 / 83(b) election critical for restricted stock |

## Common mistakes

1. **Equal split without negotiation** — founders assume equal is fair; in practice contribution-weighted splits reduce resentment but require honest early conversation.
2. **No vesting** — investors universally require vesting; a company without vesting cannot raise VC investment without retrofitting it, which requires founder agreement and is often contested.
3. **IP not assigned at inception** — code, designs, or brand built before the company's formation are the founder's personal property until explicitly assigned; if a founding CTO leaves, the company may not own its own product.
4. **Vague good/bad leaver** — disputes arise when the line between voluntary resignation and departure for good reason is blurred; precision is essential.
5. **Buy-sell not understood** — founders sometimes agree to a shotgun provision without realizing its implications; the party with more capital can always win a shotgun.
6. **Missing spouse clause** — a founder's divorce can deliver equity to an unintended party unless this clause is in place.

## Related skills

- [[draft-shareholders-agreement]] — the full shareholder agreement for institutional investor rounds
- [[draft-safe]] — convertible instrument for seed financing before formal SHA
- [[draft-ip-assignment]] — standalone IP assignment for complex pre-incorporation IP
- [[draft-incorporation-package-difc]] — DIFC incorporation for MENA-based startups
- [[draft-vesting-schedule]] — standalone vesting schedule document
