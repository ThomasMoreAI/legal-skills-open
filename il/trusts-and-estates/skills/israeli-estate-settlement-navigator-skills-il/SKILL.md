---
name: israeli-estate-settlement-navigator-skills-il
title: Israeli Estate Settlement Navigator
description: 'Operational project manager for settling an estate after a death in Israel. Use when someone has died and the family or estate administrator needs to know what to do and in what order: it builds a personalized dated bureaucratic timeline (first 72 hours, first 30 days, first year), a document-collection checklist, and ready-to-send bilingual Hebrew notification and account-closure letters. It covers the death certificate, the burial grant, the institution notification cascade, and the asset transfers that happen after the order. Do NOT use it to write or deposit a will or to obtain a succession order (צו ירושה) or probate order (צו קיום צוואה): route those to the skill israeli-wills-inheritance. Do NOT use it to check survivor-allowance or life-insurance eligibility: route those to israeli-survivor-benefits-navigator. For contested estates or foreign assets, state the facts and still recommend a licensed lawyer.'
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-estate-settlement-navigator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: trusts-and-estates
language: en
sources:
- title: Burial Charges
  path: references/burial-charges.md
- title: Domain Checklist
  path: references/domain-checklist.md
- title: Institution Checklist
  path: references/institution-checklist.md
- title: Money Tax And Employment After Death
  path: references/money-tax-and-employment-after-death.md
- title: Notification Letter Templates
  path: references/notification-letter-templates.md
---

# Israeli Estate Settlement Navigator

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. Responsibility for reporting and for paying the tax is yours, the binding computation is the Tax Authority's, and representation before the Tax Authority is reserved to those permitted by law. All use of its output is the user's sole responsibility.


## Problem

When someone dies in Israel, the family is grieving and, at the same time, is handed a maze of offices, forms, and phone numbers with no map. People visit the bank before they have the certified copies they need, wait months for a survivor allowance they were never told they had to actively claim, and pay for things the state already covers. This skill is the calm project manager: it turns the chaos into a dated to-do list, tells the user which office to visit in which order, and drafts the letters so nothing is missed and nothing is paid for twice.

## Instructions

You are an operational guide, not a lawyer and not a benefits calculator. Your job is to sequence the bureaucracy and generate paperwork. Ask only for what you need to personalize the plan, then produce the three deliverables. Never invent a form number, a fee, or a deadline: if you are unsure, point the user to the official source instead.

### What to ask first (keep it short)

1. Date of death, and did the death happen in Israel or abroad.
2. Was the deceased an Israeli resident.
3. Is there a known will, or is the family unsure.
4. What assets are involved at a high level (bank account, apartment, vehicle, pension, business).
5. Who is the user in relation to the deceased (spouse, child, named executor, other).

Use the answers to tailor the timeline and the checklist. Do not railroad: if the family already handled the burial, skip straight to the notification cascade.

### Deliverable 1: the personalized dated timeline

Anchor every milestone to the date of death. The helper `scripts/generate_timeline.py` computes the dates. Present it as three horizons.

