---
name: prompt-pack-data-subject-access-request-procedure-sboghossian
title: Data Subject Access Request Procedure
description: 'Use when a company needs to draft an internal procedure for handling Data Subject Access Requests (DSARs) or equivalent individual rights requests under applicable data protection law. Covers identity verification, search protocols, response timelines, exemptions assessment, format of response, and escalation. MENA-aware: UAE PDPL, DIFC DP Law, ADGM DP Regs, KSA PDPL alongside GDPR and UK GDPR; timelines and exemptions differ by jurisdiction.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-data-subject-access-request-procedure
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Data Subject Access Request Procedure

A Data Subject Access Request (DSAR) is a legal right that must be fulfilled on time. Missing a response deadline is itself a data protection violation and can be the basis for a regulatory complaint, even if the company has an otherwise clean compliance record. The procedure must be practical enough for non-lawyers to follow under time pressure.

## When to use this

- A company is implementing a data protection compliance program and needs a formal DSAR-handling procedure.
- The company has received a DSAR and does not have an existing procedure (urgent — the response clock is already running).
- A regulatory audit or certification exercise requires evidence of a documented rights-request procedure.
- The company has recently become subject to a new data protection law that introduces individual rights obligations.
- The company's existing procedure needs to be updated to cover new jurisdictions or rights introduced by new laws.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Company name and jurisdiction(s) of operation | Determines applicable legal framework and response timeline | Ask the user |
| Types of individual rights to be covered | GDPR covers access, erasure, portability, rectification, restriction, and objection; other laws vary | Default to access (DSAR) as primary; include erasure; extend to other rights if applicable law requires |
| Categories of personal data held | Determines the scope of searches required | Ask the user; use the company's data inventory if available |
| Current data systems and repositories | Shapes the search protocol | Ask the user |
| DPO contact details | The DPO coordinates and escalates DSARs | Ask the user |

## Optional inputs

- Whether the company uses a DSAR management platform or processes requests manually.
- Whether third parties (processors) hold data on the company's behalf that must be included in search scope.
- Whether the company processes special category data (requires extra care and confidentiality).
- Whether employees, customers, or other specific data subject categories have their own sub-procedures.

## Procedure structure

### 1. Receiving a DSAR

**1.1 Channels for submission**
A DSAR can be received by any means: email, post, phone, in-person, or via the website privacy portal (if available). There is no requirement for a specific form. However, the company should designate a single receiving address (e.g., privacy@company.com) and ensure all staff know to forward requests received through other channels.

**1.2 Log the request**
On receipt, log the DSAR in the DSAR Register immediately, noting:
- Date received (this starts the response clock).
- Identity of the requester (or stated identity if not yet verified).
- Nature of the request (access / erasure / portability / other).
- Channel received.
- Assigned case handler.

**1.3 Send acknowledgment**
Acknowledge receipt within 2 business days, providing a reference number and expected response date. Do not delay acknowledgment pending identity verification — both can run in parallel.

---

### 2. Identity verification

**Why it matters:** The company cannot disclose third-party personal data in error. Verification must be proportionate to the sensitivity of the data.

**Standard verification:**
- Confirm name, email address, and at least one additional identifier (account number, date of birth, last transaction) matches the company's records.
- For low-sensitivity data, email confirmation from the registered email address may suffice.

**Enhanced verification (for special category data or high-volume personal data):**
- Request a copy of government-issued photo ID (passport or national ID).
- For UAE data subjects: Emirates ID or passport.
- For KSA data subjects: National ID (Hawiyya) or passport (Iqama for expatriates).
- For Lebanese data subjects: Lebanese ID or passport.

**Third-party requests:**
If the request is made by an agent acting on behalf of the data subject (e.g., a lawyer or family member), verify: (a) the data subject's own identity and (b) the authority given to the agent (notarised power of attorney recommended for high-sensitivity data).

**Timeline:** Identity verification should not extend the response deadline unless the company has genuine reason to doubt the requester's identity. If clarification is sought, the response deadline is paused from the date the company requests further information until the date it is received.

---

### 3. Scope of the DSAR

**3.1 What must be provided under an access request?**
Under GDPR Art. 15 (and equivalent provisions), the data subject is entitled to:
1. Confirmation of whether personal data is being processed.
2. A copy of the personal data.
3. The purpose of processing.
4. The categories of data processed.
5. Recipients or categories of recipients to whom the data has been disclosed.
6. Envisaged retention periods (or criteria for determining them).
7. Information about the data subject's rights (rectification, erasure, restriction, objection).
8. The right to lodge a complaint with the supervisory authority.
9. Source of the data (if not collected directly from the data subject).
10. Any automated decision-making / profiling, including meaningful information about the logic involved.

**3.2 What is not required?**
The access right is to the data subject's own personal data only. Do not include:
- Third-party personal data (redact third-party names unless necessary to provide meaningful information).
- Legal privilege material (correspondence with lawyers is exempt under most frameworks).
- Commercially sensitive information (there is no "business interests" exemption under GDPR; but this may apply in some MENA frameworks — verify by jurisdiction).

**3.3 Jurisdiction-specific scope differences:**

