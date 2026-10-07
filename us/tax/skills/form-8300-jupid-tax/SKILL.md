---
name: form-8300-jupid-tax
title: Form 8300 — Report of Cash Payments Over $10,000 Received in a Trade or Business
description: 'Use this skill when a trade or business has received more than $10,000 in cash from one buyer in a single transaction or related transactions, and must file Form 8300 with IRS + FinCEN within 15 days. Triggers: "received over $10,000 cash", "Form 8300 filing", "report cash payment to IRS", "BSA E-Filing", "do I have to report cash", "customer paid cash". Do NOT use for: bank deposits over $10K (banks file CTR — different form), suspicious activity reports (SAR — banks only), individual non-business cash receipts (gifts, inheritances).'
author: jupid-tax
author_url: https://github.com/jupid-tax/jupid-skills/tree/main/forms/form-8300
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: us
practice: tax
language: en
sources:
- title: Aggregation Rules
  path: references/aggregation-rules.md
- title: Bsa E Filing
  path: references/bsa-e-filing.md
- title: Cash Definition
  path: references/cash-definition.md
- title: Common Mistakes
  path: references/common-mistakes.md
- title: Customer Notification
  path: references/customer-notification.md
- title: Penalties
  path: references/penalties.md
---

# Form 8300 — Report of Cash Payments Over $10,000 Received in a Trade or Business

This skill produces an audit-grade draft of Form 8300 from the user's transaction facts. It walks through the cash definition, applies the aggregation rules, fills Parts I–IV, validates the result, and emits a deliverable the user can transcribe into the FinCEN BSA E-Filing System (or onto the paper form when paper filing is allowed) with confidence.

The form itself is short (two pages, four parts). The judgment is in *whether the threshold was actually crossed* and *what counts as cash*. This skill optimizes for the latter — the agent should ask, not guess.

**Form revision.** The item map in this skill was verified on 2026-10-06 against IRS Form 8300 (Rev. December 2023) / FinCEN Form 8300 (Rev. August 2014) and the Instructions for Form 8300 (Rev. December 2023). Before use, check https://www.irs.gov/forms-pubs/about-form-8300 for a newer revision and re-check the item numbers if one exists.

