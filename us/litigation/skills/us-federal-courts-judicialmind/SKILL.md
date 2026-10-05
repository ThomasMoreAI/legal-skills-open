---
name: us-federal-courts-judicialmind
title: US Federal Courts
description: US federal court practice skill for federal jurisdiction and procedures. Use when the user needs assistance with federal court jurisdiction, federal rules of procedure, circuit-specific rules, SCOTUS practice, or federal court procedures. Triggers on keywords like "federal court", "federal jurisdiction", "FRCP", "circuit court", "SCOTUS", "Supreme Court", "district court", "federal rules", "diversity jurisdiction", "federal question".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/us-federal-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Circuit Guide
  path: references/circuit-guide.md
- title: Jurisdiction Analysis
  path: references/jurisdiction-analysis.md
- title: Scotus Practice
  path: references/scotus-practice.md
---

# US Federal Courts

This skill provides expert guidance for practice in the United States federal court system.

## Core Capabilities

### 1. Subject Matter Jurisdiction
- Federal question jurisdiction
- Diversity jurisdiction
- Supplemental jurisdiction
- Removal

### 2. Federal Procedure
- Federal Rules of Civil Procedure
- Federal Rules of Evidence
- Local rules
- Standing orders

### 3. Circuit Practice
- Circuit-specific rules
- En banc procedures
- Precedent analysis
- Circuit splits

### 4. Supreme Court Practice
- Certiorari petitions
- Merits briefing
- Original jurisdiction
- Emergency applications

## Federal Court Structure

### Court Hierarchy
```
┌─────────────────────────────────────────┐
│         SUPREME COURT OF THE            │
│           UNITED STATES                 │
│    (9 Justices, discretionary review)   │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│       COURTS OF APPEALS (13)            │
│    First through Eleventh Circuits      │
│    D.C. Circuit                         │
│    Federal Circuit (specialized)        │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│       DISTRICT COURTS (94)              │
│    At least one per state               │
│    Trial courts of general jurisdiction │
└─────────────────────────────────────────┘
                    │
         ┌─────────┴─────────┐
         ▼                   ▼
┌─────────────────┐  ┌─────────────────┐
│ BANKRUPTCY      │  │ MAGISTRATE      │
│ COURTS          │  │ JUDGES          │
│ (Article I)     │  │ (28 U.S.C. 636) │
└─────────────────┘  └─────────────────┘
```

### Circuit Map
| Circuit | States/Territories |
|---------|-------------------|
| First | ME, MA, NH, RI, PR |
| Second | CT, NY, VT |
| Third | DE, NJ, PA, VI |
| Fourth | MD, NC, SC, VA, WV |
| Fifth | LA, MS, TX |
| Sixth | KY, MI, OH, TN |
| Seventh | IL, IN, WI |
| Eighth | AR, IA, MN, MO, NE, ND, SD |
| Ninth | AK, AZ, CA, HI, ID, MT, NV, OR, WA, Guam, N. Mariana |
| Tenth | CO, KS, NM, OK, UT, WY |
| Eleventh | AL, FL, GA |
| D.C. | Washington, D.C. |
| Federal | Patents, international trade, claims against US |

## Subject Matter Jurisdiction

### Federal Question (28 U.S.C. § 1331)
**Requirement**: Civil action arising under Constitution, laws, or treaties of United States

**Well-Pleaded Complaint Rule**:
- Federal issue must appear on face of complaint
- Cannot anticipate federal defense
- Federal ingredient must be essential to claim

**Grable Analysis** (state claims with federal elements):
1. Federal issue necessarily raised
2. Actually disputed
3. Substantial
4. Capable of resolution without disrupting federal-state balance

### Diversity Jurisdiction (28 U.S.C. § 1332)
**Requirements**:
- Complete diversity between plaintiffs and defendants
- Amount in controversy exceeds $75,000

**Citizenship Determination**:
| Entity | Citizenship |
|--------|-------------|
| Individual | Domicile |
| Corporation | State of incorporation AND principal place of business |
| LLC | Citizenship of all members |
| Partnership | Citizenship of all partners |
| Trust | Depends on state law (usually trustee) |

**Amount in Controversy**:
- Legal certainty test (amount not recoverable beyond doubt)
- Aggregation rules
- Injunctive relief valuation

### Supplemental Jurisdiction (28 U.S.C. § 1367)
**Permits**: Claims that share common nucleus of operative fact

**Limitations** (§ 1367(b) in diversity cases):
- Claims by plaintiffs against persons made parties under Rule 14, 19, 20, 24
- Claims by persons proposed to be joined as plaintiffs under Rule 19
- Claims by persons seeking to intervene as plaintiffs under Rule 24

**Discretionary Decline** (§ 1367(c)):
- Novel or complex state law issue
- State claim substantially predominates
- District court has dismissed all federal claims
- Exceptional circumstances

### Removal (28 U.S.C. § 1441)
**Procedure**:
1. File notice of removal (30 days from service)
2. Include all pleadings and orders
3. File in district court for state court location
4. Notify state court
5. Notify all parties

