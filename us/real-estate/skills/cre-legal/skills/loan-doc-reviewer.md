---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Loan Document Reviewer

Reviews all acquisition loan documents against the term sheet, identifies restrictive covenants and borrower obligations, flags deviations unfavorable to the borrower, and produces a prioritized negotiation agenda.

---

## When to Use This Skill

Use this skill when you have received draft or final loan documents for a CRE acquisition and need to compare them against the agreed term sheet, understand the full scope of borrower obligations, and identify provisions worth negotiating. It is appropriate for any loan type — conventional bank, agency (Fannie/Freddie), CMBS, life company, or bridge — whenever you need a systematic review of the loan agreement, note, mortgage, guaranty, and related documents.

---

## What You'll Need to Provide

- The term sheet or commitment letter (or a summary of agreed loan terms)
- The full loan agreement / credit agreement (or key sections)
- The promissory note
- The mortgage or deed of trust
- The guaranty agreement (if applicable)
- The environmental indemnity (if applicable)
- The cash management or lockbox agreement (if applicable)
- Lender name, loan amount, property address, and deal entity information
- Any financing phase analysis or underwriting outputs already completed

---

## Mission

Review all loan documents for the acquisition financing. Ensure alignment with the term sheet, identify restrictive covenants, flag borrower obligations, and surface any deviations that could adversely affect the borrower. Produce a comprehensive analysis that enables informed negotiation of loan document terms.

---

## Strategy

### Step 1: Review Loan Commitment Letter vs. Term Sheet
- Line-by-line comparison of all material terms
- Verify: loan amount, interest rate (fixed/floating, spread, index, floor), maturity date, extension options, prepayment provisions, recourse structure
- Identify any term that changed between commitment and final docs
- Flag any new terms not in the original commitment
- Verify conditions precedent to closing are achievable

### Step 2: Analyze Loan Agreement Provisions
- **Financial Covenants**:
  - DSCR maintenance (threshold, calculation methodology, testing frequency)
  - Debt yield test (threshold, calculation)
  - LTV covenant (if applicable, revaluation triggers)
  - Net worth / liquidity requirements for guarantor
- **Reporting Requirements**:
  - Annual financials (audited vs. unaudited, delivery deadline)
  - Quarterly operating statements
  - Rent roll delivery schedule
  - Annual budget approval process
  - Certificate of compliance delivery
- **Cash Management / Lockbox Provisions**:
  - Lockbox type (hard lockbox vs. soft lockbox vs. springing)
  - Cash sweep triggers (DSCR trigger, debt yield trigger, event of default)
  - Cash sweep mechanics (excess cash flow definition, sweep percentage)
  - Cash trap vs. cash sweep distinction
- **Reserve Requirements**:
  - Tax reserves (monthly escrow amount)
  - Insurance reserves (monthly escrow amount)
  - Capital expenditure reserves (per unit/per SF, annual cap)
  - Replacement reserves
  - Tenant improvement / leasing commission reserves (if applicable)
  - Seasonality reserves (if applicable)
  - Upfront reserves at closing

### Step 3: Review Promissory Note
- Payment terms: P&I vs. IO, payment dates, late charge provisions
- Interest rate mechanics: index, spread, floor, cap (if floating)
- Default interest rate (spread over contract rate)
- Cure periods for payment defaults vs. non-payment defaults
- Acceleration provisions
- Prepayment: lockout period, yield maintenance, defeasance, step-down schedule
- Application of payments (interest first, then principal, then fees)

### Step 4: Review Mortgage / Deed of Trust
- Property description matches title commitment and survey
- Assignment of rents and leases
- Fixture filing provisions
- Due-on-sale / due-on-encumbrance clauses
- Permitted transfers and exceptions
- Insurance and condemnation proceeds application
- Environmental covenants in the mortgage

### Step 5: Review Guaranty Agreement
- **Scope**: Full recourse, partial recourse, non-recourse with carve-outs
- **Non-Recourse Carve-Outs ("Bad Boy" Provisions)**:
  - Springing full recourse triggers (voluntary bankruptcy filing, fraud, prohibited transfer, environmental)
  - Loss-based carve-outs (waste, misapplication of rents/insurance/condemnation proceeds)
  - Identify which carve-outs are "springing" (full recourse) vs. "loss" (limited to actual loss)
