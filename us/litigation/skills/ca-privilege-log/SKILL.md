---
name: ca-privilege-log
title: California Privilege Log
description: Generates California-compliant privilege logs for withheld or redacted discovery materials under CCP 2031.240. Use when the user mentions privilege log drafting, California privilege log, CCP 2031.240, attorney-client privilege logging, work product designation, Evid. Code 952/954, CCP 2018.030, redaction logging, meet-and-confer privilege disputes, waiver analysis, common interest doctrine, or asks for help documenting withheld documents. Also trigger on references to Hernandez v. Superior Court, Costco Wholesale, or Wellpoint.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ca-privilege-log
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# California Privilege Log

Produces defensible privilege logs meeting *Hernandez v. Superior Court* (2003) 112 Cal.App.4th 285 [VERIFY] specificity requirements — descriptions sufficient to assess the privilege without revealing privileged substance. Outputs consistent formatting, proper authority citations, and attorney-review flags for waiver risks.

## Quick Start

1. Gather intake inputs (Checkpoint A below)
2. Confirm forum and any court-ordered format
3. Normalize metadata and classify privilege basis per item
4. Draft log entries using standard columns and safe description templates
5. Flag waiver risks in a separate attorney-only section
6. Run quality audit before delivery

## Checkpoint A: Pre-Draft Intake

Ask every time unless user says "use defaults" or "just draft":

1. **Discovery context** — RFP set, request text, objections, ESI protocol/CMO/stipulation on format
2. **Document population** — withheld and redacted items with stable IDs/Bates, family links, production status
3. **Metadata** — date, author, recipients (TO/CC/BCC), doc type, subject/file name, custodian
4. **Roles list** — name-to-role map (client, in-house, outside counsel, consultants, third parties)
5. **Privilege basis** — ACP, WPD absolute, WPD qualified, common interest/joint defense (with proof)
6. **Litigation timeline** — trigger facts for "anticipation of litigation" (work product)
7. **Waiver risks** — third-party dissemination, mixed business/legal comms, forwarded chains

**Defaults** (if no response): California state court; attorney-client privilege basis; withheld (not redacted); standard column format. Label defaults clearly.

## Step 1: Confirm Forum and Governing Standard

California state court vs. federal — adapt only if an order or stipulation controls. Identify any court-specific or CMO-mandated format requirements. If federal, adapt to FRCP 26(b)(5)(A) while keeping California privilege elements.

## Step 2: Normalize Metadata

Ensure consistent names, roles, dates, and family relationships across all entries. Split attachments as separate entries unless the protocol allows categorical treatment.

## Step 3: Classify Privilege Basis

| Label | Use When | Authority |
|---|---|---|
| Attorney-Client Privilege | Confidential client-lawyer communication for legal advice | Evid. Code §§ 952, 954 |
| Work Product – Absolute | Attorney impressions, opinions, legal research, theories | CCP § 2018.030(a) |
| Work Product – Qualified | Other attorney work product | CCP § 2018.030(b) |
| Joint Defense / Common Interest | Shared legal strategy with aligned parties | Require agreement [VERIFY] |

Do not over-assert both ACP and WPD without factual support for each.

## Step 4: Draft Log Entries

### Required Columns

| Column | Required | Notes |
|---|---|---|
| Entry ID / Bates | Yes | Unique per document or family item |
| Date | Yes | "Undated" if unknown |
| Document Type | Yes | Email, memo, draft, notes, etc. |
| Author (Name + Role) | Yes | Use role mapping |
| Recipients TO (Name + Role) | Yes | Separate TO/CC/BCC |
| Recipients CC/BCC | If any | Include third parties explicitly |
| Description | Yes | Functional, non-substantive |
| Privilege Basis | Yes | ACP, WPD-Abs, WPD-Qual, or combined |
| Legal Authority | Yes | Cite relevant statutes |
| Production Status | Yes | Withheld or Redacted |
| RFP / Request No. | If tracked | Link to request |
| Notes | Optional | Family/attachment links, redaction note |

### Safe Description Templates

