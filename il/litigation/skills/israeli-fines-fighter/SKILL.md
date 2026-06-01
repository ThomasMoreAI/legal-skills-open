---
name: israeli-fines-fighter
title: Israeli Fines Fighter
description: 'Appeal parking tickets and traffic fines in Israel: generates Hebrew appeal letters, explains deadlines, covers municipal fine codes, speed camera violations, and the points system. Use when a user receives a knasa (fine) and wants to understand their options, draft an appeal, or calculate penalty points. Helps users hit the 30-day cancellation window (bakasha le-bitul) AND the 90-day court-hearing window (bakasha le-hishafet), and avoid the +50% surcharge that kicks in after the 90-day mark.'
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-fines-fighter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: litigation
language: en
---

# Israeli Fines Fighter

## Problem

Getting fined in Israel is stressful and confusing. Parking tickets arrive with cryptic violation codes, traffic fines carry penalty points that accumulate toward license suspension, and there are TWO different appeal windows running in parallel for both fine types: a **30-day cancellation request (bakasha le-bitul)** to the prosecutor or municipality, and a **90-day court-hearing request (bakasha le-hishafet)** OR 30 days from the rejection of a cancellation request. After 90 days without action, a +50% surcharge kicks in, then +5% every additional 6 months. This skill helps users hit both windows, decide whether to appeal, and generate a proper Hebrew appeal letter with the right legal grounds.

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

After **day 90** without payment or appeal, the fine carries a **+50% surcharge**, with **+5% every additional 6 months**. The pre-2026 framing of "fine doubles after 30 days" is wrong: surcharge does not start at 30 days, and it is +50% (not 100%).

| Timeline | Status | Action |
|----------|--------|--------|
| **Day 0-30** | Both windows open | Best time to file בקשה לביטול. Many municipalities also offer a 25-50% early-payment discount in this window (varies by city). |
| **Day 31-90** | Cancellation window closed; court-hearing window still open | File בקשה להישפט before day 90, OR if a בקשה לביטול was rejected, file court request within 30 days of the rejection. |
| **Day 90+** | Both standard windows closed; +50% surcharge accrues | Late-appeal exceptions (איחור מוצדק) apply only for hospitalization, military reserve service, or being abroad (see Criminal Procedure Law § 230). Otherwise enforcement via Hotza'a Lapo'al, vehicle-registration block (ikuv rishum), additional fees. |

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

| Municipality | Online Portal | In-Person |
|-------------|--------------|-----------|
| Tel Aviv-Yafo | tel-aviv.gov.il (Resident Portal) | 110 Jerusalem Blvd, Jaffa |
| Jerusalem | jerusalem.muni.il | Safra Square, City Hall |
| Haifa | haifa.muni.il | 14 Hassan Shukri St |
| Other municipalities | Check municipal website for online appeal form | Visit city hall parking department |

