---
name: israeli-renovation-scope-builder-skills-il
title: Israeli Renovation Scope Builder
description: Not legal advice. Builds a written scope of work and engagement terms for an Israeli home renovation, for a homeowner commissioning a shiputz or a tradesperson issuing terms. Produces an itemised scope with exclusions, milestone payments with retention, per trade warranty periods, agreed delay compensation, lawful working hours, and a handover checklist. Use when a user asks what to put in writing before a renovation, how to split payments to a kablan or shiputznik, what warranty to demand, or whether the job needs a permit. It matters because a renovation is a chozeh kablanut, which carries no warranty schedule of its own, so whatever the contract omits falls to weak defaults. Do NOT use for defects in a new apartment from a developer (that is israeli-home-defect-report), for building on your own land, for freelance or employment contracts, to price a quote, to sue a contractor, or to complain about a neighbour's renovation noise.
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-renovation-scope-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: construction
language: en
sources:
- title: Domain Checklist
  path: references/domain-checklist.md
- title: Permits And Trades
  path: references/permits-and-trades.md
- title: Scope And Terms
  path: references/scope-and-terms.md
---

# Israeli Renovation Scope Builder

## Legal notice

This is a free information tool operated by an AI model. It explains the law and helps you write your own engagement document. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate or an engineer. The output is not legal advice and not a legal opinion. It is a general explanation and a template only: it does not read the file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person, and before signing a document, before starting work that may need a permit, or before taking any step in a dispute, you should consult a licensed advocate. Assessing whether an element is load bearing, and whether a structure is safe, is a licensed engineer's call. All use of the output is the user's sole responsibility.

## Problem

Most Israeli renovations start on a WhatsApp thread and a number. Nobody writes down which brand of tile, who buys the fixtures, what happens on the third week of delay, or what "finished" means. Then the disagreement arrives and both sides discover the same thing: a renovation is a `חוזה קבלנות`, a statute that applies only where the contract is silent and that carries no warranty schedule at all. The periods everyone quotes, two years for carpentry, four for piping, seven for cladding, come from a different law that governs new apartments bought from a developer and has nothing to do with a renovation. So the parties argue from rights neither of them has, and the side that wrote nothing down loses the parts that were never written. This skill turns the job into an itemised scope, a payment schedule tied to completed work rather than to dates, and terms that say who buys what and what happens when it slips.

## Problem boundary

This skill writes the engagement document for work on an existing property, from either side. It does not price work and does not judge whether a quote is reasonable, because inventing a number here would be worse than useless. It does not assess whether an element is load bearing or whether a structure is safe, which is a licensed engineer's call. For defects in a new apartment bought from a contractor, use `israeli-home-defect-report`, which applies the statutory `חוק המכר (דירות)` schedule that does not apply here. For building a house on your own land, use `israeli-private-home-construction`. For non-construction freelance engagements, use `israeli-freelancer-service-agreement`. Once the user wants to sue, hand off to `israeli-small-claims-court` inside the jurisdiction limit, or to a licensed advocate.

## Instructions

You help the user produce two documents: a scope of work and a set of terms. Read `references/scope-and-terms.md` before drafting either. Read `references/permits-and-trades.md` before answering any question about permits, licensing, or who may lawfully do the work.

### Step 0, establish which side the user is on

Ask, and do not assume. A homeowner commissioning work and a tradesperson issuing terms need the same document written from opposite defaults: retention protects the homeowner, the lien and the access clause protect the tradesperson. Say plainly which side you are drafting for, and flag the clauses the other side will most likely push back on. Never write a document that only protects the side that happens to be asking, and never present a one-sided draft as neutral.

If the user is the homeowner, also establish whether they are acting privately or as a business (a company, an עמותה, a landlord operating as an עוסק). This changes the payment regime, see Step 6.

### Step 1, establish the six facts the whole document hangs on

1. **Who exactly is the other party.** Full legal name, **ת.ז. or ח.פ.**, registered address, and phone. A WhatsApp quote from "יוסי שיפוצים" names no legal person, and every mechanism below (retention, warranty, delay compensation) is enforceable against nobody until this line is filled. If the counterparty is a **חברה בע"מ**, ask for a **ערבות אישית** from the owner: a retention against a shell company is a retention against nothing. Verify the contractor at the `פנקס הקבלנים` and check the registration is **current**, not merely that it exists.
2. **What exactly is being done**, room by room and trade by trade.
3. **Who buys the materials**, per item, and who carries a price rise between quote and purchase.
4. **What the total is**, and whether it is `כולל מע"מ` or `בתוספת מע"מ`. Never leave this implicit.
5. **When it starts and how long it should take**, in working days, and what the parties will treat as an excusable delay.
6. **Where the property is**, because working hours and waste rules come from the municipal by-law on top of the national floor, and because a בית משותף adds consent questions and its own `תקנון`.

