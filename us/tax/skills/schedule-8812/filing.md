# Filing Schedule 8812 (browser automation)

How an agent equipped with browser tooling can take a completed Schedule 8812 worksheet and file it with Form 1040. The agent must produce a complete `SKILL.md`-format worksheet *first*, then pick a filing channel from the decision tree, then execute the channel-specific steps.

---

## Channel decision tree

```
User has AGI ≤ $89,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners; 2026 filing season limit,
    https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free)
    Browser automation: provider-specific.
    Skip — proprietary flows change too often for deterministic automation.

User wants to fill the form directly themselves?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has paid tax software (TurboTax, H&R Block, FreeTaxUSA)?
  → That software's "Dependents" or "Child Tax Credit" wizard
    Use Section 2 (generic pattern).

User wants to file on paper?
  → Print Form 1040 + Schedule 8812 + supporting schedules, sign, mail
    Use Section 3.
```

IRS Direct File was not offered in the 2026 filing season (it is not among the IRS free filing options, and https://www.irs.gov/filing/irs-direct-file redirects to a page that returns 404 as of 2026-10-06). Do not offer it as a channel.

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: opens in late January; for 2025 returns the program closes **October 15, 2026** (IRS Free File Fillable Forms page, reviewed 24-Sep-2026). After that date, use paid software or paper.

### Pre-flight

The agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI (for IRS identity verification)
- Each dependent's full legal name, SSN (or ITIN/ATIN), relationship, birthdate
- The completed SKILL.md worksheet
- Form 1040 inputs (filing status, AGI, tax before credits, etc.)

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms"
3. **Register / Sign in** for the current tax year
4. **Identity verification** (prior-year AGI or self-select PIN)
5. **Start a new return** → "Form 1040" landing
6. **Fill 1040 header** (name, SSN, filing status, dependents)
   - For each dependent (2025 Form 1040 Dependents rows (1)–(7)): first name, last name, SSN, relationship, lived with you more than half of 2025 (and in the U.S.), full-time student / permanently and totally disabled, and the row (7) credit box
   - The "Child tax credit" box should be checked **only** for qualifying children under 17 with an SSN valid for employment issued before the due date, and only if the filer (or one spouse if MFJ) has such an SSN
   - The "Credit for other dependents" box should be checked for dependents who don't meet CTC criteria but meet the ODC rules
   - **DO NOT check both** for the same dependent
7. **Add Schedule 8812**:
   - Click "Add a Form / Schedule"
   - Search "Schedule 8812"
   - Schedule 8812 opens

8. **Fill Schedule 8812 from the worksheet** — line-by-line mapping (2025 Schedule 8812; FFFF field labels follow the form's line numbers):

| Schedule 8812 line (2025) | Entry | Source (in worksheet) |
|--------------------|------------------|----------------------|
| 1 | Form 1040 line 11a | AGI |
| 2a / 2b / 2c / 2d | Numeric | Puerto Rico exclusion / Form 2555 lines 45 + 50 / Form 4563 line 15 / total |
| 3 | Computed | MAGI (line 1 + 2d) |
| 4 | Number | N_CTC |
| 5 | Computed | N_CTC × $2,200 |
| 6 | Number | N_ODC |
| 7 | Computed | N_ODC × $500 |
| 8 | Computed | line 5 + line 7 |
| 9 | Numeric | $400,000 MFJ / $200,000 others |
| 10 | Numeric | line 3 − line 9, rounded up to next $1,000 |
| 11 | Computed | line 10 × 5% |
| 12 | Computed | line 8 − line 11 (stop if not more) |
| 13 | Numeric | Credit Limit Worksheet A |
| 14 (→ 1040 line 19) | Computed | min(line 12, line 13) |
| **Part II-A** | | |
| 15 | — | Reserved |
| 16a | Computed | line 12 − line 14 |
| 16b | Number × $1,700 | N_CTC × $1,700 |
| 17 | Computed | min(16a, 16b) |
| 18a / 18b | Numeric | Earned income / nontaxable combat pay |
| 19 | Computed | line 18a − $2,500 (if more) |
| 20 | Computed | line 19 × 15% |
| **Part II-B** (only if line 16b ≥ $5,100 and line 20 < line 17, or Puerto Rico) | | |
| 21 | Numeric | W-2 boxes 4 + 6 |
| 22 | Numeric | Schedule 1 line 15 + Schedule 2 lines 5, 6, 13 |
| 23–26 | Computed | per the worksheet |
| **27 (→ 1040 line 28)** | Computed | ACTC |

9. **Verify auto-computed flow**:
   - Schedule 8812 line 14 → Form 1040 line 19
   - Schedule 8812 line 27 → Form 1040 line 28
   - Form 1040 totals tax (line 24) and payments (line 33) update

10. **Run FFFF's "Check Form" / "Verify"** — resolve every flag before submission

11. **Cross-check against the worksheet**:
    - Each FFFF computed line matches the worksheet
    - Each dependent's SSN entered is exactly what's in IRS records (typo = rejection)
    - Phase-out reduction matches (FFFF rounds up to nearest $1,000 for excess MAGI)

12. **Save the return** (FFFF stores progress server-side)

13. **Submit** when 1040 is complete:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN + prior-year AGI)
    - Submit

14. **Capture the submission ID** — save the screenshot

15. **Wait 24–48 hours**, then confirm IRS acceptance. A common dependent rejection is **R0000-504-02** (dependent SSN/name mismatch with IRS records). On rejection:
    - Verify name spelling against the dependent's Social Security card (not informal nicknames)
    - Verify SSN
    - If the reject is R0000-507-01 instead, the dependent's SSN was already used on another return — investigate (tiebreaker rules, Form 8332) before resubmitting or paper-file

### What the agent should NOT do

- Do not check both "qualifying child" and "other dependent" boxes for the same dependent
- Do not enter ITIN/ATIN children as qualifying children — they go in the ODC count
- Do not skip the SSN-before-the-due-date check for any qualifying child or for the filer
- Do not submit without the user's explicit go-ahead
- Do not store SSN, DOB, or PIN in any log or transcript

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| R0000-504-02 (dependent SSN and last name don't match IRS records) | Name typo or wrong SSN | Verify against the Social Security card (https://www.irs.gov/filing/free-file-fillable-forms/r0000-504-02) |
| FFFF says "qualifying child age limit exceeded" | Child turned 17 during the year | Reclassify as ODC ($500 instead of $2,200) |
| FFFF won't allow CTC for dependent with ITIN | ITIN doesn't qualify for CTC | Enter as ODC instead |
| ACTC computed as $0 despite leftover credit | Earned income ≤ $2,500, Form 2555 filed, or no qualifying child on line 4 | Confirm earned income figure and SSN status; if correct, ACTC truly is $0 |
| Phase-out reduces credit to $0 | High MAGI | Verify MAGI; user may not be eligible at all |
| Two FFFF returns claim the same dependent | Tiebreaker rules apply per IRC §152(c)(4) | The first filer wins typically; second is rejected with R0000-507-01 |

---

## Section 2 — Generic tax-software pattern

For users with paid software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the typical flow:

1. Sign in → start or resume a return
2. Navigate to the **"Dependents"** section (sometimes labeled "My Family" or "Personal Info")
3. For each dependent, the wizard asks:
   - Name, SSN, birthdate, relationship
   - "Did this person live with you more than half the year?"
   - "Did you provide more than half their support?"
   - "Did this person have a Social Security Number issued by [due date]?"
   - The wizard auto-classifies as qualifying child or qualifying relative
4. Continue to **"Tax Credits"** or **"Child Tax Credit"** section
5. The software typically shows a summary of CTC + ODC + ACTC computed automatically
6. **Verify** against the SKILL.md worksheet:
   - N_CTC and N_ODC match
   - Phase-out reduction matches
   - Non-refundable amount matches Form 1040 Line 19
   - ACTC matches Form 1040 Line 28
7. If the software's ACTC differs from the worksheet, **pause** and recompute. Most disagreements come from:
   - The software using a different earned income figure (it may include or exclude items the agent didn't)
   - The software using the alternative SS-tax method when the agent used earned income method (or vice versa)
   - The software handling MFS / Form 2120 / divorced-parents scenarios differently
8. Continue through Form 1040 review; software handles totals automatically
9. Pay software fee; e-file

**Provider-specific quirks**:
- TurboTax often asks "Do you have a custody agreement?" mid-flow for divorced parents — answer truthfully; tiebreaker rules (IRC §152(c)(4)) apply
- FreeTaxUSA puts the CTC review on a single screen with all credits
- H&R Block sometimes asks "Did anyone else claim this child?" — if yes, the user must coordinate with the other claimant before filing

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed after October 15, 2026, complex return, identity-theft concerns).

### Assemble the return

1. **Form 1040** (signed)
2. **Schedule 8812** (computes CTC + ODC + ACTC)
3. **Schedule 1, 2, 3** as applicable
4. **Schedule EIC** if EITC also claimed (separate computation but often relevant for the same children)
5. Other forms in attachment-sequence order

### Mailing

The IRS mailing address depends on filer's state, with-or-without payment, and tax year. Look up at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

### Mailing best practices

- USPS Certified Mail with Return Receipt (IRC §7502 timely-mailing rule)
- Postmark by April 15, 2026 for 2025 returns (or October 15, 2026 with an extension)
- Keep complete photocopy
- If ACTC is claimed, the IRS can't issue the refund before mid-February (PATH Act; 2025 Instructions for Schedule 8812, Reminders) — the user should expect delay

---

## Section 4 — Submission state machine

After filing (any channel):

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges receipt and basic validation
3. **Processed** — IRS has fully ingested the return
4. **Refund issued** OR **Balance due notice** OR **Audit/CP2000 notice**

For returns claiming ACTC:

- **PATH Act delay**: the IRS can't issue refunds before mid-February for returns claiming ACTC or EITC (Protecting Americans from Tax Hikes Act of 2015; the hold covers the entire refund).
- **Common audit trigger**: claiming a child also claimed by another taxpayer (e.g., divorced parents, custody dispute). The IRS applies tiebreaker rules under IRC §152(c)(4) — typically, the parent with whom the child lived longer wins; if equal, higher AGI wins.

Status checks:

- E-file: accepted or rejected within 24–48 hours
- Paper: no electronic acknowledgment; track the refund or the account transcript
- Refund tracking: https://www.irs.gov/refunds (Where's My Refund tool)
- Account transcript: https://www.irs.gov/individuals/get-transcript

---

## Security and consent rules

Non-negotiable:

1. **Never file without explicit user consent** at the moment of submission
2. **Never store SSN, DOB, PIN, or prior-year AGI** in agent logs or transcripts (this is especially sensitive for dependents — children's SSNs are common identity-theft targets)
3. **Never bypass identity verification or CAPTCHAs**
4. **Always capture submission confirmations** as screenshots stored under the user's account
5. **If anything looks wrong** (math disagreement, dependent SSN mismatch warning, MFA failures), **stop and surface the issue**. Don't retry blindly.
6. **Special for Schedule 8812**: if a dependent's SSN was issued after the due date, or the filer (and spouse) lack a valid SSN, the user must NOT claim CTC for that dependent (IRC §24(h)(7)). The agent should reclassify as ODC and document the reason. Filing CTC with a post-due-date SSN is a misstatement; a paid preparer faces the §6695(g) due-diligence penalty (CTC/ACTC/ODC, EITC, AOTC, HOH; Form 8867) and §6694 penalties.
