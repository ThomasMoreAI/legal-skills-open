---
name: foi-data-request-ur-grue
title: FOI Data Request
description: Drafts a Freedom of Information request specifically targeting datasets, databases, or digital records — written to maximise the chance of receiving complete, machine-readable data rather than summary PDFs or partial tables.
author: ur-grue
author_url: https://github.com/ur-grue/autopunk-media-skills/tree/main/skills/data-journalism/investigation/foi-data-request
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: data-protection
language: en
tags: [foi, freedom-of-information, data-request, investigation, public-records]
---

# FOI Data Request

## What This Skill Does
Drafts a Freedom of Information request specifically targeting datasets, databases, or digital records — written to maximise the chance of receiving complete, machine-readable data rather than summary PDFs or partial tables.

## When To Use This Skill
- You want to obtain a specific dataset held by a public body and need the request worded precisely enough to prevent a narrow interpretation
- You have already received an FOI response containing a summary table and want to re-request the underlying data in full
- You want to include specific clauses requesting machine-readable format, codebooks, and data dictionaries alongside the data
- You need to ask for multiple related datasets in a single, clearly organised request

## What You Need To Provide
**Required:** The name of the public body you are submitting to. A description of the data you believe they hold — what it records, the approximate time period, and what you have found in published reports or previous FOIs that suggests it exists. Your name (or a publication name if submitting formally).
**Optional:** Specific columns or fields you know exist; the file format you want the data in (CSV, Excel, database export); any known previous FOI that touched the same data; jurisdiction (to ensure correct statutory references are used).

## How the Assistant Approaches This
1. Structures the request around the specific data sought — naming fields, date ranges, and systems where known — rather than using vague language that invites partial disclosure.
2. Includes standard data-journalist clauses: requesting machine-readable format, a data dictionary or codebook if one exists, and any published schema or data model.
3. Adds standard scaffolding: statutory basis for the request, a deadline note, a request for notification if the request is likely to be refused in part, and contact information.

## Output Format
A formal letter in three sections: (1) Purpose and identification — who you are and why you are making the request (brief, neutral, no obligation to explain). (2) The request — specific numbered items, each naming the data sought with as much precision as possible. (3) Format and process — your preferred format, a request for the data dictionary, and a note on partial disclosure. Approximately 350–600 words. Formal register throughout.

## Quality Criteria
- [ ] Each requested item is a specific, numbered ask — not a single broad request
- [ ] A machine-readable format is explicitly requested
- [ ] A data dictionary or schema is requested alongside the data
- [ ] The request does not over-explain the journalistic purpose (which could invite unnecessary review)
- [ ] The statutory basis for the request is cited correctly for the jurisdiction
- [ ] A partial disclosure clause is included

## Example

### Input
Public body: National Infrastructure Agency
Data sought: I believe they hold a central database of all infrastructure contracts awarded since 2018, including contractor names, contract values, award dates, tender outcomes (whether competitive or sole-sourced), and registered company addresses. I've seen summary tables in their annual reports but never the underlying data.
Jurisdiction: EU member state with national FOI legislation
My name: [Journalist name, publication name]

### Output
[Journalist name]
[Publication name]
[Address / email]
[Date]

Freedom of Information Request
National Infrastructure Agency
[Address]

---

Dear Freedom of Information Officer,

I am writing to request access to information held by the National Infrastructure Agency under [national FOI statute, e.g. Freedom of Information Act / Accesso ai Documenti Amministrativi / applicable national law]. I am a journalist at [publication name].

**The request**

I request the following information in relation to infrastructure contracts awarded by or administered through the National Infrastructure Agency:

1. **Full contracts database, 2018–present:** All records in the National Infrastructure Agency's central contracts register (or equivalent system) covering the period January 2018 to the date of this request. For each contract record, I request all fields held, including but not limited to: contract identifier, contractor name, contractor registered address and company registration number, contract value, contract award date, contract start and end dates, tender type (open competitive / restricted / negotiated / sole-source / framework call-off), and procurement category or classification code.

2. **Data dictionary or codebook:** If the database or system described above has a data dictionary, schema document, data model, or any document explaining what each field contains and how it is coded, I request a copy of this alongside the data.

3. **Redaction log:** If any fields are withheld in part or full, I request a log identifying which fields have been withheld and the exemption relied upon for each.

**Format**

I request the data in a machine-readable, structured format — preferably CSV or XLSX. I do not require a summary table, PDF report, or printed document; I specifically request the underlying row-level data.

**Partial disclosure**

If any part of this request is refused, I request that the remainder be disclosed. Please notify me before refusing any component so that I may consider narrowing the scope if that would facilitate disclosure.

**Clarification**

I am happy to discuss the scope of this request if that would assist you in responding. I can be reached at [email address].

I expect a response within the statutory timeframe applicable under [national FOI statute]. If you require clarification to process this request, please contact me within five working days so as not to delay the response clock.

Yours faithfully,
[Journalist name]
[Publication name]
[Contact details]

## Known Limitations
- This skill produces a general-purpose FOI letter. Specific jurisdictions have different statutes, different exemptions, different statutory response times, and different tribunals for appeals. Always verify the correct statute name and response deadline for the specific country or territory before sending.
- The letter does not address commercial sensitivity exemptions, which public bodies frequently use to withhold procurement data. If the request is refused on this basis, a separate appeal letter will be needed.
- Some public bodies classify contract databases as operational IT systems and argue they are not "held" in a form accessible under FOI. This request anticipates that objection by asking for a data export rather than direct system access, but it may not prevent the objection.

## Related Skills
- [scraper-brief](../scraper-brief/SKILL.md)
- [dataset-summary-brief](../../analysis/dataset-summary-brief/SKILL.md)
- [data-story-finder](../../analysis/data-story-finder/SKILL.md)