**The WhatsApp thread is probably already a contract.** A חוזה קבלנות needs no writing to bind. Tell the user to export and preserve the thread now, and then either supersede it with an express integration clause or expressly incorporate it. Do not let him assume nothing exists yet.

### Step 2, the order of operations, and what stops being possible

The user asked what to close **before paying**. Give him a sequence, not just a document, and mark what becomes impossible once work starts.

Before any money moves: counterparty identified and registration checked; permit question answered (Step 3); scope agreed line by line; payment schedule and retention agreed; insurance certificates in hand; the `תקנון` of the building checked if it is a בית משותף; **the homeowner's own contents/building insurer notified** (most Israeli policies require notice of works and may exclude cover during them).

**Irreversible, and each one is lost the day after it passes:**

| Moment | What must happen | Why it cannot wait |
|---|---|---|
| Before the first hammer | Dated photographs of what is being kept, of the stairwell, and of adjoining apartments | A neighbour's crack claim cannot be answered later |
| Before closing walls and floors | Photograph the **first fix**, every pipe and cable run, with a tape measure in frame | At handover this is under the tiling and the drawing is whatever the contractor says |
| Before tiling a wet room | Witnessed **flood test (בדיקת הצפה)** on the exposed membrane, photographed and dated | After tiling this tests only whether the room leaks today, not whether the waterproofing was done |
| Before work starts | Meter readings for water and electricity | Nobody can reconstruct the baseline afterwards |

Tie the first-fix photographs and the flood test to **payment stages**, not to handover. That is what makes them actually happen.

### Step 3, the permit gate, run this before drafting anything

`סעיף 145(א)(2)` of the Planning and Building Law requires a permit for erecting a building, demolishing and re-erecting it, adding to it, **and any repair to it** (`וכל תיקון בו`). The only relief is the carve-out for a `שינוי פנימי בדירה`, plus the separate exemption regulations.

The statute defines `שינוי פנימי` by five negative conditions. The change must not:

1. concern the exterior of the building;
2. harm its facade, appearance, or **שלד**;
3. harm **רכוש משותף**, or piping or other equipment that also serves other dwellings;
4. harm others (`אינו פוגע בזולת`);
5. change the dwelling's **area**, or the **number of dwelling units**.

Fail any one and the job is outside the carve-out. In practice the three that bite are moving a shared plumbing riser, touching a load-bearing element, and splitting one unit into two. Tell the user which condition their job trips, and send them to the local `ועדה מקומית` rather than guessing the outcome.

Gas work is licensed under חוק הגז (בטיחות ורישוי): a person may not engage in prescribed gas work without a licence, and relocating a kitchen gas point is ordinary in a renovation. Include it in the scope as its own trade and ask to see the licence.

Several common additions are separately exempt on their own conditions (bars, a pergola, air conditioning). An exemption is conditional: `פרק א` attaches general preconditions to EVERY exempt work (stability and safety, conformity with the `תכנית` and the `הנחיות מרחביות`). Work in breach of them is unlicensed building, not exempt building, so never answer "exempt" without the rider. `references/permits-and-trades.md` carries the conditions, which require a 45 day notice, and where it is filed. Do not generalise the notice duty: it attaches to individual regulations, not to the scheme.

### Step 4, who may lawfully do the work

Two independent limbs decide whether the contractor must be a `קבלן רשום`:

- **Value.** Above the current threshold per `ענף עבודה`, or per `ענף משנה`, at a single site.
- **Nature.** Any work touching the **שלד** requires a registered contractor **regardless of value**.

Guides state only the first. State both, give the figure with its as-of date, and say that it re-indexes every 1 January, so the user should check the Registrar's current notice rather than trust an embedded number. For electrical work, check the licence grade covers the installation, and note that the electrician who did the work may not sign its inspection. Details and figures in `references/permits-and-trades.md`.

### Step 5, build the scope

The scope is the deliverable that prevents most disputes. Per trade, per room, capture: what is being done, the quantity or area, the specification (brand, model, finish, thickness, colour), who supplies it, and what is **excluded**. Exclusions matter as much as inclusions: an unlisted item is how `תוספות` inflate a price.

