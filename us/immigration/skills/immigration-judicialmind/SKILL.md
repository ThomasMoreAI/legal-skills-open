---
name: immigration-judicialmind
title: Immigration Law
description: Immigration law skill for visa applications, compliance, and immigration proceedings. Use when the user needs assistance with work visas, green cards, naturalization, employer compliance, or removal defense. Triggers on keywords like "immigration", "visa", "H-1B", "green card", "I-9", "USCIS", "deportation", "asylum", "work authorization", "PERM", "EB-5", "naturalization".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/immigration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: immigration
language: en
sources:
- title: Perm Recruitment
  path: references/perm-recruitment.md
- title: Visa Comparison
  path: references/visa-comparison.md
---

# Immigration Law

This skill provides expert guidance for employment-based and family-based immigration, compliance, and defense.

## Core Capabilities

### 1. Employment-Based Immigration
- Nonimmigrant work visas
- PERM labor certification
- Immigrant visa petitions
- Employer compliance

### 2. Business Immigration
- Corporate immigration programs
- Intracompany transfers
- Investor visas
- Treaty trader/investor

### 3. Family-Based Immigration
- Immediate relative petitions
- Preference categories
- Consular processing
- Adjustment of status

### 4. Immigration Defense
- Removal proceedings
- Asylum and relief
- Waivers
- Appeals

## Nonimmigrant Work Visas

### Visa Categories Comparison

| Visa | Purpose | Duration | Annual Cap |
|------|---------|----------|------------|
| H-1B | Specialty occupation | 3+3 years | 65,000 + 20,000 |
| L-1A | Intracompany executive/manager | 1+2+2 (7 yr max) | None |
| L-1B | Intracompany specialized knowledge | 1+2+2 (5 yr max) | None |
| O-1 | Extraordinary ability | 3 years + ext. | None |
| TN | USMCA professionals | 3 years + ext. | None |
| E-1 | Treaty trader | 2 years + ext. | None |
| E-2 | Treaty investor | 2 years + ext. | None |
| E-3 | Australian professionals | 2 years + ext. | 10,500 |
| H-2A | Temporary agricultural | 1 year | None |
| H-2B | Temporary non-agricultural | 1 year | 66,000 |

### H-1B Process
```
1. Prevailing Wage Determination (DOL)
2. Labor Condition Application (LCA) filing
3. LCA certified (7 days)
4. H-1B Petition (Form I-129) to USCIS
5. If cap-subject: Registration/lottery (March)
6. If selected: File petition
7. Adjudication (3-8 months, or 15 days premium)
8. If approved: Visa stamping (if abroad) or change of status
```

### H-1B Requirements
**Specialty Occupation**:
- Theoretical and practical application of specialized knowledge
- Bachelor's degree or equivalent minimum requirement
- Degree must be related to position

**LCA Attestations**:
- Prevailing wage or actual wage (whichever higher)
- Working conditions won't adversely affect similarly employed
- No strike or lockout
- Notice to employees

### L-1 Requirements

**L-1A (Manager/Executive)**:
- Employed abroad 1 year in past 3 years
- Manager: Manages organization, department, function, or other managers
- Executive: Directs management, establishes goals, broad discretion

**L-1B (Specialized Knowledge)**:
- Special knowledge of products/services
- Or advanced knowledge of processes/procedures

**Blanket L-1**:
- 3+ years doing business in US
- Combined US annual sales of $25M+, or
- US workforce of 1,000+, or
- 10+ approved L-1s in prior year

## Immigrant Visa (Green Card)

### Employment-Based Categories

| Category | Description | Priority Date |
|----------|-------------|---------------|
| EB-1A | Extraordinary ability | Current (usually) |
| EB-1B | Outstanding professor/researcher | Current (usually) |
| EB-1C | Multinational manager/executive | May be backlogged |
| EB-2 | Advanced degree or exceptional ability | Backlogged (India/China) |
| EB-2 NIW | National Interest Waiver | Backlogged |
| EB-3 | Skilled workers, professionals | Backlogged |
| EB-4 | Special immigrants | Varies |
| EB-5 | Investors | Backlogged (some) |

