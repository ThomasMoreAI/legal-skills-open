---
name: prompt-pack-board-resolution-sboghossian
title: Board Resolution
description: Use when drafting board resolutions for a company to approve a specific action — contract signing, officer appointment, dividend declaration, share issuance, or other corporate authority matters. Corporate governance practice area; covers the proper form, recitals, resolved clauses, and authorization language required under MENA and international corporate laws, including the critical distinction between written resolutions and meeting resolutions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-board-resolution
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Board Resolution

## When to use this

Use this skill when drafting a **specific board resolution** to authorize a particular corporate action. This skill focuses on substance — what the resolution must say — for common corporate actions. For a general reusable template, see [[prompt-pack-board-resolution-template]].

Common triggers:
- Signing a material contract (the counterparty or their lawyer requests a resolution authorizing execution)
- Appointing or removing an officer (CEO, CFO, Company Secretary, authorized signatory)
- Declaring a dividend
- Issuing new shares or approving a share buyback
- Opening or closing a bank account
- Approving a budget or capital expenditure above a threshold
- Entering into a related-party transaction
- Approving the annual financial statements

---

## Prompt template

> Draft board resolutions for [Company] to approve [describe matter: contract signing/officer appointment/dividend declaration/share issuance/other]. Include recitals, resolved clauses, authorization of officers to execute, and compliance with articles of association.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Company full legal name | Formal name for the resolution heading |
| Jurisdiction of incorporation | Determines form requirements; quorum; written resolution rules |
| Date of the resolution | Meeting date or written resolution effective date |
| The action being approved | The substance of the resolved clauses |
| Names of directors present/signing | Quorum and signatory requirements |
| Applicable articles of association provisions | Resolution must be consistent with the company's constitutional documents |

---

## Document structure

### 1. Header

```
[COMPANY FULL LEGAL NAME]
([Jurisdiction] [company type, e.g., LLC / SAL / PJSC / LLP])

RESOLUTIONS OF THE BOARD OF DIRECTORS

[Passed at a meeting of the Board of Directors held on [date] at [time] at [address]]
OR
[Passed by written resolution of the Board of Directors dated [date]]
```

### 2. Quorum and attendance (for meeting resolutions)

```
Present:
  [Name], [Director / Chairman / Managing Director]
  [Name], [Director]
  [Name], Independent Director]

Quorum: [X] directors were present, constituting a quorum in accordance with Article [X] of the Articles of Association.

Chairperson: [Name] acted as chairperson of the meeting.

Company Secretary: [Name / "No company secretary was present"]
```

### 3. Recitals

Recitals state the factual background that the board has considered. They are not themselves operative (the RESOLVED clauses are), but they provide context and support the validity of the resolution.

Standard recitals:
```
WHEREAS:
(A) The Company was incorporated in [jurisdiction] on [date] under registration number [X].
(B) The Articles of Association of the Company permit the Board to [describe the power being exercised].
(C) [Specific factual context: e.g., "The Company has been presented with a term sheet from [Investor] for a Series A investment of USD [X]..." or "The Board has reviewed the proposed [agreement] with [counterparty]..."]
(D) The Board has considered the matter and determined that the proposed action is in the best interests of the Company.
```

### 4. Resolved clauses

The resolved clauses are the operative part. Use "IT IS HEREBY RESOLVED" in capitals; start each resolution with "RESOLVED THAT" or "FURTHER RESOLVED THAT" for subsequent resolutions. Be specific — vague authority creates legal exposure.

#### 4.1 Contract signing resolution
```
RESOLVED THAT the Company enter into and execute the [name/type of agreement] dated on or about [date] with [counterparty] (the "Agreement"), a copy of which is appended hereto as Exhibit A.

FURTHER RESOLVED THAT [Name], [Title], is hereby authorized, on behalf of the Company, to execute and deliver the Agreement and all related documents and to do all acts and things necessary or desirable to give effect to the foregoing resolution.

FURTHER RESOLVED THAT any one authorized signatory is sufficient / two authorized signatories are required to execute the Agreement [choose per the articles of association].
```

#### 4.2 Officer appointment resolution
```
RESOLVED THAT [Full name] (Passport/ID No. [X]) be and is hereby appointed as [Chief Executive Officer / Chief Financial Officer / Authorized Signatory] of the Company with effect from [date].

FURTHER RESOLVED THAT [Name] is authorized to [describe scope of authority — enter into contracts up to USD X; represent the Company before government authorities; sign cheques up to AED X — be specific].

FURTHER RESOLVED THAT the Company Secretary / HR Manager is authorized to take all steps necessary to register this appointment with [Ministry of Economy / DIFC CR / ADGM Register / other relevant authority].
```

#### 4.3 Dividend declaration
```
RESOLVED THAT the Board hereby declares a [interim / final] dividend of [currency] [X] per [ordinary / class A] share, amounting to a total dividend of [currency] [total amount], in respect of [period].

FURTHER RESOLVED THAT the dividend shall be payable on [payment date] to shareholders of record as of [record date].

FURTHER RESOLVED THAT [Name], [CFO / Finance Manager], is authorized to effect payment of the dividend in accordance with this resolution.
```

