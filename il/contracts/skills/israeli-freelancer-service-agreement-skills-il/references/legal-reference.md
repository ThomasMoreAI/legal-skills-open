# Legal Reference - Israeli Freelancer Service Agreement

This reference grounds each clause of the generated agreement in Israeli statute and case law.
It is background for drafting, not legal advice. For ASCII statute links, see the table at the
bottom; Hebrew-slug source pages are named in prose.

## 1. The core risk: employee-vs-contractor reclassification

Israeli labor courts do not treat the words "independent contractor" in a contract as decisive.
They apply the **מבחן מעורב (mixed test)**, whose dominant component is the **מבחן ההשתלבות
(integration test)**: is the provider an integral part of the client's organization, or a
genuinely separate business? Secondary factors: who controls the work and hours, whether the
provider supplies its own tools, personal-performance requirement, exclusivity, and economic
dependence on the single client.

If the relationship looks like employment, a worker hired as a "contractor" can sue for
**retroactive recognition (הכרה בדיעבד)**. On recognition the worker is owed employee social
rights: severance pay, pension contributions, vacation, sick leave, holidays, and recuperation
allowance (הבראה). The contractual label is evidential, not determinative.

The leading case is **ע"ע 300256/98 אורי אייזיק נ' תה"ל**, which set the framework for both
retroactive recognition and the **restitution / set-off (קיזוז)** of the extra "contractor
premium" the worker was paid above a comparable employee wage. Restitution is allowed only in
narrow circumstances (for example, the fee was markedly higher than an employee wage AND the
contract expressly provided for set-off, or the worker insisted on עצמאי status).

Important framing: a set-off / gross-up clause **protects the client, not the freelancer**. It is
the client's mechanism to claw back the contractor premium if the relationship is reclassified, it
is enforced only in those narrow cases, and a court is not bound to honor it. It also cannot waive
non-waivable (cogent) labor rights such as severance or annual leave. So the clause should be
explained honestly, not presented to the freelancer as their protection.

Drafting implication: the freelancer's real protection against a surprise reclassification is the
**facts**, not the wording. Include an honest independent-contractor declaration (evidential only),
and pair it with operational hygiene (own tools, own hours, no company email, freedom to serve
other clients, no exclusivity, invoicing per deliverable, and an express right to use
subcontractors, since a personal-performance requirement is itself an integration-test marker).

## 2. Payment terms: חוק מוסר תשלומים לספקים, התשע"ז-2017

When a business client orders a service and the contract is silent on timing, סעיף 3 imposes a
default of **שוטף+45**: payment no later than 45 days from the end of the month in which the
invoice was submitted.

### 2a. The payment tiers (סעיף 3), by payer type

The law does not have one default. It has five, and only two of them can be varied by contract.

| Payer | Statutory term | Can the contract vary it? |
|---|---|---|
| רשות מדינה, משרד ממשלתי, מפעל הפיס, המועצה להסדר ההימורים בספורט | 45 days from invoice delivery, or **שוטף+30** when counted from month end | No. No contract-out clause |
| The same payers, for עבודות הנדסה בנאיות | 85 days from delivery, or שוטף+70 | No |
| מוסד להשכלה גבוהה מתוקצב, גוף מתוקצב, other statutory bodies | שוטף+45 | Only with the payer's CEO approval, only where justified by the engagement's special character or not exceptionally unfair, and reported to the SMB Agency |
| רשות מקומית | שוטף+45, and **שוטף+80** for building works | No. Externally funded portions may be deferred, capped at 150 days from invoice delivery |
| עסק (private business) | שוטף+45 | Yes, where justified by the engagement's special character or the term is not exceptionally unfair |

Note the direction of the common error: the ministry tier is **שוטף+30**, shorter than the business
tier, and it is mandatory rather than "often shorter". Look up the payer's tier; do not generalise.

### 2b. Interest is gated on bargaining power (סעיף 4)

Consideration not paid on time accrues shekel interest, and after a further 30 days **דמי פיגורים
(late-payment fees)** under חוק פסיקת ריבית והצמדה. But סעיף 4 restricts this remedy: for a
budgeted-body client or a **private-business client**, it applies only in an engagement where that
body or business had **עדיפות בעיצוב תנאי החוזה**, superior power in shaping the contract terms.

Drafting implication, and it is counter-intuitive: a freelancer who supplies their own draft
agreement has weakened their claim to the statutory interest remedy, because the client did not
shape the terms. So state late-payment interest as an **express contractual term** and treat the
statute as an additional, non-exclusive remedy rather than the primary one.

