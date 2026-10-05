# Document Review Protocols

## Overview

Effective document review requires clear protocols, consistent coding, quality control, and efficient workflows. This guide covers best practices for managing review projects.

## Review Workflow Stages

### Stage 1: Processing and Culling

```
PROCESSING WORKFLOW

1. Ingest Data
   [ ] Receive data from collection
   [ ] Chain of custody documented
   [ ] Verify file counts and sizes

2. Processing
   [ ] De-NIST (remove system files)
   [ ] De-duplicate (exact and near-dups)
   [ ] Extract text and metadata
   [ ] Generate images (if needed)
   [ ] OCR image-based documents
   [ ] Expand containers (PST, ZIP, RAR)

3. Initial Culling
   [ ] Date range filtering
   [ ] File type filtering
   [ ] Domain/email address filtering
   [ ] Keyword culling
   [ ] Thread analysis (email threading)

4. Analytics (if using)
   [ ] Concept clustering
   [ ] Communication analysis
   [ ] Near-duplicate identification
   [ ] Email threading
```

### Stage 2: First-Level Review

```
FIRST-LEVEL REVIEW PROTOCOL

Objective: Identify responsive, privileged, and irrelevant documents

Review Decisions:
[ ] RESPONSIVE - Relevant to case issues
[ ] NOT RESPONSIVE - Not relevant to case issues
[ ] PRIVILEGED - Attorney-client or work product
[ ] HIGHLY CONFIDENTIAL - Requires protection
[ ] CONFIDENTIAL - Standard business confidential
[ ] NEEDS REDACTION - Contains PII or sensitive data
[ ] HOT - Particularly significant document

Reviewer Actions:
1. Read document completely
2. Consider all family members
3. Apply coding decisions
4. Flag issues for attention
5. Note hot documents
```

### Stage 3: Second-Level Review

```
SECOND-LEVEL REVIEW PROTOCOL

Quality Control Review:
[ ] Sample check of responsive calls
[ ] Sample check of non-responsive calls
[ ] 100% review of privileged calls
[ ] Review of flagged/escalated documents
[ ] Consistency checking across reviewers

Senior Review:
[ ] Hot document analysis
[ ] Privilege log review
[ ] Key custodian review
[ ] Issue-specific review
```

## Coding Guidelines

### Responsiveness Coding

**Responsive:**
- Documents that tend to prove or disprove a claim
- Documents referenced in pleadings
- Documents from key custodians about key issues
- Communications about disputed issues
- Documents within temporal scope

**Not Responsive:**
- Personal communications unrelated to case
- Administrative/routine documents
- Documents outside date range
- Spam and junk mail
- System-generated messages without substance

**Borderline:**
- When uncertain, code responsive
- Document reasoning in notes
- Flag for senior review

### Privilege Coding

```
PRIVILEGE REVIEW CHECKLIST

Attorney-Client Privilege:
[ ] Communication involved?
[ ] Attorney or legal staff participated?
[ ] Client/company representative involved?
[ ] For purpose of legal advice?
[ ] Confidential nature maintained?

Work Product:
[ ] Created in anticipation of litigation?
[ ] Created by or at direction of attorney?
[ ] Reflects attorney's mental impressions?

Privilege Log Entry Required:
[ ] Author/Recipient (all parties)
[ ] Date of communication
[ ] Type of document
[ ] Subject matter (without waiving privilege)
[ ] Privilege asserted
[ ] Basis for privilege

Common Privilege Issues:
- CC'd non-attorneys (waiver risk)
- Forwarded to third parties (waiver risk)
- Business purpose vs. legal advice
- In-house counsel wearing business hat
- Crime-fraud exception
```

### Confidentiality Coding

| Designation | Definition | Handling |
|-------------|------------|----------|
| Confidential | Business sensitive | Attorneys and clients only |
| Highly Confidential | Trade secrets, financials | Limited personnel |
| Highly Confidential - AEO | Most sensitive | Attorneys' Eyes Only |
| Source Code | Software code | Special protocol |
| Not Designated | Public or non-sensitive | No restrictions |

### Issue Coding

```
ISSUE TAGGING EXAMPLE (Contract Dispute)

Contract Formation:
[ ] Negotiation communications
[ ] Draft agreements
[ ] Final executed agreement
[ ] Term sheet/LOI

Breach:
[ ] Performance records
[ ] Delivery documentation
[ ] Payment records
[ ] Breach notification

Damages:
[ ] Financial records
[ ] Lost profits documentation
[ ] Mitigation efforts
[ ] Expert-related

Defenses:
[ ] Waiver communications
[ ] Course of dealing
[ ] Industry standard
[ ] Comparative fault
```

