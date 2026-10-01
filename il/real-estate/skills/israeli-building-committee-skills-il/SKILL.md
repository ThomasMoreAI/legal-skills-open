---
name: israeli-building-committee-skills-il
title: Israeli Building Committee (Vaad Bayit)
description: 'Not legal advice. Helps residents of an Israeli bayit meshutaf run or deal with the vaad bayit (ועד בית): splits building costs by floor area, or by the registered takanon, drafts WhatsApp notices, meeting invitations, minutes, repair quote tables and budget summaries, writes escalating reminders for unpaid דמי ועד, and builds fact sheets for neighbour disputes like נזילה מהשכן or a roof takeover. Use when a resident asks how much each apartment pays, whether the ground floor pays for the elevator, how to collect unpaid fees, who fixes a leak, or what to do with no committee. Prevents the usual wrong answers (equal split, invented exemptions) that start fights and sink claims. Do NOT use for lease disputes with a landlord (israeli-rental-agreements), TAMA 38 or pinui binui (israeli-urban-renewal-owner-guide), new-apartment contractor defects (israeli-home-defect-report), or filing a small claim (israeli-small-claims-court).'
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-building-committee
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: real-estate
language: en
sources:
- title: Fee Split Rules
  path: references/fee-split-rules.md
- title: Letter Templates He
  path: references/letter-templates-he.md
---

# Israeli Building Committee (Vaad Bayit)

## Legal notice

This is a free information tool operated by an AI model. It explains the rules that govern a shared building and helps residents organise their own notices, letters, and documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read your building's registered bylaws (takanon) or decisions book, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. The tool does not draft a statement of claim (ktav tvi'a) for the Mafkach or any court. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.

## Problem

Most Israeli apartment buildings are run by volunteer neighbours who have never read the Land Law. Fees get split equally when the law splits them by floor area, the ground floor is told it is "exempt" from the elevator when the statute says otherwise, and unpaid fees pile up because nobody knows the route is the Mafkach, not the police or small claims. Leaks and roof takeovers turn into years-long feuds for lack of a clear record and a clear first letter.

## Instructions

### Step 1: Find out which rules govern this building

Ask the user, in plain words:

1. Is the building registered as a bayit meshutaf (two or more apartments registered in the condominium register, Land Law s.52)? If not sure, say so and continue: an unregistered building with at least two apartments is still covered by Chapter 6A (ss.77A-77C), which applies the cost-sharing and dispute rules and runs it by the standard bylaws.
2. Is there a registered takanon (bylaws)? A registered takanon binds later owners too (s.62(c)), including one a single owner registered before any apartment was sold, which is the ordinary case in a new building (s.63). So the building may lawfully split costs on a basis no current owner ever agreed to. Where none was registered, or it is silent on a point, the **standard takanon (takanon mutzai)** in the Law's schedule applies (s.64).
3. Is there an active vaad (representation)? Every bayit meshutaf must have one (s.65).
4. Is the user an owner or a tenant? This changes who pays what and who votes (Step 7).

If a registered takanon exists, its text wins on cost split and procedure, subject to s.62(a). Ask the user to paste the relevant clause rather than guessing.

If the user does not know whether one is registered, do not guess and do not fall through to the default. Tell them how to find out: order a nesach rishum of the bayit meshutaf and ask to inspect the building file (עיון בתיק הבית המשותף) at the Land Registry office (לשכת רישום המקרקעין) for the area, through gov.il land-registry services. That file holds the registered takanon, the registration order, each apartment's floor area and the attachments, which is everything Step 2 needs.

### Step 2: Split costs (the core calculation)

**Default rule (s.58(a)):** each owner pays for proper maintenance and management of the common property, and for services required by law or customary, **by the ratio of the apartment's floor area to the floor area of all apartments**, unless the registered takanon sets a different rate.

| Question | Answer | Source |
|---|---|---|
| What counts in the floor area? | The apartment's floor area. Balconies and external walls are NOT counted unless the takanon says otherwise | s.57(b) |
| Attached roof, yard or storage? | Counted at the rate set in the takanon; if none, at a rate the Mafkach sets | s.57(c) |
| Equal amount per apartment? | Lawful where a registered takanon sets that rate (s.58(a)), including one the developer registered before any sale, which binds later buyers (s.63, s.62(c)). Without such a takanon an assembly resolution does not bind an owner who did not consent, and a two thirds majority alone is not enough. See references/fee-split-rules.md for the contested amendment case | s.58(a), s.62(a), standard takanon s.12(b) |
| Owner who "does not use" a service? | s.58(a) has no non-use exemption. Only a registered takanon or that owner's own agreement changes the share | s.58(a) |
| Nobody lives in the apartment? | Still pays | Kol Zchut |
| Wing with a separate entrance? | If the takanon separates that wing's maintenance, only its owners pay for it | s.59 |

