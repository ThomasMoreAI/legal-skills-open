---
name: efirm-conflict-check-sboghossian
title: 'eFirm: Conflict Check'
description: Use before accepting any new matter to detect conflicts of interest across six dimensions — adverse parties, current clients, former clients (substantially related test), issue/positional conflicts, personal interests, and material-limitation conflicts. Covers ABA Model Rules 1.7–1.10 (US), LB Bar Code of Ethics, KSA Code of Law Practice, UAE Law Society rules, DIFC Rules of Conduct, and ADGM Rules of Conduct. Returns a structured clean/concern/conflict result with waiver guidance. P0 — must complete before substantive work begins.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/efirm/efirm-conflict-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# eFirm: Conflict Check

## When to use this

A conflict check is **mandatory** before any of the following:
- Accepting a new client or new matter.
- Assigning a new lawyer to an existing matter (the new lawyer may bring conflicts from their prior firm).
- A lateral hire joins the firm (screens their prior client list against the firm's).
- A client's matter scope changes materially (new adverse parties, new jurisdictions, new issues).
- A potential conflict is reported by any member of the firm.

**Never begin substantive work without completing the conflict check.** Failure to do so is a malpractice and bar-discipline issue in every covered jurisdiction.

## Inputs

| Input | Why required |
|---|---|
| New client name (legal / trading) | Core search term |
| New client corporate group and parent entities | Conflicts extend to group companies |
| New client UBOs (where known) | Positional conflicts may arise with individuals |
| All counterparties (adverse parties) | The most direct source of conflict |
| Counterparty corporate groups + UBOs | Groups must be searched, not just the named entity |
| Related parties (witnesses, lenders, advisers) | Potential issue conflicts |
| Matter description (type + subject matter) | Needed for issue-conflict analysis |
| Proposed team members (all timekeepers) | Each member must be screened individually |

## Six search dimensions

### 1. Adverse-party conflicts

Has the firm **currently or historically** represented any person or entity that is now an adverse party?

- Search firm's client database for all variations of each adverse party's name.
- Include corporate predecessor names, former names, and known aliases.
- Include affiliated entities (parent, subsidiary, sister company).
- **Result trigger**: Any positive match → conflict concern.

### 2. Current-client conflicts

Would accepting the new matter place the firm adverse to a **current active client** on any matter?

- Being adverse to a current client — even on an unrelated matter — is a concurrent conflict under ABA 1.7 and analogous rules.
- "Positional adversity" (arguing a legal position for one client that contradicts a position argued for another client in another forum) can also be a concurrent conflict, though the threshold is higher.
- **Result trigger**: Any active-client adversity → conflict, not merely concern.

### 3. Former-client conflicts (substantially related test)

Is the new matter **substantially related** to a matter on which the firm previously represented a now-adverse party?

Under ABA 1.9 and equivalent rules:
- A matter is "substantially related" if it involves the same transaction or legal dispute, or if there is a substantial risk that confidential information obtained in the prior representation could be used to the prior client's material disadvantage.
- Time since representation is relevant but does not cure the conflict automatically.
- **Result trigger**: Substantially related former representation → conflict.

### 4. Issue / positional conflicts

Would accepting the matter require the firm to take a legal position that directly contradicts a position it has advanced for another client in another proceeding or jurisdiction?

- Most sensitive in appellate, regulatory, and legislative advocacy.
- Requires substantive analysis of the legal questions in both matters.
- **Result trigger**: Direct positional contradiction on a material question of law → concern requiring partner judgment.

### 5. Personal-interest conflicts

Does any proposed team member have a personal, family, financial, or other interest that could affect their professional judgment on this matter?

Common examples:
- Family member is an officer of the adverse party.
- Attorney holds equity in a client or counterparty.
- Attorney is personally named as a witness or potential defendant.
- Attorney has a personal relationship with a key decision-maker at the counterparty.

- **Result trigger**: Any personal interest that could materially limit representation → conflict or concern.

### 6. Material-limitation conflicts

Would representation of the new client be **materially limited** by the firm's responsibilities to another client, a former client, a third person, or the lawyer's own interests?

This is the catch-all prong. Examples:
- The firm has a standing arrangement with a lender that could affect advice given to a borrower.
- A co-counsel relationship creates cross-obligations.
- A referral source expects favorable treatment.

- **Result trigger**: Any material limitation → concern requiring partner review.

## Output schema

```
CONFLICT CHECK RESULT — [New Client] vs [Matter Description] — [Date]

RESULT: [CLEAN | CONCERN | CONFLICT]

By dimension:
  1. Adverse-party check:          [Clean / Concern / Conflict — details]
  2. Current-client check:         [Clean / Concern / Conflict — details]
  3. Former-client check:          [Clean / Concern / Conflict — details]
  4. Issue/positional check:       [Clean / Concern / Conflict — details]
  5. Personal-interest check:      [Clean / Concern / Conflict — details]
  6. Material-limitation check:    [Clean / Concern / Conflict — details]

DETAILS ON ANY CONCERN OR CONFLICT:
  [Matter / client name]
  [Nature of the conflict or concern]
  [Governing rule reference]
  [Whether waivable — see below]

RECOMMENDED ACTION:
  Clean:    Proceed. Record this check in the matter file.
  Concern:  Route to conflicts partner for decision before proceeding.
  Conflict: Cannot proceed without waiver (if waivable) OR cannot proceed at all.
```

## Waiver framework

Some conflicts are **consentable** — they can be cured with the informed written consent of all affected clients. Others are **non-consentable** — no consent cures the conflict.

### Consentable conflicts (general rule)

A concurrent conflict is consentable if:
1. The lawyer reasonably believes they can provide competent and diligent representation to each affected client.
2. The representation is not prohibited by law.
3. The representation does not involve asserting a claim by one client against another in the same proceeding.
4. Each affected client gives informed written consent.

### Non-consentable conflicts (examples)

- Directly adverse representation of two clients in the same proceeding.
- Representation materially adverse to a former client on a substantially related matter where confidential information cannot be screened.
- Situations where the lawyer's own interests are so adverse that competent representation is impossible.

### Waiver drafting

Consent waivers require:
- Clear identification of the conflict.
- Explanation of the risks of dual representation.
- The client's alternatives (separate counsel).
- An unambiguous written consent signed by each affected client.

The waiver itself must be reviewed by the conflicts partner, not the matter-handling lawyer.

## Bar-rule quick reference

| Jurisdiction | Key rules | Notes |
|---|---|---|
| US (ABA) | Model Rules 1.7 (concurrent), 1.8 (specific), 1.9 (former client), 1.10 (imputation) | State rules vary; check state-specific version |
| Lebanon | Beirut Bar Code of Ethics, Art. [conflict articles] | Civil-law tradition; bar ethics council oversees |
| KSA | Code of Law Practice (Royal Decree M/38) | Emphasis on loyalty and non-adversity; Sharia-law ethical overlay |
| UAE onshore | Federal Law No. 23 of 1991 (Advocacy) + Bar rules | |
| DIFC | DIFC Rules of Conduct | Common-law framework closely tracking UK/ABA norms |
| ADGM | ADGM Rules of Conduct | Similar to DIFC |
| UK | SRA Code of Conduct 2019, Conflict Rules | Conflict of interest (own interest and client vs. client) |

## Imputation and screening

When a conflicted lawyer joins a new firm (lateral), their conflict is **imputed** to the entire new firm under most bar rules. A **Chinese wall** (ethical screen) can cure the imputation in many (but not all) jurisdictions if:
- The screen is timely erected (before any confidential information is shared).
- The screened lawyer receives no part of the fee.
- Written notice is given to the affected former client.

DIFC and ADGM explicitly permit screening to rebut imputation; US rules vary by state; UK SRA permits screens in some circumstances.

## Critical reminder

Conflict check completion must be **recorded with a timestamp and outcome** in the matter file. The check should be repeated if new parties emerge during the matter. A single check at intake is not sufficient for complex, long-running matters.

## Related skills

- [[efirm-client-intake-form]]
- [[efirm-matter-creation-flow]]
- [[efirm-engagement-letter-draft]]
- [[efirm-team-handoff-summary]]
- [[research-sanctions-screening]]
