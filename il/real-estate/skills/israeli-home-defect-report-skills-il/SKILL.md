---
name: israeli-home-defect-report-skills-il
title: Israeli New-Apartment Defect Log
description: Not legal advice. Helps a buyer of a new Israeli apartment document construction defects and act in time. Builds a room-by-room handover walkthrough, turns findings into a dated defect log for the protokol mesira, works out which statutory window each defect falls in under the Sale (Apartments) Law 1973 and who must prove what, and drafts a Hebrew repair-demand letter. Use when a user says "bedek bait", "protokol mesira", "likuyim badira", "the contractor will not fix", or "is it too late to complain". It matters because periods run from handover, differ by defect type, and differ again for flats bought before April 2011, so a missed notice deadline can forfeit a good claim. Produces a log and a letter, not an engineering opinion. Do NOT use to assess structural safety or load-bearing damage (needs a licensed engineer), to value repairs, for late-delivery compensation, for rental defects (use israeli-rental-agreements), or for a self-built home (use israeli-private-home-construction).
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-home-defect-report
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: real-estate
language: en
sources:
- title: Domain Checklist
  path: references/domain-checklist.md
- title: Periods And Burdens
  path: references/periods-and-burdens.md
- title: Walkthrough And Letter
  path: references/walkthrough-and-letter.md
---

# Israeli New-Apartment Defect Log

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate or an engineer. The output is not legal advice, not a legal opinion, and not an engineering opinion (chavat daat handasit). It is a general explanation and a template only: it does not inspect your apartment, does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. A claim that the contractor disputes, and anything intended for a court, needs a licensed engineer (mehandes) for the opinion and a licensed advocate (orech din) for the claim. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. All use of its output is the user's sole responsibility.

## Problem

Buyers of a new apartment are handed the keys under time pressure, asked to sign a handover protocol on the spot, and told that anything they do not raise now is their own problem. Almost none of that pressure reflects the law: liability cannot be waived, the periods run for years, and the burden of proof sits on the contractor for most of them. What buyers actually lose rights to is narrower and more specific, a one-year notice deadline for anything that was visible on the day. The periods themselves are widely misreported, they differ per defect type, and they are different again for apartments bought before April 2011, so buyers routinely give up on claims that are still live and chase claims that closed years ago. This skill turns a walkthrough into a dated log, works out which window each defect is actually in, and drafts the written demand that every later remedy depends on.

## Problem boundary

This skill documents and times defects in a new apartment bought from a contractor. It does not assess structural safety and does not decide whether a defect is load-bearing, because that is a licensed engineer's call and getting it wrong is dangerous. For a home you are building yourself on your own land, use `israeli-private-home-construction`. For defects in a rented apartment, use `israeli-rental-agreements`. For the separate money claim over late delivery, and for guarantees protecting your payments, see the Gotchas section, both are out of scope here.

## Instructions

You help a buyer document defects, work out the timing, and write the demand letter. Read `references/periods-and-burdens.md` before answering any timing question and `references/walkthrough-and-letter.md` before building a log or drafting a letter.

### Step 0, safety gate, run this first and every time

Before anything else, scan what the user describes for these signals:

- cracks in a load-bearing element, or any crack that is growing, stepped, or runs through a beam, column or ceiling slab
- floors or ceilings sagging, doors or windows suddenly binding, visible movement of the structure
- water reaching electrical fittings, a distribution board, or a socket
- a smell of gas, or an exposed live conductor
- anything falling from an exterior facade or a balcony

If any appear, stop the documentation workflow and say so plainly. Tell the user this needs a licensed engineer now, and where there is an immediate hazard, emergency services. Do not classify the defect, do not estimate severity, do not put it in the log as though it were an ordinary snag, and do not continue to the letter. You may resume the normal workflow for the user's other, unrelated defects once you have flagged this.

Stopping the classification does NOT mean stopping the clock. Notice for a hidden fundamental defect is due within a reasonable time of DISCOVERY (s.4a(b)), and engaging an engineer takes weeks. So still tell the user to send the contractor a short dated written notice now, describing only what they observed and saying an engineer's opinion will follow. Describe, date, send. Do not classify.

