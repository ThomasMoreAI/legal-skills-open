---
name: draft-employment-contract-lb-sboghossian
title: Employment Contract — Lebanon (LB)
description: Use when drafting a Lebanese employment contract under the Labor Code (Decree No. 207/1946 as amended) and Decree-Law No. 25/1976. Covers mandatory clauses, salary currency specification (LBP vs. USD critical post-2019), NSSF registration, indemnity calculation (Art. 50), grounds for termination with cause (Art. 74), probation (3 months), bilingual AR/EN format with Arabic controlling, and post-employment non-compete enforceability under Lebanese courts.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-employment-contract-lb
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: lb
practice: employment
language: en
---

# Employment Contract — Lebanon (LB)

## When to use this

Use this skill to draft a Lebanese law employment contract governed by the Labor Code (Decree No. 207 of 2 September 1946, as amended) and supplemented by Decree-Law No. 25/1976 on the Social Security Law (NSSF). The Labor Code applies to all employees in Lebanon except household workers (governed by separate ministerial decisions), agricultural workers, and certain liberal professions.

**Post-2019 crisis note:** Lebanon's economic collapse has made the specification of salary currency and actual payment mechanism the most commercially critical clause in any Lebanese employment contract. Many legacy contracts specified LBP salaries that have collapsed in real value by over 90% against USD. Any new contract must address currency, payment mechanism, and exchange-rate risk explicitly.

The contract must be drafted **bilingual Arabic/English**; Arabic controls in Lebanese courts and before the Ministry of Labor.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Employer (name, MOE registration, address, sector) | MOL compliance; NSSF registration | — |
| Employee (name, nationality, NSSF number or to be registered) | NSSF enrollment is mandatory | — |
| Role, reporting line, and location | Core contractual obligation | — |
| Salary (amount + **currency** + **payment method**) | Currency specification is critical post-crisis | — |
| Start date | Triggers probation, leave accrual, NSSF enrollment | — |
| Employment type (open-ended / fixed-term) | Determines notice and indemnity obligations | Open-ended default |

## Optional / typical inputs
- Working hours (default: 48 hours/week maximum per Labor Code)
- Probation period (default 3 months; maximum 3 months under Labor Code)
- Annual leave above statutory minimum
- Confidentiality and IP assignment (particularly important for creative/tech roles)
- Non-compete (if applicable; see below)

## Currency and payment — critical clause (post-2019)

Lebanon's monetary and banking crisis means that salary specification requires more precision than the standard "LBP X" formulation:

**Recommended approach:**
- State salary in USD (or other stable currency).
- State the payment method: bank transfer in fresh dollars (dollars on correspondent accounts), cash in USD, or LBP at official (BdL) or market exchange rate — specify which rate explicitly.
- If LBP is the agreed currency, include an indexation mechanism to protect against further LBP depreciation.

> "The Employee's monthly salary shall be USD [amount], payable in [cash in USD / fresh USD bank transfer / LBP at the daily Sayrafa/BdL platform rate on the date of payment]."

A contract that specifies only "LBP X" without an indexation or exchange-rate clause exposes the employee to real-wage collapse. Courts have generally been sympathetic to salary adjustment claims where the disparity is extreme.

## Mandatory clauses under LB Labor Code

### 1. Identification of parties
Full legal names, addresses, and capacity to contract.

### 2. Job description and duties
Scope of the role; core responsibilities. Courts interpret the contract strictly — assignment to substantially different duties without consent may constitute constructive dismissal.

### 3. Place of work
Specified location. Unilateral transfer to a different city or country without consent may be grounds for constructive dismissal.

### 4. Working hours
- Maximum: **48 hours per week** for adult employees (Labor Code Art. 31).
- Standard: 8 hours/day × 6 days, or equivalent arrangement.
- Overtime: permitted; rate = 1.5× regular hourly rate for overtime. Night-shift and holiday supplements apply.

### 5. Salary and method of payment
As described above — currency + amount + payment method. State the payment date (typically end of month or every two weeks).

### 6. Probation period
- Default and maximum: **3 months** under the Labor Code.
- During probation: either party may terminate without notice and without indemnity.
- After probation: termination requires notice and triggers indemnity obligations.

### 7. Notice period (Article 50)
Statutory minimum notice based on years of service:

| Years of service | Notice period |
|---|---|
| 3 months to 1 year | 1 month |
| 1 to 3 years | 2 months |
| 3 to 6 years | 3 months |
| 6 to 12 years | 4 months |
| Over 12 years | 6 months |

During the notice period, the employee continues working (pay-in-lieu of notice is permissible by agreement).

### 8. Grounds for termination with cause (Article 74)
The following are grounds for summary dismissal without notice or indemnity:
- False identity or falsified credentials at hiring.
- Disclosure of employer's trade secrets.
- Physical assault on employer, supervisor, or co-worker.
- Serious breach of workplace safety rules causing risk to life.
- Absence without justified reason for more than 10 consecutive or 15 non-consecutive days within a calendar year.
- Final criminal conviction for a crime involving dishonesty.
- Gross negligence causing serious material harm to the employer.

