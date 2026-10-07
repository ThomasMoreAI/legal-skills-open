---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Estoppel Tracker

Manages tenant estoppel certificate collection for an entire property: builds the tracking list from the rent roll, reviews each returned certificate for discrepancies, monitors threshold compliance against PSA requirements, and flags material issues that affect underwriting or closing.

---

## When to Use This Skill

Use this skill whenever you need to systematically track estoppel certificate delivery and review for a multifamily or commercial acquisition. It is appropriate after the PSA is signed and the seller has agreed to deliver estoppels, or whenever you need to verify that tenant-reported lease terms match the rent roll and lease abstracts on file.

---

## What You'll Need to Provide

- The current rent roll with unit numbers, tenant names, monthly rent amounts, lease start/end dates, security deposit amounts, and lease type (market, Section 8, other)
- Lease abstracts or lease summaries from due diligence, showing key lease terms
- The PSA's estoppel requirements: minimum return threshold percentage and delivery deadline
- The property address and total unit count
- Any estoppel certificates that have already been received (paste content or describe discrepancies)
- Property type and whether any units are vacant

---

## Mission

Manage tenant estoppel certificate collection for the entire property. For properties with more than 50 units, process tenants in batches of 50 to track delivery, review content, and flag discrepancies with the rent roll. Ensure the PSA-required minimum threshold is met before closing.

---

## Strategy

### Step 1: Generate Estoppel Certificate Tracking List
- Extract complete tenant roster from the rent roll provided
- Assign a unique tracking ID to each unit/tenant
- Record baseline data per tenant from the rent roll:
  - Unit number
  - Tenant name
  - Current monthly rent
  - Lease start/end dates
  - Security deposit amount
  - Lease type (market, Section 8, other)
- Determine PSA threshold requirement (default: 75-80% of occupied units if not specified)
- Set target collection date (PSA deadline minus 5 business days buffer)

### Step 2: Batch Processing for Large Properties
For properties with more than 50 units, organize tracking in batches:

```
totalUnits = property.totalUnits
batchSize = 50
numBatches = ceil(totalUnits / batchSize)

FOR batch 1..numBatches:
  startUnit = (batch-1) * batchSize + 1
  endUnit = min(batch * batchSize, totalUnits)
  Track estoppels for units {startUnit}-{endUnit}
```

Each batch tracks:
- Assigned unit range
- Rent roll data for those units
- Lease abstract data for those units
- Estoppel form delivery and return status
- Discrepancy findings

For properties with 50 or fewer units, process as a single batch.

### Step 3: Per-Tenant Tracking
For each tenant, track:

**Delivery Status:**
- Estoppel sent date
- Follow-up dates (1st, 2nd, 3rd reminder)
- Received date
- Status: `outstanding` | `received` | `waived` | `refused` | `vacant`

**Content Review (upon receipt):**
- **Rent Verification**: Compare stated rent to rent roll amount
  - Flag if differs by more than $0 (exact match required)
- **Lease Term Verification**: Compare stated lease dates to lease abstract
  - Flag if start date, end date, or renewal terms differ
- **Security Deposit Verification**: Compare stated deposit to records
  - Flag if amount differs
- **Landlord Default Claims**: Note any tenant-claimed defaults
  - Maintenance issues, habitability claims, lease violations by landlord
- **Tenant Claims**: Note any claims against property/landlord
  - Pending disputes, offset claims, rent abatement claims
- **Side Agreements**: Note any side agreements not in lease file
  - Verbal agreements, amendments, parking/storage deals
- **Discrepancy Classification**:
  - `minor`: Rounding differences, immaterial date discrepancies
  - `moderate`: Rent differs by < 5%, minor term differences
  - `material`: Rent differs by > 5%, missing lease term, landlord default claimed

### Step 4: Aggregate All Results
- Merge all batch results into a master tracking summary
- Calculate aggregate metrics:
  - Total units: `{N}`
  - Occupied units: `{N}`
  - Estoppels required (occupied units): `{N}`
  - Estoppels received: `{N}`
  - Estoppels outstanding: `{N}`
  - Estoppels waived: `{N}`
  - Completion rate: `{received / required * 100}%`
  - Discrepancies found: `{N}` (by severity)
  - Material issues: `{N}`

### Step 5: Calculate Threshold Compliance
- PSA threshold: `{X}%` of occupied units (from PSA or default 75-80%)
- Current completion: `{Y}%`
- Status: `MET` | `NOT MET` | `ON TRACK` | `AT RISK`
- If NOT MET:
  - Units needed to meet threshold: `{N}`
  - Outstanding units list with contact priority
  - Recommended escalation actions (seller to compel, buyer to waive specific units)
- Days remaining until PSA deadline: `{N}`
- Projected completion based on current receipt rate

### Step 6: Material Issue Assessment
- Compile all material discrepancies
- For each material issue:
  - Impact on underwriting (rent variance affects NOI)
  - Impact on closing (landlord default claim could delay)
  - Recommended resolution (verify with seller, adjust underwriting, require cure)
- Assess aggregate impact on deal economics
- Determine if any discrepancies require PSA price adjustment

---

## Output Format

