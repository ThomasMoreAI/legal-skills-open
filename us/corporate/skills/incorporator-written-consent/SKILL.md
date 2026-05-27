---
name: incorporator-written-consent
title: Action by Written Consent of Incorporator
description: Drafts an Action by Written Consent of Incorporator for newly formed U.S. corporations. Trigger when the user needs to formalize post-incorporation organizational actions (adopting bylaws, appointing initial directors) by written consent in lieu of an organizational meeting.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/incorporator-written-consent
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting]
---

# Action by Written Consent of Incorporator

Formalizes the incorporator's organizational actions after Articles of Incorporation are filed, transferring authority to the initial board of directors.

## Required Inputs

1. **Corporation legal name** — must match Articles exactly
2. **State of incorporation** — determines statutory citation
3. **Articles filing date** — date filed with Secretary of State
4. **Incorporator name(s)** — full legal name of each incorporator
5. **Initial director names** — full legal names of all appointees
6. **Bylaws** — attach as Exhibit A or note if pending

## Quick Start

1. Collect all required inputs above.
2. Identify the governing statute for the state (see State Variance below).
3. Draft per the output structure; include optional resolutions only if client requests.
4. Attach bylaws as Exhibit A or add placeholder.
5. Replace all bracketed placeholders before delivery.

## Output Structure

**Header** — Title with corporation name and effective date.

**Preamble** — Identifies incorporator, corporation name, state, and Articles filing date.

**Resolutions** (numbered):

| # | Action | Notes |
|---|--------|-------|
| 1 | Adopt Bylaws | "RESOLVED, that the Bylaws attached hereto as Exhibit A are hereby adopted…" |
| 2 | Appoint Initial Directors | List each director by full legal name; serve until successors elected and qualified |
| 3 | *(Optional)* Set fiscal year | Calendar year or specified end date |
| 4 | *(Optional)* Authorize bank accounts | Name designated institutions |
| 5 | *(Optional)* Ratify prior acts | Ratify actions taken before this consent |

**Role Conclusion** — Explicit statement that incorporator duties are complete and authority transfers to the board.

**Execution Block** — Signature line for each incorporator with printed name and title "Incorporator."

**Exhibit A** — Executed bylaws or placeholder if pending.

## State Variance

- **Delaware**: DGCL § 108
- **California**: Corp. Code § 210
- **MBCA states**: MBCA § 2.05 (most other states)
- **Default**: When state is unspecified, draft to MBCA standards
- Always verify the specific statutory citation for the target state

## Checks

- Corporation name, state, and filing date must be consistent throughout and match the filed Articles
- Director count must comply with minimums/maximums in Articles or state statute
- Multiple incorporators: all must sign unless statute or Articles permit majority action
- Notarization is typically not required; flag if state law mandates it
- Remind client: executed consent goes into corporate minute book with Bylaws and Articles
- Never deliver with unfilled bracketed placeholders

---
