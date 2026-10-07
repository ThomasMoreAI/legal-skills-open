---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Insurance Coordinator

Determines required insurance coverage types for a CRE acquisition, verifies lender compliance, identifies coverage gaps, estimates annual premiums for the underwriting model, and tracks the binding timeline to ensure all policies are in place at closing.

---

## When to Use This Skill

Use this skill when you need to coordinate property and liability insurance for a commercial real estate acquisition. It is appropriate when you have received a loan commitment with insurance requirements, when you need to build an insurance cost estimate for the underwriting pro forma, or when you need a systematic checklist confirming that all required coverage types will be bound before closing.

---

## What You'll Need to Provide

- Property address, property type (multifamily, office, retail, industrial), unit count or square footage, year built, and construction type (frame, masonry, steel, concrete)
- The loan commitment letter or lender insurance requirements (coverage types required, minimum limits, maximum deductibles, required endorsements, acceptable carrier ratings)
- Environmental review findings: flood zone designation, contamination findings, and any environmental risk factors
- Property condition report findings: structural issues, mechanical systems age, roof condition, deferred maintenance
- Any existing insurance policy (coverage summary or declarations page), if available
- Anticipated closing date and the lender's evidence of insurance deadline

---

## Mission

Coordinate property and liability insurance for the acquisition. Ensure lender requirements are met, identify coverage gaps, and coordinate binding. Produce accurate insurance cost estimates for the underwriting model and confirm all policies are in place prior to closing.

---

## Strategy

### Step 1: Determine Required Coverage Types
Based on property type, location, and lender requirements, compile the full list of required insurance:

| Coverage Type | Requirement Basis | Typical Requirement |
|---------------|-------------------|---------------------|
| **Property / Hazard** | Lender + prudent ownership | Replacement cost value |
| **General Liability** | Lender + prudent ownership | $1M per occurrence / $2M aggregate |
| **Umbrella / Excess Liability** | Lender requirement | $5M-$25M depending on asset size |
| **Flood Insurance** | Mandatory if in SFHA Zone A/V | NFIP or private flood policy |
| **Earthquake** | Lender / regional requirement | Required in seismic zones |
| **Environmental / Pollution** | Environmental review findings | If contamination risk identified |
| **Loss of Rents / Business Income** | Lender requirement | 12-18 months rental income |
| **Workers Compensation** | State law (if employees on-site) | Statutory limits |
| **Boiler & Machinery** | Property condition / lender | Equipment breakdown coverage |
| **Builder's Risk** | If renovation planned | Construction cost coverage |
| **Terrorism (TRIA)** | Lender requirement | Often required on larger assets |

### Step 2: Research Insurance Requirements
- **Lender-Specific Requirements**:
  - Minimum coverage amounts per coverage type
  - Maximum allowable deductibles
  - Named insured requirements (borrower entity, lender, servicer)
  - Required endorsements (loss payee, additional insured, notice of cancellation)
  - Acceptable carrier ratings (typically A.M. Best A- / VII or better)
  - Evidence of insurance delivery deadlines (usually 10+ days before closing)
- **State-Specific Requirements**:
  - Mandatory coverage types
  - Minimum limits
  - State-specific endorsements
  - Insurance regulatory requirements

### Step 3: Research Insurance Benchmarks
Gather benchmark data to support premium estimates:
- Typical property insurance premium per unit for asset class and region
- Typical liability premium per unit
- Flood insurance rates by zone
- Recent premium trends for property type and geography
- Carrier market conditions (hard market vs. soft market indicators)

Benchmark sources:
- Insurance industry reports by property type
- Regional premium surveys
- NFIP flood insurance rate tables
- State insurance department rate filings

### Step 4: Identify Coverage Gaps from Current Policy
If existing insurance information is available:
- Compare current coverage limits to lender requirements
- Compare current coverage limits to replacement cost estimate
- Identify any missing coverage types
- Note current carrier and rating
- Assess current deductible levels vs. lender maximums
- Flag any policy exclusions that create exposure

### Step 5: Coordinate Lender Endorsements
Prepare endorsement requirements for the insurance broker:
- **Mortgagee / Loss Payee Clause**: Lender name and address as shown in loan documents
- **Additional Insured**: Lender, servicer, and any other required parties
- **Notice of Cancellation**: 30-day prior written notice (10 days for non-payment)
- **Waiver of Subrogation**: If required by lender
- **Replacement Cost Endorsement**: No coinsurance penalty
- **Agreed Amount Endorsement**: Waive coinsurance clause
- **Inflation Guard**: Automatic coverage increase
- Compile lender endorsement requirements into a checklist for the broker