- **Burn-Off Provisions**: Does guaranty reduce over time? (DSCR achievement, LTV reduction, seasoning)
- **Guarantor Obligations**: Net worth maintenance, liquidity requirements, financial reporting
- **Permitted Guarantor Transfers**: Can guaranty be transferred to replacement guarantor?

### Step 6: Review Environmental Indemnity
- Scope of indemnification (known vs. unknown contamination)
- Survival (typically survives loan payoff)
- Carve-outs and limitations
- Relationship to environmental insurance (if any)
- Testing and remediation obligations

### Step 7: Review Lockbox and Cash Management Trigger Events
- Specific trigger events and cure provisions
- DSCR / debt yield trigger levels and cure thresholds
- Duration of cash management period once triggered
- Mechanics of cash sweep (daily sweep, monthly sweep)
- Release conditions for trapped cash
- Impact on distributions to equity

### Step 8: Identify Most Restrictive Covenants
- Rank all covenants by restrictiveness
- Model impact on operations (reporting burden, distribution restrictions)
- Identify covenants likely to be triggered in downside scenarios
- Assess cure mechanics and feasibility
- Compare against market standards for similar loan products

### Step 9: Flag Term Sheet Deviations
- Create detailed comparison table: term sheet vs. final documents
- Categorize deviations: favorable to borrower, neutral, unfavorable to borrower
- Prioritize deviations for negotiation
- Assess materiality of each deviation
- Note any oral agreements not reflected in documents

---

## Output Format

```json
{
  "loan_doc_review": {
    "metadata": {
      "review_date": "{date}",
      "lender": "{lender_name}",
      "loan_amount": "{amount}",
      "loan_type": "{fixed/floating, recourse/non-recourse}"
    },
    "term_sheet_comparison": [
      {
        "term": "{term_name}",
        "term_sheet_value": "{value}",
        "final_doc_value": "{value}",
        "deviation": "none / favorable / neutral / unfavorable",
        "materiality": "low / medium / high",
        "section_reference": "{doc and section}",
        "negotiation_priority": "critical / important / minor"
      }
    ],
    "covenant_summary": {
      "financial_covenants": [
        {
          "covenant": "{name}",
          "threshold": "{value}",
          "testing_frequency": "{frequency}",
          "cure_mechanism": "{description}",
          "consequence_of_breach": "{description}",
          "market_comparison": "tighter / market / looser"
        }
      ],
      "reporting_covenants": [
        {
          "requirement": "{description}",
          "frequency": "{frequency}",
          "delivery_deadline": "{days after period end}",
          "format": "{audited/unaudited/certified}"
        }
      ]
    },
    "reserve_requirements": [
      {
        "reserve_type": "{type}",
        "monthly_amount": "{amount}",
        "upfront_amount": "{amount}",
        "release_conditions": "{description}",
        "total_annual_impact": "{amount}"
      }
    ],
    "cash_management": {
      "lockbox_type": "{hard/soft/springing}",
      "trigger_events": [
        {
          "trigger": "{description}",
          "threshold": "{value}",
          "cure_provision": "{description}",
          "cure_threshold": "{value}"
        }
      ],
      "sweep_mechanics": "{description}",
      "distribution_impact": "{description}"
    },
    "guaranty_scope": {
      "type": "{full/partial/non-recourse with carve-outs}",
      "guarantor": "{entity/individual}",
      "springing_recourse_triggers": [
        {
          "trigger": "{description}",
          "consequence": "full recourse / loss-based"
        }
      ],
      "burn_off_provisions": "{description or N/A}",
      "guarantor_financial_requirements": {
        "net_worth": "{amount}",
        "liquidity": "{amount}"
      }
    },
    "non_recourse_carve_outs": {
      "springing_full_recourse": [
        "{description}"
      ],
      "loss_based": [
        "{description}"
      ]
    },
    "restrictive_provisions": [
      {
        "provision": "{description}",
        "document": "{doc name}",
        "section": "{section}",
        "restrictiveness": "moderate / high / very high",
        "operational_impact": "{description}",
        "market_standard": "yes / no"
      }
    ],
    "risk_flags": [
      {
        "flag": "{description}",
        "severity": "low / medium / high / critical",
        "document": "{doc name}",
        "section": "{section}",
        "recommendation": "{action}"
      }
    ],
    "recommended_negotiations": [
      {
        "provision": "{description}",
        "current_language": "{summary}",
        "requested_change": "{description}",
        "priority": "must-have / important / nice-to-have",
        "rationale": "{why}",
        "market_justification": "{basis}"
      }
    ],
    "uncertainty_flags": [
      {
        "field_name": "",
        "reason": "estimated | assumed | unverified | stale_data | interpolated",
        "impact": "Description of what downstream analysis this affects"
      }
    ]
  }
}
```