Write "supply and install" or "install only" against every line. Where a specification is not yet known, write a placeholder and a decision deadline: a blank becomes the contractor's choice.

### Step 6, the payment schedule

Tie every payment to **verified completion of a defined stage**, never to a calendar date. A date pays for time; a stage pays for work. Hold a retention that is released only after handover and after the first defects window closes.

The legal force behind retention is `סעיף 4`: if the contractor does not repair a defect within a reasonable time after being given the opportunity, the customer may repair it and recover reasonable costs, or deduct from the price the amount by which the defect reduced the value. Retention is what makes that right collectable rather than theoretical.

Two payment rules that depend on who pays:

- **Private homeowner paying.** `חוק מוסר תשלומים לספקים` does **not** apply. Its definition of `מזמין` lists public bodies and businesses, and a private individual is not among them. A tradesperson has no statutory payment date against a homeowner; only the contract creates one. Correct a user who believes otherwise, in either direction.
- **A business paying** (company, עמותה, landlord operating as an עוסק). The law applies: not later than 45 days from the end of the month in which the invoice was submitted, unless the parties expressly agree another date that is not exceptionally unfair.

**Two payment mechanics that defeat the whole schedule if missed:**

- **Cash.** Never state the Prohibition on Cash Use Law as a flat 6,000 ש׳ח cap. `סעיף 2` bites on the **transaction price**, not on the payment: where an `עוסק` is a party and the price exceeds **6,000 ש׳ח**, cash is prohibited for the transaction. What survives is not an allowance but the residue `סעיף 1` carves out of the definition of `תשלום במזומן`, the **LOWER** of ten percent of the price and the Schedule amount, so on an ordinary renovation the lawful residue is materially **less** than the Schedule figure. Compute it from the price. The duty binds the **payer as well as the payee**, so a homeowner taking the cash-without-VAT deal is exposed himself, loses the paper trail every later claim depends on, and has no invoice to hang a warranty claim on. Detail in `references/scope-and-terms.md`.
- **Post-dated cheques.** A stack of cheques for future stages destroys the schedule and the retention you just built: the money is committed whatever the contract says, and stopping a cheque puts the homeowner on the defensive in enforcement proceedings on the instrument. Pay each stage when it is verified; do not pre-fund the job.

**Who verifies a stage.** "Verified completion" is not self-executing. Name the verifier in the document (the homeowner, an independent `מפקח בנייה` or engineer, or both jointly) and say what happens when they disagree. Without a named verifier the clause collapses back into dates, which is what it existed to prevent. An independent supervisor is the normal answer on a job of any size, and a cost the user should be told about.

**Discussion thresholds, not legal limits.** A pre-work payment above roughly 15 percent stops being mobilisation and becomes an unsecured loan to the contractor; a retention below roughly 5 percent is too small to put a defect right. Neither is in any statute; both are starting points to argue from.

If you can run scripts, `scripts/payment_schedule.py` builds the table and checks the arithmetic. If you cannot, do the same checks inline: milestones plus retention must sum to exactly one hundred percent, no single milestone before work starts should exceed a modest mobilisation advance, and the retention must remain unpaid until after the acceptance date.

### Step 7, the terms

Assemble these clauses for the parties to adopt, and say for each one that it is a choice they are making rather than a rule the law supplies. The parties sign the document; the tool only puts the options in front of them:

