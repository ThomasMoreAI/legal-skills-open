# Numerical sanity checks

## Dmei havra'a: full seniority ladder (private sector)

Nothing is owed before 12 months of service. On completing year 1 the employee is paid for 5 days.

| Seniority | Days |
|---|---|
| Year 1 | 5 |
| Years 2-3 | 6 |
| Years 4-10 | 7 |
| Years 11-15 | 8 |
| Years 16-19 | 9 |
| Year 20+ | 10 |

Rate: 451.5 NIS/day private sector, 511.6 NIS/day public sector. Public-sector and some
sectoral agreements use their own, higher day tables; do not reuse the private ladder there.

## Job scope pro-rates almost everything

Ask for the employment scope (`heikef misra`) before running any of the checks below. Vacation,
dmei havra'a, the pension base, sick accrual and the minimum-wage floor all pro-rate to scope.
Running the monthly minimum-wage floor against a part-time contract without pro-rating it first produces a false blocker.

Compute these from the contract figures and flag anomalies. Every NIS figure below moves on a fixed calendar: minimum wage every April, private-sector havra'a every July, the average wage and the tax ceilings every January. Re-verify against the Reference Links in SKILL.md before quoting one as current.

Compute these from the contract figures and flag anomalies:

| Check | Formula | Expected |
|-------|---------|----------|
| Minimum wage floor | Stated gross monthly salary (or hourly rate) | At least 6,443.85 NIS/month full-time as of 1 April 2026. Hourly minimum is 35.40 NIS/hour for a 182-hour month, or 34.64 NIS/hour for a 186-hour month. Below this is a blocker. Verify the current rate |
| Employer pension contribution | Claimed % of gross | At least 6.5% benefits + 6% severance (mandatory minimum; with employee 6% this is 18.5% total). 8.33% severance is only required to fully fund a Section 14 waiver, not as a legal floor |
| Employee pension contribution | Claimed % of gross | 6% is the mandatory MINIMUM, not a maximum. 7% is common and is the rate at which the Section 45a tax credit is optimised; above 7% the extra earns no credit |
| Pension salary base | Wording of the salary the rates apply to | The Expansion Order compels contributions only on the LOWER of the employee's base gross or the average wage in the economy (13,769 NIS/month in 2026). A contract saying "pension in accordance with law" on a salary above the ceiling lawfully funds only the part up to it. Major, and expensive: require "contributions computed on full gross salary with no ceiling" |
| Keren hishtalmut split | Employer / employee % | Standard 7.5% / 2.5% |
| Total employer cost | Gross + 6.5% + severance + 7.5% KH + BL employer | Approx 120-125% of gross; above this suggests items already deducted from gross |
| Hoda'at mukdemet days | Days in contract | At least statutory minimum by tenure (see reference) |
| Annual vacation | Days in contract | Two ladders apply and the employee takes the HIGHER. Annual Leave Law s.3(a) states GROSS days (including weekly rest): 16 for each of the first 5 years, 18 in year 6, 21 in year 7, then one more per year up to 28. The Shortened Work Week extension order, which covers most 5-day workplaces, states NET days: 12 for years 1-5, 17 for years 6-8, 23 from year 9. So a year-9 employee on a 5-day week is entitled to 23 net days, not the 15 the statute alone yields. The order does NOT cover domestic work, workplaces with fewer than 4 employees, government and municipal companies, or workplaces whose 5-day week is set by a collective agreement |
| Sick days | Days in contract | Accrual is 1.5 days per full month, capped at a 90-day cumulative balance. There is NO 18-day annual cap: 18 is just 1.5 x 12, and an employee may use more than 18 in a year against the accrued balance. The material term is the ladder: day 1 unpaid, days 2-3 at half pay, day 4 onward at full pay (Sick Pay Law 1976 ss.2, 5). A contract paying from day 1 is above the floor and worth negotiating for |
| Dmei havra'a | Day count and rate in contract | Nothing is owed before 12 months of service; on completing year 1 the employee is paid for 5 days, rising to 10 days at 20+ years, at 451.5 NIS/day private sector (511.6 public). Below this is a major finding |

---

## גרסה עברית

חשבו וסמנו חריגות:

| בדיקה | נוסחה | מצופה |
|-------|-------|-------|
| רף שכר מינימום | שכר חודשי ברוטו מוצהר (או תעריף שעתי) | לפחות 6,443.85 ש"ח לחודש למשרה מלאה נכון ל-1 באפריל 2026. שכר המינימום לשעה הוא 35.40 ש"ח לחודש של 182 שעות, או 34.64 ש"ח לחודש של 186 שעות. מתחת לזה זה חוסם. כדאי לאמת את התעריף העדכני |
| הפרשת פנסיה מעסיק | % מוצהר מהברוטו | לפחות 6.5% תגמולים + 6% פיצויים (המינימום החוקי; עם 6% עובד זה 18.5% בסך הכל). רכיב פיצויים של 8.33% נדרש רק כדי לממן ויתור סעיף 14 במלואו, לא כרצפה חוקית |
| הפרשת פנסיה עובד | % מוצהר מהברוטו | 6% הוא המינימום החוקי, לא מקסימום. 7% נפוץ והוא השיעור שממצה את זיכוי המס לפי סעיף 45א; מעל 7% התוספת לא מזכה |
| בסיס השכר לפנסיה | ניסוח השכר שעליו האחוזים חלים | צו ההרחבה מחייב הפרשות רק מהנמוך מבין שכר הבסיס ברוטו לבין השכר הממוצע במשק (13,769 ש"ח לחודש ב-2026). סעיף "פנסיה לפי חוק" בשכר גבוה מהתקרה מממן כחוק רק את החלק שעד התקרה. משמעותי ויקר: לדרוש "הפרשות ממלוא השכר ברוטו ללא תקרה" |
| פיצול קרן השתלמות | % מעסיק / עובד | סטנדרט 7.5% / 2.5% |
| עלות מעסיק כוללת | ברוטו + 6.5% + פיצויים + 7.5% קרה"ש + ב"ל מעסיק | בערך 120-125% מהברוטו |
| ימי הודעה מוקדמת | ימים בחוזה | לפחות המינימום החוקי לפי ותק |
| חופשה שנתית | ימים בחוזה | חלים שני סולמות והעובד זכאי לגבוה מביניהם. סעיף 3(א) לחוק חופשה שנתית נוקב בימים ברוטו (כולל מנוחה שבועית): 16 בכל אחת מחמש השנים הראשונות, 18 בשישית, 21 בשביעית, ואחר כך יום נוסף לשנה עד 28. צו ההרחבה בדבר מעבר לשבוע עבודה מקוצר, שחל על מרבית מקומות העבודה בני 5 ימים, נוקב בימים נטו: 12 בשנים 1 עד 5, 17 בשנים 6 עד 8, ו-23 מהשנה התשיעית. כלומר עובד בשנה התשיעית בשבוע של 5 ימים זכאי ל-23 ימים נטו, ולא ל-15 שהחוק לבדו נותן. הצו אינו חל על עבודה במשק בית, על מקום עבודה עם פחות מ-4 עובדים, על חברה ממשלתית או עירונית, ועל מקומות שבהם המעבר לשבוע של 5 ימים הוסדר בהסכם קיבוצי |
| ימי מחלה | ימים בחוזה | הצבירה היא 1.5 ימים לכל חודש מלא, עד יתרה מצטברת של 90 יום. אין תקרה שנתית של 18 יום: 18 זה רק 1.5 כפול 12, ואפשר לנצל יותר מזה בשנה מתוך היתרה הצבורה. הרכיב המהותי הוא הסולם: יום ראשון ללא תשלום, ימים שני ושלישי בחצי תשלום, מהיום הרביעי תשלום מלא (חוק דמי מחלה 1976, סעיפים 2 ו-5). חוזה שמשלם מהיום הראשון מיטיב עם העובד וכדאי להתמקח עליו |
| דמי הבראה | מספר ימים ותעריף בחוזה | לא מגיע כלום לפני 12 חודשי עבודה; עם השלמת השנה הראשונה משולמים 5 ימים, ועד 10 ימים מ-20 שנה ומעלה, בתעריף 451.5 ש"ח ליום במגזר הפרטי (511.6 בציבורי). מתחת לזה זה ממצא משמעותי |