Never tell the user whether a defect is or is not an "ai hat'ama yesodit" (fundamental non-conformity). That classification decides whether the 20-year regime applies and it belongs to an engineer. Tell them the category exists, that it runs 20 years, and that only an engineer can place a defect in it.

### Step 1, establish the four dates

Everything downstream depends on these. Ask for whichever are missing and do not guess:

| Date | Why it matters |
|---|---|
| Handover (hadmadat hadira lirshut hakone) | Starts every bedek period. It is the date you actually got possession, not the contract date, and not the protocol date if that differs |
| Sale contract signature | Selects WHICH schedule of periods applies. The old schedule governs if EITHER the contract was signed before 06.04.2011 OR construction finished before it, so ask about both |
| Discovery of the defect | Places the defect in the bedek window, the warranty window, or outside both |
| Written notice to the contractor, if already sent | Tests the one-year notice deadline |

If the user is at the handover and has not received the keys yet, the handover date is today and you go to Step 2. If they already live there, go to Step 3.

One case people get wrong: a buyer who bought a nearly-new apartment from its first owner rather than from the contractor (a kone mishne) still holds these rights against the contractor. The clock does not restart on resale, it runs from the ORIGINAL handover to the first buyer, so ask for that date and not the date of their own purchase.

### Step 2, the walkthrough (before or at handover)

Work room by room. Use the checklist in `references/walkthrough-and-letter.md`, and adapt it, do not read it out mechanically. For every finding record: room, what it is, whether it is visible today, a photograph with something for scale, and the date. Visibility is not cosmetic bookkeeping, it selects which notice rule applies later, so ask about it for every item.

Raise the professional inspection here, not later. A בדק בית report from a licensed inspector or מהנדס, commissioned BEFORE the protocol is signed and attached to it, is both the cheapest and the most probative it will ever be: inside the bedek period the burden is on the contractor, so the report is doing its work at the moment the law is already on the buyer's side. Say it is worth considering and let the user decide. You still never classify anything yourself.

Then, on the protocol itself:

- The contractor cannot lawfully strip its liability, so do not let a signature panic the user. A waiver of defect liability is ineffective even if the buyer signed it freely, and a waiver made a condition of getting the keys is void outright.
- What a signature CAN do is create an evidentiary problem. Signing a statement that the apartment is defect-free is a factual admission a court will weigh, whatever the waiver rules say.
- So the advice is not "refuse to sign". It is: attach the written defect list, have it referenced on the protocol, keep a signed or photographed copy, and never sign wording like "the apartment was received to my full satisfaction" or "I have no comments" while there are open items.
- If the contractor refuses to record the reservations, note in handwriting on the protocol that the signature confirms receipt of possession only and not acceptance of the apartment's condition, and photograph it before handing it back.

### Step 3, work out the window for each defect

First check whether the Schedule is even needed. Under s.4(a)(1) the contractor is in breach if the apartment differs from the מפרט, from an official standard, or from the building regulations, full stop. That does not depend on a row, a period, or a burden. It is the route to raise when a Schedule window has closed, and it is the one most buyers never hear about. It escapes the Schedule, NOT the notice duty: s.4(b) deems it an אי-התאמה, so s.4a still applies and a specification deviation visible on handover day is barred by the same one-year rule. Run the notice analysis on it too.

Then use the helper script rather than doing the arithmetic in your head:

```bash
python3 scripts/defect_window.py --handover 2021-03-15 --contract 2020-11-01 \
  --discovered 2026-01-10 --type pipes --visible no
```

`python3 scripts/defect_window.py --list` prints both schedules. If a host cannot run scripts, do the arithmetic yourself from the tables in `references/periods-and-burdens.md`, and show your working so the user can check it.

Two clocks run independently and BOTH have to be satisfied. This is the single most common mistake in this domain, so state both explicitly every time:

1. The period for that defect type, which decides who must prove what.
2. The notice duty, which has three limbs. Visible at handover means notice was due within one year of handover (s.4a(a)(1)). Hidden means within a reasonable time after discovery, however long after handover that falls (s.4a(a)(2)). And a hidden FUNDAMENTAL defect has its own limb with no one-year cut-off at all (s.4a(b)), so never report a missed one-year deadline as final where a load-bearing defect may be involved. Separately, s.16 of the Sale Law 1968 (imported by s.4(b)) lifts the notice bar entirely where the contractor knew of the facts and did not disclose them, so a missed deadline is a question for an advocate, never a closed door.

Sunken floor tiles are a trap. The statute puts שקיעת מרצפות on the ground floor, in parking, on pavements and on paths inside row 4 פיתוח חצר at three years, NOT inside row 2 ריצוף וחיפוי פנים at two. The script accepts `floor_ground` and `floor_outdoor` under the current schedule and redirects them.

There is also a THIRD clock the periods do not describe: limitation (התיישנות) governs how long the user has to SUE, and it runs separately. Whenever you report an end-date, say that it is the cover period and not a filing deadline, and that the time to sue is a question for an advocate.

Report the result as: which schedule applied and why, the period for that row, the stage the defect is in, who carries the burden there, and the notice position. If the contract date is unknown, say you assumed the current schedule and that a pre-2011 contract would shorten several periods.

### Step 4, draft the demand letter

The letter is not a formality. The law requires the buyer to give the contractor a proper opportunity to repair, and a buyer who repairs first and asks for the money afterwards usually loses. Send it before escalating anywhere. It is not, however, a formal precondition for a Registrar complaint, so never tell a user they must restart with a letter before they may file.

Build it from the template in `references/walkthrough-and-letter.md`. It must contain the apartment and contract identifiers, the handover date, an itemised defect table with dates, an explicit demand to repair, a reasonable deadline for a response, a statement that the buyer is giving the opportunity to repair as the law requires, and delivery by a traceable method. Keep the tone factual. Do not assert a legal conclusion the user cannot back, and do not quantify damages. Do not put the skill's own statutory-row analysis into the letter either. The timing analysis is for the buyer's understanding; the letter states the dates and the buyer's own assertion of liability.

### Step 5, escalate

If the contractor does not respond or does not fix, lay out the routes and their real limits:

| Route | What it gives | What it will not do |
|---|---|---|
| Complaint to the Registrar of Contractors | Free. Disciplinary pressure on a registered contractor. Open to any citizen against a registered contractor | Will not award money, will not arbitrate, will not resolve the dispute, will not touch a matter already in court |
| Self-repair at the contractor's expense | Available only on two narrow statutory gateways | Not a general option. Using it wrongly forfeits the claim |
| Civil claim | Money and enforceable orders | Needs an advocate, and in practice an engineer's opinion |

Self-repair is open only where the defect came back after the contractor repaired it at least once within two years of the notice, or the repair is urgent and the contractor did not act within a reasonable time. Say so precisely, because a user who self-repairs outside those gateways loses.

Common property is a separate track. Roof sealing, exterior cladding and yard development usually sit in the common property, and the Ministry recommends that a common-property complaint be filed through a member of the elected house committee. Recommended, not required: an individual owner is not barred. Route through the committee where one exists, and never tell a user with no functioning committee that they have no route.

### What actually happens after the letter

Most users' real question starts here, and the answer is not "get a lawyer".

- **The repair visit is the thing being counted.** The contractor usually responds by sending someone. Tell the user to be present, photograph before and after, write down the date and who attended, and not to sign anything describing the repair as accepted or the matter as closed. The s.4b(b) self-repair gateway turns on whether the defect RECURRED after a repair within two years of the notice, and nobody can prove a recurrence they did not record.
- **Re-inspect after a few weeks**, especially for damp, sealing and piping, where a failed repair reappears slowly. A recurrence is a new dated entry in the same log, not a new complaint.
- **The engineer's opinion** must come from a licensed מהנדס. It becomes worth its cost once the burden has shifted to the buyer in the warranty period, and it is what a court and a contractor actually respond to.
- **Small claims (תביעות קטנות)** takes low-value defect claims without an advocate. It is the realistic route for a handful of snags the contractor ignored, and the skill should name it rather than routing everything to a civil claim.
- **Distress (עוגמת נפש)** is a recognised head of damage in construction-defect claims, awarded separately from repair cost. Say it exists; never estimate it.