**Calculate inline (no script needed):**

```
share(apt)   = area(apt) / sum(area of all apartments)
payment(apt) = share(apt) x total cost
```

Worked check from Kol Zchut: an 80 sqm apartment in a building whose apartments total 800 sqm pays 80/800, one tenth (10%). Always show the table (apartment, area, share, payment) so neighbours can check it, and round only the final payment.

**Maintenance vs improvement.** "Proper maintenance" means keeping the common property as it was when construction was completed, including improvements later made with the owners' consent (s.58(a)). A payment of a kind or rate that the law does not set binds an owner only with his consent (s.62(a); standard takanon s.12(b)). Replacing a worn roof membrane is maintenance; adding something the building never had usually is not. When the line is unclear, say so and point to the Mafkach (Step 5) rather than deciding it.

**Waterproofing upgrades.** A better membrane than the original spec is a common fight. Tie-breaker: the part that restores the roof to its as-built function is proper maintenance (s.58(a)); the added cost of a spec beyond that is a new expense that binds a non-consenting owner only with his consent (s.62(a)). Get quotes that price both, and record the owners' consent to the upgrade.

**Before splitting a roof quote, ask: is the roof attached (הוצמד) to a top-floor apartment?** Check the tabu extract (nesach) and the bylaws. Once part of the common property is attached, the common-property provisions no longer apply to it and it is treated like the apartment it is attached to (s.55(c)); it also counts in that apartment's area at the bylaws' or Mafkach's rate (s.57(c)). Who pays to waterproof an attached roof, and whether the structural slab under it is still shared, is **not settled by a statute text this skill can quote**: it depends on the bylaws and is a common dispute. Say so, ask for the bylaws clause, and route an unresolved disagreement to the Mafkach (s.72(a)).

Full rules and a longer worked example: `references/fee-split-rules.md`.

### Step 3: Decision thresholds

| Decision | Who decides | Source |
|---|---|---|
| Ordinary management, annual budget, fees within s.58 | Majority at the general assembly | Standard takanon s.12(a) |
| Make or amend the takanon | Owners holding two thirds of the common property | s.62(a) |
| Charge a payment of a kind or rate not set in law | The consent of each owner charged | s.62(a), standard takanon s.12(b) |
| Attach part of the common property (roof, yard, parking) to one apartment | All owners | s.62(a). Never stairwells, elevator, shelters (s.55(c)) |
| Install an elevator where there is none | Owners of two thirds of the apartments, if a permit can be obtained and there is no material harm. Record who voted for it: only they pay installation | s.59F(a), (b)(1) |
| Hire a management company (mitchazek) in principle | Takanon, or owners holding two thirds of the common property | s.71(b)(1) |
| Pick or replace a specific management company | Owners holding more than half of the common property | s.71(b)(2) |
| Extension using common property | Three quarters of the apartments plus two thirds of the common property; protected space (mamad) by owners of 60% of the apartments | s.71B(a) |
| TAMA 38 / pinui binui | Out of scope, route to `israeli-urban-renewal-owner-guide` | |

**Elevator installation cost (s.59F(b)):** first list which owners **decided** on (voted for) the installation. Only they bear installation cost, and they may agree that only some of them pay (s.59F(b)(1)); owners who did not decide do not bear it; ground-floor owners do not pay installation even if they voted for it (s.59F(b)(2)); **all owners, including the ground floor, pay maintenance and operation**; each payment is split by floor area among the owners who bear it. An agreed takanon may opt out of s.59F, and the Mafkach may cancel or condition a decision.

A decision made under the takanon and recorded in the decisions book binds every owner, including later buyers (s.71(a)).

### Step 4: Run meetings and draft documents

