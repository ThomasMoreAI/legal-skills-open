---
name: court-filings-judicialmind
title: Court Filings
description: Court filing procedures skill for document preparation and submission. Use when the user needs assistance with ECF filing, court formatting rules, service requirements, filing deadlines, or court document preparation. Triggers on keywords like "court filing", "ECF", "CM/ECF", "file", "serve", "service", "filing deadline", "court rules", "local rules", "certificate of service".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/court-filings
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Ecf Guide
  path: references/ecf-guide.md
- title: Formatting Rules
  path: references/formatting-rules.md
- title: Service Methods
  path: references/service-methods.md
---

# Court Filings

This skill provides expert guidance for preparing and filing documents with courts.

## Core Capabilities

### 1. Federal Filing (CM/ECF)
- ECF registration
- Document requirements
- Filing procedures
- Service via ECF

### 2. Document Formatting
- Federal requirements
- Local rule compliance
- Page limits
- Caption requirements

### 3. Service of Process
- Service methods
- Proof of service
- Deadline calculations
- Waivers

### 4. State Court Filing
- State variations
- E-filing systems
- Manual filing
- Fee requirements

## Federal Court Filing (CM/ECF)

### ECF Requirements
```
DOCUMENT REQUIREMENTS FOR CM/ECF

FORMAT
□ PDF format (text-searchable preferred)
□ No password protection
□ No embedded audio/video
□ Bookmarks for exhibits >25 pages

FILE SIZE
□ Maximum 35 MB per document
□ Split larger documents
□ Use correct document naming

SIGNATURES
□ /s/ [Name] format for electronic signatures
□ Scanned signatures for non-filing parties
□ Multiple signatures permitted

REDACTION
□ Social Security numbers (last 4 only)
□ Dates of birth (year only)
□ Financial account numbers (last 4 only)
□ Names of minors (initials only)
□ Home addresses (in certain cases)
```

### Filing Procedure
```
1. LOG IN TO CM/ECF
   - Use PACER credentials (or court-specific)
   - Verify correct court

2. SELECT CASE
   - Enter case number
   - Verify case information

3. SELECT DOCUMENT TYPE
   - Choose appropriate event
   - Link related documents

4. UPLOAD DOCUMENT
   - Main document first
   - Attachments/exhibits separately
   - Verify PDF quality

5. ADD PARTIES
   - Select filing party
   - Link to related parties

6. VERIFY AND SUBMIT
   - Review filing summary
   - Confirm service
   - Complete submission

7. CONFIRM
   - Save Notice of Electronic Filing (NEF)
   - Verify service list
   - Calendar deadlines
```

### NEF Contents
- Transaction receipt
- Document number
- Filing date/time
- Parties served electronically
- Parties requiring manual service

## Document Formatting

### Federal Rules Requirements

**General Format**:
- Paper size: 8.5" x 11"
- Margins: At least 1" all sides
- Font: 14-point (12-point for footnotes)
- Line spacing: Double-spaced (exceptions for block quotes, footnotes)
- Page numbers: Bottom center or lower right

**Caption Format**:
```
UNITED STATES DISTRICT COURT
[DISTRICT NAME]

[PLAINTIFF NAME],            )
                             )
          Plaintiff,         )    Case No. [XX-cv-XXXX-ABC]
                             )
     v.                      )    [DOCUMENT TITLE]
                             )
[DEFENDANT NAME],            )
                             )
          Defendant.         )
_____________________________)
```

### Page Limits (Federal)
| Document | Limit | Rule |
|----------|-------|------|
| Motion | 25 pages | Local rule typical |
| Opposition | 25 pages | Local rule typical |
| Reply | 15 pages | Local rule typical |
| Brief (appeal) | Varies by circuit | FRAP 32 |

### Certificate of Compliance
```
CERTIFICATE OF COMPLIANCE

I certify that this [document type] complies with the [page/word]
limit set forth in [rule] because:

[ ] This document contains [X] words, excluding the parts
    exempted by [rule], OR

[ ] This document does not exceed [X] pages.

Dated: [Date]

                              /s/ [Attorney Name]
                              [Attorney Name]
```

## Service of Process

### Initial Service (FRCP 4)

**Methods for Individuals**:
1. Personal service
2. Leaving at dwelling with person of suitable age
3. Delivering to authorized agent
4. Following state law methods

**Methods for Corporations**:
1. Personal service on officer, managing agent, or general agent
2. Delivery to agent authorized by law
3. Following state law methods

**Methods for Government**:
- United States: FRCP 4(i) (DOJ + agency)
- State: FRCP 4(j) (chief executive officer)