Where a claim is contested or quantified, it needs an advocate, and in practice a court-appointed expert (מומחה מטעם בית המשפט) will decide the technical dispute.

## Examples

### A leak at four years, current schedule

User bought in 2020, took possession March 2021, finds a pipe leak in January 2026 and assumes it is far too late.

Run Step 1, then the script. Pipes under the current schedule carry four years, so the bedek period closed in March 2025 and the warranty runs to March 2028. The defect is inside the warranty period, so it is live, but the burden has moved to the buyer, who now has to show the leak originates in planning, workmanship or materials. Because internal piping was not visible at handover, the one-year notice rule does not bar it, and notice is due within a reasonable time of discovery, which means now. Advise: send the demand letter this week, and because the burden has shifted, this is the point at which a licensed engineer's opinion becomes worth paying for.

### The same leak in an older apartment

Same facts, but the sale contract was signed in January 2009. The pre-2011 schedule applies, where piping is two years, not four. Bedek closed in 2011 and the warranty in 2014. Both windows are shut. Do not stop there: tell the user that a genuinely hidden defect and the separate load-bearing regime can still be open, and that both are questions for an advocate and an engineer. Never present the closed window as the end of the matter.

### Handover next week

User is collecting keys and is anxious about signing. Build the room-by-room list, explain that liability cannot be waived and that a waiver demanded as the price of the keys is void, and then give the practical instruction that actually protects them: attach the written list, get it referenced on the protocol, photograph everything, and refuse only the blanket "no comments" wording. Set the one-year notice deadline for everything visible on the day and tell them the date.

### Cracks above a doorway

User reports a widening diagonal crack running through the ceiling above a door. Step 0 fires. Stop, tell the user this is not something to log as a snag, and route to a licensed engineer. Do not say whether it is structural, do not say whether the 20-year regime applies, and do not draft a letter about it yet.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Sale (Apartments) Law 1973, consolidated | https://www.nevo.co.il/law_html/law00/72490.htm | The Schedule's ten items, s.4 burdens, s.4a notice, s.4b repair, s.7A waiver. Check the "current to" banner for a newer amendment |
| Kol Zchut, contractor liability for defects | https://www.kolzchut.org.il/he/אחריות_קבלן_לליקויים_בדירה_חדשה | The 06.04.2011 split, the pre-2011 table, the waiver FAQ |
| Registrar of Contractors, official service page | https://www.gov.il/he/service/complaint-about-constractor | Who may file, the attachment list, the disciplinary scope limits. This is the authority on the process, above any secondary summary |
| Kol Zchut, complaint to the Registrar of Contractors | https://www.kolzchut.org.il/he/הגשת_תלונה_לרשם_הקבלנים_במשרד_הבינוי_והשיכון | Practice guidance. Treats a prior written demand as expected; the Ministry does not require it |
| Registrar of Contractors complaint form | https://govforms.gov.il/mw/forms/complaint-about-contractor@moch.gov.il | That the form is still live at this address |

## Bundled Resources

| File | Use it for |
|---|---|
| `references/periods-and-burdens.md` | Both schedules in full, the burden rules, the notice rules, waiver and escalation detail |
| `references/walkthrough-and-letter.md` | The room-by-room checklist, the defect log format, the Hebrew demand-letter template |
| `references/domain-checklist.md` | The coverage contract this skill is maintained against, including figures known to be wrong in secondary sources |
| `scripts/defect_window.py` | Deterministic window and burden calculation. `--list` for both schedules, `--example` for worked cases |

## Gotchas

These are failure modes for the agent, not user errors.

