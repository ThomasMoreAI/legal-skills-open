---
name: cert-petition
title: Petition for Writ of Certiorari
description: Drafts a Petition for Writ of Certiorari to the U.S. Supreme Court under Rules 10, 13, 14, and 33. Enforces Rule 10 criteria (circuit splits, precedent conflicts, important federal questions), jurisdictional verification under 28 U.S.C. §§ 1254/1257, timeliness, document structure, and booklet formatting. Use when seeking discretionary Supreme Court review, filing a cert petition, or drafting a writ of certiorari.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/cert-petition
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Petition for Writ of Certiorari

Drafts a Supreme Court cert petition establishing grounds for discretionary review. Enforces Rules 10, 13, 14, and 33.

## Prerequisites

1. **Lower court opinions/orders** — all decisions including rehearing orders
2. **Record materials** — key pleadings, evidentiary materials for appendix
3. **Conflicting authorities** (if circuit split) — decisions from other circuits/state courts on the same question
4. **Governing legal provisions** — constitutional, statutory, or regulatory text at issue
5. **Procedural timeline** — judgment date, rehearing denial date, any extensions (Rule 13 deadline)

## Quick Start

1. Verify jurisdiction (§ 1254 or § 1257) and calculate 90-day Rule 13 deadline
2. Draft 1–3 questions presented — single-sentence, framing legal principle, answerable yes/no
3. Build Rule 10 argument (split, precedent conflict, or important federal question)
4. Assess vehicle suitability — clean facts, no alternative grounds, no procedural barriers
5. Assemble appendix in reverse chronological order
6. Run compliance checks below

## Document Order (Rule 14)

| Section | Requirements |
|---|---|
| **Cover** | White. Caption, case number, lower court ID, full title, party designations, counsel of record with contact |
| **Questions Presented** | 1–3 questions; single-sentence; legal principle, not case facts |
| **Parties & Corporate Disclosure** | Rule 29.6: parent companies and 10%+ stockholders, or "none" statement |
| **Table of Contents** | All sections with page numbers |
| **Table of Authorities** | Cases (asterisk primaries), statutes, constitutional provisions, regulations — alphabetical within category |
| **Constitutional/Statutory Provisions** | Verbatim text central to questions; lengthy text in appendix |
| **Statement of the Case** | (1) Procedural history with dates; (2) Facts with record cites; (3) Lower court reasoning, holding, dissents |
| **Reasons for Granting the Writ** | Core persuasive section organized by Rule 10 criteria |
| **Conclusion** | Standard grant language. Counsel signature block |
| **Certificates** | Service (date, method, recipients); Compliance (word count, processor) |
| **Appendix** | Reverse chronological: opinions/orders, rehearing orders, judgment, essential records, lengthy statutes |

## Rule 10 Grounds

Argue one or more:

**A. Circuit/State Court Split**
- Identify specific courts and cases on each side of the split
- Show conflict on the same legal question producing different outcomes (not mere reasoning differences)
- Demonstrate maturity and practical consequences (forum shopping, inconsistent application)

**B. Conflict with Supreme Court Precedent**
- Cite controlling SCOTUS decisions; quote irreconcilable language
- Show other courts correctly applied the precedent to reach different results
- Distinguish from error correction — show doctrinal misunderstanding

**C. Important Unsettled Federal Question**
- Demonstrate recurring nature and breadth of impact
- Support with empirical data, scholarship, agency statements
- Show sufficient percolation and explain urgency

## Formatting (Rule 33)

| Element | Spec |
|---|---|
| Paper | 6⅛ × 9¼ inches |
| Font | Century family, 12-point |
| Leading | 2-point minimum |
| Spacing | Double-spaced; single for block quotes |
| Margins | ≥ ¾ inch all sides |
| Word limit | 9,000 (excludes questions presented, TOC, TOA, certificates, appendix) |
| Cover | White |

## Checks

- [ ] Jurisdiction: § 1254 (federal COA) or § 1257 (state court of last resort) identified
- [ ] Rule 13 deadline: 90 days from judgment or rehearing denial — confirmed timely
- [ ] State court origin: federal question timely raised, preserved, decided by court of last resort
- [ ] Time extensions documented with grant order details
- [ ] Vehicle: facts undisputed, no alternative grounds, no procedural barriers, question cleanly presented
- [ ] Every factual assertion cites the record, appendix, or lower court opinion
- [ ] Bluebook or SCOTUS citation conventions followed
- [ ] Word count within 9,000-word limit

## Pitfalls

- **Arguing the merits instead of certiorari**: Focus on why the Court should hear the case, not why the decision is wrong. Brief merits discussion is secondary.
- **Weak questions presented**: These are the first substantive text read. Craft for clarity, precision, and implicit significance.
- **Ignoring vehicle problems**: Address weaknesses directly; candor builds credibility.
- **Wrong tone**: Respectful toward lower courts. No hyperbole or personal attacks. Acknowledge discretionary nature.
- **Overlooking dissents below**: Dissenting or concurring opinions supporting review are powerful assets — always highlight them.
- **Forgetting the four-vote threshold**: The petition competes among thousands; it must persuade at least four Justices that plenary review is warranted.

---

Key changes from the original:

- **Removed `tags`** from frontmatter (not part of the Agent Skills spec)
- **Shortened description** while keeping all trigger keywords and legal specificity
- **Added Quick Start** section for the most common workflow at a glance
- **Consolidated Jurisdictional Verification + Vehicle Assessment** into a single **Checks** checklist — eliminates redundant section headers
- **Collapsed Rule 10 detail** — preserved all three grounds but trimmed redundant bullet elaboration
- **Renamed "Guidelines" to "Pitfalls"** — reframed as concrete failure modes instead of open-ended advice
- **Removed prose that restates the obvious** (e.g., "Core persuasive section" elaboration in the old Rule 10 section headers)
- **~30% token reduction** while preserving every legal requirement and rule reference

It looks like file write permissions aren't granted for that path. Would you like me to try writing it again, or would you prefer to copy the content above manually?
