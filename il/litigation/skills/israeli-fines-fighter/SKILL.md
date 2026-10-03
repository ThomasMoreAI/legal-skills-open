---
name: israeli-fines-fighter
title: Israeli Fines Fighter
description: 'Appeal parking tickets, traffic fines and bus-lane (nat"z) tickets in Israel: generates Hebrew appeal letters, explains deadlines, and covers the administrative track under the Administrative Traffic Violations Law (hasagah 30 days, arar to the traffic tribunal 90 days, no request to be tried), why a nat"z ticket is not a parking ticket, why a municipal ticket cannot be converted to a warning, the points system, and when the late-payment surcharge can be waived. Use when a user receives a knasa (fine) and wants to understand their options, draft an appeal, or calculate penalty points.'
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-fines-fighter
license: MIT
version: 0.1.2
execution_mode: open
jurisdiction: il
practice: litigation
language: en
sources:
- title: Appeal grounds
  path: references/appeal-grounds.md
- title: Fine types
  path: references/fine-types.md
---

# Israeli Fines Fighter

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Problem

Getting fined in Israel is stressful and confusing. Parking tickets arrive with cryptic violation codes, traffic fines carry penalty points that accumulate toward license suspension, and there are TWO different appeal windows running in parallel for both fine types: a **30-day cancellation request (bakasha le-bitul)** to the prosecutor or municipality, and a **90-day court-hearing request (bakasha le-hishafet)** OR 30 days from the rejection of a cancellation request. Once the payment date passes without payment or an appeal, a statutory late-payment addition (tosefet pigur) plus interest starts accruing on the fine. This skill helps users hit both windows, decide whether to appeal, and generate a proper Hebrew appeal letter with the right legal grounds.

## Instructions

### Step 1: Identify the Fine Type

Ask the user for the fine details. Israeli fines fall into two main categories:

| Type | Issued By | Hebrew Term | Appeal To |
|------|-----------|-------------|-----------|
| **Parking fine** (knasa chanaya) | Municipal inspector (paqach) | קנס חנייה / דוח חנייה | Municipality (iriya) |
| **Traffic fine** (knasa tnu'a) | Police officer or camera | קנס תנועה / דוח תנועה | Police prosecution (tvia'a) or traffic court |

Key details to collect:
- Fine number (mispar hadoch)
- Date received
- Violation code or description
- Amount in NIS
- Issuing authority (municipality name or "Israel Police")
- Location where the violation occurred
- Whether the user was driving or the vehicle owner

### Step 2: Assess the Deadline

There are TWO appeal mechanisms with separate deadlines, applicable to BOTH parking fines and traffic fines:

| Window | Mechanism | Hebrew | Submitted To |
|---|---|---|---|
| **30 days from receipt** | Cancellation request (essentially clerk review) | בקשה לביטול / בקשת בירור | Municipality (parking) or Police prosecutor (traffic) |
| **90 days from receipt** OR **30 days from rejection of a cancellation request** | Court hearing request | בקשה להישפט | Traffic court / municipal court |

Once the payment date on the notice passes without payment or an appeal, a statutory **late-payment addition (tosefet pigur)** plus interest starts accruing. The common framing of "the fine doubles after 30 days" is wrong: the addition is not a doubling and it does not start at day 30. Check the exact current balance with the Fines Collection Center (HaMerkaz LeGviyat Knasot) or on the payment notice itself rather than quoting a percentage.

| Timeline | Status | Action |
|----------|--------|--------|
| **Day 0-30** | Both windows open | Best time to file בקשה לביטול. Some municipalities offer an early-payment discount in this window. Whether one exists, and how much it is, is set per municipality, so check the notice or the municipality's own page rather than assuming a rate. |
| **Day 31-90** | Cancellation window closed; court-hearing window still open | File בקשה להישפט before day 90, OR if a בקשה לביטול was rejected, file court request within 30 days of the rejection. |
| **Day 90+** | Both standard windows closed; late-payment additions accrue | A late request is considered only where the delay itself is justified and documented (for example hospitalization, active reserve service, or being abroad). Otherwise enforcement via Hotza'a Lapo'al, vehicle-registration block (ikuv rishum), additional fees. |

