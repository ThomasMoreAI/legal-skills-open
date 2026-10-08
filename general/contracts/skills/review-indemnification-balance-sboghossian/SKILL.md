---
name: review-indemnification-balance-sboghossian
title: Indemnification Balance Review
description: 'Use when reviewing a contract''s indemnification clauses for balance, scope, procedural fairness, and alignment with market norms. Covers the full indemnity analysis: trigger scope, asymmetry assessment, defense-control mechanics, settlement consent, cap alignment, and survival periods. Applies to MSAs, SaaS agreements, professional services contracts, and any bilateral commercial arrangement across MENA, UK, EU, and US jurisdictions.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-indemnification-balance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Indemnification Balance Review

## When to use this

Use this skill whenever a contract contains one or more indemnification clauses and you need to assess whether the allocation of risk is balanced, procedurally sound, and aligned with market norms for the deal type. Typical triggers:

- Reviewing an MSA, SaaS subscription, professional-services, or outsourcing agreement
- Negotiating commercial contracts where indemnification is a sticking point
- A counterparty has submitted a one-sided draft with broad indemnity language
- Pre-execution diligence on a signed agreement being acquired or novated

This skill is a focused sub-review; run it alongside [[review-msa-deep-review]] or [[review-risk-flagging]] for a complete picture.

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Contract text | The indemnification clauses themselves, plus cap and survival provisions | Required |
| Deal type | MSA / SaaS / construction / M&A / PE / employment — market norm differs | Infer from contract |
| Party perspective | Which party are you acting for? | Ask if unclear |
| Jurisdiction | Civil-law vs common-law affects enforceability of carve-outs | Infer from governing-law clause |

## Review Methodology

Work through each indemnification provision in the following order.

### 1. Scope — what triggers the indemnity?

Identify what events cause the indemnification obligation to fire:

- **Third-party claims only** — narrowest, most Provider-favored; does not cover direct losses between the parties
- **Third-party plus first-party losses** — broader; check whether this effectively makes the indemnity a strict-liability damages clause
- **Category triggers**: breach of warranty / breach of covenant / breach of law / IP infringement / data breach / willful misconduct / fraud / negligence

Flag any trigger that causes the Indemnified Party's own negligence to be covered by the Indemnifying Party — this is rare, jurisdictionally unusual, and frequently unenforceable as against public policy (especially UAE Civil Code, Lebanese Code of Obligations, KSA principles derived from Shariah where fault allocation is causal).

### 2. Asymmetry — does each party's exposure match its risk profile?

**Market-balanced setup (commercial services)**:
- Provider indemnifies: IP infringement by its own deliverables; data breach caused by its systems; willful misconduct or gross negligence of its personnel
- Client indemnifies: claims arising from Client's content or data (excluding personal data breaches caused by Provider); Client's violation of applicable law; third-party claims caused by Client's use of the service outside permitted scope

**Red flags**:
- Only one party carries indemnification obligations (acceptable in pure vendor/supplier context; unusual in professional services)
- Client required to indemnify Provider for general third-party claims without limiting to Client-caused claims
- Provider required to indemnify for consequential damages flowing from Client's specifications

### 3. Defense Procedure

A well-drafted indemnification clause contains all four procedural mechanics:

**a) Notice timing**: Indemnified Party must give prompt written notice upon becoming aware of a claim. The notice must describe the claim in sufficient detail. Consequence of late notice: typically, Indemnifying Party is relieved only to the extent it is prejudiced by the delay (US, UK, DIFC, ADGM standard) — not automatic forfeiture, which is a harsher standard.

**b) Control of defense**: Indemnifying Party typically controls defense counsel selection and strategy. Exceptions to flag:
- Reputational matters: Indemnified Party should retain the right to co-counsel at its own expense where the claim names it publicly
- Conflicts of interest between parties
- Regulatory proceedings where Indemnified Party has regulatory obligations

**c) Settlement consent**: Indemnified Party must consent before any settlement is accepted if: (i) the settlement imposes obligations on Indemnified Party; (ii) the settlement includes any admission of fault or liability by Indemnified Party; (iii) relief obtained is something other than monetary damages. Flag any clause that allows the Indemnifying Party to settle without consent — this is a significant risk.

**d) Cooperation**: Indemnified Party must cooperate reasonably at Indemnifying Party's expense. Scope of "cooperation" should be defined; open-ended cooperation obligations create risk.

### 4. Cap Alignment

Indemnification obligations frequently sit outside the general liability cap. Map which carve-outs exist and whether they are consistent:

| Indemnity type | Typical cap treatment |
|---|---|
| IP infringement | Uncapped or separate higher sublimit |
| Data breach / personal data | Uncapped or separate sublimit (GDPR/PDPL fines alone can exceed contract value) |
| Willful misconduct / fraud | Uncapped (most jurisdictions void caps for fraud) |
| Death / personal injury | Uncapped (statutory in UK, DIFC, ADGM) |
| General IP warranty breach | Often within general cap |
| Gross negligence | Increasingly uncapped; KSA courts have wide discretion under Shariah |

