---
name: fedramp-poam-quality-check
title: 'Input: poam_tsv = "fedramp_poam_2025.tsv"'
description: Validates FedRAMP Plan of Action and Milestones (POAM) files for structural integrity, naming conventions, deduplication, and cross-sheet consistency
author: williamzujkowski
author_url: https://github.com/williamzujkowski/cognitive-toolworks/tree/main/skills/compliance-fedramp-validator
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

## Purpose & When-To-Use

Use this skill when you need to validate a FedRAMP Plan of Action and Milestones (POAM) file before submission or continuous monitoring updates. The POAM tracks system weaknesses and deficiencies with corrective actions and timelines according to FedRAMP requirements (accessed 2025-10-25T21:04:34-04:00: https://www.fedramp.gov/assets/resources/documents/CSP_POAM_Template_Completion_Guide.pdf).

**Trigger conditions:**
- Pre-submission quality gates for FedRAMP POAM deliverables
- Continuous monitoring validation before AO submission
- Post-assessment cleanup to ensure data integrity
- Integration checks for OSCAL-to-TSV conversions
- Duplicate entry detection across Open/Closed sheets

## Pre-Checks

**Required validations before proceeding:**

1. **Input availability:**
   - `poam_tsv` file exists and is readable
   - File size < 10 MB (sanity check)
   - At least one header row present

2. **Time context:**
   - Compute `NOW_ET` using NIST time.gov semantics (America/New_York, ISO-8601)
   - Current timestamp: 2025-10-25T21:04:34-04:00

3. **Schema availability:**
   - If `naming_convention` provided, validate JSON schema structure
   - Required keys: `required_fields`, `date_format`, `severity_levels`
   - Default to FedRAMP standard if not provided

4. **Encoding check:**
   - Verify UTF-8 or ASCII encoding
   - Tab-delimited structure (not comma/pipe/other)

**Abort conditions:**
- File unreadable or corrupted
- No recognizable header row
- Encoding errors preventing parse

## Procedure

### Tier 1: Header & Format Sanity (≤2k tokens)

**Goal:** Fast validation for 80% of common issues

1. **Parse header row:**
   - Extract column names
   - Verify presence of core required fields:
     - `POA&M Item ID`, `Control Identifier`, `Weakness Description`
     - `Risk Level` (or `Severity`), `Scheduled Completion Date`, `Status`

2. **Row-level format checks:**
   - Count total rows (Open + Closed if multi-sheet)
   - Detect missing required fields (empty cells in required columns)
   - Flag malformed dates (must match YYYY-MM-DD or MM/DD/YYYY)
   - Check severity values: must be in {High, Moderate, Low, Informational}

3. **Output (JSON):**
   ```json
   {
     "errors": [
       {"row": 12, "field": "Scheduled Completion Date", "issue": "Invalid date format", "severity": "error"}
     ],
     "warnings": [],
     "stats": {"total_rows": 47, "duplicates": 0, "missing_required": 3}
   }
   ```

4. **Decision rule:**
   - If errors > 10% of rows OR missing_required > 5, stop and report
   - Else proceed to T2

**Token budget: ≤2k**

---

### Tier 2: Naming Convention & Deduplication (≤6k tokens)

**Goal:** Enforce naming standards and detect duplicates

1. **Apply naming convention schema:**
   - Validate `POA&M Item ID` format (e.g., `POAM-YYYY-###` or custom regex)
   - Check `Control Identifier` against NIST 800-53 rev4/rev5 catalog
   - Verify `Status` values: {Open, In Progress, Completed, Risk Accepted}

2. **Deduplication logic:**
   - Compute hash of (`Control Identifier`, `Weakness Description`, `Resource`)
   - Flag exact duplicates across Open/Closed sheets
   - Warn on near-duplicates (80%+ text similarity in Weakness Description)

3. **Timeline validation (FedRAMP requirements):**
   - High severity: remediation ≤ 30 days from discovery (accessed 2025-10-25T21:04:34-04:00: https://www.fedramp.gov/resources/documents/CSP_Vulnerability_Scanning_Requirements.pdf)
   - Moderate: ≤ 90 days
   - Low: ≤ 180 days
   - Flag overdue items with current `NOW_ET` comparison

4. **Sources cited:**
   - **FedRAMP POA&M Template Completion Guide** (accessed 2025-10-25T21:04:34-04:00): https://www.fedramp.gov/assets/resources/documents/CSP_POAM_Template_Completion_Guide.pdf
   - **FedRAMP Vulnerability Scanning Requirements** (accessed 2025-10-25T21:04:34-04:00): https://www.fedramp.gov/resources/documents/CSP_Vulnerability_Scanning_Requirements.pdf
   - **NIST SP 800-37 Rev. 2** (accessed 2025-10-25T21:04:34-04:00): https://csrc.nist.gov/pubs/sp/800/37/r2/final
   - **FedRAMP OSCAL POA&M Documentation** (accessed 2025-10-25T21:04:34-04:00): https://automate.fedramp.gov/documentation/poam/

5. **Enhanced output:**
   - Add `warnings` for near-duplicates and overdue timelines
   - Populate `duplicates` count in stats
   - Generate markdown fix suggestions prioritized by severity

**Token budget: ≤6k**

---

### Tier 3: Cross-Sheet Consistency (≤12k tokens)

**Goal:** Deep validation across Open/Closed sheets and logical integrity

1. **Sheet relationship checks:**
   - Verify no item appears in both Open and Closed sheets
   - Validate Closed items have `Completion Date` and `Status = Completed`
   - Check for reopened items (same ID moved from Closed → Open)

2. **Risk scoring consistency:**
   - If CVSS scores present, validate against declared `Risk Level`
   - Cross-reference `Weakness Description` with known CVE/CWE patterns
   - Flag discrepancies between narrative severity and numeric scores

3. **Milestone progression:**
   - For multi-milestone POAMs, verify dates are sequential
   - Check that `Original Detection Date` ≤ `Scheduled Completion Date`
   - Validate `Resources Required` field is populated for High/Moderate items

4. **Rationale generation:**
   - For each error/warning, provide context and remediation steps
   - Link to relevant sections of FedRAMP/NIST guidance
   - Estimate compliance risk (blocker vs. advisory)

5. **Comprehensive markdown report:**
   ```markdown
   ## Critical Issues (3)
   - Row 12: Invalid completion date (blocks submission)
   - Row 23: Duplicate weakness (merge required)

   ## Warnings (7)
   - Row 8: Timeline exceeds FedRAMP requirement (High: 30 days)

   ## Recommendations
   - Update naming convention to include fiscal year prefix
   - Consider automated CVE enrichment for weakness descriptions
   ```

**Token budget: ≤12k**

## Decision Rules

**Ambiguity thresholds:**
- **Exact duplicate:** 100% match on (Control ID, Weakness, Resource)
- **Near-duplicate:** ≥80% cosine similarity on Weakness Description text
- **Overdue tolerance:** Grace period of 7 calendar days beyond FedRAMP timeline

**Abort/stop conditions:**
- File parse failure → stop at Pre-Checks
- Errors > 10% rows → stop after T1, report findings
- Missing schema keys → use FedRAMP defaults, log warning

**Escalation triggers:**
- Critical errors (missing required fields, invalid dates) → halt progression
- Warnings only → continue to T3 if requested

## Output Contract

**Primary output (`findings.json`):**
```json
{
  "errors": [
    {
      "row": 12,
      "field": "Scheduled Completion Date",
      "issue": "Invalid date format (expected YYYY-MM-DD)",
      "severity": "error"
    }
  ],
  "warnings": [
    {
      "row": 8,
      "field": "Risk Level",
      "issue": "High-severity item overdue by 15 days",
      "severity": "warning"
    }
  ],
  "stats": {
    "total_rows": 47,
    "duplicates": 2,
    "missing_required": 3,
    "overdue_high": 1,
    "overdue_moderate": 4
  }
}
```

**Secondary output (`fix_suggestions.md`):**
- Markdown-formatted remediation guidance
- Grouped by severity: Critical → High → Medium → Low
- Includes row numbers, field names, and specific correction steps
- Links to authoritative sources for each issue type

**Required fields in all outputs:**
- `timestamp`: ISO-8601 Eastern Time (NOW_ET)
- `skill_version`: "1.0.0"
- `input_file`: original filename

## Examples

**Example 1: Basic T1 validation (≤30 lines)**

```python
# Input: poam_tsv = "fedramp_poam_2025.tsv"

findings = {
  "errors": [
    {"row": 5, "field": "POA&M Item ID", "issue": "Missing"},
    {"row": 12, "field": "Date", "issue": "Invalid '13/45/2025'"}
  ],
  "warnings": [
    {"row": 8, "issue": "High overdue 15d"}
  ],
  "stats": {"total_rows": 47, "duplicates": 2}
}

fix_suggestions = """
## Critical (2)
- Row 5: Add POA&M Item ID (POAM-2025-NNN)
- Row 12: Fix date (YYYY-MM-DD)

## Warnings (1)
- Row 8: High past 30-day window
"""

import json
print(json.dumps(findings))
print(fix_suggestions)
# Output: JSON findings + markdown suggestions
```

## Quality Gates

**Token budgets (mandatory):**
- T1: ≤2k tokens (header + format checks)
- T2: ≤6k tokens (naming + deduplication + 2-4 sources)
- T3: ≤12k tokens (cross-sheet + rationale generation)

**Safety checks:**
- No external network calls (file processing only)
- No credential handling or sensitive data exposure
- Read-only operations on input files
- Validate file paths are within expected directories

**Auditability:**
- Log all validation steps with timestamps
- Preserve original input (no in-place modifications)
- Link every error/warning to specific source requirement
- Include skill version in all outputs

**Determinism:**
- Same input → same output (no random sampling)
- Consistent hash functions for duplicate detection
- Fixed threshold values (no dynamic adjustment)
- Reproducible similarity scoring (cosine/Levenshtein)

**Performance targets:**
- T1: < 5 seconds for files ≤1000 rows
- T2: < 15 seconds including duplicate detection
- T3: < 30 seconds for full cross-sheet analysis

## Resources

**Official FedRAMP guidance:**
- FedRAMP POA&M Template Completion Guide: https://www.fedramp.gov/assets/resources/documents/CSP_POAM_Template_Completion_Guide.pdf
- FedRAMP OSCAL POA&M Documentation: https://automate.fedramp.gov/documentation/poam/
- FedRAMP Vulnerability Scanning Requirements: https://www.fedramp.gov/resources/documents/CSP_Vulnerability_Scanning_Requirements.pdf

**NIST references:**
- NIST SP 800-37 Rev. 2 (Risk Management Framework): https://csrc.nist.gov/pubs/sp/800/37/r2/final
- NIST SP 800-53 Rev. 5 (Security Controls): https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final

**OSCAL resources:**
- OSCAL POA&M Model: https://pages.nist.gov/OSCAL/concepts/layer/assessment/poam/
- FedRAMP OSCAL Baselines: https://github.com/GSA/fedramp-automation

**Helper tools (linked in resources/):**
- `naming_convention_schema.json` - Default FedRAMP field validation rules
- `similarity_thresholds.yaml` - Tunable deduplication parameters
