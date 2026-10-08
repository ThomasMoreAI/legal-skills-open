---
name: prompt-pack-legal-hold-management-procedure-sboghossian
title: Legal Hold Management Procedure
description: Use when drafting or implementing a legal hold management procedure for a company facing anticipated or actual litigation, regulatory investigation, or arbitration. Covers hold initiation triggers, custodian identification, notice issuance, acknowledgment tracking, hold release, and documentation for defensibility. Applicable across common-law and civil-law jurisdictions with particular attention to MENA preservation obligations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-legal-hold-management-procedure
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Legal Hold Management Procedure

## When to use this

Use this skill to create an internal legal hold management procedure — the operational framework that governs how a company preserves documents, data, and evidence whenever litigation, arbitration, regulatory investigation, or a similar triggering event is reasonably anticipated.

Triggers:
- "We've received a claim letter — what is our legal hold procedure?"
- "Draft a company policy for issuing legal holds."
- "We need a repeatable process for hold management that will be defensible in court."

**Distinction**: This skill produces the *procedure* (the internal policy and workflow). For the individual notice issued to custodians, use [[prompt-pack-litigation-hold-notice]].

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Company name | Names the procedure document | "The Company" |
| IT environment description | Determines scope of data systems to address (email, SharePoint, ERP, messaging apps) | Generic — list common systems |
| Jurisdiction(s) of operation | Determines applicable preservation law and sanctions exposure | Global — flag jurisdiction-specific requirements |
| Legal team structure | Who initiates holds, who manages custodians | GC / Deputy GC as hold manager |

## Optional inputs

- E-discovery or matter management platform in use (for automated hold tracking)
- Existing document retention schedule (to explain interaction with hold obligations)
- Regulatory or court-specific requirements (e.g., DIFC Court practice directions, ADGM arbitration rules, UAE Civil Procedure Law)

## Procedure sections

### 1. Purpose and Scope
State that the procedure governs the creation, maintenance, and release of legal holds, and applies to all employees, contractors, and third parties who may possess relevant information.

### 2. Triggering Events
A legal hold must be issued as soon as any of the following is reasonably anticipated or occurs:
- Receipt of a demand letter, pre-action notice, or formal claim
- Filing of a lawsuit, arbitration, or regulatory complaint naming the company
- A regulatory investigation, subpoena, or government inquiry
- Internal investigation that may result in external proceedings
- Knowledge of facts that make litigation or investigation likely (even without formal notice)

**Key principle**: preservation obligation attaches at the moment of reasonable anticipation — not at the moment of service. In jurisdictions with spoliation sanctions, destruction after the trigger date is sanctionable even if no formal hold notice was issued.

### 3. Hold Manager and Responsibilities

| Role | Responsibility |
|---|---|
| Hold Manager (typically GC or assigned counsel) | Initiates the hold; identifies custodians; issues notices; tracks acknowledgments; manages release |
| IT Custodian | Implements automated preservation in email/document systems; disables auto-delete for relevant custodians |
| HR | Provides current employee information; coordinates for departed employees |
| Business Unit Manager | Confirms scope of relevant documents in their team |
| Each Custodian | Acknowledges the hold; preserves documents; reports new or overlooked sources |

### 4. Custodian Identification
- Identify all employees, contractors, and agents likely to possess relevant documents based on the matter facts.
- Interview the business unit responsible for the relevant project or relationship.
- Include former employees if their documents remain in company systems or archives.
- Revisit custodian list whenever the scope of the matter expands.

### 5. Hold Notice Issuance
- Issue a written legal hold notice to each identified custodian.
- Notice must describe: the matter triggering the hold; the types of documents and data to be preserved; the systems covered (email, shared drives, messaging apps, personal devices if used for business); the prohibition on deletion or alteration; the contact for questions.
- Issue via email with read receipt, or via the company's matter management system.
- For paper records: instruct custodians to segregate and not destroy physical files.
- See [[prompt-pack-litigation-hold-notice]] for the individual notice template.

