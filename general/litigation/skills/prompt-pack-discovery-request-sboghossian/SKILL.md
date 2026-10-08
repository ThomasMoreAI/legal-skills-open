---
name: prompt-pack-discovery-request-sboghossian
title: Discovery Request
description: Use when drafting discovery requests — interrogatories, requests for production of documents, and requests for admission — for civil litigation proceedings. Covers proportionality, relevance standards, and compliance with procedural rules across jurisdictions. Relevant for disputes practitioners in UAE courts, DIFC/ADGM courts, Lebanon, Egypt, KSA, UK, EU, and US proceedings. Trigger when a client needs formal discovery instruments to compel disclosure of evidence from the opposing party.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-discovery-request
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Discovery Request

## When to use this

Use this skill when a litigant needs to compel the opposing party to provide evidence in pre-trial or pre-hearing proceedings. Discovery instruments vary significantly between common-law adversarial systems (where broad pre-trial discovery is the norm) and civil-law inquisitorial systems (where the judge controls evidence gathering and party-driven discovery is limited).

Typical triggers:
- Counsel needs interrogatories to pin down the opposing party's version of facts
- Document production is needed to build or defend the case
- Requests for admission are needed to narrow issues before trial
- Client is in US, UK, DIFC, or ADGM proceedings where formal discovery is available

**Important**: In civil-law jurisdictions (Lebanon, Egypt, UAE onshore, KSA, France), pre-trial party-driven discovery of the US/UK type does not exist. The equivalent is a court-ordered disclosure request (see [[prompt-pack-document-production-request]] for the arbitration equivalent). Adapt this skill accordingly.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Client / requesting party | Identifies who is propounding the requests | Ask before proceeding |
| Case name and number | Proper caption required | Ask |
| Jurisdiction and court/forum | Determines procedural rules that govern | Ask; critical |
| Key factual issues to be proven | Drives which categories of requests to draft | Ask in detail |
| Opposing party name | Identifies respondent | Ask |
| Stage of proceedings | Discovery is time-sensitive; rules govern when requests may be served | Ask |

## Optional inputs

- Existing pleadings or statement of claim/defense (to calibrate specific requests)
- Prior discovery responses (to assess gaps)
- Privilege log expectations
- Discovery limits (e.g., US federal FRCP Rule 33 limits interrogatories to 25 without leave of court)
- Electronic discovery (e-discovery) scope and custodians

## Document structure

### Interrogatories

1. **Caption and instructions** — Case caption; definitions section (define "you," "document," "communication," "relating to," etc.); instructions on answering under oath and objection procedure.

2. **Background interrogatories** — Identify all persons with knowledge; identify all documents relevant to the disputed facts.

3. **Merits interrogatories** — Targeted to each disputed element: 
   - Identify all persons with knowledge of [specific transaction/event]
   - Describe all communications with [counterparty] regarding [subject]
   - State the basis for the claim that [specific assertion in pleadings]

4. **Damage/quantum interrogatories** — Identify all losses claimed; describe calculation methodology; identify all mitigation steps taken.

5. **Verification block** — Signature under oath by a party officer or authorized representative.

### Requests for Production (RFP)

1. **Caption and instructions** — Same as interrogatories; include definitions for "document" (broad: paper, electronic, metadata, voicemails, etc.) and "electronically stored information" (ESI).

2. **Document categories** — Numbered requests, each targeting a specific category:
   - All contracts between the parties relating to [subject]
   - All communications (email, messaging, written) from [date range] concerning [topic]
   - All financial records evidencing [payment, loss, valuation]
   - All board minutes, resolutions, and internal approvals relating to [decision]
   - All expert materials, analyses, or valuations prepared in connection with [matter]

3. **ESI protocol reference** — If agreed, reference the parties' ESI protocol or propose one.

### Requests for Admission (RFA)

1. **Caption and instructions** — Failure to respond within the deadline (28 days in US federal court; similar in DIFC/ADGM) results in deemed admission.

2. **Fact admissions** — "Admit that on [date], [party] executed the contract attached as Exhibit A."

3. **Authenticity admissions** — "Admit that the document attached as Exhibit B is a true and accurate copy of [document description]."

4. **Legal conclusion admissions** (use sparingly) — "Admit that [party] breached the obligation set forth in Clause 5.2 of the Agreement."

## Jurisdictional notes

| Jurisdiction | Discovery regime | Key rules |
|---|---|---|
| **DIFC Courts** | Common-law adversarial; broad discovery | DIFC Courts Rules Part 28; disclosure obligations similar to English CPR Part 31 |
| **ADGM Courts** | Common-law; modeled on English procedure | ADGM Court Procedure Rules; standard disclosure plus specific disclosure on application |
| **UAE Onshore** | Civil-law inquisitorial; no party-driven discovery | Judge requests documents; parties submit evidence with pleadings; Federal Law of Evidence governs |
| **KSA** | Sharia-based civil procedure; judge-directed | Evidence Code; expert witnesses appointed by court, not parties |
| **Lebanon** | French-model civil procedure (NCPC equivalent) | Juge de la mise en état can order production; party-driven requests go through judge |
| **Egypt** | Civil Procedure Law; judge-directed | Parties can request court to order production; broad discovery unknown |
| **UK** | CPR Part 31 standard disclosure + specific disclosure | Duty to preserve from time of litigation hold; Peruvian Guano test for relevance (broad) |
| **US Federal** | FRCP Rules 26–37; broad pre-trial discovery | Rule 26 initial disclosures; 25-interrogatory limit; proportionality standard post-2015 |

## Drafting standards

- Each request must be framed to be: (a) relevant to a claim or defense, (b) proportionate to the needs of the case, (c) specific enough to identify the information sought.
- Avoid omnibus requests ("all documents relating to the dispute") that will draw objections — break them into targeted categories.
- Use defined terms consistently throughout all three instruments.
- In common-law systems, include a litigation hold reference in the cover letter accompanying the requests.
- In civil-law systems, reframe as an application to the court or tribunal requesting a document production order, citing the specific facts and legal provision that supports compelled disclosure.

## Common mistakes

- **Over-broad requests**: Courts routinely sustain "overbreadth" objections; draft tightly and you will get more.
- **Failure to define ESI scope**: Without an agreed e-discovery protocol, massive disputes arise over format, custodians, and search terms.
- **Missing the deadline**: Discovery requests in most systems must be served within fixed periods after filing; check the applicable rules.
- **Applying US-style discovery to civil-law proceedings**: Civil-law courts do not recognize interrogatories as a mechanism; use the court's procedural tools instead.
- **No verification**: Interrogatory answers must be verified under oath by an authorized party representative; unsigned answers are defective.

## Related skills

- [[prompt-pack-document-production-request]]
- [[prompt-pack-injunction-application]]
- [[prompt-pack-enforcement-of-judgment]]
- [[prompt-pack-expert-witness-report-outline]]
