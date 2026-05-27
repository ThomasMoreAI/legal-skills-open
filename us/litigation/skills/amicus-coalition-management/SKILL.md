---
name: amicus-coalition-management
title: Amicus Coalition Management
description: Manages multi-organization appellate amicus briefs with single-pen drafting, coalition sign-offs, conflict triage, and compliant disclosures. Use when coordinating a coalition amicus brief, managing amicus sign-on, handling FRAP 29 or Supreme Court Rule 37.6 disclosures, or preparing cover and interest sections for multiple amici.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/amicus-coalition-management
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Amicus Coalition Management

Produces a single, compliant coalition amicus brief with auditable approvals and proper disclosures.

## Prerequisites

Gather before starting:

1. Court, case number, caption, and all amicus deadlines
2. Party briefs and key orders (issues and timing)
3. Coalition roster: legal name, display name, entity type, disclosure flags
4. Authority map: who authorizes participation and who approves final text per org
5. Disclosure inputs per amicus: party involvement, third-party funding
6. Filing logistics: counsel-of-record, e-filing system, service and format rules
7. Known red lines and policy constraints per organization

## Required Artifacts

| Artifact | Purpose | Owner |
| --- | --- | --- |
| Workflow memo | Timeline, draft dates, comment windows, sign-off cutoff | Lead counsel |
| Alignment memo | Thesis, unique contribution, red lines | Lead counsel |
| Master roster | Names, display names, entity type, disclosure flags | Coalition manager |
| Comment log | Single consolidated comments per org | Coalition manager |
| Issue log | Conflicts and resolutions | Lead counsel |
| Sign-off log | Written authorizations and timestamps | Coalition manager |
| Disclosure text | FRAP 29(a)(4)(E) / Rule 37.6 statements | Lead counsel |
| Filing checklist | Final compliance verification | Lead counsel |

## Core Workflow

Execute in order:

1. **Verify rules** — Forum-specific amicus rules, timing, word limits, disclosure requirements, cover format, e-filing specs. Flag unconfirmed rules as `[VERIFY]`.
2. **Establish single-pen authority** — Publish workflow memo with hard internal cutoffs.
3. **Align thesis** — Circulate alignment memo; collect red lines before drafting.
4. **Controlled circulation** — One official draft version at a time; strict naming; single comment channel.
5. **Triage conflicts** — Use issue log to resolve or narrow positions without misrepresenting consensus.
6. **Capture sign-offs** — Two-step authorization; exclude any org missing written sign-off by cutoff.
7. **Assemble front matter** — Cover, interest section, disclosures, corporate disclosure statements, counsel block from master roster.
8. **Final QC and file** — Confirm consent or motion for leave; file within required window.

## Timeline (backward from filing deadline)

| Milestone | Timing | Notes |
| --- | --- | --- |
| Alignment memo sent | T-21 to T-14 | Earlier for Supreme Court |
| Draft 1 to coalition | T-14 to T-10 | Substantive comments only |
| Draft 2 (near-final) | T-7 to T-5 | Requires join authorization |
| Final proof | T-3 to T-1 | Non-substantive edits only |
| Filing | T-0 | Confirm consent or leave |

## Key Templates

**Workflow memo**

```text
Subject: Coalition Amicus Brief Workflow and Deadlines

Please provide one consolidated set of comments by [DATE/TIME].
Please provide written authorization to join the brief by [DATE/TIME].
Absent written authorization by that time, your organization will not be listed.
Only non-substantive edits after authorization unless re-confirmed.
```

**Comment instructions** — Direct reviewers to: (1) factual accuracy and citations, (2) legal soundness and non-duplication of party arguments, (3) any language preventing sign-on. Stylistic preferences welcome but may be declined for clarity or word limits.

**Sign-off**

```text
On behalf of [Organization], I confirm I am authorized to approve participation.
[Organization] joins the amicus brief in [Case Name], substantially in the form circulated on [DATE].
Counsel may make non-substantive edits (formatting, citations, typos) before filing.
```

**Disclosure text (verbatim required)**

- **FRAP 29(a)(4)(E)**: Do not paraphrase. Copy the current rule language verbatim from the controlling source, then insert only confirmed case facts.

```text
[PASTE CURRENT FRAP 29(a)(4)(E) LANGUAGE VERBATIM]
[INSERT ONLY CONFIRMED AUTHORSHIP AND FUNDING FACTS FOR THIS BRIEF]
```

- **Supreme Court Rule 37.6**: Do not paraphrase. Copy the current rule language verbatim from the controlling source, then insert only confirmed case facts.

```text
[PASTE CURRENT SUPREME COURT RULE 37.6 LANGUAGE VERBATIM]
[INSERT ONLY CONFIRMED AUTHORSHIP AND FUNDING FACTS FOR THIS BRIEF]
```

**Corporate disclosure (FRAP 26.1 `[VERIFY]`)** — Parent corporations and publicly held corporations owning 10%+ of stock, or "None."

## Conflict Resolution

| Situation | Resolution |
| --- | --- |
| Disagreement on legal test | Statutory-first framing, constitutional fallback |
| Remedy scope conflict | Narrow proposition or avoid remedy specifics |
| Messaging conflict | Prioritize legal clarity over promotional language |

## Cover and Interest Section

- Single coalition descriptor on cover; full roster on inside page or appendix if long.
- Group amici by category in interest section; no promotional adjectives.
- Keep amicus list consistent across cover, interest section, signature block, and disclosures.

## Filing Checklist

- [ ] All listed amici have written authorization in sign-off log
- [ ] Disclosures complete and match verified rule text
- [ ] Corporate disclosure statements included where required
- [ ] Word/page limits, format, and e-filing requirements satisfied
- [ ] Consent obtained or motion for leave prepared and filed

## Pitfalls

- **Never list an organization** without written authorization from an authorized signatory.
- **Never allow parallel drafts** or uncontrolled markup distribution.
- **Never introduce late arguments** without removing equivalent length and re-confirming sign-offs.
- **Never guess citations** — flag unverified sources as `[VERIFY]` for attorney review.
- **Treat all drafts and comments as confidential** — obtain permission before sharing beyond coalition.
- **Require attorney review** of all procedural rules and final filings.