### Step 6: Verify Flood Zone Status and Flood Insurance
- Confirm FEMA flood zone designation from survey and FEMA maps
- If in Special Flood Hazard Area (Zone A or V):
  - NFIP coverage required (or approved private alternative)
  - Maximum NFIP limits may require excess flood coverage
  - Lender must receive flood determination certificate
- If outside SFHA but within 500-year zone:
  - Evaluate whether flood coverage is prudent even if not required
- If LOMA/LOMR application is pending, note status
- Calculate flood insurance cost estimate

### Step 7: Estimate Annual Insurance Costs
Build insurance cost estimate for the underwriting model:

```
insurance_cost_estimate:
  property_insurance:
    replacement_cost: "{estimated RCV}"
    rate_per_100: "{rate}"
    annual_premium: "{amount}"
  general_liability:
    annual_premium: "{amount}"
  umbrella:
    annual_premium: "{amount}"
  flood:
    annual_premium: "{amount or N/A}"
  earthquake:
    annual_premium: "{amount or N/A}"
  environmental:
    annual_premium: "{amount or N/A}"
  loss_of_rents:
    annual_premium: "{amount}"
  workers_comp:
    annual_premium: "{amount or N/A}"
  boiler_machinery:
    annual_premium: "{amount}"
  terrorism:
    annual_premium: "{amount or N/A}"

  total_annual_insurance: "{sum}"
  per_unit_annual: "{total / units}"
  per_sf_annual: "{total / sf}"
```

---

## Output Format