---

## Quality Checks

Before finalizing output, verify:

1. **Schema Compliance** — All required output fields are present, non-null, and correctly typed
2. **Numeric Sanity** — Loan amount, interest rate, and reserve amounts are positive and consistent with financing terms provided
3. **Cross-Reference Validation** — Loan amount and terms match commitment letter/term sheet provided
4. **Completeness Assessment** — Every strategy step produced output or a noted data gap
5. **Confidence Scoring** — Set `confidence_level` and populate `uncertainty_flags` for any estimated or assumed values

**Self-Validation field checks:**

| Field | Valid Range | Flag If |
|-------|-----------|---------|
| loanAmount | > 0, match term sheet | Mismatch |
| interestRate | Match term sheet | Mismatch |
| loanTerm | Match term sheet | Mismatch |
| prepaymentTerms | Must be documented | Missing |
| guarantyType | FULL_RECOURSE, PARTIAL_RECOURSE, NON_RECOURSE | Invalid value |
| covenants | At least DSCR covenant present | Missing DSCR covenant |

**Validation checks:**

| Check | Method |
|-------|--------|
| All loan documents reviewed | Every document type has analysis output |
| Term sheet comparison complete | Every material term has a comparison entry |
| All covenants catalogued | Cross-reference covenant list with loan agreement sections |
| Guaranty fully analyzed | Carve-outs, burn-off, and requirements all addressed |
| Reserve calculations accurate | Monthly and upfront amounts sum correctly |
| Cash management triggers identified | All trigger events documented with cure provisions |
| Negotiations prioritized | Every recommended change has priority and rationale |

---

## Red Flags & Dealbreakers

While this review does not typically surface acquisition-level dealbreakers, treat the following as CRITICAL findings requiring immediate escalation:

- Loan terms that materially and adversely differ from the term sheet with no explanation
- Springing full recourse triggers that are unusually broad or easily triggered
- Environmental indemnity with no survival limitation and no connection to known contamination
- Cash management provisions that effectively eliminate all equity distributions in normal operating conditions
- Guaranty burn-off conditions that are practically unachievable given the property's underwritten performance

Flag any such finding with severity "CRITICAL" and include a specific recommended negotiation point.

---

## When Data is Missing

When loan documents, term sheet, or financing analysis are incomplete:

1. **Attempt a workaround** — Use market-standard terms for the loan type as a comparison baseline; note the assumption
2. **Note the assumption** — Document any assumed term, including its market basis and confidence level
3. **Mark in output** — Add an entry to `uncertainty_flags` with the field name, reason, and impact on analysis
4. **Continue analysis** — Do not halt for missing individual documents; complete analysis on available documents and list missing documents as data gaps
5. **Flag for attorney review** — Do not assume favorable interpretations of missing or ambiguous loan document provisions

---

## Confidence Scoring

Apply confidence levels to all findings:

| Level | Criteria |
|-------|----------|
| **HIGH** | Based on verified loan document text; no assumptions; term directly observed and unambiguous |
| **MEDIUM** | Based on partially available documents; minor assumptions made; some interpretation required |
| **LOW** | Based on term sheet only or summarized information; full documents not available |

Set `confidence_level` in the output and populate `uncertainty_flags` for any finding rated MEDIUM or LOW.

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- [Lender Criteria](knowledge/lender-criteria.md) for market-standard DSCR thresholds, reserve requirements, and covenant benchmarks by loan type
- [Legal Checklist](knowledge/legal-checklist.md) for a master list of lender closing conditions and required deliverables
- [CRE Risk Scoring Framework](knowledge/risk-scoring.md) for severity rating guidance on covenant breaches and restrictive provisions
- [Underwriting Calculations](knowledge/underwriting-calc.md) for DSCR and debt yield calculation methodology

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
