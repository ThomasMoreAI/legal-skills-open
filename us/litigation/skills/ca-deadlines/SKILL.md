---
name: ca-deadlines
title: California Case Deadlines
description: Use this skill whenever the user asks about timing or deadlines in a California civil case. Triggers include "when is my answer due California", "compute the deadline", "how many court days", "what's the opposition brief deadline", "I was served — when do I have to respond", "when does my discovery response have to go out", "California motion notice requirement", "CCP 1005", "CCP 12", "calendar days vs court days California", "mail service adds days California", "summary judgment timeline California CCP 437c", "how long do I have to file a motion to vacate California", "exemption claim deadline California", "FDCPA statute of limitations", "Rosenthal Act statute of limitations", "when does the discovery cutoff hit", "CMC statement deadline". Computes court-day and calendar-day deadlines under Code Civ. Proc., § 12 and § 1013 using Govt. Code § 6700 California state holidays (including Day after Thanksgiving), covers the extended service rules under CCP § 1010.6 for e-service
  and CCP § 1013 for mail, and catalogs key California civil deadlines (answer, demurrer, motion notice, opposition, reply, CMC statement, discovery cutoff, summary judgment, and post-judgment). Deterministic date arithmetic is delegated to scripts/case-calendar.py. Composes with ca-first-30-days, ca-discovery, ca-post-judgment, and ca-file-packet.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# California Case Deadlines

This skill computes deadlines in California civil cases — when
to answer, file or respond to motions, serve discovery, claim
exemptions, and the statutes of limitations that bound new
actions.

> **NOT LEGAL ADVICE.** Verify every deadline against the current
> rule and statute. The legislature can amend the Code of Civil
> Procedure without notice.

## How time is computed in California

### Code Civ. Proc., § 12 — the fundamental rule

- **Exclude the first day** (day of the act, event, or default
  triggering the period).
- **Include the last day** of the period.
- **If the last day is a holiday or weekend**: the period extends
  to the **next court day** (Code Civ. Proc., § 12a).

### Code Civ. Proc., § 12a — holiday/weekend extension

If the last day for filing or service falls on a Saturday, Sunday,
or a judicial holiday, the period extends to the next day that is
not a Saturday, Sunday, or holiday.

### Court days vs. calendar days

Many California deadlines are measured in **court days** (also
called "judicial days"). A court day is any day that the court is
open for business — Monday through Friday excluding judicial
holidays. Other deadlines are measured in **calendar days**
(including weekends and holidays, with extension only if the last
day falls on a non-court day).

Confirm whether a specific deadline uses court days or calendar
days by reading the governing statute or rule.

### Code Civ. Proc., § 12c — court day defined

A "court day" is a day that the court is open for business,
i.e., Monday through Friday excluding judicial holidays listed
in Govt. Code § 6700.

---

## California judicial holidays (Govt. Code § 6700)

| Holiday | Date |
|---|---|
| New Year's Day | January 1 |
| Martin Luther King, Jr. Day | 3rd Monday of January |
| Presidents' Day | 3rd Monday of February |
| Cesar Chavez Day | March 31 |
| Memorial Day | Last Monday of May |
| Juneteenth | June 19 |
| Independence Day | July 4 |
| Labor Day | 1st Monday of September |
| Native American Day | 4th Friday of September |
| Veterans Day | November 11 |
| Thanksgiving Day | 4th Thursday of November |
| **Day after Thanksgiving** | **4th Friday of November** (Govt. Code § 6700(a)(14)) |
| Christmas Day | December 25 |

**Observed-day rule**: when a holiday falls on a Saturday, courts
observe it on the preceding Friday; when it falls on a Sunday,
courts observe it on the following Monday. Verify per-county
closures — some courts observe additional closures.

**Note — Cesar Chavez Day (March 31)**: while it is a state
employee holiday under Govt. Code § 6700, many superior courts do
not close on Cesar Chavez Day. Verify whether the specific court
will be open before relying on this date as a holiday.

