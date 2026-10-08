---
name: review-risk-flagging-sboghossian
title: Risk Flagging (per Clause)
description: Use when you need a structured, per-clause risk assessment of a contract. Categorizes each identified risk as critical, medium, or low, with a short rationale and proposed fix for each. Applies a consistent severity taxonomy across all contract types, with MENA-specific flags for penalty clause enforceability, arbitration clause adequacy, and data protection gaps. Produces machine-readable JSON output suitable for integration into review workflows.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-risk-flagging
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Risk Flagging (per Clause)

## When to use this

Use as a first-pass risk scan on any commercial contract. This skill produces a clause-level risk register — every clause with a material issue is flagged with a severity rating, the nature of the risk, and a proposed fix. It is not a deep-dive review; for specific high-stakes clauses, escalate to the relevant specialist skill.

Run this skill:
- Before a full [[review-msa-deep-review]] to build a prioritized issues list
- As a standalone output for a time-pressured client who needs "what are the biggest risks?"
- As part of a due-diligence report where a risk register is a required deliverable

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Contract text | Full document; clause-by-clause scan | Required |
| Document type | Calibrates what is "market standard" — severity depends on contract type | Infer from document; ask if unclear |
| Party perspective | Which party's risk lens? (Client vs Provider, Landlord vs Tenant) | Ask if unclear |
| Jurisdiction | Affects enforceability rules and what constitutes a "critical" local risk | From governing-law clause |

## Severity Taxonomy

### Critical — Always Surface

Issues in this category must be flagged even in a 15-minute review. They can result in regulatory violation, unlimited liability, permanent IP loss, or complete loss of deal value.

| Risk | Trigger |
|---|---|
| Uncapped liability | No general liability cap, or cap applies only to one party |
| Cap below 1× annual fees | Cap is nominally present but set so low as to be meaningless |
| Indemnity asymmetry | One party indemnifies broadly (any claim, any loss); other indemnifies narrowly or not at all |
| Termination for convenience without reasonable notice | T4C available but notice is under 15 days; equivalent to immediate termination |
| IP assignment without carve-out for pre-existing IP | Vendor's background tools get assigned inadvertently |
| Overbroad non-compete | Scope (functional + geographic + temporal) so wide it is restraint of trade; may be void |
| Adverse governing law or forum | Law or forum that is actively hostile to the user's position (e.g., counterparty's home courts with no arbitration) |
| No DPA where personal data is processed | GDPR / KSA PDPL / UAE PDPL compliance breach; regulatory fine exposure |
| Auto-renewal with a notice window over 90 days | Creates a trap — if deadline missed, locked in for another full term |
| Most-favored-customer clause with retroactive application | Requires Provider to refund past payments if a better price was given to anyone |
| Audit rights that are unlimited or unbounded | Effectively allows counterparty to conduct continuous interference with operations |

### Medium — Surface in Standard Reviews

Issues that create material commercial risk but do not rise to immediate regulatory or unlimited-liability concern.

| Risk | Trigger |
|---|---|
| Notice periods misaligned across termination provisions | Termination for convenience requires 60 days; forfeiture requires 7 days — inconsistency creates ambiguity |
| Force majeure missing modern carve-outs | Absent: pandemic, cyber incident, government-order closure, financial system disruption (Lebanon-relevant) |
| Insurance amounts unspecified | Contract requires "adequate" insurance without naming minimum cover amounts |
| Survival clause omits key obligations | Confidentiality, IP, indemnification do not survive termination — they should |
| Confidentiality term too short for trade secrets | 2-year confidentiality term on genuinely sensitive technology — should be longer or indefinite |
| Cure period absent for material breach | No opportunity to remedy before termination right triggers |
| Penalty / liquidated damages clause | In KSA and UAE onshore: courts have discretion to reduce; in DIFC/UK: enforceability requires genuine pre-estimate of loss |
| Assignment clause silent on change of control | No restriction on counterparty being acquired — contract may transfer to a competitor |
| Most-favored-customer clause prospective-only but poorly scoped | Applied to all customers rather than similarly-situated customers — creates unworkable obligation |
| Undefined "material breach" | Each party will define it self-servingly; disputes inevitable |
| No transition assistance on termination | IT/outsourcing contract ends without data return or migration assistance obligation |

### Low — Note for Completeness

Issues that create minor risk or are best-practice gaps. Raise in a written report but do not hold up execution.

