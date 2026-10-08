---
name: review-employment-contract-employee-side-sboghossian
title: Employment Contract Review — Employee Side
description: 'Use when an employee or their counsel needs a red-flag review of an employment contract — identifying clauses that are unfavorable, unlawful, or below the statutory floor across MENA jurisdictions. Covers compensation structure, benefits (including MENA-specific allowances and EOSB), contract term, notice periods, non-compete enforceability, IP assignment scope, probation limits, and confidentiality. Jurisdiction-first: UAE (FDL 33/2021), KSA (Labor Law), Lebanon, DIFC, ADGM.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-employment-contract-employee-side
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Employment Contract Review — Employee Side

Red-flag review of an employment contract from the employee's perspective. Identifies clauses that are below the statutory floor, disproportionately restrictive, or unclear in ways that disadvantage the employee. Flags negotiation levers and suggests redlines.

## When to use this

- An employee (or their family / legal adviser) has received an offer contract and wants it reviewed before signing
- A recruit is concerned about non-compete scope before leaving a prior employer
- An employee is reviewing terms before accepting a promotion with a new agreement
- An HR professional needs to verify that an employee-facing contract meets the statutory floor in a new jurisdiction

## Required inputs

| Input | Required | Default if not provided |
|-------|----------|------------------------|
| Contract text | Yes | N/A |
| Jurisdiction / governing law | Yes | Infer from employer entity location and employee's work location |
| Employee's role and seniority | Useful | Assume junior-to-mid-level for statutory floor checks |
| Is there a pre-existing relationship? | Useful | Assume new hire |

## Review checklist — clause by clause

### 1. Compensation: base salary

- Is the base salary expressed in clear currency? In MENA, specify AED / SAR / LBP / USD; vague references to "market rate" are not acceptable
- Is the salary expressed monthly or annually? — confirm whether the formula is correct (monthly × 12)
- Does the employment contract reference salary that differs from the offer letter? Discrepancy is a red flag
- **UAE**: minimum wage requirements are sector-specific and nationality-specific; check compliance with MOHRE wage protection system (WPS)
- **KSA**: minimum wage for Saudi nationals (Nitaqat); no general minimum wage for expatriates, but common practice sets floors

### 2. Variable compensation (bonus / commission)

This is a high-risk area for disputes. Check:
- Is the bonus formula precisely defined, or is it "at the employer's discretion"? A discretionary bonus is worth little legally
- What are the conditions for entitlement? Are they objective (KPIs hit) or subjective (manager approval)?
- Is a pro-rata bonus owed on termination? If so, when? (Note: UAE FDL 33/2021 does not create a statutory right to pro-rata bonus unless the contract specifies it)
- Currency: bonus should be in the same currency as base salary
- **UAE red flag**: many UAE offer letters quote an "on-target" bonus as if it is guaranteed; the contract may say "discretionary" — the discrepancy is a dispute waiting to happen

### 3. Benefits

Standard MENA employment benefits checklist:

| Benefit | UAE standard | KSA standard | Lebanon standard |
|---------|-------------|--------------|-----------------|
| Housing allowance | Often included (25–30% of base) or in-kind housing; check whether included in basic salary (affects EOSB) | Common for expatriates | Less common; salary typically inclusive |
| Transport allowance | Common (AED 500–2,000/month) | Common | Less common |
| Annual air ticket | Standard for expatriates (home-country + family) | Standard for expatriates | Less common |
| Education allowance (children) | Common for senior roles | Common for senior roles | Rare |
| Health insurance | Mandatory in Dubai (DHA) and Abu Dhabi (DOH) for all employees | Mandatory under CCHI / SAMA for private sector | Not mandatory but common |
| End-of-Service Benefit (EOSB) — see below | Statutory: cannot contract out | Statutory | Statutory |

**UAE EOSB note**: EOSB is calculated on "basic wage" — not all-inclusive salary. Employers sometimes structure packages with a low basic salary and high allowances specifically to reduce EOSB liability. The employee should check whether the "basic wage" is the total package or a subset.

### 4. Contract term: fixed vs unlimited

**UAE (post FDL 33/2021)**: All UAE private sector contracts are fixed-term, automatically renewed for the same term unless notice is given. The concept of "unlimited" contracts was abolished by FDL 33/2021 (effective February 2022). Maximum initial term: 3 years; renewable.

**Practical impact**: Under FDL 33/2021, early termination of a fixed-term contract by the employer (other than for cause) triggers compensation. The employee should check:
- What is the stated contract term?
- What are the employer's early-termination rights?
- Is there a compensation formula for early termination?

**KSA**: Fixed-term contracts renew for the same term on expiry; unlimited contracts require notice for termination. KSA Labor Law applies to both.

### 5. Notice period

Standard commercial notice period is 30 days (1 month) in UAE (FDL 33/2021, Art. 43), though contracts may specify longer periods. In KSA, 60 days is the standard for contracts of 2+ years; shorter for newer employees.

Check:
- Is notice required from **both** sides (mutual), or only from the employee?
- Is the employer's notice period the same as the employee's? Asymmetry may be acceptable but should be negotiated
- Can the employer pay in lieu of notice? (Typically yes; employee should confirm)
- Is garden leave available? (If employer pays during notice but suspends duties, the employee cannot work elsewhere)