**First 72 hours (burial and the first documents)**
- Obtain the הודעת פטירה (death notice) from the doctor or hospital that confirmed the death. This medical document is what lets the burial proceed; it is not the official certificate.
- Contact the Chevra Kadisha or the local religious council (or a civil-burial society) to arrange the burial. The burial grant (דמי קבורה) is paid by Bituach Leumi directly to the burial society, so basic burial is free to the family: the regulations bar the society from charging the family for the burial and the customary services.
- Do NOT tell the family that every charge is unlawful. First establish whether section 266 of the National Insurance Law covers the deceased: it covers burial in Israel of anyone who died in Israel, resident or not, and of an Israeli resident who died abroad. If it does, the Bituach Leumi (Burial Grant) Regulations, 5736-1976 allow a charge on top of the grant only in closed lists (regulations 3(a) and 4(a): a closed cemetery, agreed premium sections, a plot bought in the deceased's lifetime, out-of-area transfer, a detour the family requested, non-standard shrouds): outside them, refuse; inside them, the charge is lawful. If section 266 does not cover the deceased (for example a non-resident who died abroad and is brought here for burial), regulation 3(b) lets the society charge freely and the price is a commercial matter. Full wording: `references/burial-charges.md`.
- If the death was a direct result of acts of war (a fallen soldier, a victim of hostile action), section 269 takes it out of this burial-grant regime altogether: see `references/burial-charges.md`.
- If the death was abroad: section 267 pays the grant for burial abroad of an insured person, their spouse, or their child, capped at the domestic amount; and for a deceased with an Israeli ID, the death must be recorded in the population registry before the order is applied for.
- The burial grant does NOT cover the headstone (מצבה): it is a separate family cost (except in specific cases, such as a solitary deceased with no close relatives, where the state funds it). Tell whoever pays out of pocket that funeral, burial, and headstone costs rank FIRST among the estate's debts under section 104(a)(1) of the Succession Law, so the payer can normally be reimbursed from the estate ahead of every other creditor. Keep the receipts.
- If the family wants a non-religious burial, alternative civil burial (קבורה אזרחית חלופית) is a legal right and is offered by dedicated societies.

**First 30 days (registration, certificate, notification cascade)**
- Confirm the death is registered at Misrad HaPnim (Population and Immigration Authority). The doctor/hospital death notice feeds this; the official תעודת פטירה is then issued.
- Order the official death certificate. It is issued free of charge, and a first-degree relative can now download it immediately from the personal area on gov.il rather than waiting for the post. Order several certified copies anyway: banks, pension funds, insurers, and the Land Registry each want their own original or certified copy.
- Start from the government's own one-stop service rather than office by office. gov.il runs "ליווי לאחר פטירה (צעד אחר צעד)", an authenticated step-by-step service for first-degree relatives that downloads the death certificate, files and retrieves the succession or probate order, surfaces personally-matched benefits and rights, and runs the bank-account and insurance-policy locators. Send the user there first; it collapses several of the steps below.
- Find every account and policy before you start closing things. Two free government tools locate assets the family may not know about, by the deceased's ID:
  - **Har HaKesef (הר הכסף)**, run by the Ministry of Finance, is a search engine for lost/dormant pension savings, life-insurance policies, and bank accounts.
  - **Har HaBituach (הר הביטוח)**, run by the Capital Market, Insurance and Savings Authority, aggregates all of a person's insurance policies (life, health, pension, provident, vehicle, home) in one place.
  Run both before the cascade so no fund, policy, or account is missed.
- Work through the notification cascade below. Note that Misrad HaPnim forwards the death to many bodies automatically, so much of the cascade is confirmation and claiming, not first notice.
- If the family needs money NOW for the funeral, the headstone, or other death-related costs, do not assume they must wait for the order. Banks will generally release limited, reasonable sums from the deceased's account for immediate estate expenses before any order is produced, at the bank's discretion, with the surviving joint owner's consent, or against an indemnity letter signed by the potential heirs where all account owners have died. Ask the branch for this explicitly by name; it is rarely offered unprompted. (This dovetails with the debt priority above: these are the estate's first-ranking debts.)
- Some money does not wait for the order at all. Provident funds and life insurance with named beneficiaries pay those beneficiaries, even against the will, and very small balances may be released without an order under Finance Ministry circulars 2014-2-3 and 2017-9-8. Claim these in parallel.
- If the deceased employed a caregiver or housekeeper, the death counts as the worker's dismissal: the last salary, notice pay, unpaid recuperation pay, vacation redemption, and severance are owed, usually from the estate except severance already deposited in the pension fund. They are estate debts to settle before division; for a foreign caregiver's payroll arithmetic, route to `foreign-caregiver-payroll`. Detail for this and the next items: `references/money-tax-and-employment-after-death.md`.
- Cancel standing orders (הוראות קבע) for utilities and subscriptions with both the bank and the provider, so charges stop.
- Stop the deceased's OWN Bituach Leumi allowance. If the deceased received an old-age or disability allowance (קצבת זקנה / נכות), that personal allowance ends on death; only the amount that was due up to the date of death is still payable, and it is paid to the survivors, not for months after death. Make sure Bituach Leumi has stopped it so payments credited after death do not have to be sorted out later. (The separate death grant and survivor benefits belong to `israeli-survivor-benefits-navigator`.)
- If the deceased rented their home, notify the landlord, settle the estate's liability for the remaining rent, and terminate the lease so rent does not keep accruing against the estate.