```json
{
  "estoppel_status_report": {
    "metadata": {
      "report_date": "{date}",
      "property": "{property name/address}",
      "total_units": "{N}",
      "occupied_units": "{N}",
      "psa_threshold": "{X}%",
      "psa_deadline": "{date}"
    },
    "overall_completion": {
      "estoppels_required": "{N}",
      "estoppels_received": "{N}",
      "estoppels_outstanding": "{N}",
      "estoppels_waived": "{N}",
      "estoppels_refused": "{N}",
      "vacant_units": "{N}",
      "completion_rate": "{X}%",
      "threshold_status": "MET / NOT MET / ON TRACK / AT RISK",
      "units_needed_for_threshold": "{N or 0}",
      "days_until_deadline": "{N}",
      "projected_completion_rate": "{X}%"
    },
    "batch_status": {
      "total_batches": "{N}",
      "batches": [
        {
          "batch_number": "{N}",
          "unit_range": "{start}-{end}",
          "units_in_batch": "{N}",
          "received": "{N}",
          "outstanding": "{N}",
          "discrepancies": "{N}",
          "material_issues": "{N}",
          "status": "complete / in_progress / pending"
        }
      ]
    },
    "discrepancy_summary": {
      "total_discrepancies": "{N}",
      "minor": "{N}",
      "moderate": "{N}",
      "material": "{N}",
      "discrepancies": [
        {
          "unit": "{unit number}",
          "tenant": "{name}",
          "discrepancy_type": "rent / lease_term / security_deposit / landlord_default / side_agreement",
          "severity": "minor / moderate / material",
          "rent_roll_value": "{value}",
          "estoppel_value": "{value}",
          "variance": "{amount or description}",
          "impact": "{description}",
          "recommended_action": "{action}"
        }
      ]
    },
    "material_issues": [
      {
        "unit": "{unit number}",
        "tenant": "{name}",
        "issue": "{description}",
        "financial_impact": "{estimated $ impact on NOI}",
        "closing_impact": "none / potential delay / deal risk",
        "resolution": "{recommended action}"
      }
    ],
    "outstanding_units": [
      {
        "unit": "{unit number}",
        "tenant": "{name}",
        "monthly_rent": "{amount}",
        "sent_date": "{date}",
        "followup_count": "{N}",
        "last_followup": "{date}",
        "priority": "high / medium / low",
        "notes": "{any known issues}"
      }
    ],
    "threshold_compliance": {
      "status": "MET / NOT MET",
      "current_rate": "{X}%",
      "required_rate": "{X}%",
      "gap_units": "{N}",
      "recommended_actions": [
        {
          "action": "{description}",
          "priority": "immediate / before_deadline"
        }
      ]
    },
    "underwriting_impact": {
      "rent_variance_total": "{amount}",
      "noi_adjustment_needed": "yes/no",
      "adjusted_noi": "{amount if applicable}",
      "price_adjustment_recommended": "yes/no",
      "recommended_adjustment": "{amount if applicable}"
    },
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
2. **Numeric Sanity** — All counts are non-negative; completion rate arithmetic is correct
3. **Cross-Reference Validation** — Unit counts, property address, and total units match rent roll provided
4. **Threshold Comparison** — Completion rate correctly assessed against PSA threshold (default minimum: 80% if not specified)
5. **Completeness Assessment** — Every strategy step produced output or a noted data gap
6. **Confidence Scoring** — Set `confidence_level` and populate `uncertainty_flags` for any estimated or assumed values

**Self-Validation field checks:**

| Field | Valid Range | Flag If |
|-------|-----------|---------|
| totalEstoppelsSent | Must equal total occupied units | Mismatch |
| estoppelsReceived | 0 - totalEstoppelsSent | Outside range |
| returnRate | estoppelsReceived / totalEstoppelsSent | Arithmetic mismatch |
| returnRate | >= PSA threshold (default 0.80) | Below threshold — flag as HIGH severity |
| discrepancyCount | 0 - estoppelsReceived | Outside range |
| varianceAmount per estoppel | <= 5% of stated rent | Exceeds 5% — classify as material |
| batchCounts | Sum across batches = total | Sum mismatch |
| No duplicate tenants across batches | | Duplicate found |

---

## Red Flags & Dealbreakers

Treat the following as CRITICAL severity findings requiring immediate escalation:

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| Criminal activity nexus | Tenant disclosures in estoppel certificates reveal illegal activity at the property |

If a dealbreaker is detected: set severity to "CRITICAL", add to the material issues list with category "dealbreaker", note it prominently in the summary, and continue analysis of all other estoppels.

---

## When Data is Missing

When rent roll data, lease abstracts, or estoppel certificates are incomplete:

1. **Attempt a workaround** — Use available rent roll columns, prior lease summaries, or information disclosed in due diligence to fill gaps
2. **Note the assumption** — Document any assumption, including confidence level (e.g., "security deposit assumed $0 because not on rent roll")
3. **Mark in output** — Add an entry to `uncertainty_flags` with the field name, reason, and impact on analysis
4. **Continue analysis** — Do not halt for missing individual estoppels; track as "outstanding" and continue with received certificates
5. **Flag for attorney review** — Do not assume favorable interpretations of tenant claims or landlord default allegations; flag for human review

---

## Confidence Scoring

Apply confidence levels to all findings:

| Level | Criteria |
|-------|----------|
| **HIGH** | Based on received estoppel certificates and verified rent roll; discrepancy amounts directly calculated |
| **MEDIUM** | Based on partially received estoppels; some units estimated from rent roll only |
| **LOW** | Based on few or no received estoppels; significant assumptions about tenant compliance |

Set `confidence_level` in the output and populate `uncertainty_flags` for any finding rated MEDIUM or LOW.

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- [Legal Checklist](knowledge/legal-checklist.md) for PSA estoppel requirements and standard tenant notification obligations
- [CRE Risk Scoring Framework](knowledge/risk-scoring.md) for severity rating guidance on material discrepancies
- [Underwriting Calculations](knowledge/underwriting-calc.md) for NOI adjustment methodology when rent variances are identified

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