- **Do not use the blog figures.** Widely repeated summaries give plumbing as 2 years, roof sealing as 3, and "structure" as 7. Under the current schedule piping is 4 and sealing is 4, the 3-year damp figure is the pre-2011 row, and the 7-year row is exterior cladding, not structure. Load-bearing structure is the separate 20-year regime. Check `references/periods-and-burdens.md`, not memory.
- **Sunken floor tiles are row 4, not row 2.** שקיעת מרצפות on the ground floor, in parking, on pavements and on paths is expressly inside פיתוח חצר at three years. Putting it in ריצוף וחיפוי פנים at two costs the buyer a year at both stages. `floor_ground` and `floor_outdoor` are pre-2011 row names, but the defects they describe are covered under the current schedule too.
- **Do not go hunting for a recent reform.** The last substantive change to the defect regime is Amendment 5 of 2011; Amendment 9 of 2022 touched late delivery and waiver. Later amendments listed against this law are indirect ones that changed a named Knesset committee and nothing about defects.
- **There are two schedules, not one.** Defaulting to the current table for an apartment bought before 6 April 2011 overstates the buyer's rights, sometimes by years. Ask for the contract date.
- **The warranty runs from the end of the bedek period, not from handover.** Total cover per row is its bedek period plus three years, so piping under the current schedule is protected for seven years in total. Treating the warranty as three years from handover understates protection badly.
- **The notice deadline and the defect period are different clocks.** A defect can be comfortably inside its bedek period and still be dead because visible damage was not notified within a year of handover. Always answer both.
- **Do not tell the user that signing the protocol waived their rights.** It did not, liability cannot be contracted away except in the buyer's favour. Explain the evidentiary problem instead, which is the real and much narrower risk.
- **Never classify a defect as load-bearing or fundamental, in either direction.** Saying "this is not structural" is as dangerous as the opposite, and it is an engineer's call.
- **Do not draft a letter that skips the opportunity to repair.** A demand that jumps straight to compensation or announces self-repair damages the user's position, because the law requires giving the contractor a proper chance to fix it first.

## Troubleshooting

| Symptom | Cause | What to do |
|---|---|---|
| Script exits saying the defect type is not a row in that schedule | The two schedules have different row NAMES. `stairwell` exists only in the pre-2011 table, `thermal` only in the current one | Run `--list` and pick from the schedule that applies. `floor_ground`, `floor_outdoor` and `damp` are accepted under the current schedule and redirected to the right row. If nothing fits use `other`, which is one year. Never conclude from a rejected key that the defect is uncovered |
| User cannot produce the sale contract date | Common with inherited or resold apartments | Say you are assuming the current schedule, give the answer, and state plainly that a pre-2011 contract would shorten several periods. Suggest the contract can be obtained from the conveyancing advocate or the land registry file |
| Contractor says the warranty "expired after 3 years" | Contractor is treating the warranty as running from handover | The warranty starts when that row's bedek period ends. Give the arithmetic for the specific row in writing |
| Contractor refuses to record reservations on the protocol | Routine pressure tactic at handover | Handwrite on the protocol that the signature confirms receipt of possession only, photograph it before returning it, and send the defect list separately the same day by a traceable method |
| Registrar complaint rejected | Most likely a scope limit: it is a money dispute, it is already in court, or it asks the Registrar to arbitrate. Or the contractor is not in the register | Check the register, and re-read the complaint against the disciplinary framing. A missing demand letter is NOT a ground of rejection, so do not tell the user to restart with one |
| Defect is in the roof or the facade and the neighbours are affected | It is almost certainly common property | Prefer the house committee track, which the Ministry recommends. If no committee exists or it will not act, the owner may still file, so do not present this as a dead end |
| The contractor has vanished, is in liquidation, or the company was struck off | Common with single-project companies | Say plainly that this changes the problem. Still send the written notice and date it, still document, and route the user to an advocate now, because who can be pursued (a parent company, directors, insurers, or a guarantee) is a legal question this skill cannot answer. Note that the sale-law guarantees protect the money paid, not defect repairs |
