---
name: israeli-car-accident-claim-skills-il
title: Israeli Car Accident Claim
description: 'Not legal advice. Guides a driver through the aftermath of a car accident in Israel: what to do and document at the scene, which insurance to claim under (compulsory vs comprehensive vs third-party), how the no-fault bodily-injury rule (PLATD) differs from fault-based property damage, how to fill the הודעה על תאונה report, the urgent-payment right, the compensation heads, the two different limitation periods, and when Karnit applies. Use when a user says "I had a car accident", "te''unat derachim", "the other driver hit me", "what do I do after a crash", "claim car damage from insurance", or "hit and run". Produces a scene checklist and a claim plan. Do NOT use for vehicle registration, test, or insurance shopping (use israeli-vehicle-manager), serious injury litigation (needs a lawyer), or DUI / criminal defense.'
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-car-accident-claim
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: insurance
language: en
sources:
- title: Claims Guide
  path: references/claims-guide.md
- title: Compensation And Deadlines
  path: references/compensation-and-deadlines.md
- title: Domain Checklist
  path: references/domain-checklist.md
---

# Israeli Car Accident Claim

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Problem

A car accident in Israel is stressful and the rules are counter-intuitive: bodily injury is compensated with no regard to fault, while property damage is entirely fault-based, and people routinely claim from the wrong policy or miss the steps that the insurer later uses to reject the claim. Many drivers do not know that a police confirmation is a precondition for the claim, that there is a fund (Karnit) for hit-and-run and uninsured cases, that they can demand an urgent payment within 60 days, or that the deadline against their own insurer is far shorter than the one against the other driver. This skill walks the driver through the scene and routes the claim to the right place.

## Problem boundary

This skill is about the accident and the claim. For registration renewal, the annual test (טסט), used-car checks, ownership transfer, or choosing an insurance policy, use the israeli-vehicle-manager skill, which owns that side and deliberately excludes accidents.

## Instructions

You help a driver act correctly after a road accident and route the claim. Read `references/claims-guide.md` for the scene and routing detail, and `references/compensation-and-deadlines.md` for the money and the deadlines, before advising. The single most important distinction to get right: bodily injury is no-fault, property damage is fault-based. Keep them separate at every step.

### Step 1: Safety and the first minutes at the scene

Tell the user to secure the scene (hazard lights, warning triangle, move to safety only if the vehicle is drivable and there are no injuries), check everyone for injuries, and call emergency services if anyone is hurt. If there are injuries or a death, or the other driver fled, police involvement is mandatory: the driver must stop, render aid, and report. Failing to stop or to help an injured person is a serious criminal offense under the Traffic Ordinance. A driver who merely passes an accident scene also has a duty to stop and give assistance (תקנה 146).

### Step 2: Document everything

Have the user photograph all vehicles, the damage, the license plates, the position on the road, signage, and any skid marks, and collect: the other driver's name, ID, phone, plate number, and their insurer and policy number, plus the names and phones of any witnesses. In a property-only accident the legal duty is to exchange these details on the spot (תקנה 145). In an injury accident there is the added duty to report to the police (תקנה 144). Two easily-missed rules sit in the same regulation: if the vehicle you hit was parked or its owner is not present, you must leave a written note with your details AND report to the police within 24 hours (תקנה 145(ג)); and in a property-only accident that blocks traffic you must clear the road (תקנה 145(ב)).

If anyone is hurt, the medical paper trail matters more than the car photos for the claim: get examined the same day (ER or doctor), describe every affected body part to the doctor, and keep every medical record. An injury first mentioned weeks later is easy for the insurer or Karnit to dispute. If the accident happened on the way to or from work, it may also be a work accident, so report it to the National Insurance Institute (ביטוח לאומי) as well, but read the §6ב warning in Step 8 before you let any disability percentage be fixed there.

### Step 3: Get the police confirmation

A police confirmation (אישור משטרתי) is a precondition for filing a compensation claim, in the police's own words on the gov.il service page. When there are no injuries (or injured people were treated and released within 24 hours), the driver can file the gov.il online light-accident report and receive the confirmation by email, usually within about 10 working days. A new driver (נהג חדש) may use the online report only if there were no casualties. In more serious cases, report by phone (110) or in person at a police station.