### 2c. Non-derogation (סעיף 7)

> אין להתנות על הוראות חוק זה אלא לטובת הספק.

The law is a one-way floor: its terms may be varied only in the supplier's favour. This is the
clean answer to a client pressing pay-when-paid or an unusually long term, and it should be cited
rather than hedged.

### 2d. The bounced-invoice reset and the check period (סעיף 3)

If the supplier submits an invoice missing a material detail required by the contract, or submits it
before the contractual conditions for payment were met, the client returns it and **the invoice is
treated as never having been delivered**, provided the client itemises the deficiencies. The clock
restarts on the corrected invoice.

The check period is capped: 23 business days from invoice delivery for the state, budgeted-body,
local-authority, and business tiers, and 60 days for building works. If the client returns the
invoice after that window, payment falls due within 10 business days of the original deadline.

Two traps: business-tier parties may **contract out of** the check-period rules, so a client-supplied
draft can strip the 23-day cap; and the clock runs from המצאה, so the contract should also nominate
one of the statutory delivery methods and an address.

Drafting implication: the freelancer benefits from setting an explicit, shorter term (for
example שוטף+30 or שוטף+0), fixing the check period expressly, requiring written itemised
deficiencies, naming the invoice delivery channel, writing interest in as a contractual term, and
reserving the right to suspend work on non-payment.

### 2e. Applicability: the client must be an Israeli "עסק"

The business tier keys off "עסק", defined in סעיף 2 as a מוסד כספי, עוסק מורשה, or עוסק פטור as
defined in the VAT Law. A foreign entity, including the Delaware parent an Israeli startup often
contracts through, is none of those. For a foreign client the whole of this chapter is inapplicable:
no default term, no interest regime, no non-derogation protection. Every payment safeguard must then
be drafted from scratch.

### 2e1. Allocation number on tax invoices (חשבוניות ישראל)

From 1 June 2026 a tax invoice above 5,000 ₪ before VAT between dealers must carry an allocation number
issued by the Tax Authority; without it the recipient cannot deduct the input VAT. The threshold was
10,000 ₪ from 1 January 2026. Drafting implication: an עוסק מורשה billing above the threshold should
state that invoices will carry an allocation number.

### 2f. Withholding tax (ניכוי מס במקור) and certificates

