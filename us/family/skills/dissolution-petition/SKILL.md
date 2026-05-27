---
name: dissolution-petition
title: Petition for Dissolution of Marriage
description: Drafts a Petition for Dissolution of Marriage for filing in US state family courts. Covers jurisdictional standing, grounds, child custody and support, property and debt division, spousal support, and prayer for relief. Use when preparing initial divorce petitions, dissolution pleadings, or family law filing documents.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/dissolution-petition
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
tags: [drafting, litigation, pleading]
---

# Petition for Dissolution of Marriage

Drafts a jurisdiction-compliant petition initiating divorce proceedings with all required allegations and relief requests.

## Prerequisites

1. **Jurisdiction identified** — state, county, confirmed residency period met
2. **Party information** — full legal names, DOBs, addresses, marriage date, separation date
3. **Children** — names, DOBs, current living arrangements (if applicable)
4. **Asset/debt summary** — real property, accounts, business interests, major debts
5. **Client objectives** — custody preferences, support requests, property division goals
6. **Local court rules** — formatting, mandatory forms, concurrent filing requirements

## Quick Start

1. Confirm residency satisfies statutory minimum; cite statute by number
2. Draft caption per local rules with court name, party names, case number placeholder
3. Allege grounds using exact statutory language for the filing jurisdiction
4. Address each applicable relief category (custody, support, property, debts)
5. Close with prayer for relief — every prayer item must correspond to a petition allegation
6. Add verification under penalty of perjury with proper signature blocks

## Output Structure

### Caption and Header

| Element | Requirements |
|---|---|
| Court | Full court name with jurisdiction (e.g., "Superior Court of California, County of Los Angeles") |
| Case number | `Case No. ___________` |
| Parties | Petitioner and Respondent, full legal names |
| Document title | "PETITION FOR DISSOLUTION OF MARRIAGE" |

Format caption per local rules — verify margins, font, line spacing, line numbering.

### Jurisdictional Allegations

- [ ] State residency — duration and dates satisfying statutory minimum
- [ ] County residency (if required)
- [ ] Venue basis
- [ ] Waiting period compliance (if applicable)
- [ ] Subject matter jurisdiction statement

Residency periods vary widely (6 weeks in Nevada to 1 year in some states). Cite exact statute number. Mark with `[VERIFY]` unless confirmed.

### Party Identification and Marital History

- Full legal names (including maiden/former names)
- Current addresses (or note if confidential per protective order)
- Date and place of marriage
- Date of separation
- Date marriage became irretrievably broken (if jurisdiction requires)

### Grounds for Dissolution

No-fault standard language:

> "The marriage is irretrievably broken due to irreconcilable differences, with no reasonable prospect of reconciliation."

- Use exact statutory language — "irretrievable breakdown," "incompatibility," or "insupportability" varies by state
- Cite specific statute number
- Omit fault allegations unless required by jurisdiction or relevant to custody/property

### Children of the Marriage

For each minor child: full legal name, DOB, age, relationship (biological/adopted).

Custody and support requests:
- [ ] Legal custody — sole or joint
- [ ] Physical custody — sole or joint
- [ ] Parenting time schedule proposal
- [ ] Child support per state guidelines
- [ ] Decision-making authority (education, health, religion)
- [ ] Special circumstances (special needs, safety concerns)

Check if jurisdiction requires concurrent filing of parenting plan, child support worksheet, or UCCJEA declaration.

### Property, Assets, and Debts

Categorize as marital/separate or community/separate per jurisdiction:

| Category | Examples |
|---|---|
| Real property | Primary residence, investment properties |
| Financial | Bank accounts, retirement (401k, IRA, pension), investments |
| Business | Ownership interests, professional practices |
| Titled property | Vehicles, boats |
| Personal property | Items of significant value |

**Debts:** Mortgages, credit cards, student loans, other obligations.

- [ ] Identify property characterization framework (community property vs. equitable distribution)
- [ ] Propose division consistent with applicable standard

### Spousal Support

Request type (select as applicable):
- [ ] Temporary — during pendency
- [ ] Rehabilitative — limited duration
- [ ] Long-term / permanent
- [ ] Waiver — each party self-supporting
- [ ] Reserve jurisdiction — decide later

Reference statutory factors: length of marriage, income and earning capacity, standard of living, age/health/employability, contributions including homemaking. Cite jurisdiction's spousal support statute; note if state uses formula-based calculation.

### Prayer for Relief

```
WHEREFORE, Petitioner prays for judgment as follows:

1. Dissolution of the marriage between Petitioner and Respondent;
2. [Custody arrangement] of the minor child(ren);
3. Child support pursuant to [state] guidelines;
4. Division of community/marital property and debts as set forth herein;
5. [Spousal support request or denial];
6. Attorney's fees and costs of suit;
7. Such other and further relief as the Court deems just and proper.
```

Every prayer item must correspond to an allegation in the petition body.

### Verification and Signature

- [ ] Verification under penalty of perjury (check if notarization required)
- [ ] Petitioner signature block with name, signature line, date
- [ ] Attorney signature block (if represented)
- [ ] Notary acknowledgment (if jurisdiction requires)

## Guidelines

- **Verify local rules before drafting** — caption format, mandatory cover sheets, concurrent filings (summons, UCCJEA declarations, financial disclosures) vary by jurisdiction
- **Use exact statutory language** for grounds — paraphrasing risks demurrer
- **Omit inflammatory allegations** unless legally required — petition is a public record
- **Never include full financial account numbers** — use last four digits or descriptions only
- **Check confidentiality rules** — many jurisdictions restrict disclosure of children's information or addresses in domestic violence cases
- **Flag missing information** with `[TO BE PROVIDED]` rather than fabricating details
- **Mark uncertain statutory citations** with `[VERIFY]`

## Troubleshooting

- **Residency period unclear** — check both state and county requirements; some states impose separate durational thresholds for each. When in doubt, allege both and mark `[VERIFY]`
- **No-fault language rejected** — confirm the state's exact statutory phrasing; some jurisdictions require specific terminology (e.g., "insupportability" in Texas)
- **Concurrent filing requirements missed** — review local rules for mandatory companion filings (summons, financial declarations, parenting plans) before submission
- **Confidential address needed** — check if the jurisdiction offers an address confidentiality program or allows filing under seal for DV cases
