# Domain completeness checklist: Israeli estate settlement (post-death bureaucracy)

Built from an aggregator sweep of the Kol-Zchut bereavement hub
("מדריך לבני משפחה המתמודדים עם מוות (פטירה) וקבורה") and the Kol-Zchut heirs
rights guide ("זכותון ליורשים ולקרובי אדם שנפטר לתקופה הסמוכה למוות"), then
verified against gov.il, btl.gov.il, kolzchut.org.il, and justice.gov.il.

`domain_checklist_version: 3` (re-litigated 2026-09-25)

## Must cover (core)

| Topic (He) | Topic (En) | Status |
|---|---|---|
| הודעת פטירה / קביעת מוות | Death notice issued by the doctor/hospital that confirms death | Covered |
| רישום פטירה במרשם האוכלוסין | Registering the death at Misrad HaPnim / Population and Immigration Authority | Covered |
| תעודת פטירה + העתקים מרובים | Official death certificate + why you need many certified copies | Covered |
| דמי קבורה | Burial grant paid by Bituach Leumi directly to the burial society | Covered |
| קבורה (חברה קדישא / מועצה דתית) | Burial logistics (Chevra Kadisha / religious council) | Covered |
| קבורה אזרחית / חלופית | Civil / alternative burial option | Covered |
| רשימת גופים ליידוע וסדר הפעולות | Institution notification cascade and correct order | Covered |
| בנקים והקפאת חשבון | Banks and account freezing until an order is issued | Covered |
| קופות גמל / פנסיה / ביטוח / מבטח | Pension, gemel, insurers | Covered |
| מעסיק (שכר אחרון, פיצויים, פדיון חופשה) | Employer (final pay, severance, unused vacation to heirs) | Covered |
| קופת חולים | HMO (kupat cholim) | Covered |
| עירייה / ארנונה | Municipality / arnona | Covered |
| חברות תשתית (חשמל, מים, גז) | Utilities (electricity, water, gas) | Covered |
| ספקי סלולר / אינטרנט / מנויים | Cellular, internet, subscriptions | Covered |
| ביטול הוראות קבע | Cancelling standing orders | Covered |
| מכתבי סגירה / העברה | Account closure / transfer request letters | Covered (templates) |
| אחריות היורשים לחובות (עד שווי העיזבון) | Heirs liable for debts only up to estate value | Covered |
| סדר עדיפות בפירעון חובות | Debt priority order (funeral first) | Covered |
| העברת מקרקעין בטאבו לאחר צו | Real estate re-registration at the Land Registry after the order | Covered |
| העברת רכב במשרד הרישוי | Vehicle transfer at Misrad HaRishui | Covered |
| שחרור כספים / ניירות ערך מהבנק | Releasing bank funds / securities after the order | Covered |
| הבחנה בין חשבון משותף (אריכות ימים) לחשבון יחיד | Joint account with a survivorship clause vs sole account (freeze scope) | Covered (bank note + gotcha + troubleshooting) |
| איתור חשבונות ופוליסות (הר הכסף / הר הביטוח) | Locating unknown accounts and policies via Har HaKesef and Har HaBituach | Covered (first-30-days discovery step) |
| מיסוי מקרקעין בירושה + אין מס עיזבון | Real-estate inheritance tax treatment + no estate/inheritance tax in Israel | Covered (asset transfer + gotcha) |
| הפסקת קצבת הנפטר עצמו בביטוח לאומי | Stopping the deceased's own old-age/disability allowance | Covered (first-30-days step) |
| ביטוח חיים ללווים במשכנתה | Mortgage borrower life insurance pays off the loan on death | Covered (asset transfer / debts) |
| הרשימה הסגורה של גבייה חוקית בידי חברה קדישא | The closed list of cases where a burial society MAY lawfully charge on top of the grant (תקנות דמי קבורה תשל"ו-1976, תקנות 3(א) ו-4(א)) | Covered (added v1.2.0). Previously stated as a flat prohibition, which is wrong in six enumerated cases |
| שחרור כספים מהבנק להוצאות פטירה מיידיות לפני הצו | Bank release of limited sums for immediate death expenses BEFORE the order | Covered (added v1.2.0) |
| הסמכות השיורית של 90 יום בייפוי כוח מתמשך | The 90-day residual authority of an enduring power of attorney after death (ס' 32כד(ב) לחוק הכשרות המשפטית והאפוטרופסות) | Covered (added v1.2.0). Previously stated as a flat lapse |
| משטר האחריות לפי אופן החלוקה (ס' 126 / 127 / 128) | Heir liability turns on HOW the estate was divided; s.128(a) exposes each heir to the value of the whole estate where creditors were not invited, s.128(b) puts the burden of proving value on the heir | Covered (added v1.2.0). The prior text cited ss.100-106, which govern the estate administrator, not heir liability |
| מקבלי פיצויי הפיטורים במות עובד | Severance on death is paid to the statutory שאירים (ס' 5 לחוק פיצויי פיטורים), not to the יורשים, and not out of the estate | Covered (added v1.2.0) |
| הוראת השעה בסעיף 5(ב1) לחוק פיצויי פיטורים | For a death from 7.10.2023 until one year after the home-front special-situation declaration of that date ended, only spouse and dependent child are שאירים, and heirs step in where there are none | Covered (added v1.3.0). The flat s.5 statement was wrong for every death in the period; exact end date and the effect of the 28.2.2026 declaration flagged as unverified |
| הנפטר כמעסיק (מטפל סיעודי / עוזרת בית) | Death = dismissal of a caregiver or housekeeper the deceased employed; wages, notice, recuperation, vacation, severance are estate debts | Covered (added v1.3.0), payroll routed to `foreign-caregiver-payroll` |
| כספים שמשתחררים בלי צו (מוטבים, סכומים נמוכים) | Named beneficiaries in gemel / life insurance, and small balances released under circulars 2014-2-3 and 2017-9-8 | Covered (added v1.3.0); thresholds deliberately not quoted |
| תיקי הוצאה לפועל נגד הנפטר | Execution files against a deceased debtor: registration-only measures until an order, two-year closure notice (תקנה 10א לתקנות ההוצאה לפועל) | Covered (added v1.3.0, body + reference) |
| מס שבח במכירת דירה שהתקבלה בירושה וחלוקת עיזבון | Heir steps into the deceased's purchase date and value; s.49ב(5) exemption; first division among heirs not a sale (s.5(ג)(4)) unless outside consideration | Covered (added v1.3.0) |
| פטירה בחו"ל | Burial abroad grant (s.267), registry update before the order for an Israeli ID holder | Covered (added v1.3.0); repatriation logistics not covered |
| היקף סעיף 266 לחוק הביטוח הלאומי | s.266 covers anyone who died in Israel and a resident who died abroad; reg 3(b) free charging applies only outside it | Covered (fixed v1.3.0). v1.2.1 wrongly glossed a non-resident as outside s.266 |
| שירות "ליווי לאחר פטירה" ב-gov.il | The government one-stop post-death service for a first-degree relative | Covered (added v1.2.0) |

## Should cover (advanced / adjacent)

| Topic (He) | Topic (En) | Status |
|---|---|---|
| הנחת ארנונה למשפחה שכולה / מקבלי שאירים | Arnona discount tied to survivor benefits | Mentioned, routed to municipality + survivor-benefits skill |
| ייפוי כוח מתמשך שפוקע בפטירה | Enduring power of attorney lapses at death | Noted as a gotcha |
| טופס אריכות ימים בחשבון משותף | Survivorship ("long life") clause on a joint account | Covered (bank note) |
| נשק שבבעלות הנפטר | Deceased's firearm (deactivate through the licensing bureau, or surrender to police within 30 days) | Covered (firearm note + cascade row) |
| כספת בבנק | Safe-deposit box frozen with the estate; may hold the original will | Covered (safe-deposit note) |
| הקמת מצבה | Erecting a headstone (not funded by the burial grant) | Covered (burial section + gotcha) |
| חוזה שכירות של הנפטר | Deceased's rental lease (notify landlord, terminate) | Covered (first-30-days step) |
| ימי אבל / חופשת אבל לעובד | Bereavement leave for an employed mourner | Out of scope, noted |

## Out of scope (explicit)

Every row below was re-litigated on 2026-08-18, and again on 2026-09-25, against two questions: would an ordinary
bereaved family plausibly ASK for it, and has it become capturable since the row was written.
A row that stays out of scope still gets a real answer in the form of a route, never silence.

| Topic | Why | Route to |
|---|---|---|
| כתיבת / הפקדת / בחירת צוואה | Writing, depositing, or choosing a will | Skill `israeli-wills-inheritance` |
| הוצאת צו ירושה / צו קיום צוואה | Obtaining the succession order or probate order itself. Re-litigated 2026-08-18: families DO ask, so this skill names the gov.il one-stop route and the combined order-plus-Tabu filing, and routes the procedure and its fees onward rather than staying silent | Skill `israeli-wills-inheritance` |
| אגרות הרשם לענייני ירושה | The Registrar's statutory fee schedule. Re-litigated 2026-08-18: families do ask what the order costs, and the schedule is capturable, but it belongs to the order process rather than to this skill, so it is encoded in the wills skill and not duplicated here. Two structural points a user needs regardless: the fee is fixed by the FILING date, not by the date of death, and the schedule is reindexed annually, so an amount quoted from an older page can be wrong. Do not quote an amount from this skill | Skill `israeli-wills-inheritance` |
| קצבת שאירים / פנסיית שאירים | Survivor allowance and survivor pension eligibility/amounts | Skill `israeli-survivor-benefits-navigator` |
| סכום מענק הקבורה / מצבה לניצולי שואה | Burial-grant amounts, headstone grants, benefit sums | Skill `israeli-survivor-benefits-navigator` |
| תביעות ביטוח חיים | Life-insurance claims | Skill `israeli-survivor-benefits-navigator` |
| עיזבון במחלוקת / נכסים בחו"ל | Contested estates, foreign or complex assets | A licensed lawyer (state the facts, still recommend counsel) |
| החלטות רפואיות בסוף החיים | End-of-life medical decisions, hospice, organ donation | Medical / other guides, out of scope here |
| מיסוי הנפטר והעיזבון | The deceased's final-year return, tax on estate income, and closing a self-employed deceased's VAT and NI files. Re-litigated 2026-09-25: users DO ask, so the capturable part is now stated (Income Tax Ordinance s.120: the legal personal representative is liable; Form 2805 heirs' declaration to close the file; VAT Form 18 is the only official VAT closure page and names no death route). Still out of scope: filing deadlines, computations, who signs at VAT, because no official source states them | Tax Authority assessing office; a רואה חשבון or יועץ מס |
| מינוי מנהל עיזבון | Appointing an estate administrator. Signposted in the body from v1.2.0; the application procedure is not covered | A licensed lawyer |
| יורשים קטינים / נעדרים / בחו"ל, והאפוטרופוס הכללי | Minor, absent, or overseas heirs, and the Administrator General's role. Re-litigated 2026-09-25: still out of scope because the Administrator General's supervision procedure was not verified at a primary source this cycle; the body now adds the verified fact that with no heir the State inherits (Succession Law s.17) | A licensed lawyer |
| נכסים דיגיטליים וחשבונות מקוונים | Digital assets and online accounts. Resolved 2026-09-25 (CARRY-STALE after two deferrals): no Israeli statute located; provider routes (Google deceased-user request, Apple Legacy Contact) and the keep-the-phone-line-for-2FA rule are now in the money-and-tax reference, with credit cards in the cascade | Covered in `references/money-tax-and-employment-after-death.md` |
| דייר ממשיך בדיור ציבורי | A relative who lived with a public-housing tenant may, under conditions, be a continuing tenant (no threshold stated here: unsourced). Logged 2026-09-25, NOT covered: the primary source (Public Housing Law / company procedure) was not verified this cycle | Next cycle; meanwhile the lease step should not be read as applying to public housing |
| הסכם בין יורשים / הסתלקות | Heirs' agreement and renunciation (Succession Law s.6: only before division, in favour of the deceased's spouse, child, or sibling; s.6A widens the beneficiaries for heirs of a person who died in the Swords of Iron war period, e.g. hostile-action victims and fallen soldiers). Belongs to the order process | Skill `israeli-wills-inheritance` |

## Authoritative sources

- Bituach Leumi burial grant: https://www.btl.gov.il/benefits/dmaykvura/Pages/zacautKvura.aspx
- gov.il death certificate (free): https://www.gov.il/he/service/death_certificate
- gov.il death registration: https://www.gov.il/he/service/death_registration
- Kol-Zchut bereavement family guide (search Kol-Zchut for "מדריך לבני משפחה המתמודדים עם מוות (פטירה) וקבורה")
- Kol-Zchut heirs rights guide: https://www.kolzchut.org.il/he/זכותון_ליורשים_ולקרובי_אדם_שנפטר_לתקופה_הסמוכה_למוות
- Kol-Zchut settling the deceased's debts: https://www.kolzchut.org.il/he/הסדרת_חובות_אדם_שנפטר
- Registrar of Inheritance Affairs (הרשם לענייני ירושה): https://inheritance.justice.gov.il/RashamYerusha/#/home (order process is out of scope; for the wills skill)
- gov.il vehicle transfer after death: https://www.gov.il/he/service/modification_registration_vehicle_following_death
- Har HaKesef (Ministry of Finance, locate lost accounts/policies): https://itur.mof.gov.il/
- Har HaBituach (Capital Market Authority, locate insurance/pension): https://harb.cma.gov.il/
- Kol-Zchut burial grant (headstone not covered): search Kol-Zchut for "דמי קבורה"
- Kol-Zchut mortgage insurance (pays off the loan on death): search Kol-Zchut for "ביטוח משכנתא"
- Bituach Leumi, family of a deceased allowance recipient: search btl.gov.il for "זכויות בני משפחה של מקבל קצבה שנפטר"
- Land Taxation Law, section 4 (inheritance is not a taxable sale) and abolition of estate tax (1981): see evidence.json
- Succession Law, 5725-1965 (full text, fetchable): https://www.nevo.co.il/law_html/law00/72178.htm
- Legal Capacity and Guardianship Law, 5722-1962 (full text, fetchable): https://www.nevo.co.il/law_html/law00/70325.htm
- Bituach Leumi (Burial Grant) Regulations, 5736-1976 (full text, fetchable): https://www.nevo.co.il/law_html/law01/039_109.htm
- Firearms Law, 5709-1949 (full text, fetchable): https://www.nevo.co.il/law_html/law00/72225.htm
- Note 2026-09-25: nevo.co.il IP-blocked this machine mid-cycle. Hebrew Wikisource carries the
  consolidated texts (Succession Law, Severance Pay Law, National Insurance Law, Land Taxation
  Law, Income Tax Ordinance, Execution Regulations) and is fetchable by curl.
- gov.il post-death accompaniment (one-stop): https://www.gov.il/he/service/post-death-accompaniment

## Source reachability (recorded 2026-08-18)

This matters for the evidence gate, not for users. Three access classes were measured:

- Fetchable by plain `curl`: btl.gov.il burial page, all four nevo statute pages above, the
  Mizrahi-Tefahot deceased-account page.
- HTTP 403 to `curl` and to WebFetch, readable in a real browser: the three gov.il service pages.
- Behind a Cloudflare/CloudFront challenge: every `kolzchut.org.il` URL (but the Wayback
  Machine raw endpoint `web.archive.org/web/<timestamp>id_/<url>` returns the full page, found
  2026-09-25, and is used for new evidence entries), `itur.mof.gov.il`, `harb.cma.gov.il`. These are alive for humans but
  cannot be verified by the gate, so statutory claims were re-anchored to the nevo primaries
  above and Kol-Zchut is retained only as a human-facing reading link.

Note also that the Kol-Zchut hub URL contains literal parentheses, which naive URL extraction
truncates. Write it percent-encoded (`%28`/`%29`) in `evidence.json`.
