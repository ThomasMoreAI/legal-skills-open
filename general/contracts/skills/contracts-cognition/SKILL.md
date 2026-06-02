---
name: contracts-cognition
title: contracts-cognition
description: Use when reading a contract for risk and constraint — clause shape, redline priority, what the contract actually binds. Triggers on 'review this contract', 'what does this MSA constrain'.
author: event4u-app
author_url: https://github.com/event4u-app/agent-config/tree/main/.agent-src/skills/contracts-cognition
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# contracts-cognition

## When to use

- A draft MSA / DPA / SOW / vendor contract / partner agreement lands and a non-lawyer needs to read it for *what it actually constrains*, *which clauses carry real risk*, and *what to redline first*.
- An existing contract is being renegotiated; the question is *which clauses are now misshapen* given current scale, regulatory regime, or customer mix.
- A new customer contract triggers obligations (SLA, indemnity, audit, data-handling) that need to be sized against operational capacity before signing.

Do NOT use as a substitute for actual legal counsel (this skill produces the *non-lawyer cognition* that prepares the conversation with counsel, not the legal opinion), for privacy-specific review (route to `privacy-review` (P6); this skill composes P6 for data clauses), or for contract management software / e-signature operations.

## Cognition cluster

- **Mental model 28 — Inversion.** *"What would force us to invoke this clause? What would force the counterparty to invoke it?"* Inversion surfaces which clauses are dormant boilerplate vs which are loaded triggers. See [`mental-models.md`](../../../docs/contracts/mental-models.md) § 28.
- **Mental model 21 — Second-order thinking.** Each clause has a second-order shape: indemnity caps interact with insurance coverage; SLAs interact with operating-cost; auto-renewal interacts with switching cost. Reading clauses in isolation misses the load-bearing combinations. See `mental-models.md` § 21.
- **Mental model 26 — Optionality.** Each clause either preserves or forecloses future choices (terminate-for-convenience preserves; auto-renewal forecloses; exclusivity forecloses; MFN forecloses). The cost of a clause is the optionality it removes. See `mental-models.md` § 26.
- **Context-spine — regulatory-regime + customer-segment + org-stage.** Read **regulatory-regime** (J1) for floor-bound clauses (GDPR DPA terms, HIPAA BAA, SOC 2 audit). Read **customer-segment** for risk sizing (enterprise SLA terms ≠ SMB SLA terms). Read **org-stage** for what's affordable (early-stage = avoid uncapped indemnities; growth = can absorb tighter SLAs).

## Procedure

### Step 0: Frame the contract by intent

Two questions before reading clauses:

1. *What outcome are we trying to enable?* (sell to enterprise, integrate vendor, partner co-sell, license IP).
2. *What outcomes are we trying to prevent?* (unbounded liability, lock-in, IP leakage, audit ambush, payment risk).

Without intent, every clause looks equally important. With intent, 80 % of clauses are background and 20 % are load-bearing.

### Step 1: Identify the load-bearing clause families

Five families carry most real risk for non-lawyers:

1. **Liability & indemnity** — caps, carve-outs, IP indemnity, mutual vs one-way. Uncapped indemnity is the canonical trap.
2. **Term, renewal, termination** — auto-renewal, notice windows, termination-for-convenience vs for-cause, data-return obligations.
3. **Data & privacy** — DPA, sub-processors, data location, breach notification, retention, deletion. Compose `privacy-review` (P6) for the deep read.
4. **IP & confidentiality** — work-product ownership, license grants, confidentiality term, residual-knowledge clauses.
5. **Commercial mechanics** — payment terms, MFN, exclusivity, change-of-control, audit rights.

Other clauses (governing law, force majeure, severability, notices) are usually boilerplate; flag deviations but don't lead with them.

### Step 2: Inspect each load-bearing family

For each family, read three things:

1. **The clause as written** — what does it literally say.
2. **The clause invoked** — *"under what scenario does this clause fire?"*
3. **The clause's tail risk** — *"what's the worst-case if it fires?"*

A clause whose tail risk is bounded and small = accept. Bounded and large = redline to reduce. Unbounded = redline to cap or refuse.

### Step 3: Run the inversion check

For each load-bearing clause, ask:

1. *"Would we sign this if the counterparty had 10× our leverage?"* Reveals which clauses we tolerate because of relationship, not because they're fair.
2. *"What would we want if we were the counterparty?"* Reveals which clauses are mutual vs one-way unfairly.
3. *"What scenario makes this clause matter in 18 months?"* If no scenario, the clause is dormant; if a plausible scenario exists, prioritize the redline.

### Step 4: Build the redline priority list

Rank redlines by:

1. **Tail-risk size** — uncapped > capped-large > capped-small.
2. **Probability of invocation** — high-likelihood clauses (auto-renewal, payment terms) outrank low-likelihood (force majeure).
3. **Asymmetry** — one-way clauses where the counterparty bears no symmetric risk.
4. **Optionality cost** — clauses that foreclose future moves (exclusivity, MFN, change-of-control restrictions).

