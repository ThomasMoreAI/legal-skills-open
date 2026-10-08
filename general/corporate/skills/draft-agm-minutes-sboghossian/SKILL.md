---
name: draft-agm-minutes-sboghossian
title: Draft — Annual General Meeting (AGM) Minutes
description: Use when asked to draft Annual General Meeting (AGM) minutes for a company, capturing the statutory resolutions required at an annual meeting — financial statements, auditor approval, director elections, dividends, and any other business. Applicable across MENA (UAE, KSA, Lebanon, Egypt) and common-law jurisdictions (DIFC, ADGM, UK). Outputs a minute that can be entered into the company's minute book and, where required, filed with the commercial registrar.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-agm-minutes
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Draft — Annual General Meeting (AGM) Minutes

## When to use this

Use this skill when:
- A company has held its annual general meeting and needs formal minutes.
- Minutes are needed for a company's statutory file, auditor, or commercial registrar.
- A lawyer is reviewing draft minutes prepared by a company secretary.

AGM minutes serve dual purposes: they are (1) the internal governance record and (2) often a filing requirement with the company registrar (MOC in KSA, DED/Economic Department in UAE, Commercial Register in LB and EG).

## Required inputs

| Input | Notes |
|---|---|
| Company name and registration number | Full legal name as registered |
| Jurisdiction and company type | UAE LLC / KSA Company / LB SAL / DIFC Company, etc. |
| Date, time, and location of AGM | Physical or virtual (virtual AGM rules vary by jurisdiction) |
| List of shareholders present or represented | Name, shares held, percentage; proxy holders if any |
| List of directors and officers present | |
| Agenda items | Use the statutory minimum as a default (see below) |
| Financial year-end and financials approved | Fiscal year the meeting covers |
| Auditor details | Incumbent auditor + whether re-appointed |
| Directors re-elected or newly appointed | Names + terms |
| Dividend declared (if any) | Amount per share, record date, payment date |

## Standard AGM agenda (statutory minimum)

Adapt to jurisdiction-specific requirements.

1. **Opening and confirmation of quorum** — chair opens meeting; secretary or chair confirms quorum (typically a majority or two-thirds of voting shares, depending on articles).
2. **Appointment of chairperson and secretary of the meeting** — often formality; chair is usually the Board Chair.
3. **Approval of prior AGM minutes** — resolution to adopt the minutes of the last AGM as a true and accurate record.
4. **Review and approval of annual financial statements** — audited balance sheet, P&L, cash flow, notes; resolution to approve.
5. **Review of auditor's report** — acknowledgment of auditor's findings.
6. **Appointment / re-appointment of auditors** — resolution to re-appoint (or appoint a new firm) and authorize the board to fix their remuneration.
7. **Director appointments / re-elections** — individual resolutions per director (or by class where articles permit batch elections); term stated.
8. **Dividend declaration** — if declared: per-share amount, record date, payment date (or statement that no dividend is declared).
9. **Any other business** — items from the agenda notice; miscellaneous shareholder questions.
10. **Closing** — chair declares the meeting closed; time noted.

## Document structure

```
MINUTES OF THE ANNUAL GENERAL MEETING
OF [COMPANY NAME] ([REGISTRATION NUMBER])

Held on [DATE] at [TIME] at [LOCATION / virtual meeting platform]

PRESENT:
  Shareholders: [table of names, shares, % held, proxy if any]
  Directors: [list]
  In attendance: [secretary, counsel, auditors]

CHAIRPERSON: [Name]
SECRETARY: [Name]

1. OPENING AND QUORUM
   [Quorum statement: "[X]% of issued share capital represented, constituting a quorum
   per Article [X] of the Company's [Articles / Memorandum of Association]"]

2. MINUTES OF PRIOR AGM
   RESOLVED THAT the minutes of the Annual General Meeting held on [DATE] be and 
   are hereby approved as a true and accurate record.

3. FINANCIAL STATEMENTS — [FISCAL YEAR]
   The Chairman presented the audited financial statements for the year ended [DATE].
   RESOLVED THAT the audited financial statements of the Company for the year ended 
   [DATE], as presented, be and are hereby approved.

4. AUDITOR'S REPORT
   [Acknowledgment text]

5. RE-APPOINTMENT OF AUDITORS
   RESOLVED THAT [Auditor Firm], having been nominated, be and are hereby re-appointed 
   as auditors of the Company for the ensuing year, and the Board of Directors is 
   authorized to fix their remuneration.

6. DIRECTOR ELECTIONS
   [Per director:]
   RESOLVED THAT [Name] be and is hereby re-elected / elected as a Director of the 
   Company for a term of [X] year(s) / until the next AGM.

7. DIVIDEND
   RESOLVED THAT a dividend of [AMOUNT] per [ordinary] share be and is hereby declared, 
   payable on [DATE] to shareholders of record on [RECORD DATE].
   — OR —
   The Chairman noted that the Board does not recommend a dividend for the fiscal year 
   [YEAR]. No dividend was declared.

8. ANY OTHER BUSINESS
   [Record any items raised; if none: "There being no further business, the Chairperson 
   declared the meeting closed at [TIME]."]

SIGNED AND CERTIFIED AS A TRUE AND ACCURATE RECORD:

_______________________        _______________________
[Chair Name]                   [Secretary Name]
Chairperson                    Secretary of the Meeting
Date: ___________              Date: ___________
```

## Jurisdictional notes

### UAE (LLC and PJSC)
- UAE Federal Decree-Law on Commercial Companies requires AGM within 4 months of financial year-end for LLCs; 3 months for PJSCs.
- Virtual AGMs: permitted post-pandemic under ministerial resolutions, subject to articles.
- Minutes in Arabic (for onshore entities) or English (DIFC/ADGM); Arabic takes precedence for onshore.
- Filing: AGM minutes for PJSCs filed with SCA; for LLCs typically filed with the local DED.

### KSA
- Companies Law requires AGM within 6 months of fiscal year-end.
- Quorum: 50%+ of shares for ordinary AGM; 75% for extraordinary matters.
- Minutes filed with Ministry of Commerce (Mawthq electronic system for authentication recommended).
- Arabic is the required language of corporate documents.

### Lebanon (SAL)
- Code de Commerce requirements: AGM within 6 months of financial year-end.
- Quorum: 50%+ of shares on first call; no quorum requirement on second call after adjournment.
- Minutes signed by shareholders present (or their proxies) and entered in the minute book.
- Notarization of certain AGM decisions (especially capital changes) may be required.

### Egypt
- Companies Law (Law 159/1981): AGM within 3 months of fiscal year-end.
- Notice requirements: 15 days before meeting by registered mail and newspaper publication.
- Minutes kept in a dedicated minute book; copies filed with the Companies Authority (GAFI).

### DIFC / ADGM
- DIFC Companies Law / ADGM Companies Regulations: AGM required for public companies; private companies may dispense if all shareholders consent in writing.
- English minutes sufficient.
- Virtual AGM expressly permitted.

## Common mistakes

- **Missing quorum statement**: without it, the resolutions are voidable.
- **Vague director election wording**: state term clearly; "until the next AGM" or fixed years.
- **Dividend resolution without payment mechanism**: always state record date and payment date.
- **Wrong fiscal year reference**: particularly common when meetings are held after the calendar year changes.
- **No signature by chair and secretary**: unsigned minutes are not valid corporate records.

## Related skills

- [[draft-board-resolution]]
- [[draft-articles-of-association]]
- [[draft-cap-table-resolution]]
- [[draft-bylaws]]
