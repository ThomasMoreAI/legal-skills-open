---
name: prompt-pack-document-production-request-sboghossian
title: Document Production Request
description: Use when drafting document production requests for international arbitration proceedings, following the Redfern Schedule format. Covers categories, relevance, materiality, and the "not reasonably available" standard required by IBA Rules on the Taking of Evidence. Applicable across all major arbitral seats and institutions (ICC, LCIA, DIAC, ADCCAC, SIAC, AAA/ICDR). Trigger when a party to arbitration needs to request documents from the other side or when responding to such a request.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-document-production-request
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Document Production Request

## When to use this

Use this skill when a party to international arbitration proceedings needs to request documents from the opposing party (or third parties, where rules allow). Unlike litigation discovery, arbitral document production is structured around the Redfern Schedule — a four-column table that has become the industry standard — and is governed primarily by the IBA Rules on the Taking of Evidence in International Arbitration (2020 edition) or institutional equivalents.

Typical triggers:
- Counsel is preparing a document production application to submit to the tribunal
- Responding to a production request and needing to formulate objections in Redfern format
- Tribunal has issued a Procedural Order setting the timeline for document production
- Party needs to identify what documents exist and how to request them without over-disclosure obligations on itself

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Arbitration case reference / seat | Identifies the applicable institutional rules and governing procedure | Ask before proceeding |
| Party making the request | Clarifies requestor vs. respondent framing | Ask |
| Applicable arbitration rules | ICC, LCIA, DIAC, ADCCAC, SIAC, UNCITRAL, ad hoc — affects IBA Rules applicability | Ask |
| Categories of documents sought | The substance of each production request | Ask in detail |
| Relevance and materiality for each category | IBA Rules require this to be stated per request | Ask for each category |
| Legal/factual issues each category relates to | Required for Redfern Schedule Column 2 | Ask |

## Optional inputs

- Prior document production orders from the tribunal
- Procedural Order governing document production timeline
- Privilege claims anticipated (attorney-client, professional secrecy, state secrets)
- Data protection objections (GDPR, UAE PDPL, KSA PDPL) anticipated
- Confidentiality designations applicable to produced documents

## Document structure — Redfern Schedule

The Redfern Schedule is a four-column table. Each row is one production request.

| Column | Content | Drafter's task |
|---|---|---|
| **Column 1** | Description of requested documents or category | Identify with precision — "all emails between X and Y from January 2023 to June 2023 relating to the valuation of the target" |
| **Column 2** | Relevance and materiality | Explain which factual or legal issue this category is relevant to; link to specific claim or defense |
| **Column 3** | Response by opposing party | Left blank by requestor; opposing party completes with: (a) will produce, (b) objects (with grounds), (c) confirms documents do not exist |
| **Column 4** | Tribunal's decision | Left blank; tribunal rules row by row after receiving both parties' positions |

### Standard IBA Rules criteria for production (Art. 3)

Each request must satisfy all of the following:
1. Documents or categories are **sufficiently identified** — no fishing expeditions
2. Documents are in the **possession, custody or control** of the other party
3. Documents are **relevant to the case** and **material to its outcome**
4. Documents are **not reasonably available** to the requesting party by other means

### Typical production categories in commercial arbitration

1. All contracts between [Party A] and [Party B] relating to [transaction]
2. All communications (correspondence, email, messaging) between [specific persons] from [date range] concerning [subject matter]
3. All board resolutions, shareholder resolutions, and internal approvals relating to [decision]
4. All financial records, invoices, bank statements evidencing [payment/loss]
5. All expert analyses, valuations, or due diligence reports prepared for [Party] in connection with [transaction]
6. All regulatory filings, license applications, or correspondence with [authority] regarding [subject]
7. All insurance policies and claims records relating to [asset/event]
8. All documents evidencing [specific factual contention in Statement of Claim/Defense]

### Privilege and confidentiality objections (common Column 3 responses)