### 6. IT Preservation Steps
- Suspend automatic email deletion policies for all custodian mailboxes.
- Create a preservation copy / litigation hold in the email platform (e.g., Microsoft 365 Purview, Google Vault) for custodian accounts.
- Identify and preserve relevant network shares, SharePoint sites, and document repositories.
- Flag relevant records in ERP or CRM systems to prevent routine purging.
- Collect a forensic image of custodian devices if circumstances require (e.g., suspected deletion).

### 7. Acknowledgment Tracking
- Require each custodian to acknowledge the hold in writing (email reply or system confirmation) within [5] business days.
- Maintain a hold tracking log:

| Custodian | Role | Notice date | Acknowledgment date | Acknowledgment received (Y/N) | Follow-up sent (date) |
|---|---|---|---|---|---|

- Escalate non-responses to the custodian's manager and HR after [10] business days.

### 8. Ongoing Hold Maintenance
- Issue hold reminders to all active custodians at least every [90] days.
- When new custodians are identified, add them to the hold immediately.
- When the scope expands (new claims, new time periods), issue an amended hold notice.
- When key custodians leave the company: collect and preserve their data before IT access is revoked; ensure their departure does not trigger inadvertent data deletion.

### 9. Hold Release
A hold may be released only when:
- The litigation, arbitration, or investigation has fully concluded (all appeals exhausted, regulatory file closed)
- The GC or outside counsel confirms in writing that preservation is no longer required

Release process:
1. GC issues written hold release notice to all custodians and IT.
2. IT re-enables standard document retention and auto-deletion policies.
3. Custodians informed they may return to standard document management practices.
4. Retain the hold release notice in the matter file.

### 10. Documentation for Defensibility
Maintain a master hold file containing:
- Initial hold notice and all amended notices
- Custodian acknowledgment log
- IT confirmation of preservation steps taken
- Hold reminder communications
- Any communications with outside counsel about preservation scope
- Hold release notice

This documentation demonstrates good-faith compliance with preservation obligations if spoliation sanctions are sought by an opposing party.

## Jurisdictional notes

| Jurisdiction | Key points |
|---|---|
| **Common law (DIFC, ADGM, UK, US)** | Spoliation sanctions well-established; adverse inference instruction available for deliberate destruction; proportionality principle under DIFC/ADGM court rules limits scope of preservation to relevant material. |
| **UAE (onshore)** | UAE Civil Procedure Law does not have a US-style e-discovery framework, but courts can order document production and destruction of evidence can support adverse inference; hold procedures still protect against allegation of bad faith. |
| **KSA** | Saudi courts have broad powers to order document production; best practice is to implement holds consistent with international standards for any cross-border matter. |
| **Lebanon** | Lebanese courts apply civil-law procedure; document preservation is less systematically enforced but contractual or regulatory obligations may still require holds. |
| **GDPR / data protection** | Legal hold obligations override GDPR erasure requests during the period of hold. Document the legal basis for retention. Upon hold release, process any outstanding erasure requests. |

## Common mistakes

- **Waiting for service of process**: by the time a claim is served, the trigger for preservation has often already passed. Issue holds on reasonable anticipation.
- **Forgetting messaging apps**: WhatsApp, Teams, Signal, and SMS are increasingly discoverable; include them in custodian instructions.
- **Not confirming IT auto-deletion is suspended**: issuing a notice to custodians without disabling auto-delete in email systems means documents continue to be purged.
- **Releasing holds prematurely**: do not release until all appellate periods have expired and any regulatory file is formally closed.

## Related skills

- [[prompt-pack-litigation-hold-notice]]
- [[prompt-pack-legal-opinion-on-dispute]]
- [[prompt-pack-matter-closing-procedure]]
- [[prompt-pack-legal-department-kpi-dashboard]]
