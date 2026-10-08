---
name: prompt-pack-litigation-hold-notice-sboghossian
title: Litigation Hold Notice
description: Use when drafting a litigation hold notice to be issued to employees, contractors, and third parties instructing them to preserve documents and data related to anticipated or actual litigation, arbitration, or regulatory investigation. Covers preservation scope, explanation of obligations, prohibited conduct, and escalation contacts. Applicable across common-law and civil-law jurisdictions with MENA-specific notes.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-litigation-hold-notice
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Litigation Hold Notice

## When to use this

Use this skill to draft the individual notice sent to each custodian (employee, contractor, or third party) directing them to preserve specific categories of documents and data. This is a single-custodian-addressable document; the companion [[prompt-pack-legal-hold-management-procedure]] governs the broader organizational framework.

Triggers:
- "Draft a litigation hold notice for our employees regarding the [counterparty] dispute."
- "We've received a demand letter — I need to issue a hold notice today."
- "Write a preservation notice for a regulatory investigation."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Company name | Issuing entity | Ask user |
| Dispute / matter description | Enables custodians to understand what they need to preserve | Ask user — describe without disclosing legal strategy |
| Subject matter of relevant documents | Defines scope of preservation obligation | Ask user — project name, counterparty name, time period |
| Contact person (legal department) | Custodians need a named contact for questions | GC or assigned counsel |
| Effective date | Date from which preservation obligation runs | Immediately on receipt |

## Optional inputs

- Specific document categories to preserve (if known)
- Specific IT systems to address (email, SharePoint, personal devices, messaging apps)
- Custodian's specific role in the matter (personalize where possible)
- Whether former employees are being notified (different tone and process)

## Notice structure

---

**CONFIDENTIAL — ATTORNEY-CLIENT PRIVILEGED**

**LITIGATION HOLD NOTICE**

**To:** [Custodian Name / All Department / Group of Employees]
**From:** [General Counsel / Deputy GC / Legal Department]
**Date:** [Date]
**Re:** Preservation of Documents and Data — [Matter Reference]

---

### Paragraph 1: Purpose and Trigger

State, without disclosing legal strategy: "The Legal Department has determined that [Company] is involved in or may be involved in [describe the matter in general terms: e.g., a legal dispute / regulatory inquiry / arbitration proceeding] relating to [describe subject matter, e.g., our commercial relationship with [Counterparty] during the period [Year–Year]]. As a result, [Company] has a legal obligation to preserve all documents and data that may be relevant to this matter."

**Do not**: name the specific claim, state likelihood of success, or disclose privileged analysis in this notice. The notice itself may be discoverable.

### Paragraph 2: Your Preservation Obligation

"Effective immediately, you are required to locate, preserve, and not delete, destroy, alter, or conceal any documents, electronically stored information (ESI), or tangible items that relate in any way to [describe subject matter]. This obligation overrides any standard retention schedules, automatic deletion settings, or routine document destruction policies."

### Paragraph 3: What to Preserve (Scope)

Include a specific but not exhaustive list:

- All emails, calendar entries, and attachments in your inbox, sent items, deleted items, and archive folders
- All documents, spreadsheets, presentations, and files stored on your computer, shared drives, OneDrive, SharePoint, or any cloud storage service used for work
- All instant messages, chat logs, and messages on [Teams / WhatsApp / Slack / other platforms] relating to [subject matter]
- All text messages and voicemails sent or received on any device (personal or company) used for business purposes in connection with [subject matter]
- All physical documents, printed emails, handwritten notes, and paper files relating to [subject matter]
- Any other information or materials, regardless of format or storage location, relating to [subject matter] during the period [date range]

### Paragraph 4: Prohibited Conduct

"You must NOT:
- Delete, discard, shred, or destroy any documents or data covered by this notice
- Overwrite, alter, or edit any covered documents
- Move files to locations where they may be subject to automatic deletion
- Forward or share covered documents outside the company without prior Legal Department approval
- Discuss the contents of this notice or the matter with third parties

Any violation of this notice may have serious legal consequences for both you and the company."

### Paragraph 5: Existing Documents and New Documents

"This notice covers documents and data that already exist and all new documents, communications, and data that you create or receive from this date forward relating to [subject matter], until the Legal Department notifies you that the hold has been released."

### Paragraph 6: Actions Required of You

1. **Acknowledge receipt**: reply to this notice by [date — typically 5 business days] confirming you have received it and understand your obligations.
2. **Identify relevant materials**: make a reasonable effort to identify all documents and data in your possession, custody, or control that fall within the scope described above.
3. **Disable auto-delete**: if you have set up any automatic email deletion or archive rules for relevant folders, disable them immediately and notify [IT contact / Legal].
4. **Contact your manager**: inform your manager that you have received this notice (without sharing confidential case details) so they can ensure team members under your supervision also preserve relevant materials.
5. **Report questions to Legal**: contact [Name, Title, Email, Phone] with any questions about what to preserve.

### Paragraph 7: Contact and Questions

"If you have any questions about the scope of this notice or your obligations, please contact [GC Name] at [email] / [phone]. Do not let any uncertainty lead to destruction of potentially relevant materials — when in doubt, preserve."

### Paragraph 8: Confidentiality of This Notice

"This notice is confidential and protected by attorney-client privilege to the extent applicable. Please do not share it with anyone outside the company or outside your reporting chain without express authorization from the Legal Department."

---

**Acknowledgment Form (attach or embed)**

I confirm that I have received and read the Litigation Hold Notice dated [Date] regarding [Matter Reference]. I understand my preservation obligations and will comply with the requirements set out in the notice.

Name: _________________________
Title: _________________________
Signature: _________________________
Date: _________________________

---

## Jurisdictional notes

| Jurisdiction | Key considerations |
|---|---|
| **Common law (DIFC, ADGM, UK, US)** | Spoliation can result in adverse inference instructions, striking of pleadings, or sanctions. Notices issued in good faith with clear scope are the primary defense. |
| **UAE (onshore)** | Less formalized e-discovery, but deliberate destruction of evidence can be raised before courts; preservation notices demonstrate good faith. |
| **KSA** | Court-ordered document production; preservation notices protect the company from allegations of bad faith. |
| **Cross-border / arbitration** | International arbitration tribunals (ICC, DIAC, LCIA, SIAC) have broad document production powers; preservation notices are essential to demonstrate compliance. |
| **GDPR / UAE-PDPL / KSA-PDPL** | Preservation obligations override data subject deletion requests during the hold period; document the legal basis. |

## Common mistakes

- **Generic notices not tailored to the matter**: custodians receiving a vague notice will not know what to preserve and may inadvertently delete key items.
- **Not including messaging apps**: WhatsApp, Teams, and Signal are used for business communications in MENA; generic "email" notices miss these entirely.
- **No acknowledgment mechanism**: without proof of delivery and acknowledgment, the company cannot demonstrate that custodians were notified.
- **Disclosing legal strategy in the notice**: the notice itself may be discoverable by the opposing party; describe the subject matter commercially, not legally.
- **Not re-issuing when scope expands**: if new claims or time periods arise, a supplemental notice must be issued promptly.

## Related skills

- [[prompt-pack-legal-hold-management-procedure]]
- [[prompt-pack-legal-opinion-on-dispute]]
- [[prompt-pack-matter-closing-procedure]]