In Israeli B2B practice a client is often legally required to **withhold tax at source** from
payments to a supplier, unless the supplier provides a valid **אישור ניהול ספרים** and an
**אישור פטור / שיעור מופחת מניכוי מס במקור**. A complete agreement therefore states that the
consideration is subject to lawful withholding, that the provider will furnish these certificates,
and that absent valid certificates the client withholds at the statutory rate. Omitting this is a
common, painful surprise: the first payment arrives net of withholding and the contract is silent.
(The skill states the mechanism; it does not compute the user's withholding rate.)

## 3. IP ownership: חוק זכות יוצרים, התשס"ח-2007

The default ownership rule for a **commissioned work (יצירה מוזמנת)** is counter-intuitive for
clients. Under סעיף 35, the first owner of copyright in a commissioned work is the **CREATOR
(the freelancer)**, unless the parties agreed otherwise, expressly or impliedly.

**The "impliedly" is load-bearing and cuts against the freelancer.** The statute reads
"אלא אם כן הוסכם אחרת בין המזמין והיוצר, במפורש או במשתמע". An implied agreement is enough to
displace the creator default, and a client will argue implication from the ordinary commercial
facts: bespoke work commissioned for the client's product, paid in full, source files delivered,
output shipped to the client's own customers. It is therefore wrong to advise a freelancer that
their rights are safe because the contract is silent. Silence is contested ground. Whichever way the
parties want it, the allocation belongs in writing. Under סעיף 37 an assignment of copyright (or an
exclusive licence) requires a written document in any event.

Two contrasts:

- סעיף 35 also provides that for a commissioned **portrait or photo of a family/private event**,
  the default owner is the **commissioner** (the opposite default).
- סעיף 34 provides that for a work made by an **employee** in the course of employment, the
  **employer** owns it by default. This is why the contractor case is different: there is no
  automatic transfer to the client.

### 3b. Moral rights: narrower than most drafts assume

**Moral rights (הזכות המוסרית)** are separate and **non-assignable**. Under סעיף 45 the creator's
rights of attribution and integrity are personal, survive an assignment of the economic copyright,
and cannot be transferred. But two qualifications matter, and both are routinely missed:

- **Software is excluded outright.** סעיף 45 grants the moral right to the creator of an artistic,
  dramatic, musical or literary work "למעט תוכנת מחשב". Computer software is carved out by name, and
  a typeface is partly carved out as well. For a pure software deliverable there is therefore no
  moral right in play at all: no assignment problem, no waiver needed, and a moral-rights clause in
  a developer's contract is inert boilerplate. The carve-out does not extend to a designer's visuals,
  copy, photography, or audiovisual work, where the right applies normally.
- **There is no general statutory waiver.** The Copyright Law does not provide a mechanism by which
  a creator waives moral rights wholesale, so a clause drafted as a blanket waiver is claiming
  something the statute does not offer. What the law actually provides is in סעיף 50: an act that
  impairs the **integrity** right is not an infringement where it was **reasonable in the
  circumstances**, and the court is directed to weigh, among other factors, the nature of the work,
  the nature and purpose of the act, industry practice, and expressly whether the work was created
  **by an employee or on commission**. A commissioned deliverable therefore already sits on
  favourable ground for the client.

Drafting implication: for software, drop the moral-rights clause. Otherwise, replace "waiver of
moral rights" with the two things that actually work: the creator's **consent to specified
categories of modification** (which feeds directly into the סעיף 50 reasonableness assessment), and
an explicit **attribution arrangement** stating whether and how the creator is credited.

Drafting implication for the assignment itself: if the client is to own the deliverables, the
agreement must **expressly assign** the economic rights in writing (commonly on full payment), carve
out **third-party and open-source components** (which the freelancer can only license, not assign),
and let the freelancer retain rights in pre-existing tools, know-how, and general methods.

## 3d. Inventions (חוק הפטנטים, התשכ"ז-1967)

Copyright covers code and designs but not inventions. סעיף 132 vests a service invention
(אמצאת שירות) in the employer only where the inventor is an employee. A contractor's invention
therefore stays with the contractor absent an express assignment. A complete agreement addresses
inventions expressly, together with source-file delivery and an open-source component list.

## 3a. Data protection: Amendment 13 to the Privacy Protection Law

If the freelancer processes personal data on the client's behalf (a developer touching a user
database, a marketer handling a CRM or mailing list), the Privacy Protection Law and its
**Amendment 13 (in force August 2025)**, together with the information-security regulations, call
for a data-processing clause: the freelancer acts as a holder/processor for the client only, takes
reasonable security measures, notifies the client of a security incident without delay, and returns
or deletes the data at the end of the engagement.

## 3c. The governing statute: חוק חוזה קבלנות, תשל"ד-1974

This is the law that actually defines and governs the contract this skill drafts, and it is the one
most freelancer agreements never mention. סעיף 1:

> חוזה קבלנות הוא חוזה לעשיית מלאכה או למתן שירות בשכר כשהקבלן אינו עובדו של המזמין.

That is precisely a freelancer service agreement. Its rules are **defaults**, not mandatory terms:
סעיף 8 applies them only where no other law governs the matter "ובאין כוונה אחרת משתמעת מן ההסכם בין
הצדדים". Which is exactly why a competent draft has to engage with them rather than ignore them.

**סעיף 4: the client's self-help and unilateral price reduction.** Where the freelancer fails to cure
a defect within a reasonable time after notice, the client may (1) fix it and demand reimbursement of
reasonable costs, or (2) **deduct from the fee** the amount by which the defect reduced the work's
value. For an urgent defect the client may skip notice entirely, and where the defect cannot be
cured the deduction is available directly. This is a live, default-on client remedy: a startup
client facing a production bug has a statutory route to withhold part of the fee without agreeing
anything with the freelancer first.

Drafting implication: bound it. Cap aggregate set-off, require written substantiation of the claimed
loss in value, guarantee a genuine cure window with defined notice, and channel disagreements into
the acceptance and dispute procedure instead of self-help.

**סעיף 5: the contractor's lien.**

> לקבלן תהא זכות עכבון על נכס שמסר לו המזמין לביצוע מלאכתו או למתן שירותו, כדי תשלום הסכומים
> המגיעים לו מן המזמין עקב עסקת הקבלנות.

A statutory security right running in the freelancer's favour over client property held for the
work, until sums due are paid. It is stronger than the "suspend work" remedy most drafts stop at,
and it costs nothing to reserve. State it expressly so a broad delivery or return-of-materials
clause is not later read as a waiver.

**סעיף 3: the client's duty to notify defects.** The client must notify the freelancer of a defect
within a reasonable time of discovering it, or of when it should have discovered it, and must give a
proper opportunity to cure where the defect is curable. If it does not, it **may not rely on the
defect at all** (unless the freelancer knew of it). This is a freelancer-protective default. Take
care that a short deemed-acceptance window is not drafted so as to narrow it: the intent should be
that deemed acceptance governs sign-off and payment milestones, without displacing the client's
duty to give notice and a cure opportunity for defects discovered later.

