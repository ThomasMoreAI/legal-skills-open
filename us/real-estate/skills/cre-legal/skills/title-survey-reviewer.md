---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Title & Survey Reviewer

Reviews a title commitment and ALTA/NSPS survey for a CRE acquisition, classifies every exception as permitted or objectionable, identifies survey issues, recommends title insurance endorsements, and drafts a title objection letter outline.

---

## When to Use This Skill

Use this skill when you have received a title commitment and/or ALTA survey for a property under contract and need a systematic review before closing. It is the right tool whenever you need to classify Schedule B-II exceptions, flag encroachments or access issues, determine which endorsements are appropriate, or prepare a formal title objection letter for the seller.

---

## What You'll Need to Provide

- The full title commitment (Schedule A, Schedule B-I Requirements, Schedule B-II Exceptions), or a description of the key contents
- The ALTA/NSPS survey (or a written description of survey findings, encroachments, easements, and flood zone designation)
- Property address, county, and state
- Buyer entity name and purchase price (for Schedule A verification)
- Seller entity name (to verify current owner matches)
- The PSA's definition of "Permitted Exceptions" and the title objection deadline (if known)
- Any relevant due diligence findings (environmental, zoning, property condition)
- Lender's title and endorsement requirements (if financing is involved)

---

## Mission

Review the title commitment and ALTA survey for the acquisition property. Classify all exceptions as permitted or objectionable, identify survey issues requiring resolution, recommend title insurance endorsements, and prepare a title objection letter outline. Ensure the buyer obtains clean, insurable title at closing.

---

## Strategy

### Step 1: Review Title Commitment Schedule A
- Verify proposed insured name matches the buyer entity
- Confirm coverage amount matches or exceeds purchase price
- Verify property legal description matches PSA and survey
- Confirm effective date is current (within 30-60 days)
- Note type of policy (owner's vs. lender's, standard vs. extended)
- Verify vesting deed and current owner match the seller in the PSA

### Step 2: Review Schedule B-I (Requirements)
- List all requirements to be satisfied before policy issuance
- For each requirement, identify:
  - Responsible party (buyer, seller, title company)
  - Expected timing (before closing, at closing, post-closing)
  - Difficulty level (routine, moderate, complex)
- Common requirements: payoff of existing liens, entity authorization documents, transfer tax payment, recording of deed
- Flag any unusual or potentially difficult requirements

### Step 3: Review Schedule B-II (Exceptions to Coverage)
- List every exception with document recording information
- For each exception, research and classify:

**Standard Exceptions (typically removable):**
- Rights of parties in possession (removable with survey + affidavit)
- Survey matters (removable with current ALTA survey)
- Mechanic's liens (removable with affidavit)
- Taxes not yet due (standard; verify current year status)
- Unrecorded easements (removable with survey + affidavit)

**Special Exceptions (property-specific):**
- Recorded easements (utility, access, drainage, conservation)
- CC&Rs / deed restrictions
- Prior mineral reservations
- Existing mortgages/liens (to be paid at closing)
- Judgment liens against seller
- HOA/condo declarations (if applicable)
- Government rights (eminent domain reservations)

### Step 4: Classify Each Exception
For each Schedule B-II exception:
- **Permitted Exception**: Acceptable to buyer; standard utility easements, standard restrictions, items consistent with property use
- **Objectionable Exception**: Requires cure before closing; active liens, judgments, encroachments, restrictions inconsistent with intended use, access limitations
- **Further Investigation Needed**: Ambiguous or unclear items requiring additional research or document review
- Cross-reference with PSA definition of "Permitted Exceptions"

### Step 5: Review ALTA Survey
- **Boundary**: Verify acreage/dimensions match legal description; check for gaps or overlaps with adjoining parcels
- **Easements**: Locate all recorded easements on survey; verify they match title commitment exceptions; identify any easements visible on ground but not recorded
- **Encroachments**:
  - FROM subject property onto neighboring parcels (buildings, fences, paving)
  - ONTO subject property from neighboring parcels
  - Into easement areas from improvements on subject property
- **Setback Compliance**: Verify all structures comply with zoning setback requirements
- **Flood Zone**: Confirm flood zone designation; note if any structures are in flood zone
- **Access**: Verify legal access to public right of way; identify any landlocked risk
- **Utility Locations**: Confirm utility lines and services; identify potential conflicts with improvements
- **Parking**: Verify parking count meets zoning requirements
- **Table A Items**: Confirm all requested Table A optional items are shown