**Companion guide for end users:** [Form 8300 + AI Agent Skill: Cash Reporting Guide 2026](https://jupid.com/blog/form-8300-cash-payments-over-10000-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 8300, "8300", "BSA E-Filing", "FinCEN cash report", or §6050I
- The user describes a customer paying their business more than $10,000 in cash, in a single transaction OR a series of related transactions
- The user runs one of the high-frequency 8300 trades — used/new car dealer, jeweler, attorney, real estate broker, contractor, bail bondsman, art dealer, pawnbroker, boat/RV/aircraft dealer, wedding venue/caterer — and asks about cash compliance
- The user asks "do I have to report this cash" or "what do I file when someone pays cash"
- The user describes a customer paying with multiple money orders or cashier's checks for a consumer durable, collectible, or travel/entertainment

Do **not** engage this skill when:

- The user is a bank or financial institution required to file the FinCEN Currency Transaction Report (FinCEN Report 112) → no Form 8300 for that cash
- The user is a casino receiving cash in its gaming business → it files FinCEN Report 112, not Form 8300. Cash a casino receives in nongaming activities (restaurants, shops, nightclubs) IS reported on Form 8300 (Form 8300 instructions, "Casinos")
- The user wants to file a Suspicious Activity Report (SAR) → that is a separate FinCEN form, only filed by financial institutions and limited other categories
- The user received cash as a gift, inheritance, or personal transaction outside a trade or business → §6050I does not apply
- The user is making a personal cash deposit at their bank → the bank handles CTR reporting; the depositor files nothing

If the user's situation is ambiguous (e.g., a sole proprietor who occasionally takes cash but isn't sure their activity rises to a "trade or business"), ask before proceeding. The IRS reads "trade or business" expansively — operating regularly with a profit motive almost always qualifies.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **The transaction trigger.** What did the customer pay, when, in what form (currency / cashier's check / money order / mixed)? Was it one payment or multiple?
2. **Buyer identity.** Full legal name, current mailing address, date of birth, occupation, and TIN (SSN or ITIN). A nonresident alien who meets the TIN exception in the Form 8300 instructions (no effectively connected income, no U.S. office or paying agent, etc.) does not need a TIN; ask whether the exception applies rather than assuming it.
3. **Government-issued ID.** Type (driver's license, passport, state ID, alien registration card), document number, issuer. Identity of a person who claims to be an alien must be verified with a passport, alien identification card, or other official document evidencing nationality or residence (26 CFR §1.6050I-1(e)(3)(ii)). The agent should confirm the user has a photocopy or scan stored.
4. **Person on whose behalf** (if different from the buyer in the room). If an employee is paying on behalf of a company, or one spouse is paying for the other, Part II applies. Ask explicitly: "Is the person who handed you the cash buying for themselves, or for someone else?"
5. **Transaction details.** Date cash was received (or date the threshold was crossed for aggregated payments). Total cash amount. Amount in $100 bills or higher denominations. Item or service description (VIN for vehicles, matter description for legal services, project description for contractors).
6. **Filing business identity.** Business legal name, EIN (a sole proprietorship enters the owner's SSN, plus the EIN if it has one), address, nature of business, the authorized official who will sign (name and title), and the contact person's name and phone number (items 42–45).
7. **Aggregation history.** Has this same buyer paid the business cash before in the past 12 months? If so, total amount and dates of prior payments. The 12-month look-back is required to determine whether the threshold was crossed on this payment or earlier.
8. **Filing channel.** How many information returns OTHER than Form 8300 (Forms W-2, 1099 series, etc.) is the business required to file this calendar year? 10 or more → Form 8300 must be e-filed through BSA E-Filing (unless a Form 8508 waiver or the religious exemption applies); fewer than 10 → paper is allowed, e-filing optional. If e-filing, does the business already have a registered BSA E-Filing account? If not, registration comes first — see [`filing.md`](./filing.md).

For payment-method edge cases, additionally ask:

- If a cashier's check or money order was used: face amount of each instrument and whether the transaction was a "designated reporting transaction" (sale of consumer durable, collectible, or travel/entertainment). See [`references/cash-definition.md`](./references/cash-definition.md).
- If the buyer paid in foreign currency: the USD equivalent at the date of receipt.
- If the buyer paid using a mix of cash and other instruments: a breakdown of every component.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm the cash threshold actually triggered

Apply the §6050I cash definition strictly. **Personal checks, wire transfers, ACH, credit cards, and debit cards are NOT cash for Form 8300 purposes.** A customer paying you $50,000 by personal check triggers no 8300 obligation.

What IS cash:

- US currency and coins
- Foreign currency (convert to USD at the date of receipt)
- Cashier's checks, money orders, traveler's checks, and bank drafts **with face amounts of $10,000 or less** AND received in either (a) a designated reporting transaction (consumer durable / collectible / travel-or-entertainment retail sale) or (b) a transaction where the recipient knows the payer is structuring to evade reporting

Cashier's checks, money orders, bank drafts, and traveler's checks with face amounts **over $10,000** are NOT cash for Form 8300 — if they were bought with currency, the issuing bank must file its own currency transaction report (Pub 1544). A cashier's check that is the proceeds of a bank loan, or a payment on certain promissory notes, installment sales contracts, or down payment plans, is also not cash (Form 8300 instructions, Definitions, "Exceptions").

Digital assets were added to the statutory definition of cash (IRC §6050I(d)(3)), but under IRS Announcement 2024-4 a business does not have to count digital assets toward the $10,000 threshold until Treasury issues regulations. Re-check that status before relying on it.

If the cash definition is not met, stop. Do not file an 8300.

Full reference: [`references/cash-definition.md`](./references/cash-definition.md).

### Step 2 — Apply the aggregation rules

Sum all cash payments from the same buyer to the same business across:

- A single transaction
- Multiple payments for a single transaction (installments)
- A series of connected transactions within 12 months that the recipient knows or has reason to know are connected

If the cumulative cash exceeds $10,000 on the *current* payment, the 15-day clock starts on the date of the current payment.

If an 8300 was already filed for this buyer, start a new count: a new 8300 is triggered when *additional*, previously unreported cash from the same buyer within a 12-month period itself exceeds $10,000 (26 CFR §1.6050I-1(b)(3); Form 8300 instructions, item 29).

Full reference: [`references/aggregation-rules.md`](./references/aggregation-rules.md).

### Step 3 — Confirm the 15-day deadline date

Filing deadline = the **15th day after** the date of receipt (or the date the threshold was crossed for aggregated payments). If the 15th day falls on a weekend or federal holiday, the deadline rolls to the next business day. State the deadline date explicitly in the deliverable.

### Step 4 — Collect Part I (and Part II) identification data

For Part I (the individual from whom cash was received), items 3–14:

- Last name, first name, middle initial (items 3–5)
- TIN (item 6) — SSN or ITIN; leave blank only if the nonresident-alien TIN exception applies, or explain a missing TIN in the Comments section
- Address, city, state, ZIP, country if not U.S. (items 7, 9–12)
- Date of birth (item 8, MM/DD/YYYY)
- Occupation, profession, or business (item 13) — specific ("plumber", "retired attorney"), never "self-employed"; e-filed entries are limited to 25 characters
- Identifying document (item 14a type, 14b issuer, 14c number) — all three are required

For Part II (the person on whose behalf the transaction was conducted), items 16–27, if applicable: name or organization name, TIN (item 19; a sole proprietor gives both SSN and EIN), DBA name (item 20), address, occupation, and — only for a person not required to furnish a TIN — the alien identification document in item 27. Part II has no date-of-birth field. If the Part I individual is acting on their own behalf, skip Part II.

If two or more individuals conducted the transaction (e.g., joint buyers of a vehicle), check item 2 and complete Part I on page 2 for the others. The paper form holds three Part I entries; paper filers attach copies of Part I for more, e-filers can add up to 99. Item 15 works the same way for multiple Part II persons. Ask the user which individuals were physically present.

### Step 5 — Fill Part III (Description of Transaction and Method of Payment)

- Item 28: date cash received (or the date of the payment that caused the total to exceed $10,000)
- Item 29: total cash received as of that date
- Item 30: check if the item 29 amount was received in more than one payment
- Item 31: total price, if different from item 29
- Item 32: amount by form of cash, in U.S. dollar equivalent; the sum must equal item 29 — 32a U.S. currency (with the amount in $100 bills or higher), 32b foreign currency (with country), 32c–32f cashier's checks, money orders, bank drafts, traveler's checks (issuer name and serial number of every instrument)
- Item 33: type of transaction, boxes a–j (personal property, real property, personal services, business services, intangible property, debt obligations paid, exchange of cash, escrow or trust funds, bail received by court clerks, other). Check up to three; box i is only for court clerks, and bail bondsmen use box d
- Item 34: specific description (serial or registration number, address, docket number, VIN, etc.)

### Step 6 — Fill Part IV (Business That Received Cash)

- Item 35: name of business that received cash (legal entity name; a consolidated-group member reports its own information and puts the common parent's name and EIN in Comments)
- Item 36: EIN; a sole proprietorship must enter the owner's SSN, plus the EIN if it has one
- Items 37–40: address, city, state, ZIP
- Item 41: nature of business — specific ("used motor vehicle dealer", "jewelry dealer"), never "business" or "store"
- Item 42: signature of an authorized official, with title
- Item 43: date of signature
- Items 44–45: contact person's name and telephone number

### Step 7 — Run validation checks

See **Validation** below. Run every check. Don't skip checks even if the math looks clean.

### Step 8 — Produce the deliverable

See **Output format** below.

### Step 9 — Schedule the customer notification

The written statement to each person named on the Form 8300 (Part I and Part II) is required by IRC §6050I(e) and 26 CFR §1.6050I-1(f) and is due **January 31 of the year following the calendar year in which the cash was received**. Always include this in the deliverable as a scheduled follow-up. The statement is a separate obligation; failing to furnish it is penalized under IRC §6722. Reference: [`references/customer-notification.md`](./references/customer-notification.md).

### Step 10 — Hand off downstream

State the next steps the user must take:

- **File within 15 days** (BSA E-Filing, or paper if allowed) — see [`filing.md`](./filing.md) for the field-by-field flow
- **Save a copy of the completed form before submitting, plus the BSA tracking ID** — the instructions require keeping a copy of each Form 8300 for 5 years and say a filing confirmation is not a substitute for the form
- **Photocopy the customer's ID** if not already on file (5-year retention)
- **Schedule customer notification for January 31 of next year**
- **Retain all 8300 records, supporting documents, and notification proof for 5 years**

### Step 11 — File the return (optional, if the user wants the agent to file)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- BSA E-Filing System login flow and field-by-field mapping
- Paper path (fewer than 10 other information returns, Form 8508 waiver, or religious exemption)
- Submission state machine (Submitted → Acknowledged → Tracking ID issued)
- Security rules — never email or text the 8300 with SSN visible; encrypt at rest

If the user only wants a draft and will file themselves, skip this step.

---

## Critical ask-don't-guess rules

These rules exist because the wrong default looks like a working answer until the IRS audit reveals the misclassification.

1. **If the user mentions a "money order" or "cashier's check," ASK whether the face amount of the single instrument is over or under $10,000, AND whether the underlying transaction is a designated reporting transaction (consumer durable, collectible, or travel/entertainment).** A money order or cashier's check with face of $10,000 or less is *only* "cash" under §6050I if the transaction is a designated reporting transaction or the recipient knows the buyer is structuring. A cashier's check with face over $10,000 is never "cash" for Form 8300.
2. **If the user describes multiple payments from the same buyer, ASK for the cumulative cash total within the past 12 months.** The aggregation rule only triggers once cumulative cash exceeds $10,000. Don't assume a single $11,000 deposit is the trigger if the buyer also paid $5,000 cash three months ago.
3. **NEVER assume "cash" includes a personal check.** Personal checks are explicitly excluded from the §6050I definition regardless of amount. A $50,000 personal check is not reportable on Form 8300 (the bank may report on suspicious-activity grounds, but that is a separate filing the bank initiates).
4. **NEVER assume the buyer in the room is the principal.** If the cash was delivered by an employee, agent, attorney, or relative, Part II applies — ask explicitly who the goods or services are for.
5. **If the business must e-file and has not registered a BSA E-Filing account, do not skip ahead to filing instructions.** Registration is a prerequisite and takes its own time. Surface this gap before producing the field-by-field draft.
6. **If the user wants to file on paper, ASK how many information returns other than Form 8300 the business must file this calendar year.** Since January 1, 2024, a business required to file 10 or more information returns (excluding Forms 8300) must e-file its Forms 8300, unless it has an IRS waiver granted on Form 8508 or the religious exemption. A required e-filer that files on paper is treated as filing late (Form 8300 instructions, "Late returns"). Fewer than 10 → paper is allowed.

---

## Line-by-line guidance

Item numbers below are from Form 8300 (Rev. December 2023) and cover every item on the form.

### Item 1 (top of page 1)

- **1a Amends prior report** — Check only when amending. Complete the whole form (Parts I–IV) with the corrected information; do not attach the original. On BSA E-Filing, the amendment references the prior filing's BSA ID.
- **1b Suspicious transaction** — Check to report a suspicious transaction (it may be filed voluntarily even at $10,000 or less) and describe what was suspicious in the Comments section. Never mention this box in the statement sent to the customer.

### Part I — Identity of Individual From Whom the Cash Was Received (items 2–14)

| Item | What to enter | Source from user |
|------|---------------|------------------|
| 2 | Check if more than one individual conducted the transaction; complete Part I on page 2 for the others | Who was physically present |
| 3–5 | Last name, first name, middle initial | Government ID |
| 6 | TIN: SSN or ITIN | Buyer-provided |
| 7 | Address (number, street, apt. or suite no.) | Government ID |
| 8 | Date of birth, MM/DD/YYYY | Government ID |
| 9–11 | City, state, ZIP code | Government ID |
| 12 | Country (only if not U.S.) | Passport / ID |
| 13 | Occupation, profession, or business (specific; 25 characters if e-filed) | Buyer-stated |
| 14a–c | ID type ("driver's license"), issuer ("Utah"), number (no formatting or special characters) | Photocopy on file |

If a TIN was requested but could not be obtained within 15 days, file anyway and explain the missing TIN in the Comments section on page 2; a missing or incorrect TIN can draw a penalty. Ask the user whether the TIN was actually obtained or refused.

### Part II — Person on Whose Behalf This Transaction Was Conducted (items 15–27)

Used only when the Part I individual is acting for someone else. Common cases:

- An employee of a corporation paying for goods purchased by the corporation (Part II = the corporation, item 16 name and item 19 EIN)
- A relative paying on behalf of another household member
- An attorney or agent paying on behalf of a client

| Item | What to enter |
|------|---------------|
| 15 | Check if conducted on behalf of more than one person; complete Part II on page 2 for the others |
| 16–18 | Individual's last name, first name, M.I., or organization's name in item 16 |
| 19 | TIN (sole proprietor with an EIN: both SSN and EIN) |
| 20 | Doing business as (DBA) name, if different, with its EIN |
| 21, 23–26 | Address, city, state, ZIP, country if not U.S. |
| 22 | Occupation, profession, or business |
| 27a–c | Only for a person not required to furnish a TIN: ID type, issuing country, number |

If Part II applies, ask for the principal's TIN — it is required unless the nonresident-alien exception applies. A return that does not identify both the principal and the agent, when the recipient knows an agent is involved, is incomplete (26 CFR §1.6050I-1(e)(3)(ii)).

### Part III — Description of Transaction and Method of Payment (items 28–34)

| Item | What to enter |
|------|---------------|
| 28 — Date cash received | Date of payment, or date of the payment that caused the total to exceed $10,000 |
| 29 — Total cash received | Total cash as of that date, in USD |
| 30 — More than one payment | Check if item 29 was received in more than one payment |
| 31 — Total price if different from item 29 | E.g., full vehicle price when part was paid by check or loan |
| 32a–f — Amount by form of cash | U.S. currency (with amount in $100 bills or higher), foreign currency (with country), cashier's checks, money orders, bank drafts, traveler's checks; issuer name and serial number for every instrument; sum must equal item 29 |
| 33 — Type of transaction | Boxes a–j; up to three |
| 34 — Specific description | VIN, serial or registration number, property address, docket number |

### Part IV — Business That Received Cash (items 35–45)

| Item | What to enter |
|------|---------------|
| 35 — Name of business that received cash | Legal name of the entity |
| 36 — EIN (and SSN box) | EIN; a sole proprietorship enters the owner's SSN, plus EIN if any |
| 37 — Address | Business street address |
| 38–40 — City, state, ZIP | |
| 41 — Nature of your business | Specific description |
| 42 — Signature, title | Authorized official |
| 43 — Date of signature | MM/DD/YYYY |
| 44 — Contact person | Name |
| 45 — Contact telephone number | |

For e-filing, the signature is captured inside the BSA E-Filing System.

### Comments (page 2)

Up to 720 characters. Use it to explain a missing TIN, describe a suspicious transaction (item 1b), list extra instrument serial numbers, write "RELATED PARTY TRANSACTION" when the filer is related to the payer or principal (IRC §267(b)), name a consolidated group's common parent, and write "LATE" on a late e-filed report.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Threshold and definition checks

- [ ] Total cash (item 29) is **strictly greater than** $10,000. Exactly $10,000 does not trigger 8300 — the statute reads "more than $10,000."
- [ ] Every payment instrument counted toward the total fits the §6050I "cash" definition. Personal checks, wires, ACH, credit/debit cards excluded.
- [ ] If any cashier's check or money order is included, the underlying transaction is a designated reporting transaction OR the business knows the buyer is structuring. If neither, the instrument is not cash and should be removed from the total.
- [ ] If multiple payments are aggregated, all payments are from the same buyer (or its agent) to the same business, for one transaction or related transactions, within 12 months.
- [ ] Item 32 amounts sum exactly to item 29.

### Identification checks

- [ ] Buyer's TIN is present, OR the Comments section explains why it is missing (or the nonresident-alien TIN exception applies).
- [ ] Date of birth is present and in MM/DD/YYYY format.
- [ ] Item 14a, 14b, and 14c (ID type, issuer, number) are all filled; the number has no formatting or special characters.
- [ ] If more than one individual conducted the transaction, item 2 is checked AND each extra individual has a Part I entry on page 2 (or an attached Part I copy / additional e-file entry).
- [ ] If the Part I person is paying on behalf of someone else, Part II is filled with the principal's identity AND TIN.

### Deadline check

- [ ] 15-day deadline calculated from the date in item 28. Deadline rolls forward if it falls on a weekend or federal holiday.
- [ ] Deadline is in the future at time of draft. If it is already past, surface this loudly — the filing is late and a penalty has accrued.

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] The item 32a "$100 bills or higher" amount is $0 but item 32a is large — possibly an oversight; ask user to confirm the denomination breakdown.
- [ ] Item 29 is just over the threshold (e.g., $10,001) or earlier payments sat just under it — could be structuring; ask the user whether item 1b should be checked.
- [ ] Buyer's address is a PO Box — IRS prefers a residential or business address; capture both if available.
- [ ] Buyer refused to provide a TIN — file anyway, explain in Comments, and document the refusal.
- [ ] The transaction is the third or fourth 8300 from the same buyer in 12 months — pattern that may warrant item 1b (suspicious transaction).

### Cross-form checks

- [ ] Statement to each person named on the form (Part I and Part II) scheduled for January 31 of the year following the year the cash was received.
- [ ] Filing channel decided (10-return test); if e-filing, BSA E-Filing account exists OR registration step added to the deliverable.
- [ ] Document retention plan in place — a copy of the Form 8300 itself (5 years from filing, required), plus bill of sale, ID copies, BSA tracking ID, statement proof.

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe into the BSA E-Filing System. Format:

```markdown
# Form 8300 — DRAFT for filing year YYYY

## Filing context
- Date cash received: MM/DD/YYYY
- 15-day filing deadline: MM/DD/YYYY (state weekend/holiday rollover if any)
- Filing channel: <e-file required (10+ other information returns) / paper allowed / waiver / religious exemption>
- BSA E-Filing account status: <registered / needs registration / n/a>

## Item 1
1a. Amends prior report: <Yes / No>  (if Yes, prior BSA ID: ...)
1b. Suspicious transaction: <Yes / No>

## Part I — Identity of Individual From Whom Cash Was Received
2.  More than one individual:  <checked / not checked>
3.  Last name:                 <name>
4.  First name:                <name>
5.  M.I.:                      <initial>
6.  TIN (SSN/ITIN):            <xxx-xx-xxxx | blank — reason in Comments>
7.  Address:                   <number, street, apt/suite>
8.  Date of birth:             MM/DD/YYYY
9.  City:                      <city>
10. State:                     <state>
11. ZIP code:                  <ZIP>
12. Country (if not U.S.):     <country | blank>
13. Occupation:                <specific, ≤25 characters if e-filed>
14a. ID type:                  <driver's license / passport / etc.>
14b. Issued by:                <state or country>
14c. Number:                   <document number, no formatting>

## Part II — Person on Whose Behalf
<items 15–27 if applicable, otherwise "Skipped — Part I individual acted on own behalf">

## Part III — Description of Transaction and Method of Payment
28. Date cash received:                  MM/DD/YYYY
29. Total cash received:                 $X,XXX.00
30. Received in more than one payment:   <checked / not checked>
31. Total price if different from 29:    $X,XXX.00 | blank
32. Amount of cash received (must equal item 29):
    a. U.S. currency:      $X,XXX.00 (amount in $100 bills or higher: $X,XXX.00)
    b. Foreign currency:   $X,XXX.00 (country: ...)
    c. Cashier's check(s): $X,XXX.00
    d. Money order(s):     $X,XXX.00
    e. Bank draft(s):      $X,XXX.00
    f. Traveler's check(s):$X,XXX.00
    Issuer name(s) and serial number(s): <every instrument>
33. Type of transaction: <up to three of boxes a–j>
34. Specific description: <VIN, serial, address, docket number>

## Part IV — Business That Received Cash
35. Name of business:                    <legal name>
36. EIN:                                 XX-XXXXXXX   (SSN box: sole proprietor's SSN, else blank)
37. Address:                             <street>
38. City:                                <city>
39. State:                               <state>
40. ZIP code:                            <ZIP>
41. Nature of your business:             <specific description>
42. Signature / title:                   <authorized official, title>
43. Date of signature:                   MM/DD/YYYY
44. Contact person:                      <name>
45. Contact telephone number:            (XXX) XXX-XXXX

## Comments (page 2, ≤720 characters)
<missing-TIN reason, suspicious-transaction description, extra serial numbers, RELATED PARTY TRANSACTION, LATE — or "none">

## Required follow-ups
- [ ] File via FinCEN BSA E-Filing System (https://bsaefiling.fincen.treas.gov/) or on paper (if allowed) by MM/DD/YYYY
- [ ] Capture and save BSA tracking ID
- [ ] Save PDF copy with customer file (5-year retention)
- [ ] Send the statement to each person named on the form by January 31, YYYY (year after the cash was received)
- [ ] Retain ID copies, bill of sale, and BSA tracking ID for 5 years

## Validation summary
- Threshold: passed | <list failures>
- Identification: passed | <list failures>
- Deadline: <date>; status: future | past
- Sanity warnings: <list any warnings raised>

## Sources cited in this draft
- IRC §6050I (cash receipts in trade or business)
- 31 USC §5331 (BSA cash reporting)
- 26 CFR §1.6050I-1 (regulatory definitions)
- 26 CFR §301.6011-2 and Form 8300 instructions (e-filing required since Jan 1, 2024 for filers of 10+ other information returns)
- IRS Form 8300 (Rev. December 2023) and instructions
- IRS Publication 1544
- Rev. Proc. <year> (current penalty inflation adjustments)
```

The draft is **not** the filed form. The user (or the agent, with explicit authorization) still has to enter it into BSA E-Filing or onto the paper form. The deliverable's value is that every field is computed, every rule applied, and the customer-notification follow-up is scheduled before it falls through the cracks.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/cash-definition.md`](./references/cash-definition.md) — IRC §6050I "cash" definition, designated reporting transactions, what counts and what doesn't
- [`references/aggregation-rules.md`](./references/aggregation-rules.md) — Single vs. related transactions, 12-month look-back, installment payment timing
- [`references/customer-notification.md`](./references/customer-notification.md) — January 31 deadline, Pub 1544 model letter, §6722 penalty exposure
- [`references/penalties.md`](./references/penalties.md) — $340 per return (returns due in 2026), intentional disregard tiers, criminal exposure for structuring
- [`references/bsa-e-filing.md`](./references/bsa-e-filing.md) — FinCEN BSA E-Filing System overview, account registration, BSA tracking IDs
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Frequent 8300 filer errors with fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for the BSA E-Filing System, field-by-field map, paper path

## Examples

End-to-end worked Form 8300s. Use these as patterns when the user's situation is similar.

- [`examples/car-dealer-single-transaction.md`](./examples/car-dealer-single-transaction.md) — Used car dealer Hector receives $14,500 cash for a single vehicle sale
- [`examples/service-business-aggregating-payments.md`](./examples/service-business-aggregating-payments.md) — Contractor receives multiple cash deposits aggregating to $11,000 across a project
- [`examples/attorney-receiving-retainer.md`](./examples/attorney-receiving-retainer.md) — Attorney receives a $25,000 cash retainer delivered by a third party on behalf of a client

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS and FinCEN sites for the year being filed — penalty amounts adjust annually under inflation Rev. Procs.

- [Form 8300 + AI Agent Skill: Cash Reporting Guide 2026](https://jupid.com/blog/form-8300-cash-payments-over-10000-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 8300 (latest)](https://www.irs.gov/pub/irs-pdf/f8300.pdf) — the form itself
- [Instructions for Form 8300 (latest)](https://www.irs.gov/pub/irs-pdf/i8300.pdf) — line-by-line IRS guidance
- [About Form 8300](https://www.irs.gov/forms-pubs/about-form-8300) — IRS landing page with current revisions
- [Publication 1544](https://www.irs.gov/pub/irs-pdf/p1544.pdf) — Reporting Cash Payments of Over $10,000
- [FinCEN BSA E-Filing System](https://bsaefiling.fincen.treas.gov/) — required channel since 2024 for businesses that file 10 or more other information returns
- [FinCEN Form 8300 guidance](https://www.fincen.gov/resources/statutes-regulations/guidance/form-8300-information-trades-businesses)
- IRC §6050I (information reporting on cash transactions in a trade or business)
- 31 USC §5331 (BSA reporting of cash receipts in nonfinancial trades or businesses)
- IRC §6721 (failure-to-file information return penalties)
- IRC §6722 (failure to furnish payee statement — covers customer notification)
- IRC §7203 (willful failure to file; a felony with up to 5 years for §6050I violations)
- IRS Announcement 2024-4 (digital assets not yet counted toward the $10,000 threshold): https://www.irs.gov/pub/irs-drop/a-24-04.pdf
- 26 CFR §1.6050I-1 (Treasury Regulations defining cash, related transactions, designated reporting transactions)
- 26 CFR §301.6011-2 (e-filing of information returns; 10-return threshold from Jan 1, 2024)
- Form 8508 (Application for a Waiver from Electronic Filing of Information Returns): https://www.irs.gov/forms-pubs/about-form-8508
- 31 CFR Chapter X (FinCEN BSA regulations)
- Rev. Proc. 2024-40, §2.58–.59 — §6721/§6722 amounts for returns required to be filed (statements furnished) in 2026; Rev. Proc. 2025-32, §4.57–.58 — amounts for 2027. Verify the current-year Rev. Proc. before filing

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS and FinCEN forms, publications, and regulations. It is not tax or legal advice. It does not establish a CPA-client or attorney-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that high-volume cash businesses or unusual fact patterns warrant a licensed tax professional or AML/BSA compliance specialist's review.
