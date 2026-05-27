---
name: shareholders-meeting-minutes
title: Shareholders Meeting Minutes
description: 'Drafts minute-book-ready U.S. corporate shareholders meeting minutes covering notice, record date, quorum, attendance, reports, votes, and resolutions. Use for annual or special shareholders meetings, director elections, auditor ratification, and shareholder proposals. Triggers: "shareholders meeting minutes", "annual meeting minutes", "special meeting minutes", "quorum", "record date", "proxy", "election of directors", "ratify auditors".'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/shareholders-meeting-minutes
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Shareholders Meeting Minutes

Drafts formal minutes recording shareholders meeting proceedings and vote outcomes, suitable for the corporate minute book.

## Required Inputs

Collect before drafting:

- Corporation legal name, state of incorporation, principal office address
- Meeting type (annual/special), date, time, location or virtual platform
- Record date, notice method, date sent
- Bylaws/charter quorum and voting thresholds
- Shareholder list and proxy data as of record date
- Agenda, reports, proposals, resolutions, vote tabulations
- Prior meeting minutes for approval (if any)
- Presiding officer and secretary names/titles
- Vote results per item (for/against/abstain/withheld)

## Workflow

1. **Validate meeting** — Confirm notice compliance, record date, quorum met, shareholder list available
2. **Record attendance** — In person, by proxy, key officers present
3. **Summarize reports** — High-level only; no editorializing or privileged commentary
4. **Document each action** — Exact vote tallies per item; note any supermajority requirements
5. **Close** — Adjournment time, motion, secretary certification

## Template

```text
MINUTES OF [ANNUAL/SPECIAL] MEETING OF SHAREHOLDERS
OF [CORPORATION LEGAL NAME]
Date: [Month DD, YYYY]
Time: [HH:MM a.m./p.m. Time Zone]
Location: [Address or Virtual Platform + Access Method]

1. Call to Order
The [annual/special] meeting of shareholders of [Corporation Legal Name] (the "Corporation") was called to order at [time] by [Name, Title], who acted as Chair. [Name, Title] acted as Secretary and recorded the minutes.

2. Notice and Record Date
The Chair reported that notice of the meeting was [given/waived] in accordance with the Corporation's bylaws and applicable state law. The record date for determining shareholders entitled to notice and vote was [Record Date]. A list of shareholders entitled to vote was made available for inspection during the meeting.

3. Quorum
The Secretary reported that [#] shares, representing [#/%] of the [#] shares outstanding, were present in person or by proxy. A quorum was declared present in accordance with the bylaws and applicable law.

4. Approval of Prior Minutes
The minutes of the shareholders meeting held on [Prior Meeting Date] were [approved as presented/approved as amended].

5. Reports
- [Officer Title/Name] presented a report on [operations/financials/other].
- [Additional reports as applicable.]

6. Election of Directors (if applicable)
Nominations:
- [Nominee Name] (nominated by [Name])
Nominations were [closed by motion/duly closed].
Results:
- [Nominee Name]: [#] FOR, [#] WITHHELD, [#] ABSTAIN
Elected to serve until [term/meeting]: [Names].

7. Ratification of Independent Auditors (if applicable)
Upon motion duly made and seconded, the shareholders voted to ratify the appointment of [Firm Name] as independent auditors for the fiscal year ending [Date].
Vote: [#] FOR, [#] AGAINST, [#] ABSTAIN. [Approved/Not approved].

8. Other Proposals/Resolutions (each separately)
Proposal: [Description and resolution text reference]
Vote: [#] FOR, [#] AGAINST, [#] ABSTAIN. [Approved/Rejected].
[If supermajority required: "The required [__]% threshold was [met/not met]."]

9. Adjournment
There being no further business, the meeting was adjourned at [time] upon [motion duly made and seconded/mutual consent].

CERTIFICATION
I hereby certify that the foregoing minutes are a true and accurate record of the proceedings of the [annual/special] meeting of shareholders of [Corporation Legal Name].

____________________________________
[Name], Secretary
Date: [Month DD, YYYY]
```

## Pitfalls and Checks

- **Never invent facts.** If data is missing, insert `[NEEDED]` and list all gaps at the end of the document.
- Use past tense, neutral tone, and consistent defined terms ("the Corporation").
- Verify quorum and voting thresholds against bylaws/charter and state statute before stating compliance.
- For virtual/hybrid meetings, state the platform and confirm governing-document compliance.
- Reflect proxy voting and inspector of elections when provided.
- Flag any inconsistency between vote results and required thresholds.