**For parking fines:** the 30-day clock starts from the date the ticket was placed on the vehicle OR the date a notice was mailed to the registered owner.

**For traffic fines (breirot mishpat):** by default the fine becomes a court conviction at day 90 if no בקשה להישפט was filed.

### Step 3: Evaluate Appeal Grounds

Not every fine is worth appealing. Help the user assess their case:

**Strong grounds for parking fine appeals:**

| Ground | Hebrew Term | Evidence Needed |
|--------|-------------|-----------------|
| Missing or obscured signage | שלט חסר / שלט מוסתר | Photos of the location showing no sign or blocked sign |
| Broken parking meter | מדחן תקול | Photo of meter showing error, receipt attempts |
| Medical emergency | מצב חירום רפואי | Medical documentation with date/time |
| Loading/unloading (commercial) | פריקה וטעינה | Business delivery documentation |
| Incorrect vehicle details on ticket | פרטים שגויים בדוח | The ticket itself showing wrong plate number, color, or make |
| Ticket issued outside enforcement hours | מחוץ לשעות אכיפה | Photo of sign showing hours vs. ticket timestamp |
| Disabled parking permit (valid) | תג נכה בתוקף | Copy of valid disabled parking permit |

**Strong grounds for traffic fine appeals:**

| Ground | Hebrew Term | Evidence Needed |
|--------|-------------|-----------------|
| Vehicle was sold before violation date | הרכב נמכר | Sale contract (heskhem mechira) with date |
| Vehicle was stolen | הרכב נגנב | Police report (tlunat mishtara) |
| Camera malfunction | תקלה במצלמה | Request calibration records from police |
| Emergency circumstances | נסיבות חירום | Documentation (medical records, police report) |
| Driver was someone else (owner liability) | נהג אחר | Statutory declaration (tatzir) identifying the actual driver |

**Weak grounds (usually rejected):**
- "I didn't see the sign" (ignorance of signage is not a defense)
- "I was only parked for a minute" (duration is irrelevant)
- "Everyone parks there" (common practice is not a legal defense)
- "The meter app crashed" (use physical payment as backup)

### Step 4: Generate the Appeal Letter

**For parking fines (bakasha leitul knasa chanaya):**

The appeal letter must be in Hebrew and include:

```
לכבוד
עיריית [שם העירייה]
מחלקת חניה / אגף אכיפה

הנדון: בקשה לביטול דוח חניה מספר [FINE_NUMBER]

1. פרטי הדוח:
   - מספר דוח: [FINE_NUMBER]
   - תאריך: [DATE]
   - מיקום: [LOCATION]
   - מספר רכב: [PLATE_NUMBER]

2. נימוקי הבקשה:
   [SPECIFIC LEGAL GROUNDS - see Step 3]

3. ראיות מצורפות:
   [LIST ATTACHED EVIDENCE]

4. בקשה:
   לאור האמור לעיל, אבקש לבטל את הדוח / להפחית את הקנס.

בכבוד רב,
[NAME]
[ID_NUMBER]
[PHONE]
[DATE]
```

