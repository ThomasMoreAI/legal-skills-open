---
name: israeli-consumer-claim-kit-skills-il
title: Israeli Consumer Claim Kit
description: Not legal advice. Drafts Israeli consumer demand letters, cancellation notices and complaints that the user signs and sends. Use when a technician, delivery or gas inspection was hours late or never came (chok hatechnaim), when cancelling a purchase made online, by phone, at the door, at a sales event or in a shop, or a subscription (bitul iska), including the 4-month right for seniors, olim and people with disabilities, when a warranty repair is refused or overdue, or when complaining to the Consumer Protection Authority or the Consumer Council. It works out the statutory figure first (300 or 600 NIS, the cancellation deadline, the fee cap) because guides often get these wrong. Do NOT use for filing the court claim itself (use israeli-small-claims-court), for seller-side compliance (use israeli-ecommerce-compliance), for flight compensation (use israeli-flight-compensation), or for bank and card fees (use israeli-consumer-fee-fighter).
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-consumer-claim-kit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: consumer
language: en
sources:
- title: Domain Checklist
  path: references/domain-checklist.md
- title: Rules And Letters
  path: references/rules-and-letters.md
---

# Israeli Consumer Claim Kit

## Legal notice

This is a free information tool operated by an AI model. It explains consumer-protection law and helps you organise your own demand letter or complaint. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.

## Problem

The technician never showed up, the online order arrived broken, a telemarketer sold your father something he did not need, or the lab has held your washing machine for a month. Israeli consumer law gives fixed, specific rights in each of these cases, but most people do not know the exact figures, and the popular "2 hours late = 300 NIS" rule is itself wrong. A short written demand that cites the right section is usually what gets the refund, and it is also the written request the law requires before suing for exemplary damages.

## Problem boundary

This skill covers a consumer (a private person) against a dealer (a business), under the Consumer Protection Law 1981, the 2010 Cancellation Regulations and the 2006 Warranty Regulations. It does not cover deals between two private people, business-to-business deals, purchases from foreign websites, flights, banks, insurance or rentals.

## Instructions

### Step 0: Classify the case

Ask what happened, then pick a track. If two apply (a late technician on a warranty repair, or an elderly buyer who was also pressured), run both and combine them in one letter.

| Track | Trigger | Main sources |
|---|---|---|
| A. Late or no-show visit | Technician, installer, delivery, gas inspection, cable/router service | CPL s.18A(c)-(f) |
| B. Cancel a purchase | Bought by phone, online, at the door, at a sales event, in a shop, or a subscription, and wants out | CPL s.14, s.14C, s.14C1, s.14E, s.13D; Cancellation Regs 2010 |
| C. Warranty repair | Electrical, electronic or gas product not repaired, repaired late, or charged for | Warranty Regs 2006 |
| D. Exploited consumer | Pressure, exploitation of a disability, or a buyer who did not understand the language of the deal | CPL s.3 and s.32, plus s.14C1 for seniors, olim and people with disabilities, plus a complaint to the Authority (Chapter E2) |

### Step 1: Collect the facts before computing anything

- Dates: deal date, delivery date, date the written disclosure document arrived (if ever), date of refusal.
- How the deal was made: online checkout, phone call, chat, in a shop, at a sales event, or **did the seller call and then come to the home?** That last pattern is door-to-door under the statute, not a distance sale, and it changes the money rules.
- Track A: what the visit was for (it must be one of the covered categories), the coordinated hour, arrival time or "never came", whether a postponement notice arrived and when.
- Status: age, oleh certificate date, disability certificate (Tracks B and D).
- In-store: what the item is, whether it was used, plugged in or assembled at home, and whether the user has the receipt.
- Price, payment method (card, instalments, standing order), and any posted return-policy sign.
- What the user already asked for, in writing or by phone.

Never assume a missing date. Ask for it, because every deadline below runs from the LATER of several dates.

### Step 2: Compute the statutory result

Run the helper if code execution is available, otherwise apply the tables by hand:

```bash
python3 scripts/claim_check.py technician --category warranty --coordinated 10:00 --arrived 14:20
python3 scripts/claim_check.py cancel --type distance --received 2026-10-01 --price 1200 --status senior --conversation
python3 scripts/claim_check.py cancel --type instore --goods listed --received 2026-10-01 --price 900
```

