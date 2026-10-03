---
name: legal-risk-assessment
title: Legal Risk Assessment
description: Assesses and classifies LEGAL risks (contract exposure, regulatory liability, IP, privacy, employment, dispute, breach-notification) using a severity-by-likelihood framework with explicit escalation criteria and cited rationale. Use when the user says assess legal risk on [matter], classify the risk in this contract, what's our exposure if [scenario], does this need outside counsel, evaluate the legal risk of [deal/feature/action], or describes potential liability, contractual obligation, regulatory consequence, or litigation threat. Tie-breaker vs operations:risk-assessment — if the question is about LIABILITY, NOTIFICATION CLOCKS, REGULATORY CONSEQUENCE, or CONTRACTUAL EXPOSURE, use this skill; if it is about UPTIME, CAPACITY, OPERATIONAL CONTINUITY, or PROCESS FAILURE only (no notification clock, no liability claim), defer to operations:risk-assessment. A security incident with PII triggers BOTH skills (chain). Do NOT use for pure operational risks like outages, vendor downtime,
  capacity gaps with no legal exposure.
author: nmoralescyber
author_url: https://github.com/nmoralescyber/claude-skill-optimization/tree/main/skills/legal/legal-risk-assessment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Legal Risk Assessment

Severity-by-likelihood classification for legal exposure with explicit escalation thresholds and cited rationale.

## Scope: LEGAL risks only

This skill handles: contract liability, regulatory consequence, IP infringement, privacy obligations (GDPR, CCPA, HIPAA, PR Ley 111-2005), employment claims, breach-notification clocks, dispute and litigation risk.

For pure operational risk (outages, capacity, process gaps, system reliability with NO liability/notification consequence) → use `operations:risk-assessment`.

### Boundary tie-breaker (the most-confused split)

| Signal in the prompt | Skill |
|---|---|
| "exposure," "liability," "breach notification," "fine," "claim," "subpoena" | THIS skill |
| "downtime," "SLA credit owed to customer" (because $$ owed) | THIS skill |
| "uptime target," "capacity," "process bottleneck," "redundancy" | `operations:risk-assessment` |
| Security incident with PII | BOTH — chain this skill (notification/liability) and operations (containment) |
| Vendor outage with no contractual penalty | `operations:risk-assessment` only |
| Vendor outage that breaches our customer SLA | THIS skill (downstream liability) |

## Framework

Every legal risk gets classified on two axes.

**Severity (impact if it occurs):**
- **5 — Catastrophic:** Existential threat (loss of license, regulatory shutdown, criminal liability, multi-million-dollar judgment, uninsured cyber loss exceeding cash runway)
- **4 — Major:** Significant business disruption (large fine, key customer loss via SLA breach, IP injunction, breach notification to >10k individuals)
- **3 — Moderate:** Material but bounded (single-jurisdiction fine, settled dispute, contract renegotiation forced, single-customer breach notification)
- **2 — Minor:** Recoverable cost (small fine, minor breach remediation, single-customer credit)
- **1 — Negligible:** Notice or correction only

**Likelihood (probability over the next 12 months):**
- **5 — Near-certain:** >75% — trigger condition already met or imminent
- **4 — Probable:** 40–75% — known patterns suggest this happens
- **3 — Possible:** 15–40% — has happened in similar contexts
- **2 — Unlikely:** 5–15% — would require unusual circumstances
- **1 — Rare:** <5% — theoretical possibility

## Risk score = Severity × Likelihood (1–25)

| Score | Action | Owner |
|---|---|---|
| 20–25 | Stop. Outside counsel today. Brief CEO/board. Notify cyber carrier if cyber-related. | GC + CEO |
| 12–19 | Outside counsel review within 5 days. Mitigation plan. | GC |
| 6–11 | Internal counsel decision. Documented mitigation. | In-house counsel |
| 3–5 | Standard risk register entry. Quarterly review. | Risk owner |
| 1–2 | Note. No action required. | Auto |

## Escalation triggers (independent of score — escalate immediately)

1. **Regulator inquiry received** — even informal
2. **Litigation hold notice** — preserve docs, freeze deletion
3. **Data breach suspected** — clocks start: GDPR 72hr, US states vary 30–90 days, **PR Ley 111-2005 = without unreasonable delay; DACO notification required for PR residents**, HIPAA 60 days
4. **Subpoena or warrant served** — counsel handles directly
5. **Whistleblower or anonymous tip** about legal violation
6. **Counterparty bankruptcy filing** affecting material agreement
7. **IP cease-and-desist received**
8. **Government investigation announced** (industry-wide or company-specific)
9. **Cyber-insurance claim conditions triggered** — most policies require notice within 24–72hr of "discovery of incident"; late notice = denial. Identify carrier, policy number, incident-response panel counsel before remediating.
10. **Customer DPA notification clock triggered** — many enterprise DPAs require 24–72hr sub-processor or incident notice; missing this = contractual breach independent of statutory clock.

