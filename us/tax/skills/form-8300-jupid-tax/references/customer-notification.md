# Customer Notification — January 31 Deadline

Form 8300 has a second-stage obligation that catches many filers by surprise: a written notification to the customer, due by **January 31 of the year following the filing year**. Failure carries an independent penalty under IRC §6722.

## Statutory and regulatory basis

- **IRC §6050I(e)(2)** — "Every person required to make a return … shall, on or before January 31 of the year following the calendar year for which such return was required to be made, furnish to each person whose name is required to be set forth in such return a written statement showing — (A) the name and address of the person required to make such return, and (B) the aggregate amount of cash described in subsection (a) received by the person required to make such return from the person required to be furnished the written statement."
- **IRC §6722** — penalty for failure to furnish correct payee statements; mirrors the §6721 information-return penalty structure.
- **IRS Publication 1544** — provides the model notification language.

## Who gets notified

Every person whose name is on **Part I** of Form 8300 must receive a notification. If Part II has a principal (a person on whose behalf the cash was paid), the regulations require notification to the Part I individual; some practitioners also notify the Part II principal as a defensive practice.

If multiple individuals delivered cash for one transaction (and additional 8300s were filed or attachments listed them), each individual on Part I of any such filing must be notified.

## When the notification is due

**By January 31 of the year following the year in which Form 8300 was filed.**

- 8300 filed in 2026 → notification due by January 31, 2027
- 8300 filed in March 2026 → notification due by January 31, 2027
- 8300 filed in December 2026 → notification due by January 31, 2027

If January 31 falls on a weekend or federal holiday, the deadline rolls to the next business day.

## What the notification must contain

Per IRC §6050I(e)(2) and Pub 1544, the written statement must contain:

1. **The name and address of the business** that filed Form 8300
2. **A statement that Form 8300 was filed** with the IRS
3. **The aggregate amount of reportable cash received** during the calendar year from the recipient of the notice
4. **A statement that the information was furnished to the IRS**

Some practitioners add the date(s) the 8300(s) were filed and the BSA tracking ID — these are not required by statute but help the customer reconcile their own records.

## Model notification language (Pub 1544)

> _On [date], we filed IRS Form 8300, Report of Cash Payments Over $10,000 Received in a Trade or Business. The form was filed because we received from you more than $10,000 in cash in [year]. The aggregate amount we reported was $[amount]. The information was reported to the Internal Revenue Service._
>
> _[Business name]_
> _[Business address]_

The notification can be longer or include additional context, but it must contain the four required elements.

## How to deliver the notification

- **Mailed paper letter to the customer's address of record on the 8300** is the audit-proof default. Use first-class mail; certified mail is overkill but harmless.
- **Email is acceptable** if the customer has provided an email address AND has consented to electronic delivery. The consent should be documented (signed form, recorded acknowledgment).
- **Hand delivery** is permitted but creates documentation difficulty — capture a signed receipt if used.

Retain proof of delivery for 5 years:

- For mailed letters: a copy of the letter, the date mailed, and (if certified) the certified-mail tracking number
- For email: a copy of the email, sent timestamp, and the recorded consent

## What the notification must NOT contain

- Do **not** include the customer's SSN, ID number, or other PII beyond their name and address
- Do **not** include the BSA tracking ID's full string in plaintext on a piece of paper that could be intercepted (last 4 digits is fine if any)
- Do **not** speculate about the IRS's future actions or imply audit risk to the customer

## Penalty for failure to notify

Under IRC §6722, the negligent failure-to-furnish-payee-statement penalty matches the §6721 failure-to-file structure. As of the most recent inflation adjustment (Rev. Proc. 2024-40 for 2025; verify the current year):

- **$310 per recipient** for negligent failure to furnish (timely)
- Higher tier for filings furnished late but within 30 days, after 30 days but by August 1, and after August 1
- **Intentional disregard:** the greater of $660 per statement or 10% of the aggregate amount required to be reported, with no annual cap

Critically, **this penalty is independent of and in addition to any 8300-filing penalty.** A business that filed the 8300 timely but missed the January 31 customer notification still owes the §6722 penalty.

## Common failure modes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Treating the notification as optional | $310+ per recipient | Schedule on the calendar at time of 8300 filing |
| Sending only one notification when multiple 8300s were filed for the same customer in a year | Per-statement penalty | Aggregate the year's filings into a single notification covering all reported amounts |
| Sending the notification before December (year of filing) | Technically not "for the year that just ended" — premature | Send between January 1 and January 31 of the following year |
| Sending after January 31 | Late-filing penalty tier | File the late notification anyway — late is cheaper than not at all |
| Including the customer's SSN in the notification | Privacy and security exposure | Remove; the customer already knows their SSN |

## When the customer is the same across multiple 8300s in one year

If the business filed three 8300s in 2026 for the same customer (different transactions), one consolidated notification by January 31, 2027 is acceptable. The notification should state the aggregate of all 2026 reported cash from that customer.

## Practical workflow

1. **At time of 8300 filing:** add a calendar reminder for January 15 of next year — review all 8300 filings from the prior year and identify unique customers.
2. **By January 31 of the next year:** mail one notification per unique customer covering all 8300s filed for them in the prior year.
3. **Retain proof of mailing or email delivery for 5 years** alongside the 8300 records.

The Jupid AI accountant or an equivalent workflow tool should automate this — most §6722 failures are not malicious; they are forgotten.