### Step 6: Identify Survey Issues
- Encroachments that affect use or value
- Gap parcels between subject property and public road
- Unrecorded easements visible on ground
- Improvements crossing property lines
- Zoning setback violations
- Insufficient parking
- Access issues (no direct public road access, shared access)
- Flood zone issues (structures in flood zone, LOMA needed)
- Discrepancies between survey and title commitment

### Step 7: Recommend Title Endorsements
Based on property type, lender requirements, and issues identified:
- **Zoning 3.1**: Confirms zoning classification and compliance
- **Survey / Same as Survey**: Removes survey exception, matches legal to survey
- **Access**: Confirms legal access to public road
- **Contiguity**: Confirms parcels are contiguous (multi-parcel properties)
- **Environmental Protection Lien**: Coverage for environmental super-liens
- **Tax Parcel**: Confirms tax parcel matches insured land
- **Comprehensive (ALTA 9)**: Covers restrictions, encroachments, minerals
- **Subdivision**: Confirms legal subdivision compliance
- **Utility Access**: Confirms utility availability
- **Lender-specific endorsements**: Per lender requirements
- Note endorsement availability by jurisdiction (some not available in all states)

### Step 8: Prepare Title Objection Letter Outline
- List all objectionable exceptions with specific cure requested
- Deadline for seller's response (per PSA)
- Consequences if seller fails to cure (PSA termination rights)
- Proposed resolution for each objection
- Distinguish between "must cure" items and "request cure" items

---

## Output Format

