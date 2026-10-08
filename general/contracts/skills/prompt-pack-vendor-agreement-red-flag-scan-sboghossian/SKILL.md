---
name: prompt-pack-vendor-agreement-red-flag-scan-sboghossian
title: Vendor Agreement Red Flag Scan
description: Use when a user pastes or uploads a vendor agreement and needs a rapid structured analysis of the clauses that create financial exposure, restrict flexibility, or are unusually one-sided — followed by suggested redlines. This is a review/redline skill, not a drafting skill. Covers payment terms, liability limits, termination conditions, IP ownership, service obligations, and governing law issues. Applicable across all commercial contracts in MENA and common-law jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-vendor-agreement-red-flag-scan
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Vendor Agreement Red Flag Scan

## When to use this

Use this skill when a legal team or contract manager receives an incoming vendor agreement and needs to:

1. Identify the clauses that create the most financial, operational, or reputational exposure before negotiation begins
2. Understand which terms are unusually one-sided compared to market standard
3. Generate draft redline language to counter problematic provisions

This is not a full due-diligence or legal-opinion exercise. It is a structured first-pass review designed to surface the top issues efficiently — typically before a lawyer spends time on a line-by-line review.

Typical contract types: SaaS subscription agreements, professional services MSAs, IT infrastructure contracts, outsourcing agreements, facilities and maintenance agreements, logistics and supply agreements.

## Inputs

| Input | Why it matters |
|-------|---------------|
| Vendor agreement text (paste or upload) | The document to be reviewed |
| Company name and primary jurisdiction | Shapes the applicable law analysis and risk-tolerance benchmarks |
| Company's role (customer / service recipient) | Confirms whose lens to apply — this skill defaults to reviewing on behalf of the customer |
| Industry / sector (optional) | Sector-specific obligations (e.g., financial services, healthcare) affect risk threshold |

## Review methodology

Work through the agreement in this order:

### Pass 1 — Structural scan (2 minutes)

Identify: parties, governing law, term, fee structure, service description. Flag if:
- Governing law is an unusual or foreign jurisdiction without explanation
- The contract is dated but unsigned — review may be moot
- Material defined terms are referenced but not defined

### Pass 2 — Financial exposure flags

Examine each of the following:

1. **Payment terms and automatic renewal**
   - Is there an auto-renewal clause with short notice-to-cancel window (< 60 days)?
   - Are there price escalation provisions (uncapped CPI escalator, unilateral vendor right to reprice)?
   - Are there success fees, overage fees, or true-up mechanisms that are uncapped or vaguely defined?
   - Red flag: "Fees may be adjusted by vendor at any time upon notice" with no cap