- **Warranty, per trade.** There is no statutory warranty schedule for renovation work. Set separate periods for waterproofing, tiling, carpentry, electrical, plumbing, and paint, each with its own line on what counts as a defect against fair wear. Do not import the developer periods from `חוק המכר (דירות)`, they are a different law for a different transaction.
- **Defect notice and cure.** `סעיף 3` requires notice within a reasonable time after discovery and a proper opportunity to cure, with no fixed day count. Convert that into a concrete number of days for each, in writing. Warn the homeowner that hiring a replacement before offering the cure opportunity can forfeit the claim entirely, except where the defect is genuinely urgent.
- **Delay.** Agreed compensation (`פיצוי מוסכם`) with a daily rate, a cap, and a defined list of excusable delays. Without a liquidated figure the homeowner must prove actual loss.
- **Working hours.** Complying with the hours is not a complete defence: noise inside permitted hours can still be an actionable nuisance if it is unusual, prolonged, or materially harms quality of life. The national floor prohibits noisy repair, renovation, or building work in a residential building between 20:00 and 07:00 on weekdays, and from 17:00 on the eve of a rest day until 07:00 the day after. Machinery for excavation, building, or demolition in a residential area stops an hour earlier, at 19:00. Both bind whoever **permits** the work, so the homeowner is exposed too, not only the tradesperson. Municipal by-laws are often stricter and frequently add a midday break that the national regulations do not impose on renovation work. Send the user to their local `חוק עזר`.
- **Common property, and the two different majorities.** Read the building's `תקנון` first (the registered one, or the `תקנון המצוי` in the Schedule to חוק המקרקעין if none was registered). It is a third layer on top of the national noise floor and the municipal by-law, and it routinely restricts hours, stairwell and lift use, and works in common areas. Then note that two distinct rules are routinely conflated:
  - **Taking an existing piece of common property and attaching it to one apartment (`הצמדה`)** requires the consent of **ALL** owners (`סעיף 62(א)`). A majority is not enough. This is the rule for the corridor niche or the stairwell recess.
  - **Detaching and attaching common property in order to BUILD an extension to an apartment (`הרחבה`)** is the narrower `סעיף 71ב` route, needing owners of three quarters of the apartments holding two thirds of the common property, and 60 percent where the expansion is for a `ממ"ד`.
  Separately, stairwells, lifts, shelters, and installations serving all owners can **never** be attached to one apartment at all (`סעיף 55(ג)`), so annexing stairwell space is a hard stop rather than a consent question. Anything touching a `ממ"ד` needs `פיקוד העורף` clearance before it is designed, not after; do not assume an internal wall of a protected space may be moved.
- **Termination, and suspension.** The clause bank is useless without an exit. Set out what counts as a material breach, the notice and cure period before termination, and the accounting on termination (paid to date, less the reasonable cost to complete, plus who owns materials already paid for and on site). Unilaterally firing a contractor without a contractual right makes the HOMEOWNER the breaching party. Give the tradesperson the mirror image: a right to suspend work for non-payment after written notice, because suspending without a clause is itself a breach.
- **Indemnity, separately from insurance.** A policy has an excess, exclusions, and can lapse. Require the tradesperson to indemnify the homeowner for damage to neighbours and to the `רכוש משותף` on top of carrying cover. Insurance without indemnity leaves the homeowner personally liable to the neighbour with no recourse.
- **Insurance.** Require third-party cover naming the homeowner, **employers' liability** cover for the crew, and the certificates before the first day. Present these as contractual requirements, not legal duties: for a private renovation they are not. An uninsured injured worker is the homeowner's largest realistic exposure.
- **A standard form triggers `חוק החוזים האחידים`.** Terms drafted in advance for use with many clients are a `חוזה אחיד`, and three clauses in this very list are presumed `מקפח` under `סעיף 4`: a liability cap (`4(1)`), an unreasonable suspension or cancellation right (`4(2)`), and agreed compensation unreasonably favouring the supplier (`4(6א)`). Two are void outright: limiting access to the courts (`5(א)`) and excluding liability for bodily injury (`5(ב)`). Tell BOTH sides, it is a warning to one and a defence to the other. Terms negotiated for a single job are not a `חוזה אחיד`. Detail in `references/scope-and-terms.md`.
- **Security beyond a cash retention.** A `ערבות ביצוע` or `ערבות בדק` is the alternative where the tradesperson resists a retention on cash-flow grounds, or where a company counterparty makes withheld cash the only real security. Its term must outlast the longest warranty period agreed.
- **Name the `מבצע בניה`.** Where there is demolition, scaffolding, or work above two metres, say who is the `מבצע בניה`, who appoints the `מנהל עבודה`, and who notifies the regional labour inspector. See `references/permits-and-trades.md` section 5.
- **Subcontracting and change orders.** Bar or condition subcontracting and keep the head contractor liable. Require every extra to be agreed and priced in writing before it is executed.

### Step 8, handover

Acceptance is a legal event, not a formality: `סעיף 6` obliges the customer to accept at the agreed time or within a reasonable time, and until then the contractor carries the risk. Acceptance starts the contractual warranty clock, so date it.

Require at handover: a marked or as-built routing of concealed plumbing and electrical lines, appliance warranties and manuals, surplus tile and paint with batch numbers, the dated evidence of the flood test that was witnessed BEFORE tiling (Step 2), not a test run now, the electrician's inspection certificate where the contract required one, confirmation that construction waste was removed, and a signed acceptance protocol listing outstanding items with dates.

The concealed-services drawing is the item most often skipped and the one that most reliably protects the next renovation.

### Step 9, when it goes wrong

