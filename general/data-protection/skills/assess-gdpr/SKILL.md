---
name: assess-gdpr
title: GDPR Compliance Assessment
description: Conduct a GDPR compliance assessment for a system or processing activity.
author: melodic-software
author_url: https://github.com/melodic-software/claude-code-plugins/tree/main/plugins/compliance-planning/skills/assess-gdpr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# GDPR Compliance Assessment

Conduct a comprehensive GDPR compliance assessment.

## Workflow

### Step 1: Load Required Skills

Load these skills:

- `gdpr-compliance` - GDPR requirements and DPIA guidance
- `data-classification` - Personal data categorization

### Step 2: Spawn Privacy Officer Agent

Spawn the `privacy-officer` agent with the following prompt:

```text
Conduct a comprehensive GDPR compliance assessment for: $ARGUMENTS

Perform the following assessments:

1. Data Mapping
   - Identify all personal data collected
   - Categorize data (standard vs special category)
   - Map data flows (collection, processing, storage, sharing)
   - Identify controllers and processors
   - Document international transfers

2. Lawful Basis Assessment
   - Determine lawful basis for each processing activity
   - Validate consent mechanisms (if applicable)
   - Conduct Legitimate Interest Assessment (if applicable)

3. DPIA Determination
   - Assess if DPIA is required
   - If required, conduct risk assessment
   - Recommend mitigations for identified risks

4. Data Subject Rights
   - Assess implementation of all rights
   - Identify gaps in rights fulfillment
   - Recommend improvements

5. Privacy by Design
   - Evaluate data minimization
   - Assess purpose limitation
   - Review storage limitation
   - Check transparency measures

6. Documentation Review
   - Privacy notices
   - Processing records (Article 30)
   - Data protection policies

Provide a complete GDPR assessment with:
- Compliance score by area
- Gap analysis with priorities
- Remediation roadmap
- Evidence requirements
```

### Step 3: Generate Assessment Report

Ensure the report includes:

- Executive summary with overall compliance rating
- Detailed findings by GDPR article
- Prioritized remediation plan
- Timeline for compliance

## Example Usage

```bash
# Assess a customer data processing system
/compliance-planning:assess-gdpr "customer relationship management system processing EU customer data"

# Assess a marketing platform
/compliance-planning:assess-gdpr "email marketing platform with subscriber consent management"

# Assess an e-commerce site
/compliance-planning:assess-gdpr "e-commerce website serving EU customers with payment processing"
```

## Output Format

```markdown
# GDPR Compliance Assessment: [System Name]

## Executive Summary

### Overall Compliance: [HIGH/MEDIUM/LOW]

| Area | Score | Status |
|------|-------|--------|
| Lawful Basis | [X/10] | [Status] |
| Data Subject Rights | [X/10] | [Status] |
| Security | [X/10] | [Status] |
| Documentation | [X/10] | [Status] |
| **Overall** | **[X/10]** | **[Status]** |

### Key Findings
- [Critical finding 1]
- [Critical finding 2]

---

## Personal Data Inventory

[Detailed data mapping]

---

## Lawful Basis Analysis

[Assessment per processing activity]

---

## Data Subject Rights Assessment

[Implementation status per right]

---

## DPIA Assessment

### Required: [Yes/No]
[If yes, full DPIA]

---

## Gap Analysis

### Critical Gaps
| Gap | GDPR Article | Risk | Remediation |
|-----|--------------|------|-------------|

---

## Remediation Roadmap

### Immediate (0-30 days)
1. [Action]

### Short-term (30-90 days)
1. [Action]

### Long-term (90+ days)
1. [Action]

---

## Documentation Checklist

- [ ] Privacy notice updated
- [ ] Article 30 records complete
- [ ] DPIAs conducted
- [ ] BAAs/DPAs in place
- [ ] Consent records maintained
```
