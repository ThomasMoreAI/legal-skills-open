---
name: review-employment-contract-employer-side-sboghossian
title: Employment Contract Review — Employer Side
description: 'Use when an employer or their HR/legal counsel needs a red-flag review of an employment contract from the employer''s risk perspective — identifying compensation traps, IP assignment gaps, non-compete enforceability issues, termination-for-cause clarity, compliance with Saudization/Emiratization requirements, and confidentiality scope. MENA-first: UAE (FDL 33/2021), KSA Labor Law, Lebanon, DIFC, ADGM. Companion to the employee-side review skill; covers the same clauses from the opposite perspective.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-employment-contract-employer-side
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Employment Contract Review — Employer Side

Red-flag review of an employment contract from the employer's perspective. Identifies clauses that create unexpected liability, fail to adequately protect the employer's business interests, or do not comply with mandatory local employment law. Designed for HR teams, in-house counsel, and external employment lawyers reviewing offer letters and employment agreements.

## When to use this

- Before sending an employment contract to a new hire
- When updating a standard form to comply with new legislation (e.g., post-UAE FDL 33/2021 transition)
- During an M&A transaction — employment contract review is standard due diligence
- When an employee has raised a dispute and the employer needs to understand their contractual position
- When entering a new MENA jurisdiction and adapting a standard form to local requirements

## Required inputs

| Input | Required | Default |
|-------|----------|---------|
| Contract text | Yes | N/A |
| Jurisdiction / governing law | Yes | Infer from employer entity and work location |
| Employee's role and seniority | Useful | Assume mid-senior level |
| Is employee local national or expatriate? | Important | Affects Emiratization/Saudization and visa coupling |

## Review checklist — employer risk perspective

### 1. Compensation traps

**Ambiguous bonus formula**: the single most common source of employment disputes. Check:
- Is the bonus formula objective (clearly defined metrics, thresholds, and calculation) or subjective ("at the employer's discretion" / "subject to performance")? Subjective bonuses reduce liability but damage trust and retention
- Is there an "on-target earning" stated in the offer letter that does not appear in the contract? If so, this creates a potential claim that the OTE is contractual
- Deferred compensation / clawback: if the employer wants to claw back a bonus on early departure, the clawback provision must be explicit, with a clear trigger and repayment mechanism — courts in UAE and Lebanon are hostile to vague clawbacks
- Currency: if the contract is in USD but the payroll is in AED, specify the exchange rate mechanism

**UAE WPS compliance**: under the UAE Wage Protection System, salary must be paid by the 14th of the month following the pay period; delays trigger MOHRE fines. Ensure the contract specifies a payment date compatible with WPS.

### 2. IP assignment — employer protection

Check that the employer adequately protects its intellectual property:

- **Scope of assignment**: does the contract assign all IP created "in the course of employment" or "in connection with the employer's business"? The narrower the scope, the greater the risk that an employee argues a valuable creation falls outside it
- **Works for hire**: in common-law jurisdictions (DIFC, ADGM, UK, US), the concept of "work made for hire" vests IP automatically in the employer; in civil-law jurisdictions (UAE onshore, KSA, Lebanon), explicit assignment is more important
- **Moral rights**: in France and Lebanon, employees retain moral rights in their works even after economic rights are assigned — the employer cannot waive this on the employee's behalf. Plan accordingly (the employer can require the employee to exercise moral rights only in specified ways)
- **Pre-existing IP**: clearly identify any IP the employee brings to the role (to avoid an assignment clause inadvertently capturing it)
- **Post-employment duty**: employees who leave may argue that IP created after departure — using knowledge from the employer — is theirs. A specific post-employment IP clause should address this

### 3. Non-compete — practically enforceable?

The employer's interest: the non-compete must actually prevent the employee from joining a direct competitor or poaching key clients. The trap: many standard non-competes are drafted so broadly that they are unenforceable as a matter of law.

**UAE** (FDL 33/2021, Art. 10):
- Maximum 2 years duration — if longer, the excess is void
- Geographic scope must be reasonable — "the Middle East" for a junior analyst is likely excessive
- Financial compensation payment: Art. 10 requires that the employer pay compensation during the restricted period if it chooses to enforce the non-compete — failure to specify this renders enforcement uncertain
- The clause is only enforceable if the employee was exposed to business secrets or clients

**Employer best practice (UAE)**:
1. State the compensation payment (can be nominal, but must be specified)
2. Define "competing business" narrowly (specific activity types, not "any business")
3. Define geography to match the employee's actual market territory
4. Tie it to employees who have had access to trade secrets, key clients, or confidential pricing

**KSA** (Labor Law Art. 83):
- Same 2-year maximum
- Scope and geographic restriction must be proportionate to the employer's legitimate interest
- Compensation not required by law but courts apply a proportionality test: an unsupported global non-compete will be struck down

### 4. Confidentiality — trade secrets and customer lists

