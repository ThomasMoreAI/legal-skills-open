# Filing Form 1099-NEC (browser automation)

How an agent equipped with browser tooling files Form 1099-NEC with the IRS and delivers Copy B to recipients. This file describes deterministic flows; it's complementary to `SKILL.md`, which produces the issuance plan or recipient reconciliation.

The agent must produce a complete `SKILL.md`-format issuance plan *first*, then pick a filing channel from the decision tree, then execute channel-specific steps.

This file applies to the **payor side** (issuing 1099-NECs). Recipients do not file 1099-NEC themselves — they receive Copy B and use the data to fill out Schedule C / Schedule 1, which has its own filing path.

---

## Channel decision tree

```
Issuing 10+ information returns total in the calendar year (any 1099 + W-2 combined)?
  → Electronic filing is MANDATORY (IRC §6011(e); T.D. 9972)
  → Use IRIS (free) or a paid service. FIRE is retired: from filing season
    2027 (tax year 2026 forms) IRIS is the only IRS intake system for
    information returns (Pub. 1099 (2026), What's New)
  → Skip paper Form 1096

Issuing < 10 information returns total?
  → Electronic optional, paper allowed
  → Default recommendation: still use IRIS (free, easier than paper)
  → Use Section 1 (IRIS) or Section 2 (paper) below

Already paying for tax software or payroll service that issues 1099-NEC?
  → That software's 1099 module
  → Use Section 3 (generic pattern)
```

---

## Section 1 — IRS IRIS (Information Returns Intake System)

URL: https://www.irs.gov/filing/e-file-information-returns

IRIS is the free IRS portal for filing 1099-series forms (NEC, MISC, K, INT, DIV, B, C, R, S, G, OID, PATR, Q, SA) plus Form W-2G. It has a Taxpayer Portal (manual entry / CSV upload, Pub. 5717) and an Application to Application channel (XML, Pub. 5718). A2A needs an IRIS Transmitter Control Code; Pub. 1099 (2026) says TCC applications typically take 45 business days, so apply early.

**Account model**: payer registers an IRIS account (one per EIN). The IRS may require ID.me identity verification for the responsible individual.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Payer's legal name, EIN, address, phone
- An ID.me account or equivalent for the responsible individual (mandatory in 2024+ for IRIS)
- Each recipient's full data: legal name, TIN, address, Box 1 amount, Box 4 amount (if any), state info
- The completed issuance plan from `SKILL.md`
- An email the user controls (IRIS sends submission confirmations)

### Browser flow

1. **Navigate** to https://www.irs.gov/filing/e-file-information-returns
2. **Click** "Sign in to IRIS" → ID.me login flow
3. **Complete identity verification** — document upload + biometric. Agent **must pause** here for user to complete; do not attempt to bypass.
4. **Land on IRIS dashboard** — select "File Forms" → "Form 1099-NEC"
5. **Choose method**:
   - **Manual entry**: type each form one at a time (good for ≤ 5 forms)
   - **CSV upload**: agent prepares a CSV per IRIS schema (good for batches)
6. **Manual entry path** — for each recipient, fill:
   - Recipient name, address, TIN
   - Box 1a (Nonemployee compensation; Box 1 on 2025 forms)
   - Boxes 1b–1d (cash tips, TTOC, overtime) — 2026 forms only, usually blank for contractors
   - Box 2 (direct sales ≥ $5,000) — checkbox
   - Box 3 (excess golden parachute payments) — rare
   - Box 4 (Federal tax withheld)
   - Boxes 5-7 (state) — repeat for additional states
   - Account number (if used)
7. **CSV upload path** — agent generates CSV matching the IRIS template (download from IRIS site for current year), validates columns, uploads, and confirms each row landed
8. **Review summary** — IRIS displays each form with totals; verify against the issuance plan
9. **Submit** — IRIS produces a Submission ID. Save the screenshot.
10. **Wait for IRS acceptance** (usually within minutes). On rejection, IRIS displays the error code; common codes:
    - `T-NAME-MISMATCH` — recipient name/TIN combo doesn't match IRS records → re-verify W-9, possibly issue B-Notice
    - `TIN-INVALID` — TIN format wrong (not 9 digits) → fix and resubmit
    - `DUPLICATE-FILING` — same recipient + same year already filed → was this a correction? Use "Corrected" flag
11. **Distribute Copy B to recipients**:
    - IRIS offers an option to e-deliver Copy B to recipients with their consent
    - Otherwise, the payer mails Copy B (postmarked by January 31, or the next business day; February 1, 2027 for 2026 forms) — IRIS generates a printable Copy B PDF
12. **State filing**: if state is in CF/SF program, IRIS can submit to states. Otherwise, agent files separately with state DOR.

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 9
- Do not bypass IRS identity verification
- Do not store SSN / EIN / TIN in agent logs
- Do not submit for the wrong tax year — IRIS lets you pick the year, but a misfile creates a duplicate-filing flag

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Identity verification failed" | ID.me biometric / document mismatch | Pause, ask user to complete via ID.me portal |
| "Form rejected — TIN mismatch" | Recipient name/TIN combo wrong | Verify W-9, send B-Notice if necessary |
| "Filing window closed" | Past deadline | Late-file with penalty (IRC §6721); use "Corrected" or "Late" flag |
| Session timeout | Idle > 30 min | Log back in; IRIS saves drafts |

