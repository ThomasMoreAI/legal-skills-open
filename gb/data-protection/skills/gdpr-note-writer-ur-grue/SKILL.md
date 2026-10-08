---
name: gdpr-note-writer-ur-grue
title: GDPR Note Writer
description: Drafts a GDPR compliance note for a specific piece of journalistic content or data collection activity — documenting the lawful basis for processing personal data, what data is held, how long it is retained, and who has access.
author: ur-grue
author_url: https://github.com/ur-grue/autopunk-media-skills/tree/main/skills/archive-legal/gdpr-note-writer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: data-protection
language: en
tags: [gdpr, privacy, compliance, personal-data]
---

# GDPR Note Writer

## What This Skill Does
Drafts a GDPR compliance note for a specific piece of journalistic content or data collection activity — documenting the lawful basis for processing personal data, what data is held, how long it is retained, and who has access.

## When To Use This Skill
- You are publishing an article, database, or interactive feature that includes personal data about named or identifiable individuals
- You have collected personal data in the course of reporting — interview recordings, source contact details, survey responses — and need to document how it is handled
- Your publication requires internal data protection records for editorial projects
- You are preparing a story that involves scraping, compiling, or analysing datasets containing personal information and need to note your lawful basis and safeguards

## What You Need To Provide
**Required:** A description of the content or activity — what personal data is involved, who the individuals are (e.g. private individuals, public figures, sources, interview subjects), how the data was collected, and what the editorial purpose is.

**Optional:** How long you intend to retain the data, who within your organisation will have access, whether the data will be shared with third parties, whether any data will be published, the country your publication is based in.

## How the Assistant Approaches This
1. Identifies the categories of personal data involved (names, images, location data, financial information, health data, etc.) and flags any special category data under GDPR Article 9, which carries higher obligations.
2. Determines the most appropriate lawful basis for processing under GDPR Article 6 — and, where special category data is involved, Article 9 — with a focus on the journalistic exemptions that most editorial organisations rely on.
3. Drafts a structured compliance note covering: data categories, purpose, lawful basis, retention period, access controls, and any third-party sharing.
4. Flags any specific risks or obligations the journalist or editor should be aware of — for example, the right to erasure, the need for a data processing agreement with a freelancer, or heightened obligations when publishing data about vulnerable individuals.
5. Produces a document that is ready to file internally or share with a data protection officer for review.

## Output Format
A structured compliance note of 350–500 words, organised under five headings: **Data Categories**, **Purpose and Lawful Basis**, **Retention**, **Access and Third-Party Sharing**, and **Risks and Actions Required**. Tone is factual and administrative — suitable for internal records or DPO review. Plain English throughout; technical GDPR terms are used where necessary but always followed by a brief explanation.

## Quality Criteria
- [ ] Correctly identifies all categories of personal data described in the input
- [ ] Flags special category data (Article 9) if present and notes the higher threshold
- [ ] Identifies a specific, plausible lawful basis — not a vague reference to "legitimate interests"
- [ ] Includes concrete retention and access details, even if approximate
- [ ] Flags at least one specific risk or action point relevant to the described content
- [ ] Is written in a form a non-lawyer data protection officer could read and act on

## Example

### Input
I am writing an investigation into a pattern of workplace injury claims at a logistics company. I have interview recordings with six former employees who spoke on the record about their experiences. I also have a spreadsheet of 340 workers compiled from public tribunal records — names, dates of injury, and outcomes. The article will name the six interviewees and refer to the tribunal dataset in aggregate, but will not publish individual rows. I am based in the UK.

### Output

**Data Categories**

This project involves two categories of personal data:

1. **Interview subjects (6 individuals):** Full names, employment history, and health information relating to workplace injuries. Health information is special category data under GDPR Article 9 and carries heightened obligations.
2. **Tribunal dataset (340 individuals):** Full names, dates of injury, and legal outcomes, compiled from publicly available tribunal records. Although sourced from public records, this data remains personal data under UK GDPR and includes health-adjacent information (injury details).

**Purpose and Lawful Basis**

The processing is for journalistic purposes — investigation and publication of a matter of significant public interest (workplace safety accountability).

- **Lawful basis (Article 6):** Substantial public interest (Article 6(1)(e)), applied under the UK GDPR's journalism exemption as enacted in the Data Protection Act 2018, Schedule 2, Part 5.
- **Special category basis (Article 9):** Substantial public interest in journalism (Article 9(2)(g)), subject to the condition that processing is proportionate to the aim and that publication of health data is limited to what is necessary.

The six interview subjects have given informed consent to be named and for their accounts to be published. Consent is documented in signed release forms retained with project files.

**Retention**

- Interview recordings: retained for 24 months post-publication for verification and legal purposes, then securely deleted.
- Signed release forms: retained for 7 years post-publication.
- Tribunal dataset spreadsheet: retained for 24 months post-publication, then deleted. Not published in individual form.

**Access and Third-Party Sharing**

Access is restricted to the lead journalist and the managing editor. The dataset will not be shared with third parties. If the article is fact-checked externally, the checker will be granted read-only access to anonymised extracts only and will be required to sign a confidentiality agreement before access is granted.

**Risks and Actions Required**

- **Special category data:** Health information requires extra care. Publishing the names of interviewees alongside their injury details is proportionate given their consent, but the investigation piece should not reproduce injury details for any of the 340 dataset individuals by name.
- **Right to erasure:** Any interview subject who later withdraws consent may request erasure of their data. Retain a log of consent dates to handle such requests efficiently.
- **Action:** Confirm with your data protection officer that the DPA 2018 Schedule 2 journalism exemption applies before publication. File this note with the project folder.

This note is for internal records only. It is not a substitute for qualified legal or data protection advice.

## Known Limitations
- GDPR implementation varies between EU member states and the UK post-Brexit. This skill reflects UK GDPR as a default; users in other jurisdictions should verify that the lawful basis and exemptions described apply in their country.
- The journalistic exemption is not automatic or unlimited. Whether it applies in a specific case depends on the nature of the content and the proportionality of the data processing. A data protection officer or media lawyer should confirm this before publication.
- This skill cannot assess risks that depend on facts not provided — for example, whether a source's identity is genuinely protected if their account is sufficiently distinctive.
- This skill is not a substitute for qualified legal advice or the review of a registered data protection officer.

## Related Skills
- [copyright-holder-finder](../../media-business/legal/copyright-holder-finder/SKILL.md)
- [creative-commons-explainer](../../media-business/legal/creative-commons-explainer/SKILL.md)
