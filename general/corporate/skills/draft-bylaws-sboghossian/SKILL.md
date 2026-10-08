---
name: draft-bylaws-sboghossian
title: Draft — Corporate Bylaws
description: Use when asked to draft or review corporate bylaws (or bye-laws) — the internal governance rules that operate alongside and beneath the Articles of Association. Covers shareholder meeting procedures, board structure and procedures, officer roles, director and officer indemnification, stock transfer procedures, conflict-of-interest policy, and amendment mechanics. Particularly relevant for US-style companies, Delaware incorporations, and common-law jurisdictions (DIFC, ADGM, UK); in civil-law MENA jurisdictions bylaws-style provisions are typically embedded in the Articles.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-bylaws
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Draft — Corporate Bylaws

## When to use this

Bylaws are the internal operating rules of a corporation. They sit below the Articles of Association (or Certificate of Incorporation in US practice) in the corporate governance hierarchy:

```
Certificate of Incorporation / Memorandum of Association (highest)
  ↓
Articles of Association / Charter
  ↓
Bylaws (internal operating rules)
  ↓
Board resolutions (specific decisions)
```

Use this skill when:
- A newly incorporated company needs initial bylaws.
- Existing bylaws need to be amended (after a financing, restructuring, or change in board composition).
- A company needs bylaws that accommodate a shareholders' agreement (cross-reference and consistency check).

**Civil-law MENA note**: In UAE onshore LLCs, KSA companies, Lebanon SALs, and Egypt SAEs, the "bylaws" equivalent is embedded in the Articles of Association / Statuts. There is typically no separate bylaws document. Use [[draft-articles-of-association]] for those jurisdictions. Bylaws as a separate document are most common in US corporations, DIFC and ADGM companies, and UK-style companies.

## Required inputs

| Input | Notes |
|---|---|
| Company name and jurisdiction of incorporation | |
| Share structure | Classes, number of shares authorized |
| Board size and composition | Minimum / maximum directors; any class-specific nomination rights |
| Officer structure | Which officers are required (CEO, CFO, Secretary, etc.) |
| Quorum requirements | For shareholder and board meetings |
| Voting thresholds | Ordinary vs supermajority matters |
| Indemnification scope | Broad (DGCL-maximum) or limited |
| Amendment process | Board only, or shareholder approval required |

## Document structure

### Article I — Offices
- **Registered office**: state-registered agent for service of process.
- **Principal office**: principal place of business (may differ from registered office).

### Article II — Shareholders' meetings

1. **Annual meeting**: timing (e.g., within 5 months of financial year-end); purpose (elect directors, approve financials, conduct other business).
2. **Special meetings**: who may call (typically: the board, a majority of directors, or holders of ≥10–25% of shares).
3. **Notice**: written notice at least 10 (minimum) and no more than 60 days before a meeting; content requirements (record date, agenda for special meetings).
4. **Record date**: the date on which shareholders are identified for voting and notice purposes; set by board, typically 10–60 days before the meeting.
5. **Quorum**: majority (50%+1) of shares entitled to vote, represented in person or by proxy. If quorum not achieved, meeting adjourned.
6. **Voting**: one vote per share unless articles specify otherwise. Voice vote default; any shareholder may demand a ballot.
7. **Proxies**: any shareholder may appoint a proxy; proxy need not be a shareholder.
8. **Written action in lieu of meeting**: shareholders holding sufficient votes may act without a meeting by written consent (useful for controlled companies).
9. **Remote / virtual meetings**: expressly authorize participation by conference call or video; note that certain states require in-person option.

### Article III — Board of directors

1. **General powers**: the business and affairs of the Corporation shall be managed by or under the direction of the Board.
2. **Number of directors**: minimum and maximum; initial number set by incorporator; subsequent changes by board or shareholder resolution.
3. **Classification of board** (if applicable): staggered board with three classes (each serving 3-year terms staggered); anti-takeover protection but reduces accountability — include only if deliberate choice.
4. **Election**: directors elected by shareholders at the annual meeting; plurality voting default (most votes wins regardless of majority) or majority voting (common in large public companies).
5. **Term**: until successor is elected and qualified, or earlier removal.
6. **Vacancies**: filled by board (not shareholders) for efficiency; filled for remainder of term.
7. **Removal**: with or without cause by shareholders; "for cause" only by board (specify clearly).
8. **Compensation**: board may fix its own compensation; disclose and manage conflicts.

### Article IV — Board meetings and committees

