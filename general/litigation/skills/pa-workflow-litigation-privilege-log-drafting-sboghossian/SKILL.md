---
name: pa-workflow-litigation-privilege-log-drafting-sboghossian
title: Privilege Log Drafting
description: Use when a litigation team must produce a privilege log as part of discovery or disclosure proceedings. Automatically processes a document set to identify privilege candidates, draft log entries with the required fields (date, author, recipient, privilege basis, description), and flag documents requiring attorney review. Covers attorney-client privilege and work-product doctrine under US, UK, DIFC, ADGM, and MENA procedural frameworks.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-litigation-privilege-log-drafting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Privilege Log Drafting

## Purpose

A privilege log is a mandatory component of discovery and disclosure compliance whenever a party withholds documents on privilege or work-product grounds. An incomplete or inaccurate log exposes the withholding party to court sanctions, waiver of privilege, and adverse inferences. This workflow drafts log entries systematically from a document set, producing a compliant log without revealing the protected content.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Document set (privilege candidates) | Yes | Output from [[pa-workflow-litigation-discovery-first-pass-tagging]] is the standard upstream feed |
| List of attorneys of record | Yes | Internal and external counsel — needed to identify attorney communications |
| Applicable forum / court | Yes | Determines log format and privilege standards |
| Date of litigation / claim | Recommended | For work-product dating (materials prepared "in anticipation of litigation") |
| Log format requirements | Optional | Some courts specify exact column requirements — override defaults if so |

## Privilege Standards by Jurisdiction

### Attorney-Client Privilege

| Jurisdiction | Standard | Key nuances |
|---|---|---|
| US federal | Communication from/to attorney; legal advice purpose; confidential | Applies to in-house counsel; subject-matter waiver risk; common interest doctrine available |
| UK | Legal advice privilege (advice-seeking communications) + litigation privilege (docs for dominant purpose of litigation) | Litigation privilege is broader; Three Rivers distinction applies to in-house counsel communications |
| DIFC | English common-law standard applies | DIFC Courts follow English privilege doctrine; Three Rivers may be applied |
| ADGM | English common-law standard | Same as DIFC |
| UAE onshore | No statutory attorney-client privilege equivalent | Practical confidentiality is respected; formal privilege doctrine as in common law does not exist; flag for counsel to determine case-by-case |
| KSA | No formal statutory privilege | Licensed Saudi lawyers have professional confidentiality obligations; structural protection is weaker than common law |
| Lebanon | Professional secrecy (sirr mihnawi) for licensed attorneys | Civil-law confidentiality; court-filing privilege is recognized but doctrine is less developed |
| Egypt | Professional secrecy for licensed attorneys | Similar to Lebanon |

### Work-Product Doctrine

Applies to documents and mental impressions prepared by or for a party or its attorney in anticipation of litigation. In US federal courts (FRCP 26(b)(3)), opinion work product (attorney's mental impressions) enjoys near-absolute protection; factual work product is discoverable on showing of need. DIFC/ADGM: litigation privilege serves a similar function. UAE/KSA/LB/EG: no equivalent doctrine; approach on a case-by-case basis through professional secrecy.

## Log Entry Drafting

### Required Fields

| Field | Content | Notes |
|---|---|---|
| Document number | Sequential log reference | |
| Date | Date of document | Use document metadata; flag if metadata is unreliable |
| Author | Full name and role | Note if attorney |
| Recipient(s) | Full name(s) and role(s) | CC/BCC where relevant |
| Document type | Email / memo / draft / report / notes | |
| Privilege basis | ACP, WP, or both | See codes below |
| Description | Nature of document without revealing privileged content | See drafting rules below |
| Redaction note | Full withhold / partial redact | If partial, note what portion is withheld |

### Privilege Codes

- **ACP**: Attorney-Client Privilege — communication seeking or providing legal advice to/from legal counsel
- **WP-F**: Work Product (Factual) — prepared in anticipation of litigation; factual content
- **WP-O**: Work Product (Opinion) — attorney's mental impressions, conclusions, or legal theories
- **CI**: Common Interest — shared privilege between parties with aligned legal interests
- **3P**: Third-Party Privilege — e.g., accountant-client, mediation privilege (where applicable)

### Description Drafting Rules

The description must convey enough information to allow the opposing party to assess the privilege claim — without revealing the privileged content itself.

**Correct format:**
> Email from external counsel to CFO dated [date] transmitting legal advice regarding regulatory filing obligations under [regulation].

**Too vague (challengeable):**
> Email regarding legal matters.

**Too revealing (waiver risk):**
> Email from counsel advising that the payment structure violates the regulatory threshold and recommending a restructuring to avoid detection.

Guidelines:
- Identify the legal subject matter at a categorical level (contract review, regulatory compliance, litigation strategy)
- Identify the legal counsel involved by role (outside counsel, in-house General Counsel)
- Do not quote the substance of the advice
- Do not include trade secrets or commercially sensitive information in the description even if not privileged — those should be noted separately

## Output Format

### Standard Log (spreadsheet / table)

```
| Log No. | Date       | Author            | Recipient(s)        | Type  | Privilege | Description                                              | Withheld/Redacted |
|---------|------------|-------------------|---------------------|-------|-----------|----------------------------------------------------------|-------------------|
| PL-001  | 2023-10-15 | Jane Smith (GC)   | CEO; CFO            | Email | ACP       | Email from General Counsel providing legal advice on     | Withheld in full  |
|         |            |                   |                     |       |           | proposed joint-venture structure under UAE Federal Law.  |                   |
| PL-002  | 2023-11-01 | External Counsel  | Jane Smith (GC)     | Memo  | ACP; WP-O | Memo from outside counsel transmitting litigation        | Withheld in full  |
|         |            |                   |                     |       |           | strategy assessment for pending DIFC arbitration.        |                   |
```

### Cover Letter / Certification (US FRCP 26(b)(5))

The log is accompanied by a certification that:
- A reasonable inquiry was conducted
- All withheld documents are identified
- The privilege claimed is believed in good faith to apply

## Common Mistakes

- Describing a document as "legal advice" when the communication is purely commercial (business advice by an attorney is not automatically privileged)
- Withholding documents authored by in-house counsel on purely business topics — especially vulnerable in UK/DIFC proceedings (Three Rivers limitation on in-house ACP)
- Including documents on the log that are clearly not privileged (over-designation invites a court order to re-review and produce)
- Failing to list common-interest participants — the common-interest doctrine must be asserted affirmatively
- Sending a draft to a third party (non-attorney) and claiming privilege — third-party disclosure generally waives ACP unless common-interest applies

## Jurisdictional Filing Requirements

- **US**: FRCP 26(b)(5) — description must enable the opposing party to assess the privilege claim. Many courts' local rules specify exact log format.
- **UK**: CPR 31.19 — claim for withholding inspection; court may order inspection to assess the claim.
- **DIFC**: DIFC Practice Direction — follows CPR approach; electronic log submission via e-filing portal.
- **UAE onshore**: No statutory privilege log requirement; produce to court on request with explanation.
- **KSA**: Documents withheld based on professional confidentiality explained by counsel in written submissions.

## Related Skills

- [[pa-workflow-litigation-discovery-first-pass-tagging]]
- [[pa-workflow-litigation-brief-cite-checker]]
- [[pa-workflow-litigation-motion-template-library]]
- [[pa-workflow-litigation-deposition-binder-builder]]