## 4. Tax and invoicing context (background, not tax advice)

- **עוסק פטור** (VAT-exempt dealer): allowed only while annual business turnover does not exceed
  **122,833 ₪ (2026)**. An עוסק פטור does not charge VAT and reports turnover once a year (by
  31 January for the prior year). Above the threshold the provider must register as **עוסק
  מורשה**.
- **מע"מ (VAT)**: the rate is **18%** for transactions whose tax-liability date is on or after
  1 January 2025 (raised from 17%). An עוסק מורשה adds VAT against a חשבונית מס.

- **Foreign clients and the zero rate**: under סעיף 30 of חוק מס ערך מוסף a service supplied to a
  foreign resident may be **zero-rated**. It is not automatic. The benefit is denied where the
  subject of the engagement is that the service is in fact supplied, in addition to the foreign
  resident, also to an Israeli resident in Israel, and a single Israeli beneficiary is enough to
  defeat it. This bites often in practice: a developer contracting with a foreign parent while
  serving the Israeli subsidiary's team is exactly the contested pattern. Flag it and send the user
  to a רואה חשבון; do not pick a rate for them.

Drafting implication: the price clause must state whether the fee is +VAT, and the provider's
status (פטור/מורשה) drives whether VAT is added. Where the client is foreign, do not default the
clause to 18%. The skill states these figures as context; it does not compute the user's tax
liability.

## 5. Non-compete and restraint of trade: ע"ע 164/99 צ'ק פוינט נ' רדגארד

A bare non-compete clause is generally **not enforceable** in Israel. The court enforces a
restraint only where it protects a **legitimate interest**, chiefly a genuine **trade secret
(סוד מסחרי)**, special employer-funded training, special consideration paid for the restriction,
or good-faith/fiduciary duties, AND the restraint is reasonable in scope, duration, and
geography.

Drafting implication: default to a narrow confidentiality + non-solicitation + trade-secret
clause rather than a broad "do not compete" clause that a court will likely strike.

## 6. Liability, indemnity, and insurance

- A **liability cap** (for example, total liability limited to fees paid in the prior 12 months)
  with carve-outs for willful misconduct, IP infringement, and confidentiality breach is
  standard and enforceable by contract freedom.
- **Professional liability insurance (ביטוח אחריות מקצועית)** covers professional negligence,
  errors and omissions, breach of confidentiality, and document loss, including legal costs and
  client compensation. It is frequently a precondition for contracting with companies and public
  bodies, so the agreement may require the provider to carry stated coverage.

## 7. Governing law and forum

Use Israeli law and name a district's courts for general disputes, but note a caveat the skill
should surface: **classification disputes go to the labor courts (בתי הדין לעבודה)** regardless
of a contractual forum clause.

## ASCII source links

| Source | URL | What to check |
|---|---|---|
| חוק זכות יוצרים 2007 | https://www.nevo.co.il/law_html/law00/3953.htm | סעיף 34 / סעיף 35 defaults, סעיף 37 writing, סעיף 45 and סעיף 50 moral rights |
| חוק חוזה קבלנות 1974 | https://www.nevo.co.il/law_html/law00/71886.htm | סעיף 1 definition, סעיף 3 notice, סעיף 4 set-off, סעיף 5 lien, סעיף 8 default-only |
| חוק מוסר תשלומים לספקים 2017 | https://www.nevo.co.il/law_html/law00/144599.htm | סעיף 2 "עסק", סעיף 3 tiers and check period, סעיף 4 interest gate, סעיף 7 non-derogation |
| מע"מ בשיעור אפס לתושב חוץ | https://www.klf.co.il/tax-updates/zero-rate-vat-understanding-section-30-a-5-of-the-value-added-tax-law | סעיף 30 zero rate and the Israeli-beneficiary exception |
| כל-זכות: עוסק מורשה | https://www.kolzchut.org.il/he/%D7%A2%D7%95%D7%A1%D7%A7_%D7%9E%D7%95%D7%A8%D7%A9%D7%94 | VAT added at 18% |
| ע"ע 164/99 צ'ק פוינט נ' רדגארד | https://he.afiklaw.com/caselaw/2573 | non-compete enforceability standard |
| ביטוח אחריות מקצועית | https://www.bizreviews.co.il/article/professional-liability-insurance-guide | scope of professional liability cover |
