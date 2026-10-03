---
name: israeli-divorce-navigator
title: Israeli Divorce Navigator
description: 'Not legal advice. Walks a person through the Israeli divorce process end to end: the rabbinical-court vs. family-court jurisdiction choice and the joinder doctrine (kricha), the mandatory intake track (bakasha leyishuv sikhsukh and the MAHUT meetings under the 2014 family-disputes law) and the urgent-relief / protective-order carve-out, property balancing (izun mashabim, default 50/50 under the 1973 law, with section 8 deviation), spousal maintenance (mezonot isha) vs. child support (mezonot yeladim) and the Bagatz 919/15 shared-custody reform, custody / parental responsibility, the ketubah, common-law partners (yeduim betzibur), and the get plus get-refusal sanctions. Use when someone in Israel is starting or facing girushin and needs a roadmap, a property-balancing worksheet, or a checklist of what a divorce agreement must cover. Do NOT use for pension-split math (use israeli-pension-advisor), and always recommend a family lawyer for the actual filing.'
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-divorce-navigator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: real-estate
language: en
sources:
- title: Court jurisdiction comparison
  path: references/court-jurisdiction-comparison.md
- title: Domain checklist
  path: references/domain-checklist.md
- title: Izun mashabim worksheet
  path: references/izun-mashabim-worksheet.md
---

# Israeli Divorce Navigator

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Problem

Israeli divorce runs on two parallel court systems, a mandatory intake step you cannot skip, and a property-division rule whose exceptions trip up almost everyone. People lose real leverage by filing in the wrong forum, by assuming a clean 50/50 split, or by not realizing the marriage is not dissolved until a get is granted. This skill turns that maze into an ordered roadmap and gives the person a worksheet and a checklist of agreement topics to bring to a lawyer or mediator.

## Instructions

You are a navigator, not the lawyer. Give the person a clear map and decision criteria, produce the worksheet and a checklist of agreement topics (never agreement wording), and hand the actual filing and signature to a family lawyer (עורך דין לענייני משפחה). Never invent a statute section, amount, or waiting period. If a fact is not below, describe the process qualitatively and route to the source.

### Step 0: triage before drawing the map

Six answers change the law, the forum, or the urgency, so ask them first:

1. **Married or common-law?** Common-law partners follow Step 7, not this map.
2. **Married before 1 January 1974?** The balancing regime does not apply to couples married before the property law came into force (`לא יחולו על בני זוג שנישאו זה לזה לפני תחילת חוק זה`, section 14; commencement 1.1.1974, section 19). Their property runs on the case-law presumption of community property, so the worksheet and script below do not apply. Route to a lawyer.
3. **Domicile at the wedding?** Section 15: `יחול חוק מושבם בשעת עריכת הנישואין`. Olim who married while living abroad may have their property governed by foreign law. Lawyer question.
4. **Is there a property agreement (הסכם ממון)?** The balancing regime applies only where `לא עשו בני הזוג הסכם ממון`, or to the extent the agreement does not provide otherwise (section 3(a)). Ask for it, and whether it was approved as the law requires.
5. **Are both spouses Jewish, married in a Jewish ceremony, and Israeli citizens or residents?** The rabbinical court's exclusive jurisdiction is over `עניני נישואין וגירושין של יהודים בישראל אזרחי המדינה או תושביה` (1953 law, section 1); foreign non-resident spouses need a lawyer on international jurisdiction. If either spouse is not Jewish, the couple is same-sex, or they married civilly abroad, the divorce forum differs (another religious court or the family court). Do not apply Steps 1 and 6 as written; route to a lawyer. The property law still binds a religious court unless the parties consented before it to religious law (section 13(b)).
6. **Violence, or a risk of a child being taken abroad?** Go straight to the urgent-relief carve-out in Step 2.

### Step 1: frame the two forums and how matters get attached (joinder)

Israel has no civil divorce for Jews. Two forums matter:

| Matter | Rabbinical court (בית דין רבני) | Family court (בית המשפט לענייני משפחה) |
|--------|-------------------------------|----------------------------------------|
| The get (גט) that dissolves the marriage | Exclusive, under Jewish law (חוק שיפוט בתי דין רבניים (נישואין וגירושין), תשי"ג-1953) | No jurisdiction |
| Property balancing (איזון משאבים) | Concurrent | Concurrent |
| Spousal maintenance (מזונות אישה) | Concurrent | Concurrent |
| Child support (מזונות ילדים) | When validly joined to a divorce claim (temporary provision from 18.11.2025, for two years); otherwise only with both parties' consent | Concurrent |
| Custody / parental responsibility | Concurrent | Concurrent |
| Get-refusal sanctions (צווי הגבלה) | Yes, under חוק בתי דין רבניים (קיום פסקי דין של גירושין), תשנ"ה-1995 | No |

The get always goes to the rabbinical court and only there. For the concurrent matters, do NOT reduce the choice to "whoever files first wins." The governing doctrine is joinder (כריכה): a spouse can attach (join) the ancillary matters to a divorce claim in the rabbinical court, and that court then hears them instead of the family court. A valid joinder is not about filing order alone; it turns on three cumulative conditions a court tests together:

- the divorce claim is genuine (תביעת גירושין כנה),
- the joinder is genuine (כריכה כנה),
- the joinder was done lawfully (כריכה כדין).

If all three hold, the rabbinical court acquires jurisdiction over the joined matters, which can include property division, spousal maintenance (מזונות אישה), and custody. Child support changed on 18.11.2025: a temporary provision in force for two years gives the rabbinical court exclusive jurisdiction over `מזונות לילדי הזוג` (defined to include housing, education and medical expenses) as part of a divorce claim between Jews, without the other parent's consent (1953 law, section 3, as amended), and it also covers past support and reimbursement of child-support expenses between the parents. It reaches only matters `הכרוך בתביעת הגירושין`, so child support must still be validly joined under the three kricha conditions above; a child-support claim already filed in the family court is a lawyer question. The provision runs two years, to about 17.11.2027. Before that date the rabbinical court had no child-support jurisdiction without both parties' consent. Whether the provision reaches a case filed before it, and what happens when it expires, are lawyer questions; do not assert them. Chronology still matters only as a tie-breaker for a matter that was not validly joined. Tell the person the forum and the joinder are a genuine strategic decision a lawyer must make fast, sometimes within days. See `references/court-jurisdiction-comparison.md`.

### Step 2: the mandatory intake, and the urgent-relief carve-out

Before litigating in either forum the person generally files a Request to Resolve a Dispute (בקשה ליישוב סכסוך) under the family-disputes law of 2014 (חוק להסדר התדיינויות בסכסוכי משפחה, תשע"ה-2014). Then:

- The parties attend up to four MAHUT meetings (פגישות מהו"ת, meaning information, acquaintance and coordination) at an assistance unit (יחידת סיוע). All MAHUT meetings are held within 45 days of filing, a period that can be extended once by 15 days.
- A stay of proceedings runs for 45 days from filing (60 if the MAHUT period was extended), PLUS the 10 days the parties have to give notice, PLUS 15 days after that, plus any further period they agree to in writing (section 3(e)). In practice that is about 70 days, or 85 if extended, unless a different period was set for exceptional matters under section 5(a)(5). During the stay no family-dispute claim may be filed in any forum, and no forum may hear one, including on the jurisdiction question.

CRITICAL, and this is a safety point: the stay does NOT block urgent relief (סעד דחוף). Domestic violence, exit-from-country, urgent maintenance, securing a minor's contact, and medical matters are express exceptions the court can decide urgently, within about 14 days, without waiting out the stay. In particular, a domestic-violence protective order (צו הגנה) under the Prevention of Family Violence Law, 5751-1991 (חוק למניעת אלימות במשפחה, התשנ"א-1991) can be obtained urgently, including where a person is in a domestic-violence shelter. Never tell someone in danger that they must sit through the intake before they can get protection; route them to file for a צו הגנה and urgent relief immediately, and to a lawyer or a domestic-violence hotline.

Flag that filing the Request also interacts with the forum question, so where and when it is filed is itself a lawyer question.

### Step 3: build the property balance (izun mashabim)

Default rule under the Spousal Property Relations Law, 5733-1973 (חוק יחסי ממון בין בני זוג, תשל"ג-1973), section 5: on dissolution each spouse is entitled to half the value of ALL the couple's assets, EXCEPT a closed list of exclusions. You balance value, not physical items.

Excluded from the balance (section 5):
- Assets owned before the marriage (ערב הנישואין).
- Gifts and inheritances received during the marriage (מתנה או ירושה).
- National Insurance / Bituach Leumi benefits (גמלה מהמוסד לביטוח לאומי).
- Personal-injury compensation (פיצוי בגין נזק גוף).
- Anything agreed in writing not to balance.

Included by default, because the balance covers future rights accrued during the marriage: the statute lists `זכויות עתידיות לפנסיה, פיצויי פרישה, קרנות השתלמות, קופות תגמולים וחסכונות` (section 5(c)), so pension, manager's insurance (ביטוח מנהלים), severance, study funds (קרנות השתלמות, often the largest liquid asset) and provident funds built up during the marriage are part of the balanced property. Registration in one spouse's name does not by itself prove an asset is excluded (section 9); what matters is when and how it was acquired. Route the pension and actuarial split to the `israeli-pension-advisor` skill.

50/50 is the default, not a guarantee: under section 8 (סעיף 8) the court has the power to order that the division not be equal, and to fix qualitatively when the balance is measured (for example the severance or valuation date), where an equal split would be unjust. Present the equal split as the default the court can vary.

Tax note: real-estate transfers between spouses that are incident to the divorce are generally exempt from betterment tax (מס שבח) and purchase tax (מס רכישה). Do not state a statute section for this; route the exact mechanics and eligibility to a tax adviser or accountant.

Walk the person through `references/izun-mashabim-worksheet.md`, classify each asset as balanceable or excluded, subtract debts, then compute the difference each net position shows against the half share under the default rule (arithmetic on the person's own classification, not a finding of what anyone owes). Debts are deducted `למעט חובות בקשר לנכסים שאין לאזן שוויים` (section 6(a)): a mortgage on a pre-marriage apartment stays out of the pool together with the apartment. If one spouse's debts exceed their balanceable assets, the statutory half-the-difference formula (section 6(b)) would make the other spouse share that deficit; whether a court does so, especially for debts not taken for the family, is a lawyer question. The bundled `scripts/izun_mashabim.py` does the arithmetic for the 50/50 default. Flag commingling (for example a pre-marriage apartment retitled jointly) as a lawyer question, do not decide it.

Timing lever: section 5א allows early balancing (הקדמת איזון) before the get is finalized once a balancing request is filed and a condition is met, for example a year has passed since a dissolution proceeding or property claim opened; the court may shorten those waiting periods in a written reasoned decision. It is also available after nine months of living apart (even under one roof) within a year (`במשך תקופה מצטברת של תשעה חודשים לפחות`), and the court may advance it where a protective order was given against the other spouse, an indictment for violence against the applicant or their child was filed, or the spouse was detained on such a suspicion (section 5א(b)). The court may condition the balance on the applicant depositing consent to the get, or delay it for bad faith over the divorce, though refusing to waive rights the applicant or their child are entitled to is not bad faith (section 5א(c), (d)). This helps when one spouse stalls the get to freeze the money.

Two protections to raise in the first week: where a spouse acts, or is reasonably feared about to act, to defeat the balance, the court can order disclosure and security, require both spouses' consent for listed acts, or register a caution note (הערה) against the asset (section 11), and an asset given away or moved `בכוונה לסכל` the other spouse's balancing right can be treated as still belonging to that spouse (section 7). And the court will not order the sale of the family home until it is satisfied the minor children and the parent they live with have `הסדר מגורים אחר` (section 6א).

### Step 4: spousal maintenance vs. child support (do not conflate them)

These are two SEPARATE claims with different bases, payers, and durations. A layperson runs them together; keep them apart.

Spousal maintenance (מזונות אישה): a married woman can claim maintenance from her husband as long as the marriage has not been dissolved (כל עוד לא הותר קשר הנישואין). It is paid until the divorce or until a divorce ruling is given. Where the spouses have no personal-law maintenance duty (for example a couple defined as "without religion", חסרי דת), the duty falls under the Family Law Amendment (Maintenance) Law, 5719-1959 (חוק לתיקון דיני המשפחה (מזונות), התשי"ט-1959). Levers and limits to flag: a woman who works may, outside special cases, lose the entitlement, and a wife found to be a מורדת can forfeit both her spousal maintenance and her ketubah. When a husband refuses the get, withheld maintenance (מזונות מעוכבת) is a pressure lever, because his maintenance duty continues while the marriage is not dissolved.

Child support (מזונות ילדים): paid for the children, follows the payer's personal law and, from age 6, the 919/15 time-and-income split (see Step 5). It is owed independently of any spousal maintenance, runs on the children's needs and ages, and does not end at the divorce the way spousal maintenance does.

### Step 5: children (custody and child support)

Custody and place of residence follow the best interests of the child under the Legal Capacity and Guardianship Law, 5722-1962 (חוק הכשרות המשפטית והאפוטרופסות, תשכ"ב-1962). Section 25 carries the tender-age presumption that children up to age 6 are with their mother absent special circumstances; today the framing has shifted toward shared parental responsibility, so present it as a presumption a court can rebut, not a guarantee.

Child support (mezonot yeladim) follows the personal law of the payer. Under Jewish law and case law, from birth to age 6 the father bears an absolute obligation for the child's necessary needs regardless of his financial ability. From age 6, per בע"מ 919/15 (Supreme Court, July 2017), in shared custody both parents bear support jointly, split by the time each parent spends with the children and by the ratio of their incomes. Do not quote a shekel figure; explain the method and route the number to a lawyer.

### Step 6: the get, get-refusal remedies, and the ketubah

The marriage is not dissolved until a get is granted by the rabbinical court. A spouse trapped without a get is an עגונה (commonly, a מסורבת גט, a get-refused spouse). Suing on grounds can lead the rabbinical court to a ruling that obliges the get (חיוב גט) or, in narrower cases, compels it (כפיית גט). If a spouse still refuses, the court can impose restrictive orders (צווי הגבלה) under the 1995 enforcement law, and the list is broad: barring leaving the country, restricting an Israeli passport, restricting getting, holding or renewing a driver's license, seizing real estate and movable property (לעקל מקרקעין ומיטלטלין), placing a lien on a pension or allowance (עיקול על גמלה או קצבה), and in the hardest cases imprisonment. A 2024 amendment added two more: coercive-compliance payments to the spouse who won the ruling (section 3B) and the religious and social `הרחקות דרבנו תם` (section 3C). A civil tort suit (תביעת נזיקין) against a recalcitrant spouse has also been used as a separate pressure route. Tell the person a signed money-and-children agreement does not end the marriage on its own; the get is a separate, mandatory step.

The ketubah (כתובה): the ketubah sum is a monetary claim the wife can collect from the husband on divorce, adjudicated in the rabbinical court. It is part of the money picture but can be reduced or defeated where the wife is found to be a מורדת or in cases of adultery. Treat the amount as a lawyer question, not a fixed number.

### Step 7: common-law partners (ידועים בציבור) change the whole map

If the couple are not married but are common-law partners (ידועים בציבור), the map above shifts. Their property is not decided by the Spousal Property Relations Law (חוק יחסי ממון); it runs on the presumption of community property (חזקת השיתוף) and general law, proved case by case. There is no get and no rabbinical-court marriage-dissolution step, though maintenance and children questions can still arise. Flag early whether the couple were actually married, because it changes which law and which forum apply.

### Step 8: mediation and the agreement

Mediation (גישור) is the main way to avoid a contested fight: the couple reaches a divorce agreement (הסכם גירושין) with a mediator. The agreement must be submitted to the court or rabbinical tribunal for approval to receive the force of a binding judgment. Do not draft the agreement or any clause of it; the lawyer or mediator writes the text. Instead give the person a checklist of the topics the agreement must decide and the questions to bring to that meeting: property balancing per the worksheet, a parenting plan (residence, parenting time, decision-making), the child-support method, spousal maintenance where relevant, completion of the get and its timing, and submission for approval by the court or rabbinical court.

## Examples

### Example 1: high-earner spouse, pre-marriage apartment

A user says his wife filed for property division in the family court yesterday and asks if his apartment (bought before the wedding, still only in his name) gets split. Response: explain that under section 5 pre-marriage assets are excluded from the balance, so by default an apartment bought before the marriage stays outside the balance, but warn that if it was ever retitled jointly or heavily funded from joint money the exclusion can erode, which is a lawyer question. Then note that his wife filing first in the family court may have started the race to jurisdiction on the concurrent property matter, so he should see a lawyer quickly about his own filing.

### Example 2: shared custody, who pays mezonot

A father with true 50/50 shared custody of an 8-year-old, earning about the same as the mother, asks how much child support he owes. Response: explain that for age 6 and up, בע"מ 919/15 splits support by time and income ratio rather than putting it all on the father, so with equal time and similar incomes the transfer can be small or none, but the exact number depends on both incomes and expenses and must be set with a lawyer. Do not state a figure.

### Example 3: get refusal

A woman has a signed divorce agreement but her husband will not give the get. Response: explain that the agreement settles money and children but does not dissolve the marriage; only a get from the rabbinical court does. Point her to the refusal-sanction route (צווי הגבלה) under the 1995 law and recommend a family lawyer to file for the get and the sanctions.

## Gotchas

- Do NOT assume a flat 50/50 on everything. Section 5 excludes pre-marriage assets, gifts, inheritances, National Insurance benefits, and injury compensation, and under section 8 (סעיף 8) the court can order an unequal division. Applying community-property 50/50 to a pre-marriage apartment, or treating the equal split as guaranteed, is a classic error.
- Do NOT net a mortgage on an excluded asset against the pool. Section 6(a) deducts debts except those `בקשר לנכסים שאין לאזן שוויים`, so the debt leaves the balance with its asset. Mark such a debt as excluded in the worksheet and script.
- Do NOT conflate spousal maintenance (מזונות אישה) with child support (מזונות ילדים). They have different bases, payers, and durations: spousal maintenance is the husband's duty to the wife and ends at the divorce; child support is for the children and does not.
- Do NOT conflate custody with who pays support. Custody follows best interests; support liability follows personal law and, from age 6, the 919/15 time-and-income split. A parent can have shared custody and still owe or receive support.
- Do NOT tell someone in danger to wait out the intake. Urgent relief (סעד דחוף), including a domestic-violence protective order (צו הגנה) under חוק למניעת אלימות במשפחה, התשנ"א-1991, plus exit-from-country, urgent maintenance, and medical matters, is an express exception the stay does not block. Otherwise you generally cannot litigate before filing the Request to Resolve a Dispute and going through the MAHUT meetings.
- Do NOT apply the married-couple map to common-law partners (ידועים בציבור). Their property runs on חזקת השיתוף and general law, not חוק יחסי ממון, and there is no get.
- Do NOT tell the person the family court can grant the get. The get is exclusive to the rabbinical court; a family-court money-and-children ruling leaves the couple still married.
- Do NOT quote a specific child-support shekel amount, a specific izun payment, or a ketubah sum as fact. Produce the method and worksheet, and route the number to a lawyer.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| חוק יחסי ממון בין בני זוג, תשל"ג-1973 (Nevo) | https://www.nevo.co.il/law_html/law00/72138.htm | Sections 5 and 5א: default balance and the exclusions |
| חוק שיפוט בתי דין רבניים (נישואין וגירושין), תשי"ג-1953 (Nevo) | https://www.nevo.co.il/law_html/law00/73178.htm | Exclusive rabbinical jurisdiction over marriage and the get |
| חוק בתי דין רבניים (קיום פסקי דין של גירושין), תשנ"ה-1995 (Nevo) | https://www.nevo.co.il/law_html/law00/73181.htm | Restrictive orders against a get-refuser |
| חוק הכשרות המשפטית והאפוטרופסות, תשכ"ב-1962 (Nevo) | https://www.nevo.co.il/law_html/law00/70325.htm | Section 25 tender-age presumption |
| מזונות אישה (Kol Zchut) | https://www.kolzchut.org.il/he/מזונות_אישה | Spousal maintenance until the marriage is dissolved; the 1959 law for חסרי דת |
| כריכת עניינים נלווים לתביעת גירושין (Kol Zchut) | https://www.kolzchut.org.il/he/כריכת_עניינים_נלווים_לתביעת_גירושין_בבית_הדין_הרבני | The three cumulative joinder conditions; child support was consent-only before the 18.11.2025 temporary provision |
| הסדר איזון משאבים (Kol Zchut) | https://www.kolzchut.org.il/he/הסדר_איזון_משאבים | Section 8 unequal division; pension, manager's insurance and severance in the balance |
| הטלת סנקציות על סרבני גט (Kol Zchut) | https://www.kolzchut.org.il/he/הטלת_סנקציות_על_סרבני_וסרבניות_גט | The full list of restrictive orders against a get-refuser |
| חזקת השיתוף בין בני זוג (Kol Zchut) | https://www.kolzchut.org.il/he/חזקת_השיתוף_בין_בני_זוג | Common-law partners' property runs on חזקת השיתוף, not חוק יחסי ממון |
| בקשה ליישוב סכסוך במשפחה (Kol Zchut) | https://www.kolzchut.org.il/he/בקשה_ליישוב_סכסוך_במשפחה | MAHUT meetings within 45 days; the stay of proceedings; urgent-relief carve-out |
| בקשה ליישוב סכסוך (Kol Zchut, with the official judiciary filing link) | https://www.kolzchut.org.il/he/בקשה_ליישוב_סכסוך_במשפחה | Where and how to file the intake request, and the link to the official gov.il service |

## Bundled Resources

- `scripts/izun_mashabim.py`: computes a 50/50 default-rule property-balancing worksheet (arithmetic, not an entitlement) from a JSON or CLI list of assets and debts. Run with `--example` for a worked case.
- `references/domain-checklist.md`: coverage contract (must / should / out of scope) and the balance sub-dimensions.
- `references/izun-mashabim-worksheet.md`: step-by-step method for building the property balance.
- `references/court-jurisdiction-comparison.md`: rabbinical vs. family court and the race to jurisdiction.

## Troubleshooting

- The user asks for pension division math: stop and route to the `israeli-pension-advisor` skill; this skill only flags pensions as balanceable, it does not do the actuarial split.
- The user wants you to file or draft a binding document for signature: do not draft the document; give the checklist of agreement topics and route to a family lawyer to draft and file. State the legal facts, but do not present the skill as a substitute for a lawyer.
- The user gives incomes and expects an exact mezonot number: give the method (personal law under 6, 919/15 time-and-income split from 6) and explain the number must be set with a lawyer or the court.
- A fact the user needs is not in this skill: describe the process qualitatively and send them to the matching Reference Link rather than guessing a section number or amount.
