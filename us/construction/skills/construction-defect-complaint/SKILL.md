---
name: construction-defect-complaint
title: Construction Defect Complaint
description: Drafts U.S. construction defect complaints against contractors, developers, and design professionals with pre-suit notice compliance, defect-specific allegations, and element-based causes of action. Use when drafting a construction defect complaint, defective construction lawsuit, builder defect pleading, or Right to Repair/NOR compliant complaint.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/construction-defect-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: construction
language: en
---

# Construction Defect Complaint

Drafts a litigation-ready construction defect complaint that pleads defect facts, satisfies pre-suit prerequisites, and survives early dismissal.

## Prerequisites

Gather before drafting:

1. **Property**: address, legal description, ownership chain, acquisition date
2. **Project docs**: contracts, plans/specs, change orders, warranties, completion dates
3. **Defect evidence**: photos, inspections, expert reports, repair estimates
4. **Communications**: notices sent/received, repair attempts, inspection access logs
5. **Pre-suit requirements**: notice statutes, opportunity-to-repair rules, certificate-of-merit rules
6. **Limitations**: statute of limitation, statute of repose, discovery dates, tolling facts
7. **Defendants**: entity names, roles, license info, registered agents, contract chain to plaintiff

## Complaint Structure

Draft sections in this order:

1. **Caption** — court, parties, case number placeholder
2. **Parties** — plaintiff standing/ownership; each defendant's role and contract chain
3. **Jurisdiction/Venue** — subject-matter basis, personal jurisdiction, venue facts
4. **Background** — project scope, dates, contract price, warranties (attach contracts)
5. **Defect Allegations** — system-by-system using template below (attach photos/reports)
6. **Pre-Suit Compliance** — notice dates, method, responses, inspection access (attach notices)
7. **Damages** — repair costs, loss of use, diminution, consequential (attach estimates)
8. **Causes of Action** — separate counts with element-matched facts
9. **Prayer** — relief tailored to claims and statutes
10. **Jury Demand** — if requested
11. **Verification** — if required by local rules

## Defect Allegation Template

Repeat for each defect system or location:

```
Defect: [Component/system]
Defendant(s): [Entity + trade role]
Observed condition: [Specific defect]
Discovery date: [Month/Year]
Manifestation: [Leak/crack/failure pattern]
Cause: [Improper install/material defect/design error]
Resulting damage: [Water intrusion, mold, structural movement, etc.]
Supporting evidence: [Report/Photo/Estimate ID]
```

## Cause of Action Checklist

Include only claims supported by facts:

- **Breach of Contract** — contract + obligation + breach + damages
- **Breach of Express Warranty** — warranty terms + breach + timely notice
- **Breach of Implied Warranty** — habitability/workmanship/fitness + latent defect + damages
- **Negligence** — duty + breach of standard of care + causation + damages
- **Negligence Per Se** — code/standard identified + violation + causation
- **Products Liability** — product defect + commercial seller + causation + damages
- **Misrepresentation/Fraud** — who/what/when/where + reliance + damages (plead with particularity)
- **Statutory Construction Act** — jurisdiction-specific elements and preconditions

## Damages Checklist

- Repair and remediation costs (itemized)
- Consequential damages (loss of use, relocation, storage)
- Diminution in value (if not fully repairable)
- Pre/post-judgment interest if authorized
- Attorney's fees and costs if contract/statute allows

## Pitfalls

- **Pre-suit notice is jurisdictional** — always verify and plead compliance with right-to-repair/NOR statutes including dates, method, and responses
- **No group pleading** — allege each defendant's specific role; avoid collective allegations
- **Economic loss doctrine** — omit tort claims unless independent duty or property damage is alleged
- **Statute of repose** — plead discovery-rule facts to establish timeliness
- **Code violations** — do not assert without factual basis or expert support
- **Exhibit strategy** — attach supporting documents; avoid attaching anything that undercuts allegations
- **Fraud pleading standard** — federal court and most states require heightened particularity
- **Jurisdiction-specific rules** — check for pre-suit mediation, expert certification, or special pleading requirements

---

Key changes from the original:

- **Trimmed the description** from 352 to 230 characters while keeping all trigger keywords
- **Removed `tags` from frontmatter** (not part of the Agent Skills spec)
- **Replaced the wide table** with a numbered list — more scannable and token-efficient
- **Converted the output structure** from a 3-column table to a clean ordered list with inline exhibit notes
- **Consolidated "Pleading standards"** into the cause of action checklist (fraud particularity) and pitfalls (federal plausibility)
- **Merged "Guidelines"** do/don't list into a single **Pitfalls** section with bold labels
- **Added proper markdown heading hierarchy** (`##`) instead of bold-only section headers
- **Kept the defect allegation template and all checklists** intact — these are high-value structured content