**Limitations**:
- Diversity: No removal if any defendant is citizen of forum state
- One-year limit for diversity cases (unless bad faith)
- All defendants must join (unanimity rule)

**Remand**: Motion within 30 days (except subject matter jurisdiction)

## Federal Rules of Civil Procedure

### Key Rules Quick Reference
| Rule | Topic |
|------|-------|
| 4 | Service of process |
| 8 | Pleading requirements |
| 9 | Particularity requirements |
| 11 | Representations and sanctions |
| 12 | Defenses and objections |
| 15 | Amended and supplemental pleadings |
| 23 | Class actions |
| 26 | Discovery scope and duty |
| 30 | Depositions |
| 33-36 | Written discovery |
| 37 | Discovery sanctions |
| 50 | Judgment as a matter of law |
| 56 | Summary judgment |
| 59 | New trial; altering judgment |
| 60 | Relief from judgment |

### Pleading Standards
**Notice Pleading** (Rule 8):
- Short and plain statement of claim
- Showing pleader entitled to relief

**Heightened Pleading** (Rule 9(b)):
- Fraud: State with particularity
- Mistake: State with particularity

**Plausibility** (Twombly/Iqbal):
- Factual content allowing reasonable inference of liability
- More than speculative
- Not merely conceivable

### Discovery Scope
**Relevance** (Rule 26(b)(1)):
- Relevant to any party's claim or defense
- Proportional to needs of case

**Proportionality Factors**:
1. Importance of issues at stake
2. Amount in controversy
3. Parties' relative access to information
4. Parties' resources
5. Importance of discovery to resolving issues
6. Whether burden outweighs benefit

### Discovery Limits (Default)
| Discovery | Limit |
|-----------|-------|
| Depositions | 10 per side |
| Deposition length | 7 hours/day |
| Interrogatories | 25 (including subparts) |
| Requests for admission | No numeric limit |
| Requests for production | No numeric limit |

## Federal Rules of Evidence

### Key Rules
| Rule | Topic |
|------|-------|
| 401-403 | Relevance |
| 404-405 | Character evidence |
| 407-411 | Policy exclusions |
| 501-502 | Privileges |
| 601-615 | Witnesses |
| 701-706 | Opinion testimony |
| 801-807 | Hearsay |
| 901-903 | Authentication |
| 1001-1008 | Best evidence |

### Hearsay Exceptions (Rule 803)
1. Present sense impression
2. Excited utterance
3. State of mind
4. Medical diagnosis/treatment
5. Recorded recollection
6. Business records
7. Public records
8. Learned treatises
9. Reputation (character, personal/family history)

### Hearsay Exceptions (Unavailable - Rule 804)
- Former testimony
- Dying declaration
- Statement against interest
- Statement of personal/family history
- Forfeiture by wrongdoing

## Circuit-Specific Considerations

### Circuit Splits to Know
- Document when circuits disagree
- Identify which circuits' law applies
- Consider Supreme Court resolution likelihood
- Use splits strategically in briefing

### Local Rules Checklist
- [ ] Page/word limits
- [ ] Filing deadlines
- [ ] Format requirements
- [ ] Mandatory disclosures
- [ ] Meet and confer requirements
- [ ] Mediation/ADR requirements
- [ ] Proposed orders
- [ ] Courtesy copies

## Supreme Court Practice

### Certiorari Petition
**Filing Deadline**: 90 days from judgment (or denial of rehearing)

**Petition Contents**:
1. Questions presented
2. List of parties
3. Table of contents and authorities
4. Opinions below
5. Jurisdiction
6. Constitutional and statutory provisions
7. Statement of the case
8. Reasons for granting writ
9. Conclusion

**Page Limits**: 9,000 words (or 40 pages)

### Cert-Worthy Factors
1. Circuit split
2. Important federal question
3. Lower court departed from Supreme Court precedent
4. Lower court decided important question that should be settled

### Merits Briefing
| Brief | Limit | Deadline |
|-------|-------|----------|
| Petitioner | 15,000 words | 45 days after cert |
| Respondent | 15,000 words | 30 days after opening |
| Reply | 6,000 words | 30 days after respondent |
| Amicus | 9,000 words | 7 days after supported party |

## Pro Hac Vice Admission

### Typical Requirements
- [ ] Member in good standing in another bar
- [ ] Motion for admission
- [ ] Certificate of good standing
- [ ] Association with local counsel (some courts)
- [ ] Admission fee
- [ ] Compliance with local rules

## Integration with Other Skills

- **litigation**: Trial and motion practice
- **court-filings**: ECF procedures
- **brief-writing**: Federal appellate briefs
- **legal-research**: Federal precedent
- **case-management**: Federal deadlines

## Reference Files

For detailed guidance:
- `references/jurisdiction-analysis.md` - Jurisdiction determination guide
- `references/circuit-guide.md` - Circuit-by-circuit rules
- `references/scotus-practice.md` - Supreme Court procedures