- **Attorney-client privilege**: Documents prepared for or by legal counsel for the purpose of obtaining or giving legal advice.
- **Work product / litigation privilege**: Documents prepared in anticipation of litigation or for use in these proceedings.
- **State secrets**: Documents involving government communications (in disputes involving state entities).
- **Professional secrecy** (civil-law jurisdictions): Broader than common-law privilege; may cover communications with auditors, notaries, certain advisers.
- **Data protection**: Production of documents containing personal data may require redaction or data processing justification under GDPR, UAE PDPL (Federal Decree-Law No. 45 of 2021), KSA Personal Data Protection Law, or Lebanese data protection norms.

## Jurisdictional notes

### Arbitral seat considerations

| Seat | Key considerations |
|---|---|
| **DIFC** | DIFC Arbitration Law (DIFC Law No. 1 of 2008, as amended); DIFC Courts support arbitration by granting interim orders; IBA Rules commonly adopted |
| **ADGM** | ADGM Arbitration Regulations; similar DIFC framework; sophisticated commercial court support |
| **Dubai (onshore)** | DIAC Arbitration Rules; Federal Arbitration Law (UAE Federal Law No. 6 of 2018); IBA Rules applicable if parties agree or tribunal adopts |
| **Abu Dhabi (ADCCAC)** | ADCCAC Rules; arbitral awards enforceable under UAE Federal Arbitration Law |
| **KSA (SAGIA / Saudi Center for Commercial Arbitration)** | Saudi Arbitration Law (Royal Decree M/34); SCCA Rules; growing alignment with international standards; document production less routinely ordered than in Western arbitrations |
| **Lebanon (CIAM)** | Lebanese Code of Civil Procedure (Arts. 762 et seq.); CIAM Rules; IBA Rules can be adopted; political environment creates enforcement challenges |
| **Egypt (CRCICA)** | CRCICA Rules; Egyptian Arbitration Law (Law No. 27 of 1994); New York Convention signatory |
| **ICC (Paris seat)** | ICC Rules 2021; Note to Parties on document production; IBA Rules widely adopted; strong enforcement under New York Convention |

### Civil-law vs. common-law approach to production

In civil-law traditions, document production is narrower. Parties are not obligated to produce documents that harm their case. Tribunals with civil-law arbitrators (especially French, Egyptian, or Lebanese-trained) may apply a restrictive approach to Column 4 rulings. Common-law practitioners should frame requests narrowly and specifically rather than requesting broad categories.

## Drafting standards

- **Each request = one row**: Do not bundle multiple distinct categories in one row — the tribunal needs to be able to rule on each separately.
- **Be specific about date ranges and persons**: Vague categories ("all relevant documents") will be objected to as fishing expeditions and rejected.
- **Identify the nexus to the case**: Column 2 must explain precisely why this category is material — cite the specific contractual clause, factual allegation, or legal issue.
- **Acknowledge anticipated objections**: If privilege is likely, pre-address it by narrowing the request to "non-privileged documents" or "communications not prepared for the purpose of legal advice."
- **Request confirmation of non-existence**: Where documents are expected to exist but may have been deleted or never created, explicitly request confirmation that they do not exist.

## Common mistakes

- **Over-requesting**: Large Redfern Schedules with dozens of broad requests signal inexperience and often result in blanket objections; focus on the 5-10 categories that are truly material.
- **Conflating arbitration production with common-law discovery**: Arbitral document production is narrower; the IBA Rules standard is stricter than FRCP or CPR standard disclosure.
- **No follow-up on Column 3 objections**: If the other party objects in Column 3, counsel must engage with the objection in writing and file a short response for the tribunal's Column 4 ruling.
- **Missing the procedural order deadline**: Document production is strictly timetabled; late requests require tribunal permission and may not be permitted.
- **Privilege log failures**: If a party claims privilege over withheld documents, it must typically provide a privilege log (document-by-document or category-by-category); failure to provide one weakens the privilege claim.

## Related skills

- [[prompt-pack-discovery-request]]
- [[prompt-pack-emergency-arbitrator-application]]
- [[prompt-pack-expert-report-arbitration]]
- [[prompt-pack-injunction-application]]
