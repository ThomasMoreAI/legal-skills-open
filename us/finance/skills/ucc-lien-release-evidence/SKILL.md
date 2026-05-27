---
name: ucc-lien-release-evidence
title: Evidence of UCC Lien Release
description: 'Drafts an Evidence of UCC Lien Release documenting termination of a UCC-1 financing statement for U.S. transactional closings. Trigger when the user needs a UCC-3 termination certificate, secured-party release letter, payoff evidence, or clear-title closing deliverable. Keywords: "UCC-1", "UCC-3 termination", "lien release", "secured party release", "clear title", "payoff letter".'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ucc-lien-release-evidence
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, drafting, transactional]
---

# Evidence of UCC Lien Release

Produces a formal certificate or letter evidencing full or partial release of a UCC-1 lien, suitable for closing binders and due-diligence packages.

## Quick Start

Gather before drafting:

1. UCC-1 details — file number, filing date, filing office, jurisdiction
2. Debtor and secured party legal names and addresses (as filed)
3. Collateral description from UCC-1 (and any amendments)
4. Security agreement date and governing documents
5. Satisfaction evidence — payoff statement, wire confirmation, release letter, settlement, or order
6. UCC-3 termination details if filed — file number, date, stamped copy
7. Release scope (full or partial) and effective date
8. Any continuation, assignment, or amendment filings on the same collateral

## Workflow

### 1. Build Source Data Table

| Field | Req | Source | Notes |
|---|---|---|---|
| Debtor legal name | Yes | UCC-1 | Exact spelling, punctuation, entity suffix |
| Secured party legal name | Yes | UCC-1 | Exact spelling, punctuation, entity suffix |
| Filing office + jurisdiction | Yes | UCC-1 | Secretary of State or equivalent |
| UCC-1 file number | Yes | UCC-1 | Include filing date |
| Collateral description | Yes | UCC-1 | Mirror verbatim |
| Security agreement date | Yes | Agreement | Identify governing document |
| Release scope | Yes | Instructions | Full vs partial; list retained collateral |
| Effective date | Yes | Instructions | Execution or payoff date |
| UCC-3 termination file no. | If filed | UCC-3 | Include date and stamped copy |
| Satisfaction evidence | Yes | Payoff/letters | Cite exhibit numbers |

Resolve any inconsistencies (name mismatches, collateral gaps) before proceeding.

### 2. Build Filing Chronology (if multiple filings)

| Filing No. | Type | Filing Office | Filing Date | Purpose |
|---|---|---|---|---|
| | UCC-1 | | | Original financing statement |
| | UCC-3 | | | Amendment / continuation / assignment / termination |

### 3. Draft Document

**Required sections:**

| Section | Content | Notes |
|---|---|---|
| Title + Date | "Evidence of UCC Lien Release"; document date | Exact title |
| Parties | Debtor and secured party details | Match UCC-1 |
| Filing Identification | File number, office, date | All jurisdictions |
| Secured Transaction Summary | Agreement date, obligation, collateral | Track UCC-1 text |
| Release Statement | Full/partial release; satisfaction; no further claims | Unambiguous language |
| Termination Status | UCC-3 details or intent to file | Never imply filed if not filed |
| Effective Date | Specific date | Tie to payoff or execution |
| Exhibits | List supporting documents | Labeled exhibits |
| Execution | Authorized signatory + title | Notarization if required |

### 4. Assemble Exhibits

- [ ] UCC-1 financing statement (file-stamped)
- [ ] UCC-3 termination (file-stamped if available)
- [ ] Payoff letter or satisfaction evidence
- [ ] Security agreement (if cited)
- [ ] Order/settlement (if release from legal proceeding)

Verify all exhibit cross-references in the document body.

## Template

```text
EVIDENCE OF UCC LIEN RELEASE

Date: {Document Date}

1. Parties
Secured Party: {Legal Name}, {Entity Type}, {Jurisdiction of Organization}
Address: {Address}
Debtor: {Legal Name}, {Entity Type}, {Jurisdiction of Organization}
Address: {Address}

2. Financing Statement Identification
UCC-1 File Number: {File Number}
Filing Office/Jurisdiction: {Filing Office, State}
Filing Date: {Filing Date}
Additional Filings (if any): {List UCC-3 amendments/continuations/assignments}

3. Secured Transaction Summary
Security Agreement Date: {Date}
Obligation: {Brief description of secured obligations}
Collateral: {Collateral description mirroring UCC-1}

4. Release and Termination
The Secured Party hereby releases, terminates, and fully discharges all security interests,
liens, and claims in the collateral described above arising under the UCC-1 financing
statement identified in Section 2. All secured obligations have been satisfied in full, and
the Secured Party asserts no further interest in the collateral or proceeds.

5. Termination Filing
{If filed} A UCC-3 Termination Statement has been filed under File No. {UCC-3 No.} on {Date}.
{If not filed} The Secured Party will file a UCC-3 Termination Statement with the filing office
identified above.

6. Effective Date
This release is effective as of {Effective Date}.

7. Exhibits
Exhibit A: UCC-1 Financing Statement
Exhibit B: UCC-3 Termination Statement (file-stamped, if available)
Exhibit C: Payoff/Release Evidence {wire confirmation / payoff letter / order}

Secured Party:

By: ___________________________
Name: {Signatory Name}
Title: {Title}
Date: {Signature Date}

{Optional Notary Acknowledgment}
```

## Pitfalls

- **Name matching** — Debtor and secured party names must exactly match the UCC-1; flag any discrepancy for confirmation.
- **Collateral scope** — Mirror the UCC-1 collateral description verbatim; paraphrasing can narrow or expand scope.
- **Partial releases** — Explicitly list released collateral and expressly preserve remaining liens.
- **UCC-3 status** — Never state a UCC-3 was filed without the file number and date.
- **Filing office terminology** — Use consistent format: "Secretary of State, {State}".
- **Notarization** — Add only if required by jurisdiction or client request.
- **Uncertain citations** — Mark with `[VERIFY]`.
- **Tone** — Keep neutral and evidentiary; no advocacy or legal conclusions.
