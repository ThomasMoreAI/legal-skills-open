---
name: israeli-wills-inheritance-skills-il
title: Israeli Wills & Inheritance Navigator
description: 'Not legal advice. Draft an Israeli will in the form the Succession Law 1965 requires and navigate the inheritance process. Drafts a witnessed will (צוואה בעדים), which Israeli law does not require a lawyer for (one is still recommended): the testator writes the wishes, dates and signs, and two witnesses (who may not be beneficiaries or their spouses) sign. Explains the four will types, depositing the will with the Registrar, and obtaining a succession order (צו ירושה, when there is no will) or a probate order (צו קיום צוואה, when there is a will). Use when a user asks to "write a will", "deposit my will", "get a succession order", "my parent died without a will", "צוואה", "צו ירושה", or "צו קיום צוואה". Prevents common self-made-will mistakes. Do NOT use for binding enduring power of attorney (ייפוי כוח מתמשך needs a certified attorney, see israeli-elder-care-navigator), guardianship, contested-estate litigation between heirs (use a lawyer), or formal legal advice on complex
  estates.'
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-wills-inheritance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: trusts-and-estates
language: en
sources:
- title: Domain Checklist
  path: references/domain-checklist.md
- title: Orders And Process
  path: references/orders-and-process.md
- title: Will Templates
  path: references/will-templates.md
---

# Israeli Wills & Inheritance Navigator

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Problem