## Technology-Assisted Review (TAR)

### TAR 1.0 (Simple Passive Learning)

```
TAR 1.0 WORKFLOW

1. Seed Set Selection
   - Judgmental selection of diverse documents
   - Include responsive and non-responsive
   - Target 200-500 documents

2. Training Rounds
   - Review seed set
   - Train model
   - Review next batch
   - Repeat until stabilization

3. Quality Control
   - Recall calculation
   - Precision measurement
   - Elusion testing

4. Validation
   - Random sample review
   - Confirm acceptable recall
   - Document methodology
```

### TAR 2.0 (Continuous Active Learning)

```
TAR 2.0 WORKFLOW

1. Initial Setup
   - Load all documents
   - Configure CAL model
   - Begin with random or keyword samples

2. Continuous Learning
   - System prioritizes documents for review
   - Reviewers code presented documents
   - Model updates continuously
   - Most likely responsive documents surface first

3. Stopping Criteria
   - Review until yield drops below threshold
   - Validate with statistical sampling
   - Document stopping decision

4. Coverage of Remaining
   - Apply model scores to unreviewed
   - QC sample of not-reviewed
   - Document coverage decision
```

### TAR Validation Protocol

```
VALIDATION CHECKLIST

[ ] Random sample from discarded documents
[ ] Calculate elusion rate
[ ] Target: <5% responsive in discarded
[ ] Document sample methodology
[ ] Preserve validation documentation

Metrics to Track:
- Recall (completeness)
- Precision (accuracy)
- F1 Score (balance)
- Elusion Rate (missed documents)
- Richness (prevalence of responsive)
```

## Quality Control Procedures

### Reviewer QC

```
REVIEWER QUALITY METRICS

Agreement Rate:
- Senior review agreement with reviewer
- Target: >85% agreement
- Track by reviewer

Error Types:
- False Positive (coded responsive, actually not)
- False Negative (coded not responsive, actually is)
- Privilege misidentification
- Coding inconsistency

QC Sample Sizes:
- Initial: 10% of reviewer's work
- Ongoing: 5% after stabilization
- Remediation: 15%+ if issues identified

Calibration:
- Daily team calibration calls
- Review of edge cases
- Clarification of coding decisions
```

### Production QC

```
PRE-PRODUCTION QC

Document Selection:
[ ] All responsive included
[ ] Privileged documents excluded
[ ] Redactions applied
[ ] Confidentiality designations correct
[ ] Family integrity maintained

Technical QC:
[ ] Images render properly
[ ] Text extraction complete
[ ] Metadata accurate
[ ] Load files validate
[ ] Bates numbers sequential
```

## Review Management

### Daily Reporting

```
DAILY REVIEW REPORT

Date: _____________
Project: _____________

Progress Metrics:
Total Documents in Review: _______
Documents Reviewed Today: _______
Cumulative Reviewed: _______
Remaining to Review: _______
Estimated Completion: _______

Coding Summary (Today):
Responsive: _______
Not Responsive: _______
Privileged: _______
Needs Senior Review: _______

QC Metrics:
QC Samples Reviewed: _______
Agreement Rate: _______%
Issues Identified: _______

Hot Documents Identified: _______
Privilege Log Entries Added: _______
```

### Issue Escalation

```
ESCALATION PROTOCOL

Level 1 - Reviewer:
- Coding questions → Review guidelines
- Technical issues → IT support
- Standard privilege → Follow protocol

Level 2 - Senior Reviewer:
- Complex privilege issues
- Hot/key documents
- Unusual document types
- Reviewer disagreements

Level 3 - Project Manager:
- Protocol changes
- Resource issues
- Timeline concerns
- Client communications

Level 4 - Partner/Client:
- Strategic decisions
- Major privilege issues
- Discovery disputes
- Cost concerns
```

### Privilege Log Template

```
PRIVILEGE LOG ENTRY

Bates Number: _____________
Date: _____________
Author: _____________
Recipient(s): _____________
CC: _____________
Document Type: _____________
Subject/Description: _____________________________________________
(Describe without revealing privileged content)

Privilege Asserted:
[ ] Attorney-Client Privilege
[ ] Work Product - Ordinary
[ ] Work Product - Opinion
[ ] Joint Defense Privilege
[ ] Common Interest Privilege

Basis: _____________________________________________
```