**Note on dividends**: in many MENA civil-law jurisdictions (Lebanon, UAE, Egypt), dividends can only be declared if the company has distributable profits and the legal reserve requirement has been met. Include a recital confirming this where required.

#### 4.4 Share issuance resolution
```
RESOLVED THAT [Number] [ordinary / preference] shares of [par value / no par value] in the capital of the Company are hereby issued and allotted to [Name / Entity] at a price of [currency] [X] per share, for a total consideration of [currency] [total].

FURTHER RESOLVED THAT the share register of the Company be updated to reflect the foregoing issuance.

FURTHER RESOLVED THAT [Name] is authorized to execute and deliver to [investor] a share certificate for the issued shares.

FURTHER RESOLVED THAT, to the extent required by law or the Articles of Association, the approval of the shareholders for this issuance shall be sought at the next [extraordinary] general meeting.
```

**Warning**: in most MENA jurisdictions, the board alone cannot issue new shares without prior shareholder authorization (unless the articles expressly grant this authority up to a stated limit). Verify the articles before drafting.

#### 4.5 Bank account resolution
```
RESOLVED THAT the Company open a [current / savings / USD] bank account with [Bank Name] at its [Branch] branch.

FURTHER RESOLVED THAT the following persons are authorized to operate the account [individually / jointly]:
  - [Name], [Title] — signatory authority: up to [currency] [X] individually; above that amount requires joint signature with any other authorized signatory
  - [Name], [Title] — signatory authority: up to [currency] [X]

FURTHER RESOLVED THAT [Name] is authorized to execute all bank mandate forms and other documentation required by [Bank Name] to open and maintain the account.

FURTHER RESOLVED THAT a certified copy of this resolution may be provided to [Bank Name] as evidence of the foregoing authority.
```

### 5. Certification

The resolution is typically signed by the chairperson of the meeting or by all directors (for written resolutions):

**Meeting resolution:**
```
Signed by the Chairman of the meeting in accordance with the Articles of Association.

_________________________
[Chairperson name], Chairman
Dated: [date]
```

**Written resolution:**
```
We, the undersigned, being all of the directors of [Company], hereby pass the foregoing resolutions by written resolution in lieu of a meeting, in accordance with [Article X of the Articles of Association / Companies Law s. X].

[Director 1 name] _________________________ Date: _______
[Director 2 name] _________________________ Date: _______
[Director 3 name] _________________________ Date: _______
```

---

## Jurisdictional notes

### UAE (mainland companies — LLC and PJSC)
- Resolutions for LLCs: UAE Commercial Companies Law Federal Decree-Law 32/2021 requires board meetings to have a quorum of at least half the members; majority of those present for ordinary decisions; specific percentages for major decisions (check the articles)
- Notarization: board resolutions authorizing real estate transactions, government submissions, or banking mandates often require notarization before the UAE Notary Public
- Arabic: board resolutions for submission to UAE government authorities (Ministry of Economy, courts, land department) must be in Arabic or accompanied by a certified Arabic translation

### DIFC
- DIFC Companies Law: board meetings require notice per the articles; quorum per the articles (usually majority)
- Written resolutions: permitted by DIFC Companies Law if authorized by the articles
- DIFC CR: director appointments must be notified to the DIFC Companies Registrar

### KSA (closed joint-stock companies and LLCs)
- Shareholder approval required for many decisions that boards in other jurisdictions can make independently (significant contracts, related-party transactions)
- Resolutions must be in Arabic; notarization may be required

### Lebanon (SAL and SARL)
- Board resolutions for SAL (Société Anonyme Libanaise): quorum and majority per the commercial code and articles
- Lebanese courts sometimes require resolutions to bear the company's official stamp (cachet)
- Notarization required for real estate and government matters

### Egypt
- Board resolutions should be in Arabic (official language for all legal documents)
- Companies Law No. 159/1981 (for stock companies) and Law No. 116/1983 (for LLCs) govern resolution procedures

---

## Common mistakes

- Resolved clauses too vague ("authorized to do everything necessary") — counterparties and registries want specific authorization
- No exhibit attached for the agreement being approved (the resolution says "a copy of which is appended" — attach it)
- Wrong signatory authority — board resolution says "any one director" but articles require two
- Dividend resolution without confirming distributable profits exist
- Share issuance without checking whether board has the power to issue shares without shareholder approval

---

## Related skills

- [[prompt-pack-board-resolution-template]] — a reusable blank template for any action
- [[prompt-pack-board-committee-charter]] — committee charter adopted by board resolution
- [[prompt-pack-annual-report-governance-section]] — annual governance disclosure of board activity
- [[kb-corporate-governance-mena]] — MENA corporate governance and companies law reference
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction determines form and notarization requirements