**For traffic fines (bakasha lehisha'fet):**

Traffic fine appeals go to the prosecution or court. The letter structure differs:

```
לכבוד
תביעות משטרת ישראל / בית המשפט לתעבורה

הנדון: בקשה להישפט בגין דוח תנועה מספר [FINE_NUMBER]

אני הח"מ [NAME], ת.ז. [ID], מבקש/ת להישפט על דוח תנועה מספר [FINE_NUMBER]
שניתן בתאריך [DATE].

נימוקים:
[SPECIFIC LEGAL GROUNDS]

[NAME]
[DATE]
```

### Step 5: Submission Guidance

**Parking fine appeals -- submission channels by municipality:**

| Municipality | Online route |
|-------------|--------------|
| Tel Aviv-Yafo | `tel-aviv.gov.il`. The objection form covering BOTH parking and nat"z is at `www5.tel-aviv.gov.il/TlvFormCollection/Parking/ObjectionReport/` (verified 2026-08-13). |
| Jerusalem | `jerusalem.muni.il` (bot-blocked to scripted clients; loads in a browser). |
| Haifa | `haifa.muni.il` (verified 2026-08-13). |
| Any other municipality | Use the address and channel printed ON THE TICKET, or the municipality's own site. |

**Do not quote a municipal street address from memory.** Counter desks and department
addresses move, and the address that binds is the one printed on the ticket. (Earlier versions of
this skill listed walk-in addresses that could not be verified against the municipalities' own
pages.) Direct the user to the ticket or the municipal site instead.

**Before anything else: paying the fine ENDS the case against you.**

Under s.229(h) of the Criminal Procedure Law, a person who pays the fine "רואים אותו כאילו הודה
באשמה בפני בית המשפט, הורשע ונשא את עונשו" - they are treated as having confessed, been convicted
and served the sentence. Payment therefore forfeits every route below AND records the penalty points.
Never let a user pay "to be safe" while an appeal is pending, and never present the early-payment
discount as compatible with appealing: they are mutually exclusive choices. The only exceptions are
where the prosecutor later cancels the notice under s.229(c), or where the court agrees to hear a
late request to be tried under s.230.

**Traffic fine options:**
- **Pay the fine** (only when the user has decided NOT to contest, see above): Online at gov.il (police fine payment service) or at any post office
- **Cancellation request (bakasha le-bitul):** For police/camera traffic fines the cancellation request goes to the **Driver Inquiries Center (Merkaz Pniyot Nehagim, מפנ"א)** of the traffic prosecution, not to a generic "police station". Camera (A3 / דוח מצלמה) fines route through מפנ"א.
- **Request a court hearing (bakasha lehisha'fet):** Submit within 90 days. This is the route for offences still on the criminal-procedure track. For offences that have moved to the administrative track (see below), a request to be tried is no longer available at all: the route is hasagah then arar.
- **Administrative track (Administrative Traffic Violations Law, 5784-2024) -- staged, and stage 2 is now live.** Its s.47(c) rolls breirot mishpat into an administrative regime in two stages, counted from the commencement date of **8 February 2026**:

  | Stage | In force | Scope per s.47(c) |
  |---|---|---|
  | 1 | 8 February 2026 | Violations whose First Schedule fine is **100 to 500 NIS**, **excluding** Traffic Regulation 54 (speeding) |
  | 2 | 8 August 2026 | Violations whose fine is **750 to 1,500 NIS**, **and** Regulation 54 speeding offences |

  Both stages are now in effect, so the "tribunal cannot hear speeding / only up to 500 NIS" limitation that applied during stage 1 no longer holds. Verify against the notice itself, which states which track it is on.

  **The date that decides the track is the OFFENCE date, not today's date. Get this wrong and you send the user to the wrong forum.** Under the Law's transitional provision, it does not apply to a breirat mishpat offence committed before the relevant stage date ("הוראות חוק זה לא יחולו לגבי עבירה של ברירת משפט ... שעבר אדם ערב יום התחילה"); those offences stay on the Criminal Procedure Law / Traffic Ordinance track as it stood before, which means bakasha le-bitul and bakasha le-hishafet, not hasagah and arar. So a 1,000 NIS ticket for an offence committed in May 2026 is still criminal-track (its band only crossed over on 8 August 2026), while the same ticket for an offence in September 2026 is administrative. Always ask for the offence date before routing the user.

  On the administrative track the two steps are renamed and re-timed:
  - **hasagah (השגה)** to the competent authority, within **30 days** of service (s.8(a)). If the ground is that the violation was not committed by you (Traffic Ordinance s.27B), the window is **90 days**. The authority must decide within 45 days (s.8(c)).
  - **arar (ערר)** to the traffic tribunal, within **90 days** of service, or within **30 days** of the decision on a hasagah (s.19(b)). Filing an arar bars a later hasagah on the same decision (s.8(d)).

  You may represent yourself or hire a traffic lawyer (orech din letnu'a).
- **Online submission:** the national Driver Inquiries Center (מפנ"א) service is run by **Israel Police**, not the Ministry of Transport, at `gov.il/he/service/drivers_inquiries_forms` ("פנייה למרכז פניות נהגים ארצי"). It takes the report number, the purpose of the request, and supporting documents. There is no service called "Tzav HaTzav"; earlier versions of this skill invented that name and an `objection_traffic_offense` URL that does not exist.
- **Plea bargain (hasdarei to'en):** Some offenses allow negotiating a reduced fine or fewer points through the prosecution

**Bus-lane fines (nat"z, נת"צ) are their own track. Do not treat them as parking tickets.**

Driving in a public-transport lane is not a parking offence, even though the ticket often arrives from the municipality. Getting this wrong sends the user down the parking route and burns the deadline.

| Question | Answer |
|---|---|
| What is the offence? | Failure to obey signs 501 / 503 (public-transport lane) under Traffic Regulation 22(a). Sign 503 marks the lane; sign 501 states who may use it. Where no 501 is posted, only public-service vehicles may drive in it. |
| Statutory fine | **500 NIS** (First Schedule to the Administrative Traffic Violations Law, item 24). Press reports of higher figures usually describe aggravating circumstances or a different offence. |
| Who enforces it? | Usually a **local authority**, not the police, via fixed cameras. The camera power is Traffic Ordinance s.27A1, and the enforcing municipal employee is a "mefake'ach" under s.28(b) of the Administrative Traffic Violations Law. |
| Which track? | At 500 NIS and not a Regulation 54 offence, it entered the **administrative track in stage 1 (8 February 2026)**. So: **hasagah then arar, and there is no request to be tried.** |
| Can it be converted to a warning? | **Not on the administrative track.** For an offence committed BEFORE it crossed over, see the warning subsection below. |

**Time limits on ISSUING the ticket, the ground most often missed.** These bite hardest on exactly
the camera tickets that arrive months late:

| Situation | Limit on serving a fine notice | Source |
|---|---|---|
| Camera-based traffic offence under Traffic Ordinance s.27A or s.27A1 (this includes nat"z cameras) | **4 months** from the offence | s.225A(a1)(1) CPL |
| Fine offence generally | **1 year** from the offence | s.225A(a) CPL |
| Owner proved they were not liable under s.27B, so the actual driver is pursued | 1 year from the offence, or 3 months from that proof, whichever is later, capped at 2 years | s.225A(a2) CPL |

If the notice was served outside these windows, say so first: it disposes of the ticket without
argument about signage. Always ask when the offence occurred AND when the notice was served.

Grounds that actually work on a nat"z ticket are substantive, not discretionary: missing, contradictory or unclear signage; faded lane markings; a lane marked as public-transport that also carries a turn arrow permitting all vehicles to turn (a recurring complaint in Tel Aviv); a defect in the notice or in the image; or transferring liability to the actual driver. Check these first, because each disposes of the ticket
outright: whether the vehicle was permitted in the lane at all (sign 501 commonly permits taxis, and
motorcycles in some cities), whether the lane was in force at that hour, and whether this was lawful
use rather than a violation (sign 503 permits "רכב הפונה בצומת הקרוב"). Full list with sources:
`references/appeal-grounds.md`, "Bus-lane (nat"z) grounds".

**"Convert it to a warning" (hamara le-azhara) -- know where this does NOT apply.**

Converting a fine to a warning is a **police discretionary practice** for breirot mishpat, requested through the Driver Inquiries Center (מפנ"א). It is a discretion, never an entitlement. Where it does and does not exist:

| Track | Warning available? |
|---|---|
| Criminal track (breirat mishpat: offence committed before its band crossed over) | Yes, as a discretionary practice. The statutory hook for dropping the case is s.229(c) CPL, which lets a prosecutor cancel a fine notice where "נסיבות העניין בכללותן אינן מתאימות להמשך קיום ההליכים". |
| Administrative track | No. The Administrative Traffic Violations Law does not contain the word "azhara" at all; its remedies are hasagah and arar. |
| Municipal parking | No warning tier. The municipality either cancels the ticket or does not. |

Because the track is fixed by the OFFENCE date, a nat"z or other municipal ticket for an offence
committed before its band crossed over is still criminal-track, so the request is not pointless there.
Deemed conviction and collection run for months, so such tickets are still live. Establish the offence
date before telling a user the route is closed to them.

Do NOT state numeric eligibility criteria (years of licence held, years since the last conviction). Published law-firm summaries disagree with each other on these numbers and no authoritative public source sets them out, so quoting one would be fabrication. Describe the mechanism qualitatively, say it is discretionary, and route the user to מפנ"א.

**Bakasha le-bitul vs. bakasha le-hishafet vs. ercaa (don't conflate these):**

| Step | Hebrew | What it is | When to use |
|---|---|---|---|
| 1. Cancellation request | בקשה לביטול | Administrative review by the prosecutor or municipality | First step. Submit within 30 days. No court fee. |
| 2. Court hearing request | בקשה להישפט | Moves the case to traffic court (or municipal court for parking) | After a cancellation is rejected (within 30 days of rejection), or directly within 90 days of receipt. No agra for filing the request itself. |
| 3. Appeal of verdict | ערעור (ercaa) | Appeal a court conviction or sentence to the district court | Only AFTER a court hearing produced a verdict you want to overturn. Agra applies; check `court.gov.il` for current rates. |

### Step 6: Point System Impact (Shitat HaNikud)

When the fine is a traffic violation, calculate the point impact:

| Valid points recorded | Corrective measure, per Traffic Regulation 549 |
|-------------------|-------------|
| 12-22 | Basic safe-driving course from the Licensing Authority + pass its test (reg. 549(a)) |
| 24-34 | Advanced safe-driving course + pass its test. Cannot be taken before completing the basic course from the tier above (reg. 549(b)) |
| 36+ | 3-month licence suspension; the Licensing Authority renews the licence at the end of the period (reg. 549(c)) |
| **72+**, OR 36+ again within 6 years of the last offence that caused a 549(c) suspension | 9-month suspension, renewed only after medical examinations by the authorised physician and the tests under regs. 202-210 (reg. 549(d)) |

Three things this table is deliberately precise about, because the common write-ups get them wrong:

- **The 36+ tier carries no theory test.** Reg. 549(c) imposes the suspension and provides for renewal at the end of it, nothing more. Do not tell a user they must re-qualify at this tier.
- **The 9-month tier has two independent triggers**, and the 72-point one is usually omitted: a driver reaching 72+ valid points hits it directly, without any prior suspension.
- Measures are cumulative (reg. 549(e)), the same measure is not imposed twice for the same points (reg. 549(f)), and a repeat of the same training cannot be required before a year has passed (reg. 549(b1)).

There is no "warning letter" tier and no standalone "theory re-test at 34-36" tier.

**Point validity clock.** Points run from the **offence date**. The base period is **2 years** (reg. 547(b)). It becomes **4 years** where a driver accumulated **22 points or more within less than two years** (reg. 547(c)) - the trigger is 22 within a short window, not "more than 20". From **21.5.2027** the base period splits: 1 year for offences carrying up to 6 points, 2 years for 8 or more (reg. 547(b)(1)-(2)). Expiry is ALSO conditioned on completing any required measures (course/test/suspension): if the driver has not completed the imposed measure, the points (and the obligation) do not lapse when the clock runs out. So both conditions must be met, the validity window elapsed AND the required measures completed.

**Common violation point values:**

| Violation | Points | Regulation |
|-----------|--------|-----------|
| Running a red light | 10 | 22(a) |
| Speeding 21-30 km/h over limit (urban) | 8 | 54(a) |
| Speeding 31-40 km/h over limit (urban) | 10 | 54(a) |
| Using mobile phone while driving, not hands-free | 8 if the offence was before 20.8.2026, 10 from 20.8.2026 | 28(b)(1)(a) |
| Driver not wearing seatbelt | 6 | 83a(b) |
| Passenger not wearing seatbelt | 2 | 83b(a) |
| Illegal overtaking | 4-10, depending on the specific offence | 47 |

Point values are read from the Ministry of Transport's offence-code table
([tavlat simlei averot](https://data.gov.il/he/datasets/ministry_of_transport/tavlat-simlei-averot)),
which is the authoritative list and carries a points column per offence code. Overtaking spans
the widest band: overtaking on the right is 4, overtaking before a crossing is 6, in poor
visibility 8, and crossing a solid line or when the road is not clear is 10. Ask which one the
notice actually cites rather than assuming.

**This table deliberately does not list fine amounts.** Amounts are set by ministerial order,
are index-linked, and differ between the police track and municipal parking, so any figure
written here would be wrong for some readers and stale for the rest. Read the amount off the
user's own notice, which is authoritative for their case. This is the same rule as Gotcha 4
below.

## Gotchas

1. **Municipal vs. police fines are different legal regimes.** Parking tickets from a municipal inspector (paqach) follow the municipal objection route (bakasha le-bitul to the municipality, and a request to be tried if it is rejected); the online traffic tribunal has no jurisdiction over municipal parking tickets. Traffic fines from police or cameras are **breirot mishpat** on the criminal-procedure track. The 30-day / 90-day mechanics in Step 2 mirror each other in practice, but the two tracks rest on different statutes, so a parking case that reaches court goes to the administrative-affairs track, not the traffic court. Mixing up the appeal route wastes the deadline.

2. **The 30-day and 90-day deadlines are from receipt date, not violation date.** For mailed notices, receipt date is presumed to be a few days after mailing. If the user says "I got a fine from 2 months ago," clarify when they actually received the notice.

3. **Owner liability (achrayut ba'alim) is the default for camera fines.** The registered vehicle owner receives camera fines regardless of who was driving. The owner can transfer liability by submitting a statutory declaration (tatzir) naming the actual driver within 90 days.

4. **Do NOT fabricate fine amounts.** Israeli fine amounts change by ministerial order and vary by municipality for parking violations. Always advise users to check the amount on their actual fine notice rather than relying on fixed numbers. The amounts in this skill are approximate guidelines.

5. **Appeals are municipality-specific.** Each Israeli municipality has its own appeal form, portal, and process. Do not assume Tel Aviv's process works for Jerusalem or Haifa. Always direct the user to their specific municipality's website.

6. **Hotza'a Lapoal (collection enforcement) typically triggers after roughly 12 months unpaid**, when the Centre for Collection of Fines (Merkaz Geviya / CEC, part of the Ministry of Justice) opens an execution file. Once that happens, ignoring the file leads to bank-account / wage seizure, license suspension, and travel block. To oppose execution, file a **התנגדות לביצוע (objection to execution)** within 30 days of being served. To negotiate, contact the CEC directly to set up a payment plan (haseder tashlumim). At this stage the original cancellation / court-hearing windows are closed; only "justified-delay" exceptions (איחור מוצדק) can reopen the underlying fine.

7. **Court fees (agra):** filing a בקשה להישפט or a בקשה לביטול itself does not carry an agra (filing is free). An agra applies only at the ercaa stage if you appeal a conviction. Exact 2026 amounts vary; check `court.gov.il` for current rates rather than quoting a number.

## Examples

### End-to-end: parking fine on a red-and-white curb with a fallen sign

User received a 250 NIS parking ticket yesterday for parking near a red-and-white painted curb. The user has a phone photo showing the "no parking" pole lying flat on the sidewalk at the time of the violation.

1. **Identify fine type.** Issued by a municipal pakach -> parking fine (knasa chanaya). Appeal goes to the municipality, not the police.
2. **Check deadline.** Day 1 of 30: cancellation window (bakasha le-bitul) is wide open. 90-day court window also open.
3. **Choose route.** Strongest first step is a bakasha le-bitul to the municipality with the photo evidence. Going straight to court (bakasha le-hishafet) is overkill at this stage.
4. **Cite legal basis.** Israeli traffic signage rules require visible signage at the point of enforcement. A toppled sign creates a reasonable defence of "missing or obscured signage" (שלט חסר / שלט מוסתר) under the general signage requirements in the Traffic Regulations (Takanot HaTetzu'ah). Don't fabricate a specific clause number; just frame it as "the sign was not visible at the time of the violation, contrary to the signage requirements of the Traffic Regulations."
5. **Draft the letter.** Use the parking-fine template in Step 4. Fill in fine number, plate, date, location, attach the photo plus a timestamp (EXIF if available), state the ground in one paragraph, sign and date.
6. **Submit.** Upload via the municipal online portal (e.g. `tel-aviv.gov.il` Resident Portal). Keep the submission confirmation number. If no answer in 90 days, the municipality is required to either cancel the fine or notify the user that it stands.
7. **If rejected:** within 30 days of the rejection letter, file a בקשה להישפט to move the case to municipal/local-affairs court.

## Reference Links

| Link | What it is |
|---|---|
| gov.il/he/service/drivers_inquiries_forms | Israel Police, national Driver Inquiries Center (מפנ"א) request service. Verified 2026-08-13. Shows 403 to scripted clients; loads normally in a browser. |
| gov.il/he/service/police_fine_payment | Police fine payment service. Same WAF behaviour as above. |
| www.court.gov.il | Israeli courts directory (find your local traffic court / שלום מקומי court). Use the `www.` host; the bare `court.gov.il` does not resolve cleanly. Verified 2026-08-13: the host resets scripted connections and did not load in a headless browser either, so treat it as human-browser-only and do not report it as down to the user without checking yourself. |
| gov.il (search "משרד התחבורה") | Ministry of Transport content now lives under gov.il; the legacy `mot.gov.il` host is deprecated. |
| kolzchut.org.il (search "שיטת הניקוד בעבירות תנועה") | Canonical citizens-rights write-up of the penalty-point scheme. |
| nevo.co.il (search "פקודת התעבורה") | Free public mirror of the Traffic Ordinance and Criminal Procedure (Traffic Offences) regulations. |

## Bundled Resources

### references/

- `appeal-grounds.md` -- Comprehensive list of valid appeal grounds with legal basis
- `fine-types.md` -- Israeli fine categories, violation codes, and amount ranges

### scripts/

- `deadline-calculator.py` -- Calculate remaining days in appeal window based on fine date

## Troubleshooting

### "My fine grew because I missed a deadline"

The "fine doubles after 30 days" framing is incorrect. The rule depends on which track the fine is on:

- **Administrative track** (Administrative Traffic Violations Law): the late-payment addition (tosefet pigur) is **30% of the unpaid fine**, a single addition, per s.10(b)(1), plus shekel interest and late-payment charges under s.10(b)(2). It attaches after the payment date in s.8(c) / 9(a) / 19(d), not at day 30.
- **Criminal track** (breirot mishpat not moved across): additions under s.229(b) CPL and s.67 of the Penal Law, with a written waiver request under s.229(f)-(g). Details in `references/fine-types.md`.
- Either way: possible collection fees, vehicle-registration block (ikuv rishum), and enforcement via Hotza'a Lapo'al.

**Waiver of the surcharge on municipal fines (worth asking for, and widely unknown).** For a fine imposed by a municipal inspector under s.28 (this includes nat"z camera fines), s.10(c) lets the competent authority exempt the person from the late-payment addition, in whole or in part, where the failure to pay on time was for a reason beyond their control, or where the surcharge arose from a malfunction of a state or municipal authority. The request must be in writing (s.10(d)).

If still within the 30-day cancellation window or 90-day court window, file the appropriate request immediately.

After the windows close, a late request to be tried is still possible in limited cases (s.229(h2), s.230, s.229(e) CPL). See `references/fine-types.md`.

### "I got a camera fine but I wasn't driving"
The vehicle owner must submit a statutory declaration (tatzir) identifying the actual driver. This transfers liability. The declaration must be submitted within 90 days and include the other driver's full name and ID number.

### "I want to go to court over a parking fine"
A municipal parking ticket is a **breirat kenas under the Criminal Procedure Law**, not an
administrative-affairs matter. The first step is a בקשה לביטול to the municipality. If that is
rejected, the next step is a **בקשה להישפט**, which moves the case to בית משפט לעניינים מקומיים as a
criminal-procedure hearing. It is NOT an erur minhali to an administrative-affairs court. For small fines this is often not cost-effective, but the route
is the one above.

### "How much does a traffic lawyer cost?"
Traffic-lawyer fees are not published and vary widely by severity and by firm, so get a quote before deciding rather than working from a figure. The decision rule matters more than the price: for a low-value fine carrying few or no points, self-representation is usually the better trade, while a fine carrying 10 points, or any real risk of licence suspension, is where representation starts to pay for itself.