## Output structure

Every assessment produces:

1. **Matter summary** (2–3 sentences)
2. **Risk classification** — severity score with rationale (cite the specific liability source: statute, contract clause, or case theory), likelihood score with rationale (cite the trigger condition observed). Use the rationale template below.
3. **Risk score** (severity × likelihood)
4. **Recommended action** per the score table
5. **Escalation flags** raised (or "none") with clock-start timestamp if any
6. **Mitigation options** ranked by cost vs. risk reduction
7. **Documentation requirements** — memo, contract amendment, communication log, evidence preservation
8. **Re-assessment trigger** — what would change the score

### Rationale template (use verbatim structure)

```
Severity = N because [specific harm], driven by [statute / clause / case theory: cite exactly].
  Worst-case quantum: [$ figure or qualitative bound].
Likelihood = N because [observed trigger condition or pattern], frequency baseline: [reference].
```

Example: "Severity = 4 because uncapped indemnification exposes us to defense costs and judgments without limit, driven by absence of mutual LoL clause in MSA §11. Worst-case quantum: ~$2M (estimated defense + settlement for one IP claim). Likelihood = 3 because the counterparty's product overlaps with two existing patents in our space; one prior C&D was sent to a competitor in 2024."

## Decline triggers (do NOT use this skill if)

- Question is purely financial modeling with no liability angle → use finance skills
- Question is "should we hire X for this matter" (resourcing) → use ops/HR
- Question is operational continuity only with no contract/regulatory consequence → use `operations:risk-assessment`
- Question is a contract redline request (not a risk score) → use `legal:review-contract`

## Common patterns (quick-reference, with citations)

| Pattern | Severity × Likelihood = Score | Driving authority / clause | Action |
|---|---|---|---|
| Indemnification cap missing or uncapped | 4 × 3 = 12 | Common-law unlimited liability default | Outside counsel |
| DPA missing where personal data is processed | 4 × 5 = 20 | GDPR Art. 28; CCPA service-provider requirements; PR Ley 111-2005 | Stop; fix today |
| IP assignment ambiguous (contractor work) | 4 × 4 = 16 | US Copyright Act §201(b) work-for-hire limits | Outside counsel |
| Auto-renewal without notice provision | 3 × 4 = 12 | State auto-renewal statutes (CA BPC §17600 et seq.; many states) | Counsel review |
| Choice of law in unfriendly jurisdiction | varies | Forum-selection clause | Assess on actual terms |
| LoL survives but indemnity doesn't | 4 × 3 = 12 | Contract-construction risk | Outside counsel |
| Pen-test requirement in customer MSA but not flowed to sub-processor | 4 × 4 = 16 | Customer MSA security exhibit | Flow-down required |
| Cyber policy notice window missed | 5 × 3 = 15 | Insurance policy "Conditions" section | Notify carrier NOW; escalate |
| Sub-processor added without 30-day customer notice | 3 × 4 = 12 | Customer DPA sub-processor clause | Cure notice immediately |
| Right-to-audit clause invoked by enterprise customer | 3 × 3 = 9 | Customer MSA audit clause | Internal counsel + InfoSec |
| PR resident PII in unencrypted storage | 4 × 4 = 16 | PR Ley 111-2005; cyber-insurance encryption warranty | Encrypt + assess notice obligation |

## When to chain to other skills

- **Vendor paperwork status driving the risk:** chain to `legal:vendor-check` first to confirm what's signed/missing
- **Operational containment of incident in parallel:** chain to `operations:risk-assessment` for ops side
- **Regulatory feature/launch question:** chain to `legal:compliance-check` for jurisdictional analysis
- **Need contract redlines to mitigate:** chain to `legal:review-contract`

## Tools that should be connected for best output

- CLM (Ironclad, Spotdraft, etc.) — contract context
- Legal hold system — litigation status
- Privacy management (OneTrust, etc.) — data inventory
- Cyber-insurance policy on file (PDF in document storage) — for notice clocks and panel-counsel list
- Incident-response runbook — to confirm clock-start timestamp