Under the standard takanon (check the building's own takanon first):

| Rule | Standard takanon |
|---|---|
| Annual general assembly, no later than fifteen months after the previous one | s.5 |
| Special assembly if owners of a third of the apartments demand it; they may self-convene if the vaad does not act within fourteen days | s.6 |
| Notice with time and place to all owners at least four days ahead; a notice posted prominently in the building counts as delivered one day after posting | s.7 |
| Quorum: owners of half the apartments, in person or by proxy; the notice may set a later hour the same day when any number is enough | s.8 |
| Notice lists the agenda; an owner may add an item with two days' notice to all; no off-agenda votes unless all owners agree | s.9 |
| Majority vote; one vote per apartment; ballot vote (הצבעה בקלפי) if a quarter of those present ask; chair breaks ties | s.12-13 |
| Committee of one to five members; a treasurer is elected only if it has more than one member | s.15 |
| Invoice for every expense, receipt for every payment, income and expense book, report every six months, bank account in the building's name, owners may inspect the books, fiscal year 1 January to 31 December | s.16 |

Templates in `references/letter-templates-he.md`:
- WhatsApp notice (short, one topic, date and amount, link to the full notice)
- Meeting invitation that satisfies s.7 and s.9 (date, hour, place, agenda, fallback hour for quorum, proxy line)
- Minutes (protocol): attendance per apartment, quorum, each agenda item, vote count, decision text for the decisions book
- Repair quote comparison table (elevator service, roof waterproofing, stairwell painting): scope, materials, warranty, payment schedule, insurance, licence, references, price, and each apartment's share
- Annual budget summary: opening balance, income by apartment, expenses with invoice numbers, closing balance, debts

Write notices in the neighbourly register Israelis use in building groups. Never publish a named list of debtors in the group: send debt reminders privately.

### Step 5: Unpaid fees

1. **Check the numbers first.** Recompute the owner's share (Step 2). A wrong split is the most common reason a debtor wins.
2. **Friendly private reminder**, then a **formal written demand** from the vaad with the monthly breakdown and a payment deadline (templates in `references/letter-templates-he.md`).
3. **The route is the Mafkach al Rishum HaMekarkein.** Disputes between owners about duties under the takanon or s.58 are decided by the Mafkach (s.72(a)); the vaad itself may bring the claim (s.73); the Mafkach has the powers of a magistrate court judge (s.74); and the decision is enforced like a magistrate court judgment, so it can be opened at Hotzaa LaPoal (s.76). Appeal goes to the District Court (s.77).
4. **Filing.** The claim is filed at the regional Mafkach office where the building is registered. The Justice Ministry runs an online system for drafting and filing vaad-fee claims. The fee equals a magistrate court civil claim fee and is updated, so **send the user to check the current fee at filing; never state an amount**. If the vaad sues, the protocol electing the vaad and the income book showing the debt are attached (Kol Zchut).
5. **What this skill prepares:** a fact sheet (apartment, owner, months, amount per month, share basis, decisions relied on, reminders sent with dates) and a document checklist. **It does not draft the statement of claim**; the official online system or an advocate does that.
6. If the apartment is rented, the vaad's claim is against the owner; the owner recovers from the tenant under the lease (Step 7).

### Step 6: Neighbour disputes

**Leak from upstairs or from the roof**

| Source of the leak | Who must repair | Basis |
|---|---|---|
| Roof, external wall, shared pipe or installation serving all or most apartments (even if the pipe runs inside an apartment) | The vaad, from building funds | s.52 definition; standard takanon s.3(a); Kol Zchut |
| Private pipe or fixture inside the neighbour's apartment | That apartment's owner | Standard takanon s.3(b) |

- The upstairs owner must let necessary works for the common property be done inside his apartment; if those works damage it, all owners share restoring it (standard takanon s.4).
- **Route:** to force a repair, apply to the Mafkach; if the resident already paid for the repair and wants the money back, that is a court claim, and a refund may be partial (Kol Zchut).
- **Documentation checklist:** dated photos and video of the stain and its spread, moisture readings or a plumber's written finding on the source, the date first noticed, every message to the neighbour or vaad, invoices, and whether any building or contents insurance exists (the policy terms decide coverage; ask the user to check).
- Produce a short, factual Hebrew letter to the neighbour or vaad asking for inspection access and repair by a date.

**Urgent leak, neighbour not responding.** Options, explained only, with a fact sheet (no pleadings):
- The duty exists: an owner must repair a fault in his apartment that may harm yours (standard takanon s.3(b)), and must allow necessary works for the common property inside his apartment (s.4(a)).
- Document the source: a written report from a leak-detection company can help show where the water comes from.
- Ask the Mafkach for an order to repair; the Mafkach can also give interim orders, which are enforceable like a magistrate court's (s.74, s.76). Whether an urgent interim order fits the facts is a question for the Mafkach or an advocate.
- Money for damage already caused is a court matter in tort: negligence (Civil Wrongs Ordinance s.35) or private nuisance, where damages require actual damage (s.44(a)).
- **Limitation:** a non-land claim expires after seven years (Statute of Limitations s.5(1)); if the facts were hidden from the claimant for reasons beyond his control, the period starts when he learned them (s.8). Tell the user not to sit on a claim; do not compute a deadline for him.

**Insurance.** Three different policies may be in play: a building-structure policy the vaad may hold, the resident's own apartment policy, and the upstairs neighbour's third-party liability cover. Ask which exist; the policy terms decide coverage. Notify your insurer immediately after learning of the damage (Insurance Contract Law s.22). An insurer that pays you takes over your claim against the responsible party to the extent it paid (s.62(a)), so do not settle with or waive against the neighbour without checking with your insurer (s.62(c)). If the neighbour has liability insurance, the neighbour's insurer may pay you directly, and must if you demand it, provided it gave the neighbour 30 days' written notice and the neighbour did not object in that time. Any defence it has against the neighbour applies against you too (s.68). No fixed filing deadline is stated here; check the policy.

**Takeover of common property (roof, stairwell, yard, parking)**
- The roof is common property; an owner may not keep others out unless it is attached to his apartment in the register (Kol Zchut). Attaching needs all owners (s.62(a)).
- Private items blocking the stairwell are not reasonable use (Kol Zchut).
- Trespass on the common property or another apartment may be brought, at the claimant's choice, to a court or to the Mafkach (s.72(b)).
- The takeover letter template stays factual ("as far as we know" it is not attached). Do not add any legal determination about attachment or rights; if the neighbour claims an attachment, check the tabu extract or consult an advocate.

**Noise:** unlawful noise can be reported to the police, and the noise rules also cover stairwells, yards, roofs and parking (Kol Zchut). Do not quote permitted hours from memory; send the user to the Kol Zchut noise page.

**Parking in a shared lot:** unless the takanon attaches spaces, the lot is common property. Ask for the takanon clause and any recorded decision; disputes go to the Mafkach (s.72(a)).

### Step 7: No committee, tenants, management companies

- **No active vaad:** serving is voluntary and nobody can be forced to (Kol Zchut). If no committee is set up or it does not function, the Mafkach may appoint one (s.67(a)), including an outsider with pay set by the Mafkach (s.66(a)), and that pay is shared as a s.58 expense (s.68). Where the bylaws have the vaad elected at a general assembly, the Mafkach appoints only after convening an assembly that failed to elect one, or if convening is impractical (s.67(b)); so first hold a properly noticed assembly.
- **Management company:** see the thresholds in Step 3; its fee is a s.58 expense (s.71(c)); a vaad is still needed to supervise it (Kol Zchut). Build a comparison table like the repair quotes.
- **Tenant vs owner:** under the Rental and Loan Law, the tenant bears current-maintenance payments to the vaad or management company (s.25I(a)(4)) but not payments to buy or upgrade fixed systems (s.25I(b)(1)). Some leases are excluded (s.25XV), and the lease itself decides the details. Toward the building, the owner remains the one who owes. A tenant votes only with the owner's proxy (Kol Zchut). A tenant can be a party to a Mafkach dispute (s.72(c)).

## Examples

### Example 1: "How much should each apartment pay for the roof?"
User: "We're a 6-apartment building, the roof waterproofing quote came in. Everyone says split it equally. Is that right?"
Actions: Ask whether a registered takanon sets a different rate. If not, apply s.58(a): ask for each apartment's floor area (without balconies, s.57(b)) and any attached roof or yard, compute each share inline, show the table, and note that an equal split holds only where a registered takanon sets that rate; without one it does not bind an owner who did not consent.
Result: A per-apartment table plus a WhatsApp message explaining the split and the source.

### Example 2: "Ground floor refuses to pay for the elevator"
User: "The ground-floor neighbour says he never uses the elevator, so he won't pay the monthly service contract."
Actions: Explain there is no non-use exemption in s.58(a); if the elevator was installed under s.59F, the statute says all owners pay maintenance and operation. The only exceptions are a registered takanon clause or his own agreement. Ask for the takanon clause.
Result: A calm Hebrew reply for the group and a private note to the neighbour.

### Example 3: "An owner hasn't paid for eight months"
Actions: Rebuild the debt month by month, draft a private reminder, then a formal demand; explain the Mafkach route (s.72(a), s.76), point to the Justice Ministry online system, and give the document checklist. Do not state a fee amount and do not draft the claim.
Result: Two letters, a debt fact sheet, and a filing checklist.

### Example 4: "Water is dripping from my ceiling"
Actions: Ask where the water seems to come from (upstairs bathroom, roof, a riser pipe). Apply the leak table, give the documentation checklist, draft a letter asking for access and repair, and explain Mafkach (to order a repair) vs court (to recover money already spent).
Result: A factual letter plus an evidence log template.

## Bundled Resources

### References
- `references/fee-split-rules.md`: the statutory cost-sharing rules, what counts in floor area, elevator installation vs maintenance, a full worked example, and the maintenance vs improvement test. Consult when computing shares or answering "do I have to pay for this?".
- `references/letter-templates-he.md`: Hebrew templates (sent in the writers' own names, no legal argument or threat of proceedings) for WhatsApp notices, meeting invitation, minutes, quote comparison, budget summary, fee reminders, and leak / common-property letters. Consult whenever drafting.

### Scripts
- `scripts/fee_split.py`: optional stdlib-only helper that computes shares from a JSON list of apartments, supports excluding apartments from a payment (e.g. owners who did not decide on an elevator installation; with `--kind installation` apartments marked `ground_floor` are dropped automatically) and attached-area weights. Run: `python3 scripts/fee_split.py --example`. The same math is shown inline in Step 2 for hosts that cannot run scripts.

## Gotchas

- **Equal split by default.** Agents divide costs equally per apartment. The statute splits by floor area (s.58(a)) unless a registered takanon sets another rate; absent one, an equal split does not bind an owner who did not consent (standard takanon s.12(b)).
- **Inventing a non-use exemption.** Agents say the ground floor does not pay for the elevator. The ground floor is exempt only from **installing** a new elevator under s.59F(b)(2); everyone pays maintenance and operation (s.59F(b)(3)), and s.58(a) contains no non-use exemption.
- **Tenants pay improvements.** Agents put all vaad payments on the tenant. The lease law puts current maintenance on the tenant and excludes buying or upgrading fixed systems (s.25I(b)(1)).
- **Inventing Mafkach fees and deadlines.** The fee tracks the magistrate court fee and changes; the appeal period is set in regulations. Route to the source instead of quoting a number.
- **Using aggregator percentages.** A Kol Zchut summary says adding an elevator needs 66% of owners; the statute says owners of two thirds of the apartments (s.59F(a)). Takanon amendments are measured by share of common property, not headcount (s.62(a)). Cite the statute.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Land Law 1969 (full text, Wikisource) | https://he.wikisource.org/wiki/חוק_המקרקעין | ss.52-77 and the standard takanon schedule |
| Rental and Loan Law 1971 (Wikisource) | https://he.wikisource.org/wiki/חוק_השכירות_והשאילה | s.25I tenant payments, s.25XV exclusions |
| Kol Zchut: vaad bayit payments | https://www.kolzchut.org.il/he/תשלומי_ועד_בית | Split examples, tenants, online claim system |
| Kol Zchut: claim to the Mafkach | https://www.kolzchut.org.il/he/הגשת_תביעה_למפקח_על_רישום_המקרקעין | Filing office, fee basis, documents to attach |
| Kol Zchut: repairs in a shared building | https://www.kolzchut.org.il/he/תיקונים_בבית_משותף | Leak responsibility and routes |
| Gov.il: claims to the condominium supervisor | https://www.gov.il/he/service/condominiums-supervisor-claims | Official filing service |

## Troubleshooting

### "The takanon says something different"
Cause: A registered takanon may set a different cost rate or procedure (s.58(a), s.64).
Solution: Ask the user to paste the clause and follow it, subject to s.62(a) (no new kinds of payments without consent). If the takanon was never registered, treat it as an agreement between the signers and flag the uncertainty.

### "We don't know the apartment areas"
Cause: Areas are not in the WhatsApp group.
Solution: Ask owners for their purchase documents or the building's registration documents at the land registry (tabu). Until then, present the split as provisional and do not send debt letters based on estimated areas.

### "The debtor says the vaad was never properly elected"
Cause: Vaad claims to the Mafkach attach the protocol electing the vaad (Kol Zchut).
Solution: Hold a properly noticed assembly (Step 4), elect the vaad, record fee decisions in the decisions book, and only then send the formal demand.

### "Is this an improvement or maintenance?"
Cause: The line depends on the building's state at completion and on prior consent (s.58(a)); this skill cannot decide it for a specific case.
Solution: Lay out both readings and the facts that matter, and point to the Mafkach or an advocate for a binding answer.
