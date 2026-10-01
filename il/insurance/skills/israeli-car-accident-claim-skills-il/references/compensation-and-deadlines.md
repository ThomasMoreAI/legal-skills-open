# Compensation, urgent payment, and the clock

This file carries the money side and the deadlines. `claims-guide.md` carries the scene and the routing.

## 1. תשלום תכוף, the urgent payment

The single most valuable early right, and the only deadline that runs **against the insurer** rather than against the victim.

- Who pays: whoever is liable in damages under PLATD, and the insurer who insured that liability (PLATD §5(ב), §5(ג)).
- What: expenses the victim incurred for treatment including hospitalization, plus monthly payments covering, until the final decision on compensation, the victim's treatment and nursing needs and the living needs of the victim, his family, and his dependants. Living-needs payments take the victim's pre-accident income into account, capped at the maximum income figure.
- Deadline: `תוך 60 ימים מקבלת דרישתו בכתב`.
- How: a written demand on the form prescribed by the 1989 regulations, supported by an affidavit. If 60 days pass without payment, the victim applies to the Magistrates' Court, which may be done separately from the main claim (§5א).
- Late payment: linkage differences plus `ריבית צמודה בשיעור של 12% לשנה` from the due date to actual payment, unless the court finds grounds for a lower rate (§5ד).
- Not binding: the court's decision on an urgent payment is not res judicata for the main claim (§5ג).
- Ceilings: no urgent payment for a period exceeding two years from the accident (§5ה(ב)); after a decision, a further or amended application requires six months to have passed and a material change of circumstances (§5ה(א)). The court may vary both periods for recorded reasons (§5ה(ג)).
- Clawback: if the main claim is dismissed, or is never filed by the date the court set, the payer can recover the urgent payment (§5ב(ב), §5ז).
- Health-basket carve-out: the treatment-expenses limb does not apply to a resident for services inside the health basket, with the same three exceptions as §2(ב1) (§5ה of the payment section, i.e. PLATD §5(ה)).

Because a script that promises to surface time limits must surface this one, `scripts/claim_router.py` prints the urgent-payment deadline whenever there are injuries.

## 2. Compensation heads

### Non-pecuniary damage (כאב וסבל)

Set by תקנות הפיצויים לנפגעי תאונות דרכים (חישוב פיצויים בשל נזק שאינו נזק ממון), תשל"ו-1976. Everything is a share of `הסכום המקסימלי`, the CPI-linked ceiling under PLATD §4.

| Item | Rule |
|---|---|
| Hospitalization | `שני פרומיל מן הסכום המקסימלי כפול מספר הימים` that the victim was hospitalized (0.2% of the maximum per day), תקנה 2(א)(1) |
| Permanent disability | `אחוז אחד מן הסכום המקסימלי כפול אחוזי הנכות לצמיתות` (1% of the maximum per disability point), תקנה 2(א)(2), assessed on the Bituach Leumi work-injury disability tests |
| Age reduction | Where the victim was 30 or older on the day of the accident, the disability component is reduced `באחוז אחד לכל שנה שמלאה לו מעל לשלושים שנה` (1% per year over 30). It applies to the disability component only, not to the hospitalization component, תקנה 3 |
| Neither hospitalization nor permanent disability, OR non-pecuniary harm not covered by the two heads above | The agreed or awarded sum, capped at `עשרה אחוזים מהסכום המקסימלי` (10% of the maximum), תקנה 2(ב). Both limbs are in the text (`לא היה הנפגע זכאי לפיצוי לפי תקנת משנה (א) או שסבל נזק שאינו נזק ממון שאינו מכוסה`), so a hospitalized or disabled victim can receive this on top of the formula |
| Overall ceiling | The total non-pecuniary award `לא יעלו על` the maximum (PLATD §4(א)(3)), so a formula result above 100% is cut to 100% |
| Death | `עשרים וחמישה אחוזים מן הסכום המקסימלי` to the estate (25% of the maximum), תקנה 4 |

**The shekel value of `הסכום המקסימלי` is deliberately not stated here.** PLATD §4(א)(3) fixes it at `מאה אלף לירות` with a power to increase it, and §4(ב) links it to the Consumer Price Index from the law's commencement. Secondary sources circulate several different current figures. Quote the formula, then look up the current ceiling in an up-to-date source before putting a number in front of a user.

### Loss of earnings and earning capacity

PLATD §4(א)(1): `בחישוב הפיצויים בשל אבדן השתכרות ואבדן כושר השתכרות לא תובא בחשבון הכנסה העולה על שילוש השכר הממוצע במשק`. Where the loss of earning capacity is below 100%, the maximum income taken into account is reduced by the same proportion. The average wage is the higher of the CBS figure and the National Insurance figure as at the determination, so look up the current figure at btl.gov.il rather than quoting one from memory.

### Tax gross-down

PLATD §4(א)(2): where the compensation is income-tax exempt, losses are computed net of tax, but the reduction for tax `לא תעלה על 25 אחוזים` of the income base.

### Death and dependants

