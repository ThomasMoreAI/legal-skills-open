---
name: proprietary-information-inventions-agreement
title: Proprietary Information and Inventions Agreement (PIIA)
description: Drafts U.S. Proprietary Information and Inventions Agreements (PIIA) for employee or consultant onboarding. Use when drafting a PIIA, inventions assignment, proprietary information agreement, or onboarding confidentiality/IP paperwork. Covers invention assignment, DTSA immunity, prior inventions disclosure, and state-specific carve-outs.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/proprietary-information-inventions-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
tags: [agreement, drafting, transactional]
---

# Proprietary Information and Inventions Agreement (PIIA)

Drafts a U.S. PIIA that assigns inventions and protects proprietary information with DTSA and state carve-out compliance.

## Quick Start

Gather these before drafting:

1. Company legal name, entity type, state of incorporation
2. Individual name, address, role title, effective date
3. Relationship type — employee or consultant
4. Primary work state(s) — drives statutory carve-outs
5. Governing law + forum selection
6. Prior inventions list (if any) and third-party IP restrictions

## Intake Fields

| Field | Req | Notes |
|---|---|---|
| Company name, entity type, state | Yes | Match org docs |
| Individual name, address | Yes | Legal name |
| Relationship type | Yes | Employee or consultant |
| Role title | Yes | Scope context |
| Effective date | Yes | Tie to start date |
| Primary work state(s) | Yes | Drives carve-outs |
| Governing law + forum | Yes | Must not override mandatory law |
| Prior inventions list | Yes | Attach Exhibit if any |
| Devices/personal storage policy | No | If allowed, define controls |
| Post-termination cooperation rate | No | For wage compliance |

## Agreement Sections

| Section | Must Include | Notes |
|---|---|---|
| Parties + consideration | Access to proprietary info as consideration | Reference role |
| Definitions | Proprietary Information, Inventions | Broad but reasonable |
| Confidentiality | Non-disclosure, non-use, care standard, no removal | Survival clause |
| Return of materials | Return, deletion, certification | Include device/cloud |
| Invention assignment | Present assignment, scope triggers | "Hereby assigns" |
| Work for hire | Works of authorship language | Assign if not WFH |
| Prior inventions | Exhibit + representation if blank | Improvements assigned if in scope |
| Cooperation | Disclosure, filings, testimony | Survival + expense reimbursement |
| Power of attorney | Attorney-in-fact for filings | Coupled with interest |
| DTSA notice | 18 U.S.C. 1833(b) immunity | Verbatim safe harbor |
| Governing law/forum | Choice of law + venue | Respect mandatory local law |
| Entire agreement | Integration + amendment | Severability |

## Required Clauses Checklist

Copy and track progress:

- [ ] **Proprietary Information definition** — technical, business, financial, customer, supplier, pricing, marketing, R&D, roadmap, personnel data, and info marked or reasonably understood as confidential
- [ ] **Carve-outs** — public info (no breach), independently developed without company resources, rightfully received without duty
- [ ] **Non-use/non-disclosure** for any purpose outside company duties
- [ ] **Reasonable care standard** (no less than reasonable care)
- [ ] **No unauthorized copying, removal, or personal device storage**
- [ ] **Return of materials** on termination + written certification of return/deletion
- [ ] **Present assignment of Inventions** with scope triggers:
  - [ ] Relates to company business or anticipated R&D
  - [ ] Arises from company work
  - [ ] Uses company time, equipment, supplies, facilities, or trade secrets
- [ ] **Works made for hire** + assignment fallback
- [ ] **Prior Inventions Exhibit** + representation if none
- [ ] **Improvements/derivatives** of prior inventions assigned if within scope
- [ ] **Cooperation obligation** survives termination; reimburse expenses; compensate significant post-termination time
- [ ] **Power of attorney** for filings if non-cooperative/unavailable
- [ ] **DTSA immunity notice** verbatim or substantially similar
- [ ] **Governing law/forum** does not waive mandatory local employee protections

## State Invention Carve-Outs

Include the applicable statutory notice when the work state triggers it. **[VERIFY]** each citation before drafting.

| State | Statute |
|---|---|
| California | Labor Code 2870–2872 |
| Washington | RCW 49.44.140 |
| Illinois | 765 ILCS 1060/1 |
| Minnesota | Stat. 181.78 |
| Utah | Code 34-39-3 |
| North Carolina | Gen. Stat. 66-57.1 |
| Kansas | Stat. 44-130 |
| Delaware | Employee inventions statute |

Include statutory notice text if required by local law.

## Key Templates

Adapt to fit facts.

**Present Assignment:**
> Employee hereby assigns and agrees to assign to Company all right, title, and interest in and to all Inventions that are conceived, developed, reduced to practice, or authored by Employee, alone or jointly with others, during the term of employment and that (a) relate to Company's business or anticipated research or development, (b) result from any work performed for Company, or (c) are developed using Company equipment, supplies, facilities, trade secrets, or time.

**DTSA Immunity Notice:**
> Pursuant to 18 U.S.C. 1833(b), Employee is notified that an individual shall not be held criminally or civilly liable under any federal or state trade secret law for the disclosure of a trade secret that is made (i) in confidence to a government official or to an attorney solely for the purpose of reporting or investigating a suspected violation of law, or (ii) in a complaint or other document filed in a lawsuit or proceeding, if such filing is made under seal.

**Prior Inventions Exhibit:**
> Employee has listed below all inventions, original works of authorship, developments, improvements, and trade secrets that were made by Employee prior to employment and that Employee wishes to exclude from the scope of this Agreement. If no items are listed, Employee represents there are no such prior inventions.

## Pitfalls

- **No non-competes** — do not include unless separately authorized and jurisdictionally compliant
- **Wage compliance** — post-termination cooperation must not create uncompensated work
- **Multi-state roles** — add state-specific rider or carve-out for mandatory local law
- **Confidentiality survival** — obligations survive as long as info remains confidential
- **Personal devices** — if allowed, require approved storage, access controls, and deletion on termination
- **Signature block** — include acknowledgment of voluntary execution and opportunity to consult counsel
- **Overbreadth** — use clear defined terms; avoid restraints that could be deemed unreasonable

---

**Key changes from the original:**

- **Description** tightened — removed redundant enumeration, kept trigger phrases
- **Prerequisites** renamed to **Quick Start** — numbered list instead of prose
- **Monolithic "Output Structure / Process"** broken into distinct scannable sections: Intake Fields, Agreement Sections, Required Clauses Checklist, State Carve-Outs, Key Templates
- **State carve-outs** converted from checkbox list to table — more compact, same info
- **Templates** switched from code fences to blockquotes — cleaner for legal text
- **Guidelines** renamed to **Pitfalls** — reformatted as bolded-key + dash pattern for quick scanning
- **Checklist** items use bold labels for at-a-glance readability; sub-items properly nested
- Reduced from ~115 lines to ~100 lines with better information density