2. **Liability cap**
   - What is the liability cap? (Common market standards: 1× or 2× annual fees; 12-month fees)
   - Is the cap mutual (covers both parties' liability) or only limits vendor's liability?
   - Are there uncapped liabilities on the customer's side (e.g., IP indemnification, data breach caused by customer)?
   - Red flag: Cap only applies to vendor; customer has unlimited liability for IP warranties or data breach

3. **IP ownership**
   - Who owns deliverables, custom developments, and modifications?
   - Is there a work-for-hire or IP assignment clause for custom work?
   - Does the vendor retain a broad license to customer's data for its own AI training or analytics purposes?
   - Red flag: "Vendor retains all IP in deliverables" with no assignment or exclusive license back to customer
   - Red flag: "Customer grants vendor a perpetual, irrevocable license to use customer data for product improvement"

4. **Indemnification imbalance**
   - Does customer indemnify vendor against third-party claims arising from customer's use? What is the scope?
   - Is vendor's indemnification of customer limited to IP infringement only, leaving customer exposed for data breaches, service failures, etc.?
   - Red flag: Customer indemnifies vendor for any regulatory fines arising from vendor's service failures

5. **Termination and exit**
   - What triggers entitle vendor to terminate? Are they subjective (e.g., "vendor may terminate if it determines customer's use is harmful to vendor's reputation")?
   - What happens to customer data on termination? Is there a data export window?
   - Are termination-for-convenience rights mutual or one-sided?
   - Red flag: Vendor may terminate at will; customer must give 12 months' notice
   - Red flag: No data export right; customer data deleted immediately on termination

6. **Service obligations and SLAs**
   - Are service levels defined with objective metrics (uptime %, response time)?
   - What is the remedy for SLA breach — service credits only? Is the credit mechanism a full substitute for damages?
   - Red flag: Credits are sole and exclusive remedy for any service failure (bars damages claim even for catastrophic outage)

7. **Data handling and confidentiality**
   - Does vendor have appropriate data security obligations?
   - Is there a data processing addendum / DPA?
   - What is the breach notification timeline?
   - Red flag: No DPA where vendor processes personal data; breach notification timeline > 72 hours

8. **Governing law and dispute resolution**
   - Is governing law neutral or strongly vendor-favorable?
   - Is dispute resolution by arbitration or litigation? In which seat?
   - Are there asymmetric rights (vendor may sue in any court; customer must arbitrate)?
   - Red flag: Vendor's home jurisdiction with no neutral forum option

### Pass 3 — Jurisdiction-specific flags

| Jurisdiction | MENA-specific checks |
|---|---|
| UAE (onshore) | Confirm Arabic-language contract obligation; UAE Commercial Transactions Law caps on late payment interest; TDRA / SCA sector-specific obligations if relevant |
| DIFC / ADGM | Common-law contract — check consequential damages exclusion is clearly worded; DIFC Courts jurisdiction clause |
| KSA | SAR currency obligations; ZATCA VAT compliance on invoices; Saudi local content (Iktva) requirements if applicable; Arabic version required |
| LB | Code of Obligations and Contracts caps; FX risk allocation given currency instability |
| EG | Egyptian Investment Authority approval requirements; Egyptian Court exclusive jurisdiction for certain regulated activities |
| EU | GDPR compliance mandatory; standard DPA required; data residency requirements |

## What to flag

Rank each flag by severity:

| Severity | Definition | Examples |
|---|---|---|
| Critical | Clause creates large financial exposure or strips a fundamental right | Uncapped IP indemnification; no data return on termination; unlimited price escalation |
| High | Clause is materially one-sided vs. market standard | Sole remedy clause for SLA breach; auto-renewal with 30-day notice |
| Medium | Clause is suboptimal but negotiable | Short warranty period; vague service description; no most-favored-customer clause |
| Low | Minor drafting issue; low practical risk | Undefined capitalized term; formatting inconsistency |

## Output format

Structure the output as:

```
## Executive Summary
[2-3 sentence summary of the overall balance and top 3 concerns]

## Red Flag Table
| # | Clause ref | Severity | Issue | Suggested redline |
|---|-----------|----------|-------|------------------|
...

## Suggested Redline Language
[For each Critical and High flag: proposed replacement or additional clause language]

## Governing Law Note
[If governing law creates specific risks for the customer]
```

## Jurisdictional / practice-area notes

**Consequential damages:** In civil-law jurisdictions (LB, EG, KSA onshore, UAE onshore), a consequential damages exclusion may be read as excluding only "indirect" damages per the civil code but not as a liability cap — civil law courts may still award direct damages well above the contractual cap. Redline should address both.

**Penalty clauses:** UAE and Lebanese civil codes allow judges to adjust penalty clauses (liquidated damages) to the actual damage. US-style liquidated damages clauses may be read differently in MENA courts.

**Currency:** KSA and UAE contracts should specify SAR or AED or USD to avoid ambiguity. LB contracts should address the multi-currency environment.

## Limits and escalation

- This scan identifies risk flags; it does not constitute a legal opinion
- Escalate to qualified local counsel for: regulated industries (banking, healthcare, telecoms), government contracts, contracts exceeding [AED 5M / USD 1.5M] in value, or contracts where the identified flags are critical
- AI-generated redlines must be reviewed by legal counsel before use in live negotiation
- Do not use this skill to generate a final redlined document without lawyer review — it provides a starting point, not a final product

## Related skills

- [[prompt-pack-vendor-data-protection-addendum]]
- [[prompt-pack-vendor-risk-assessment-questionnaire]]
- [[review-commercial-contract]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
- [[ref-verification]]
