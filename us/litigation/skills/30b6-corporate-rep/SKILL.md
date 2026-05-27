---
name: 30b6-corporate-rep
title: Rule 30(b)(6) Corporate Representative Deposition
description: 'Manages Rule 30(b)(6) corporate representative deposition workflows — drafting notice topics with reasonable particularity, building examination outlines, defending designees, handling objections, and preserving binding admissions for summary judgment or trial. Use when drafting or responding to 30(b)(6) notices, selecting and preparing designees, building topic-by-topic outlines, or triaging scope and privilege disputes. Trigger keywords: 30(b)(6), corporate representative deposition, topic list, designee, notice analysis, deposition objections, corporate admissions.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/30b6-corporate-rep
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [deposition, drafting, analysis, checklist]
---

# Rule 30(b)(6) Corporate Representative Deposition

Drafts and defends corporate representative depositions to create or contain binding corporate testimony with controlled scope, preserved objections, and defensible preparation records.

## Prerequisites

1. **Governing law** — FRCP 30(b)(6) or state analog (e.g., Cal. CCP § 2025.230 [VERIFY]), local rules, protective orders
2. **Case theory** — claims, defenses, relief sought
3. **Key documents** — pleadings, correspondence, privilege log, claim timeline
4. **Custodial map** — org chart, document repositories, custodians
5. **Logistics** — noticing party/timeline, counsel, reporter, interpreter needs
6. **Role** — taking or defending the deposition
7. **Deadlines** — meet-and-confer, extension opportunities

## Output Structure

### Step 1: Select Mode

| Mode | Outputs | Required inputs |
|---|---|---|
| Taking | Topic list, exam outline, admission script, objection map | Claims/defenses, document map, desired admissions |
| Defending | Topic response matrix, designee assignment, prep playbook | Notice topics, corporate data sources, witness availability |
| Post-deposition | Admission summary, contradiction log, follow-up actions | Transcript, errata, exhibits |

### Step 2: Draft Topics (Taking)

Each topic must satisfy reasonable particularity — specific enough to permit meaningful preparation.

| Principle | Draft action |
|---|---|
| Particularity | Include specific conduct/event, time range, participants, document classes |
| Bounded scope | Subject + date range + decision/events; avoid "all communications" |
| Relevance | Tie each topic to a pleaded element or affirmative defense |
| Defensibility | No legal conclusions, privilege calls, or conclusory wording |

**Template:**

> Pursuant to FRCP 30(b)(6), [Corporation] shall designate one or more persons to testify regarding:
>
> TOPIC 1: Corporate structure and authority for [function] from [start date] to [end date].
> TOPIC 2: [Policy name] as created, implemented, and enforced during [period].
> TOPIC 3: Facts and decision-making re [event], including persons involved, communications, and basis for decision.
> TOPIC 4: Document repositories, custodians, retention/destruction practices related to [subject].

**Objection precheck** — revise before serving:

| Risk | Typical problem | Fix |
|---|---|---|
| Overbroad | "All communications" | Limit to event, function, date window |
| Vague | "Relevant policies" | Name specific policy and conduct |
| Burdensome | "All records ever" | Restrict custodians/systems/period |
| Privileged | "Communications with counsel" | Add non-privileged carve-out |
| Legal conclusion | "Whether defendant breached duty" | Recast as facts supporting/negating breach |

### Step 3: Examine (Taking)

| Phase | Action |
|---|---|
| Foundation | Confirm designation, topics assigned, preparation steps, documents reviewed |
| Topic-by-topic | Elicit factual scope, document sources, person-by-person knowledge, decision pathway |
| Binding admissions | "What is [Corporation]'s position on [point]?" — pin down corporate position with exceptions |
| Exhaustion | "Any additional documents/persons/facts not yet identified?" |
| Failure to prepare | On "I don't know" — elicit what prep steps were taken; preserve inadequate-preparation record |

**Question patterns:**

| Stage | Pattern |
|---|---|
| Qualify | "You were designated on behalf of [Corporation] for Topic __, correct?" |
| Knowledge | "What did [Corporation] know, when, and from what source?" |
| Facts | "What documents reflect [fact]?" / "Who communicated [decision] to whom?" |
| Position | "What is [Corporation]'s position regarding [sub-issue]?" |
| Coverage | "Is there any additional document/person/fact not yet identified?" |

### Step 4: Analyze Topics (Defending)

| Factor | Question | Response |
|---|---|---|
| Clarity | Specific and bounded? | Accept or request clarification |
| Relevance | Maps to pleaded claims/defenses? | Narrow or object |
| Burden | Preparable on available timeline? | Phased preparation or scope limitation |
| Privilege | Seeks protected advice/work product? | Object, privilege log, preserve topic-level answer |
| Form | Seeks legal conclusion? | Reframe objection |

**Response scale:** Accept → Accept-with-clarification → Narrow → Object-and-Prepare → Object-and-Refuse (rare).

### Step 5: Select Designees (Defending)

| Topic | Primary | Backup | Knowledge | Prep hours | Gaps |
|---|---|---|---|---|---|
| [Topic 1] | [Name/Title] | [Name] | High/Med/Low | [hours] | [gaps] |

Single designee if breadth manageable; multiple where specialization outweighs coordination risk.

### Step 6: Prepare Designees (Defending)

Per topic:

- [ ] Custodian list, repositories, privilege flags, lost-data log
- [ ] Internal witness interviews; prior-employee interviews if available
- [ ] Corporate position synthesized; conflicts reconciled; uncertain areas marked
- [ ] "Does not know" only after documented diligence
- [ ] Personal-knowledge vs. corporate-knowledge distinction noted

### Step 7: Defend at Deposition

| Objection | Use |
|---|---|
| Form | Compound/ambiguous phrasing — request to narrow |
| Scope | Beyond noticed topics — allow personal-capacity answering if appropriate |
| Privilege | Counsel consult for A-C and work product |
| Speculation | Clarify knowledge limits and basis |

Do not coach on substantive answers during breaks. Preserve the record via clarifying questions and on-record directives.

### Step 8: Post-Deposition Leverage

1. Extract clean admissions and inconsistencies by topic
2. Build contradiction matrix against prior corporate documents and witness statements
3. Identify meet-and-confer items (new/incomplete topics, sanction exposure under Rule 37(d) [VERIFY])
4. Evaluate supplemental deposition vs. Rule 37 motion posture

## Guidelines

- Tie every topic to a litigation objective and time-bound it
- **Taking**: treat answers as party admissions; pin down "corporation's position" precisely
- **Defending**: prepare as if every topic will be used at summary judgment and trial
- Objections preserve rights — do not obstruct proper questioning
- Mark jurisdictional limits for state analogs and local rules [VERIFY]
- Use `[VERIFY]` for all unconfirmed citations before finalizing filings

## Cross-references

- @deposition-preparation
- @deposition-witness-prep-session
- @deposition-notice-drafter
- @deposition-objection-reference
- @deposition-questioning-techniques

## References

- FRCP 30(b)(6) [VERIFY]
- FRCP 37(d) [VERIFY]
- *Brazos River Auth. v. GE Ionics, Inc.*, 469 F.3d 416 (5th Cir. 2006) [VERIFY]
- *QBE Ins. Corp. v. Jorda Enters., Inc.*, 277 F.R.D. 676 (S.D. Fla. 2012) [VERIFY]
- *Calzaturficio v. Fabiano Shoe Co.*, 201 F.R.D. 33 (D. Mass. 2001) [VERIFY]
- Cal. CCP § 2025.230 [VERIFY]
