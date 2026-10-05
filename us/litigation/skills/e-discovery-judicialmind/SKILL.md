---
name: e-discovery-judicialmind
title: E-Discovery
description: Electronic discovery skill for document review and litigation support. Use when the user needs assistance with ESI collection, document review, privilege logs, predictive coding, or EDRM processes. Triggers on keywords like "e-discovery", "ediscovery", "ESI", "document review", "privilege log", "predictive coding", "TAR", "litigation hold", "custodian", "production", "Relativity".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/e-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Hold Templates
  path: references/hold-templates.md
- title: Production Specs
  path: references/production-specs.md
- title: Review Protocols
  path: references/review-protocols.md
---

# E-Discovery

This skill provides expert guidance for electronic discovery processes from preservation through production.

## Core Capabilities

### 1. Preservation
- Litigation holds
- Custodian identification
- Data mapping
- Defensible preservation

### 2. Collection
- Forensic collection
- Cloud data
- Mobile devices
- Structured data

### 3. Processing & Review
- De-duplication
- Document review workflows
- Privilege review
- Technology-assisted review

### 4. Production
- Production formats
- Privilege logs
- Quality control
- Load files

## EDRM Framework

### Electronic Discovery Reference Model
```
┌────────────────────────────────────────────────────────────────────┐
│                    EDRM FRAMEWORK                                   │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Information    →  Identification  →  Preservation  →  Collection  │
│  Governance                                                         │
│                                                                     │
│              ↓           ↓              ↓              ↓           │
│                                                                     │
│  Processing  →  Review  →  Analysis  →  Production  →  Presentation│
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

Volume decreases as you move through the EDRM →
```

## Litigation Hold

### Hold Notice Elements
```
1. INTRODUCTION
   - Matter identification
   - Hold effective date
   - Importance of compliance

2. SCOPE OF HOLD
   - Relevant time period
   - Subject matter
   - Key custodians/departments

3. DATA TYPES TO PRESERVE
   - Email and attachments
   - Documents (electronic and paper)
   - Databases
   - Instant messages/collaboration tools
   - Mobile devices
   - Social media
   - Voicemail
   - Backup tapes (if relevant)

4. PRESERVATION INSTRUCTIONS
   - Do not delete, destroy, modify
   - Suspend auto-delete policies
   - Preserve metadata
   - Report relevant information

5. ACKNOWLEDGMENT
   - Require written acknowledgment
   - Deadline for response

6. CONTACT INFORMATION
   - Questions/reporting
   - Legal hold coordinator
```

### Spoliation Risks
**Factors Courts Consider**:
- Duty to preserve (when triggered)
- Reasonable anticipation of litigation
- Culpability (negligence vs. willful)
- Relevance of lost evidence
- Prejudice to other party

**Sanctions** (FRCP 37(e)):
- Curative measures (any loss with prejudice)
- Adverse inference/dismissal (intent to deprive only)

## Data Sources

### Common ESI Sources
| Source | Considerations |
|--------|---------------|
| Email (Exchange/O365) | Largest volume, journal vs. mailbox |
| File shares | Permissions, metadata preservation |
| Cloud storage | OneDrive, SharePoint, Google Drive |
| Collaboration (Teams/Slack) | Messages, channels, files |
| Mobile devices | SMS, apps, MDM considerations |
| Social media | Preservation challenges, authentication |
| Databases | Structured data, reporting |
| Legacy systems | Format conversion, access |
| Backup tapes | Disaster recovery vs. litigation |

### Custodian Interview Checklist
- [ ] Role and responsibilities
- [ ] Relevant time period involvement
- [ ] Email accounts (primary, shared, personal)
- [ ] File storage locations
- [ ] Mobile devices
- [ ] Collaboration tools
- [ ] Cloud storage (personal and business)
- [ ] Home computer use
- [ ] Departed employee handoffs
- [ ] Relevant communications
- [ ] Key documents
- [ ] Third-party systems

## Processing

### Processing Steps
1. **Ingestion**: Load raw data
2. **Expansion**: Extract containers (PST, ZIP)
3. **Hashing**: Generate MD5/SHA-1 values
4. **De-duplication**: Global or custodian-level
5. **De-NISTing**: Remove system files
6. **Text extraction**: OCR for images
7. **Metadata extraction**: Populate fields
8. **Exception handling**: Password files, corrupted
9. **QC**: Validate processing accuracy

### De-Duplication Options
| Method | Approach | Use Case |
|--------|----------|----------|
| Global | Remove all duplicates | Maximum reduction |
| Custodian | Keep one per custodian | Preserve custodian context |
| Exact | MD5 hash match | Standard approach |
| Near-duplicate | Similarity clustering | Review efficiency |

## Document Review

### Review Workflow
```
1. First-Level Review
   - Responsiveness determination
   - Privilege identification
   - Issue coding

2. Second-Level Review
   - QC sampling
   - Privilege review
   - Confidentiality designations

3. Final Review
   - Production preparation
   - Privilege log generation
   - Redaction review
```