---

## Section 2 — Paper filing (Form 1096 + Copy A)

For payers issuing < 10 information returns total who prefer paper.

### Assemble the return

1. **Form 1099-NEC Copy A** for each recipient (red ink scannable form — must be ordered from IRS or office supply store; cannot print from PDF and submit)
2. **Form 1096** — Annual Summary and Transmittal of US Information Returns. One Form 1096 per type of 1099 form. Submitting both 1099-NEC and 1099-MISC? Two 1096s.
3. **Form 1096** boxes:
   - Filer's name, address, TIN
   - Box 3: total number of forms transmitted
   - Box 5: total amount reported (for 1099-NEC, the box 1 and box 3 amounts per the Form 1096 instructions)
   - Box 6: form type code (form 1099-NEC has its own code: "71")

### Mailing address

The IRS mailing address for paper Form 1096 + 1099-NEC Copy A varies by state. The IRS posts current addresses at:

https://www.irs.gov/pub/irs-pdf/p1099.pdf (Pub. 1099, General Instructions for Certain Information Returns — the former "General Instructions" document) and the Form 1096 instructions

Look up the address by:
1. Form type (1099-NEC)
2. Filer's state

Do not hardcode — the IRS shifts addresses periodically.

### Mailing best practices

- Send via **USPS Certified Mail with Return Receipt** for proof of timely filing
- Postmark by **January 31** (next business day if it falls on a weekend or legal holiday; 1099-NEC has the same IRS deadline as recipient deadline)
- Keep a complete photocopy of the entire submission

### Copy B to recipient

- Print Copy B from IRS PDF (this copy can be printed in black ink — only Copy A must be the red ink scannable form)
- Mail to recipient by January 31 (or e-deliver with prior consent under IRS Pub. 1179 e-delivery rules)

---

## Section 3 — Generic third-party software pattern

For users with QuickBooks, Track1099, Tax1099, Gusto, Rippling, or similar:

1. Sign in → 1099 / Year-end module
2. Confirm payer info (EIN, address)
3. Import or enter recipients (most platforms pull from existing vendor records)
4. Verify each recipient's W-9 status and TIN match
5. Enter Box 1 amounts (often pulled automatically from payment records — verify against payer's GL)
6. Software files with IRS (e-file under the platform's IRIS transmitter control code) AND distributes Copy B to recipients (mail or e-delivery)
7. Pay platform fee per form (typically $2-5 per recipient)

Most platforms file CF/SF states automatically. Verify state coverage in the platform's documentation before relying.

---

## Section 4 — Backup withholding deposits (Form 945)

If the payer withheld 24% backup withholding on any payment:

1. Deposit the withheld amount with the IRS by EFT (EFTPS, IRS Direct Pay, or business tax account) using deposit schedules per IRC §6302 (monthly or semi-weekly depending on the Form 945 liability in the second preceding calendar year — Pub. 15 (2026), section 11)
2. File **Form 945** (Annual Return of Withheld Federal Income Tax) by **January 31** (or February 10 if all deposits made on time); February 1, 2027 for 2026
3. Report total backup withholding on Form 945 Line 2 (Line 1 is for pension, annuity, IRA, and gambling withholding)
4. The Form 945 total must equal sum of Box 4 across all 1099s issued

See https://www.irs.gov/forms-pubs/about-form-945 for current Form 945.

---

## Section 5 — Corrections

If a 1099-NEC was filed with errors:

- **One-step correction** (wrong dollar amount, wrong recipient address): file a corrected 1099-NEC with the "Corrected" box checked, showing the correct amount. Send a corrected Copy B to the recipient.
- **Two-step correction** (wrong TIN, wrong recipient name): file two forms — one with original (incorrect) info and $0 in Box 1 marked Corrected; then a separate new 1099-NEC with correct info.

See Pub. 1099 (2026), part H, for paper corrections; Pub. 5717 (IRIS Taxpayer Portal) and Pub. 5718 (IRIS A2A) for electronic corrections.

---

## Section 6 — Submission state machine

After filing:

1. **Submitted** — sent to IRS via IRIS / paper
2. **Accepted** — IRS acknowledges; for IRIS, usually within minutes
3. **Processed** — IRS posts to recipient's account; appears on recipient's IRS account transcript
4. **Notices** — Notice 972CG proposes information-return penalties (late or incorrect filing); CP2100 / CP2100A lists name/TIN mismatches that start the B-Notice process

Status checks:

- IRIS dashboard shows submission status
- IRS sends confirmation email per submission
- Recipients can verify their 1099-NEC appeared on their IRS account transcript (https://www.irs.gov/individuals/get-transcript)

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file these 1099-NECs through IRIS now" must be captured.
2. **Never store SSN, EIN, TIN, or banking data** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass IRS identity verification or ID.me.** If the system asks the user to prove identity, pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account.
5. **If a TIN mismatch appears**, surface it — do not silently file with a known-bad TIN. The fix flow involves a B-Notice to the recipient, not a workaround.
6. **Recipient consent for e-delivery**: payer must obtain affirmative recipient consent before e-delivering Copy B (Reg. §31.6051-1(j) for W-2; analogous Pub. 1179 rules for 1099). Do not e-deliver without consent on file.