**First year (orders, asset transfer, benefits)**
- The succession order (צו ירושה, when there is no will) or probate order (צו קיום צוואה, when there is a will) is obtained from the Registrar of Inheritance Affairs. That process is out of scope here: route the user to the `israeli-wills-inheritance` skill.
- Once the order is in hand, do the asset transfers (see the transfer checklist). A sole account in the deceased's name (and the deceased's share of any account with no survivorship clause) stays frozen until the order is presented; a joint account where the co-owners signed a survivorship clause in advance stays accessible to the surviving co-owner (see the bank note below).
- Survivor benefits must be actively claimed; they are not automatic. Route eligibility and amounts to `israeli-survivor-benefits-navigator`.

### Deliverable 2: the document-collection checklist

Generate it with `scripts/checklist.py` or use `references/institution-checklist.md`. The core documents the family will reuse everywhere:

| Document (He) | Document (En) | Where it comes from |
|---|---|---|
| תעודת פטירה (מספר עותקים) | Death certificate (several certified copies) | Population and Immigration Authority (free) |
| תעודת זהות של הנפטר | Deceased's national ID | Family / to be surrendered per office rules |
| תעודות זהות של היורשים | Heirs' national IDs | Family |
| צו ירושה / צו קיום צוואה | Succession order / probate order | Registrar of Inheritance Affairs (out of scope: `israeli-wills-inheritance`) |
| פירוט חשבונות, פנסיה, ביטוחים | List of accounts, pensions, insurance | Bank / funds / mislaka |
| נסח טאבו / הסכמי הלוואה ומשכנתה | Land Registry extract / loan and mortgage agreements | Land Registry / lenders |

### Deliverable 3: the notification and closure letters

Use the bilingual templates in `references/notification-letter-templates.md` (bank account closure, standing-order cancellation, utility/subscription cancellation, employer notification). Fill in the deceased's details, attach a certified death certificate copy, and, where the institution requires it, note that the succession/probate order will follow.

### The notification cascade (rough order)

| # | Institution (He) | Institution (En) | Why / note |
|---|---|---|---|
| 1 | ביטוח לאומי | Bituach Leumi | Often learns from Misrad HaPnim, but survivor benefits must be actively claimed |
| 2 | בנקים | Banks | Sole accounts (and a joint account with no survivorship clause) freeze until the order; a joint account with a pre-signed survivorship clause stays open to the surviving co-owner; cancel standing orders |
| 3 | קופות גמל / פנסיה / חברות ביטוח | Pension, gemel, insurers | Beneficiary payouts and claims |
| 4 | מעסיק | Employer | Final salary, unused-vacation redemption, and severance. Note the recipient: under section 5 of the Severance Pay Law, 5723-1963 severance on death goes to the statutory שאירים (spouse including a common-law partner living with them, and a dependent child; failing those, dependent children and parents, and dependent siblings who lived in the home for at least twelve months, whose share the labour court divides). Those are NOT necessarily the יורשים, and the money is not part of the estate. Exception, section 5(b1): for a death in the "determining period" (from 7 October 2023 until one year after the home-front special-situation declaration of that date ended: 28 October 2026 on the reported 28.10.2025 expiry, unless extended by ministerial order), only the spouse and a dependent child count, and if there are none the heirs take their place. Confirm the date with the employer or a lawyer |
| 5 | קופת חולים | HMO (kupat cholim) | Deregister the member |
| 6 | חברות תשתית (חשמל, מים, גז) | Utilities (electricity, water, gas) | Transfer or close the account holder |
| 7 | עירייה / ארנונה | Municipality / arnona | Change holder; a survivor-allowance-linked discount may apply |
| 8 | משרד הרישוי | Licensing Bureau (vehicle) | Vehicle transfer after the order |
| 9 | סלולר / אינטרנט / מנויים דיגיטליים / כרטיסי אשראי | Cellular, internet, digital subscriptions, credit cards | Cancel to stop recurring charges; notify each card issuer separately; keep the phone line until two-factor codes are moved |
| 10 | משטרה / האגף לרישוי כלי ירייה | Israel Police / firearms licensing division | The deceased's personal firearms license lapses on death; deal with any licensed weapon (see the firearm note below) |

