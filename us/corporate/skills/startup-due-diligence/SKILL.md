---
name: startup-due-diligence
title: Startup Due Diligence Skill
description: 'Legal due diligence review for seed-stage and Series A startups (US, Delaware C-Corp focus). Supports both investor and founder perspectives. Capabilities include: (1) Interactive document review and issue spotting; (2) Document request list generation; (3) Cap table and SAFE/convertible note analysis; (4) Red flag identification with severity ratings; (5) Diligence report generation. TRIGGERS: due diligence, DD, startup investment, cap table review, Series A, seed round, investor diligence, legal review startup, SAFE analysis, convertible note, 409A, founder vesting.'
author: skala-io
author_url: https://github.com/skala-io/legal-skills/tree/main/skills/startup-due-diligence
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: us
practice: corporate
language: en
sources:
- title: Cap table
  path: references/checklists/cap-table.md
- title: Compliance
  path: references/checklists/compliance.md
- title: Contracts
  path: references/checklists/contracts.md
- title: Corporate
  path: references/checklists/corporate.md
- title: Employment
  path: references/checklists/employment.md
- title: Financials
  path: references/checklists/financials.md
- title: Ip
  path: references/checklists/ip.md
- title: Litigation
  path: references/checklists/litigation.md
- title: 409a options
  path: references/guidance/409a-options.md
- title: Delaware corp
  path: references/guidance/delaware-corp.md
- title: Founder equity
  path: references/guidance/founder-equity.md
- title: Safe notes
  path: references/guidance/safe-notes.md
- title: Common issues
  path: references/red-flags/common-issues.md
---

*First published on [Skala Legal Skills](https://www.skala.io/legal-skills)*

## Legal Disclaimer

This skill is provided for informational and educational purposes only and does not constitute legal advice. The analysis and information provided should not be relied upon as a substitute for consultation with a qualified attorney. No attorney-client relationship is created by using this skill. Laws and regulations vary by jurisdiction and change over time. Always consult with a licensed attorney in your jurisdiction for advice on specific legal matters. The creators and publishers of this skill disclaim any liability for actions taken or not taken based on the information provided.

---

# Startup Due Diligence Skill

## Overview

Conduct legal due diligence on early-stage US startups (Seed/Series A). This skill supports:
- **Investors**: Identify risks before investing
- **Founders**: Prepare for diligence, fix issues proactively

## Workflow

### Step 1: Intake

Collect context before proceeding:

```
1. Perspective: Investor or Founder?
2. Stage: Pre-seed / Seed / Series A
3. Scope: Full DD or specific area (Corporate, Cap Table, IP, etc.)
4. Company basics: Name, State, Entity type, Industry
```

### Step 2: Document Collection

Based on scope, request documents by category. See `references/checklists/` for complete lists:

| Category | Reference File |
|----------|----------------|
| Corporate & Formation | `references/checklists/corporate.md` |
| Cap Table & Securities | `references/checklists/cap-table.md` |
| Intellectual Property | `references/checklists/ip.md` |
| Employment & Founders | `references/checklists/employment.md` |
| Material Contracts | `references/checklists/contracts.md` |
| Compliance & Regulatory | `references/checklists/compliance.md` |
| Litigation | `references/checklists/litigation.md` |
| Financial | `references/checklists/financials.md` |

### Step 3: Document Review

For each document received:
1. Identify document type and category
2. Check against category-specific criteria
3. Flag issues using severity ratings (see below)
4. Cross-reference with other documents for consistency

**Severity Ratings:**
- 🔴 **CRITICAL**: Deal blocker, must resolve before closing
- 🟠 **MATERIAL**: Significant risk, requires remediation plan
- 🟡 **MINOR**: Should be fixed, but not blocking

See `references/red-flags/common-issues.md` for comprehensive issue patterns.

### Step 4: Issue Analysis

For identified issues, provide:
1. **Description**: What the issue is
2. **Risk**: Why it matters
3. **Remediation**: How to fix it
4. **Timeline**: Estimated effort to resolve
5. **Escalation**: Whether legal counsel required

### Step 5: Report Generation

Generate deliverables using templates in `assets/templates/`.

**CRITICAL: Template Usage Protocol**

NEVER directly edit template .docx files. Always use the deterministic script:

```bash
# 1. Collect data into JSON
cat > data.json << 'EOF'
{
  "COMPANY_NAME": "Acme Inc.",
  "REPORT_DATE": "2024-01-15",
  ...
}
EOF

# 2. Validate data
python scripts/validate_data.py diligence-report data.json

# 3. Populate template (deterministic - only fills {{PLACEHOLDERS}})
python scripts/populate_template.py assets/templates/diligence-report.docx data.json output.docx
```

This ensures template text is NEVER modified - only placeholders are filled.

## Guidance Documents

Load these as needed based on the issues encountered:

| Topic | Reference |
|-------|-----------|
| SAFE notes & convertibles | `references/guidance/safe-notes.md` |
| Delaware C-Corp specifics | `references/guidance/delaware-corp.md` |
| Stock options & 409A | `references/guidance/409a-options.md` |
| Founder equity & vesting | `references/guidance/founder-equity.md` |

## Quick Reference: Common Red Flags

**Corporate**
- Missing board/stockholder consents for key actions
- Charter not filed or not current
- No bylaws or outdated bylaws

**Cap Table**
- Discrepancies between cap table and stock ledger
- Options granted without 409A valuation
- SAFE/note terms not modeled in pro forma

**IP**
- No IP assignment from founders (pre-incorporation work)
- Missing PIIA from contractors who built product
- Open source license violations

**Employment**
- Founder shares not vesting (or fully vested day 1)
- Key employees without offer letters/agreements
- Misclassified contractors

**Compliance**
- No securities filings (Form D, Blue Sky)
- Missing 83(b) elections for early exercises

## Output Formats

1. **Summary Table**: Quick overview of findings by category
2. **Detailed Report**: Full analysis with recommendations (DOCX)
3. **Issue Tracker**: Spreadsheet format for tracking remediation
4. **Document Request List**: Customized checklist for target company

## Disclaimers

- This is diligence assistance, not legal advice
- All findings should be reviewed by qualified legal counsel
- Escalate securities, tax, and regulatory matters to specialists
- Document review is point-in-time; circumstances may change