**Track A, technician law (CPL s.18A).** Covers ONLY: warranty work (including extended warranty), service that depends on equipment at the consumer's home, installation or removal of goods the same dealer sold, rented or lent, periodic home gas inspections, delivery of goods the dealer sold, and paid continuing repair contracts. A one-off paid call-out (a plumber or electrician the user hired once) is not on the list, so the fixed amounts do not apply to it.

| Rule | Value |
|---|---|
| Waiting window | No more than two hours past the coordinated time (s.18A(c)(2)) |
| Visiting hours (warranty, equipment service, installation, gas) | 8:00 to 19:00 on weekdays, 8:00 to 13:00 on Fridays and holiday eves |
| Valid postponement | Notice no later than 20:00 the evening before, with a new agreed date and hour, and only if it does not push the service past its legal deadline (s.18A(c)(3)). It does not cancel the right: lateness is then counted from the NEW agreed hour |
| NIS 300 | Once two hours have passed BEYOND the two-hour waiting window |
| NIS 600 | Once three hours have passed beyond the waiting window |
| NIS 300 | For breaching the "wait for our call" alternative rules (instead of a coordinated hour) |
| Proof | No proof of damage needed |
| In kind | A voucher or service instead of cash only if the consumer was told they may choose cash and agreed; the provider must prove it |
| Defence | No compensation if the delay came from circumstances the provider did not know of, and should not have known of, when the appointment was set, or could not have foreseen, AND could not prevent (s.18A(f)) |

So for a 10:00 appointment, arrival at 12:00 is lawful, NIS 300 is owed from 14:00, and NIS 600 from 15:00. If nobody came at all, NIS 600 applies once 15:00 passed. The right depends on the time passing, not on the user staying home, but the user has to be able to show nobody came: being home until then, the company's own record, or a call log. A user who left at 11:00 cannot know whether the technician came at 12:30, so ask. The statute counts from "the hour that was coordinated". If the company gave a range instead of an hour, say so to the user and show the figure counted from the end of the range as the safer claim.

**Track B, cancellation.**

| Deal type | Period | Source |
|---|---|---|
| Distance sale (online, phone, mail), goods | 14 days from receipt of the goods or of the disclosure document, whichever is later | s.14C(c)(1) |
| Distance sale, one-off service | Within 14 days and at least two non-rest days before the service | s.14C(c)(2) |
| Door-to-door, including a phone approach followed by the seller coming to the home | 14 days from delivery or receipt of the required details, whichever is later | s.1 definition, s.14(a)(1) |
| Senior (65), oleh (less than five years since the certificate), person with a disability | Four months: for door-to-door deals (s.14C1(b)), and for distance deals ONLY if the deal included a conversation with the dealer, electronic included (s.14C1(c)) | s.14C1 |
| Continuing deal (subscription) | Ends within three business days of notice, six business days if sent by registered mail | s.13D(c) |
| In-store, schedule goods above NIS 50: furniture, home and garden equipment, electrical and electronic devices, unopened goods, ordered goods not yet supplied, water purifiers, watches | 14 days from receipt | Cancellation Regs reg.2(1) |
| In-store, clothing and footwear | Two non-rest days after purchase, price tag not removed | reg.2(2) |
| In-store, jewelry up to NIS 3,000 | Two non-rest days after purchase | reg.2(7) |
| In-store services in schedule items 10-19 (cosmetics, long-term vacation clubs, discount clubs, telecom and internet providers, broadcasters, gyms, dating clubs, lotteries) | 14 days from the deal or the written contract, whichever is later, even if the service started | reg.2(4) |
| Goods or services bought at a sales event the dealer invited people to | Goods: 14 days from receipt. A one-off service: within 14 days and at least two non-rest days before it starts | reg.2(5), schedule item 20 |

In-store conditions (reg.2-3): the goods must be returned undamaged and unused. Return in the original packaging is enough proof of non-use. For furniture, home equipment, electrical devices, water purifiers and watches, opening the packaging is not use by itself, but **connecting to electricity, gas or water is use**. The user must show an invoice, till slip or exchange note. A franchisee that posts a notice may refuse refunds for goods bought at another branch (reg.3(e)). Items not on the schedule have no statutory in-store right; only the shop's posted policy applies.

Money rules:

- **Door-to-door:** the dealer returns the full price paid, with NO cancellation fee. Only an installation charge of up to NIS 100 is allowed (s.14(b)). The same applies to the 4-month door-to-door right.
- **Distance, no reason given:** refund within 14 days of the notice, and the dealer must cancel the charge and give a copy of the charge-cancellation notice. The fee is capped at 5% of the price or NIS 100, whichever is LOWER, and shipping and packaging count inside that cap (s.14E). Installation charge capped at NIS 100.
- **Distance, because of a defect, non-conformity, late delivery or other dealer breach:** refund within 14 days and NO fee at all (s.14E(a)(1)).
- **In-store:** refund no later than seven business days, same payment method; fee capped at 5% or NIS 100, whichever is lower, plus a card-clearing charge only if the shop proves it paid one (regs 4-5).
- **Instalments for goods never delivered:** after notifying the dealer of cancellation, the user can tell the card issuer to stop the remaining guaranteed payments (Payment Services Law 2019, s.17).
- **Return-policy sign (s.4C):** if the shop breaches its own posted policy, the consumer may return within seven days of the refusal for full price in the original payment method. If no sign is posted, the shop is presumed to allow returns.
- The dealer may ask a senior, oleh or person with a disability for one certificate proving status and may not demand further proof (s.14C1(d)).
- Exclusions exist (perishables, food, made-to-measure goods, furniture assembled in the home, jewelry above NIS 3,000, travel within seven non-rest days of the service, and more). Check `references/rules-and-letters.md` before demanding a refund.

Valid ways to send a cancellation (s.14I): by phone or in person, registered mail, email, fax if the dealer has one, or the dealer's website link. Always prefer a written channel the user can prove.

**Track C, warranty (Warranty Regs 2006).** Applies to new electrical, electronic and gas products, including mechanisms in furniture (a recliner, an adjustable bed), above NIS 150. Minimum warranty one year.

| Duty | Rule |
|---|---|
| Home-repair items (Second Schedule) | Repaired at the consumer's home (reg.7(a)). When the fault prevents main use: refrigerator and freezer within one day, cooking stove within two days, washing machine, air conditioner, oven, TV above 20 inch, dishwasher and dryer within 3 days (reg.10(c)) |
| Other goods | One week from the call, ten days from delivery to a service station, or two weeks if left at the point of sale (reg.10(a)); a dealer liable instead of the manufacturer has three weeks |
| Counting | Sabbaths and holidays are not counted (reg.10(d)) |
| Repair fails to restore the goods | New equivalent goods or a refund, at the MANUFACTURER'S choice (reg.6(c)). This is the remedy for a failed repair, not for a late one |
| Technician late more than twice in a row in the repair period | The manufacturer is in breach (reg.11(c)) |
| Spare parts | Through the warranty, plus one more year for goods above NIS 300; longer periods for the appliances listed in the First Schedule (reg.3(c)) |
| Charging for a repair | Only if the manufacturer proves, BEFORE repairing, that the fault came from force majeure after delivery, the consumer's malice or negligence, or an unauthorised repair (reg.8) |
| Manufacturer cannot be found | A dealer that sold goods above NIS 400 carries the duties (reg.19) |

For a LATE repair the demand is: complete the repair now. Failure to repair under warranty is on the s.31A list, so the letter can serve as the written request for exemplary damages.

**Track D, exploited consumer.**

- Seniors, olim and people with disabilities: use the 4-month right above when it applies.
- After those 4 months, or for anyone else: exploiting a consumer's mental, cognitive or physical limitation, or the fact that the consumer did not understand the language of the deal well enough, is unfair influence (s.3(b)(5)-(6)). Under s.32 the consumer may cancel within a **reasonable time** from when the exploitation ended, and the dealer refunds within seven days, the same way the consumer paid. This is not a fixed deadline, so tell the user to act quickly and describe the facts precisely.
- Also file a detailed complaint with the Authority (Step 5).

**Exemplary damages (s.31A), the lever behind Tracks B and C.** A court may award up to NIS 10,000 per breach without proof of damage, and up to NIS 50,000 for a repeat, continuing or aggravated breach, but ONLY for breaches on the s.31A list (refusing a distance-sale refund, charging after a subscription was cancelled, breaching the return-policy sign, failing to repair under warranty, and others). The technician law is NOT on that list; it has its own fixed 300 or 600. A suit for exemplary damages requires a prior written request (email counts), which is what the letter in Step 3 is.

### Step 3: Draft the letter

Use the building blocks in `references/rules-and-letters.md`. Rules:

1. Hebrew by default (it is going to an Israeli business); offer an English or Russian copy for the user's own reading.
2. Open with the facts and dates, then the exact section, then ONE concrete demand with an amount and a deadline (seven days is a reasonable default, and it is a choice, not a statutory period).
3. Quote the figure the statute gives, never a bigger one. Do not threaten exemplary damages for a breach that is not on the s.31A list.
4. For a cancellation, the letter IS the cancellation notice: include the user's name and ID number, the deal details, and the words "הריני מודיע/ה על ביטול העסקה". Cite the section that matches the deal type: s.14 for door-to-door, s.14C for distance, s.14C1(b) or (c) for the 4-month right, s.32 for exploitation.
5. For a card or instalment payment, ask for a copy of the charge-cancellation notice.
6. For Track D, add a line that the user is a senior, oleh or person with a disability and attach the certificate.
7. End with the escalation path: Consumer Council, Authority complaint, small claims. Do not promise an outcome.
8. Leave signature, ID number and contact details as placeholders the user fills in.

### Step 4: Send and keep proof

Email with a read receipt, the company's website form (screenshot the confirmation), or registered mail. Keep the coordination SMS, the call log, photos, and the receipt. The Consumer Council handles a complaint only after the consumer approached the business in writing, so this step is not optional.

### Step 5: Escalate if there is no answer

| Route | What it does | What it does NOT do |
|---|---|---|
| Israel Consumer Council complaint form | Takes up an individual complaint, after a written approach to the business | Not a court; cannot force payment |
| Consumer Protection and Fair Trade Authority | Uses complaints for investigation, supervision and enforcement | Does not recover money for an individual |
| Small claims court | Can order payment, up to NIS 39,900 in 2026 | Hand off to `israeli-small-claims-court` for the filing itself |

**Track D extra:** Chapter E2 of the Consumer Protection Law, added in 2024 (reported to take effect on 4 October 2024), lets the Commissioner declare a dealer an "aggravated violator" when it targets seniors, olim, people with disabilities, minors or people who did not know the language of the deal. Payment providers then stop paying the dealer, and the Execution Office stops new collection files, closes existing ones and returns the money collected to the debtors (s.22LB(b)). A consumer cannot trigger this directly. The route is a detailed complaint to the Authority, so for an exploited parent, file the Authority complaint in addition to the cancellation letter.

## Examples

### No-show technician

User: "The cable company set a technician for 10:00, nobody came, I waited until 17:00."
Track A: a converter or router service is a covered category. Nobody came at all, so once 15:00 passed the full NIS 600 is owed. Ask whether a postponement SMS with a new agreed time arrived by 20:00 the previous evening; if so, count from the new time. Draft a demand for NIS 600 in cash or as a bill credit, seven-day deadline, Consumer Council then small claims as escalation. Do not add exemplary damages.

### Elderly parent, phone call then a home visit

User: "My father, 80, got a call, a salesman came to the house and sold him an expensive vacuum, two months ago."
A call followed by a visit to the home is door-to-door under the statute, and he is a senior, so he has four months under s.14C1(b). The refund is the full price with no cancellation fee (s.14(b)). Draft the notice in his name with his ID number, attach his senior certificate, ask for a copy of the charge cancellation if he paid by card, and add an Authority complaint describing the sales pressure. If the four months have passed, use s.32 if the facts show exploitation.

### Sofa bought in a shop last week

Furniture is on the in-store schedule: 14 days from receipt, provided it is returned undamaged and unused, with the receipt. A sofa that was sat on for a week may be argued to be "used", so say that the shop may contest it. If it was assembled in the home (by anyone), the reg.6 exclusion applies and there is no statutory right; check the shop's posted policy instead.

### Refrigerator not repaired

Track C: a refrigerator is a home-repair item, and when the fault stops it cooling, the repair must be completed within one day of the call, Sabbaths and holidays not counted. Demand immediate repair, note that failure to repair under warranty is on the s.31A list, and keep the call log.

## Recommended MCP Servers

