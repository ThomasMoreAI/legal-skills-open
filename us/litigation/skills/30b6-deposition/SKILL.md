---
name: 30b6-deposition
title: 30(b)(6) Corporate Representative Deposition
description: Guides taking and defending Rule 30(b)(6) corporate representative depositions. Drafts topic lists with reasonable particularity, builds examination outlines for binding corporate admissions, analyzes noticed topics for objections, and prepares designees. Use when drafting 30(b)(6) notices, preparing corporate deposition topics, selecting or preparing designees, or defending corporate representative depositions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/30b6-deposition
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# 30(b)(6) Corporate Representative Deposition

Covers both sides of FRCP 30(b)(6) depositions: drafting topic notices and examination outlines (taking), and analyzing topics, selecting designees, and preparation (defending).

## Quick Start

1. Determine role: **taking** or **defending**
2. If taking → draft topic list (Part A), then build examination outline
3. If defending → analyze noticed topics (Part B), select designees, prepare them

## Part A: Taking

### Topic List Drafting

Each topic must meet "reasonable particularity." See *Calzaturficio v. Fabiano Shoe Co.*, 201 F.R.D. 33 (D. Mass. 2001) [VERIFY].

**Drafting rules:**

| Rule | Bad | Good |
|------|-----|------|
| Time-bound | "All communications about plaintiff" | "HR-supervisor communications re: performance, Jan 2023–Jun 2024" |
| Not too narrow | "The email sent March 15 at 2:47 PM" | "Communications regarding the termination decision" |
| Tied to claims | Topics of mere curiosity | Each topic maps to a claim element |
| No legal conclusions | "Whether defendant discriminated" | "Criteria applied in the promotion decision" |
| Carve out privilege | "Communications with counsel" | Add "excluding attorney-client privileged communications" |

**Standard topic categories:** Org structure and reporting lines, relevant policies (creation/modification/enforcement), persons involved in key decisions, document retention and custodians, chronology of key events, financial calculations and damages basis.

**Topic template:**

```
Pursuant to FRCP 30(b)(6), [Corporation] shall designate representatives
to testify regarding:

TOPIC 1: [Corporation's] organizational structure from [date] to present,
including reporting relationships and decision-making authority for
[department].

TOPIC 2: Policies and procedures regarding [subject], including creation,
modification, and enforcement from [date] to [date].

TOPIC 3: Facts and circumstances surrounding [event], including persons
involved, communications, criteria considered, and basis for the decision.

TOPIC 4: Documents relating to [subject], including creation, maintenance,
location, and any destruction or loss.
```

**Objection risk check per topic:**

| Objection | Fix |
|-----------|-----|
| Overbroad | Narrow time or scope |
| Vague | Add specific definitions |
| Burdensome | Limit custodians or sources |
| Seeks privileged info | Carve out attorney-client communications |
| Legal conclusions | Reframe to seek facts |

### Examination Strategy

**Opening sequence** (always establish):

1. Confirm designation for each topic
2. Establish preparation per topic: documents reviewed, persons interviewed, sources consulted
3. "Do you feel prepared to testify fully on this topic?" — builds inadequate-preparation record

**Per-topic structure:**

1. **Foundation** — Confirm designation and preparation
2. **Substantive** — Start broad ("Tell me what [Corp] knows about [topic]"), then drill with documents
3. **Binding admissions** — "Is it [Corp's] position that...?" / "Does [Corp] contend...?" / "What is [Corp's] explanation for...?"
4. **Exhaustion** — "Any other information [Corp] has on [topic] you haven't shared?"

**Handling problems:**

| Problem | Response |
|---------|----------|
| "I don't know" | "Designated for this topic?" → "What did you do to find out?" → "Who would know?" → "Corp doesn't know, or you weren't prepared?" |
| "Outside my topics" | Read topic aloud; ask if question falls within it; may question in personal capacity |
| Defers to counsel | "I need you to answer, not your attorney." |

### Post-Deposition Use

- **Summary judgment**: Corporate admissions establish undisputed facts; corporation cannot easily contradict. *Brazos River Auth. v. GE Ionics*, 469 F.3d 416 (5th Cir. 2006) [VERIFY]
- **Trial**: Party admission; read to jury; impeach if trial position differs
- **Discovery motions**: Failed preparation supports motion to compel re-deposition or FRCP 37(d) sanctions

## Part B: Defending

### Topic Analysis

Assess each noticed topic:

| Factor | Question |
|--------|----------|
| Clarity | Reasonable particularity? |
| Scope | Limited in time and subject? |
| Relevance | Tied to claims or defenses? |
| Burden | Preparation difficulty? |
| Privilege | Seeks privileged info? |

**Response options:** Accept, accept with clarification, narrow (propose limits), object but prepare (avoid sanctions), object and refuse (be ready to litigate).

**Output — topic analysis matrix:**

| Topic | Assessment | Recommendation | Designee |
|-------|------------|----------------|----------|
| 1 | Clear, relevant | Accept | [Name] |
| 2 | Overbroad | Narrow to [dates] | [Name] |
| 3 | Privilege issue | Object; testify on non-privileged aspects | [Name] |

### Designee Selection

**Criteria:** Topic knowledge, preparation capacity, demeanor, availability, authority to speak for corporation.

| Option | Pros | Cons |
|--------|------|------|
| Most knowledgeable person | Minimal prep | May be poor witness or very senior |
| Professional corporate witness | Composed, experienced | Extensive prep needed |
| Multiple designees | Deeper per-topic expertise | Gap risks, coordination complexity |

Single designee avoids gaps but requires broader prep. Multiple allow depth but demand clear delineation — every topic must map to a designee with no gaps.

### Designee Preparation

The designee must know the **corporation's** collective knowledge, not just personal knowledge.

**Per-topic checklist:**

- Documents to review
- People to interview and what they know
- Key facts to master
- Problem areas and how to address them
- Corporation's position on each sub-issue

**Preparation sessions:**

| Session | Focus |
|---------|-------|
| 1: Foundation | Walk topics; identify gaps; assign doc review and interviews |
| 2: Synthesis | Test knowledge per topic; establish corporate positions; fill gaps |
| 3: Practice | Mock exam; binding admission questions; "I don't know" handling |

**"I don't know" coaching:**

- Acceptable: "The corporation does not have information about that" (after adequate prep)
- Acceptable: "I've reviewed all available documents and interviewed relevant personnel, and the records don't reflect that"
- Problematic: Bare "I don't know" without explaining preparation efforts — signals inadequate preparation
- Problematic: "I wasn't told about that" — same problem

### Defending at Deposition

- **Preserve objections**: Form, beyond noticed topics, assumes facts, calls for speculation
- **Instruct not to answer** (rare): Attorney-client privilege, work product, questions clearly outside all topics and personal knowledge
- **Do not**: Coach during breaks, make speaking objections that signal answers, obstruct legitimate questioning
- **Post-deposition**: Debrief witness, assess errata needs, evaluate re-deposition risk

## Pitfalls

- Test every topic against objection categories before finalizing the notice
- Binding admissions are the primary asset when taking — always frame as corporate positions, not individual opinions
- Duty to prepare when defending is absolute — *QBE Ins. v. Jorda Enters.*, 277 F.R.D. 676 (S.D. Fla. 2012) [VERIFY]
- State equivalents vary (e.g., Cal. CCP § 2025.230); always check local rules
- Privilege carve-outs must be explicit in both topic drafting and objection responses
- If using multiple designees, map every topic to a designee with no gaps
