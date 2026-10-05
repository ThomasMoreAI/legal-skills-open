# Filing Form 8300 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) can take a completed Form 8300 draft and actually file it through FinCEN's BSA E-Filing System. This file describes deterministic flows the agent can follow; it is complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, then execute the BSA E-Filing flow below. **Electronic filing has been mandatory since January 1, 2024** under 26 CFR §301.6011-2. Paper filing is permitted only for filers with an active hardship waiver from FinCEN.

---

## Channel decision tree

```
Has the user filed an 8300 before from this business?
  - Yes, account exists → Section 1 (BSA E-Filing — return user)
  - No, never filed → Section 2 (BSA E-Filing — first-time registration), then Section 1
  - Yes, but credentials lost → Section 3 (account recovery), then Section 1

Does the user have an active hardship waiver under 31 CFR §1010.306(e)?
  - Yes → Section 4 (paper filing fallback — only with waiver in hand)
  - No → e-filing is mandatory. Refer the user to register before filing.
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

| Form 8300 field | BSA E-Filing field label | Source (in draft) |
|-----------------|---------------------------|-------------------|
| Box 1a multiple parties | "Multiple parties" checkbox | Header |
| Box 1b suspicious | "Suspicious transaction" checkbox | Header |
| Amendment box | "Amends prior report" checkbox + prior tracking ID | Header |
| Part I — Last name | "Individual's last name" | Part I |
| Part I — First name | "Individual's first name" | Part I |
| Part I — M.I. | "Middle initial" | Part I |
| Part I — TIN | "Taxpayer Identification Number" | Part I |
| Part I — Address | "Address (number, street)" | Part I |
| Part I — City/state/ZIP | "City", "State", "ZIP" | Part I |
| Part I — Country (if non-US) | "Country" | Part I |
| Part I — DOB | "Date of birth" (MM/DD/YYYY) | Part I |
| Part I — Occupation | "Occupation, profession, or business" | Part I |
| Part I — ID type | "Document used to verify identity" radio/dropdown | Part I |
| Part I — ID number | "Identification document number" | Part I |
| Part I — Issuing authority | "Issued by" | Part I |
| Part II (if applicable) | "Person on whose behalf — [field]" — same as Part I | Part II |
| Part III — Line 27 | "Date cash received" | Part III |
| Part III — Line 28 | "Total cash received in U.S. dollars" | Part III |
| Part III — Line 29 | "Amount in $100 bills or higher denomination" | Part III |
| Part III — Line 30 | "Was this transaction conducted in more than one cash payment?" Yes/No | Part III |
| Part III — Line 31 | "Method of payment" — checkboxes for currency / foreign currency / cashier's check / money order / bank draft / traveler's check, with issuer + serial number sub-fields | Part III |
| Part III — Line 32 | "Type of transaction" radio | Part III |
| Part III — Line 33 | "Specific description of property or service" text | Part III |
| Part IV — Line 34 | "Business name" | Part IV |
| Part IV — Line 35 | "Employer Identification Number" | Part IV |
| Part IV — Line 36 | "Business address" | Part IV |
| Part IV — Line 37 | "Nature of business" | Part IV |
| Part IV — Line 38 | "Individual who handled the transaction" | Part IV |
| Part IV — Line 39 | "Title of individual" | Part IV |
| Part IV — Line 40 | "Date signed" — auto-populated to current date | Part IV |
| Part IV — Line 41 | "Phone" | Part IV |

   The agent fills each labeled field from the draft. After each field, capture a screenshot for the user's records. The user may want to verify visually before submission.

9. **Run the system's "Validate" or "Check Form" function.** BSA E-Filing flags missing required fields and basic format errors (e.g., TIN not 9 digits, DOB in the future). Resolve every flag before submission.

10. **Cross-check** the data on screen against the draft. If anything disagrees, **stop**; one of the two is wrong. Don't override blindly.

11. **Submit.** The submission button is typically labeled "Submit" or "File this report":
    - Confirm the submission dialog
    - The system may ask for the Supervisory User's PIN
    - Wait for the confirmation page

12. **Capture the BSA tracking ID** displayed on the confirmation page. Format: usually a long numeric string (e.g., `2026XXXXXXXXXXXX`). Save the screenshot AND the tracking ID separately.

13. **Download the submitted form** as PDF from the confirmation page. Save to the user's records folder. This is the audit-trail document.

14. **Schedule the customer notification follow-up** for January 31 of the year following filing — see [`references/customer-notification.md`](./references/customer-notification.md).

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
| "Date in the future" on Line 27 | Typo in transaction date | Re-confirm with user; the date is when cash was received, not today |
| Session timeout | Idle > 20 min on most BSA pages | Re-authenticate; system saves draft if you used "Save" before timeout |
| MFA / CAPTCHA | Routine | Pause for user input |
| "Duplicate report detected" | A prior filing with the same Part I + Line 27 already exists | This is an amendment — go back to step 7 and choose Amended |

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
- If both lost AND the email of record is also lost: contact the BSA E-Filing Help Desk at 1-866-346-9478 (verify number on the site each year)
- Recovery can take 1-3 business days; if the 15-day filing deadline is closer than that, surface the timing risk loudly

---

## Section 4 — Paper filing (waiver-only fallback)

Effective January 1, 2024, paper Form 8300 filing is permitted **only** for filers with an active hardship waiver under 31 CFR §1010.306(e). Without a waiver, a paper-only filing is itself a non-compliance event subject to penalty.

### When paper is allowed

The hardship waiver is granted by FinCEN on a per-filer basis when:

- The filer demonstrates lack of reliable internet access
- E-filing imposes undue hardship (e.g., a very small business with no electronic recordkeeping at all)
- The filer has applied via FinCEN's published waiver process and received written approval

The waiver is specific to a filing period and must be renewed.

### Paper filing flow (with waiver)

1. **Download** the latest Form 8300 PDF: https://www.irs.gov/pub/irs-pdf/f8300.pdf
2. **Print** at full size on letter paper, single-sided
3. **Fill** Parts I–IV by hand or via PDF form fields
4. **Sign** the bottom of Part IV
5. **Mail** to the IRS at:

```
Internal Revenue Service
Detroit Federal Building
P.O. Box 32621
Detroit, MI 48232
```

   Verify the address each year against the current Form 8300 instructions — the IRS occasionally updates filing addresses.

6. **Send via USPS Certified Mail with Return Receipt** for proof of timely filing under the IRC §7502 timely-mailing-as-timely-filing rule
7. **Postmark within 15 days** of the date cash was received (or threshold crossed)
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
   - FinCEN inquiry if Box 1b (suspicious) was checked or the report appears on a SAR-related lookup
   - Customer notification deadline (Jan 31) approaching → send the notification

Status checks:

- E-filing tracking ID: visible immediately on the confirmation page; also retrievable from the BSA E-Filing dashboard's "View History"
- Paper filing: no positive acknowledgment; the certified-mail return receipt is the only proof of filing

The agent should set a follow-up reminder for the customer notification due by January 31 of the year following filing.

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