### Asset-transfer checklist (only AFTER the order)

**How the order actually reaches the bank or the Tabu.** It neither arrives everywhere by itself nor must be hand-delivered. The Registrar emails the digital order to the applicant (or their lawyer). Onward transmission is per-body and triggered by the family: once a request for the action is filed, the Registrar sends the digital order directly to the banks, the insurance companies and government bodies such as the Land Registry (the "Tabu"), the Ministry of Transport, the Israel Land Authority, the Tax Authority and the Corporations Authority, which then do not need it presented at the counter. So: file the request for the action, and still keep the digital order and a certified copy to hand for any body outside that transmission. The service covers orders issued from 1998 onward.

- Bank funds and securities: have the order transmitted to the bank as above, and be ready to present it, to release the frozen accounts.
- Real estate: re-register at the Land Registry (טאבו / לשכת רישום המקרקעין). The Tabu is one of the bodies the Registrar transmits the digital order to once the request for the action is filed, so the re-registration usually starts from an order already on file rather than from a copy carried in by hand. Reassure the family up front: Israel does NOT levy an estate or inheritance tax, so simply inheriting is not taxed. Receiving real estate by inheritance is not treated as a taxable sale, so the heirs pay no purchase tax and no betterment tax at the moment of inheritance. A tax question (מס שבח / betterment tax) can arise only later, if and when an heir SELLS the inherited property. Then the heir steps into the deceased's purchase date and value (no step-up at death), but section 49B(5) of the Land Taxation Law exempts the sale of an inherited qualifying apartment by the deceased's spouse, descendant, or descendant's spouse, where the deceased owned only one residential apartment and would have been exempt selling it. The first division among the heirs is not a sale (section 5(c)(4)) unless an heir pays with money from outside the estate: the sibling-buyout trap. Detail in the money-and-tax reference; confirm any sale or buy-out with a יועץ מס.
- Vehicle: transfer at Misrad HaRishui with the death certificate and the order (a surviving spouse may have a simplified route). Before anyone drives it: the licensing bureau renews the vehicle license (רישיון רכב) for the relatives for ONE further year from its expiry, and the annual fee (אגרת רישוי) is still paid. No second renewal is issued without the order, so if that year passes without the succession or probate order the license lapses; once the order is in hand the heirs renew by appointment, so this is a window problem, not a permanent bar. Transferring registration by inheritance does not add a "hand" (יד) to the vehicle's ownership count. Because the mandatory insurance (ביטוח חובה) and license are tied to the registered owner, the car may be uninsured or unlawful to drive until things are regularized. Confirm valid insurance with the insurer before anyone drives it.

**Bank note (joint vs sole accounts).** The blanket "everything is frozen" is not quite right. A sole account in the deceased's name is frozen once the bank learns of the death and is released only against the order. A joint account is also frozen by default, UNLESS the co-owners signed a survivorship clause (טופס "אריכות ימים" / סעיף "היוותרות בחיים") in advance: with that clause the surviving co-owner can keep operating the account for routine activity before the order. Two caveats: the clause must have been signed in advance (you cannot add it after the death), and it does not override inheritance law, so a court may later require the survivor to return amounts that belong to the heirs.

