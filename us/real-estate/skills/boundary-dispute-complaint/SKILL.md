---
name: boundary-dispute-complaint
title: Boundary Dispute Complaint
description: Drafts a U.S. state-court complaint to establish the true boundary line between adjoining properties, with optional trespass/encroachment claims. Trigger when a user needs to initiate litigation over conflicting property descriptions, ambiguous deed language, or unauthorized encroachments by an adjoining landowner.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/boundary-dispute-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [drafting, litigation, pleading]
---

# Boundary Dispute Complaint

Drafts a plaintiff-side complaint to judicially establish the true boundary line between adjoining parcels, with optional trespass/encroachment counts.

## Prerequisites

Collect before drafting:

- **Plaintiff's deed** — legal description (metes-and-bounds, lot/block, or recorded plat)
- **Defendant's deed** — adjoining parcel legal description
- **Survey** — surveyor name, date, methodology, findings, recording info
- **Encroachment details** — type, dimensions, date discovered (if applicable)
- **Jurisdiction** — state and county where the property sits
- **Pre-suit notice** — whether defendant was notified before filing

## Quick Start

1. Gather deeds, survey, and encroachment facts.
2. Identify the filing court, venue basis, and applicable quiet-title statute.
3. Draft per the structure below.
4. Flag all `[VERIFY]` items for attorney review.

## Complaint Structure

### Caption

Court name, case-number placeholder, full legal names of all parties. Follow local formatting rules.

### Parties & Jurisdiction

| Element | Allegation |
|---|---|
| Subject-matter jurisdiction | Real property dispute; amount in controversy if threshold required |
| Personal jurisdiction | Defendant's contacts with forum state |
| Venue | Property located in [County], [State] |

### Factual Allegations (Numbered Paragraphs)

1. **Plaintiff's property** — full legal description per deed/survey; recording info
2. **Defendant's property** — legal description; recording info; relationship to plaintiff's parcel
3. **Boundary dispute** — how positions differ; reference deeds, conveyances, surveys, physical markers
4. **Survey findings** — surveyor's conclusion on true boundary; methodology
5. **Discrepancies** — conflicting deed language, ambiguous conveyances, inconsistent prior surveys
6. **Encroachment** *(if applicable)* — structure type, dimensions, extent of intrusion, date discovered, notice given

### Counts

**Count I — Quiet Title to Boundary Line**

- Judicial determination and declaration of the true boundary
- Cite applicable state quiet-title statute `[VERIFY statute]`
- Incorporate deed-interpretation principles, survey evidence, boundary-determination standards

**Count II — Trespass** *(if encroachment present)*

- Defendant's placement/maintenance of improvements on plaintiff's land as ongoing trespass
- Damages: diminution in value, loss of use/enjoyment, remediation costs
- Relief: compensatory damages + mandatory injunction for removal

### Prayer for Relief

1. Declaratory judgment establishing the true boundary line
2. Order requiring defendant to recognize the judicially determined boundary
3. Mandatory injunction requiring removal of encroachments *(if applicable)*
4. Compensatory damages for trespass *(if applicable)*
5. Costs and attorney's fees `[VERIFY statutory basis]`
6. Such other relief as the court deems just

### Exhibits

- **A** — Plaintiff's deed
- **B** — Survey/plat
- **C** — Photographs of encroachment *(if applicable)*

## Pitfalls & Checks

- Reproduce all legal descriptions **verbatim** from source documents.
- Quiet title often requires joinder of all interest holders (lienholders, prior owners) — `[VERIFY per state rules]`.
- Some states require a **lis pendens** filed concurrently — flag for review.
- Use numbered paragraphs; keep tone factual; avoid conclusory allegations unsupported by facts (12(b)(6) survival).
