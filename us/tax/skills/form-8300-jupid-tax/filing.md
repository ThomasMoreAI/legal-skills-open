# Filing Form 8300 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) can take a completed Form 8300 draft and actually file it through FinCEN's BSA E-Filing System. This file describes deterministic flows the agent can follow; it is complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, then execute the BSA E-Filing flow below. **Since January 1, 2024, electronic filing is mandatory for a business required to file 10 or more information returns other than Form 8300 in the calendar year** (26 CFR §301.6011-2; Instructions for Form 8300, Rev. December 2023). A business under that threshold may file on paper (e-filing is optional and encouraged). A required e-filer may file on paper only with an IRS waiver granted on Form 8508 or under the religious exemption.

---

## Channel decision tree

```
How many information returns OTHER than Form 8300 (W-2, 1099 series, etc.)
must the business file this calendar year?
  - 10 or more → e-filing required, unless:
      - Form 8508 waiver granted for this year → Section 4 (paper, write "WAIVER")
      - religious exemption → Section 4 (paper, write "RELIGIOUS EXEMPTION")
  - Fewer than 10 → paper allowed (Section 4) or e-file voluntarily (below)
  - Unknown → ASK; do not pick a channel

E-filing:
  - Account exists → Section 1 (BSA E-Filing — returning filer)
  - Never filed → Section 2 (BSA E-Filing — first-time registration), then Section 1
  - Credentials lost → Section 3 (account recovery), then Section 1
```

---

## Section 1 — BSA E-Filing System (returning filer)

URL: https://bsaefiling.fincen.treas.gov/

**Availability:** the BSA E-Filing System is open year-round for Form 8300, unlike seasonal IRS filing channels.

**Account model:** one BSA E-Filing account per business. The Supervisory User (designated administrator) controls additional sub-users. Credentials persist across years; no re-registration each tax year.

### Pre-flight

The agent must have:

- The user's permission to log in and submit on their behalf
- BSA E-Filing username and password (Supervisory User or authorized sub-user)
- The completed Form 8300 draft from `SKILL.md`
- All buyer identification details (TIN, DOB, ID number) — the agent will input these but must NOT cache them
- Confirmation from the user that the buyer's ID has been photocopied or scanned for the 5-year retention requirement
- An IP address the user is willing to file from (BSA E-Filing logs submission IP)

### Browser flow

The agent navigates and interacts deterministically. Stable selectors are listed where known; treat label text as fallback when DOM IDs change.

1. **Navigate** to https://bsaefiling.fincen.treas.gov/
2. **Click** "Login" and submit the BSA E-Filing username and password
3. **Complete MFA** if prompted — pause for user input; do not bypass
4. **Land on the BSA E-Filing dashboard** — the main menu lists supported forms (CTR, SAR, Form 8300, FBAR-related forms)
5. **Click** "File a New Report" or the equivalent link for Form 8300
6. **Choose** "Form 8300 — Report of Cash Payments Over $10,000 Received in a Trade or Business"
7. **Select filing type:**
   - "Initial filing" for a new transaction
   - "Amended filing" if correcting a previously filed 8300 (will require the original BSA tracking ID)
8. **Fill the e-form** field-by-field from the draft:

   Item numbers are from Form 8300 (Rev. December 2023). E-form labels change; match on the item caption printed on the paper form and treat the e-form layout as the variable part.

| Form 8300 item | Caption on the form | Source (in draft) |
|-----------------|---------------------------|-------------------|
| 1a | Amends prior report (plus prior BSA ID on the e-form) | Item 1 |
| 1b | Suspicious transaction | Item 1 |
| 2 | More than one individual involved (adds Part I entries, up to 99 when e-filed) | Part I |
| 3–5 | Last name, first name, M.I. | Part I |
| 6 | Taxpayer identification number | Part I |
| 7 | Address (number, street, and apt. or suite no.) | Part I |
| 8 | Date of birth (MM/DD/YYYY) | Part I |
| 9–12 | City, state, ZIP code, country (if not U.S.) | Part I |
| 13 | Occupation, profession, or business (25 characters max when e-filed) | Part I |
| 14a–c | Identifying document: describe ID, issued by, number | Part I |
| 15 | Conducted on behalf of more than one person | Part II |
| 16–27 | Person on whose behalf: name, TIN, DBA/EIN, address, occupation, alien ID (item 27 only if no TIN required) | Part II |
| 28 | Date cash received | Part III |
| 29 | Total cash received | Part III |
| 30 | Cash received in more than one payment | Part III |
| 31 | Total price if different from item 29 | Part III |
| 32a–f | Amount of cash by form (U.S. currency with $100-bill amount, foreign currency with country, cashier's checks, money orders, bank drafts, traveler's checks) plus issuer names and serial numbers | Part III |
| 33 | Type of transaction (up to three of boxes a–j) | Part III |
| 34 | Specific description of property or service | Part III |
| 35 | Name of business that received cash | Part IV |
| 36 | Employer identification number (sole proprietor: also SSN) | Part IV |
| 37–40 | Address, city, state, ZIP code | Part IV |
| 41 | Nature of your business | Part IV |
| 42 | Signature, authorized official, title | Part IV |
| 43 | Date of signature | Part IV |
| 44–45 | Contact person name and telephone number | Part IV |
| Comments | Up to 720 characters; "LATE" here for a late e-filed report | Page 2 |

   The agent fills each field from the draft. After each field, capture a screenshot for the user's records. The user may want to verify visually before submission.

