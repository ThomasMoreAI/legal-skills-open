# Domain checklist: Israeli Divorce Navigator

Coverage contract for the skill. Every "Must cover" row is grounded in a claim in `evidence.json`.

## Must cover (core)

| Topic | Source / statute | Why core |
|-------|------------------|----------|
| Dual-track jurisdiction: rabbinical court vs. family court | חוק שיפוט בתי דין רבניים (נישואין וגירושין), תשי"ג-1953; חוק בית המשפט לענייני משפחה, תשנ"ה-1995 | The first structural choice in every Israeli divorce; the get is exclusive to the rabbinical court, most everything else is concurrent. |
| Joinder (כריכה) of ancillary matters to the divorce claim | Case law; three cumulative conditions (genuine claim / genuine joinder / lawful joinder) | Validity is not filing order alone; child support: from 18.11.2025 (two-year temporary provision, 1953 law s.3) the rabbinical court has exclusive jurisdiction when joined to a divorce claim, without consent; before that, consent of both was required. Chronology is only a tie-breaker. |
| Mandatory intake: Request to Resolve a Dispute + MAHUT meetings | חוק להסדר התדיינויות בסכסוכי משפחה, תשע"ה-2014 | You generally cannot litigate before this step; up to four MAHUT meetings within 45 days (+15), stay of 45/60 days plus 10 plus 15 (about 70/85), s.3(e). |
| Urgent-relief (סעד דחוף) carve-out + domestic-violence protective order | חוק למניעת אלימות במשפחה, התשנ"א-1991; kolzchut yishuv-sikhsukh page | Safety-critical: DV, exit-from-country, urgent maintenance, and medical relief are NOT barred by the intake stay; decided within about 14 days. |
| Property balancing (איזון משאבים) default 50/50 and what is excluded | חוק יחסי ממון בין בני זוג, תשל"ג-1973, ס' 5 | The core money question; the exclusions (pre-marriage, gift/inheritance, NII benefits, injury compensation) are the most misunderstood part. |
| Section 8 deviation from equal division; pension/manager's insurance/severance in the balance | חוק יחסי ממון, ס' 8; kolzchut izun page | The court can order an unequal split and fix the valuation date; future rights accrued in the marriage are balanced. |
| Early balancing (הקדמת איזון) | ס' 5א of the same law | Lets a spouse balance assets before the get is finalized; the one-year trigger matters for timing. |
| Spousal maintenance (מזונות אישה) vs. child support | Din ishi; חוק לתיקון דיני המשפחה (מזונות), תשי"ט-1959 | Two separate claims; spousal maintenance runs until the marriage is dissolved and a working woman may lose it; מזונות מעוכבת is a get-refusal lever. |
| Child support (מזונות ילדים) and the personal-law basis | Din ishi; חוק לתיקון דיני המשפחה (מזונות), תשי"ט-1959 | Determines who pays and how much; the father's absolute duty for necessary needs to age 6 is Israel-specific. |
| בע"מ 919/15 shared-custody child-support reform | Supreme Court, July 2017 | From age 6, shared custody splits support by time and income ratio; changed decades of practice. |
| Custody / parental responsibility and the tender-age presumption | חוק הכשרות המשפטית והאפוטרופסות, תשכ"ב-1962, ס' 25 | The framework for where children live and the best-interests test. |
| The get (גט), get-refusal remedies, and the ketubah | חוק בתי דין רבניים (קיום פסקי דין של גירושין), תשנ"ה-1995 | Civil divorce does not exist for Jews in Israel; חיוב/כפיית גט, the עגונה/מסורבת גט status, the broad צווי הגבלה list (exit ban, passport/license, asset/pension seizure, imprisonment), the תביעת נזיקין route, and the ketubah as a wife's monetary claim reduced/defeated by מורדת/adultery. |
| Common-law partners (ידועים בציבור) | חזקת השיתוף / general law | Their property is NOT under חוק יחסי ממון and there is no get; the whole map changes. |
| Mediation (גישור) and the divorce agreement (הסכם גירושין) | Alternative track; agreement submitted for judicial approval | The main way to avoid a contested fight; the agreement needs court/tribunal approval to be binding. |

## Should cover (advanced)

| Topic | Source / statute | Why advanced |
|-------|------------------|--------------|
| "Career assets" / earning capacity in the balance | Case law under חוק יחסי ממון, ס' 8 | Courts can balance a spouse's enhanced earning capacity; nuanced and fact-heavy. |
| Tax treatment of spousal asset transfers on divorce | Real-estate transfers incident to divorce are generally exempt from מס שבח / מס רכישה | Route the exact mechanics to a tax adviser; do not cite a section. |
| Assistance-unit process cost and legal-aid eligibility | תשע"ה-2014 regime | The MAHUT process itself is free; useful but not decision-critical. |

## Out of scope (explicit)