| Jurisdiction | Key scope difference |
|---|---|
| GDPR / UK GDPR | Full Art. 15 obligations as above; strong rights |
| UAE PDPL | Art. 7 right of access; broadly equivalent to GDPR; TDRA guidance to be monitored |
| DIFC DP Law | Art. 19–20; equivalent to GDPR; DIFC Commissioner guidance available |
| ADGM DP Regs | Equivalent to DIFC; ADGM Commissioner guidance available |
| KSA PDPL | Art. 4–5; right to know what data is held and its purposes; rectification and erasure rights; NDMO guidance governs specifics |
| Lebanon | No comprehensive law in force; apply GDPR as best practice |
| Egypt | Law No. 151 of 2020 Art. 26; access and rectification rights; MCIT oversight |

---

### 4. Search protocol

A systematic, documented search is essential — both to fulfill the request accurately and to demonstrate compliance to a regulator.

**4.1 Search scope mapping**
For each DSAR, the case handler sends a search request to each data repository owner:

| Repository | Owner | Search method | Estimated time |
|---|---|---|---|
| CRM system | Sales / Customer Service | Name + email search | 1 hour |
| HR system | HR | Employee ID or name search | 30 minutes |
| Email (all company email) | IT | eDiscovery search by name, email | 2–4 hours |
| Finance system | Finance | Customer / supplier ID search | 1 hour |
| Cloud storage (SharePoint, Drive) | IT | Keyword search | 2 hours |
| Third-party processors (list) | DPO | Sub-requests to processors per DPA | Processor response window |

**4.2 Search documentation**
Record: what was searched, by whom, using what search terms, and the number of results retrieved. This documentation protects the company if the completeness of the response is challenged.

**4.3 Third-party processor searches**
The company must include data held by processors on its behalf. Issue sub-requests to processors as soon as the DSAR is confirmed. DPA terms should provide a mechanism for processors to respond within a timeframe that allows the controller to meet its own deadline.

---

### 5. Exemptions assessment

Before compiling the response, review whether any exemptions apply:

| Exemption | When it applies | Jurisdiction |
|---|---|---|
| Legal privilege | Documents containing legal advice or litigation communications | GDPR; DIFC DP Law; most frameworks |
| Crime prevention and detection | Processing for prevention, detection, investigation of crime | GDPR; applicable in MENA frameworks with local law basis |
| Third-party privacy | Redact third-party personal data that would identify individuals not party to the request | All frameworks |
| Disproportionate effort | Where providing a copy would involve disproportionate effort — provide a description instead; must justify | GDPR Art. 15(4); DIFC DP Law |
| Repeated or manifestly unfounded requests | Company may charge a reasonable fee or refuse | GDPR Art. 12(5); equivalent in MENA frameworks |
| National security / law enforcement | Data processed by or for national security purposes; narrow | Jurisdiction-specific |

Document the exemption decision and the legal basis. Partial redaction is preferable to complete refusal — redact the exempt information and provide the rest.

---

### 6. Compiling and sending the response

**6.1 Format**
- Electronic format is the default for electronic requests (PDF compilation is typical; secure file transfer or portal download link for large datasets).
- The response must be in a "commonly used, machine-readable format" if portability is requested (GDPR Art. 20).
- Paper format for paper requests or where the data subject does not have access to electronic means.

**6.2 Content**
- Cover letter identifying the legal basis for processing, the categories of data, retention periods, and the data subject's further rights.
- Annex: the personal data itself (redacted where third-party data or exemptions apply).
- Information about the right to complain to the supervisory authority.

**6.3 Secure transmission**
- Do not send personal data in unencrypted email attachments.
- Use a secure file transfer method, password-protected PDF, or the company's secure portal.
- For physical records: use tracked, signed-for delivery.

---

### 7. Response timelines

| Jurisdiction | Standard deadline | Extension |
|---|---|---|
| GDPR / UK GDPR | 1 calendar month from receipt | Up to 2 additional months for complex or numerous requests; notify data subject of extension and reason within 1 month |
| UAE PDPL | Not explicitly specified; apply 30 days as a reasonable standard pending TDRA guidance |  |
| DIFC DP Law | 30 days | 30-day extension with notification |
| ADGM DP Regs | 30 days | 30-day extension |
| KSA PDPL | NDMO regulations specify; apply 30 days pending clear guidance | — |
| Egypt | Law No. 151 specifies 30 days | — |

**The clock starts on the date the request is received, not the date it is first reviewed.** If identity verification is sought, the clock is paused from the date the company requests information until the date it is received, but only if the request to verify is proportionate and necessary.

---

### 8. Refusal procedure

If a request is refused (wholly or in part):
- Inform the data subject within 1 month of receipt of the request.
- State the reasons for refusal.
- Inform the data subject of their right to complain to the supervisory authority and to seek judicial remedy.
- Do not simply ignore the request.

---

### 9. Escalation and complaints

If the data subject is dissatisfied with the response or escalates to the supervisory authority:
- The DPO manages the supervisory authority interaction.
- Preserve all documentation of the response process.
- External privacy counsel is engaged if a formal investigation is commenced.

---

## Common mistakes

- Missing the response deadline because the search protocol takes too long — preemptively map all data repositories and assign owners before a request is received.
- Disclosing third-party personal data in the response — always redact before sending.
- Not logging the request immediately — the clock runs from receipt, not from when someone notices it.
- Treating privileged legal advice as outside the scope of the search — privilege is an exemption to disclosure, not an exemption from searching.
- Sending the response by unencrypted email — this creates a new personal data breach.

## Related skills

- [[prompt-pack-data-processing-agreement]]
- [[prompt-pack-data-retention-policy]]
- [[prompt-pack-data-breach-response-plan]]
- [[prompt-pack-privacy-policy]]
- [[prompt-pack-cross-border-data-transfer-assessment]]