**Note — Lincoln's Birthday (Feb. 12)**: historically observed;
largely phased out. Do not assume courts close on Feb. 12.

---

## Service additions

### Code Civ. Proc., § 1013 — mail service

When service is by mail, **additional time** is added to any
period requiring response or act:

| Distance | Additional days |
|---|---|
| Within California | 5 calendar days |
| Outside California, within U.S. | 10 calendar days |
| Outside U.S. | 20 calendar days |

The 5-day addition is for the period within which the served
party must perform an act. It applies only when the triggering
act was service by mail; it does NOT apply when the triggering
act was filing or a court order.

### Code Civ. Proc., § 1010.6 — electronic service

When service is by electronic means (e-service through an e-
filing system or by email/fax):

- Add **2 court days** to any response period (Code Civ. Proc.,
  § 1010.6(a)(3)(B)).
- Note: mandatory e-filing systems in LASC and many other
  counties deliver e-service at the time of filing; the 2-court-
  day addition still applies to the opposing party's response
  period.

---

## Deterministic computation

Use the bundled `scripts/case-calendar.py` for date arithmetic:

```bash
# Compute the answer deadline — 30 calendar days from service
# on 2025-04-15
python3 plugins/ca-court-docs/scripts/case-calendar.py \
  --from 2025-04-15 --rule answer-due

# Compute a custom deadline — 16 court days from a given date
python3 plugins/ca-court-docs/scripts/case-calendar.py \
  --from 2025-04-15 --days 16 --mode court

# List all known rules
python3 plugins/ca-court-docs/scripts/case-calendar.py --rules
```

The script encodes Code Civ. Proc., §§ 12, 12a, 1013, 1010.6
and Govt. Code § 6700 holidays.

---

## Deadlines by procedural posture

### Initial response (defendant)

| Trigger | Deadline | Authority |
|---|---|---|
| Personal service (in California) | 30 calendar days from date of service | Code Civ. Proc., § 412.20(a)(3) |
| Service by mail within California (with acknowledgment) | 30 days from signing of acknowledgment | § 415.30(c) |
| Service by publication | 30 days from date of completion of publication | § 415.50 |
| Substituted service (deliver + mail) | 30 days from the date service was deemed complete (10 days after mailing date) | § 415.20(b); § 415.20(c) |
| Defendant served outside California | 40 calendar days | § 412.20(a)(4) |
| Demurrer overruled | 10 days after service of the ruling | § 430.30(c) |

### Motion practice — timing

| Event | Timing | Authority |
|---|---|---|
| Motion notice minimum | **16 court days** before hearing | Code Civ. Proc., § 1005(b) |
| Opposition deadline | **9 court days** before hearing | § 1005(b) |
| Reply deadline | **5 court days** before hearing | § 1005(b) |
| Service of motion (adds to above) | Mail: +5 calendar days; e-service: +2 court days | §§ 1013, 1010.6 |
| Meet-and-confer before demurrer | At least 5 days before demurrer deadline | § 430.41(a)(3) |
| Meet-and-confer before motion to strike | At least 5 days before MTS deadline | § 435.5(a)(3) |

**Practical note on motion notice**: if the motion is served by
mail (within California), the 16-court-day notice period is
extended by 5 calendar days under § 1013, making the minimum
notice effectively 16 court days + 5 calendar days.

### Case Management Conference (CMC)

| Event | Timing | Authority |
|---|---|---|
| CMC statement due | **15 calendar days** before the CMC | Cal. Rules of Court, rule 3.725 |
| CMC scheduling | Typically within 180 days of filing of complaint | CRC 3.722 |

### Discovery