9. **Run the system's "Validate" or "Check Form" function.** BSA E-Filing flags missing required fields and basic format errors (e.g., TIN not 9 digits, DOB in the future). Resolve every flag before submission.

10. **Cross-check** the data on screen against the draft. If anything disagrees, **stop**; one of the two is wrong. Don't override blindly.

11. **Submit.** The submission button is typically labeled "Submit" or "File this report":
    - Confirm the submission dialog
    - The system may ask for the Supervisory User's PIN
    - Wait for the confirmation page

12. **Capture the BSA tracking ID** displayed on the confirmation page. Format: usually a long numeric string (e.g., `2026XXXXXXXXXXXX`). Save the screenshot AND the tracking ID separately.

13. **Download the submitted form** as PDF from the confirmation page. Save to the user's records folder. This is the audit-trail document.

14. **Schedule the customer statement follow-up** for January 31 of the year following the year the cash was received — see [`references/customer-notification.md`](./references/customer-notification.md).

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 11
- Do not bypass BSA E-Filing's validation (step 9) even if it looks like a false positive
- Do not store the buyer's SSN, DOB, ID number, or any Part I/II identification in agent logs, transcripts, or vector stores. Pull at filing time, use, discard.
- Do not email or text the completed Form 8300 with SSN visible. If transmission is needed, encrypt in transit (e.g., password-protected PDF over a separate channel) AND encrypt at rest.
- Do not file a duplicate — if a tracking ID already exists for this transaction, this is an amendment, not a new filing.

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Account not authorized for this form" | Sub-user lacks Form 8300 permission | Have Supervisory User grant permission |
| "Invalid TIN format" | TIN entered with dashes when system expects no dashes (or vice versa) | Strip/add dashes per the field's format hint |
| "Date in the future" on item 28 | Typo in transaction date | Re-confirm with user; the date is when cash was received, not today |
| Session timeout | Idle > 20 min on most BSA pages | Re-authenticate; system saves draft if you used "Save" before timeout |
| MFA / CAPTCHA | Routine | Pause for user input |
| "Duplicate report detected" | A prior filing with the same Part I + item 28 already exists | This is an amendment — go back to step 7 and choose Amended |

---

## Section 2 — BSA E-Filing System (first-time registration)

If the business has never filed an 8300 (or any BSA report) before, registration is a separate step that takes minutes to a few hours depending on FinCEN review.

URL: https://bsaefiling.fincen.treas.gov/

### Registration flow

1. **Navigate** to the BSA E-Filing System
2. **Click** "Become a BSA E-Filer" or "Register"
3. **Choose** "Individual" if filing as a sole proprietor; "Institution" if filing for an entity (LLC, corporation, partnership)
4. **Complete the registration form:**
   - Business legal name and EIN (or filer SSN for sole proprietor)
   - Business address
   - Supervisory User name, title, email, phone
   - Account credentials (username + password)
5. **Submit and verify the email address** — FinCEN sends a verification link
6. **Wait for FinCEN approval** — usually same-day for Individuals, may take longer for Institutions
7. **Once approved, log in and complete profile setup:**
   - Designate the Supervisory User formally
   - Add additional sub-users if multiple employees will file
   - Grant Form 8300 filing permissions
8. **Proceed to Section 1** (returning filer flow) for the actual filing

### Pre-flight for registration

- Business legal name, EIN, address
- Supervisory User identity (name, title, work email, phone)
- A monitored email address — FinCEN sends submission confirmations and security alerts here
- The user's authorization to register their business with FinCEN

The agent should NOT register a BSA E-Filing account without the business owner's explicit consent — registration creates a federal compliance obligation.

---

## Section 3 — Account recovery

