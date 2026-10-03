# Payee Classification for 1099-NEC

The hardest decision in 1099-NEC issuance is whether to issue at all. The wrong answer in either direction creates problems:

- Issuing to a payee who shouldn't get one (e.g., a corporation, an employee mislabeled as contractor) can trigger an IRS audit of the payer's worker classifications.
- Failing to issue when required triggers IRC §6721 / §6722 penalties ($60-$310 per form depending on how late, indexed for inflation), plus potential disallowance of the deduction.

This file walks the agent through the classification decisions.

---

## Decision 1 — Worker classification: employee or contractor?

This is upstream of 1099-NEC. If the worker is actually an employee (per IRC §3121(d)(2) and the common-law test), the payer issues a **W-2**, withholds taxes, pays employer payroll taxes — not a 1099-NEC.

The common-law test (IRS Pub. 15-A) considers:

**Behavioral control** — does the payer direct how, when, where the work is done?
- Employee: schedule set by payer, location fixed, instructions detailed
- Contractor: contractor sets their own hours, methods, location

**Financial control** — who bears the financial risk?
- Employee: paid hourly or salary, expenses reimbursed, payer provides tools
- Contractor: paid by project / deliverable, contractor provides own tools, contractor bears profit-or-loss risk

**Type of relationship** — written contract, benefits, permanency
- Employee: ongoing relationship, benefits offered, written employment agreement
- Contractor: project-based, no benefits, written services agreement

**If misclassification is suspected**: file Form SS-8 (Determination of Worker Status) with the IRS. The IRS issues a determination letter. Outside this skill's scope — but flag the issue if the relationship looks like employment dressed as contracting.

**Consequences of misclassification**:
- IRC §3509 — payer liable for the worker's portion of FICA + federal income tax that should have been withheld, plus payer's share of FICA + FUTA
- Possible 100% trust-fund-recovery penalty on the responsible person (IRC §6672)
- State penalties separately

---

## Decision 2 — Entity classification: corporation, partnership, SMLLC, individual?

If the worker is correctly a contractor, the next question is what type of entity they are. This determines whether 1099-NEC applies.

### Rule: corporations are generally exempt

Payments to **C-corps and S-corps** for services are **not reportable** on 1099-NEC. Two exceptions:

1. **Medical / health-care payments** (1099-MISC Box 6) — reportable even to a corporation
2. **Attorney fees / legal services** (1099-MISC Box 10) — reportable even to a corporation

Both exceptions go on **1099-MISC**, not 1099-NEC.

### How to tell if the payee is a corporation

The W-9 Form Line 3 entity-type checkbox tells you:

| W-9 Line 3 box | Entity type | 1099-NEC required? |
|----------------|-------------|--------------------|
| Individual / sole proprietor or SMLLC | Individual or disregarded SMLLC | **Yes**, if threshold met |
| C Corporation | C-corp | **No** (except medical / legal — those go on MISC) |
| S Corporation | S-corp | **No** (except medical / legal — those go on MISC) |
| Partnership | Partnership | **Yes**, if threshold met |
| Trust / estate | Trust or estate | **Yes**, if threshold met |
| Limited liability company (with tax classification: C, S, or P) | LLC taxed as corp or partnership | C/S = No (with exceptions); P = Yes |
| Other | Government, nonprofit, etc. | Depends — usually exempt for nonprofits and govt entities |

### Common error: SMLLC mis-tagged as corporation

A single-member LLC that has NOT elected corporate / S-corp tax treatment is a **disregarded entity** — for federal tax purposes, it's the same as a sole proprietorship. The owner reports business income on their personal Schedule C.

Per W-9 Line 3, the SMLLC is supposed to check "Individual / sole proprietor or single-member LLC", NOT the LLC tax classification box.

Common error scenarios:

- SMLLC writes "ABC LLC" on W-9 Line 1 and provides the LLC's EIN. That's wrong — Line 1 should be the owner's name; Line 4 (TIN) should be the owner's SSN. (The IRS makes an exception if the SMLLC has its own EIN for payroll, but the W-9 instructions still say the *owner's* name must appear.)
- Payer treats the SMLLC as a corporation because it has "LLC" in the name — wrong. LLC is a state-law designation; for federal tax, default for SMLLC is disregarded.
- Payer fails to issue 1099-NEC because they assumed the LLC was incorporated — wrong, see above.

### Verifying corporate status

Don't take the payee's word — request a current W-9 in writing. The W-9 has a perjury declaration (Part II) — the payee certifies their entity type under penalty of perjury. The payer is protected if they relied on the W-9 in good faith (Reg. §31.3406(j)-1(c)).

If the payee refuses to provide a W-9, apply backup withholding (24%) on every payment until W-9 is received.

---

## Decision 3 — Service vs. goods

1099-NEC is for **services**. Payments for goods / merchandise / inventory are not reported.

**Mixed transactions** (services + goods bundled): the IRS expects the *services portion* to be reported if it's separately identifiable and crosses the threshold. If services and goods are bundled in a single price, look at the substance:

- Substantially services with incidental materials (e.g., a designer who ships a printed proof) → Box 1
- Substantially goods with incidental services (e.g., a vendor who delivers and installs) → not reportable (goods-dominant)

If unsure, require the contractor to itemize their invoices. This protects both sides.

---

## Decision 4 — Trade or business of the payer

1099-NEC reporting applies only to payments made **in the course of the payer's trade or business**.

**Personal payments are not reportable**. Examples:

- Paying a babysitter / housekeeper: not reportable on 1099-NEC (different rules apply for household employees — Schedule H)
- Paying a contractor for personal home renovation: not reportable
- Paying a personal trainer at home: not reportable

If the payer has both business and personal payments to the same individual, only the business portion is reportable.

A nonprofit / tax-exempt organization is treated as a trade or business for these purposes (IRC §6041(a) per Reg. §1.6041-1).

---

## Decision 5 — Payment channel

If the payer paid the contractor via a **third-party payment network** (Stripe, PayPal goods/services, Venmo business, Square, Cash App for Business, Zelle through some banks), the platform is the entity that issues a 1099-K, not the payer issuing 1099-NEC.

To avoid double-reporting, the payer **does not** issue a 1099-NEC for amounts paid via these channels.

**Direct payments NOT through a third-party network** are still 1099-NEC reportable:
- Cash
- Check
- ACH directly from payer's bank to contractor's bank (no intermediary platform)
- Wire transfer
- Direct debit from payer's account to contractor's account (Bill.com, some payroll-adjacent services may or may not be 1099-K covered — verify in the platform's documentation)

The litmus test: does the platform send a 1099-K to the contractor? If yes, the platform handles reporting. If no, the payer's 1099-NEC obligation stands.

For Zelle specifically: Zelle does not currently issue 1099-Ks (Zelle takes the position that it's a bank-to-bank rail, not a third-party network). Treat Zelle payments as direct ACH — payer issues 1099-NEC if threshold met.

---

## Quick reference table

For a contractor paid $3,500 in services during 2026:

| Payment method | Payee entity | 1099 required? | Form |
|----------------|--------------|----------------|------|
| Check or direct ACH | Individual / SMLLC / partnership | Yes | 1099-NEC |
| Check or direct ACH | C-corp or S-corp | No | None (unless medical / legal) |
| Stripe / PayPal goods-services / Venmo business | Any | No (payer side); platform issues 1099-K | 1099-K (by platform) |
| Zelle | Individual / SMLLC | Yes (Zelle ≠ TPN currently) | 1099-NEC |
| Personal payment (home babysitter, personal services) | Any | No | None (or Schedule H if household employee) |
