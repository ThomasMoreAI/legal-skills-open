---
name: israeli-freelancer-service-agreement-skills-il
title: Israeli Freelancer Service Agreement
description: Draft a tailored Israeli freelancer service agreement (heskem matan sherutim) between an independent service provider (osek patur or osek murshe) and their client. Covers scope of services, payment terms under the 2017 Prompt Payment to Suppliers Law, the independent-contractor declaration that lowers the risk of a court reclassifying the relationship as employment (yachasei oved-maavid), IP ownership, confidentiality, termination, and indemnity. Use when a freelancer, consultant, designer, or developer needs a written contract before a project, or asks to draft a heskem hitkashrut or contractor agreement. Prevents costly retroactive employee-reclassification and unpaid-invoice disputes. Do NOT use for employment contracts (use israeli-employment-contracts), auditing a contract before signing (use israeli-employment-contract-reviewer), day-to-day invoicing (use israeli-freelancer-ops), or leases (use israeli-rental-agreements).
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-freelancer-service-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: contracts
language: en
sources:
- title: Domain Checklist
  path: references/domain-checklist.md
- title: Legal Reference
  path: references/legal-reference.md
---

# Israeli Freelancer Service Agreement

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Problem

Israeli freelancers (עצמאים) routinely start projects on a handshake or a one-line email, then get
burned two ways: a client pays 90 days late with no recourse, or, worse, a long engagement ends with
the "contractor" suing for retroactive recognition as an employee and winning severance, pension, and
back-benefits because the relationship looked like employment. A generic downloaded contract does not
account for Israeli law: the reclassification tests, the default copyright rule that leaves IP with the
freelancer, the statutory payment timing, or the VAT framing. This skill drafts a service agreement
built around exactly those Israeli rules.

## Instructions

This skill drafts a bilateral **service / contractor agreement (הסכם למתן שירותים)** from the
**freelancer's side**. Work through the steps; produce the contract in Hebrew (RTL) because it is
governed by Israeli law and will be read by Israeli parties.

> Always tell the user, once, that this is a drafting aid and not legal advice, and that a lawyer
> should review the agreement before signing. This is especially important when money or IP is
> significant.

### Step 1: Gather the deal facts

Collect the minimum needed to draft:

| Field | Why it matters |
|---|---|
| Provider name + ת.ז./ע.מ., status (עוסק פטור / עוסק מורשה) | Drives the VAT and invoicing clause |
| Client name + ח.פ./ע.מ., business or private | Drives payment-law applicability (the 2017 law applies to business clients) |
| **Is the contracting entity Israeli-registered?** | Decides whether the payment law and the VAT clause apply at all (see below) |
| Services / deliverables | The scope clause and IP clause |
| Fee + structure (fixed, hourly, monthly, milestones) | The consideration clause |
| Payment term wanted (e.g. שוטף+30) | Overrides the statutory default |
| Who keeps the IP | Decides whether to assign or license deliverables |
| Term and notice | Termination clause |

If the user does not know a field, use a sensible default and flag it in a "review these" list at
the end. Never invent the parties' identifying numbers.

**Ask the foreign-entity question before drafting anything else.** Israeli startups routinely
contract through a foreign (often Delaware) parent. If the counterparty is not an Israeli-registered
business, two whole sections of this skill stop applying:

- **The payment law does not apply.** חוק מוסר תשלומים keys its business tier off "עסק", defined in
  סעיף 2 as a מוסד כספי, עוסק מורשה, or עוסק פטור under the VAT Law. A foreign entity is none of
  those, so שוטף+45, the interest regime, and the non-derogation rule are all unavailable. Every
  payment protection must then be written into the contract from scratch.
- **The 18% VAT line may be a pricing error.** Under סעיף 30 of חוק מס ערך מוסף, a service supplied
  to a foreign resident can be zero-rated. It is **not automatic**: the benefit is denied where the
  service is in fact also supplied to an Israeli resident, and a single Israeli beneficiary defeats
  it. Flag it and route the user to their רואה חשבון rather than picking a rate for them.