If credentials were lost:

- "Forgot username" / "Forgot password" flows on https://bsaefiling.fincen.treas.gov/
- If both lost AND the email of record is also lost: contact the BSA E-Filing Help Desk at 1-866-346-9478 (option 1) or BSAEFilingHelp@fincen.gov, or open a help ticket at https://bsaefiling.fincen.gov/help-ticket (verify on fincen.gov each year)
- Recovery can take 1-3 business days; if the 15-day filing deadline is closer than that, surface the timing risk loudly

---

## Section 4 — Paper filing

### When paper is allowed

Per the Instructions for Form 8300 (Rev. December 2023):

- The business is required to file fewer than 10 information returns (of any type other than Form 8300) during the calendar year — no waiver needed; or
- The IRS granted an undue-hardship waiver on Form 8508 for the business's information returns for this calendar year (it covers Forms 8300 automatically; a waiver for Form 8300 alone cannot be requested). Write "WAIVER" at the center top of page 1; or
- Using the required technology conflicts with the filer's religious beliefs (automatic exemption). Write "RELIGIOUS EXEMPTION" at the center top of page 1.

A required e-filer that files on paper without a waiver or exemption has not filed in the required manner; the form is treated as late.

### Paper filing flow

1. **Download** the latest Form 8300 PDF: https://www.irs.gov/pub/irs-pdf/f8300.pdf
2. **Print** at full size on letter paper, single-sided
3. **Fill** Parts I–IV by hand or via PDF form fields
4. **Sign** item 42 (authorized official, title) and date item 43; write "LATE" at the center top of page 1 if the form is late, and "WAIVER" or "RELIGIOUS EXEMPTION" there if that is the basis for paper filing
5. **Mail** to the IRS at:

```
Internal Revenue Service
Detroit Federal Building
P.O. Box 32621
Detroit, MI 48232
```

   Verify the address each year against the current Form 8300 instructions — the IRS occasionally updates filing addresses.

6. **Send via USPS Certified Mail with Return Receipt** for proof of timely filing under the IRC §7502 timely-mailing-as-timely-filing rule
7. **Postmark by the 15th day** after the date cash was received (or threshold crossed); if that day is a Saturday, Sunday, or legal holiday, the next business day
8. **Keep a complete photocopy** of the filed form along with the certified-mail receipt

### Producing the printable PDF (deterministic)

If the agent has the latest Form 8300 fillable PDF, the deterministic flow is:

1. Download from https://www.irs.gov/pub/irs-pdf/f8300.pdf
2. Open in a PDF tool that supports form filling (`pypdf`, `pdftk`, etc.)
3. Map draft values to PDF field names
4. Save as flattened PDF for printing

---

## Section 5 — Submission state machine

After filing (any channel), the report moves through:

1. **Submitted** — sent to BSA E-Filing System (or postmarked for paper)
2. **Acknowledged** — BSA E-Filing returns a tracking ID; this confirms the system received the report
3. **Processed** — FinCEN and IRS have ingested the data
4. **Possible follow-ups:**
   - IRS audit referral if filing pattern raises questions
   - FinCEN inquiry if item 1b (suspicious) was checked or the report appears on a SAR-related lookup
   - Statement deadline (Jan 31 of the year after the cash was received) approaching → send the statement

Status checks:

- E-filing tracking ID: visible immediately on the confirmation page; also retrievable from the BSA E-Filing dashboard's "View History"
- Paper filing: no positive acknowledgment; the certified-mail return receipt is the only proof of filing

The agent should set a follow-up reminder for the customer statement due by January 31 of the year following the year the cash was received.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 8300 through BSA E-Filing on my behalf right now" must be captured.
2. **Never store buyer SSN, DOB, ID number, or other Part I/II identification** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard. The 8300 is a high-value identity-data document — treat it accordingly.
3. **Never email, text, Slack, or otherwise transmit the filled Form 8300 with SSN visible.** If sharing with the user is required, redact the SSN to the last 4 digits, OR use a password-protected PDF on a separate channel from the password.
4. **Never bypass BSA E-Filing's identity verification or MFA.** If the system asks for 2FA, pause and let the user authenticate directly.
5. **Always capture submission confirmations** (BSA tracking ID + screenshot) and store them under the user's account, not the agent's.
6. **If anything looks wrong** (validation error, unexpected screen, system rejection), **stop and surface the issue.** Don't retry blindly — repeated submission attempts can create duplicate-report flags.
7. **For paper filings, never claim "filed" until the certified-mail return receipt has been scanned back.** Until then, the filing is "in transit."
