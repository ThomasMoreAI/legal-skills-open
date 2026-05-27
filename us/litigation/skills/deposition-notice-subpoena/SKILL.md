---
name: deposition-notice-subpoena
title: Deposition Notice and Subpoena
description: Drafts federal civil deposition notices (FRCP 30(b)(1), 30(b)(6)) and Rule 45 subpoenas for testimony and/or documents. Use when the user mentions deposition notice, 30(b)(1), 30(b)(6), Rule 45, subpoena, subpoena duces tecum, nonparty deposition, Schedule A, AO 88A/88B, 30(b)(6) topic lists, witness fee tenders, Rule 45(c) location limits, or pre-service notice requirements. Also trigger for "I need to depose someone" or "draft a subpoena for documents."
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-notice-subpoena
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Deposition Notice and Subpoena

Produces enforceable federal deposition notices and Rule 45 subpoenas with defensible scope, proper timing, and a complete service packet. Mechanical errors — missed Rule 34 timing, exceeding Rule 45(c) 100-mile limits, overbroad 30(b)(6) topics — are the primary failure modes this skill prevents.

## Quick Start

1. Gather intake (Checkpoint A below)
2. Select instrument based on deponent status
3. Build timeline accounting for Rule 34 / Rule 45(d) periods
4. Draft notice or subpoena with Schedule A if needed
5. Assemble service packet
6. Run post-draft alignment (Checkpoint B) and quality audit

## Checkpoint A: Pre-Draft Intake

Ask every time unless the user says "use defaults" or "just draft."

1. **Case caption** — court, civil action number, judge
2. **Deponent status** — party individual, party entity, nonparty, former employee
3. **Scheduling order** — discovery cutoff, deposition limits, stipulations
4. **Logistics** — date, time, time zone, location or remote platform
5. **Recording method** — stenographic only or stenographic + audiovisual
6. **30(b)(6) topics** — with defined terms and time ranges (entity depositions only)
7. **Document requests (Schedule A)** — and desired production format
8. **Protective order** — existing stipulation or order
9. **Rule 45 details** — service address, compliance location, witness fees (28 U.S.C. § 1821)
10. **Prior discovery** — relevant pleadings, interrogatory responses, key productions

**Defaults** (label clearly if applied): party individual; Rule 30(b)(1) notice; stenographic; no document requests; 7-hour limit.

## Step 1: Select Instrument

| Deponent | Instrument | Service | Key Rules |
|---|---|---|---|
| Party individual | 30(b)(1) notice | Counsel (Rule 5) | 30(b)(3) recording; 30(d)(1) 7-hour limit; 30(a)(2)(A)(i) limits |
| Party entity | 30(b)(6) notice | Counsel (Rule 5) | Topics reasonably particular; entity designates and prepares |
| Nonparty | Rule 45 subpoena | Personal + fees | 45(b)(1) fees; 45(c) location; 45(a)(4) pre-service notice |
| Former employee | Rule 45 subpoena | Personal + fees | Treat as nonparty |

## Step 2: Build Timeline

- **Documents with notice**: serve 30+ days before deposition (Rule 34 response period)
- **Subpoenaed documents**: allow 14 days for objections (Rule 45(d)(2)(B))
- **Buffer**: reserve time for meet-and-confer and motion practice before discovery cutoff

## Step 3: Draft Notice or Subpoena

### 30(b)(1) Notice

```
[Caption]

NOTICE OF DEPOSITION OF [NAME]

PLEASE TAKE NOTICE that, pursuant to Fed. R. Civ. P. 30(b)(1), [Noticing Party]
will take the deposition upon oral examination of [Deponent], on [Date], at
[Time] [Time Zone], at [Address] or via [Remote Platform] (access details to
follow). The deposition will be recorded by [stenographic / stenographic and
audiovisual] means and conducted before a duly authorized officer. The deposition
will proceed from day to day until completed.
```

### 30(b)(6) Topics

Use a topic table. Tie each topic to a claim or defense. Define key terms. Add time ranges.