Give notice in writing, offer the cure opportunity, keep a dated photographic record. A contractual claim runs for seven years, the clock starts on discovery where the facts were genuinely hidden, and a contractor who returns for a partial repair may restart it in the homeowner's favour.

**Route to the right forum. This is where a wrong answer costs the user his claim:**

| The dispute | Where it goes |
|---|---|
| Between apartment owners in a בית משותף about **rights or duties under the `תקנון`, or under the sections `סעיף 72(א)` actually lists** (58, 59, 59א-59ג, 59ה-59י) and the three statutes it names: use of common areas, the shares of expenses, works requiring the owners' consent | **המפקח על רישום המקרקעין** (`סעיף 72(א)`), who decides these |
| A neighbour's **damage** claim over the works, the cracked wall being the standard case | A claim in tort, not one about rights or duties under the `תקנון`, so `סעיף 72(א)` does not reach it: it goes to the competent **court**, and small claims is open to an individual within the ceiling. Never tell a neighbour his damage claim will be dismissed for want of jurisdiction |
| `הסגת גבול` by one owner against another apartment or the common property | The plaintiff **may choose**, `סעיף 72(ב)` says `לפי בחירתו`: a competent court or the supervisor. The supervisor is an option here, never a compulsory forum |
| Homeowner against the contractor, modest sum | `israeli-small-claims-court`, but only if the plaintiff is an **individual** and the sum is within the ceiling (the statute enacts 30,000 ש"ח, index-linked; the Justice Minister's annual notice sets it at 39,900 ש"ח from 1 January 2026). A full multi-trade renovation claim usually exceeds it |
| Anything above the ceiling, or brought by a business | A licensed advocate, in the competent court |
| The contractor is a `קבלן רשום` and the complaint is about his conduct or workmanship | A complaint to `רשם הקבלנים` is a **parallel** free track needing no advocate. Raise it alongside a money claim, never instead. Do not state what sanction follows |

Do not draft pleadings and do not assess the merits.

One correction to offer proactively, because renovation guides assert the opposite: there is **no** 14 day right to cancel a renovation engagement. The consumer cancellation regulations grant that right only for enumerated goods and services, and trade services are not among them; made-to-measure joinery is separately excluded. A cancellation right may still arise if the contractor signed the homeowner up at their door or remotely, but that is a different provision and should not be conflated.

## Examples

### A kitchen and electrical job in an apartment

Internal work, no shared riser moved, nothing structural. Passes the `שינוי פנימי` gate, so no permit. Scope splits into demolition, plumbing, electrical, carpentry, tiling, and paint, each with quantities, specifications, and exclusions. Payments at mobilisation, after first fix, after tiling, after carpentry installation, and a retention released after acceptance plus the agreed defect window. Warranty set per trade. Electrician's grade checked against the installation.

### Moving a bathroom

The user wants to relocate a bathroom, which moves waste piping into the shared riser. That trips condition three of the `שינוי פנימי` definition, so it is outside the carve-out and needs a permit, and it touches `רכוש משותף`, so it needs the owners' consent as well. Say both, and send them to the `ועדה מקומית` before any scope is drafted.

### A tradesperson issuing terms

An electrician wants terms before a large job. Draft from his side: mobilisation, stage payments on verified completion, materials price escalation, an access clause covering delays the homeowner causes, and the statutory lien noted explicitly. He has no statutory payment date against a private homeowner, so the contract is the only thing that gives him one.

### Late and disputed

The job is three weeks late and the parties disagree on what was agreed. Reconstruct the scope from the WhatsApp record, document what is complete against what is outstanding, and put the remaining stages and dates in writing. Then stop: the delay claim itself is a hand-off.

## Reference Links

| Source | URL | What to check |
|---|---|---|
| חוק חוזה קבלנות | https://he.wikisource.org/wiki/חוק_חוזה_קבלנות | Sections 3 to 8: defect notice and cure, remedies, lien, acceptance, dispositive application |
| חוק התכנון והבניה | https://he.wikisource.org/wiki/חוק_התכנון_והבניה | Section 145(a)(2) and the definition of שינוי פנימי |
| תקנות הפטור מהיתר | https://he.wikisource.org/wiki/תקנות_התכנון_והבנייה_%28עבודות_ומבנים_הפטורים_מהיתר%29 | Exemption categories, their conditions, and which carry a 45 day notice |
| תקנות למניעת מפגעים (מניעת רעש) | https://he.wikisource.org/wiki/תקנות_למניעת_מפגעים_%28מניעת_רעש%29 | Regulation 4 (renovation hours) and regulation 5 (machinery, one hour earlier) |
| תקנות רישום קבלנים (היקף כספי) | https://www.nevo.co.il/law_html/law00/74262.htm | Current threshold amounts, the שלד limb, and the 1 January indexation |
| תקנות החשמל (רשיונות) | https://he.wikisource.org/wiki/תקנות_החשמל_%28רשיונות%29 | Regulation 13 (what a מוסמך may do) and regulation 23 (the self-inspection bar) |
| חוק המקרקעין | https://he.wikisource.org/wiki/חוק_המקרקעין | Sections 55 and 71b: common property and expansion consent |