### PERM Labor Certification Process
```
1. Prevailing wage request to DOL
2. Receive prevailing wage (6-12 months)
3. Recruitment (minimum 30 days)
   - Job order with SWA
   - 2 Sunday newspaper ads
   - 3 additional recruitment steps
4. 30-day quiet period
5. File PERM application (ETA Form 9089)
6. Certification (6-12 months) or audit
7. File I-140 within 180 days of certification
```

### I-140 Immigrant Petition
**Filing Requirements**:
- Approved PERM (EB-2, EB-3) or evidence of category
- Evidence of qualifications
- Evidence of ability to pay (employer)

**Priority Date**: Date PERM filed (or I-140 if no PERM required)

### Adjustment of Status (I-485)
**Concurrent Filing**: When priority date is current
**Requirements**:
- Approved or pending I-140
- Visa number available
- Admissible
- Maintain status

**Benefits of Pending I-485**:
- Employment Authorization (EAD)
- Advance Parole (travel)
- Portability after 180 days

## Employer Compliance

### I-9 Requirements
**Timing**:
- Section 1: First day of employment
- Section 2: Within 3 business days of start

**Documents**:
- List A (identity + work authorization), OR
- List B (identity) + List C (work authorization)

**Common Violations**:
- Incomplete or missing I-9s
- Over-documentation
- Document discrimination
- Untimely completion
- Failure to reverify

### I-9 Audit Defense
```
1. Notice of Inspection received
2. 3 business days to produce I-9s
3. Review and identify deficiencies
4. Technical vs. substantive violations
5. Good faith defense documentation
6. Response to Notice of Intent to Fine
7. Hearing request if needed
```

### LCA Public Access File
**Contents Required**:
- LCA and cover pages
- Prevailing wage documentation
- Actual wage documentation
- Explanation of actual wage system
- Benefits documentation
- Notice of LCA posting

### Corporate Immigration Compliance Program
- [ ] Written immigration policy
- [ ] I-9 procedures and training
- [ ] Visa tracking system
- [ ] Travel policy for visa holders
- [ ] Merger/acquisition due diligence
- [ ] Public access file maintenance
- [ ] H-1B LCA posting procedures
- [ ] Status change/extension tracking
- [ ] Departure procedure for terminated employees

## Removal Defense

### Grounds of Deportability (INA §237)
- Present without admission
- Violated status
- Immigration fraud
- Criminal grounds
- Security grounds
- Public charge (limited)

### Relief from Removal

| Relief | Requirements |
|--------|--------------|
| Cancellation (LPR) | 7 years residence, 5 years LPR, no aggravated felony |
| Cancellation (Non-LPR) | 10 years presence, good moral character, exceptional hardship |
| Asylum | Persecution (race, religion, nationality, political, social group) |
| Withholding | Clear probability of persecution |
| CAT | Torture by government likely |
| Voluntary Departure | Good moral character, means to depart |

### Immigration Court Process
```
Master Calendar → Individual Hearing →
Decision → Appeal to BIA →
Federal Court Review (limited)
```

## Family-Based Immigration

### Immediate Relatives (No Wait)
- Spouse of USC
- Unmarried child under 21 of USC
- Parent of USC (if USC is 21+)

### Preference Categories
| Category | Relationship | Wait Time |
|----------|--------------|-----------|
| F1 | Unmarried adult children of USC | 7+ years |
| F2A | Spouse/minor children of LPR | 2-3 years |
| F2B | Unmarried adult children of LPR | 7+ years |
| F3 | Married adult children of USC | 13+ years |
| F4 | Siblings of adult USC | 15+ years |

## Key Resources

| Source | Content | URL |
|--------|---------|-----|
| USCIS | Forms, case status | uscis.gov |
| DOL FLAG | LCA filing, PERM | flag.dol.gov |
| State Dept | Visa bulletin | travel.state.gov |
| EOIR | Immigration courts | justice.gov/eoir |
| CBP | Entry, ESTA | cbp.gov |

## Integration with Other Skills

- **employment-labor**: Work authorization verification
- **compliance-tracking**: Immigration compliance
- **corporate-ma**: Immigration due diligence
- **litigation**: Removal defense
- **criminal-defense**: Immigration consequences

## Reference Files

For detailed guidance:
- `references/visa-comparison.md` - Visa category analysis
- `references/perm-recruitment.md` - PERM advertising requirements
- `references/i-9-compliance.md` - I-9 audit preparation