| Event | Timing | Authority |
|---|---|---|
| Interrogatory response | 30 days after service; or 45 if served with complaint | Code Civ. Proc., § 2030.260(a) |
| RFP response | 30 days after service; or 45 if served with complaint | § 2031.260(a) |
| RFA response | 30 days after service; or 45 if served with complaint | § 2033.250(a) |
| Deposition notice — party | At least 10 days | § 2025.270(a) |
| Deposition notice — non-party (subpoena) | At least 15 days | § 2020.410(c) |
| Motion to compel further responses (after timely response) | **45 days** after service of response | § 2030.300(c); § 2031.310(c) |
| Discovery cutoff before trial | **30 days before trial** | § 2024.020(a) |
| Discovery motion cutoff | **15 days before trial** | § 2024.020(a) |
| Expert exchange | 50 days before trial (simultaneous) OR per court order | § 2034.230 |

### Summary judgment

| Event | Timing | Authority |
|---|---|---|
| MSJ/MSA notice | **75 days** before hearing date | Code Civ. Proc., § 437c(a)(2) |
| MSJ/MSA opposition | **14 days** before hearing | § 437c(b)(2) |
| MSJ/MSA reply | **5 days** before hearing | § 437c(b)(4) |
| MSJ/MSA filing cutoff | Must be heard at least **30 days** before trial (unless court allows later) | § 437c(a)(3) |

**Mail/e-service additions apply**: if the MSJ is served by mail,
add 5 calendar days to the 75-day notice period. If served by e-
service, add 2 court days.

### Post-judgment

| Event | Timing | Authority |
|---|---|---|
| Motion to vacate default (§ 473 discretionary) | Within **6 months** of entry of order/judgment | Code Civ. Proc., § 473(b) |
| Motion to vacate default (§ 473 mandatory, attorney fault) | Within **6 months** of entry | § 473(b) |
| Motion to vacate void judgment (§ 473(d)) | No time limit | § 473(d) |
| Motion for new trial | Within **15 days** of service of notice of entry of judgment | § 659 |
| Motion to vacate judgment after non-jury trial (§ 663) | Within **15 days** of service of notice of entry | § 663a |
| Notice of appeal (limited civil) | **30 days** from service of notice of entry of judgment | CRC 8.822 |
| Notice of appeal (unlimited civil) | **60 days** from service of notice of entry of judgment | CRC 8.104(a)(1) |
| Earnings withholding order — claim of exemption | **10 days** from service of the order on employer | Code Civ. Proc., § 706.104 |
| Bank levy — claim of exemption | **10 days** from service of notice of levy | § 703.520 |
| Acknowledgment of satisfaction — after demand | **15 days** from written demand | § 724.050(d) |
| Judgment renewal | Before original **10-year** period expires | § 683.130 |
| Statement of attorney fees (after judgment) | Per court order; typically 10 days | CRC 3.1702 |

### Arbitration

| Event | Timing | Authority |
|---|---|---|
| Mandatory settlement conference / arbitration (LASC) | Per court order | Local rules |
| Request for de novo trial after mandatory arbitration | **30 days** from notice of arbitration award | Code Civ. Proc., § 1141.20 |

---

## Statutes of limitations — California

### Contract and debt

| Claim type | SOL | Authority |
|---|---|---|
| Written contract | **4 years** | Code Civ. Proc., § 337(a) |
| Open book account / credit card | **4 years** (written contract theory) | § 337(a) |
| Oral contract | **2 years** | § 339(1) |
| Account stated | **4 years** | § 337(b) |
| Breach of warranty | **4 years** | Commercial Code, § 2725 |

### Tort

| Claim type | SOL | Authority |
|---|---|---|
| Personal injury | **2 years** | Code Civ. Proc., § 335.1 |
| Fraud / mistake | **3 years** from discovery | § 338(d) |
| Defamation | **1 year** | § 340(c) |

### Judgments

| Event | Limit | Authority |
|---|---|---|
| Judgment lifespan | **10 years** from entry | § 683.020 |
| Judgment renewal | Each renewal extends 10 years | §§ 683.110–683.220 |

### Consumer protection