**Safe-deposit box (כספת).** A safe-deposit box is treated like the account: a box in the deceased's sole name (or a jointly-held box with no advance arrangement) is inaccessible until the order is presented. This creates a chicken-and-egg problem when the original will is kept inside the box, because opening it may itself need the order or a registrar/court route. Raise this early if the family suspects the will is in a bank box.

**Firearm (כלי ירייה).** The deceased's personal firearms license lapses on death. Section 5(b)(5) of the Firearms Law, 5709-1949 exempts an heir or estate administrator from the licence requirement for exactly 30 days from the death; holding the weapon after that without a licence is an offence. To keep it, have it temporarily deactivated by a licensed dealer through the licensing bureau; otherwise surrender it to the police within those 30 days with the death certificate and the deceased's firearms license, and keep the deposit confirmation.

**Mortgage life insurance (ביטוח חיים ללווים).** Most Israeli mortgages carry borrower life insurance whose purpose is to guarantee the bank the remaining loan balance if the borrower dies. Before anyone keeps paying the mortgage, check for this cover and notify the lender and the insurer: the policy may pay off the balance.

### The debts question (reassure correctly)

Heirs never pay the deceased's debts from their own pocket: liability is capped by the value of estate assets, never by the heir's personal wealth. This is the Succession Law, 5725-1965, Chapter Six (sections 126 to 134). Funeral, burial, and gravestone costs rank first in the debt priority order under section 104(a)(1), ahead of the costs of the orders themselves and ahead of the deceased's ordinary creditors.

**But do not give the flat reassurance, because the cap depends on HOW the estate was divided.** Three regimes:

- **Before division** (section 126): heirs are not liable for estate debts at all except out of estate assets.
- **Divided AFTER creditors were invited** under section 99 or 123 and the then-known debts were settled (section 127(a)): an heir is liable for an unsettled debt only if it is proved they knew of it at the time of division, and only up to the value of **what that heir received**.
- **Divided WITHOUT inviting creditors** (section 128(a)): each heir is liable for the unsettled debts up to the value of the **whole estate** at the time of division, not merely their own share. Only an heir who proves they did not know of a particular debt drops back to the value of what they received, and section 128(b) puts the burden of proving value on the heir, not on the creditor. Concealing assets or a debt (section 129) exposes the heir to the whole estate's value regardless.

So the protective advice is procedural, not reassurance: invite the creditors before dividing, settle the known debts, and keep the division schedule. A family that quietly splits the money is in the section 128 regime. Section 133 lets a court relieve an heir who acted in good faith and either received little or has another special reason, but that is a discretionary remedy, not a right. Execution (Hotzaa LaPoal) files against the deceased are limited to registration-only measures until an administrator, succession, or probate order is produced (regulation 10A of the Execution Regulations, 5740-1979); a notice from the execution office does not by itself reach the heirs' own money. For a contested claim, an insolvent estate, or any division where debts are suspected, state these facts and still recommend a licensed lawyer.

### What this skill does NOT cover (say so, do not improvise)

Four things a family in this situation commonly needs are outside this skill, and the
failure mode is not silence but improvisation: an agent that does not know the procedure
will invent one. Name the gap and route it.

- **The deceased's tax computations.** What can be stated: under section 120 of the Income
  Tax Ordinance the legal personal representative (an heir, the administrator, the executor)
  is liable for the deceased's tax and must do what the deceased would have had to do; the
  heirs declare themselves to the assessing office on Form 2805 so the deceased's file can be
  closed. The year-of-death return, estate income, and closing a self-employed (עוסק) file at
  מע"מ and ביטוח לאומי are not worked here: send the user to the assessing office and to a
  רואה חשבון or יועץ מס. Do not guess a deadline.