### 6. Non-compete (post-employment restriction)

This is consistently the highest-risk clause for employees:

| Jurisdiction | Maximum duration | Maximum geographic scope | Consideration required |
|---|---|---|---|
| UAE (FDL 33/2021, Art. 10) | 2 years from termination | Reasonable scope per role | Financial compensation for the restriction period |
| KSA (Labor Law Art. 83) | 2 years from termination | Reasonable scope | Not explicitly required; courts apply proportionality |
| Lebanon | Not codified; courts apply proportionality | | |
| DIFC (DIFC Employment Law) | No statutory cap; reasonableness test applies | Reasonable | Not required but affects reasonableness |
| ADGM | No statutory cap; reasonableness test | Reasonable | |

**Employee-side red flags**:
- Duration exceeds statutory maximum → automatically void/reduceable in UAE
- Geographic scope covers the entire world or an entire industry without nexus to the employee's actual role
- No compensation payment specified (UAE: compensation is required — its absence may make the clause unenforceable)
- Restriction covers activities the employee was never actually involved in at this employer
- Restriction triggered by any termination, including wrongful dismissal by the employer

**Negotiation lever**: in UAE, if the employer fails to specify a compensation payment, the employee can argue the clause is unenforceable or negotiate that the restriction applies only if the employer chooses to enforce it (by paying).

### 7. IP assignment

Check the scope of IP assigned to the employer:

- Does it cover only work created **in the scope of employment**, or everything created **during employment** (including personal projects)?
- Does it purport to assign IP in inventions not related to the employer's business? This may be void or unenforceable
- Moral rights: in civil-law jurisdictions (Lebanon, France), moral rights cannot be assigned; any clause purporting to do so is ineffective
- **UAE**: UAE Federal Law No. 38 of 2021 on Copyright provides that works created by an employee in the course of employment belong to the employer, but the employee retains moral rights
- Pre-existing IP: should be expressly carved out if the employee brings IP into the role (e.g., a developer with prior open-source contributions)

### 8. Probation period

| Jurisdiction | Maximum probation | Rules |
|---|---|---|
| UAE (FDL 33/2021, Art. 9) | 6 months | Can be reduced but not extended beyond 6 months; notice during probation: 14 days for employee to employer; 1 month for employer to employee |
| KSA (Labor Law Art. 53) | 90 days | May not be extended; counts as part of employment for EOSB |
| Lebanon | Not codified; market practice 3 months | |
| DIFC | No statutory maximum; must be reasonable | |

Check: does the contract specify a probation period longer than the statutory maximum? If so, the excess is void.

### 9. EOSB (End-of-Service Benefit / Gratuity)

EOSB is a statutory entitlement in UAE, KSA, and Lebanon — the equivalent of a mandatory severance gratuity:

**UAE** (FDL 33/2021, Art. 51):
- 21 days' basic wage per year for the first 5 years
- 30 days' basic wage per year for each year beyond 5 years
- Payable on any termination (except termination for cause under Art. 44)
- Calculated on basic wage only (not allowances)

**KSA** (Labor Law Art. 84):
- Employee who resigns after 2 years: 1/3 of 10-day wage per year for years 2–5; 2/3 for years 5–10; full for years 10+
- Employee terminated by employer: full 10-day wage per year of service
- Calculated on last wage

**Lebanon** (Labor Law Art. 54):
- 1 month's wage per year of service
- Payable on termination; complex rules for resignation timing

Check: does the contract attempt to contract out of EOSB or offer a lesser amount? **Any clause reducing EOSB below the statutory floor is void** — the statutory floor cannot be waived.

### 10. Governing law and forum

- Is the governing law specified?
- **UAE**: even if a foreign governing law is chosen, mandatory UAE Labor Law provisions apply if the employee works in UAE — cannot be contracted out of
- **DIFC**: DIFC Employment Law applies to DIFC-registered employers regardless of governing law clause
- **Forum**: disputes under UAE onshore employment contracts typically go to the MOHRE and then Labor Court; check whether the contract specifies a different forum

## Output format

```json
{
  "findings": [
    {
      "clause": "Clause 5 — Non-Compete",
      "issue": "Duration is 3 years — exceeds UAE FDL 33/2021 Art. 10 maximum of 2 years",
      "severity": "critical",
      "legalBasis": "Federal Decree-Law No. 33 of 2021, Article 10",
      "suggestedRedline": "Reduce duration to 24 months from the Termination Date"
    }
  ],
  "negotiationLevers": [
    "Non-compete compensation payment: not specified — request clarification or deletion",
    "Bonus: change 'discretionary' to 'target of X% subject to performance review with defined KPIs'"
  ],
  "statutoryFloorIssues": [
    "EOSB calculation based on all-in salary, not basic salary — corrected formula required"
  ]
}
```

## Related skills

- [[review-employment-contract-employer-side]]
- [[review-contract-redline]]
- [[research-statute-lookup]]
- [[kb-employment-lb-ksa-uae]]
