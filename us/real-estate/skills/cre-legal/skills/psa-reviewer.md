---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# PSA Reviewer

Reviews a Purchase and Sale Agreement clause by clause, surfaces risk provisions, tracks all deadlines, and produces a structured analysis that protects buyer interests.

---

## When to Use This Skill

Use this skill when you have received a draft or executed Purchase and Sale Agreement for a commercial real estate acquisition and need a systematic legal review. It is appropriate any time you want to identify non-standard terms, assess buyer risk exposure, build a deadline calendar, or prepare a list of recommended modifications before signing or before closing.

---

## What You'll Need to Provide

- The full text of the Purchase and Sale Agreement (paste the document or describe its key provisions)
- Buyer entity name and seller entity name
- Purchase price and earnest money amount
- Key dates you already know (expected closing date, due diligence period length, if available)
- Any due diligence findings, environmental reports, or financing terms that are relevant to the PSA review
- The property address and state (for jurisdiction-specific context)

---

## Mission

Review the Purchase and Sale Agreement. Identify key terms, contingencies, representations & warranties, indemnification provisions, and deadline tracking. Ensure the PSA protects buyer interests and surface all provisions that create risk, impose tight deadlines, or deviate from market-standard language.

---

## Strategy

### Step 1: Review PSA Structure and Key Provisions
- Identify parties, property description, purchase price, and closing date
- Confirm legal descriptions match title commitment and survey
- Verify entity names match formation documents and deal terms provided
- Note any defined terms that narrow or expand standard meanings

### Step 2: Analyze Contingency Periods
- **Due Diligence**: Start date, end date, termination rights, deposit refund provisions
- **Financing**: Commitment deadline, failure-to-obtain provisions, termination rights
- **Title**: Objection deadline, cure period, uncured objection remedies
- **Environmental**: Phase I deadline, Phase II rights, remediation responsibilities
- Map every contingency to a calendar date with notice requirements

### Step 3: Review Representations and Warranties
- **Property Condition**: "As-is" vs. specific condition reps; survival post-closing
- **Income/Financials**: Accuracy of operating statements, rent roll certification
- **Leases**: Completeness of lease schedule, no defaults, no side agreements
- **Litigation**: Pending or threatened claims, governmental actions
- **Environmental**: Known contamination, USTs, compliance history
- **Compliance**: Zoning, ADA, building code, permits
- Assess materiality thresholds and knowledge qualifiers ("to seller's knowledge")

### Step 4: Assess Indemnification Provisions
- Scope of buyer vs. seller indemnification obligations
- Survival periods for each category of representation
- Caps, baskets, and deductibles on indemnification claims
- Exclusive remedy provisions (does indemnification replace other claims?)
- Insurance offset provisions

### Step 5: Review Deposit Structure
- Earnest money amount and form (cash, LOC)
- Hard money dates (when deposit becomes non-refundable)
- Additional deposits and triggers
- Deposit application at closing
- Dispute resolution for deposit (escrow agent interpleader rights)

### Step 6: Identify Default and Remedy Provisions
- Buyer default: seller's remedies (liquidated damages, specific performance, both)
- Seller default: buyer's remedies (specific performance, damages, termination + return of deposit)
- Notice requirements and cure periods for each party
- Limitation of liability provisions
- Waiver of consequential damages

### Step 7: Review Assignment and Assumption Provisions
- Right to assign to affiliate entity without consent
- Assignment to unrelated party (requires consent?)
- Assumption of existing contracts, permits, warranties
- Seller's cooperation obligations post-assignment

### Step 8: Track All Deadlines and Notice Requirements
- Build comprehensive deadline calendar from PSA
- Identify notice methods (email, courier, certified mail)
- Note business days vs. calendar days for each deadline
- Flag any "time is of the essence" provisions

### Step 9: Identify Unusual or Non-Standard Terms
- Compare against market-standard CRE PSA provisions
- Flag any one-sided provisions favoring seller
- Note any missing standard protections for buyer
- Identify jurisdiction-specific unusual requirements

### Step 10: Flag Risk-Creating Provisions
- Provisions that expose buyer to unexpected liability
- Ambiguous language subject to multiple interpretations
- Tight deadlines with inadequate cure periods
- Limitations on buyer's inspection or access rights
- Post-closing obligations that could create ongoing exposure

---

## Output Format