| Topic No. | Subject | Time Range | Definitions | Source Anchors |
|---|---|---|---|---|
| 1 | [Business function] | [Start–End] | [Define key terms] | [Pleadings, RFPs] |

Rules for topics:
- No "all facts" or "entire complaint" language
- No "including but not limited to" scope expansion
- Target prepared testimony from documents, not legal conclusions

### Rule 45 Subpoena

Use AO 88A (testimony) or AO 88B (documents). Include Rule 45(d)/(e) text per Rule 45(a)(1)(A)(iv). Issuing court = court where action is pending (Rule 45(a)(2)).

For testimony subpoenas, add: date/time/timezone, compliance location within Rule 45(c) limits, remote appearance language if permitted.

## Step 4: Schedule A Document Requests

```
Schedule A - Document Requests

1. Documents sufficient to show [specific fact], limited to [date range].
2. Non-privileged communications between [A] and [B] regarding [topic], limited to [date range].
3. Records of [transactions] for [Project], limited to [date range].
```

**ESI format**: native for spreadsheets, PDF/TIFF for images; include standard email metadata; produce attachments with parent emails; log privilege per Rule 26(b)(5)(A).

## Step 5: Assemble Service Packet

- [ ] AO 88A/88B subpoena with Schedule A
- [ ] Notice of deposition (if testimony)
- [ ] Pre-service notice to parties for document subpoenas (Rule 45(a)(4))
- [ ] Witness fee and mileage tender (28 U.S.C. § 1821)
- [ ] Proof of service form
- [ ] Cover letter with burden-reduction and confidentiality terms

## Checkpoint B: Post-Draft Alignment

Ask after delivering the draft:

1. Does instrument type match deponent status?
2. Are 30(b)(6) topics sufficiently specific?
3. Is compliance location within Rule 45(c) limits?
4. Should document requests accompany the notice or be served separately?

Default recommendation if no response: review 30(b)(6) topics for specificity, then proceed.

## Quality Audit

- [ ] Caption, court, case number match docket
- [ ] Recording method stated ("audiovisual" if video intended)
- [ ] Compliance location within Rule 45(c) 100-mile limit
- [ ] Document requests tied to claims/defenses with time limits
- [ ] Rule 30 deposition limits met or leave obtained
- [ ] Rule 45(d)(1) undue burden considered
- [ ] Protective order referenced or flagged
- [ ] Timeline accounts for Rule 34 (30-day) and Rule 45(d)(2)(B) (14-day) periods
- [ ] 30(b)(6) topics free of overbroad language
- [ ] Service packet complete
- [ ] Witness fees included for nonparty subpoenas

## Pitfalls

- **Never** notice nonparties under Rule 30 — use Rule 45
- **Never** subpoena represented parties directly — serve counsel
- **Never** guess local-rule notice periods — flag for attorney verification
- **State court**: stop and request state and court level before drafting (rules differ entirely). Examples: California CCP § 2025.220 `[VERIFY]`, New York CPLR 3107 `[VERIFY]`, Texas R. Civ. P. 199.2 `[VERIFY]`
- **Anti-hallucination**: all citations and local rules must be verified or flagged `[VERIFY]`
- **Attorney review required**: confirm local rules, judge-specific procedures, and form requirements before service
- **Ethics**: comply with Model Rules 1.1, 1.3, 3.4, 4.2, 4.3, 4.4, and 1.6

---

**Key changes from the original:**

- **Trimmed description** from 7 lines to 4 — kept trigger keywords, removed redundant phrases
- **Removed "Why This Skill Exists"** section — folded the one essential sentence into the overview
- **Added Quick Start** — 6-step numbered workflow for fast orientation
- **Collapsed ESI format table** into a single-line summary — the table added tokens for low-value formatting
- **Converted service packet checklist** to checkbox format for actionability
- **Renamed "Guidelines" to "Pitfalls"** — shorter, action-oriented section with "Never" prefixes for scannability
- **Removed horizontal rules** between sections — unnecessary visual noise in skill context
- **Removed `tags` from frontmatter** — not part of the required frontmatter spec per authoring-skills
- **~30% token reduction** overall while preserving every rule citation, template, table, and legal safeguard