### Coding Fields
| Field | Purpose | Options |
|-------|---------|---------|
| Responsiveness | Relevant to case | Responsive, Non-Responsive, Needs Review |
| Privilege | Protected communications | AC, WP, Joint Defense, None |
| Confidentiality | Protective order | Confidential, Highly Confidential, AEO |
| Issues | Subject matter | Case-specific coding |
| Hot documents | Key evidence | Hot, Interesting, Not Hot |

### Technology-Assisted Review (TAR)

**TAR 1.0 (Simple Active Learning)**:
```
1. Create seed set (human-coded)
2. Train classifier
3. Review top-ranked documents
4. Iterate until stable
5. Validate with sampling
```

**TAR 2.0 (Continuous Active Learning)**:
```
1. Start reviewing any documents
2. Algorithm learns from each decision
3. Prioritizes documents for review
4. Continues until coverage sufficient
5. Validates with statistical sampling
```

### TAR Protocol Considerations
- Seed set composition
- Training methodology
- Validation metrics
- Recall targets
- Quality control sampling
- Disclosure to opposing counsel

## Privilege Review

### Privilege Categories
| Privilege | Elements |
|-----------|----------|
| Attorney-Client | Communication, with attorney, for legal advice, confidential |
| Work Product | Prepared in anticipation of litigation, by/for party |
| Joint Defense | Common interest, joint defense agreement |
| Deliberative Process | Pre-decisional, deliberative (government) |

### Privilege Log Requirements (FRCP 26(b)(5))
**Required Information**:
- Document date
- Author
- Recipients (To, CC, BCC)
- Document type
- Subject matter (without revealing privileged content)
- Privilege asserted

### Privilege Log Template
```
| Bates Range | Date | Author | Recipients | Description | Privilege |
|-------------|------|--------|------------|-------------|-----------|
| ABC001234 | 1/1/24 | J. Smith (Atty) | B. Jones (Client) | Email re: legal advice on contract | AC |
| ABC001235 | 1/2/24 | Litigation Team | | Memo analyzing litigation strategy | WP |
```

### Clawback Agreements (FRE 502)
**502(d) Order Benefits**:
- Inadvertent production doesn't waive privilege
- Binding on all parties and future cases
- Reduces privilege review costs

## Production

### Production Formats
| Format | Description | Use Case |
|--------|-------------|----------|
| TIFF | Image files, Bates stamped | Standard production |
| Native | Original file format | Spreadsheets, databases |
| PDF | Searchable PDF | Some courts prefer |
| Paper | Hard copy | Legacy requirement |

### Load File Components
| File | Contents |
|------|----------|
| DAT/CSV | Metadata fields, delimiters |
| OPT | Image cross-reference |
| Text files | Extracted/OCR text |
| Native files | Original format documents |
| Image files | TIFF/PDF renditions |

### Production Specifications
```
PRODUCTION SPECIFICATIONS

IMAGES
- Format: Single-page TIFF, Group IV
- Resolution: 300 DPI
- Color: Color for photographs, B&W for text

LOAD FILE
- Metadata: UTF-8 encoded, comma delimited
- Field delimiter: ASCII 20
- Text qualifier: ASCII 254
- Newline: ASCII 174

NATIVE FILES
- Produce in native: Excel, PowerPoint, Audio, Video
- Naming convention: Bates number

TEXT
- Extracted text at document level
- Naming: [BegDoc].txt

BATES NUMBERING
- Prefix: ABC
- Format: ABC000000001
```

## Proportionality (FRCP 26(b)(1))

### Proportionality Factors
1. Importance of issues at stake
2. Amount in controversy
3. Parties' relative access to information
4. Parties' resources
5. Importance of discovery to resolving issues
6. Whether burden outweighs benefit

### Cost Considerations
| Phase | Cost Drivers |
|-------|--------------|
| Collection | Volume, source complexity, forensics |
| Processing | Volume, file types, exceptions |
| Hosting | Volume, review platform |
| Review | Document count, complexity, reviewers |
| Production | Format, QC requirements |

## Platform Features (Relativity Example)

### Key Features
- Analytics (clustering, email threading)
- TAR (Active Learning)
- Structured Analytics (near-dupes, textual analysis)
- Reviewer tools (coding layouts, shortcuts)
- Dashboards (progress, QC metrics)
- Productions (automated workflows)

### Search Types
| Type | Use |
|------|-----|
| Keyword | Simple term searching |
| Boolean | AND, OR, NOT, proximity |
| Regex | Pattern matching |
| Concept | Find similar documents |
| dtSearch | Fast indexed searching |

## Integration with Other Skills

- **litigation**: Discovery in civil litigation
- **criminal-defense**: Criminal discovery
- **corporate-ma**: Transaction data rooms
- **legal-analytics**: Review metrics
- **compliance-tracking**: Regulatory investigations

## Reference Files

For detailed guidance:
- `references/hold-templates.md` - Litigation hold samples
- `references/review-protocols.md` - Review workflow guides
- `references/production-specs.md` - Standard specifications
