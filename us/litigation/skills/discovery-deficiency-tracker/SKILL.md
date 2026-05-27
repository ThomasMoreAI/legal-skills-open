---
name: discovery-deficiency-tracker
title: Discovery Deficiency and Meet-and-Confer Tracker
description: Builds and maintains a litigation-grade discovery deficiency and meet-and-confer tracker for compulsion motion practice. Use this skill when the user mentions deficient discovery responses, motion to compel preparation, meet-and-confer tracking, FRCP 37 sanctions, discovery dispute charts, joint discovery letters, informal discovery conferences, deficiency logging, or California Separate Statements. Also trigger when the user references boilerplate objections, privilege log deficiencies, incomplete productions, evasive answers, discovery conferral documentation, or asks for help organizing disputes for court. Even if the user just says "track these discovery problems" or "help me build a compel motion," use this skill.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/discovery-deficiency-tracker
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, checklist, drafting, letter, summary]
---

# Discovery Deficiency and Meet-and-Confer Tracker

## Why This Skill Exists

Discovery disputes are won or lost on organization and documentation, not on the merits of any single objection. Without a structured, request-by-request tracker, deficiencies blur together, conferral history gets lost in email threads, deadlines slip, and the motion to compel becomes a credibility fight about who said what. Courts increasingly require detailed dispute charts and documented good-faith conferral before entertaining any compulsion motion.

This skill produces a tracker that serves as the factual backbone for FRCP 37 motions to compel, sanctions requests, informal discovery conferences, joint letters, and California Separate Statements — with every assertion grounded in verbatim quotations from primary sources.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Full discovery requests** — complete text of each disputed interrogatory, RFP, or RFA, including definitions, instructions, and identifiers
2. **Complete written responses** — exact response text as served, including all general and specific objections, verifications, and any "subject to and without waiving" language
3. **Production records** — Bates ranges for documents produced, privilege logs served, and supplementation dates/descriptions
4. **All conferral communications** — emails, letters, call notes in chronological order; any court orders relating to discovery
5. **Governing orders** — protective order, ESI order, clawback agreement
6. **Scheduling deadlines** — discovery cut-off, motion cut-off, and any forum-specific compel deadlines
7. **Forum identity** — court, assigned judge, local rules URL, and standing/individual rules

**If the user doesn't respond**, apply and clearly label these defaults: federal court; FRCP 26–37 governing rules; all disputed requests included; court-facing chart format.

> If exact request/response text or applicable deadlines are missing, pause and prompt the user before generating a court-ready tracker. Label provisional entries **[ATTORNEY VERIFICATION NEEDED]**.

---

## Step 1: Build the Tracker Schema

Create one entry per disputed request number. Never combine multiple requests in a single row.

| Field | Content |
|---|---|
| **Entry ID** | Persistent slug, e.g., `RFP12-PRIVLOG`, `INT7-SPEC` |
| **Request No. & Type** | RFP No. 12 / Interrogatory No. 7 / RFA No. 3 |
| **Request Text** | Verbatim — including temporal scope, defined terms |
| **Response Date & Method** | Date served, service method |
| **Response Text** | Verbatim — including all objections and conditional language |
| **Production / Bates** | Bates range(s) or "None" |
| **Privilege Log** | Date served or "None" |
| **Supplementation** | Date(s) and description of each supplement |
| **Deficiency Type** | See taxonomy below |
| **Deficiency Statement** | Rule-grounded narrative, court-paste ready |
| **Proposed Cure** | Phrased as an order a judge can sign |
| **Materiality** | Tie to claim element, damages, cert, expert, or impeachment |
| **Conferral Log** | See format below |
| **Opposing Justification** | Verbatim or accurate paraphrase |
| **Agreed Narrowing** | Any scope reductions agreed |
| **Commitments & Deadlines** | What OC committed to produce/revise and by when |
| **Forum Requirement Satisfied?** | Yes / No / Partial + explanation |
| **Regulatory Constraint** | HIPAA, FERPA, GDPR, state privacy — if applicable |
| **External Deadline** | Motion-to-compel deadline (forum-verified) |
| **Internal Deadline** | Next follow-up, letter draft, IDC request |
| **Sanctions Flag** | Yes/No — basis under FRCP 37(a)(5) or 37(b) |
| **Status** | See status taxonomy below |
| **Relief Sought** | Order language for motion or joint letter |

---

## Step 2: Classify Deficiencies

Apply the deficiency taxonomy to each entry:

| Code | Deficiency | Governing Standard |
|---|---|---|
| `BOILERPLATE` | General objections without specificity | FRCP 34(b)(2)(B); [VERIFY: district-specific case law] |
| `34C-WITHHOLD` | Fails to state whether docs withheld on objection | FRCP 34(b)(2)(C) |
| `34B-PARTIAL` | Objects in part, produces in part, no specification | FRCP 34(b)(2)(B) |
| `PROPORTIONALITY` | Conclusory burden claim without 26(b)(1) factor analysis | FRCP 26(b)(1) (2015 amendments — 6 factors) |
| `PRIVLOG` | Privilege claimed without adequate log | FRCP 26(b)(5)(A) |
| `WORKPRODUCT` | Work-product claim without log distinguishing from A/C | FRCP 26(b)(3) |
| `CONDITIONAL` | "Subject to and without waiving" — ambiguous withholding | FRCP 34(b)(2)(C); [VERIFY: controlling district authority] |
| `INCOMPLETE-SEARCH` | Insufficient custodians, date range, or data sources | FRCP 26(g)(1) |
| `ESI-FORMAT` | Production format non-compliant with ESI order | FRCP 34(b)(2)(E) |
| `VERIFICATION` | Missing verification for interrogatories | FRCP 33(b)(3)–(5) |
| `SUPPLEMENT` | Failure to supplement timely | FRCP 26(e) |
| `EVASIVE` | Non-responsive or evasive answer | FRCP 37(a)(4) |