If the employer terminates for cause outside these grounds, Lebanese courts typically reclassify the termination as wrongful and award indemnity.

### 9. End-of-service indemnity (Article 50)

Mandatory for open-ended contracts terminated by the employer without cause (or by employee resignation with cause):

| Years of service | Indemnity |
|---|---|
| First 5 years | 1 month salary per year |
| After 5 years | 0.5 month salary per year |

Calculation base: last salary (all components).

**Cap**: indemnity is capped at 12 months' salary under Lebanese law (though courts have at times awarded above-cap amounts in egregious dismissal circumstances).

Note: employees enrolled in the NSSF end-of-service scheme (طابع الصندوق الوطني للضمان الاجتماعي) receive both NSSF end-of-service entitlement (employer contributes 8.5% of salary monthly) and the statutory indemnity, which may be reduced by the NSSF amount already paid.

### 10. NSSF registration acknowledgment
The employer must enroll the employee in the National Social Security Fund (NSSF) within 3 months of hire. NSSF branches:
- **Sickness and maternity branch**: employer 7% + employee 2% of salary.
- **Family allowances branch**: employer 6% of salary.
- **End-of-service branch**: employer 8.5% of salary.

Include an acknowledgment of enrollment and the parties' contribution obligations.

### 11. Governing law
"This Agreement is governed by and construed in accordance with the laws of Lebanon, and in particular the Lebanese Labor Code and Decree-Law No. 25/1976."

## Foreign employees

- Foreign employees require a **work permit** (Ministry of Labor), a **residence permit** (General Security / Sécurité Générale), and labor clearance.
- Work permits are subject to kafala-equivalent sponsorship by the employer in practice.
- Specify dependency: "This Agreement is conditional upon the Employee obtaining and maintaining a valid work and residence permit throughout the Term."
- Palestinian and Syrian nationals are subject to specific labor restrictions; seek specialist advice.

## Non-compete clause

Lebanese courts enforce non-compete clauses that satisfy all of:
- **Specific scope** — limited to the employer's actual business activity, not an entire industry.
- **Limited territory** — Lebanon, or a specific region; national bans are scrutinized.
- **Time-limited** — typically 1–2 years post-employment.
- **Legitimate business interest** — protecting confidential information, customer relationships, or specialized training.
- **Not oppressive** — must not prevent the employee from earning a living entirely.

Draft as a separate clause; include severability so that a court narrowing the scope does not void the entire clause.

## IP assignment and confidentiality

For technology, creative, or legal roles:
- Include an IP assignment clause: all work-product created in connection with employment is assigned to the employer from creation.
- Include a confidentiality clause covering trade secrets, client data, pricing, and business strategy.
- Post-employment confidentiality for trade secrets is enforceable under general civil-law principles even without a specific clause.

## Bilingual format

Contract must be bilingual Arabic-English:
- Side-by-side format (Arabic column / English column): preferred for court readability.
- Sequential format (full Arabic text followed by full English text) is also common.
- All defined terms capitalized in both languages.
- Arabic version controls in all court proceedings and before the Ministry of Labor.

Use [[draft-bilingual-ar-en-side-by-side]] for formatting guidance and [[heuristic-bilingual-ar-en-mirror-clauses]] for clause-by-clause translation consistency.

## Common mistakes

1. **Salary in LBP only** — post-2019 economic crisis; LBP salary without USD peg or indexation has collapsed. Employees now routinely challenge purely LBP-denominated contracts.
2. **Wrong indemnity calculation base** — use the last paid salary (all components); do not use only basic salary.
3. **Probation period exceeding 3 months** — exceeds the Labor Code maximum; any excess is void and the employer bears full notice and indemnity obligations from day 91.
4. **Summary dismissal for causes not on the Art. 74 list** — employers routinely terminate "for cause" on behavioral grounds not enumerated; courts award indemnity.
5. **No NSSF enrollment** — regulatory violation; also exposes employer to employee claims for unpaid NSSF benefits.
6. **Non-compete without territorial limit** — courts in Lebanon scrutinize broad clauses; include a specific territory.
7. **English-only contract** — not filed at Ministry of Labor; not enforced by Lebanese courts.

## Related skills

- [[kb-employment-law-lb]] — Lebanese labor law reference pack with updated statutory thresholds
- [[draft-employee-handbook]] — workplace policies document that supplements this contract
- [[draft-bilingual-ar-en-side-by-side]] — bilingual formatting skill
- [[heuristic-bilingual-ar-en-mirror-clauses]] — quality check for bilingual clause consistency
- [[draft-employment-contract-ksa]] — KSA employment contract for comparison