- **Appointing an estate administrator (מנהל עיזבון).** Typically raised where the estate is
  contested, complex, has business assets, or cannot be settled by the heirs between
  themselves. This skill does not run that application. Route to a licensed lawyer.
- **Minor heirs, absent heirs, and heirs abroad.** Distribution touching a minor's share
  engages the guardianship regime and the אפוטרופוס הכללי. Do not tell the family they can
  simply divide. Route to a licensed lawyer. (Where there is no heir at all, the State
  inherits under section 17 of the Succession Law.)
- **A deceased who was a foreign resident, or an estate holding assets abroad.** Route to a
  licensed lawyer, as the domain checklist already records.

State the facts you do know, name which of these applies, and hand off. A confident wrong
procedure in this area costs the family more than an honest "this skill does not cover it".

## Bundled Resources

- `references/domain-checklist.md`: the full Must-cover / Should-cover / Out-of-scope map used to build this skill.
- `references/institution-checklist.md`: the institution-by-institution notification and document table.
- `references/notification-letter-templates.md`: ready-to-fill bilingual Hebrew letter templates.
- `references/burial-charges.md`: the full section 266 test and the closed lists of lawful burial-society charges.
- `references/money-tax-and-employment-after-death.md`: severance and its temporary provision, a caregiver the deceased employed, money released without the order, the deceased's tax files, real-estate tax on sale or division, execution files, death abroad, digital accounts and credit cards.
- `scripts/generate_timeline.py`: prints a dated 72h / 30-day / 1-year task timeline from a date of death.
- `scripts/checklist.py`: emits the document-collection checklist, optionally tailored by asset type.

## Recommended MCP Servers

| MCP | What it's for |
|---|---|
| kolzchut | Pulling the up-to-date Kol-Zchut rights pages for bereavement, burial, and estate procedures |
| israel-vehicles | Looking up the deceased's vehicle details before a Misrad HaRishui transfer |
| nadlan | Checking real-estate records before a Land Registry (Tabu) re-registration |

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Bituach Leumi: burial grant | https://www.btl.gov.il/benefits/dmaykvura/Pages/zacautKvura.aspx | Who is eligible and that the family pays nothing for standard burial |
| gov.il: death certificate | https://www.gov.il/he/service/death_certificate | How to order the free certificate and additional copies |
| gov.il: death registration | https://www.gov.il/he/service/death_registration | How the death is registered at Misrad HaPnim |
| Kol-Zchut: heirs rights guide | https://www.kolzchut.org.il/he/זכותון_ליורשים_ולקרובי_אדם_שנפטר_לתקופה_הסמוכה_למוות | The notification cascade and order of steps |
| Kol-Zchut: settling the deceased's debts | https://www.kolzchut.org.il/he/הסדרת_חובות_אדם_שנפטר | Heir liability limited to estate value; debt priority |
| Succession Law, 5725-1965 (full text) | https://www.nevo.co.il/law_html/law00/72178.htm | Section 104(a)(1) debt priority; sections 126 to 134 heir liability |
| Legal Capacity and Guardianship Law, 5722-1962 | https://www.nevo.co.il/law_html/law00/70325.htm | Section 32kd(b): the 90-day residual authority of an enduring power of attorney |
| Bituach Leumi (Burial Grant) Regulations, 5736-1976 | https://www.nevo.co.il/law_html/law01/039_109.htm | Regulations 3(a) and 4(a): the enumerated lawful burial-society charges; regulation 3(b): free charging where section 266 does not apply to the deceased |
| Severance Pay Law, 5723-1963 | https://he.wikisource.org/wiki/חוק_פיצויי_פיטורים | Section 5: who receives severance on death; 5(b1) temporary provision where heirs step in |
| Firearms Law, 5709-1949 | https://www.nevo.co.il/law_html/law00/72225.htm | Section 5(b)(5): an heir may hold the weapon licence-free for 30 days from the death |
| gov.il: post-death accompaniment (one-stop) | https://www.gov.il/he/service/post-death-accompaniment | Certificate download, order filing, matched benefits, account and policy locators |
| gov.il: vehicle transfer after death | https://www.gov.il/he/service/modification_registration_vehicle_following_death | Vehicle license lapses on death; one-year renewal for relatives; confirm insurance before driving |
| Har HaKesef (Ministry of Finance) | https://itur.mof.gov.il/ | Locate the deceased's lost pension savings, life-insurance policies, and bank accounts |
| Har HaBituach (Capital Market Authority) | https://harb.cma.gov.il/ | Locate all of the deceased's insurance policies and pension/provident savings |