### Deficiency Statement Format

```
Deficiency [Entry ID]: [DEFICIENCY TYPE]
Rule: FRCP [X] requires [specific obligation].
Deficiency: [Exact objection language] fails to [specific requirement] because [precise legal reason].
Proposed Cure: Serve an amended response that (1) [concrete step], (2) [concrete step], (3) [concrete step] by [date].
Relief Sought: Order compelling [specific custodians / sources / date range / format] and amended response confirming search methodology.
```

---

## Step 3: Document Meet-and-Confer History

Log each conferral event per entry using this format:

```
[DATE] [MODE: phone/video/in-person/email] | Participants: [Atty A / Atty B]
Summary: OC stated [X]. We stated [Y]. Agreed: [Z]. Commitments: OC to produce [X] by [date]; we to defer [Y] pending [Z].
Confirmation email sent: [yes/no, date]
Issues resolved this session: [list or "none"]
Issues remaining: [list]
Next follow-up: [date / action]
```

> After each substantive conferral, send a written confirmation to OC summarizing agreements, commitments, and dates. Attach that email to the tracker entry.

---

## Step 4: Assign Status and Flag Sanctions Exposure

### Status Taxonomy

| Status | Meaning |
|---|---|
| `Open — awaiting supplement by [date]` | OC committed; deadline pending |
| `Partially Cured — reviewing production` | Some production received; deficiency may persist |
| `Narrowed — privilege log only` | Core deficiency resolved; sub-issue remains |
| `Impasse — ready for IDC/motion` | Good-faith conferral exhausted |
| `Escalated — joint letter due [date]` | Forum process initiated |
| `Resolved — no further action` | Deficiency cured |

Flag entries where the same deficiency persists across ≥ 2 conferral cycles for FRCP 37(a)(5) fee-shifting analysis. Document the number of conferral events per entry.

---

## Step 5: Generate Output Views

**Client-facing report:** Plain-language summary of each dispute, litigation value, cost-benefit of escalation, and timeline. Omit internal strategy notes. No "bad faith" labels without evidentiary basis and deliberate strategy.

**Court-facing chart:** Strictly factual, request-by-request, impasse items only. Format per forum:

| Forum | Required Format |
|---|---|
| Federal (most districts) | Request-by-request chart or joint letter; confirm judge's individual rules |
| SDNY | Pre-motion letter ≤ 3 pages |
| N.D. Cal. / D. Del. | Joint letter; issue-narrowed; practical compromise proposals required |
| California state court | **Separate Statement** under CRC 3.1345 — full verbatim request and response reproduced for each dispute; cannot incorporate by reference |
| NY Commercial Division | Pre-motion conference required under Comm. Div. Rule 14 before formal motion |
| Texas state court | Certificate of Conference under TRCP 191.2 — must confirm actual verbal contact or explain why impossible |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial tracker, ask:

1. Does the tracker capture the correct set of disputed requests — any to add or remove?
2. Are the deficiency classifications and severity flags accurate for your motion strategy?
3. Which output view should be generated first — client-facing report, court-facing chart, or California Separate Statement?
4. Are there any conferral events or OC commitments not yet reflected in the log?

If the user doesn't answer, recommend generating the court-facing chart for impasse items and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- Every request and response quoted verbatim — no paraphrasing
- One entry per request number — no combined rows
- Each deficiency statement cites a specific FRCP rule and identifies the precise failure
- Meet-and-confer log entries include date, mode, participants, and commitments
- All deadlines computed and labeled verified or unverified
- Sanctions flags documented with conferral cycle count
- Status taxonomy applied consistently
- Materiality tied to specific claims, defenses, or issues
- Forum-specific format requirements confirmed
- Every factual assertion traceable to a document or labeled as assumption
- No invented case citations

---

## Guidelines

- **Verbatim only** — quote requests and responses exactly; even minor paraphrase creates opposition ammunition
- **Citations** — provide URL to authoritative source for every rule and statute cited, or mark `[VERIFY]`; never generate unverified case citations
- **Deadlines are mandatory** — California motion-to-compel deadlines are typically 45 days from service of response (CCP §§ 2030.300, 2031.310, 2033.290 [VERIFY for method-of-service extensions]); missing them forfeits the right to compel; label all deadlines unverified until confirmed via local rules
- **Forum confirmation required** — ask for court, judge, and local rules at intake; treat all escalation procedures as unverified until checked against court website and standing order
- **Work-product protection** — tracker contains attorney mental impressions and strategy; treat as privileged work product under FRCP 26(b)(3); segregate strategy commentary from factual content before any sharing; confirm common-interest basis before sharing with co-counsel
- **Regulatory constraints** — when withholding is justified by HIPAA, FERPA, GDPR, or state privacy law, note the specific statute and confirm applicability before asserting as a bar
- **Anti-hallucination** — all case citations must be verified via web search and URL-cited, or left as explicit attorney-fill placeholders; no plausible-sounding but unverified citations
- **Attorney review required** — all tracker output is practice-support work product; it is not legal advice and must be reviewed by supervising counsel before use in any external communication or court filing