Attach the required documents: a copy of the ID, medical documents where anyone was hurt, a damage estimate in a casualty-free accident, scene photos or videos, and, when the person filing was the driver, a valid compulsory-insurance certificate for the day of the accident. **The classification trap:** the page warns that a report sent without medical documents will be classified as a damage-only event and not as a road accident, and that this classification can matter in dealings with insurers and in civil claims. A user who was hurt and files without the medical papers can damage their own PLATD claim.

### Step 4: Route the claim to the right regime

This is the core decision. Run the helper for a clean routing, or apply the same logic from `references/claims-guide.md` (agents that cannot run scripts should read the guide, which carries the full routing rules in prose):

```bash
python3 scripts/claim_router.py --damage none --injuries --my-fault no
python3 scripts/claim_router.py --damage property --my-fault yes --other-insured yes
python3 scripts/claim_router.py --damage property --hit-and-run --injuries --role pedestrian
python3 scripts/claim_router.py --injuries --role passenger --my-insured no --other-insured yes
```

- Bodily injury (anyone hurt): no-fault. Liability is `מוחלטת ומלאה` and it makes no difference whether the driver was at fault or whether others were at fault or contributorily negligent (PLATD §2(ג)). The allocation rule (PLATD §3(א)) decides which compulsory insurer pays: a driver and the passengers in a vehicle claim against that vehicle's own compulsory insurance (ביטוח חובה), and in a multi-vehicle crash each driver's own injury goes to his own vehicle's insurer, regardless of who was at fault. A pedestrian or cyclist claims against the vehicles that hit them, jointly and severally. Do not chase the other driver's compulsory insurer for your own injuries. Compulsory insurance covers bodily injury only, never property.
- Because the injury regime is exclusive (PLATD §8), a road-accident victim has **no** tort claim against the other driver for bodily injury, except where the accident was caused deliberately by another person. Never promise an injured user that they can "sue the other driver" for their injuries.
- No-fault has hard exceptions (PLATD §7): a person is NOT entitled to bodily-injury compensation if they caused the accident deliberately, drove without a valid licence, drove a vehicle without permission or a stolen one, used the vehicle for a felony, drove with no valid compulsory insurance, or, as owner or keeper, permitted another to drive uninsured and was hurt in that drive (§7(6)). The licence exception is narrow but wider than people think: a licence that lapsed only for non-payment of the fee, or because of a restriction imposed under chapter ו'1 of the Execution Law, still counts. Two safety valves exist: a person who drove by permission and neither knew nor could reasonably have known there was no insurance can claim from Karnit (§7א), and dependants can claim even where the victim himself was excluded by §7 (§7ב). If §7 applies, flag it and route to a lawyer. Do not tell the user whether a tort claim survives: §8(ג) preserves the tort claim of someone with no PLATD cause of action, and whether a §7-excluded person falls inside it is a case-law question for the lawyer, not something to assert either way.
- Who pays the medical bills: for a resident, the tortfeasor's duty does **not** cover health-basket services, which the kupat holim provides (PLATD §2(ב1)); the exceptions are the waiting period, a soldier outside the health law, and a person entitled to a work-injury benefit. Karnit likewise pays the hospital its treatment costs (§12(ב)).
- Property damage: fault-based, and it sits **outside** PLATD entirely, under the Torts Ordinance, which is why §8's bar does not touch it. The at-fault driver or their insurer pays. A not-at-fault driver can claim from their own comprehensive (מקיף) and let the insurer recover from the at-fault party by subrogation (the deductible is refunded once that succeeds), or claim directly against the at-fault driver's third-party (צד ג') cover, or sue them.
- Hit-and-run, untraced, or uninsured at-fault driver: Karnit (קרנית) compensates a victim who is entitled to compensation `ואין בידו לתבוע פיצויים מאת מבטח` (PLATD §12(א)). **That last condition is the whole test.** A driver or a passenger who was riding in their own insured vehicle when an untraced driver hit them still has an insurer of their own, because §3(א) puts them on their own vehicle's compulsory policy, so Karnit is NOT their address. Karnit is for the victim with no insurer of their own: a pedestrian or cyclist struck by an untraced vehicle, or an occupant of an uninsured vehicle, who goes to Karnit even when the other vehicle was insured and traced, because §3(א) makes only his own (uninsured) driver liable to him and §12(א)(2) then applies. The property side of a hit-and-run has no one to claim from: only the user's own comprehensive covers it, since Karnit pays bodily injury only.

### Step 5: Fill the accident report and submit

Walk the driver through the standard insurer report (הודעה על תאונה). It is one-sided, filed with their own insurer. It captures the insured and policy details, the driver, the accident details with a scene diagram and the impact zones and witnesses, the third-party details, and the insured's signed declaration. Notify the insurer immediately after the accident, then submit the form with the photos, the police confirmation, and a damage assessment.

### Step 6: Demand the urgent payment (תשלום תכוף)

This is the most valuable early right and most victims never hear of it. Whoever is liable under PLATD, and the compulsory insurer, must pay, within 60 days of a written demand, the victim's medical and hospitalization expenses and monthly payments covering treatment, nursing, and the living needs of the victim and his dependants (PLATD §5). The demand is made on the prescribed form with an affidavit; if the 60 days pass without payment, the victim applies to the Magistrates' Court, and the application can be filed separately from the main claim (§5א). Late payment carries linkage differences plus interest at 12% a year (§5ד). The court's decision is not res judicata for the main claim (§5ג). Two ceilings apply: no urgent payment is awarded for a period beyond two years from the accident, and once the court has decided, a further application needs six months to pass plus changed circumstances (§5ה).

### Step 7: How much, and what a lawyer may charge

Give the user the structure, not invented numbers. Non-pecuniary damage (כאב וסבל) is computed by regulation: two per mille (0.2%) of the statutory maximum per day of hospitalization, plus one percent (1%) of the maximum per point of permanent disability, with the disability component reduced by 1% for each year of the victim's age above 30 at the date of the accident. Where there is neither hospitalization nor permanent disability, or where the victim suffered non-pecuniary harm that the hospitalization and disability heads do not cover, the agreed or awarded sum for it is capped at 10% of the maximum (תקנה 2(ב) has both limbs, so a hospitalized or disabled victim is not limited to the formula). The whole non-pecuniary award may never exceed the maximum itself (PLATD §4(א)(3)), and where the victim died the estate receives 25% of the maximum. The maximum itself is CPI-linked, so quote the formula and look the current figure up rather than stating one from memory. Loss of earnings is capped at three times the average wage, pro-rated down where the loss of earning capacity is below 100% (PLATD §4(א)), and the tax gross-down may not reduce the base by more than 25%. A lawyer's contingency fee in a PLATD claim is capped by statute at 8% of an agreed sum, or 13% where there were legal proceedings, and anyone who paid more is entitled to a refund (PLATD §16(א)). See `references/compensation-and-deadlines.md`.

### Step 8: Deadlines, the medical expert, and the work-accident trap

Two limitation periods, and conflating them is the classic way to lose a claim. See Step 6 in `references/compensation-and-deadlines.md`. A lasting-injury claim is NOT decided by a ועדה רפואית: under PLATD §6א the court appoints a single medical expert (מומחה רפואי), and the parties may not bring further expert evidence except by leave of the court for special reasons. The ועדה רפואית is the Bituach Leumi mechanism, and that is exactly where the trap is: under PLATD §6ב a disability percentage determined under any other law before the evidence stage binds the PLATD claim too. Settling a low work-injury percentage at Bituach Leumi early can lock the civil claim at that figure. Get legal advice before that determination becomes final.

### Step 9: Know when a lawyer is needed

The law does not require a lawyer to start a claim, but for anything beyond minor injury you should still consult one, and the statutory fee cap makes that cheaper than most people assume. Frame it honestly: the skill helps document and understand rights, it does not replace a lawyer. If the insurer underpays or rejects unfairly, the driver can complain to the Public Inquiries Unit at the Capital Market, Insurance and Savings Authority (which does not bar going to court) and, for smaller property sums, file in small claims. Hand off to the israeli-small-claims-court skill for that.

## Examples

### Example 1: Rear-ended, not at fault, minor damage

User says: "Someone hit me from behind at a light. My bumper is cracked, nobody's hurt."
Actions:
1. Property-only, no injuries: exchange details, photograph, file the gov.il light-accident report for the police confirmation.
2. Route: not at fault. Claim from your own comprehensive and let them subrogate, or claim against the other driver's third-party cover.
3. Run `python3 scripts/claim_router.py --damage property --my-fault no --my-comprehensive`.
Result: A scene checklist and a claim plan, the deductible-refund explanation, and the warning that a claim for insurance benefits against your own insurer prescribes in three years from the accident, not seven.

### Example 2: Injury accident

User says: "I was in a crash, my passenger hurt her neck and went to the ER."
Actions:
1. Injuries: police involvement is mandatory, get the police confirmation, and attach the medical documents so the event is classified as a road accident.
2. Route: bodily injury is no-fault. The passenger claims from the compulsory insurance of the car she was in, regardless of fault, and she has no tort claim against the other driver for the injury (§8).
3. Raise the urgent payment (§5) and flag that a lasting-injury claim should go to a lawyer, whose fee is capped at 8% or 13%.
Result: The no-fault explanation, the documentation list, the urgent-payment demand, and a lawyer referral for the injury side.

### Example 3: Hit and run in a car park

User says: "Someone scraped my car in a lot and drove off, and I twisted my wrist getting out."
Actions:
1. Hit-and-run with injury: report to police, get the confirmation, attach the medical documents.
2. Route the injury: getting out of the vehicle (`ירידה ממנו`) is use of a motor vehicle under PLATD §1, so this is a road accident and it goes to **his own vehicle's compulsory insurer** under §3(א). Karnit is not the address, because he has an insurer of his own (§12(א)).
3. Route the property: the scrape is fault-based and outside PLATD, so it falls on his own comprehensive if he holds one.
Result: Own חובה for the wrist, own מקיף for the scrape, and an explicit correction of the common belief that any hit-and-run means Karnit.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Road Accident Victims Compensation Law 1975 (PLATD, Nevo) | https://www.nevo.co.il/law_html/law00/4554.htm | No-fault liability, exclusions, urgent payment, medical expert, Karnit, fee cap |
| Non-pecuniary damage regulations 1976 (Nevo) | https://www.nevo.co.il/law_html/law00/4555.htm | The כאב וסבל formula, the age reduction, the death award |
| Insurance Contract Law (Nevo) | https://www.nevo.co.il/law_html/law00/71902.htm | The duty to notify, the three-year limitation, subrogation |
| Limitation Law 1958 (Nevo) | https://www.nevo.co.il/law_html/law00/71809.htm | The seven-year tort period and the minors rule |
| National Insurance Law (Wikisource) | https://he.wikisource.org/wiki/חוק_הביטוח_הלאומי | §328א: no subrogation against the motor insurer, benefits netted off the award |
| Traffic Regulations (Nevo) | https://www.nevo.co.il/law_html/law01/p230_011.htm | The scene duties for injury and property accidents |
| gov.il online accident report | https://www.gov.il/he/service/traffic-accident-notice | Eligibility, required attachments, and the classification warning |
| Kol Zchut, road-accident bodily-injury claim | https://www.kolzchut.org.il/he/תביעה_לקבלת_פיצויים_בגין_נזקי_גוף_בתאונת_דרכים | The e-bike and e-scooter carve-out |
| Kol Zchut, hit-and-run and Karnit compensation | https://www.kolzchut.org.il/he/פיצוי_על_תאונת_פגע_וברח | When Karnit pays bodily-injury compensation |
| Capital Market, Insurance and Savings Authority, public inquiries | https://www.gov.il/he/pages/consumer-info-public-inquiries | Complaining about an insurer |

## Bundled Resources

### Scripts
- `scripts/claim_router.py` -- Routes the claim to the right insurance or to Karnit and lists the time limits, from the injury/fault/insured inputs. Run: `python3 scripts/claim_router.py --example`

### References
- `references/claims-guide.md` -- The scene and routing guide: the 3 insurance types, no-fault vs fault, scene duties, exclusions and their safety valves, Karnit, subrogation.
- `references/compensation-and-deadlines.md` -- The money and the clock: urgent payment, compensation heads, the fee cap, court fees, the two limitation periods, the medical expert, and the Bituach Leumi interaction.
- `references/domain-checklist.md` -- The coverage contract for this skill.

## Gotchas

- The limitation period against your OWN insurer is three years, not seven. A claim for insurance benefits (a מקיף or other own-policy claim) prescribes three years after the insured event, running from the accident and NOT from the day the insurer rejected it. The seven-year figure belongs to the tort claim against the at-fault driver and to the PLATD bodily-injury claim. Telling a user "you have seven years" for their own comprehensive claim is the single most harmful error this skill can make.
- Karnit is not the address whenever the other driver fled. Karnit is only for a victim who has no insurer of their own. An occupant of an insured vehicle hit by an untraced driver claims from their own compulsory insurance, because the allocation rule already gives them a carrier.
- Bodily injury is no-fault, property is fault-based. Injuries are claimed from the compulsory insurance regardless of fault; property damage follows fault and lives outside PLATD. Never tell an injured passenger they cannot claim because the driver was at fault, and never tell them to sue the other driver for the injury.
- Compulsory insurance never covers property. ביטוח חובה is bodily injury only. Your own car's dents are covered only by comprehensive (מקיף), and damage you cause to others' property by third-party (צד ג').
- A lasting-injury claim goes to a court-appointed expert, not a ועדה רפואית. Confusing the PLATD medical expert with the Bituach Leumi committee misinforms the victim about the single most consequential step in the case.
- Do not let a Bituach Leumi disability percentage be fixed before taking advice. A determination under another law before the evidence stage binds the PLATD claim (§6ב).
- Electric bikes and scooters are outside PLATD. Kol Zchut states that under court rulings `אופניים וקורקינטים חשמליים לא נחשבים כרכב מנועי` under PLATD, because the definition requires a vehicle whose main purpose is land transport. An injured e-bike or scooter rider has no no-fault claim: the routes are an ordinary negligence action or דמי תאונה לנפגעי תאונות אישיות from Bituach Leumi. This bites often, because the skill's readers are as likely to be the rider as the driver.
- Filing the online report without medical documents can be self-harm. It gets the event classified as damage-only rather than a road accident, which the police page itself warns can matter against insurers and in civil claims.
- Accidents abroad are not covered by PLATD. The law extends only to the Area, the Palestinian civil-responsibility territories, and the Areas under the Israel-Jordan implementation law. There is no general accident-abroad rule here; treat any other foreign accident as out of scope and route to a lawyer.
- Do not say "no lawyer needed" for an injury claim. State the rights, then recommend a lawyer for anything beyond minor injury.

## Troubleshooting

### Error: "The other driver was at fault, so my injuries are their insurance's problem"
Cause: Applying property (fault) logic to bodily injury.
Solution: Bodily injury is no-fault. The injured person claims from the compulsory insurance of the vehicle they were in or hit by, regardless of who was at fault. Fault matters for the property side, not the injury side.

### Error: "My own car is damaged but I only have compulsory insurance"
Cause: Expecting compulsory insurance to cover the vehicle.
Solution: Compulsory insurance covers bodily injury only. Your own car's damage is covered only if you hold comprehensive (מקיף). If you are not at fault, you can still claim your car's damage against the at-fault driver's third-party cover or sue them directly. That property claim is fault-based and sits outside PLATD.

### Error: "The other driver drove off, so I go to Karnit"
Cause: Treating hit-and-run as an automatic Karnit case.
Solution: Karnit applies only where the victim cannot claim from any insurer. If you or your passengers were in your own insured vehicle, your own compulsory insurer pays the bodily injury even though the other driver is untraced. Karnit is for a pedestrian or cyclist struck by an untraced vehicle, or an occupant of an uninsured vehicle. Your car's own damage goes to your comprehensive policy either way.

### Error: "My insurer rejected the claim, so the clock restarts from the rejection"
Cause: Assuming the limitation period runs from the rejection or that negotiation stops it.
Solution: The three-year period for insurance benefits runs from the insured event, and delivering the claim to the insurer does not stop it. In liability insurance there is an extension: the claim does not prescribe while the third party's claim against the insured is still alive, so a צד ג' route can track the third party's longer period. The insurer must warn you in writing 12 months and again 3 months before the period ends, but do not rely on that warning arriving.
