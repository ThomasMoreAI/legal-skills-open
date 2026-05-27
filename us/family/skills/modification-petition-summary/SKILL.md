---
name: modification-petition-summary
title: Modification Petition Summary
description: Produces structured summaries of U.S. family law modification petitions for attorney review. Captures existing order terms, requested changes, alleged material change in circumstances, supporting facts, evidence inventory, and procedural posture. Use when summarizing petitions to modify custody, visitation, child support, spousal support, or other post-judgment orders.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/modification-petition-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Modification Petition Summary

Condense a family law modification petition into a decision-ready, neutral summary using the template below.

## Quick Start

Gather before summarizing:

- [ ] Modification petition and referenced exhibits
- [ ] Current order/judgment (or its date and terms)
- [ ] Docket metadata (court, case number, filing date)
- [ ] Jurisdiction/state and party roles
- [ ] Cited statutes/case law from the petition

## Output Template

Fill all fields present in the petition. Mark missing items "Not provided".

### Case Snapshot

| Field | Details |
| --- | --- |
| Court / County | |
| Case No. | |
| Parties | |
| Petitioner / Respondent | |
| Filing Date | |
| Order at Issue (type/date) | |
| Requested Hearing Date | |
| Emergency/Temporary Relief Sought | Yes/No; details |

### Order Comparison

| Topic | Current Order | Requested Modification |
| --- | --- | --- |
| Custody (legal/physical) | | |
| Parenting time / visitation | | |
| Child support | | |
| Spousal support | | |
| Other provisions | | |

### Grounds for Modification

- Material change in circumstances alleged: Yes/No
- Nature of change: relocation, income change, child needs, health, safety, cohabitation/remarriage, school issues, other
- Best interests factors invoked: Yes/No; specify
- Statutory standard cited: Yes/No; cite if provided
- Retroactive modification requested: Yes/No; scope

### Factual Allegations

Bulleted chronology:

- Date/period: event/fact alleged
- Link to requested change: how petitioner connects fact to relief
- Allegations of noncompliance with prior order

### Evidence Inventory

| Evidence Type | Attached? | Description / Purpose |
| --- | --- | --- |
| Financial declaration | | |
| Party declaration(s) | | |
| Witness declaration(s) | | |
| Expert report(s) | | |
| School records | | |
| Medical records | | |
| Other exhibits | | |

### Legal Framework

- Statutes cited
- Case law cited
- Local rules/procedural standards cited

### Procedural Posture

| Item | Details |
| --- | --- |
| Service/Notice described | |
| Prior modification history | |
| Related proceedings (contempt, enforcement, DV) | |
| Requested fees/costs | |
| Mediation/ADR requested or required | |

### Relief Requested

- Primary modification(s)
- Temporary/emergency orders
- Ancillary relief (fees, costs, transportation, exchanges, supervised visits, etc.)

### Gaps / Flags

- Missing: current order text/date, financial data, parenting plan, jurisdiction facts, service info
- Jurisdiction/venue issue: flag if facts suggest multi-state custody or relocation
- Procedural defect: missing verification, required forms, untimely filing, lack of notice

## Pitfalls

- **Neutral tone only** — do not argue merits or recharacterize allegations.
- **Mirror petition terminology** — preserve the petitioner's language for accuracy.
- **Attached vs. referenced** — distinguish evidence actually attached from documents merely cited.
- **No inferred standards** — jurisdiction-specific rules vary by state; only state what the petition states.
- **Unverifiable citations** — tag with `[VERIFY]` if you cannot confirm a legal citation.
