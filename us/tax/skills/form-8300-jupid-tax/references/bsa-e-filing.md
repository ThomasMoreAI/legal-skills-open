# FinCEN BSA E-Filing System

Form 8300 has been required to be filed electronically through FinCEN's BSA E-Filing System since **January 1, 2024**, under the broader information-return e-filing mandate at 26 CFR §301.6011-2. This reference covers what the system is, how an account is structured, and what to expect when filing.

## What is the BSA E-Filing System?

URL: https://bsaefiling.fincen.treas.gov/

The BSA E-Filing System is FinCEN's free secure portal for filing Bank Secrecy Act reports — the same channel used for SARs (Suspicious Activity Reports), CTRs (Currency Transaction Reports), FBARs (Reports of Foreign Bank and Financial Accounts), and Form 8300. The system has been operational since 2002 for banks; Form 8300 was added in 2012, when IRS and FinCEN consolidated the joint reporting onto a single submission.

The portal accepts:

- Discrete e-filing (one form at a time, web UI) — what most 8300 filers use
- Batch filing (XML upload) — used by high-volume filers like large dealerships

For Form 8300, the discrete web UI is sufficient unless the business files dozens of reports per year.

## Why e-filing is mandatory

26 CFR §301.6011-2, as amended in February 2023, lowered the threshold for mandatory e-filing of information returns from 250 returns to **10 returns** in aggregate across all information-return types. For Form 8300 specifically, the IRS clarified that the 10-return aggregate threshold applies, AND that a separate FinCEN regulation effectively makes e-filing mandatory for nearly all 8300 filers regardless of count.

In practice: unless the business has an active hardship waiver, paper Form 8300 is non-compliant.

## Account structure

### Account types

| Account type | Used by | Notes |
|--------------|---------|-------|
| Individual | Sole proprietors, single-member LLCs filing as themselves | Filer's SSN ties to the account |
| Institution | Multi-member LLCs, S-corps, C-corps, partnerships, large enterprises | Filer's EIN ties to the account |

For most small businesses filing Form 8300, "Institution" with the business EIN is the right choice even if there is only one owner.

### Roles

| Role | Permissions | Typical assignee |
|------|-------------|-------------------|
| Supervisory User | Manages the account, adds/removes sub-users, files all forms | Business owner, principal, or compliance officer |
| Sub-User | Files specific forms based on permissions granted by Supervisory User | Employees who handle cash transactions |
| Read-Only | Views past submissions, no filing rights | Bookkeepers, CPAs |

For a small business, the owner registers as Supervisory User and either files personally or grants 8300 filing rights to one trusted employee.

## Registration

### What's needed

- Business legal name and EIN (or filer SSN for sole proprietors)
- Business address
- Supervisory User name, work email, phone
- A monitored email — FinCEN sends submission confirmations and security alerts here
- The user's authorization (registration creates a federal compliance record)

### How long it takes

- "Individual" accounts: usually approved same day
- "Institution" accounts: minutes to a few hours; occasionally up to 2 business days for FinCEN review

### Steps

1. Navigate to https://bsaefiling.fincen.treas.gov/
2. Click "Become a BSA E-Filer" / "Register"
3. Choose Individual or Institution
4. Complete the form (legal name, EIN, address, contact, credentials)
5. Verify the email address via the link FinCEN sends
6. Wait for approval notification
7. Once approved, log in and configure sub-users (if any) and form permissions

The agent should NOT register an account on behalf of the user without explicit consent.

## BSA tracking IDs

When a Form 8300 is successfully submitted, BSA E-Filing returns a **BSA Tracking ID** on the confirmation page. Format: typically a long numeric string (e.g., `2026XXXXXXXXXXXXX`).

The tracking ID is the canonical record of the filing. It is required when:

- Amending the report (the amendment references the original tracking ID)
- Responding to an IRS or FinCEN inquiry about the filing
- Demonstrating timely filing in case of audit

**Save the tracking ID immediately.** Best practice: capture both a screenshot of the confirmation page AND the tracking ID copied to a separate note. Store with the 8300 PDF download in the customer's file.

## Submission states

| State | What it means | Typical timing |
|-------|---------------|-----------------|
| Draft | In progress, not submitted | Indefinite — saved on FinCEN servers |
| Submitted | Sent to BSA E-Filing System | Real-time |
| Acknowledged | Tracking ID issued, system has accepted format | Seconds after submission |
| Processed | FinCEN/IRS data ingestion complete | Hours to days |

The Acknowledged state is the legally relevant moment — once the tracking ID is issued, the filing is "filed" for §6050I purposes. Subsequent processing delays don't change the filing date.

## Amendments and corrections

If a filed Form 8300 contains an error, file an amendment:

1. Log into BSA E-Filing
2. Choose "File a New Report" → Form 8300 → "Amends a prior report"
3. Enter the **prior BSA tracking ID** in the amendment field
4. Re-fill all parts with the corrected data (the amendment fully replaces the prior filing for that transaction)
5. Submit; capture the new tracking ID

Amendments do not extend the original 15-day deadline. The original timely filing still controls; an amendment is just a correction.

## Hardship waiver path

Under 31 CFR §1010.306(e), FinCEN can grant a hardship waiver to a filer who can demonstrate that e-filing imposes undue hardship — typically due to lack of reliable internet, very small operation with no electronic recordkeeping, or comparable circumstances.

Process:

1. Submit a written waiver request to FinCEN before the filing deadline
2. Include: filer identification, basis for hardship, period requested
3. Wait for FinCEN approval (timing varies, usually weeks)
4. With an approved waiver, paper filing is permitted to:

   ```
   Internal Revenue Service
   Detroit Federal Building
   P.O. Box 32621
   Detroit, MI 48232
   ```

   (Verify the address each year against the current Form 8300 instructions.)

A waiver is specific to a filer and a period; it must be renewed.

## Common system issues

| Issue | Cause | Workaround |
|-------|-------|------------|
| "Form not yet supported" | Annual system maintenance window (rare for 8300) | Wait; contact Help Desk |
| "Account locked" | Multiple failed login attempts | Wait 30 minutes or use account recovery |
| "Session expired" | Idle > 20 min on most pages | Re-authenticate; saved drafts persist |
| Browser compatibility | Older browsers (legacy IE, very old Safari) | Use a current Chrome, Firefox, or Edge |
| MFA not received | Email or SMS delay | Use the resend option; check spam folder |

## Help Desk

BSA E-Filing Help Desk: 1-866-346-9478 (verify on the site each year). Hours typically 8 AM – 6 PM Eastern, Monday–Friday. The Help Desk handles registration issues, login recovery, and technical questions. They do NOT provide tax or legal advice — content questions go to a CPA or attorney.

## Security best practices

- Use a unique, strong password for the BSA E-Filing account; do not reuse from other systems
- Enable MFA if offered
- Limit Supervisory User access to one or two trusted individuals
- Audit sub-user activity periodically — the Supervisory User can view all filings made under the account
- Never share login credentials over email or chat; rotate if a sub-user leaves
- Treat the BSA E-Filing portal as a federal information system — same caution as IRS or e-Verify

## Record retention

Independent of BSA E-Filing's own retention, the business must retain its own copies of every filed Form 8300 for **5 years from the date of filing**. The BSA tracking ID, the PDF copy, and supporting documents (ID copies, bill of sale) constitute the audit-defense package.