| Topic | Why out | Route to |
|-------|---------|----------|
| Pension-split mechanics and actuarial math | Deep actuarial domain of its own | Cross-reference the `israeli-pension-advisor` skill. |
| Binding legal advice / actual court filing and drafting for signature | Requires a licensed advocate; unauthorized practice risk | Recommend a family lawyer (עורך דין לענייני משפחה). |
| Detailed tax math on asset transfers (exact exemption mechanics, sections, amounts) | Separate tax domain | A tax adviser / accountant. The skill still flags the general מס שבח / מס רכישה exemption qualitatively. |
| Non-Jewish, mixed, same-sex, and civil-abroad divorce specifics | Different forums; reviewed 2026-09-19: users do ask, so SKILL.md Step 0 now triages them (1953 law s.1 scope; property law s.13(b)) and routes to a lawyer, but forum-by-forum procedure stays out | A lawyer; the relevant religious court or the family court. |

## Property-balancing (איזון משאבים) sub-dimensions

Included in the balance by default (ס' 5, "כלל נכסי בני הזוג"):
- Salary, savings, and pensions accrued during the marriage (pension math routed to `israeli-pension-advisor`).
- Future rights accrued during the marriage: pension, manager's insurance (ביטוח מנהלים), and severance pay (פיצויי פרישה).
- The family home and other real estate acquired during the marriage.
- Vehicles, business value, securities, and other property acquired during the marriage.
- Joint and individual debts accrued during the marriage (netted against assets), EXCEPT debts connected with excluded assets (s.6(a)); a negative net position is flagged for a lawyer (s.6(b)).
- Scope gates: marriage before 1.1.1974 (s.14, s.19), foreign domicile at the wedding (s.15), a property agreement (s.3(a)).
- Protective measures (s.11) and the family-home sale stay for minor children (s.6א).

Deviation from equal division (ס' 8): the 50/50 default is not guaranteed. The court can order an unequal division and fix the valuation/severance date qualitatively where an equal split would be unjust. `scripts/izun_mashabim.py` computes only the equal balance and does not model this.

Excluded from the balance (ס' 5):
- Assets each spouse owned before the marriage (נכסים ערב הנישואין).
- Gifts and inheritances received during the marriage (מתנה או ירושה).
- National Insurance (Bituach Leumi) benefits (גמלה מהמוסד לביטוח לאומי).
- Personal-injury compensation (פיצוי בגין נזק גוף).
- Anything the couple agreed in writing not to balance.

Note: an excluded asset can lose its exclusion if it was commingled (e.g. a pre-marriage apartment retitled into joint names). Flag this as a question for a lawyer, do not decide it.

## Authoritative sources

- חוק יחסי ממון בין בני זוג, תשל"ג-1973: https://www.nevo.co.il/law_html/law00/72138.htm
- חוק להסדר התדיינויות בסכסוכי משפחה, תשע"ה-2014: https://www.nevo.co.il/law_html/law01/501_151.htm
- חוק בית המשפט לענייני משפחה, תשנ"ה-1995: https://www.nevo.co.il/law_html/law00/98460.htm
- חוק שיפוט בתי דין רבניים (נישואין וגירושין), תשי"ג-1953: https://www.nevo.co.il/law_html/law00/73178.htm
- חוק בתי דין רבניים (קיום פסקי דין של גירושין), תשנ"ה-1995: https://www.nevo.co.il/law_html/law00/73181.htm
- חוק הכשרות המשפטית והאפוטרופסות, תשכ"ב-1962: https://www.nevo.co.il/law_html/law00/70325.htm
- Kol Zchut, בקשה ליישוב סכסוך במשפחה: https://www.kolzchut.org.il/he/בקשה_ליישוב_סכסוך_במשפחה
- Kol Zchut, מזונות ילדים: https://www.kolzchut.org.il/he/מזונות_ילדים
- Kol Zchut, מזונות אישה: https://www.kolzchut.org.il/he/מזונות_אישה
- Kol Zchut, כריכת עניינים נלווים לתביעת גירושין: https://www.kolzchut.org.il/he/כריכת_עניינים_נלווים_לתביעת_גירושין_בבית_הדין_הרבני
- Kol Zchut, הסדר איזון משאבים: https://www.kolzchut.org.il/he/הסדר_איזון_משאבים
- Kol Zchut, הטלת סנקציות על סרבני וסרבניות גט: https://www.kolzchut.org.il/he/הטלת_סנקציות_על_סרבני_וסרבניות_גט
- Kol Zchut, חזקת השיתוף בין בני זוג: https://www.kolzchut.org.il/he/חזקת_השיתוף_בין_בני_זוג
- Kol Zchut, בקשה ליישוב סכסוך במשפחה (כולל הקישור לשירות הרשמי של הרשות השופטת): https://www.kolzchut.org.il/he/בקשה_ליישוב_סכסוך_במשפחה