Check:
- Scope: does the clause cover trade secrets, customer lists, pricing, business strategies, technology, AND know-how? Omitting know-how is a common gap — employees carry knowledge, not just documents
- Duration: post-employment confidentiality for an indefinite period is generally enforceable for genuine trade secrets; a fixed post-employment period (2–3 years) is more pragmatic
- Customer lists: particularly important; an employee who leaves and calls on former clients using a memorized customer list may argue the confidentiality clause only covers written information
- "Deemed knowledge": add a clause stating that confidentiality obligations apply to information the employee knows to be confidential even if not labeled as such

### 5. Restrictive covenants — garden leave

Garden leave is a tool increasingly used in MENA practice (borrowed from English law):
- During a notice period, the employer pays the employee but asks them not to work
- The employee remains bound by their employment terms (IP, confidentiality) but is economically neutralized as a competitive threat
- UAE: generally permissible; the employer must pay full salary and benefits during garden leave
- KSA: permissible; MENA practitioners increasingly use it in senior employment agreements

Check: does the contract include a garden leave provision that protects the employer's interests during a notice period for a senior hire?

### 6. Termination for cause — list grounds clearly

**UAE FDL 33/2021 (Art. 44)** provides a statutory list of grounds for termination without notice (gross misconduct). The contract should:
- List specific grounds for termination for cause that are relevant to the role (fraud, misrepresentation, insubordination, breach of confidentiality, etc.)
- Align with the Art. 44 statutory grounds — cause listed in the contract must fall within or supplement the statutory categories
- Include a disciplinary procedure if required by company policy (failure to follow a fair procedure can result in wrongful dismissal liability even if the ground for termination was valid)

**KSA** (Labor Law Art. 80):
- Similar statutory list of grounds for termination without pay
- Employer must follow a formal dismissal procedure: written notification, allow defense
- Labor courts are employee-protective; vague cause or procedural failures result in re-instatement or compensation orders

### 7. Reduction in force

If the contract may be used for a mass layoff scenario, check:
- Notice period is reasonable and consistent across similar roles
- EOSB liability is correctly calculated (and the employer has provisioned for it)
- UAE: Article 43 FDL 33/2021 requires notice or pay in lieu; no "at-will" termination
- KSA: notice required; Labor Law Art. 75 permits termination for legitimate economic reasons with notice

### 8. Drug testing and fitness-for-work clauses

- UAE: employers in regulated sectors (aviation, healthcare, construction, oil & gas) may require periodic drug testing; include in the contract with reference to the applicable policy
- KSA: permitted; pre-employment drug test is standard for most professional roles
- Privacy considerations: any data collected in drug testing or health screening is personal data subject to UAE PDPL and KSA PDPL

### 9. Saudization / Emiratization compliance

**UAE Emiratization (Tawteen)**:
- For entities with 50+ employees, minimum Emiratization quotas apply by sector under the NAFIS program
- Employment contracts for non-UAE nationals should not conflict with Emiratization obligations (e.g., do not offer a contract term that would make it difficult to terminate a non-national if Emiratization adjustments are required)
- Visa coupling: expatriate employees' residence visa is tied to the employer; the employment relationship cannot be separated from the immigration status

**KSA Saudization (Nitaqat)**:
- All private-sector employers are assigned a Nitaqat band (Platinum, Green, Yellow, Red) based on their Saudi employment ratio
- Non-compliance (Yellow or Red band) restricts the employer's ability to: hire new foreign workers, renew existing work visas, extend commercial licenses
- Employment contracts for expatriate workers should include an acknowledgment that the employment relationship is subject to applicable Saudization requirements

### 10. Choice of law and dispute resolution

- **Mandatory application of local law**: UAE Labor Law (FDL 33/2021) and KSA Labor Law are mandatory statutes — their protections apply to employees working in those jurisdictions regardless of the governing law clause. A governing law clause choosing English law does not exempt the employer from UAE EOSB obligations
- **Dispute forum**: UAE employment disputes go to MOHRE conciliation, then Labor Court. Specify the applicable process
- **DIFC/ADGM entities**: subject to DIFC/ADGM Employment Law for employees employed by DIFC/ADGM entities; dispute resolution in DIFC/ADGM Courts or arbitration

## Output format

```json
{
  "findings": [
    {
      "clause": "Clause 7 — Bonus",
      "issue": "Bonus formula is 'at the employer's sole discretion' — creates ambiguity and reduces retention; OTE of X% stated in offer letter may be argued as contractual",
      "severity": "material",
      "riskExposure": "Employee may claim OTE as contractual if offer letter is interpreted as part of the employment terms",
      "suggestedRedline": "Replace discretionary bonus with defined performance target: 'Annual bonus of up to X% of base salary, subject to annual review against KPIs defined in Schedule 1'"
    }
  ],
  "riskExposure": "narrative summary of top 3 employer-side risks",
  "complianceGaps": ["Emiratization acknowledgment absent", "WPS payment date not specified"],
  "suggestedRedlines": ["list of specific drafting improvements"]
}
```

## Related skills

- [[review-employment-contract-employee-side]]
- [[review-contract-redline]]
- [[research-statute-lookup]]
- [[kb-employment-lb-ksa-uae]]
- [[review-compliance-gap-analysis]]