Check that the carve-out language in the indemnification section aligns exactly with the carve-out language in the liability cap section. Mismatches are a frequent drafting error (e.g., cap section carves out "willful misconduct" but indemnity section uses "intentional acts" — not necessarily synonymous in civil-law jurisdictions).

### 5. Survival Period

Indemnification obligations must survive termination/expiration of the agreement. Verify:

| Category | Market survival period |
|---|---|
| General indemnification | 12–36 months post-termination |
| IP indemnification | 5–7 years or applicable statute of limitations |
| Data breach | 3–5 years (linked to breach-notification limitation periods) |
| Tax indemnification (M&A) | Length of tax audit exposure (typically 5–10 years) |

Flag if a survival clause omits indemnification obligations entirely or caps survival at the general limitation of liability.

## What to Flag — Severity Scale

| Severity | Issue |
|---|---|
| Critical | Indemnity covers Indemnified Party's own sole negligence |
| Critical | No settlement consent requirement — Indemnifying Party can bind Indemnified Party |
| Critical | No notice requirement at all — Indemnifying Party may have no knowledge of claim before judgment |
| Critical | Indemnity uncapped on both IP AND data breach but general cap is near-zero (e.g., 1-month fees) |
| High | No defense-control mechanic — ambiguous who runs the litigation |
| High | Cooperation obligations are open-ended with no cost cap |
| Medium | Survival period shorter than relevant limitation periods |
| Medium | IP indemnity trigger limited to "finally adjudicated" infringement — misses settlement scenarios |
| Low | "Promptly" not defined with a number of days for notice |

## Jurisdictional Notes

**UAE (onshore)**: Civil Code penalty-clause rules (similar to Article 390 on adjustability) can affect indemnification provisions styled as liquidated amounts. Courts have broad discretion to reduce disproportionate claims. Ensure indemnification is framed as indemnification against loss, not as a pre-agreed penalty.

**KSA**: Shariah-derived principles require proportionality between obligation and loss. Gross negligence and willful misconduct: courts may adjust based on causal contribution. Arbitration clauses within indemnification disputes must specify SCCA or ICC rules + seat.

**DIFC / ADGM**: Common-law jurisdiction. Standard English-law indemnification concepts apply. "Defend, indemnify, and hold harmless" has distinct meaning from "indemnify only" — the former includes cost of defense. DIFC Courts have confirmed enforceability of broad third-party-claim indemnities subject to standard negligence-caused-by-Indemnified-Party carve-outs.

**Lebanon**: Moral fault (faute) allocation follows civil-law contributory negligence — pure strict-liability indemnities are unusual; courts may reduce based on parties' proportional fault.

**France / Egypt**: Similar civil-law adjustability concerns. "Defend" obligations as a standalone contractual duty are less established than in common-law systems; often replaced with payment-on-demand obligations after judgment.

**US**: "Defend" and "indemnify" trigger separate duties. Duty to defend is broader (triggered by allegations; does not wait for judgment). Duty to indemnify is narrower (triggered by actual liability). Anti-indemnity statutes in some states (Texas, California) restrict indemnification of a party's own negligence in construction contracts.

## Output Format

For each indemnification clause identified, produce:

```json
{
  "clause_id": "<section number>",
  "scope": "<third-party only | first-party and third-party | mixed>",
  "triggers": ["ip", "data-breach", "breach-of-warranty", ...],
  "asymmetry_rating": 1-5,
  "procedure_completeness": {
    "notice": true/false,
    "defense_control": true/false,
    "settlement_consent": true/false,
    "cooperation": true/false
  },
  "cap_carve_out": true/false,
  "survival_adequate": true/false,
  "overall_balance": 1-5,
  "issues": [
    { "severity": "critical|high|medium|low", "issue": "...", "recommended_fix": "..." }
  ]
}
```

Overall balance scale: 1 = heavily Indemnified-Party-unfavorable; 3 = market-balanced; 5 = heavily Indemnifying-Party-friendly.

## Common Mistakes

- Drafting "Indemnify and hold harmless" without "defend" — counterparty may argue no obligation to fund litigation
- Using "third-party claims" but omitting regulatory proceedings (regulators are not "third parties" in the common sense but impose enforceable fines)
- IP indemnification that covers only "infringement of third-party patents" — misses copyright, trade secrets, and trademark claims
- Bilateral indemnification without clear "each party separately indemnifies the other for its own acts" framing — creates argument that indemnities are circular and offset

## Related Skills

- [[review-liability-cap-reasonableness]]
- [[review-msa-deep-review]]
- [[review-risk-flagging]]
- [[review-missing-clauses]]
- [[draft-msa]]
- [[draft-indemnification-clause]]