People who draft a will alone often void part of it without knowing, most often by letting a beneficiary (or a beneficiary's spouse) sign as a witness. After a death, families confuse the two inheritance orders, and assume that holding the order settles the estate. This skill prepares a correctly-structured draft of a witnessed will for advocate review, keeps the witnesses valid, routes the user to the right order, and flags the traps that follow it.

## Instructions

The skill does three jobs. Identify which the user needs.

### Job 1: Draft a will (focus on the witnessed will, צוואה בעדים)

Israel's Succession Law recognises four will forms. Pick the right one, then draft it.

| Will type | When it fits | Lawyer required by law? |
|-----------|--------------|----------------|
| צוואה בעדים (witnesses) | The default for most people. Typed or written, signed before 2 witnesses. | No (but recommended) |
| צוואה בכתב יד (handwritten) | Written entirely in the testator's own hand, dated, signed. No witnesses. | No (but recommended) |
| צוואה בפני רשות (before an authority) | Stated aloud to, OR handed in writing personally to, a judge, court registrar, Inheritance Registrar, or religious-court judge (Section 22). A notary counts as a judge. The authority reads it back, the testator declares it is their will, and the authority certifies that on the will's face. | An authority, e.g. a notary, takes it |
| צוואה בעל פה (oral / שכיב מרע) | Only for someone on their deathbed or in mortal danger. The two witnesses must record the words, the date and the circumstances in a memorandum (זכרון דברים), sign it, and deposit it with the Registrar as soon as practicable (Section 23). It lapses one month after the danger passes if the testator is still alive. | No, but very limited |

**The witnessed will is the skill's main deliverable.** The Succession Law does not require a lawyer for it, but using an inheritance lawyer to draft or review the will is recommended, especially to reduce the chance it is later challenged. It has FOUR formal elements (Section 20), and missing any one exposes the will to challenge. State all four:
1. **In writing** (typed is fine).
2. **Dated.**
3. The testator **declares before two witnesses** that this is their will and **signs** it.
4. The two witnesses **confirm in writing on the will itself, by their signature**, that the testator declared and signed. This witness-confirmation clause is not optional boilerplate; a will where the witnesses just sign a blank line without the confirmation language is defective.

**Defective is not the same as void (Section 25).** Draft all four elements every time, but never tell a user that a flawed will is dead. Section 25 lets the Inheritance Registrar or the court admit a will despite a missing or faulty element, by reasoned decision, if they have no doubt it reflects the testator's free and true intent. What cannot be cured is the מרכיב היסוד: for a witnessed will, that the will is in writing and the testator brought it before two witnesses; for a handwritten will, that the whole will is in the testator's own handwriting. A missing date, and a missing signature, are curable defects in both forms.

**Who can make it (Section 26):** the testator must be an adult (18+) and of sound mind. A will by a minor, by a person declared legally incompetent (פסול דין), or by someone who at the time did not understand what a will is, is VOID. The template's "sound mind" line is a declaration, not proof of capacity.

**The rules that void a bequest (state them every time):**
- A witness must be an adult and not legally incompetent (Section 24).
- A beneficiary, or a beneficiary's spouse, must NOT be a witness. More broadly (Section 35), a bequest in favour of anyone who **wrote the will, witnessed it, or otherwise took part in making it**, or in favour of that person's spouse, is VOID. Section 35 opens with an express carve-out for an oral will (פרט לצוואה בעל־פה), so it does not bite on a deathbed will under Section 23. This matters here: if a beneficiary dictates or prepares the will, the gift to them can be attacked. So have a neutral person handle the wording, and use two neutral adult witnesses who inherit nothing.

To draft, collect: the testator's full name + Teudat Zehut, the bequests (who gets what), any guardian wish for minor children, and whether to name an executor (מנהל עיזבון). Then produce a Hebrew draft of the will using the structure in `references/will-templates.md`: a clear-mind declaration, a clause revoking earlier wills, numbered bequests, an optional executor clause, date and place, the testator's signature line, and the two-witness confirmation clause (the Section 20 wording) with name/ID/signature lines.

**What the will does NOT control (state this every time you draft one):**
- **Pension, provident funds and life insurance are outside the estate (Section 147).** Money payable on death under an insurance contract, a pension fund (קופת קיצבה), or a provident fund (קופת גמל) is not part of the estate unless the contract says it goes to the estate. The will does not override the beneficiary designation (מוטבים) held by the fund or insurer. For most Israelis this is the largest asset they own. Tell the user to update the מוטבים separately with each institution; a will that contradicts them does not win.
- **You cannot contract about a future inheritance (Section 8).** An agreement about a living person's estate, and a waiver of a future inheritance, are both void. A gift meant to take effect only on death is void unless it is made as a will under this law. Section 27 adds that an undertaking to make, change, or revoke a will has no effect, and a will clause purporting to bar its own revocation is void.
- **Mutual wills between spouses (צוואה הדדית, Section 8א)** are a separate regime with their own revocation rules: while both live, revoking needs written notice to the other spouse and cancels BOTH wills; after one dies, the survivor can revoke only by disclaiming or returning what they took under the deceased's will. A clause completely barring revocation during both lives is void. Recommend a lawyer before drafting one.

Always tell the user, in this order. First: this is an automatic draft, no advocate has reviewed it, and one should before they sign. Beyond simple bequests (a business, foreign assets, a trust, minor children needing a guardian, or a likely dispute) that review is not optional. Only then: print it, sign by hand in front of both witnesses at one sitting (all signing the same copy, in each other's presence), and keep the original safe. Remind them to update the will after a major life change (marriage, divorce, a new child), because Israeli law does NOT automatically cancel a gift to an ex-spouse on divorce.

### Job 2: Deposit the will with the Inheritance Registrar

Depositing the will with the Inheritance Registrar (הרשם לענייני ירושה) is OPTIONAL, a will is fully valid without it. Deposit safeguards the original from loss or tampering and records that it existed. Walk the user to the gov.il will-deposit service / the Registrar's online portal (inheritance.justice.gov.il). The deposit can be made either by attending a Registrar office in person or remotely online, but only the testator can do it, and only the testator can take the will back. Make clear deposit is not a stamp of validity, the will still has to meet the form requirements above.

**What deposit actually buys, and it is not nothing (Section 21(b)).** A will that was deposited and stayed in deposit until the testator's death is **prima facie evidence** (ראיה לכאורה) that the person named in it as testator made it, and that it was made no later than the day of deposit. That is the real reason to deposit: it takes the two facts most often attacked after a death, "is this his signature" and "when was this written", and puts the burden on whoever wants to dispute them. Say this, rather than presenting deposit as mere safekeeping. Section 22(f) gives the same prima facie effect to a will made before an authority, as to both the maker and the date and place stated in it. Neither provision makes a defective will good, and neither forecloses a challenge, it shifts who has to prove what.

**The deposit fee, and when it is waived.** The fee schedule lists 126 NIS for depositing a will, but item 5א exempts the deposit entirely if the testator has not deposited an earlier will in the five years before. In practice a first deposit, or one made five or more years after the last, is free. Say this rather than quoting the 126 alone, because most users depositing a will are exempt.

Also tell the testator: they may take a deposited will back at any time, free, and withdrawing it does NOT revoke it. Only one will can be on deposit at a time. If no application about the will is filed, the Registrar opens a deposited will three months after the death and notifies the beneficiaries. Anyone holding a will must hand it over once they learn the testator has died.

### Job 3: Get the right inheritance order after a death

This is where users go to the wrong door. The rule is simple:

| Situation | Order to request | What it does |
|-----------|------------------|--------------|
| The deceased left NO will | Succession order (צו ירושה) | Declares the legal heirs (spouse, children, parents, per the Succession Law order) and their shares. |
| The deceased left a will covering the WHOLE estate | Probate / will-execution order (צו קיום צוואה) | Gives the will binding effect and distributes the estate as written in it. |
| The deceased willed only PART of the property | BOTH: a probate order on the willed part, a succession order on the remainder (Section 66(b)) | The willed part passes under the will, the rest passes to the legal heirs. |

**The choice is not binary, and this is the case agents get wrong.** A will that disposes of the apartment and says nothing about the bank account, the car, or a later-acquired asset is a partial will, and it is common. Under Section 66(b) the family needs both orders, with the heirs set out for the intestate remainder as in a no-will file. Ask whether the will covers everything, and treat "I am not sure" as the partial case until the will is read.

Both applications go to the **Inheritance Registrar** (הרשם לענייני ירושה), filed online at the Registrar's portal. The Registrar, not a court, issues most orders.

**Three doors, not two.** A file leaves the Registrar for the **Family Court** only on a Section 67א ground: an objection; the State or one of its institutions is a party; the Attorney General or their representative opens or joins a proceeding; the Public Trustee represents someone whose property it manages; or the Registrar transfers it. The AG and Public Trustee grounds routinely pull in files with minor or incapacitated heirs. A **religious court** may issue either order under Section 155 only if every party concerned consents in writing.

**Fees.** State the rule, not one number, because the amounts reindex every 1 January by CPI. The base fee for a succession-order or probate-order application is 597 NIS; filing online costs 85% of that, which is where the commonly-quoted 507 NIS comes from; publication is a separate 66 NIS. The full schedule and the exemptions (including the Regulation 4(5) exemption for bereaved relatives, which covers a succession-order application or one connected to it, not a probate-order application) are in `references/orders-and-process.md`. Once granted, the digital order is emailed to the applicant; the Registrar sends it on to a bank, insurer or government body (Tabu, Ministry of Transport, Israel Land Authority, Tax Authority) only after a בקשה לפעולה is filed for that body.

**The objection window:** the Registrar publishes notice of the application and sets a period for objections which by law cannot be shorter than two weeks; in practice this is 14 days. An objection (התנגדות) can be filed within that period as long as the order has not yet been issued. Tell heirs to expect this waiting period.

**Tax:** there is no estate or inheritance tax in Israel; the estate tax law was repealed for anyone who died after 31 March 1981, and receiving an inheritance is not itself a taxable event. The real exposure comes on SELLING an inherited asset (מס שבח or capital gains tax); route that to a tax professional.

**Who inherits when there is NO will (Section 11):** the surviving spouse takes the household chattels including the family car, and of the rest of the estate the spouse takes one-half when the deceased left children (or their descendants) or parents, two-thirds when the deceased left only siblings (or their descendants) or grandparents, and the whole estate if none of those relatives survive. The children share the remaining portion equally. If the deceased left no children, that remaining portion goes to the parents and their line, then to grandparents and their line (see `references/orders-and-process.md`). Give the actual fraction, not just "spouse and children".

**Representation, and the carve-out that reverses it (Section 14).** This is the most-asked intestacy question after the spouse's share, and it has a limb that is routinely stated backwards.
- **The rule (Section 14(a)).** A child of the deceased who died before them and left children of their own is replaced by those children, who inherit in their place; the same applies down the line to the children of any relative of the deceased who died before them. Under Section 14(b) those children split equally between them whatever they take by representation, so a predeceased child's one-third is divided among that child's own children, not shared out to the surviving siblings.
- **The carve-out (the closing limb of Section 14(a)).** Representation does NOT operate where the deceased left a surviving spouse together with parents or grandparents as described in Section 11(a). So where a widow or widower survives alongside the deceased's parents or grandparents, the children of a parent or grandparent who predeceased do NOT step up into that share. Never tell a user that a predeceased parent's line always steps up: in the parents' and grandparents' line it depends on whether a spouse survived. The statutory drafting here is terse, so where this configuration actually arises, say that it is the Registrar who applies it on the facts and that it is worth a lawyer.
- **An heir found unfit to inherit, as amended in 2024 (Section 14(c)-(d)).** Section 5 makes an heir unfit if they caused the deceased's death intentionally or with indifference, were convicted of attempting to, or were convicted of concealing, destroying or forging the deceased's last will or of claiming under a forged will; the court may limit or lift the unfitness where satisfied that was the deceased's wish. Where the unfit heir is the deceased's child or that child's descendant, their children DO inherit in their place, unless the court is satisfied it was the deceased's wish that they should not. Where the unfit heir is any other relative, their children do NOT inherit in their place, unless the court is satisfied it was the deceased's wish that they should. The default flips depending on which line the unfit heir sits in.

Two things that change the spouse's real take, and that agents routinely omit:
- **The apartment proviso, inside Section 11(a)(2).** In the two-thirds case, if the spouse had been married to the deceased for three years or more and was living with them at that time in an apartment that is wholly or partly part of the estate, the spouse takes the deceased's ENTIRE share in that apartment, plus two-thirds of what remains of the rest. For a childless couple facing the deceased's siblings this decides whether the widow or widower owns the home outright.
- **Marital property is settled before heirs take.** What a spouse is owed under חוק יחסי ממון or a property agreement is an estate DEBT ranked in Section 104(a)(4), paid out before any heir receives a share, and Section 11(c) separately deducts a כתובה from the spouse's share. Quoting "half" without this understates the spouse's position.

**An unmarried partner inherits too (Section 55).** Where a man and a woman lived a family life in a shared household without being married, and neither was married to anyone else at the time of death, the survivor is treated as if the deceased had left them by will whatever they would have inherited by law had they been married. A contrary provision in an actual will, express or implied, overrides this. Do not tell a ידוע/ה בציבור they have no claim.

**Two things a will cannot do, and one fear it does not justify:**
- **Maintenance from the estate (Section 56):** a spouse, children, or parents of the deceased who genuinely need support are entitled to maintenance from the estate, whether the estate passes by law or by will. A will cannot simply cut off a dependent who needs maintenance.
- **Debts:** heirs take what is left after the estate's debts. If the debts may exceed the assets, get advice before accepting; an heir can disclaim (הסתלקות) rather than take on a negative estate.

**If you recommend disclaiming, give the rules with it (Section 6).** Written notice to the Registrar, only after the death and before distribution; retroactive; only in favour of the deceased's spouse, child or sibling, never a person of the heir's choosing; a conditional disclaimer is void; a minor or a legally incompetent person needs court approval; and an heir who already transferred or charged the share has lost the right (Section 7(c)). The full rules, including the 2024 war-related widening in Section 6א, are in `references/orders-and-process.md`.

**After the order: the home, the debts, and minor heirs.** The order says who inherits; it does not settle the estate. State these four traps, then route estate administration to `israeli-estate-settlement-navigator`:
- **The family home.** First establish how the flat is owned. Only the deceased's share is in the estate: a spouse who is a registered co-owner keeps that share as their own and inherits on top of it. A property-relations claim is different: it is a money claim paid out of the estate as a debt (Section 104(a)(4)), not co-ownership of the flat. The deceased's share passes to the heirs, who become co-owners, and any co-owner may demand dissolution at any time (Land Law Section 37(a)); an indivisible flat is sold and the proceeds split (Section 40(a)). In a court-ordered division, an indivisible asset first goes to the heir who bids highest, at no less than market value, credited against their share (Succession Law Section 113), so a spouse can buy the others out. Occupation: anyone who lived with the deceased may stay three months, an heir six (Section 108(a)); and under the statutory division rules the spouse, children and parents who lived there may stay as paying TENANTS of the heirs who receive the flat (Section 115). Those rules yield to a will's own distribution directions (Section 111(c)) and do not apply at all when the heirs divide by agreement (Section 110(d)), so a user should get an advocate's advice BEFORE signing a division agreement or registering at the Tabu. Details: `references/orders-and-process.md`.
- **Dividing without inviting creditors.** If the heirs divide without inviting creditors and without paying the debts known at the time, each heir is liable for the unpaid debts up to the value of the WHOLE estate; an heir who proves they did not know of a particular debt answers for it only up to what they received (Section 128(a)), and the burden of proving values is on the heir (128(b)).
- **Minor heirs.** Parents may not, without advance approval, transfer, divide or charge a minor's flat, perform an act whose validity depends on registration, or make any legal act between the minor and the parents or the parents' relatives other than receiving gifts (Legal Capacity and Guardianship Law Section 20(a)(1), (2), (5)). A widowed parent dividing the estate with minor children is exactly that last case. Since the 2024 amendment the request goes first to the Public Trustee (האפוטרופוס הכללי), with the court as the fallback (Section 74א). A minor's disclaimer needs court approval (Section 6(c)).
- **Registration is a separate step.** Recording the heirs at the Tabu needs its own request after the order.

## Examples

### Example 1: Draft a simple will
User says: "Draft a will leaving my apartment to my two children equally."
Actions:
1. Collect the testator's name + Teudat Zehut and the children's names.
2. Produce a Hebrew draft of a witnessed will: clear-mind declaration, revocation of prior wills, a bequest splitting the apartment 50/50, date/place, signature line, and the two-witness clause.
3. Warn: the two witnesses must NOT be the children, their spouses, or anyone inheriting. Use two neutral adults. Sign by hand in front of both.
Result: An automatic Hebrew draft for the user to take to an advocate for review, plus the signing instructions that apply once it is reviewed. Never call it a finished or valid will.

### Example 2: Deposit a will
User says: "How do I make sure my will can't be lost or thrown out?"
Actions:
1. Explain deposit with the Inheritance Registrar is optional but protects the original.
2. Point to the gov.il will-deposit service / the Registrar portal; the testator deposits in person with ID.
3. Note deposit safeguards the document but does not by itself prove validity; the form requirements still apply.
Result: Clear steps to deposit, with the right expectation.

### Example 3: Death with no will
User says: "My father passed away and did not leave a will. How do I inherit?"
Actions:
1. Identify this as the no-will path, so the order is a succession order (צו ירושה), not a probate order.
2. Walk through the online application to the Inheritance Registrar, the 2026 fees, and who the legal heirs are.
3. Mention an objection would move the file to the Family Court.
Result: The correct order, where to file it, and what it costs.

## Bundled Resources

### Scripts
- `scripts/inheritance_helper.py` -- two deterministic checks: which order to request (`--has-will yes|no|partial`, where `partial` returns the Section 66(b) both-orders answer) and whether a proposed witness or preparer triggers Section 35, taking `--beneficiaries`, optional `--beneficiary-spouses`, `--witnesses`, and optional `--preparers` (anyone who wrote the will or took part in making it). It compares names only, so it cannot see a relationship it was not told about, and it cannot check age or capacity (Section 24). The witness check exits non-zero when a bequest would be void or a witness is duplicated, so a caller can branch on it. Run: `python3 scripts/inheritance_helper.py order --has-will no`

### References
- `references/will-templates.md`: fill-in Hebrew draft structures for the witnessed will and the handwritten will, plus the witness attestation clause, for advocate review before signing. Consult when drafting.
- `references/orders-and-process.md` -- the succession-order vs probate-order decision, the Registrar application steps, fees, and the legal-heir order. Consult when handling a death.
- `references/domain-checklist.md` -- coverage contract for this skill (used by maintenance).

## Recommended MCP Servers

| MCP | Use |
|-----|-----|
| `kolzchut` | Look up the All-Rights (כל-זכות) pages on wills, deposit, and the inheritance orders for current procedure and Hebrew terms. |

This helps confirm current procedure and terminology.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Kol-Zchut: witnessed will | https://www.kolzchut.org.il/he/צוואה_בעדים | No-lawyer rule, signing, witness disqualification |
| Kol-Zchut: will types | https://www.kolzchut.org.il/he/צוואה | The four will forms |
| Kol-Zchut: will deposit | https://www.kolzchut.org.il/he/הפקדת_צוואה_אצל_רשם_הירושה_במשרד_המשפטים | Optional; how it works |
| Kol-Zchut: succession order | https://www.kolzchut.org.il/he/הגשת_בקשה_מקוונת_לקבלת_צו_ירושה | No-will order, online filing, fees |
| Kol-Zchut: probate order | https://www.kolzchut.org.il/he/הגשת_בקשה_מקוונת_לקבלת_צו_קיום_צוואה | With-will order |
| Kol-Zchut: objection to an order | https://www.kolzchut.org.il/he/התנגדות_למתן_צו_ירושה | 14-day objection window |
| Succession Law 1965 (full text) | https://he.wikisource.org/wiki/חוק_הירושה | Sections 5, 6, 8, 8א, 11, 14, 19, 20, 21, 22, 23, 24, 25, 26, 27, 35, 39, 55, 56, 66, 67, 67א, 108, 115, 128, 147, 155 |
| Registrar fee regulations (full schedule) | https://he.wikisource.org/wiki/תקנות_הירושה_%28אגרות_הרשם_לעניני_ירושה%29 | Fee rows, 85% online rule, 1 January indexation, exemptions |
| Estate Tax Law (repealed) | https://he.wikisource.org/wiki/חוק_מס_עזבון | Repeal, deaths after 31 March 1981 |
| Inheritance Registrar portal | https://inheritance.justice.gov.il/ | Online filing of orders |

## Gotchas

- **The witnessed will has FOUR elements, not three (Section 20).** Agents routinely write "testator declares and signs, witnesses sign" and drop the fourth: the witnesses must CONFIRM IN WRITING ON THE WILL, by their signature, that the testator declared and signed. Without that confirmation clause the will is defective. Always include the Section 20 witness-confirmation wording.
- **Section 35 reaches preparers, not just witnesses.** A gift to whoever wrote, witnessed, or took part in making the will (or their spouse) is void, except in an oral will. Since an AI is helping draft, make sure a beneficiary is not the one preparing it.
- **The testator must be 18+ and of sound mind (Section 26).** Do not draft for a minor.
- **There are three order cases, not two (Section 66(b)).** Succession order (צו ירושה) for NO will; probate order (צו קיום צוואה) when a will covers the estate; and BOTH orders when the will covers only part of the property, a probate order on the willed part and a succession order on the remainder. Agents default to a binary answer and send partial-will families away with half an estate unresolved.
- **Representation stops where a spouse meets the parents' line (Section 14(a)).** Children step into a predeceased heir's place, but not where the deceased left a spouse together with parents or grandparents under Section 11(a). Do not state representation as an unqualified rule.
- **Ask how the flat was owned before answering "can they force me out" (Land Law Section 37, Succession Law Sections 113 and 115).** Co-heirs can force a sale of the inherited share, and the statutory tenancy is lost on a division by agreement.
- **A will does nothing until the probate order issues (Section 39).** No right can be claimed under a will, and the will cannot be relied on as a will, unless a probate order has been granted. Heirs holding the paper cannot make a bank move on it.
- **Never tell a user a flawed will is void.** Section 25 lets the Registrar or the court admit a will despite a missing date, signature, or witness-competence problem, if the מרכיב היסוד survives and there is no doubt about the testator's intent.
- **The will does not reach the pension or the life policy (Section 147).** Those pass by the מוטבים designation.
- **Deposit is not validity, but it is evidence (Section 21(b)).** Depositing the will protects the paper and does not make a defective will good. It does make the will prima facie evidence that the named testator made it and that it was made no later than the day of deposit, which is the reason to bother. Skipping deposit does not make a valid will invalid.

## Troubleshooting

### Error: "I had my spouse witness the will and they also inherit"
Cause: a beneficiary or their spouse signed as a witness.
Solution: that bequest to them can be voided. Re-sign the will with two neutral adult witnesses who inherit nothing, in everyone's presence.

### Error: "There is a will but they told me to apply for a succession order"
Cause: succession order (צו ירושה) is for estates with NO will.
Solution: when a will exists, apply for a probate order (צו קיום צוואה) instead, at the Inheritance Registrar.

### Error: "There is a will but it only mentions the apartment"
Cause: treating a partial will as though the choice of order were binary.
Solution: this is Section 66(b). Apply for a probate order over the willed part AND a succession order over everything the will does not cover. Set out the legal heirs for the remainder as in a no-will file.

### Error: "Is my typed will valid without a lawyer?"
Cause: assuming a lawyer or notary is required.
Solution: the Succession Law accepts a typed witnessed will that the testator dates and signs after declaring before two qualified witnesses, who confirm it in writing; no lawyer is required by law. Still recommend an inheritance lawyer's review of the draft before signing.
