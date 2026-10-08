---
name: prompt-pack-board-resolution-template-sboghossian
title: Board Resolution Template
description: Use when generating a reusable board resolution template for any approval, appointment, or policy change, with fill-in fields for company name, action, authorized signatories, and jurisdiction-specific signature blocks. Corporate governance practice area; this is the blank-template companion to the substantive board-resolution skill — useful when the user needs a clean structural template to adapt for a recurring use case.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-board-resolution-template
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Board Resolution Template

## When to use this

Use this skill when the user needs a **reusable, blank-form board resolution template** that can be adapted for any corporate action. This complements [[prompt-pack-board-resolution]] (which drafts a substantive resolution for a specific action). Use this skill when:
- Setting up a template for a law firm's or company's corporate secretarial library
- Creating a standard internal template for recurring corporate actions (e.g., monthly account authorizations, regular contract signings)
- Onboarding a client who needs a starting-point template to use repeatedly
- The user wants a clean structural form, not a completed resolution

---

## Prompt template

> Draft a board resolution for [approval of transaction/appointment/policy change]. Include recitals, resolved clauses, authorization details, and signature blocks per [jurisdiction] corporate law requirements.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs — particularly the jurisdiction and the recurring action type.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Jurisdiction | Determines signature block format, quorum requirements, language requirements, notarization notes |
| Company type | LLC, PJSC, SAL, SARL, LTD — affects the form of resolution |
| Action category | Contracts, appointments, financial, governance — sets which resolved clause blocks to include |
| Signatory approach | One director / two directors / all directors (depends on articles and action type) |

---

## Master template

The following is the full master template. Customize per the action and jurisdiction. Replace all `[BRACKETED]` fields before use.

---

```
[COMPANY FULL LEGAL NAME]
[Company type — e.g., Limited Liability Company / Société Anonyme Libanaise / Private Joint Stock Company]
[Jurisdiction of Incorporation]
[Commercial Registration / Trade License Number: XXXXXXX]

─────────────────────────────────────────────────────────
RESOLUTIONS OF THE BOARD OF DIRECTORS
─────────────────────────────────────────────────────────

[OPTION A — MEETING RESOLUTION]
Resolutions adopted at a duly convened meeting of the Board of Directors of the Company
held on [DATE] at [TIME] at [MEETING LOCATION / via video conference]

[OPTION B — WRITTEN RESOLUTION IN LIEU OF MEETING]
Resolutions adopted by written resolution of the Board of Directors of the Company
in lieu of a meeting, effective as of [DATE], pursuant to [Article X of the Articles of
Association / Section X of the Companies Law]

─────────────────────────────────────────────────────────
DIRECTORS PRESENT / SIGNING
─────────────────────────────────────────────────────────

[For meeting:] Present at the meeting:
  1. [Full Name]          — [Chairman / Director / Managing Director]
  2. [Full Name]          — [Director / Independent Director]
  3. [Full Name]          — [Director]

[Confirm quorum]: [X] directors were present, constituting a quorum pursuant to
Article [X] of the Articles of Association. [The meeting was duly convened with
[X] days' notice to all directors.]

[For written resolution:] The undersigned, being all [a majority / the required
number of] directors of the Company, hereby pass the following resolutions by way of
written resolution in lieu of a meeting.

─────────────────────────────────────────────────────────
RECITALS
─────────────────────────────────────────────────────────

WHEREAS:

(A)  The Company was incorporated in [jurisdiction] on [date] and is registered under
     commercial registration / trade license number [X].

(B)  The Articles of Association of the Company empower the Board of Directors to
     [DESCRIBE THE BOARD POWER BEING EXERCISED — e.g., "approve the entering into of
     agreements on behalf of the Company"; "appoint officers and authorized signatories";
     "declare interim dividends"].

(C)  [FACTUAL CONTEXT — describe what is being approved in plain terms, e.g.:
     "The Company has been presented with a [type] agreement with [counterparty] and
     has reviewed the terms thereof."]

(D)  The Board has considered the matter and is satisfied that the proposed action is
     in the best interests of the Company and its shareholders.

─────────────────────────────────────────────────────────
RESOLUTIONS
─────────────────────────────────────────────────────────

NOW, THEREFORE, BE IT RESOLVED as follows:

RESOLVED THAT
[PRIMARY RESOLUTION — state the action being approved with precision]
[e.g., "the Company enter into and execute the [agreement name] dated on or about
[date] with [counterparty], a copy of which is attached hereto as Exhibit A"]
[e.g., "the Company appoint [Full Name], [ID/Passport No.], as [Title] with effect
from [date], with the authority described in the attached schedule"]
[e.g., "the Company declare an interim dividend of [currency] [X] per [ordinary/class]
share for the period ended [date], payable on [payment date] to shareholders of record
as of [record date]"]

FURTHER RESOLVED THAT
[AUTHORIZATION CLAUSE — who is authorized to implement the resolution]
[Full Name], [Title], is hereby authorized, for and on behalf of the Company, to:
(a) execute and deliver [the Agreement / appointment documents / all relevant documents];
(b) do all acts and things, and execute all documents, as may be necessary or
    desirable to give full effect to the foregoing resolution; and
(c) [any other specific authority — e.g., "make all filings with the relevant
    regulatory authorities"].

[ADDITIONAL RESOLVED CLAUSES AS NEEDED]

FURTHER RESOLVED THAT
A certified copy of these resolutions may be provided to [counterparty / bank /
regulatory authority] as evidence of the foregoing authority.

─────────────────────────────────────────────────────────
CERTIFICATION / SIGNATURES
─────────────────────────────────────────────────────────

[OPTION A — MEETING RESOLUTION — signed by Chairman]

Certified as a true extract of the minutes of the meeting held on [DATE].

_________________________________          Date: ______________
[CHAIRMAN NAME], Chairman of the Meeting

[OPTION B — WRITTEN RESOLUTION — signed by all participating directors]

We, the undersigned directors of [COMPANY NAME], hereby adopt the foregoing
resolutions by written resolution effective as of [DATE].

_________________________________          Date: ______________
[DIRECTOR 1 NAME], Director

_________________________________          Date: ______________
[DIRECTOR 2 NAME], Director

_________________________________          Date: ______________
[DIRECTOR 3 NAME], Director

─────────────────────────────────────────────────────────
[NOTARIZATION BLOCK — add where required by jurisdiction or counterparty]

Sworn before me, the Notary Public, on [date]:
_________________________________
[Notary Public Name and stamp]
─────────────────────────────────────────────────────────

EXHIBIT A: [Attach the approved document or relevant schedule]
```