## Bundled Resources

| File | Use it for |
|---|---|
| `references/scope-and-terms.md` | The scope template, the clause bank, and the handover checklist |
| `references/permits-and-trades.md` | The permit gate, exemption conditions, contractor registration, electrician grades |
| `references/domain-checklist.md` | Coverage contract for this skill, plus known bad figures circulating in guides |
| `scripts/payment_schedule.py` | Builds and sanity-checks a milestone schedule. Optional, see Step 5 |

## Gotchas

- **The developer warranty periods are the wrong law.** An agent asked about renovation defects will reach for the `חוק המכר (דירות)` schedule because it dominates Hebrew search results. It governs a new apartment bought from a developer. A renovation has no statutory warranty schedule; the periods are contractual. Say so explicitly rather than quietly omitting numbers, because the user has usually already read the wrong ones.
- **"Internal work needs no permit" is a trap.** The statute requires a permit for `וכל תיקון בו`, any repair. The carve-out is narrow and fails on any of five conditions. Moving a shared riser or touching the שלד is outside it, and those are ordinary renovation requests.
- **Two different noise cut-offs.** Renovation work stops at 20:00, machinery at 19:00. Every summary that reports a single figure has flattened two regulations. The prohibition also binds whoever permits the work, so the homeowner is exposed, which is not what either party expects.
- **The registered-contractor rule is not only about money.** Anything touching the שלד needs a registered contractor at any value. An agent that checks only the shekel threshold will clear a cheap structural job that is not lawful.
- **Do not invent prices, periods, or a "standard" payment split.** There is no statutory or standard split. Offer a structure and make the user choose the numbers. Inventing a market rate for a renovation is the highest-risk fabrication in this domain.
- **Two different majorities for common property.** Taking an existing piece of `רכוש משותף` and attaching it to one apartment needs EVERY owner (`סעיף 62(א)`). The three-quarters-and-two-thirds rule is `סעיף 71ב` and applies only to detaching common property in order to BUILD an extension. An agent that quotes the majority for a corridor niche is inviting a proprietary trespass.
- **Do not over-read the `מפקח`'s jurisdiction.** `סעיף 72(א)` covers disputes about rights or duties under the `תקנון` or the sections it enumerates, and nothing else. A neighbour's tort claim for damage from the works goes to court, where small claims may well be open. `סעיף 72(ב)` is a choice (`לפי בחירתו`), not a compulsory forum. Routing a modest damage claim to the supervisor as though small claims were barred costs the user his cheapest forum.
- **Do not tell a tradesperson he is owed שוטף plus 45 by a homeowner.** The payment law does not reach a private individual. It does reach a company or a landlord operating as a business.

## Troubleshooting

| Symptom | Cause | What to do |
|---|---|---|
| User quotes a warranty period you cannot find in the contract | They are quoting `חוק המכר (דירות)`, which governs new apartments from a developer | Explain the two regimes, then ask what their own contract says. If it says nothing, that is the finding |
| User insists a 14 day cancellation right applies | Widely asserted in renovation guides, and wrong for this engagement | The cancellation regulations list enumerated items only, and trade services are not among them. Check separately whether the deal was signed at the door or remotely, which is a different provision |
| The contractor's registration number checks out but the job still looks unlawful | Registration is per `ענף`, and the שלד limb is value-independent | Check the branch matches the work, and whether anything touches the structure |
| The permit answer depends on whether a wall is load bearing | This is an engineering question, not a legal one | Do not answer it. Route to a licensed engineer, then return to the permit gate with their answer |
| Working hours in the contract conflict with what the municipality allows | The national regulations are a floor; by-laws are frequently stricter | Draft to the stricter of the two and cite the local `חוק עזר` |
| User asks what the renovation should cost | Out of scope, and unanswerable without inventing a number | Say the skill does not price work, and offer to structure the scope so competing quotes become comparable |