### Step 2: Decide the independent-contractor framing (the most important step)

Israeli labor courts ignore the contract's label and apply the **מבחן מעורב (mixed test)**, dominated
by the **מבחן ההשתלבות (integration test)**: is the freelancer a separate business, or an integrated
part of the client's organization? If it looks like employment, the freelancer can later sue for
**retroactive recognition (הכרה בדיעבד)** and collect severance, pension, vacation, sick days,
holidays, and הבראה.

What actually protects the freelancer from a *surprise* reclassification is the **real facts**, not
the contract wording. So:

1. Include an **independent-contractor declaration** stating the provider runs its own business,
   bears its own tax, Bituach Leumi, and pension, and that the parties intend a commercial, not an
   employment, relationship. Courts give this **evidential weight only** (per ע"ע 300256/98 אורי
   אייזיק) and will apply the integration test to the real facts, so never present the label as
   decisive.
2. Build in **operational separation** that the contract reflects: own tools, own hours, freedom to
   serve other clients, no company email, no exclusivity, invoicing per deliverable, and an express
   right to use **subcontractors** (no personal-performance requirement, which itself helps the
   contractor case).
3. Understand the **set-off / gross-up clause** correctly before using it. It says that if a court
   later finds employment, the fee is treated as already inclusive of social rights and the excess
   over a comparable employee wage is set off against any award. This clause **protects the client,
   not the freelancer**: it is the client's tool to claw back the "contractor premium", it is enforced
   only in narrow cases (express term plus a fee markedly above a comparable salary), and a court is
   not bound to honor it. Do not sell it to the freelancer as their shield. It also cannot waive
   non-waivable (cogent) labor rights. Leave it out of the freelancer's own draft by default (the
   script adds it only with `--setoff`), and include it only when the client asks for it.

### Step 3: Draft the consideration, payment, VAT, and withholding clause

State the fee and structure, then set an **explicit payment term**. Under חוק מוסר תשלומים לספקים,
התשע"ז-2017, if the contract is silent and the client is a business, the default is **שוטף+45** (no
later than 45 days from the end of the month the invoice was submitted). A freelancer is better off
naming a shorter term (e.g. שוטף+30 or שוטף+0), and reserve the right to suspend work on non-payment.

Four things about this law that most drafts get wrong. Full tier table and statutory text are in
`references/legal-reference.md`:

1. **The tiers are not "government is shorter".** Ministries and state authorities pay 45 days from
   invoice delivery, or שוטף+30 when counted from month end, and they have **no** contract-out
   clause. Local authorities are שוטף+45, rising to שוטף+80 for building works. Only the business
   tier and the budgeted-body tier can vary the term at all. Look up the payer's tier; do not assume.
2. **The statutory interest is not automatic in B2B.** Under סעיף 4, the interest and דמי פיגורים
   remedy reaches a private-business client only where that client had **עדיפות בעיצוב תנאי החוזה**
   (superior power in shaping the terms). A freelancer who supplies their own draft may have argued
   themselves out of it. So write interest in as an **express contractual term**, and reference the
   statute only as an additional, non-exclusive remedy.
3. **The law is a floor, not a ceiling.** סעיף 7 provides אין להתנות על הוראות חוק זה אלא לטובת
   הספק: the parties may contract only in the supplier's favour. This is the direct answer to a
   client pushing pay-when-paid terms.
4. **A bounced invoice restarts the clock.** Under סעיף 3, if the invoice is missing a material
   detail or the contractual conditions for payment were not met, the client returns it and the
   invoice is treated as never delivered. The check period is capped at 23 business days for
   business clients, but B2B parties may contract out of that cap, so a freelancer's own draft
   should fix it expressly and require the client to itemise the deficiencies in writing.

