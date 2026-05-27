---
name: cafa-notice-of-removal
title: CAFA Notice of Removal
description: Drafts a Notice of Removal under the Class Action Fairness Act (CAFA), 28 U.S.C. § 1332(d), transferring a state court class action to federal court. Covers minimal diversity, aggregate amount in controversy exceeding $5 million, 100+ class members, CAFA exceptions, unanimity, timeliness, and required exhibits. Use when a defendant needs to remove a state-filed class action to federal court within 30 days of service.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/cafa-notice-of-removal
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# CAFA Notice of Removal

Drafts a procedurally compliant Notice of Removal invoking federal jurisdiction under CAFA for class actions filed in state court. The removing party bears the burden of establishing jurisdiction; removal statutes are strictly construed against removal.

## Prerequisites

Collect before drafting:

1. **State court complaint** with all exhibits and filing date
2. **Service documents** — date and method of service on each defendant
3. **State court docket sheet**
4. **Party citizenship** — state of incorporation + principal place of business (corporate); domicile (individual)
5. **Class size evidence** — basis for 100+ putative members
6. **AIC basis** — prayer for relief, damages model, or other support for aggregate amount > $5,000,000
7. **Co-defendant consents** — written consent from all other properly served defendants (if not co-signing)

## Output Structure

Draft the notice with these ten sections in order:

### 1. Caption and Title
- Federal district court and correct division; case style mirroring state court caption
- State court case number
- Title: `NOTICE OF REMOVAL PURSUANT TO 28 U.S.C. §§ 1332(d), 1441, AND 1446`

### 2. Introductory Statement
- Identify removing defendant(s), originating state court, and county
- Cite statutory basis: 28 U.S.C. §§ 1441(a), 1446, and § 1332(d)
- State complaint filing date, service date, and affirm filing within 30 days

### 3. CAFA Jurisdictional Elements

| Element | Threshold | Show |
|---|---|---|
| Minimal diversity | ≥1 class member diverse from ≥1 defendant | Named plaintiff + defendant citizenships; corporate = state of incorp. + principal place of business (*Hertz Corp. v. Friend*, 559 U.S. 77) |
| Amount in controversy | >$5M aggregate (excl. interest and costs) | (est. class size) × (per-member damages) + penalties/multipliers/fees. Good-faith short plain statement suffices (*Dart Cherokee*, 574 U.S. 81) |
| Class size | ≥100 putative members | Cite complaint class definition and size allegations |

### 4. CAFA Exceptions Analysis

Address each exception with a risk of application:

| Exception | Statute | Trigger | Counter-argument |
|---|---|---|---|
| Home state | § 1332(d)(4)(B) | Primary defendants + ≥2/3 class are forum-state citizens | Show defendant citizenship outside forum or multi-state class |
| Local controversy | § 1332(d)(4)(A) | ≥2/3 class are forum citizens + significant local defendant + no similar class action in 3 yrs | Show multi-state class or no qualifying local defendant |
| Discretionary decline | § 1332(d)(3) | 1/3–2/3 of class are forum citizens | Apply multi-factor analysis; argue federal interest predominates |

### 5. Procedural History
Chronological narrative: complaint filed, claims asserted, service on each defendant, prior state court activity. If removal is triggered by an amended pleading or other paper, identify the document, date received, and the information that first made removability ascertainable.

### 6. Timeliness

| Trigger | Deadline | Statute |
|---|---|---|
| Initial pleading | 30 days from service | § 1446(b)(1) |
| Amended pleading / other paper | 30 days from receipt | § 1446(b)(3) |
| Outer limit | 1 year from commencement (absent bad faith) | § 1446(c)(1) |

State the specific service date and filing date; show the day count.

### 7. Unanimity of Defendants
- All properly joined and served defendants must consent — § 1446(b)(2)(A)
- All co-sign this notice, or attach written consent from each non-signing served defendant
- Identify unserved defendants; unanimity does not extend to them

### 8. Exhibits

| Exhibit | Contents |
|---|---|
| A | State court complaint + attachments |
| B | Summons and proof of service per defendant |
| C | State court docket sheet |
| D | Co-defendant consents (if applicable) |
| E+ | Amended complaints or other removal-triggering papers (if applicable) |

### 9. Prayer for Relief
Request the Court: (1) accept this Notice; (2) exercise CAFA jurisdiction; (3) deny any remand motion; (4) grant further relief as just and proper. Include § 1446(d) compliance statement re: filing copy with state court clerk and serving all parties.

### 10. Signature Block
Attorney name, bar number, firm, address, phone, email, party represented. FRCP 11 certification. Date = filing date. Comply with local e-filing signature rules.

## Pitfalls and Checks

- **Strict construction**: Ambiguities resolve against removal — ground every jurisdictional assertion in the record
- **CAFA-only basis**: Do not assert § 1331 federal question jurisdiction unless independently supported; state CAFA as sole basis
- **Corporate citizenship**: State of incorporation + principal place of business (nerve center test)
- **Local rules**: Check font, margins, page limits, e-filing requirements, Civil Cover Sheet (JS-44), and CAFA disclosure statement requirements before filing
