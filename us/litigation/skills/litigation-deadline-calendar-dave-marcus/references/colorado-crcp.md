# Colorado Rules of Civil Procedure — Deadline Reference

This reference contains the key CRCP rules relevant to computing litigation deadlines in Colorado state court. The skill should use this as its primary reference when the user specifies Colorado as the jurisdiction.

**Important**: These rules reflect the state of Colorado law as of early 2026. The skill's verification step should confirm these remain current by searching for recent rule changes before relying on them.

---

## Table of Contents

1. [Rule 6 — Computing Time](#rule-6)
2. [Rule 26 — Disclosure and Discovery Framework](#rule-26)
3. [Rule 33 — Interrogatories](#rule-33)
4. [Rule 34 — Requests for Production](#rule-34)
5. [Rule 36 — Requests for Admission](#rule-36)
6. [Rule 30 — Depositions](#rule-30)
7. [Rule 56 — Summary Judgment](#rule-56)
8. [Rule 16 — Case Management](#rule-16)
9. [Expert Witness Deadlines](#expert-deadlines)
10. [Motion Deadlines](#motion-deadlines)
11. [Colorado Legal Holidays](#holidays)

---

## Rule 6 — Computing Time {#rule-6}

### Core Counting Method (Rule 6(a))
- **Exclude the trigger day**: Do not count the day of the act, event, or default that starts the clock.
- **Count every day** (including weekends and holidays) for periods of **11 days or more**.
- **For periods less than 11 days** (not specified as "calendar days"): exclude intermediate Saturdays, Sundays, and legal holidays from the count.
- **If the last day falls on a Saturday, Sunday, or legal holiday**: the deadline extends to the end of the next day that is not a Saturday, Sunday, or legal holiday.
- **"Calendar days"** means consecutive days including all weekends and holidays with no exclusions.

### Service Method Adjustments
- **Electronic service (e-filing)**: No additional days added.
- **Mail service**: Add **3 days** to any response period after service by mail (Rule 6(e)).

---

## Rule 26 — Disclosure and Discovery Framework {#rule-26}

### Initial Disclosures (Rule 26(a)(1))
- Due within **28 days** of the at-issue date.

### Case Management Order
- Parties must begin conferring within **14 days** of the case being at issue.
- Proposed CMO must be filed within **42 days** after the case is at issue.

### Discovery Cutoff (Rule 16(b)(11))
- All discovery (including responses) must be completed no later than **49 days before the trial date**.
- This is the critical backward-computation anchor for many discovery deadlines.

### Expert Witness Disclosures (Rule 26(a)(2))
- **Plaintiff's expert disclosures**: Due **126 days** before trial.
- **Defendant's expert disclosures**: Due **98 days** before trial.
- **Rebuttal expert disclosures**: Due **63 days** before trial.

---

## Rule 33 — Interrogatories {#rule-33}

- **Response deadline**: **35 days** after service.
- **Presumptive limit**: 30 interrogatories per party (may be modified by CMO).
- **Backward computation**: To ensure responses are received before the discovery cutoff, interrogatories must be served at least **35 days + discovery cutoff buffer** before trial. In practice: serve no later than **84 days before trial** (49 days discovery cutoff + 35 days response time).

---

## Rule 34 — Requests for Production {#rule-34}

- **Response deadline**: **35 days** after service.
- **Presumptive limit**: 20 requests per party.
- **Backward computation**: Same as interrogatories. Serve no later than **84 days before trial**.

---

## Rule 36 — Requests for Admission {#rule-36}

- **Response deadline**: **35 days** after service.
- **Presumptive limit**: 20 requests per party.
- **Critical consequence**: Failure to respond within the deadline means the matters are **deemed admitted**. This is one of the most dangerous deadlines in Colorado litigation.
- **Backward computation**: Serve no later than **84 days before trial**.

---

## Rule 30 — Depositions {#rule-30}

- **Notice requirement**: Reasonable notice must be given to every other party. While no specific day count is prescribed, **14 days** is generally considered reasonable notice.
- **Duration limit**: 1 day of 7 hours per deponent (may be modified by court order or stipulation).
- **Backward computation**: All depositions must be completed before the discovery cutoff (49 days before trial). With reasonable notice, the last day to notice a deposition is approximately **63 days before trial** (49 + 14 days notice).

---

## Rule 56 — Summary Judgment {#rule-56}

- **Motion filing**: Must be filed at least **91 days** before trial (unless the court sets a different deadline in the CMO).
- **Response deadline**: **35 days** after service of the motion.
- **Reply deadline**: **14 days** after service of the response.

Note: The CMO will typically set a dispositive motion deadline that may differ from Rule 56's default. Always defer to the CMO deadline when one is specified.

---

## Rule 16 — Case Management {#rule-16}

- **Trial preparation conference**: Typically set by the court, often 30-60 days before trial.
- **Pretrial statement/order**: Due as specified in the CMO, often 14-21 days before trial.
- **Proposed jury instructions**: Due as specified in the CMO, often 14-28 days before trial.
- **Witness and exhibit lists**: Due as specified in the CMO, typically with the pretrial statement.
- **Motions in limine**: Due as specified in the CMO, often 21-35 days before trial.

---

## Expert Witness Deadlines {#expert-deadlines}

Working backward from trial:

| Deadline | Days Before Trial | Rule |
|----------|------------------|------|
| Plaintiff expert disclosure | 126 days | Rule 26(a)(2) |
| Defendant expert disclosure | 98 days | Rule 26(a)(2) |
| Rebuttal expert disclosure | 63 days | Rule 26(a)(2) |
| Expert deposition completion | 49 days | Rule 16(b)(11) |

---

## Motion Deadlines {#motion-deadlines}

### Dispositive Motions
- **Default deadline (Rule 56)**: 91 days before trial.
- **CMO deadline**: Overrides the default when specified.
- **Response**: 35 days after service.
- **Reply**: 14 days after service of response.

### Non-Dispositive Motions
- **Response**: 21 days after service (unless the court sets a different deadline).
- **Reply**: 7 days after service of response.

### Motions to Amend Pleadings / Join Parties
- Deadline set by CMO; no default rule deadline.

---

## Colorado Legal Holidays {#holidays}

For deadline computation purposes, these are legal holidays under Rule 6(a)(2):

- January 1 — New Year's Day
- Third Monday in January — Martin Luther King Jr. Day
- Third Monday in February — Washington-Lincoln Day (Presidents' Day)
- Last Monday in May — Memorial Day
- July 4 — Independence Day
- First Monday in September — Labor Day
- Second Monday in October — Columbus Day
- November 11 — Veterans Day
- Fourth Thursday in November — Thanksgiving Day
- December 25 — Christmas Day
- Any other day (except Saturday or Sunday) when the court is closed

Note: When a holiday falls on a Saturday, it is typically observed on Friday. When it falls on a Sunday, it is typically observed on Monday. The skill should compute actual observed dates for each year.