- §7ב: dependants can claim even where the victim himself was excluded under §7, and where the victim drove uninsured they claim from Karnit.
- The estate's non-pecuniary award is 25% of the maximum (תקנה 4).
- Bituach Leumi side: the family generally elects between קצבת שאירים and גמלת תלויים (work-accident death), normally taking the higher. Get advice before electing, because §6ב-style interactions and the §328א netting both bite here.
- הלכת אלסוחה recognises a claim for psychiatric harm suffered by a close family member of a physically injured victim, subject to the proximity conditions the case law sets. This is a recognised head of damage and it needs a lawyer.

## 3. Lawyer's fee and court fees

**The fee cap is the single most useful consumer fact in the statute.** PLATD §16(א): the Bar Association sets a maximum tariff for handling PLATD claims, `ובלבד ששכר טרחה שנקבע לפי תוצאות הטיפול לא יעלה על 8% מהסכום שהוסכם לשלמו לנפגע, ואם היו הליכים משפטיים - על 13% מהסכום שנפסק`, and `מי ששילם שכר טרחה העולה על התעריף המקסימלי, זכאי להחזר העודף`. Tell every injured user this before they sign a retainer.

Court fees are set by תקנות בתי המשפט (אגרות) and the small-claims fee and ceiling by תקנות שיפוט בתביעות קטנות. Both are updated periodically, so check the current schedule rather than quoting a figure. What is stable: a money claim for property damage is charged an ad valorem fee with a floor, payable in instalments, while small claims carry a much lower percentage fee and a statutory ceiling on the amount claimed. Confirm the current ceiling before routing a user to small claims, because a claim above it must go to the Magistrates' Court instead.

## 4. Who pays the medical bills

PLATD §2(ב1)(1): for a victim who is a תושב under the National Health Insurance Law, the driver's (and the permitting owner's) duty to compensate does not extend to health services in the second schedule or in an order under §8(ז) of that law, provided the victim is entitled to them. §2(ב1)(2) preserves the duty for a resident inside the waiting period under §58, a soldier outside the health law under §55, and a person entitled in respect of the injury to a benefit under chapter ה' of the National Insurance Law. Karnit must pay the hospital the cost of treating the victim as an insurer would (§12(ב)).

## 5. Work accident overlap

If the accident is also a work accident, the victim claims from **both** Bituach Leumi and the motor insurer, and the two are reconciled by netting, not by subrogation.

- חוק הביטוח הלאומי §328א(ב)(1): the Institute does not sue the motor insurer and no reporting duty applies to it.
- §328א(ב)(2): where a court orders a motor insurer to pay compensation to someone entitled to a benefit, `יופחת סכום הגמלה שחייב המוסד לשלם... מסכום הפיצויים`. The benefit is deducted from the award. Claiming both is correct and expected; it is not double-dipping.
- The Bituach Leumi route runs through a ועדה רפואית, which grades permanent disability and then splits the outcome between a recurring קצבת נכות מעבודה above a threshold percentage and a one-off מענק in a band below it. The threshold and the band are set by the National Insurance Law and its regulations and are NOT stated here; look them up before quoting a number to a user.
- **The §6ב trap.** PLATD §6ב: `נקבעה על פי כל דין דרגת נכות לנפגע בשל הפגיעה שנגרמה לו באותה תאונת דרכים, לפני שמיעת הראיות בתביעה לפי חוק זה, תחייב קביעה זאת גם לצורך התביעה על פי חוק זה`. The court may allow rebuttal evidence only for recorded special reasons. A low Bituach Leumi percentage agreed early therefore locks the civil claim. Take advice before that determination becomes final.

## 6. The two limitation periods

| Claim | Period | Runs from | Source |
|---|---|---|---|
| Insurance benefits (תגמולי ביטוח) against your own insurer, including a מקיף property claim | **3 years** | The insured event, i.e. the accident | חוק חוזה הביטוח §31 |
| Tort claim against the at-fault driver, and the PLATD bodily-injury claim | **7 years** | The cause of action | חוק ההתיישנות §5 |
| Either of the above where the victim is a minor | The clock is suspended below 18 | Age 18, so about age 25 on the 7-year figure | חוק ההתיישנות §10 |

`תקופת ההתיישנות של תביעה לתגמולי ביטוח היא שלוש שנים לאחר שקרה מקרה הביטוח` (§31). Two nuances follow.

- **Liability insurance extension, §70**: `בביטוח אחריות, התביעה לתגמולי ביטוח אינה מתיישנת כל עוד לא התיישנה תביעת הצד השלישי נגד המבוטח`. So a צד ג' route effectively tracks the third party's period, not the 3-year one.
- **The insurer's warning duty, §31א**: once the insured has notified the insurer under §22, the insurer must state the limitation period and that delivering the claim does not stop the clock, and must warn in writing 12 months before the period ends and again 3 months before it ends, even while negotiations are running. Do not rely on receiving that warning.

Notify the insurer immediately after the accident in any case (חוק חוזה הביטוח §22; the standard policy's own notification clause).

## 7. Escalation

Complain to the Public Inquiries Unit at the Capital Market, Insurance and Savings Authority; the complaint does not bar going to court. For smaller property sums, small claims (route to israeli-small-claims-court). None of this replaces a lawyer for an injury claim, and the §16 cap means a lawyer costs less than most people assume.