Top 3–5 redlines = the negotiation; everything else is acceptable or backlog.

### Step 5: Validate the read before emitting

Before producing the artifact, verify three things:

1. **Family coverage** — confirm each of the five load-bearing families was inspected (Step 2); silent skips mean the contract was not read, only skimmed.
2. **Tail-risk sizing** — assert every top-5 redline has a named worst-case scenario and a named cap / carve-out / refusal-shape ask; un-sized redlines fail.
3. **Counsel handoff** — check that the contract-cognition note explicitly flags which clauses need legal counsel review vs which are commercial / operational decisions; this skill does not replace counsel.

All three must pass. If any fails, return to the failing step.

### Step 6: Emit the contract-cognition note

Produce the contract-cognition artifact for the negotiation lead (founder, sales lead, ops lead) and for counsel. The artifact is the non-lawyer cognition that prepares the conversation with counsel, not the legal opinion.

## Related Skills

**WHEN to use this**

- Reading a draft MSA / DPA / SOW / vendor / partner contract for risk and constraint.
- Renegotiating an existing contract at a new scale or under a new regulatory regime.
- Sizing customer-contract obligations against operational capacity.

**WHEN NOT to use this**

- Privacy-specific deep read — route to [`privacy-review`](../privacy-review/SKILL.md) (P6); this skill composes P6 for data clauses.
- Data-classification / retention judgment — route to [`data-handling-judgment`](../data-handling-judgment/SKILL.md) (P7).
- Build-vs-buy / partner-vs-vendor decision shape — route to [`build-buy-partner`](../build-buy-partner/SKILL.md) (P1); P1 outputs the *whether*, this skill outputs the *what to redline*.
- Actual legal opinion — route to qualified counsel; this skill prepares the cognition for the counsel conversation, not replaces it.

## When the agent should load this

- "Review this MSA."
- "What does this DPA actually bind us to?"
- "Which clauses do we redline first?"
- "Is this contract safe to sign?"
- "Lies mir den Vertrag durch."

## Output

1. **`contract-frame.md`** — intent (what to enable / prevent), counterparty leverage read, regulatory-regime context.
2. **`load-bearing-clauses.md`** — five families × clause-as-written + invocation scenario + tail risk per clause.
3. **`redline-priority.md`** — top 3–5 redlines ranked by tail-risk × probability × asymmetry × optionality cost; named asks per redline.
4. **`counsel-handoff.md`** — explicit list of clauses that need legal counsel review vs commercial / operational decisions.

## Gotcha

- Uncapped indemnity is the silent killer. If the cap is missing or excludes major risk categories (IP, data breach), it's the first redline.
- Auto-renewal with short notice windows compounds across years — calendar the notice window the day the contract is signed.
- "Industry-standard" is a marketing word, not a legal one. Push for the specific cap / term / carve-out.
- Mutual NDAs that look symmetric often aren't — confidentiality term, residual-knowledge, and remedy clauses skew one-way silently.

## Do NOT

- Do NOT issue legal opinions; this skill prepares cognition for counsel, not replaces counsel.
- Do NOT collapse all clauses into one list; the five families carry the real risk, treat them differently.
- Do NOT skip the inversion check — clauses that look fine in our shoes often look terrible in the counterparty's.

## Runnable example

Growth-stage SaaS, customer is Fortune-500 enterprise, MSA draft from customer's legal.

- Step 0 — Intent: enable enterprise deal, prevent uncapped liability + audit ambush + data-handling overreach.
- Step 1 — Identify families: liability (mutual indemnity, uncapped on IP); term (3-year auto-renew, 90-day notice); data (DPA references but no DPA attached); IP (work-product ownership unclear for integration scripts); commercial (MFN clause buried in pricing schedule).
- Step 2 — Inspect: uncapped IP indemnity → tail risk = bet-the-company (uncapped patent claim). Auto-renewal 3-year → tail risk = $1.2M locked in if missed notice. MFN → tail risk = forecloses bundle pricing across portfolio.
- Step 3 — Inversion: would we sign this with 10× leverage? No. Symmetric? Indemnity is one-way; MFN is one-way.
- Step 4 — Redline priority: (1) cap IP indemnity at 2× annual contract value with reasonable carve-outs; (2) reduce auto-renewal to 1 year, expand notice to 180 days; (3) strike MFN or limit to identical-SKU; (4) attach DPA before signing; (5) clarify integration-script IP ownership.
- Step 5 — Validate: five families inspected; top-5 redlines sized with cap / refusal asks; counsel-handoff names IP indemnity + MFN as counsel-led, auto-renewal as commercial-led. Pass.
- Step 6 — Emit contract-cognition note for negotiation lead; route IP indemnity + MFN to counsel; sales lead negotiates auto-renewal and DPA attachment.