```json
{
  "title_survey_review": {
    "metadata": {
      "review_date": "{date}",
      "title_company": "{name}",
      "commitment_number": "{number}",
      "effective_date": "{date}",
      "property_address": "{address}",
      "county": "{county}",
      "state": "{state}"
    },
    "schedule_a_review": {
      "proposed_insured": "{entity}",
      "matches_buyer_entity": "yes/no",
      "coverage_amount": "{amount}",
      "adequate_coverage": "yes/no",
      "legal_description_matches": "survey/PSA/both/neither",
      "current_owner": "{name}",
      "matches_psa_seller": "yes/no",
      "policy_type": "standard/extended"
    },
    "schedule_b1_requirements": [
      {
        "requirement": "{description}",
        "responsible_party": "buyer / seller / title company",
        "timing": "pre-closing / at closing / post-closing",
        "difficulty": "routine / moderate / complex",
        "status": "open / in progress / satisfied"
      }
    ],
    "schedule_b2_exception_analysis": {
      "total_exceptions": "{count}",
      "permitted_count": "{count}",
      "objectionable_count": "{count}",
      "investigate_count": "{count}",
      "exceptions": [
        {
          "exception_number": "{N}",
          "description": "{description}",
          "recording_info": "{book/page or instrument number}",
          "type": "standard / special",
          "classification": "permitted / objectionable / investigate",
          "rationale": "{why classified this way}",
          "cure_required": "yes/no",
          "cure_action": "{description if needed}",
          "impact_on_use": "none / minor / moderate / significant"
        }
      ]
    },
    "survey_issues": {
      "boundary": {
        "acreage_matches": "yes/no",
        "gap_parcels": "none / identified",
        "overlap_issues": "none / identified"
      },
      "easements": {
        "recorded_count": "{N}",
        "unrecorded_visible": "{N}",
        "conflicts_with_improvements": "yes/no"
      },
      "encroachments": [
        {
          "type": "from property / onto property / into easement",
          "description": "{description}",
          "severity": "minor / moderate / major",
          "recommended_action": "{action}"
        }
      ],
      "setback_compliance": "compliant / violation identified",
      "flood_zone": {
        "designation": "{zone}",
        "structures_in_flood_zone": "yes/no",
        "flood_insurance_required": "yes/no"
      },
      "access": {
        "legal_access_confirmed": "yes/no",
        "access_type": "direct / shared / easement",
        "issues": "{description or none}"
      },
      "parking": {
        "count": "{N}",
        "meets_zoning": "yes/no"
      }
    },
    "endorsement_recommendations": [
      {
        "endorsement": "{name and ALTA number}",
        "purpose": "{description}",
        "priority": "required / recommended / optional",
        "lender_required": "yes/no",
        "available_in_jurisdiction": "yes/no/unknown",
        "estimated_premium": "{amount or TBD}"
      }
    ],
    "title_insurance_gap_analysis": {
      "owner_policy_gaps": "{description or none}",
      "lender_policy_gaps": "{description or none}",
      "coverage_recommendations": "{description}"
    },
    "objection_letter_outline": {
      "objection_deadline": "{date per PSA}",
      "seller_cure_period": "{days per PSA}",
      "objections": [
        {
          "exception_number": "{N}",
          "objection": "{description}",
          "requested_cure": "{action}",
          "priority": "must-cure / request-cure",
          "consequence_if_uncured": "{PSA provision}"
        }
      ]
    },
    "risk_flags": [
      {
        "flag": "{description}",
        "severity": "low / medium / high / critical",
        "related_exception": "{exception number or survey item}",
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
2. **Numeric Sanity** — Exception counts, acreage, and coverage amounts are positive and internally consistent
3. **Cross-Reference Validation** — Property address, buyer entity, and coverage amount match deal terms provided
4. **Completeness Assessment** — Every strategy step produced output or a noted data gap
5. **Confidence Scoring** — Set `confidence_level` and populate `uncertainty_flags` for any estimated or assumed values

**Self-Validation field checks:**

| Field | Valid Range | Flag If |
|-------|-----------|---------|
| titleExceptionsCount | 0 - 50 | Above 50 is unusual |
| titleStatus | CLEAR, ISSUES, CRITICAL | Invalid value |
| surveyArea | > 0 | Zero or negative |
| encroachments | Each must have description and severity | Incomplete |
| legalDescription | Must match title commitment | Mismatch noted |

**Validation checks:**

| Check | Method |
|-------|--------|
| All exceptions classified | Count classified = total in Schedule B-II |
| No exceptions unaddressed | Every exception has classification + rationale |
| Survey cross-referenced | All recorded easements appear on survey |
| Endorsements jurisdiction-checked | Each endorsement verified for state availability |
| Objection letter complete | Every objectionable exception in letter outline |
| Legal descriptions match | Survey, title, and PSA descriptions compared |
| Flood zone verified | Survey and FEMA map cross-referenced |
| Lender requirements addressed | All lender-required endorsements included |

---

## Red Flags & Dealbreakers

Treat the following as CRITICAL severity findings requiring immediate escalation:

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| Active title dispute or lis pendens | Found in title search or Schedule B-II exceptions |
| Fraud in title chain | Discovered during chain of ownership review |
| Property in bankruptcy estate | Found in lien search or judgment search |
| Dissolved entity ownership | Entity in title chain found to be dissolved or revoked |

If a dealbreaker is detected: set severity to "CRITICAL", add to `risk_flags` with category "dealbreaker", note it prominently in the review summary, and continue analysis of all other items.

---

## When Data is Missing

When title commitment text, survey details, or supporting information is incomplete:

1. **Attempt a workaround** — Search county recorder/assessor portals, GIS mapping sites, or FEMA flood map service for publicly available information
2. **Note the assumption** — Document any assumption made, including its basis and confidence level
3. **Mark in output** — Add an entry to `uncertainty_flags` with the field name, reason, and impact on analysis
4. **Continue analysis** — Do not halt for non-critical gaps; complete all other review steps
5. **Flag for attorney review** — Do not assume favorable interpretations of missing title data; flag items requiring human attorney review

---

## Confidence Scoring

Apply confidence levels to all findings:

| Level | Criteria |
|-------|----------|
| **HIGH** | Based on verified title commitment and survey documents; no assumptions; data directly observed |
| **MEDIUM** | Based on partially available documents; minor assumptions made; some data interpolated |
| **LOW** | Based on unverified or summarized information; significant assumptions; stale or incomplete sources |

Set `confidence_level` in the output and populate `uncertainty_flags` for any finding rated MEDIUM or LOW.

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- [Legal Checklist](knowledge/legal-checklist.md) for a master list of CRE closing documents and curative requirements
- [CRE Risk Scoring Framework](knowledge/risk-scoring.md) for severity rating guidance and risk aggregation methodology
- [Lender Criteria](knowledge/lender-criteria.md) for lender-specific title and endorsement requirements

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