1. **Regular meetings**: board may schedule recurring meetings without additional notice.
2. **Special meetings**: called by Chair, CEO, or any two directors; notice requirements (typically 48 hours).
3. **Notice waiver**: a director present at a meeting waives notice unless they object at the start.
4. **Quorum**: majority of the total number of directors then in office.
5. **Voting**: majority of directors present at a duly-constituted meeting.
6. **Action without meeting**: unanimous written consent of all directors.
7. **Telephonic/video meeting**: explicitly authorized; counts as presence.
8. **Committees**:
   - **Audit Committee**: independent directors only; responsible for financial reporting oversight, external auditor relationship.
   - **Compensation Committee**: executive compensation decisions.
   - **Nominating/Governance Committee**: director nominations, governance policies.
   - Committee may act within its delegated authority without full board vote.

### Article V — Officers

1. **Required officers**: President/CEO; Secretary; Treasurer/CFO. Additional officers as board determines.
2. **Appointment and removal**: by board at any time; at-will unless employment agreement provides otherwise.
3. **CEO authority**: general supervision of business; implements board directives; executes contracts authorized by the board.
4. **Secretary**: keeps corporate records, minute books, resolutions; certifies resolutions to third parties.
5. **CFO/Treasurer**: financial records; banking relationships; financial reports to board.
6. **Dual roles**: one person may hold multiple officer roles, but not both President and Secretary (for internal control purposes).

### Article VI — Indemnification

1. **Scope**: broad indemnification of directors, officers, employees, and agents to the maximum extent permitted by applicable corporate law (e.g., Delaware DGCL Section 145).
2. **Standard**: indemnification if the person acted in good faith and in a manner reasonably believed to be in the best interests of the corporation; not applicable if finally adjudicated to have acted with gross negligence or willful misconduct.
3. **Advancement of expenses**: the corporation advances legal fees and costs pending final determination; repayment obligation if ultimately determined not entitled to indemnification.
4. **Insurance**: the corporation may (and should) purchase D&O liability insurance.
5. **Non-exclusivity**: indemnification rights are in addition to, not exclusive of, any other rights under applicable law.

### Article VII — Stock / share matters

1. **Certificates**: shares may be certificated or uncertificated; if certificated, state signed by officers.
2. **Transfer of shares**: registration of transfer; transfer agent; lost certificate procedure.
3. **Record holders**: beneficial vs record ownership distinction.
4. **Pre-emption rights** (if applicable): reference to Articles or shareholders' agreement for any right of first refusal on transfer; bylaws should cross-reference rather than duplicate.

### Article VIII — Conflicts of interest

1. **Disclosure obligation**: a director with a material financial interest in a transaction must disclose fully to the board or a committee.
2. **Approval**: conflicted director abstains from voting; transaction approved by disinterested directors (or shareholders if board approval not adequate).
3. **Safe harbor**: a properly disclosed and approved conflict transaction is not voidable solely due to the interest.
4. **Related party transactions policy**: reference to or incorporate a separate RPT policy for public companies.

### Article IX — Amendments

1. **Board authority**: board may adopt, amend, or repeal bylaws unless the articles reserve this to shareholders.
2. **Shareholder authority**: shareholders may adopt, amend, or repeal bylaws by vote.
3. **Special provisions**: certain protective provisions (e.g., removal of directors only for cause) may require supermajority to amend.

## Jurisdictional notes

### Delaware (US)
- Most sophisticated US private companies and many public companies incorporate in Delaware.
- Delaware General Corporation Law (DGCL) is the primary reference.
- DGCL Section 102(b)(7): permits broad exculpation of directors for duty-of-care claims (include in certificate, not bylaws).
- Bylaws can be amended by board unless the certificate reserves amendment to shareholders.

### DIFC
- DIFC Companies Law (DIFC Law 5/2018): similar in structure to English company law.
- Companies may adopt "articles of association" covering what in a US company would be bylaws.
- Board resolutions and minutes requirements: as per DIFC Companies Law.

### ADGM
- ADGM Companies Regulations 2020: similar structure to DIFC.
- Separate bylaws not a recognized concept; governance provisions are in the articles.

### UK
- Companies Act 2006: "articles of association" cover governance; separate bylaws not used.
- Model articles available as default; companies may adopt bespoke articles.

## Common mistakes

- **Bylaws conflict with the Articles**: if the Articles restrict board authority and the bylaws attempt to expand it, the Articles control; always read them together.
- **Quorum set too high**: if a director feud makes quorum impossible to achieve, the company is paralyzed; include an adjournment and reduced-quorum mechanism.
- **No virtual meeting provision**: not expressly authorizing virtual meetings can create uncertainty.
- **Indemnification provision not reviewed against applicable law**: the scope of permissible indemnification differs by state/jurisdiction; DGCL Section 145 is more permissive than many other states.
- **Omitting conflict-of-interest procedure**: without a clear safe harbor procedure, related-party transactions are vulnerable to challenge.

## Related skills

- [[draft-articles-of-association]]
- [[draft-board-resolution]]
- [[draft-agm-minutes]]
- [[draft-shareholders-agreement]]