| Risk | Trigger |
|---|---|
| Defined terms not capitalized consistently | Minor drafting error; could create ambiguity in dispute |
| Boilerplate variations from standard | e.g., no waiver clause absent; severability clause narrower than standard |
| Cosmetic style inconsistencies | Cross-references to wrong clause numbers; defined term used before definition |
| Excessive recitals that create obligations | Recitals are generally not operative; but "WHEREAS Party A agrees to…" language can bind |

## Jurisdiction-Specific Flags

Always run these checks in addition to the general flags above:

### UAE (onshore)
- **Penalty clauses**: UAE Civil Code allows courts to adjust penalties to reflect actual loss, regardless of what the contract says. A clause with a disproportionate penalty is enforceable but likely to be reduced judicially. Draft as indemnification for actual loss rather than pre-agreed penalties.
- **IP assignment language**: present-tense assignment is required; "agrees to assign" may be insufficient
- **Stamp duty / registration**: commercial property leases and certain IP assignments may need registration

### KSA
- **Arbitration clause adequacy**: a clause saying only "disputes shall be resolved by arbitration" is inadequate. Must specify: institution (SCCA/ICC/DIAC preferred), seat, language, number of arbitrators. An incomplete clause may result in SCCA or general court jurisdiction by default.
- **Penalty clauses**: Saudi commercial courts apply Shariah principles on proportionality; penalties exceeding actual loss are routinely reduced
- **Personal data**: PDPL compliance is now actively enforced by SDAIA; missing DPA on Saudi personal data is a critical flag

### Lebanon
- **Currency denomination**: for long-term contracts, USD denomination with Banque du Liban regulatory acknowledgment is essential. LBP-denominated contracts for meaningful amounts create significant risk given exchange rate instability.
- **Force majeure**: should expressly address banking system restrictions, port closures, and regulatory moratoriums as potential force majeure events, given Lebanon's recent history
- **Arbitration**: specifying ICC, DIFC-LCIA, or Paris arbitration (given Lebanon-France legal ties) is recommended; domestic courts are less predictable

### DIFC / ADGM
- **DIFC Data Protection Law / ADGM Data Protection Regulations**: DPA required for any personal data processing; breach notification within 72 hours
- **Unfair contract terms**: DIFC Contract Law includes protections for unreasonable standard terms in B2B contracts
- **Death and personal injury**: caps on liability for death or personal injury caused by negligence are void

### France / EU
- **Gross negligence (faute lourde)**: liability limitation clauses may be ineffective for gross negligence under French law; do not rely on cap for deliberate or grossly negligent conduct
- **GDPR**: DPA with standard contractual clauses required for cross-border data transfers outside EEA

## Output Structure

Per flagged clause, output:

```json
{
  "clause": "<section number and title>",
  "severity": "critical|medium|low",
  "issue": "<one sentence description of the risk>",
  "rationale": "<one sentence explaining why this is a risk and for whom>",
  "proposed_fix": "<one sentence redline recommendation or alternative approach>",
  "jurisdiction_note": "<if the risk is jurisdiction-specific>"
}
```

At the end of the risk register, provide:

```json
{
  "overall_risk_level": "critical|high|medium|low",
  "critical_count": <int>,
  "medium_count": <int>,
  "low_count": <int>,
  "top_3_issues": ["<brief description>", ...]
}
```

## Escalation Triggers

Escalate to a specialist skill when:
- More than 3 critical issues in the liability / indemnification cluster → use [[review-indemnification-balance]] + [[review-liability-cap-reasonableness]]
- IP ownership issues are critical → use [[review-ip-ownership-clarity]]
- Full MSA review is needed → use [[review-msa-deep-review]]
- Structural gaps (missing clauses) → use [[review-missing-clauses]]
- Atypical / non-standard clauses → use [[review-unusual-terms-detector]]

## Common Mistakes in Risk Flagging

- Marking every clause as medium — dilutes the report; only flag actual risk, not theoretical risk
- Failing to distinguish between what is unenforceable (legal risk) vs what is commercially unfavorable (negotiation risk) — these require different remediation approaches
- Rating enforceability under US law when the governing law is UAE — always apply the actual governing jurisdiction's rules
- Omitting a proposed fix — a finding without a remedy is unhelpful; always provide a direction even if approximate

## Related Skills

- [[review-msa-deep-review]]
- [[review-missing-clauses]]
- [[review-unusual-terms-detector]]
- [[review-indemnification-balance]]
- [[review-liability-cap-reasonableness]]
- [[review-nda-quick-check]]