State VAT correctly and unambiguously, because a wrong VAT framing is a direct error in the price:
- **עוסק מורשה**: "the fee is exclusive of VAT; VAT at 18% (as of 2026) will be added against a
  חשבונית מס." Say "exclusive of VAT" explicitly, since a bare number with no "+VAT" wording can be
  read as VAT-inclusive.
- **עוסק פטור**: "the provider is an עוסק פטור and does not charge VAT; a receipt will be issued." Add
  that if the provider crosses the turnover cap (122,833 ₪ for 2026) and converts to עוסק מורשה, VAT
  applies from that point.

**Allocation number (מספר הקצאה).** Under the חשבוניות ישראל model, from 1 June 2026 a tax invoice
above 5,000 ₪ before VAT between dealers must carry an allocation number from the Tax Authority, or the
client cannot deduct the input VAT. An עוסק מורשה billing a business client above that amount should
state in the invoicing clause that the invoice will carry one, so a client does not hold payment over it.

Add a **withholding-tax clause (ניכוי מס במקור)**: in Israeli B2B, the client may be legally required
to withhold tax from the payment unless the freelancer hands over a valid **אישור ניהול ספרים** and an
**אישור פטור / שיעור מופחת מניכוי מס במקור**. State that the provider will furnish these certificates,
failing which the client withholds at the statutory rate. Without this clause the freelancer is
blindsided when the first payment arrives net of withholding.

### Step 4: Draft the IP clause

This is the clause clients get wrong. Under חוק זכות יוצרים, התשס"ח-2007 (סעיף 35), the default owner
of a **commissioned work** is the **CREATOR (the freelancer)**, not the client. (Contrast: סעיף 34
gives an employer the copyright in an employee's work; a commissioned portrait or family-event photo
defaults to the commissioner.)

**Do not tell the freelancer that silence protects them.** סעיף 35 displaces the creator default
where the parties agreed otherwise **במפורש או במשתמע**, expressly *or by implication*. A client can
and does argue an implied transfer from the commercial context: bespoke work, full payment, source
files handed over, deliverables deployed to customers. So the freelancer who wants to retain anything
must say so in writing, exactly as a client wanting to own it must. Note too that under סעיף 37 an
assignment of copyright requires a written document, which is why "we agreed on a call" transfers
nothing.

So decide and draft explicitly:
- If the client should own the deliverables, **expressly assign** the economic rights, typically on
  full payment.
- If the freelancer is retaining anything, say so expressly. Silence is not retention.
- **Moral rights (הזכות המוסרית)**, attribution and integrity, are personal and non-assignable under
  סעיף 45. Two things follow that most drafts miss. First, **סעיף 45 excludes computer software
  outright**, so for a pure software deliverable there is no moral right to assign, waive, or worry
  about (typefaces are also partly carved out). Second, the Copyright Law provides no general waiver
  mechanism: under סעיף 50 an act touching the integrity right is simply not an infringement where it
  was reasonable in the circumstances, and the court expressly weighs the fact that the work was
  commissioned. So draft **consent to specified modifications plus an attribution arrangement**, not
  a blanket "waiver of moral rights" that the statute does not recognise.
- **Inventions and source code.** The Copyright Law covers code and designs, not inventions. Under
  חוק הפטנטים, התשכ"ז-1967, סעיף 132 vests a service invention in the employer only where the
  inventor is an **employee**, so an invention a contractor makes stays with the contractor unless the
  contract assigns it. A startup client will insist on this (investor due diligence checks it), so
  address inventions expressly, together with delivery of source files and a list of open-source
  components and their licences on full payment. Decide who owns inventions (`--inventions provider`
  or `client` in the script) instead of leaving it to the general IP assignment. The `provider` default
  keeps the invention with the freelancer and grants the client a non-exclusive, irrevocable,
  perpetual, royalty-free licence covering derivative versions. Where the invention is the startup's
  core technology, expect the client to demand exclusivity or `client`, and negotiate that price.