```json
{
  "psa_review": {
    "metadata": {
      "review_date": "{date}",
      "psa_date": "{psa_execution_date}",
      "parties": {
        "buyer": "{buyer_entity}",
        "seller": "{seller_entity}"
      }
    },
    "key_terms_table": {
      "purchase_price": "{amount}",
      "earnest_money": "{amount}",
      "hard_money_date": "{date}",
      "closing_date": "{date}",
      "due_diligence_period": "{start} to {end}",
      "financing_contingency": "{date}",
      "property_condition": "as-is / with-reps",
      "assignment_rights": "permitted / restricted"
    },
    "contingency_deadline_tracker": [
      {
        "contingency": "{name}",
        "start_date": "{date}",
        "end_date": "{date}",
        "notice_required": "yes/no",
        "notice_method": "{method}",
        "termination_right": "{description}",
        "deposit_refund": "yes/no",
        "status": "open / satisfied / waived / expired"
      }
    ],
    "rep_warranty_summary": [
      {
        "category": "{category}",
        "scope": "{description}",
        "knowledge_qualifier": "yes/no",
        "materiality_threshold": "{amount or N/A}",
        "survival_period": "{months/years}",
        "risk_level": "low / medium / high"
      }
    ],
    "indemnification_analysis": {
      "seller_indemnification": {
        "scope": "{description}",
        "cap": "{amount or uncapped}",
        "basket": "{amount or none}",
        "survival": "{period}"
      },
      "buyer_indemnification": {
        "scope": "{description}",
        "cap": "{amount or uncapped}"
      },
      "exclusive_remedy": "yes/no"
    },
    "risk_flags": [
      {
        "flag": "{description}",
        "severity": "low / medium / high / critical",
        "provision_reference": "Section {X}",
        "recommendation": "{action}"
      }
    ],
    "recommended_modifications": [
      {
        "provision": "Section {X}",
        "current_language": "{summary}",
        "recommended_change": "{description}",
        "priority": "must-have / nice-to-have",
        "rationale": "{why}"
      }
    ],
    "deadline_calendar": [
      {
        "date": "{date}",
        "event": "{description}",
        "notice_required": "yes/no",
        "consequence_of_miss": "{description}",
        "days_from_signing": "{N}"
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
2. **Numeric Sanity** — Purchase price, earnest money, and all dollar amounts are positive and internally consistent
3. **Cross-Reference Validation** — Buyer/seller entity names, property address, and purchase price match what was provided
4. **Completeness Assessment** — Every strategy step produced output or a noted data gap
5. **Confidence Scoring** — Set `confidence_level` and populate `uncertainty_flags` for any estimated or assumed values

**Self-Validation field checks:**

| Field | Valid Range | Flag If |
|-------|-----------|---------|
| purchasePrice | > 0, match deal terms provided | Mismatch or zero |
| contingencyDeadlines | All dates must be future or match PSA | Past date without explanation |
| earnestMoneyDeposit | > 0 | Zero or negative |
| dueDiligencePeriodDays | > 0 | Zero or negative |
| closingDate | After due diligence period ends | Closing before DD end |
| riskItems | At least 1 identified | Zero risks unusual for any PSA |

**Validation checks:**

| Check | Method |
|-------|--------|
| All PSA sections reviewed | Every strategy step produced output |
| All dates extracted | Cross-reference deadline calendar with PSA text |
| All reps catalogued | Count reps in summary vs. reps found in PSA |
| Risk flags complete | Every non-standard provision has a flag |
| Deadline calendar accurate | Validate dates against PSA terms |
| Modifications prioritized | Every recommended change has priority and rationale |

---

## Red Flags & Dealbreakers

Treat the following as CRITICAL severity findings requiring immediate escalation:

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| Active title dispute or lis pendens | Referenced in PSA disclosures or seller representations |
| Property in bankruptcy estate | Disclosed in PSA or seller entity status |
| Fraud in title chain | Referenced in representations and warranties |
| Dissolved entity ownership | Seller entity issues discovered during review |

If a dealbreaker is detected: set severity to "CRITICAL", add to `risk_flags` with category "dealbreaker", note it prominently in the review summary, and continue analysis of all other provisions.

---

## When Data is Missing

When PSA text or supporting information is incomplete:

1. **Attempt a workaround** — Use available document sections, publicly available jurisdiction information, or market-standard assumptions where appropriate
2. **Note the assumption** — Document any assumption made, including its basis and confidence level
3. **Mark in output** — Add an entry to `uncertainty_flags` with the field name, reason, and impact on analysis
4. **Continue analysis** — Do not halt for non-critical gaps; complete all other review steps
5. **Flag for attorney review** — Do not assume favorable interpretations of missing legal provisions; flag items requiring human attorney review

---

## Confidence Scoring

Apply confidence levels to all findings:

| Level | Criteria |
|-------|----------|
| **HIGH** | Based on verified PSA text; no assumptions; provision directly observed and clear |
| **MEDIUM** | Based on partially available text; minor assumptions made; some interpretation required |
| **LOW** | Based on unverified or summarized information; significant assumptions; stale or incomplete sources |

Set `confidence_level` in the output and populate `uncertainty_flags` for any finding rated MEDIUM or LOW.

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- [Legal Checklist](knowledge/legal-checklist.md) for a master list of CRE closing documents and legal requirements
- [CRE Risk Scoring Framework](knowledge/risk-scoring.md) for severity rating guidance and risk aggregation methodology
- [Lender Criteria](knowledge/lender-criteria.md) for financing contingency benchmarks and lender-specific PSA requirements

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
