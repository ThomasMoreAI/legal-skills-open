---
name: written-consent
title: Written Consent in Lieu of Meeting
description: Drafts Written Consents in Lieu of Meeting for corporate boards or shareholders. Ensures compliance with state corporate law (e.g., DGCL §§141(f), 228), bylaws, and governing documents. Use when drafting board consent, shareholder consent, unanimous written consent, action by written consent, or consent in lieu of meeting.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/written-consent
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Written Consent in Lieu of Meeting

Drafts a legally sufficient written consent enabling directors or shareholders to take formal corporate action without a meeting.

## Prerequisites

Gather before drafting:

1. **Entity** — full legal name, jurisdiction, entity type (corporation, LLC)
2. **Governing documents** — bylaws or operating agreement (consent-procedure provisions, thresholds, notice/waiting periods)
3. **Consent type** — board vs. shareholder
4. **Signatories** — directors (board) or shareholders with share counts, classes, and ownership percentages
5. **Proposed actions** — specific resolutions; attach supporting transaction documents
6. **Authorizing statute** — e.g., DGCL §141(f) (board), §228 (shareholders)

Extract information from uploaded organizational documents, prior minutes, bylaws, cap tables, and stock ledgers before asking the user.

## Document Structure

1. **Title** — `WRITTEN CONSENT OF THE [BOARD OF DIRECTORS/SHAREHOLDERS] OF [ENTITY NAME] IN LIEU OF [ANNUAL/SPECIAL] MEETING`
2. **Preamble** — cite statutory authority (code, section, subsection); reference bylaws/OA; state unanimous vs. majority; specify effective date
3. **Recitals** — WHEREAS clauses: identify signatories by name/title/shares; state factual background, business rationale, conditions precedent, conflicts of interest
4. **Resolutions** — numbered, each beginning `RESOLVED,` (see resolution rules below)
5. **Execution clause** — counterparts permitted; electronic signature authorization (cite E-SIGN Act if applicable); filing directive to secretary
6. **Signature blocks** — Board: name + "Director" + date. Shareholders: name + shares (number, class, % outstanding) + date
7. **Secretary's certificate** — attestation of due execution, filing with corporate records, continued effect

## Resolution Rules by Type

- **Contracts/transactions** — identify counterparty by full legal name; all material terms and amounts; attach agreement as numbered exhibit (not "substantially the form presented"); specify officer authority scope for changes
- **Officer authorizations** — name officers; document categories; monetary limits; individual vs. joint authority; time/transaction limitations
- **Equity issuances** — exact number, class/series, price/valuation method, recipient, vesting/transfer restrictions, consideration form, securities law compliance, preemptive rights clearance
- **Governing document amendments** — full amendment text or exhibit with incorporation by reference; identify exact section amended; confirm supermajority/procedural compliance
- **Financial transactions** — maximum principal, material terms (rate, maturity), collateral/security interests, lender identity, delegation parameters

## Consent Threshold Reference

| Jurisdiction | Board | Shareholder |
|---|---|---|
| Delaware (DGCL) | Unanimous — §141(f) | Majority of voting power — §228 (unless charter requires more) |
| MBCA states | Unanimous — §8.21 | Unanimous — §7.04 (unless articles authorize less) |
| Delaware LLC Act | Per operating agreement — §18-404 | Per operating agreement — §18-302 |

Always verify the entity's charter/bylaws for stricter-than-statutory requirements.

## Pitfalls and Checks

- **Effective date** — some jurisdictions tie effectiveness to the last required signature; others to filing. State explicitly in the preamble
- **Fundamental actions** (mergers, dissolution, charter amendments) may require unanimous consent even where majority is otherwise permitted — verify per jurisdiction
- **Related-party transactions** — include recitals confirming disinterested-director approval, independent valuation, or other conflict-clearance procedures
- **Downstream obligations** — flag disclosure obligations (securities laws, exchange rules), regulatory filings, or third-party consents triggered by the approved actions
- **Defined terms** — capitalize consistently; define at first use or in a definitions section for complex consents
- **Cross-references** — verify all internal cross-references and exhibit numbering before finalizing
- **Missing information** — surface gaps to the user rather than guessing; the consent must be legally sufficient, not merely formally complete