- The freelancer keeps rights in pre-existing tools, know-how, and general methods, and **third-party
  / open-source components are licensed, not assigned** (the freelancer often cannot transfer them).

### Step 5: Add the scope-protection and standard clauses

- **Displace the חוק חוזה קבלנות defaults deliberately.** This is the statute that actually governs
  the contract being drafted: סעיף 1 defines a חוזה קבלנות as a contract for work or services for
  payment where the contractor is not the client's employee, and סעיף 8 makes its rules apply only
  where the agreement does not provide otherwise. Two of its defaults matter enormously. Under
  סעיף 4, if the freelancer does not cure a defect in reasonable time the client may fix it at the
  freelancer's expense **or unilaterally deduct** the drop in value from the fee, with no notice at
  all for urgent defects. Bound that: cap any set-off, require written substantiation and a real cure
  window, and route disputes to the acceptance procedure rather than to self-help. Working in the
  freelancer's favour, סעיף 5 grants the contractor a **lien (זכות עכבון)** over client property held
  for the work until sums due are paid, and סעיף 3 bars the client from relying on a defect it failed
  to notify in reasonable time. Preserve both expressly; do not let a broad acceptance clause be read
  as giving them up.
- **Acceptance and revisions**: define how the client signs off on a deliverable, a deemed-acceptance
  window (e.g. silence for 7 business days = accepted), and how many revision rounds are included.
  "What counts as done" is where payment disputes live, so do not push it into an empty annex.
- **Termination and accrued fees**: state the notice period AND that on termination the freelancer is
  paid pro-rata for work done and approved expenses; for a cancelled fixed-price project, add a
  **kill / cancellation fee** based on progress. Without this, a designer terminated mid-project gets
  nothing.
- **Confidentiality (סודיות)**, surviving termination.
- **Restraint of trade**: default to a narrow trade-secret + non-solicitation clause, NOT a broad
  non-compete. A bare non-compete is generally unenforceable in Israel; courts enforce a restraint
  only to protect a legitimate interest like a real trade secret and only if reasonable in scope,
  time, and geography (ע"ע 164/99 צ'ק פוינט נ' רדגארד).
- **Liability cap + mutual indemnity**, with carve-outs for willful misconduct, IP infringement, and
  confidentiality breach. Make indemnity **mutual**: the client should indemnify the freelancer for
  client-supplied materials and for client misuse of the deliverables. Optionally require
  **professional liability insurance (ביטוח אחריות מקצועית)** if the client is a company or public
  body.
- **Data protection**: if the freelancer processes the client's personal data (a developer touching a
  user database, a marketer handling a CRM or mailing list), add a clause defining the freelancer as a
  processor with security obligations and breach notification, per the Privacy Protection Law and its
  Amendment 13 (in force August 2025).
- **Term, termination, and notice**; **governing law (Israeli) and jurisdiction**, noting that
  classification disputes go to the labor courts regardless of a forum clause.

### Step 6: Generate and hand off the draft

Assemble the Hebrew agreement. You can produce it directly, or use the helper script for a
consistent skeleton:

```bash
python3 scripts/build_agreement.py --provider "ישראל ישראלי" --provider-id 000000000 \
  --client "חברת לקוח בעמ" --client-id 510000000 \
  --services "עיצוב גרפי וניהול מותג" --fee 8000 --vat murshe --payment-net 30 \
  --out agreement.md
```

Switches: `--foreign-client` (drops the payment-law framing and leaves the VAT rate to a CPA),
`--personal-data` (processor clause), `--recurring` (monthly fee), and `--setoff` (the client-protective
reclassification set-off clause, off by default). The script warns when a `--vat patur` fee alone
exceeds the osek patur ceiling. Late interest is drafted by reference to the rates under חוק פסיקת
ריבית והצמדה, התשכ"א-1961, so the clause is not left without a rate.

