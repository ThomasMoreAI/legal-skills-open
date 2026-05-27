---
name: annual-meeting-notice
title: Notice of Annual Shareholders Meeting
description: Drafts legally compliant Notice of Annual Shareholders Meeting for US corporations, covering state-specific notice periods, record dates, quorum and voting thresholds, proxy procedures, and SEC Regulation 14A compliance for public companies. Use when preparing annual meeting notices, shareholder meeting notifications, or proxy notice and access mailings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/annual-meeting-notice
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Notice of Annual Shareholders Meeting

Drafts a formal notice of annual shareholders meeting satisfying state corporate code requirements and, for public companies, SEC proxy rules.

## Prerequisites

Gather before drafting:

1. **Corporate documents** — articles of incorporation, current bylaws, prior meeting notices
2. **State of incorporation** — determines applicable business corporation act and notice periods
3. **Public vs. closely held status** — determines SEC disclosure obligations
4. **Record date** — board-approved date fixing shareholder eligibility (if not set, flag for client)
5. **Meeting logistics** — date, time, location, format (in-person / virtual / hybrid), platform details
6. **Agenda items** — director nominees, auditor ratification, proposed amendments, other business
7. **Stock classes and voting rights** — shares outstanding, votes per share, class voting requirements

## Quick Start

1. Confirm state of incorporation and look up statutory notice window
2. Verify record date compliance with state law
3. Draft notice using the output structure below
4. Apply public-company overlay if SEC-reporting entity
5. Mark any uncertain statutory citations with `[VERIFY]`

## Output Structure

### Header

- Title: "NOTICE OF ANNUAL MEETING OF SHAREHOLDERS" (prominent)
- Full legal company name per articles of incorporation
- Notice date within statutory notice period

### Opening Statement

- Formal notice of meeting, identifying record date shareholders entitled to notice and vote
- Confirm notice date falls within required statutory window

### Meeting Logistics

- **In-person**: full street address, building, floor, room; security/access procedures
- **Virtual**: URL, meeting ID, password, tech requirements; registration deadline
- **Hybrid**: both of the above
- Include board authority to change format/location and notification method for changes

### Agenda Items

For each item, state the approval threshold (plurality, majority, supermajority) and board recommendation:

1. **Election of Directors** — number of seats, term length, individual vs. slate
2. **Financial Statements** — approval of audited financials; reference to full reports
3. **Auditor Ratification** — firm name, tenure, fees
4. **Proposed Amendments** (if any) — summary of changes, impact on shareholder rights, reference to full text in proxy materials
5. **Other Business** — standard catch-all provision

### Voting and Proxy Information

Include all of the following:

- Record date and eligibility (ownership as of close of business on record date)
- Votes per share for each stock class
- Quorum requirement (shares present in person or by proxy)
- Vote threshold for each proposal type
- Proxy submission methods (mail, telephone, internet) and deadline
- Right to revoke proxy: later-dated proxy, written revocation to secretary, or in-person vote
- **Public companies only**: compliance with Securities Exchange Act section 14(a) and Regulation 14A; reference proxy statement availability

### Shareholder Resources

- Corporate secretary / investor relations contact (phone, email, mailing address)
- How to access annual report, proxy statement, meeting materials (website, EDGAR for public companies, paper copy request)
- Notice and access procedures if applicable
- Accessibility accommodations statement

### Signature Block

```
By Order of the Board of Directors,

_________________________
[Name]
[Title — Corporate Secretary or Assistant Secretary]
[Date of execution]
```

## Compliance Checks

- **Notice period**: verify state-specific statutory window (typically 10-60 days before meeting); bylaws may impose stricter requirements — use the stricter standard
- **Record date**: must comply with state law on advance-of-meeting timing; if not provided, flag for client
- **SEC compliance**: for public companies, reference proxy statement availability per Regulation 14A and notice-and-access rules; omit SEC provisions for closely held companies
- **Multi-class stock**: detail voting power per class and any class-specific approval requirements
- **Distribution method**: note applicable delivery method (mail, e-delivery with consent, notice and access posting); advise client to maintain distribution records
- **Tone**: formal corporate register — clear and precise, no ambiguity in dates, times, locations, or procedures
- **Do not** fabricate specific statutory citations without verification; mark uncertain references with `[VERIFY]`

---

**Key changes made:**

- **Removed `tags`** — not part of the Agent Skills spec
- **Added Quick Start section** — gives the agent a concise 5-step workflow entry point
- **Collapsed verbose tables** into bullet lists (meeting logistics, header) — same information, fewer tokens
- **Merged "Guidelines" into "Compliance Checks"** — renamed for clarity and tightened prose
- **Removed redundant checkbox formatting** in Voting and Proxy section — kept as plain bullets since it's output guidance, not a task checklist
- **Condensed opening** to a single sentence instead of repeating the description
- **~85 lines** (down from ~99), with better scannability and no lost legal substance
