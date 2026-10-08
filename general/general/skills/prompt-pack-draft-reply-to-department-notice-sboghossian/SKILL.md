---
name: prompt-pack-draft-reply-to-department-notice-sboghossian
title: Draft Reply to Department Notice
description: Use when drafting a formal professional reply to a notice, inquiry, or assessment issued by a government department or regulatory authority — covering tax authorities, labor departments, financial regulators, customs agencies, and other public bodies. Draws on relevant legal provisions, procedural rights, and judicial or administrative precedents to contest, clarify, or comply with the notice. Applicable across MENA (UAE, KSA, LB, EG), EU, UK, and other jurisdictions. Trigger when a client has received a government notice and needs a structured, legally grounded response within the specified deadline.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-draft-reply-to-department-notice
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Draft Reply to Department Notice

## When to use this

Use this skill when a company or individual has received a formal notice from a government department or regulatory authority and requires a professionally drafted, legally grounded reply. Government notices demand careful, timely responses — the reply creates an official record, may preserve appeal rights, and can affect penalty outcomes.

Common department notice types:
- Tax authority notices (deficiency assessment, audit request, penalty notice, request for information)
- Labor/employment department notices (inspection, violation notice, worker complaint)
- Financial regulator notices (licensing inquiry, compliance breach, AML/KYC deficiency)
- Customs and trade authority notices (misclassification, valuation dispute, import prohibition)
- Municipal or building authority notices (planning, occupancy, safety)
- Central bank or payment authority notices (e-money, payment system licensing)
- Data protection authority notices (data breach, GDPR/PDPL inquiry)

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| The original department notice | The substance to be responded to | Must be provided; cannot draft without it |
| Responding party (client) name and registration details | Identity on record with the authority | Ask |
| Jurisdiction and authority name | Determines applicable laws, procedures, and precedent | Ask |
| Response deadline | Many notices have strict response windows; missing them waives rights | Ask; flag urgency if less than 7 days |
| Client's position on the substance | Do they contest, accept with explanation, or partially comply? | Ask in detail |
| Supporting documents to attach | Proof of compliance, payment records, correspondence | Ask |

## Optional inputs