**Traffic fine options:**
- **Pay the fine:** Online at gov.il (police fine payment service) or at any post office
- **Request a court hearing (bakasha lehisha'fet):** Submit within 90 days. You will receive a court date. You may represent yourself or hire a traffic lawyer (orech din letnu'a)
- **Online appeal (Tzav HaTzav):** Misrad Hatachburah's online traffic-appeal portal at `gov.il/he/service/objection_traffic_offense` accepts cancellation requests (bakasha le-bitul) and supporting evidence digitally
- **Plea bargain (hasdarei to'en):** Some offenses allow negotiating a reduced fine or fewer points through the prosecution

**Bakasha le-bitul vs. bakasha le-hishafet vs. ercaa (don't conflate these):**

| Step | Hebrew | What it is | When to use |
|---|---|---|---|
| 1. Cancellation request | בקשה לביטול | Administrative review by the prosecutor or municipality | First step. Submit within 30 days. No court fee. |
| 2. Court hearing request | בקשה להישפט | Moves the case to traffic court (or municipal court for parking) | After a cancellation is rejected (within 30 days of rejection), or directly within 90 days of receipt. No agra for filing the request itself. |
| 3. Appeal of verdict | ערעור (ercaa) | Appeal a court conviction or sentence to the district court | Only AFTER a court hearing produced a verdict you want to overturn. Agra applies; check `court.gov.il` for current rates. |

### Step 6: Point System Impact (Shitat HaNikud)

When the fine is a traffic violation, calculate the point impact:

| Points Accumulated | Consequence (per Traffic Regulations Part 14A) |
|-------------------|-------------|
| 12-22 points | Warning letter from licensing authority + driver risk assessment |
| 22-34 points | Mandatory basic safe-driving course (kurs yesodi) |
| 34-36 points | Advanced safe-driving course + theory re-test (kurs metkadem + ranan iyuni) |
| 36+ points (first time within 2 years) | 3-month license suspension + practical re-test |
| 36+ points (second time within 6 years) | 9-month license suspension + practical re-test |

Points expire only AFTER any required courses/tests are completed, on a tiered schedule tied to total accumulated count (not severity of the underlying offence). Without completing the required course, points do not expire. See `kolzchut.org.il` ("שיטת הניקוד בעבירות תנועה") for the canonical scheme.

**Common violation point values:**

| Violation | Fine (NIS) | Points |
|-----------|-----------|--------|
| Running a red light | 1,000 | 10 |
| Speeding 21-30 km/h over limit (urban) | 750 | 8 |
| Speeding 31-40 km/h over limit (urban) | 1,500 | 10 |
| Using mobile phone while driving | 1,000 | 8 |
| Not wearing seatbelt | 250 | 2 |
| Illegal overtaking | 500-1,000 | 6-8 |

Note: Fine amounts are updated periodically by ministerial order. Always verify current amounts on gov.il. The amounts above are approximate as of early 2026.

## Gotchas

1. **Municipal vs. police fines are different legal processes.** Parking tickets from a municipal inspector (paqach) follow the municipal appeal process (bakasha leitul). Traffic fines from police or cameras follow criminal traffic law (breirot mishpat). Mixing up the appeal process wastes the deadline.

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
| gov.il/he/service/objection_traffic_offense | Misrad Hatachburah online traffic-appeal portal (Tzav HaTzav). May show 403 to scripted clients; loads normally in a browser. |
| gov.il/he/service/police_fine_payment | Police fine payment service. Same WAF behaviour as above. |
| court.gov.il | Israeli courts directory (find your local traffic court / שלום מקומי court). |
| mot.gov.il | Misrad Hatachburah (Ministry of Transport) homepage. |
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

The pre-2026 "fine doubles after 30 days" framing is incorrect. The actual rule:
- Past day 90 without payment or appeal: **+50% surcharge** (not +100%, not at day 30).
- Past 6 months thereafter: **+5% every additional 6 months**.
- Possible additional collection fees, vehicle-registration block (ikuv rishum), and enforcement via Hotza'a Lapo'al.

If still within the 30-day cancellation window or 90-day court window, file the appropriate request immediately. After day 90, late-appeal exceptions (איחור מוצדק) apply only for hospitalization, active reserve service, or being abroad (see Criminal Procedure Law § 230), and you must document the cause.

### "I got a camera fine but I wasn't driving"
The vehicle owner must submit a statutory declaration (tatzir) identifying the actual driver. This transfers liability. The declaration must be submitted within 90 days and include the other driver's full name and ID number.

### "I want to go to court over a parking fine"
Parking fines in Israel are administrative, not criminal. The appeal goes to the municipality, not a court. If the municipal appeal is rejected, the next step is filing an administrative appeal (erur minhal'i) with the local court, but this is rarely cost-effective for small fines.

### "How much does a traffic lawyer cost?"
Traffic lawyers in Israel typically charge 1,500-5,000 NIS depending on the violation severity. For minor fines under 500 NIS, self-representation is usually more economical. For fines with 10+ points or license suspension risk, a lawyer may be worthwhile.