| Claim type | SOL | Authority |
|---|---|---|
| Rosenthal FDCPA (Cal.) | **1 year** from violation | Cal. Civ. Code, § 1788.30(f) |
| FDCPA federal | **1 year** from violation | 15 U.S.C. § 1692k(d) |
| FCRA | 2 years from discovery; 5-year repose | 15 U.S.C. § 1681p |
| TILA | 1 year from violation (rescission: 3 years) | 15 U.S.C. § 1640(e); § 1635(f) |
| Unfair Competition Law (Bus. & Prof. Code § 17200) | **4 years** | Bus. & Prof. Code, § 17208 |
| Consumer Legal Remedies Act | **3 years** | Civil Code, § 1783 |

---

## Computing examples

### Example 1: Answer to complaint

Defendant personally served on **Wednesday, April 15, 2025**.

Code Civ. Proc., § 412.20(a)(3) — 30 calendar days.

Exclude April 15 (day of service). Start counting April 16.
30 days → **May 15, 2025** (Thursday). May 15 is a court day.

**Answer due May 15, 2025.**

### Example 2: Opposition to motion

Motion served by **mail** on **Friday, April 25, 2025**.
The hearing is set for **Monday, May 19, 2025**.

§ 1005(b) — opposition due 9 court days before hearing.

9 court days before May 19 = count back: May 18 (Sun — skip),
May 17 (Sat — skip), May 16 (1), May 15 (2), May 14 (3),
May 13 (4), May 12 (5), May 9 (6), May 8 (7), May 7 (8),
May 6 (9) = **May 6, 2025**.

Service was by mail (+5 calendar days). Does the mail extension
apply to the opposition deadline? No — the 5-day mail addition
applies to the time to respond to a served document, not to
the opposition deadline which is keyed to the hearing date. The
opposition remains due May 6.

**Opposition due May 6, 2025.**

### Example 3: Summary judgment timeline

Trial date: **Monday, September 8, 2025**.

MSJ notice must be at least 75 days before the hearing. The
last possible hearing date that is at least 30 days before trial
(September 8): on or before August 9, 2025.

Work backward from August 9: 75 days earlier = **May 26, 2025**
(Memorial Day — court holiday). Extend to next court day:
**May 27, 2025**.

MSJ must be **filed and served no later than May 27, 2025** for a
hearing on August 9.

Opposition due 14 days before August 9 = **July 26, 2025.**
Reply due 5 days before August 9 = **August 4, 2025.**

### Example 4: Notice of appeal (unlimited civil)

Judgment entered on the docket; notice of entry of judgment
served on **Friday, April 18, 2025**.

CRC 8.104(a)(1) — 60 days from service of notice of entry.

60 days from April 18 = June 17, 2025 (Tuesday).

**Notice of appeal due June 17, 2025.**

---

## Common deadline-computation mistakes

| Mistake | Consequence |
|---|---|
| Including the day of service | Off-by-one; early deadline |
| Forgetting the 5-day mail addition for § 1013 | Under-served opposition period |
| Confusing court days and calendar days | Wrong deadline (often shorter than actual) |
| Forgetting to extend for the holiday or weekend on the last day | Missed deadline |
| Confusing the 16-court-day motion notice rule with calendar days | Improperly noticed motion |
| Missing Cesar Chavez Day (March 31) — checking if court is open | Varies by court; verify |
| Missing the Day after Thanksgiving (some practitioners skip it) | Off by one day |
| Using 30-day summary judgment notice instead of 75-day California notice | Invalid MSJ; court may take it off calendar |

## When in doubt, file early

Late filings in California civil cases can be fatal — motions to
vacate, notices of appeal, and exemption claims all have strict
deadlines. Build a 5–7 day buffer whenever possible.

## Cross-references

- `scripts/case-calendar.py` — deterministic date arithmetic
- `ca-law-references/references/civil-rules.md` — CCP §§ 12, 12a,
  1005, 1013, 1010.6 verbatim
- `ca-law-references/references/ca-statutes-debt/` — SOL
  references
- `ca-first-30-days` — initial response workflow
- `ca-discovery` — discovery timeline

**NOT LEGAL ADVICE.** Generated content is a drafting aid;
verify against current rules and case law before filing.