End with a short "review these before signing" list (any defaulted fields, the IP choice, and the
recommendation to have a lawyer review).

## Examples

### Example 1: Designer with a new client

User says: "I'm a freelance graphic designer (עוסק מורשה). New client wants a 6,000 ₪/month brand
retainer. Draft me a contract."

Actions:
1. Gather facts; set fee 6,000 ₪/month +VAT, payment שוטף+30, designer keeps IP until paid then
   assigns deliverables.
2. Add the independent-contractor declaration. Leave out the set-off clause (it protects the client)
   unless the client asks for it, and then explain what it does.
3. Generate the Hebrew agreement and list "review these": notice period, insurance requirement.

Result: A draft Hebrew הסכם למתן שירותים for the designer to adapt and have reviewed before sending,
with VAT and IP handled correctly.

### Example 2: Developer worried about reclassification

User says: "I've been a 'contractor' for one company full-time for 2 years. They want a new contract.
What should it say so I'm not treated like an employee?"

Actions:
1. Flag the elevated reclassification risk (single client, full-time, long duration = strong
   integration-test markers).
2. Draft the declaration (no set-off clause unless the client demands it), AND advise concrete operational changes (own tools, serve
   other clients, no company email), explaining the clause alone is not decisive.
3. Suggest, where relevant, the user consult a lawyer given the exposure.

Result: A contract plus a practical risk-reduction checklist, with realistic expectations.

## Bundled Resources

### Scripts
- `scripts/build_agreement.py` -- Assembles a Hebrew service-agreement skeleton from parameters.
  Run: `python3 scripts/build_agreement.py --example`

### References
- `references/legal-reference.md` -- Clause-by-clause grounding in Israeli statute and case law
  (reclassification, payment law, IP default, VAT, non-compete, insurance).
- `references/domain-checklist.md` -- Coverage checklist the agreement is drafted against.

## Gotchas

- **Do not promise the contract label protects against reclassification.** Agents tend to write "the
  parties agree there is no employment relationship" as if it settles the matter. It does not: Israeli
  courts treat the label as evidence only and apply the integration test to the real facts. Always add
  the honest caveat.
- **Do not assume the client owns the deliverables by default.** The intuition from many jurisdictions
  is wrong here: under סעיף 35 of the 2007 Copyright Law, a commissioned work defaults to the
  freelancer.
- **But do not tell the freelancer that silence protects them either.** The same סעיף 35 displaces
  the creator default on agreement "במפורש או במשתמע", express *or implied*. A client can argue an
  implied transfer from the commercial circumstances. Retention must be written down, not assumed.
- **Do not draft a moral-rights waiver for software.** סעיף 45 excludes computer software from moral
  rights entirely, so the clause is inert in a developer's contract. Even for design and copy, the
  law provides no general waiver: use consent to specified modifications plus an attribution
  arrangement, and rely on the סעיף 50 reasonableness standard.
- **Do not leave payment timing silent and "rely on the law."** The statutory default (שוטף+45) is the
  worst case for the freelancer. Always set an explicit, shorter term.
- **Do not promise statutory late-payment interest in a B2B contract.** Under סעיף 4 that remedy
  reaches a business client only where the client had עדיפות בעיצוב תנאי החוזה, which is exactly what
  a freelancer-supplied draft undercuts. Make interest an express contractual term instead.
- **Do not ignore חוק חוזה קבלנות.** It governs this contract type by default and hands the client a
  unilateral fee-deduction right under סעיף 4. A draft that never mentions it leaves that weapon
  live and leaves the freelancer's סעיף 5 lien unclaimed.
- **Do not draft a broad non-compete.** A sweeping "shall not compete for 2 years" clause is usually
  unenforceable in Israel and signals an employment-like relationship. Use a narrow trade-secret /
  non-solicitation clause.
