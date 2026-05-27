---
name: pour-over-will
title: Pour-Over Will
description: 'Drafts a pour-over will directing the testator''s residuary estate into an existing revocable living trust. Covers fiduciary appointments, guardianship, debt/tax payment, specific bequests, the central pour-over clause, and execution formalities with self-proving affidavit. Use when drafting pour-over wills, testamentary trust transfers, estate planning safety nets, or residuary estate instruments. Trigger keywords: pour-over will, residuary estate, revocable trust, testamentary transfer, UTATA, personal representative, guardian nomination, self-proving affidavit.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/pour-over-will
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [agreement, drafting, transactional]
---

# Pour-Over Will

Drafts a pour-over will transferring the testator's residuary estate to an existing revocable living trust, ensuring unified distribution for assets not titled in the trust at death.

## Checkpoint A: Pre-Draft Intake

Gather before drafting. If user says "use defaults," apply bracketed defaults and note them.

| Item | Details |
|---|---|
| Testator | Full legal name (as on ID), city/state of domicile |
| Trust | Exact legal name, date of trust agreement, settlor/grantor name |
| Personal Representative | Full name, relationship; successor(s) if primary unable/unwilling |
| Guardian of Person | Full name, address, relationship (minor children only) |
| Guardian of Estate | Same or separate from guardian of person; note reasoning if split |
| Specific bequests | Property descriptions, beneficiary names (if any) |
| Governing law | State of domicile: execution requirements, witness count, self-proving affidavit statute, pour-over statute |

## Output Structure

### Article I — Declaration

| Element | Requirement |
|---|---|
| Testamentary intent | Explicit "Last Will and Testament" declaration |
| Revocation | Revoke all prior wills and codicils |
| Domicile | City and state of residence |
| Capacity | Sound mind, legal age, voluntary, no undue influence |

### Article II — Fiduciary Appointments

| Role | Include |
|---|---|
| Personal Representative | Full name, relationship; successor(s) |
| Guardian of Person | Full name, address, relationship (minor children only) |
| Guardian of Estate | Same or separate individual; state reasoning if split |
| Powers | Broad administration without court supervision (if state permits) |
| Bond | Waiver provision for all nominated fiduciaries |

### Article III — Debts and Expenses

- [ ] Legally enforceable debts
- [ ] Funeral and burial expenses
- [ ] Costs of administration
- [ ] Estate taxes — apportioned among beneficiaries OR paid from residuary
- [ ] Secured debts — beneficiary takes subject to encumbrance OR estate pays off
- [ ] Priority of payments
- [ ] PR discretion to contest or compromise claims

### Article IV — Specific Bequests and Tangible Property

- Draft specific bequests before residuary pour-over
- Reference separate written statement/list if state law permits (UPC § 2-513 or equivalent) [VERIFY]
- Address **ademption** (property no longer in estate), **lapse** (beneficiary predeceases testator), and **anti-lapse statute** applicability

### Article V — Pour-Over of Residuary Estate

Core clause template:

```text
I give, devise, and bequeath all the rest, residue, and remainder of my estate,
whether real, personal, or mixed, wherever situated, to the then-acting Trustee
of the [TRUST NAME], dated [TRUST DATE], established by [SETTLOR NAME],
as amended from time to time, to be held, administered, and distributed
in accordance with the terms of said trust and not as a testamentary trust.
```

| Issue | Required Language |
|---|---|
| Trust amendments | "as amended from time to time" — recognizes post-execution amendments |
| Trust revocation/invalidity | Contingent residuary beneficiary or alternative distribution scheme |
| Statutory compliance | Conform to UTATA or state equivalent [VERIFY] |
| Trust existence | Confirm trust in existence at will execution (required in most jurisdictions) |

### Article VI — Execution and Attestation

| Requirement | Detail |
|---|---|
| Witnesses | Minimum per state law (typically 2; some states require 3) |
| Attestation clause | Witnesses confirm: (1) observed signing, (2) testator declared it as will, (3) appeared of sound mind, (4) no undue influence, (5) signed in presence of testator and each other |
| Self-proving affidavit | Include if state permits; requires notarization; cite applicable statute [VERIFY] |
| Signature lines | Testator + all witnesses: printed name, address, date |
| Page numbering | "Page ___ of ___" on each page |

## Checkpoint B: Post-Draft Alignment

After delivering draft, confirm:

1. Are fiduciary appointments and succession order correct?
2. Is the trust correctly identified by name, date, and settlor?
3. Does the tax apportionment clause reflect the testator's intent?
4. Are execution formalities (witness count, self-proving affidavit) correct for the domicile state?

## Quality Audit

- [ ] "As amended from time to time" included in pour-over clause
- [ ] Contingent beneficiary if trust is revoked or invalid
- [ ] UTATA or state pour-over statute compliance verified [VERIFY]
- [ ] Trust confirmed in existence at will execution
- [ ] No substantive trust distribution terms in the will
- [ ] Tax apportionment explicitly stated (not relying on state default)
- [ ] Execution formalities match domicile state requirements
- [ ] Self-proving affidavit cites correct statute [VERIFY]
- [ ] All bracketed terms filled or flagged for attorney review
- [ ] Separate tangible property list referenced only if state permits incorporation by reference [VERIFY]

## Guidelines

- **Domicile controls** — verify all provisions against the domicile state's probate code
- **"As amended" language is critical** — without it, only original trust terms apply; most states honor this under UTATA
- **Pour-over assets pass through probate** — this is a safety net, not a probate-avoidance tool
- **No trust terms in the will** — distribution governed by the trust instrument exclusively
- **Tax apportionment** — default state rules vary; always specify intent explicitly
- **Placeholders** — use `[BRACKETED CAPS]` for all client-specific information
- All outputs require attorney review before execution