```json
{
  "insurance_coordination_report": {
    "metadata": {
      "report_date": "{date}",
      "property": "{property name/address}",
      "property_type": "{multifamily/office/retail/industrial}",
      "units_or_sf": "{N units or N SF}",
      "year_built": "{year}",
      "construction_type": "{frame/masonry/steel/concrete}"
    },
    "required_coverage_checklist": [
      {
        "coverage_type": "{type}",
        "required": "yes / no / conditional",
        "requirement_source": "lender / state law / prudent ownership / environmental",
        "minimum_amount": "{amount or limit}",
        "maximum_deductible": "{amount}",
        "status": "quoted / bound / pending / not needed",
        "notes": "{additional details}"
      }
    ],
    "estimated_premiums": {
      "property_hazard": {
        "replacement_cost_value": "{amount}",
        "estimated_annual_premium": "{amount}",
        "rate_basis": "{per $100 RCV or flat}"
      },
      "general_liability": {
        "limits": "{per occurrence / aggregate}",
        "estimated_annual_premium": "{amount}"
      },
      "umbrella_excess": {
        "limit": "{amount}",
        "estimated_annual_premium": "{amount}"
      },
      "flood": {
        "zone": "{FEMA zone}",
        "required": "yes/no",
        "estimated_annual_premium": "{amount or N/A}"
      },
      "earthquake": {
        "required": "yes/no",
        "estimated_annual_premium": "{amount or N/A}"
      },
      "environmental": {
        "required": "yes/no",
        "estimated_annual_premium": "{amount or N/A}"
      },
      "loss_of_rents": {
        "coverage_period": "{months}",
        "estimated_annual_premium": "{amount}"
      },
      "workers_comp": {
        "required": "yes/no",
        "estimated_annual_premium": "{amount or N/A}"
      },
      "boiler_machinery": {
        "estimated_annual_premium": "{amount}"
      },
      "terrorism": {
        "required": "yes/no",
        "estimated_annual_premium": "{amount or N/A}"
      },
      "builder_risk": {
        "required": "yes/no",
        "estimated_premium": "{amount or N/A}"
      },
      "total_estimated_annual": "{sum}",
      "per_unit_annual": "{amount}",
      "per_sf_annual": "{amount}",
      "benchmark_comparison": "below / at / above market"
    },
    "lender_requirement_compliance": [
      {
        "requirement": "{description}",
        "lender_minimum": "{value}",
        "proposed_coverage": "{value}",
        "compliant": "yes / no / pending",
        "action_needed": "{description or none}"
      }
    ],
    "lender_endorsements": [
      {
        "endorsement": "{name}",
        "lender_requirement": "{specific language}",
        "status": "ordered / received / pending"
      }
    ],
    "coverage_gaps": [
      {
        "gap": "{description}",
        "risk_level": "low / medium / high",
        "recommendation": "{action}",
        "cost_to_close_gap": "{estimated amount}"
      }
    ],
    "flood_zone_analysis": {
      "fema_zone": "{zone}",
      "flood_insurance_required": "yes/no",
      "nfip_coverage": "yes / no / N/A",
      "excess_flood_needed": "yes/no",
      "loma_pending": "yes/no",
      "flood_determination_certificate": "ordered / received / N/A"
    },
    "binding_timeline": {
      "evidence_of_insurance_deadline": "{date}",
      "quote_deadline": "{date}",
      "binder_deadline": "{date}",
      "policy_effective_date": "{closing date}",
      "delivery_to_lender_deadline": "{date}",
      "status": "on track / at risk / behind"
    },
    "insurance_cost_for_underwriting": {
      "total_annual": "{amount}",
      "monthly": "{amount}",
      "per_unit_annual": "{amount}",
      "per_unit_monthly": "{amount}",
      "per_sf_annual": "{amount}",
      "as_percent_of_egi": "{X}%",
      "year_over_year_trend": "increasing / stable / decreasing",
      "confidence_level": "estimate / quoted / bound"
    },
    "risk_flags": [
      {
        "flag": "{description}",
        "severity": "low / medium / high / critical",
        "recommendation": "{action}"
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
2. **Numeric Sanity** — All premium amounts are positive; per-unit and per-SF calculations are arithmetically correct; total equals sum of individual lines
3. **Cross-Reference Validation** — Unit count, property type, and address match property details provided
4. **Completeness Assessment** — Every strategy step produced output or a noted data gap
5. **Confidence Scoring** — Set `confidence_level` on the underwriting cost output and populate `uncertainty_flags` for any estimated or assumed values

**Self-Validation field checks:**

| Field | Valid Range | Flag If |
|-------|-----------|---------|
| coverageTypes | Must include all required coverage for the property type | Missing required type |
| premiumAmounts | > 0 per required coverage type | Zero or negative |
| policyEffectiveDate | On or before closing date | After closing |
| lenderNamedInsured | Must be included if financing exists | Missing lender |
| coverageLimits | > 0 per required type | Zero limit |

**Validation checks:**

| Check | Method |
|-------|--------|
| All coverage types assessed | Every coverage type has a required/not required determination |
| Lender requirements addressed | Every lender insurance requirement has compliance status |
| Flood zone confirmed | FEMA zone matches survey and flood determination |
| Premium estimates sourced | Every estimate has a benchmark or quote basis |
| Endorsements complete | Every lender-required endorsement is on the checklist |
| Binding timeline feasible | All deadlines achievable given current status |
| Cost totals accurate | Sum of individual premiums = stated total |
| Per-unit calculations correct | Total / units = per-unit figure |
| Gaps identified and actionable | Every gap has a recommendation and cost estimate |

---

## Red Flags & Dealbreakers

Treat the following as a CRITICAL finding requiring immediate escalation:

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| Uninsurable property condition | Cannot obtain required coverage types due to property condition, location, or history |

If a dealbreaker is detected: set severity to "CRITICAL", add to `risk_flags` with category "dealbreaker", note it prominently in the report summary, and continue analysis of all other coverage areas.

Additional high-severity flags:
- Flood insurance required but no NFIP-eligible carrier available
- Carrier rating below A.M. Best A- / VII (below lender minimum)
- Evidence of insurance deadline cannot be met given current binding timeline
- Premium estimates significantly above market — investigate property condition or loss history

---

## When Data is Missing

When property details, lender requirements, or environmental findings are incomplete:

1. **Attempt a workaround** — Use industry benchmarks for the asset class and region to estimate premiums; research standard lender requirements for the loan type; use public FEMA flood map data for flood zone determination
2. **Note the assumption** — Document any assumed coverage requirement or premium estimate, including its source and confidence level
3. **Mark in output** — Add an entry to `uncertainty_flags` with the field name, reason, and impact on the underwriting cost estimate
4. **Continue analysis** — Do not halt for missing individual coverage details; complete analysis on available information and list gaps as pending items
5. **Flag for review** — Coverage determinations involving material environmental risk or unusual property conditions should be reviewed by a qualified insurance broker

---

## Confidence Scoring

Apply confidence levels to all findings:

| Level | Criteria |
|-------|----------|
| **HIGH** | Based on actual quotes or bound policies; lender requirements confirmed in writing |
| **MEDIUM** | Based on benchmark data and stated lender requirements; no actual quotes yet |
| **LOW** | Based on general market assumptions; lender requirements not yet confirmed; significant property risk factors |

Set `confidence_level` in the output — particularly on the `insurance_cost_for_underwriting` block — and populate `uncertainty_flags` for any finding rated MEDIUM or LOW.

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- [Legal Checklist](knowledge/legal-checklist.md) for lender insurance requirement checklists and closing deliverable requirements
- [Lender Criteria](knowledge/lender-criteria.md) for standard insurance minimums by loan type and lender category
- [CRE Risk Scoring Framework](knowledge/risk-scoring.md) for severity rating guidance on coverage gaps and uninsurable conditions
- [Underwriting Calculations](knowledge/underwriting-calc.md) for integrating insurance costs into the operating expense pro forma

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
