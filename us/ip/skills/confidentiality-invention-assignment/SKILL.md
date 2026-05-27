---
name: confidentiality-invention-assignment
title: Confidentiality and Invention Assignment Agreement
description: 'Drafts U.S. Confidentiality and Invention Assignment Agreements (PIIA/CIIA) for employees or contractors. Covers DTSA immunity notice, present-tense invention assignment, prior-inventions schedule, return-of-property, and optional non-solicit/non-compete clauses with state-specific carve-outs. Use when onboarding workers, protecting IP, or forming a company. Trigger: confidentiality agreement, invention assignment, PIIA, CIIA, proprietary information, trade secrets, DTSA, prior inventions, work made for hire.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/confidentiality-invention-assignment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# Confidentiality and Invention Assignment Agreement

Produces an execution-ready PIIA/CIIA protecting trade secrets and assigning work-related IP, compliant with federal DTSA requirements and state invention-assignment carve-outs.

## Quick Start

Collect before drafting:

1. Company legal name, entity type, address
2. Worker name, role, status (employee/contractor), effective date
3. Governing law and primary work location(s)
4. Business description and sensitive-information categories
5. Prior inventions list (or confirmation of none) for Exhibit A
6. Restrictive-covenant decisions: include non-solicit/non-compete? Scope, duration, geography?

## Document Sections

| Section | Key Content |
|---|---|
| Parties & Recitals | Legal names, addresses, role labels; access to confidential info, IP expectations |
| Definitions | Confidential Information; Inventions; Company Business; Trade Secrets |
| Confidentiality | Use-only-for-company, no disclosure, reasonable care, no unauthorized copying |
| Exceptions | Public domain, prior possession, lawful third-party receipt, independent development |
| Term | Trade secrets: indefinite; other confidential info: defined period |
| Return/Destruction | Immediate return, delete copies, written certification |
| DTSA Notice | Whistleblower immunity text (required post-2016-05-11) |
| Invention Assignment | Present assignment + backup "agree to assign"; scope triggers (a)–(c) |
| Prior Inventions | Exhibit A disclosure; "None" representation if empty |
| Disclosure & Cooperation | Prompt written disclosure; filing cooperation; post-termination compensation |
| Work Made for Hire | Copyright ownership + backup assignment |
| Moral Rights | Waiver where jurisdiction permits |
| Restrictive Covenants | Optional non-solicit, non-compete, tolling, blue-pencil |
| Consideration | Employment, continued employment, or separate consideration |
| General Provisions | Governing law, forum/arbitration, entire agreement, severability, notices |
| Acknowledgments | Counsel opportunity, voluntariness, reasonableness, DTSA notice receipt |
| Signatures & Exhibits | Both parties sign; Exhibit A (Prior Inventions), Exhibit B (CA 2870 if applicable) |

## Jurisdiction Compliance Gate

| Jurisdiction | Action |
|---|---|
| Federal | Insert DTSA whistleblower immunity notice (agreements after 2016-05-11) |
| California | Include Lab. Code 2870 carve-out; attach full 2870 text as Exhibit B per 2872 |
| DE, IL, KS, MN, NC, UT, WA | Insert statutory invention-assignment carve-out. `[VERIFY]` current statute text |

## Key Clause Language

**DTSA immunity notice:**

> Employee is hereby notified that under the Defend Trade Secrets Act, an individual shall not be held criminally or civilly liable under any federal or state trade secret law for the disclosure of a trade secret that is made (i) in confidence to a federal, state, or local government official, either directly or indirectly, or to an attorney, and solely for the purpose of reporting or investigating a suspected violation of law; or (ii) in a complaint or other document filed in a lawsuit or other proceeding, if such filing is made under seal.

**Present assignment:**

> Employee hereby assigns and agrees to assign to Company all right, title, and interest worldwide in and to all Inventions that: (a) relate to Company's business or actual or demonstrably anticipated research or development; (b) result from work performed for Company; or (c) are created using Company equipment, supplies, facilities, time, or trade secret information.

**CA 2870 carve-out:**

> This Agreement does not require assignment of any invention that qualifies fully under California Labor Code Section 2870. A copy of Section 2870 is attached as Exhibit B.

**Prior inventions (Exhibit A):**

> Employee lists all inventions, original works, developments, or improvements created before employment that relate to Company's business and are excluded from assignment. If none, Employee indicates "None."

**Return and certification:**

> Upon termination or request, Employee shall return all Company property and Confidential Information and certify in writing that no copies are retained, including from personal devices and cloud accounts.

## Restrictive Covenants Checklist

- [ ] Non-compete prohibited in CA, ND, OK (narrow statutory exceptions only)
- [ ] Non-solicit duration and scope proportional to role and jurisdiction
- [ ] Adequate consideration for any post-employment restriction
- [ ] Geographic scope matches actual business footprint
- [ ] Blue-pencil clause only if jurisdiction enforces reformation

## Pitfalls

- **Overreaching assignment scope** — include jurisdiction-specific carve-outs; do not claim inventions outside statutory triggers
- **Missing DTSA notice** — required for all agreements entered or updated after May 2016; omission forfeits exemplary damages and attorney fees
- **Non-compete in banned states** — prefer narrowly tailored non-solicit instead
- **Stale statutory text** — mark uncertain citations `[VERIFY]` before finalizing
- **Choice-of-law end-run** — forum and governing-law clauses must not waive mandatory worker protections in the employee's state
- **No post-termination cooperation pay** — some jurisdictions require compensation for ongoing IP-cooperation obligations

---

**Key changes from the original:**

- **Removed `tags`** from frontmatter (not part of the Agent Skills spec — trigger guidance belongs in `description`)
- **Collapsed "Prerequisites"** into a tighter "Quick Start" numbered list
- **Consolidated the document outline table** — merged Title/Effective Date, Signatures, and Exhibits rows; shortened all cell text
- **Collapsed the compliance gate** — DE/IL/KS/MN/NC/UT/WA share identical guidance, so they're a single row instead of seven
- **Replaced code-fenced clause templates** with blockquotes — same content, fewer formatting tokens
- **Merged "Guidelines" into a "Pitfalls" section** — each guideline became a named pitfall with a dash explanation, which is the pattern the authoring-skills spec recommends
- **Removed the standalone "Exhibits" subsection** — already covered in the document-sections table
- **Cut ~40% of total tokens** while preserving every legal requirement and clause template