- **Do not state VAT generically.** Whether VAT is added depends on the provider's status (עוסק פטור
  charges none). Getting this wrong is a direct error in the price the client pays. The rate is 18%
  (from 1 January 2025), not the old 17%. State the fee as "exclusive of VAT" so a bare number is not
  read as VAT-inclusive.
- **Do not forget withholding tax (ניכוי מס במקור).** Israeli business clients often must withhold tax
  unless the freelancer provides a valid אישור ניהול ספרים and ניכוי-מס certificate. If the contract
  is silent, the freelancer is surprised by a payment that arrives net of withholding. Always include
  the certificate clause.
- **Do not sell the set-off clause as the freelancer's protection.** It is the client's tool to claw
  back the contractor premium if the relationship is reclassified, it is rarely enforced, and it
  cannot waive non-waivable labor rights. The freelancer's real protection is operational separation,
  not contract wording. Never recite in the freelancer's own draft that the fee is "higher than a
  comparable employee wage": in a later reclassification claim that sentence is the client's evidence.
- **Do not assign moral rights.** Moral rights (הזכות המוסרית) are personal and non-assignable under
  the 2007 Copyright Law. Assigning "all rights including moral rights" is partly void; use consent to
  specified modifications plus an attribution arrangement instead, and carve out third-party /
  open-source components the freelancer can only license.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| חוק זכות יוצרים 2007 | https://www.nevo.co.il/law_html/law00/3953.htm | סעיף 34 / סעיף 35 ownership defaults, סעיף 45 moral rights |
| חוק חוזה קבלנות 1974 | https://www.nevo.co.il/law_html/law00/71886.htm | סעיף 4 client set-off, סעיף 5 contractor lien |
| חוק מוסר תשלומים לספקים 2017 | https://www.nevo.co.il/law_html/law00/144599.htm | payment tiers, סעיף 7 non-derogation |
| מע"מ בשיעור אפס לתושב חוץ | https://www.klf.co.il/tax-updates/zero-rate-vat-understanding-section-30-a-5-of-the-value-added-tax-law | when a foreign-client fee is zero-rated |
| כל-זכות: עוסק מורשה | https://www.kolzchut.org.il/he/%D7%A2%D7%95%D7%A1%D7%A7_%D7%9E%D7%95%D7%A8%D7%A9%D7%94 | VAT added at 18% |
| ע"ע 164/99 צ'ק פוינט נ' רדגארד | https://he.afiklaw.com/caselaw/2573 | non-compete enforceability standard |
| ביטוח אחריות מקצועית | https://www.bizreviews.co.il/article/professional-liability-insurance-guide | professional liability cover |

## Troubleshooting

### Error: "The client says they own everything I make for them"
Cause: The client assumes a work-for-hire default that does not exist for contractors in Israel.
Solution: Point to סעיף 35 of the 2007 Copyright Law (commissioned work defaults to the creator).
Caveat the freelancer needs to hear: that default is displaced by agreement "במפורש או במשתמע", so a
client can argue an implied transfer from the commercial context. Do not rest on silence. Put the
allocation in writing either way, and negotiate assignment on full payment.

### Error: "Is the no-employment clause enough to protect me?"
Cause: Over-reliance on the contract label.
Solution: No. It is evidential only. Combine the clause with real operational separation (own tools,
own hours, multiple clients, no company email) and, for high exposure, advise a lawyer.

### Error: "The client wants to pay 'when they pay their client', is that allowed?"
Cause: Pay-when-paid terms that push beyond the statutory default.
Solution: If the client is an Israeli business, the law answers this directly. סעיף 7 provides that
its terms may be varied only in the supplier's favour, and the business tier allows a different term
only where the engagement's special character requires it or the term is not exceptionally unfair.
A pay-when-paid clause tied to a third party's behaviour is neither. Set an explicit term instead.
If the client is a foreign entity, none of this applies and the term must be negotiated on its own.