## Gotchas

- Do not confuse the two orders: צו ירושה is for an estate with no will; צו קיום צוואה is for an estate with a will. Using the wrong term sends the family down the wrong application.
- Do not tell the family they are personally on the hook for the deceased's debts, and do not give the opposite flat reassurance either. They never pay from their own money, but an estate divided without inviting the creditors exposes each heir up to the value of the WHOLE estate, with the burden of proving value on the heir. Give the procedural advice: invite creditors, settle known debts, then divide.
- Do not tell the family they must pay the burial society, and do not tell them every charge is unlawful either. Where section 266 covers the deceased (anyone who died in Israel, or a resident who died abroad), only the enumerated charges are lawful; where it does not, regulation 3(b) lets the society charge freely. Do not assume a non-resident who died in Israel is outside section 266: its text covers anyone who died in Israel.
- Do not say severance on death always skips the heirs. For a death in the section 5(b1) determining period, the heirs take the place of absent spouse and dependent children.
- Do not say "notify Bituach Leumi and the survivor allowance will start." Bituach Leumi often already knows of the death, but survivor benefits must be actively claimed, and eligibility belongs to `israeli-survivor-benefits-navigator`.
- Do not hand over a generic global "after a death" checklist. The value here is the Israeli, institution-specific sequence (Misrad HaPnim, Bituach Leumi, Chevra Kadisha, the Registrar of Inheritance Affairs, the Land Registry, Misrad HaRishui).
- Do not tell the family they owe an "inheritance tax" or "estate tax": Israel does not levy one. Do reassure them, but note that selling an inherited property later can trigger betterment tax.
- Do not say all bank accounts are frozen. A joint account with a pre-signed survivorship clause stays accessible to the surviving co-owner; only sole accounts (and joint accounts without that clause) freeze until the order.
- Do not let anyone drive the deceased's car on the assumption it is still insured. The license lapses on death and the mandatory insurance is tied to the owner; confirm cover with the insurer first.
- Do not assume the free burial includes the headstone. The headstone (מצבה) is a separate, family-paid cost.

## Troubleshooting

- The bank refuses to release funds: for a sole account that is expected, and it stays frozen until the succession or probate order is presented. Route the order process to `israeli-wills-inheritance`. But if it is a joint account and the co-owners signed a survivorship clause (אריכות ימים / היוותרות בחיים) in advance, the surviving co-owner should be able to keep operating it for routine activity before the order; if the branch still blocks it, point them to that signed clause.
- The family only has one death certificate and offices keep asking for originals: order more certified copies (they are free) rather than photocopying.
- An enduring power of attorney (ייפוי כוח מתמשך) that the deceased signed: do not tell the family it is simply dead. It expires on death under section 32kb(2) of the Legal Capacity and Guardianship Law, 5722-1962, but section 32kd(b) gives the attorney for property matters a residual authority, for up to 90 days and without applying to court, to pay ongoing charges for services to the deceased or their property, pay reasonable burial and mourning expenses, and run a rented property or a business. It applies unless the principal directed otherwise and only while no one else is lawfully authorized, so it ends once an administrator is appointed or the order is produced. In the first weeks this is often the only lawful way to keep the mortgage paid and the shop open.
- The estate looks like it owes more than it holds: reassure that heirs are not personally liable beyond the estate value, then recommend a licensed lawyer for an insolvent or contested estate.
