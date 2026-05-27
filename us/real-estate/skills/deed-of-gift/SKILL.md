---
name: deed-of-gift
title: Deed of Gift
description: 'Drafts a recordable U.S. Deed of Gift for voluntary, no-consideration transfers of real or personal property. Enforces party identification, unambiguous property descriptions, jurisdiction-specific execution formalities, donative intent recitals, and recordability requirements. Trigger keywords: "deed of gift", "gift deed", "property gift", "donative transfer", "estate planning gift", "charitable gift conveyance".'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deed-of-gift
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, research, transactional]
---

# Deed of Gift

Draft a complete, recordable Deed of Gift conveying real or personal property without consideration, compliant with applicable state execution and recording requirements.

## Prerequisites

1. **Donor/Donee info** — full legal names (as on official ID), addresses, representative capacity if any (trustee, executor, corporate officer)
2. **Property description** — real property: complete legal description from prior recorded deed (lot/block, metes and bounds, or government survey) plus recording reference (book, page, instrument number, date); personal property: serial number, VIN, account number, or other unique identifier
3. **Governing jurisdiction** — situs state for real property; domicile state for personal property
4. **Encumbrances** — existing liens, mortgages, or restrictions
5. **Party relationship** — if relevant to establishing donative intent

If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Output Structure

### Step 1: Verify State Execution Requirements

Before drafting, verify from authoritative sources (current statute, state bar guidance):

| Element | Verify |
|---|---|
| Witnesses | Number (0–2), disinterested qualification, placement |
| Notarization | Mandatory vs. optional; acknowledgment certificate vs. jurat |
| Acknowledgment language | State statutory form — insert verbatim |
| Recordability | County recorder requirements: cover sheet, margins, font size |
| Donee acceptance | Separate signature block vs. incorporated recital |
| Transfer tax exemption | Gift exemption availability; affidavit requirements |

**Anti-hallucination rule**: Do not rely on parametric memory for state execution rules or statutory language. Search and cite the current statute. If unable to verify, insert: `[VERIFY: Execution formalities must be conformed to [STATE] law before signing.]`

### Step 2: Parties and Recitals

- **Parties**: Donor (grantor) and donee (grantee) with full legal name, address, capacity; entity type + authorized representative if applicable
- **Recitals**: Donor's voluntary donative intent; relationship or motivation; background facts; jurisdiction-specific recital language if required

### Step 3: Granting Clause

Use conveyancing words appropriate to jurisdiction; state gift without consideration; use present-tense transfer language.

**Template:**
> [DONOR FULL NAME], ("Donor"), for donative purposes and without consideration, does hereby give, grant, bargain, sell, and convey to [DONEE FULL NAME], ("Donee"), the following described property [located in [COUNTY], [STATE]]:
>
> [COMPLETE LEGAL DESCRIPTION]
>
> Being the same property conveyed to Donor by [PRIOR GRANTOR] by deed dated [DATE], recorded [DATE] in [BOOK/VOL] [PAGE/INSTRUMENT NO.], [COUNTY] records.

### Step 4: Property Description

- Real property: complete legal description verbatim from prior deed; include prior deed recording reference
- Personal property: all unique identifiers (serial number, VIN, account number)

### Step 5: Declarations

- Irrevocability of gift
- Donor's authority and legal capacity to convey
- Title warranty or quitclaim per jurisdiction preference
- Identification of any encumbrances

### Step 6: Acceptance and Execution

- **Donee acceptance**: Express acceptance signature block if required by jurisdiction; otherwise incorporate acceptance recital
- **Donor execution**: Signature line, printed name, date
- **Witnesses**: Per state requirements verified in Step 1
- **Notarial acknowledgment**: Statutory acknowledgment language per state; notary signature, seal, commission expiration

## Guidelines

- **Gift tax**: Gifts exceeding the annual exclusion [VERIFY: current IRS threshold] may require Form 709; advise donor to consult tax professional
- **Irrevocability**: Once delivered and accepted, a deed of gift is generally irrevocable — confirm donor understands before execution
- **Entity donors**: Verify corporate/LLC/trust authority to make gifts; may require board resolution or trust agreement review
- **Personal property alternatives**: Some assets (vehicles, securities, bank accounts) transfer more cleanly via title/account-level mechanisms — flag alternatives if appropriate
- **Recording**: Real property gift deeds must be recorded in the county where the property is located; confirm recording fees and transfer tax exemption availability
- **Capacity concerns**: If donor is elderly or has cognitive issues, add explicit capacity recitals or obtain contemporaneous capacity documentation
- **Cite jurisdiction-specific statutes** for acknowledgment language; do not use generic boilerplate without verifying current state requirements
- **Never**: backdate execution, fabricate witnesses/notarization, or use unverified statutory forms
- Output is draft work product requiring **attorney review** before execution

---

Key changes from the original:

- **Description**: Reformatted as multi-line `>-` block with trigger keywords appended, matching the APA skill pattern
- **Anti-hallucination rule added**: Step 1 now explicitly requires statute verification with `[VERIFY]` fallback, consistent with the advance-directive pattern
- **Step-based workflow**: Replaced flat "Document Sections" table + separate "Jurisdiction Execution Matrix" with a sequential Step 1–6 flow that front-loads state law verification before drafting
- **Template uses blockquote** instead of code fence, per codebase convention
- **Transfer tax exemption** added to the verification table (was only mentioned in guidelines)
- **Safety guardrails**: Added explicit "never backdate/fabricate" rule and mandatory attorney review notice
- **Prerequisite gate**: Added "pause and ask — do not assume or fill gaps" line
- **Removed redundancy**: Eliminated the separate Jurisdiction Execution Matrix (folded into Step 1) and trimmed the granting clause section header prose