---

## How to adapt the template

### Action-specific customization
| Action | Key resolved clause content | Special notes |
|--------|----------------------------|--------------|
| Contract signing | Approval of specific agreement; authority to execute | Attach the agreement as an exhibit |
| Officer appointment | Name, ID, title, scope of authority | Specify limits on authority; register with relevant authority |
| Dividend | Amount per share, record date, payment date | Confirm distributable profits in recital |
| Share issuance | Number, class, price, allottee | Confirm pre-emption rights waived or not applicable |
| Bank account | Bank name, branch, signatories, signing limits | Banks often require their own form — attach this resolution to the bank's form |
| Budget/capex approval | Description of budget/project, amount, approving officer | Set threshold above which further board approval is required |
| Related-party transaction | Full description of transaction and party relationship | Additional approval process per corporate governance code |

### Jurisdiction-specific notes

**UAE (onshore — Ministry of Economy or free zone)**
- Resolutions submitted to government authorities must be in Arabic or with a certified Arabic translation
- Notarization: required for real estate transactions, court submissions, and some government filings; UAE Notary Public or DIFC/ADGM Notary
- DIFC and ADGM: resolutions in English are accepted; DIFC Companies Registrar filings use English forms
- LLCs: resolutions are often called "manager's resolutions" not board resolutions (in single-manager LLCs)

**KSA**
- All resolutions must be in Arabic
- Ministry of Justice notarization required for many submissions
- Closed joint-stock companies: board quorum and majority requirements in the Companies Law (Royal Decree M/3/2022 new Companies Law)

**Lebanon**
- Resolutions in French or Arabic (both official); Arabic required for government submissions
- Official company stamp (cachet) often expected by Lebanese authorities and banks
- SAL board: quorum and majority per the Commercial Code (Code de commerce du Liban)

**Egypt**
- Arabic required; Ministry of Justice notarization for real estate and government submissions
- Companies Law 159/1981: joint stock company board procedures

---

## Common mistakes

- Recitals not aligned with the company's actual articles — check the articles before using any standard form
- Authorization clause too broad ("do everything necessary") — specify what the authorized person can actually do
- No exhibit attached when the resolution refers to one
- Template used without updating the company type, jurisdiction, and officer names
- Written resolution used in a jurisdiction where the articles do not permit it — check the articles first

---

## Related skills

- [[prompt-pack-board-resolution]] — a fully drafted substantive resolution for a specific action
- [[prompt-pack-board-committee-charter]] — committee charter adopted by board resolution
- [[kb-corporate-governance-mena]] — MENA companies law reference
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction determines form requirements