- Prior correspondence with the authority on the same matter
- Relevant judicial or administrative tribunal decisions (if client has knowledge of favorable precedents)
- Audit or third-party expert report supporting the client's position
- Certified translations (if the authority's notice was in a different language than the response)

## Document structure

1. **Header and reference** — Authority name and address; date; reference number of the original notice; subject: "Reply to Notice Reference [X] dated [date]."

2. **Opening acknowledgment** — Confirm receipt of the notice; identify the responding party; note the matter in general terms: "We write on behalf of [Client] in response to your notice dated [date] concerning [subject]."

3. **Factual background** — A brief, accurate account of the relevant facts from the client's perspective:
   - The client's business and its relationship to the authority's jurisdiction
   - What the notice alleges or requests
   - What the client's position is

4. **Legal and factual submissions** — The substantive response, organized by issue:

   **If contesting the notice:**
   - Identify the specific grounds of disagreement (factual error, legal misapplication, procedural defect in the notice)
   - Cite applicable statutory provisions, regulations, or administrative guidance
   - Reference any favorable precedents or published authority guidance (without fabricating citations)
   - Submit supporting evidence

   **If accepting with explanation:**
   - Acknowledge the finding; explain any mitigating circumstances
   - Identify corrective action already taken or proposed
   - Request reduction of penalty based on cooperation and remediation

   **If requesting clarification or extension:**
   - Note which part of the notice is unclear or requires additional time to respond to
   - Request specific relief: "We respectfully request an extension of [X] days to gather the documentation requested in Item 3 of the notice."

5. **Procedural rights reservation** — Where applicable, expressly reserve the right to appeal or file an administrative review if the authority issues an adverse decision.

6. **Undertakings (if appropriate)** — Specific commitments the client is willing to make: remediation steps, payment plans, compliance undertakings. Only include if the client has authorized them.

7. **Attachments list** — Number and describe each exhibit attached.

8. **Closing and signature** — Formal close; authorized signatory's name, title, and contact details.

## Jurisdictional notes

### Tax authority notices — MENA

| Jurisdiction | Authority | Key considerations |
|---|---|---|
| **UAE** | Federal Tax Authority (FTA); Ministry of Finance | VAT and Excise Tax administered by FTA; response periods specified in the Federal Tax Procedure Law; objection then appeal to Tax Disputes Resolution Committee before court |
| **KSA** | Zakat, Tax and Customs Authority (ZATCA) | Zakat (for Saudi entities) and income tax (for foreign entities) and VAT; formal objection within 60 days of assessment; review then tax appeal committee |
| **Lebanon** | Ministry of Finance — Tax Directorate | Income tax, built property tax, VAT; formal contestation within 30 days of assessment; contentious and often delayed process |
| **Egypt** | Egyptian Tax Authority (ETA) | Income tax, VAT; internal appeal then Tax Appeals Commission; Egyptian courts have jurisdiction over final appeals |

### Labor/employment authority notices — MENA

- **UAE Ministry of Human Resources and Emiratization (MoHRE)**: Notices regarding Emiratization quotas, labor camp standards, or worker complaints require response and may trigger on-site inspection; consider whether to engage MoHRE's conciliation service.
- **KSA Ministry of Human Resources**: Nitaqat program compliance notices; Saudization quota requirements; responses should demonstrate compliance or propose a remediation plan with timeline.
- **Lebanon Ministry of Labor**: Notices regarding NSSF (social security) contributions, illegal employment, or worker claims; engage labor law counsel given political sensitivity.

### Financial regulatory notices — MENA

- **UAE Central Bank / SCA / CBUAE**: Notices about AML/KYC deficiencies require immediate acknowledgment and a remediation plan within the notice period; unresponsive institutions face license suspension.
- **DIFC / ADGM FSRA / DFSA**: Notices are formally structured; right to make representations before enforcement action is triggered; sophisticated regulatory process.
- **KSA Capital Market Authority**: CMA enforcement notices require formal written response; legal representation is common.

### Civil-law notice response formalities

In Lebanon, Egypt, and France, responses to regulatory notices often need to be:
- In the official language of the authority
- Signed by an authorized legal representative
- Submitted via the prescribed channel (physical delivery to the ministry, or digital portal if available)
- Accompanied by certified copies of supporting documents

## Drafting standards

- Adopt a formal, professional, respectful tone throughout — avoid adversarial language; authorities are not opposing parties yet.
- Organize the response clearly by reference to the sections/items in the original notice; make it easy for the official to follow.
- Do not make admissions that are not strategically deliberate — every sentence may become part of a subsequent enforcement record.
- Distinguish between factual submissions (what happened) and legal submissions (why the law does not apply or why the penalty should be reduced).
- If requesting an extension, provide a genuine reason and a specific proposed new deadline.
- In tax responses, always include supporting calculations and source documents for any figures relied upon.

## Common mistakes

- **Missing the response deadline**: In UAE, KSA, and most MENA jurisdictions, failing to respond within the stipulated period can result in the authority's assessment or finding becoming final and unappealable.
- **Admitting liability unintentionally**: Phrases like "we apologize for the oversight" or "the error occurred because..." can constitute admissions; use carefully.
- **Not reserving appeal rights**: The reply should always note that the client reserves all rights to challenge any adverse decision.
- **Submitting incomplete supporting documents**: A well-written letter without the supporting evidence it references is weaker than a plain letter with the documents.
- **Wrong language**: UAE FTA requires Arabic submissions for formal objections; ensure Arabic translation is certified and accurate.
- **Underestimating urgency**: Department notices often have 15–30 day response windows; escalate to the client immediately on receipt.

## Related skills

- [[prompt-pack-draft-legal-notice]]
- [[prompt-pack-injunction-application]]
- [[prompt-pack-enforcement-of-judgment]]
- [[prompt-pack-e-money-license-application-memo]]