### Waiver of Service (FRCP 4(d))
```
BENEFITS OF WAIVER
- Defendant: 60 days to answer (vs. 21)
- Plaintiff: Avoids service costs
- Both: Good faith cooperation

WAIVER REQUEST
- Mail request + complaint
- Allow 30 days to return waiver
- Prepaid return envelope

CONSEQUENCES OF REFUSAL
- Defendant bears service costs
- Unless good cause shown
```

### Service of Subsequent Documents

**Electronic Service** (via ECF):
- All registered users served automatically
- Effective upon NEF transmission
- +3 days for response deadlines

**Other Methods** (FRCP 5(b)(2)):
| Method | When Complete |
|--------|---------------|
| Personal delivery | When delivered |
| Mail | When mailed |
| Electronic (non-ECF) | When transmitted |
| Leaving at office | When left |

### Certificate of Service
```
CERTIFICATE OF SERVICE

I hereby certify that on [Date], I [served/caused to be served]
a copy of the foregoing [Document Title] on the following:

[VIA CM/ECF:]
[Name], Esq.
[Firm]
[Address]
[Email]

[VIA FIRST CLASS MAIL:]
[Name]
[Address]

                              /s/ [Attorney Name]
                              [Attorney Name]
                              Attorney for [Party]
```

## Filing Deadlines

### Deadline Calculation (FRCP 6)

**Basic Rules**:
1. Exclude trigger day
2. Count all days (including weekends/holidays)
3. If last day is weekend/federal holiday, extend to next business day

**Periods Less Than 11 Days**:
- Exclude weekends and federal holidays from count

**Service Extensions** (FRCP 6(d)):
- +3 days when served by mail, electronic means, or leaving with clerk

### Federal Holidays (Court Closures)
1. New Year's Day
2. Martin Luther King Jr. Day
3. Presidents' Day
4. Memorial Day
5. Juneteenth
6. Independence Day
7. Labor Day
8. Columbus Day
9. Veterans Day
10. Thanksgiving
11. Christmas

### Common Deadlines Quick Reference
| Filing | Deadline |
|--------|----------|
| Answer to complaint | 21 days from service |
| Answer (waiver) | 60 days from waiver request |
| Motion to dismiss | Before responsive pleading |
| Discovery responses | 30 days from service |
| Expert disclosure | Per scheduling order |
| Summary judgment | Per scheduling order |
| Notice of appeal | 30 days (civil); 60 days (gov't party) |

## Local Rules

### Key Local Rule Areas
| Area | Common Variations |
|------|-------------------|
| Page limits | May be shorter than national |
| Font/format | Specific requirements |
| Exhibits | Separate filing requirements |
| Proposed orders | When/how to submit |
| Courtesy copies | Paper copies to chambers |
| Conferences | Meet and confer requirements |
| Briefing schedule | Different timelines |

### Checking Local Rules
```
1. Federal courts: [court].uscourts.gov
2. Standing orders: Individual judge requirements
3. ECF policies: Court-specific procedures
4. Filing fees: Current fee schedule
5. Pro hac vice: Admission requirements
```

## Filing Fees

### Federal Court Fees (2024)
| Filing | Fee |
|--------|-----|
| Civil complaint | $405 |
| Notice of appeal | $605 |
| Habeas corpus | $5 |
| Bankruptcy (Ch. 7) | $338 |
| Bankruptcy (Ch. 11) | $1,738 |
| Bankruptcy (Ch. 13) | $313 |
| Motion fees | Varies |

### Fee Waivers
- In forma pauperis (28 U.S.C. § 1915)
- Application required
- Financial qualification
- Prisoner Litigation Reform Act limitations

## Quality Control Checklist

### Pre-Filing Review
- [ ] Caption correct and complete
- [ ] Case number accurate
- [ ] Document title matches content
- [ ] All pages included
- [ ] Page numbers correct
- [ ] Signature block complete
- [ ] Certificate of service attached
- [ ] Exhibits properly labeled
- [ ] Redactions complete
- [ ] PDF searchable
- [ ] File size acceptable
- [ ] Local rules compliance verified

### Post-Filing
- [ ] NEF received and saved
- [ ] All parties served
- [ ] Response deadline calendared
- [ ] Client copy sent
- [ ] Matter file updated
- [ ] Billing entry made

## Integration with Other Skills

- **litigation**: Motion practice procedures
- **case-management**: Deadline tracking
- **document-drafting**: Pleading preparation
- **brief-writing**: Appellate filings
- **us-federal-courts**: Federal court procedures

## Reference Files

For detailed guidance:
- `references/ecf-guide.md` - CM/ECF procedures
- `references/formatting-rules.md` - Document format requirements
- `references/service-methods.md` - Service of process guide