| MCP | Use it for |
|---|---|
| `kolzchut` | Search Kol Zchut for the current consumer-rights page when the user's case falls outside the tables above |

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Consumer Protection Law (consolidated) | https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%94%D7%92%D7%A0%D7%AA_%D7%94%D7%A6%D7%A8%D7%9B%D7%9F | s.1, s.3, s.4C, s.13D, s.14, s.14C, s.14C1, s.14E, s.14I, s.18A, s.31A, s.32, Chapter E2 |
| Cancellation Regulations 2010 | https://he.wikisource.org/wiki/%D7%AA%D7%A7%D7%A0%D7%95%D7%AA_%D7%94%D7%92%D7%A0%D7%AA_%D7%94%D7%A6%D7%A8%D7%9B%D7%9F_%28%D7%91%D7%99%D7%98%D7%95%D7%9C_%D7%A2%D7%A1%D7%A7%D7%94%29 | In-store periods, exclusions, refund deadline |
| Payment Services Law 2019 | https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%A9%D7%99%D7%A8%D7%95%D7%AA%D7%99_%D7%AA%D7%A9%D7%9C%D7%95%D7%9D | s.17, stopping instalments for goods never delivered |
| Warranty Regulations 2006 | https://he.wikisource.org/wiki/%D7%AA%D7%A7%D7%A0%D7%95%D7%AA_%D7%94%D7%92%D7%A0%D7%AA_%D7%94%D7%A6%D7%A8%D7%9B%D7%9F_%28%D7%90%D7%97%D7%A8%D7%99%D7%95%D7%AA_%D7%95%D7%A9%D7%99%D7%A8%D7%95%D7%AA_%D7%9C%D7%90%D7%97%D7%A8_%D7%9E%D7%9B%D7%99%D7%A8%D7%94%29 | Repair deadlines, failed-repair remedy |
| Authority complaint form | https://www.gov.il/he/service/filing_a_complaint_to_fair_trade_authority | Online complaint |
| Consumer Council complaints | https://www.consumers.org.il/category/complaint-form | Individual complaint forms |
| Kol Zchut, late technician | https://www.kolzchut.org.il/he/%D7%A4%D7%99%D7%A6%D7%95%D7%99_%D7%91%D7%92%D7%99%D7%9F_%D7%90%D7%99%D7%97%D7%95%D7%A8_%D7%98%D7%9B%D7%A0%D7%90%D7%99_%D7%90%D7%95_%D7%90%D7%99%D7%A9_%D7%A9%D7%99%D7%A8%D7%95%D7%AA | Plain-language summary |

## Bundled Resources

- `scripts/claim_check.py`: offline calculator for the technician tier and cancellation deadlines and fees.
- `references/rules-and-letters.md`: exclusions, letter building blocks in Hebrew, escalation wording.
- `references/domain-checklist.md`: coverage contract and known bad figures.

## Gotchas

- **The 2-hour figure is the waiting window, not the trigger.** Agents repeat "more than 2 hours late = NIS 300". The statute pays NIS 300 only two hours BEYOND the two-hour window, and NIS 600 three hours beyond it.
- **The 4-month right is narrow.** It covers door-to-door deals and distance deals that included a conversation. A plain online checkout gets 14 days, and there is no 4-month right in a shop.
- **"Phone sale" is often door-to-door.** If the seller called and then came to the home, the deal is door-to-door under the statute: full refund, no cancellation fee. Agents treat it as a distance sale and wrongly allow a 5% fee.
- **The in-store right is conditional.** Only schedule goods above NIS 50, returned undamaged and unused, with a receipt. Plugging in an appliance counts as use, and furniture assembled in the home is excluded.
- **A fridge is not a one-week repair.** Second Schedule home-repair items have deadlines of one to three days when the fault prevents main use.
- **The fee cap is the LOWER of 5% or NIS 100**, and there is no fee at all when cancelling because of the dealer's breach. Agents often invert this.
- **Do not inflate the claim with exemplary damages.** NIS 10,000 is a maximum a court may award, only for breaches on the s.31A list, and the technician law is not on it.
- **"The Authority will get your money back" is false.** It is an enforcement body. Money comes from the dealer, the Consumer Council's handling, or small claims.
- **"Three failed repairs means a new product" is not in the Warranty Regulations.** When a repair fails, the manufacturer chooses between new goods and a refund.
- **After the 4 months, the elderly buyer is not out of options.** s.32 allows cancelling a deal made through exploitation within a reasonable time after the exploitation ended.
- **The aggravated-violator law is from 2024** and is not new.

## Troubleshooting

| Symptom | Cause | What to do |
|---|---|---|
| Company says compensation is only a voucher | s.18A(e) allows in-kind compensation only with informed consent | Demand cash; the provider must prove consent |
| Company says the technician was "delayed by an earlier call" | That is a foreseeable delay, not necessarily the s.18A(f) defence (interpretation, not a ruling) | Keep the demand; let the company prove the exception |
| Shop refuses to cancel a sale item | The item may or may not fall under a reg.6 exclusion; the posted return-policy sign also binds the shop | Check reg.6 first, then cite reg.2 or s.4C |
| Dealer demands several documents to prove age | s.14C1(d) allows one certificate only | Send one certificate and cite the section |
| No reply after the deadline | Normal | Escalate per Step 5; hand off to `israeli-small-claims-court` |