```text
Confidential email between [Client Role] and [Counsel Role] requesting or providing legal advice regarding [high-level issue]; withheld under attorney-client privilege (Evid. Code §§ 952, 954).

Internal memorandum prepared by [Counsel Role] at counsel's direction in anticipation of litigation regarding [high-level issue], reflecting counsel's impressions and legal theories; withheld as work product—absolute (CCP § 2018.030(a)).

Draft [document type] prepared for attorney review and legal advice concerning [high-level issue]; produced with redactions for privileged portions; redactions based on attorney-client privilege (Evid. Code §§ 952, 954).
```

### Description Checklist

- [ ] Identify document type and general purpose
- [ ] Identify roles of participants (client, in-house, outside counsel)
- [ ] State legal purpose at high level (request/provision of legal advice; prepared for litigation)
- [ ] Avoid quoting privileged subject lines or legal theories
- [ ] Specify redacted vs. withheld

## Step 5: Flag Waiver and Risk Issues

Generate a separate **attorney-only** review section (non-produced):

- Third-party recipient present → confirm necessity under Evid. Code § 952
- Forwarded to non-legal distribution list → assess waiver under Evid. Code § 912
- Mixed business/legal purpose → confirm dominant purpose (*Costco Wholesale Corp. v. Superior Court* (2009) 47 Cal.4th 725 [VERIFY])
- Work product claimed before litigation trigger → confirm timeline
- Expert involvement → confirm designation and potential waiver

## Checkpoint B: Post-Draft Review

After delivering the initial log, ask:

1. Are role assignments accurate for all participants?
2. Any entries needing privilege basis reconsideration (e.g., mixed business/legal)?
3. Should any withheld documents be redacted instead of fully withheld?
4. Does the format match any court order or stipulation?

If no response, recommend reviewing waiver-risk flags first and proceed if authorized.

## Quality Audit

Before finalizing, verify:

- [ ] Every entry has a unique ID/Bates number
- [ ] All participants mapped to roles consistently
- [ ] Descriptions specific enough under *Hernandez* [VERIFY] without revealing substance
- [ ] Privilege basis supported by facts, not boilerplate
- [ ] Redacted vs. withheld correctly designated per entry
- [ ] Attachments treated as separate entries (unless protocol allows grouping)
- [ ] No privileged subject lines, legal theories, or settlement positions exposed
- [ ] Waiver risks flagged in attorney-only section
- [ ] All statutory citations verified or marked `[VERIFY]`
- [ ] Format matches any applicable court order or ESI protocol

## Pitfalls

- **Never invent** metadata, roles, or privilege bases — stop and request missing inputs
- **Never expose** privileged substance, legal strategy, or settlement positions
- **Prefer redactions** over complete withholding when only part is privileged
- **Consistency matters** — inconsistent naming/formatting signals weakness to opposing counsel
- **Burden framework** — apply *Wellpoint Health Networks v. Superior Court* (1997) 59 Cal.App.4th 110 [VERIFY]
- **Anti-hallucination** — all case citations must be verified or flagged `[VERIFY]`; never generate unverified case law
- **Attorney review required** — all output must be reviewed by supervising counsel before service; comply with Cal. Rules of Prof. Conduct 1.1, 1.6, 3.3 [VERIFY]

---

**Key changes from the original:**

- **Frontmatter**: Removed non-spec `tags` field; tightened `description` while keeping all trigger keywords
- **Removed "Why This Skill Exists"**: Replaced verbose rationale paragraph with a 2-sentence overview that conveys the same standard
- **Added Quick Start**: 6-step numbered workflow at the top for fast orientation
- **Removed CSV header template**: Claude already knows CSV format — the column table is sufficient
- **Streamlined Checkpoint B**: Shortened heading and trimmed wording without losing the four review questions
- **Merged Guidelines into Pitfalls**: Consolidated the separate "Guidelines" section into a compact bullet list, eliminating duplicate guidance (e.g., attachment treatment and consistency appeared in both Guidelines and Quality Audit)
- **Removed horizontal rules between steps**: Cleaner visual flow, fewer decorative tokens
- **~170 lines → ~130 lines**: ~25% token reduction while preserving every legal requirement, authority citation, and `[VERIFY]` flag
