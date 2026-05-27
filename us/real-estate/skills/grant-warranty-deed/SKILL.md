---
name: grant-warranty-deed
title: Grant Deed / Warranty Deed
description: 'Drafts execution-ready Grant Deeds and Warranty Deeds for residential real property transfers, enforcing state-specific granting language, legal descriptions, covenant selection, and recording compliance. Use when preparing grant deeds, warranty deeds, property conveyances, title transfers, or real estate closing documents. Trigger keywords: grant deed, warranty deed, property conveyance, title transfer, deed of conveyance, real property transfer, recording deed.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/grant-warranty-deed
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Grant Deed / Warranty Deed

Draft a recordable deed transferring residential real property from grantor to grantee, compliant with applicable state recording statutes.

## Prerequisites

1. Deed type: Grant Deed (limited warranties) vs. Warranty Deed (full covenants through entire chain).
2. Current title report with vesting deed, legal description, encumbrances, and APN.
3. Full legal names for all parties matching title documents; entity formation docs and signing authority if applicable.
4. Transaction documents: purchase agreement, escrow instructions, consideration terms.
5. Jurisdiction confirmed: state-specific statutory language, witness/acknowledgment rules, recording standards.

## Output Structure / Process

**Document Header**

| Element | Requirement |
| --- | --- |
| Instrument type | "GRANT DEED" or "WARRANTY DEED" — must match operative language |
| Recording jurisdiction | County and state |
| Return address | For recorded document return |
| APN / Document ID | Per local recording statutes |
| Preparation date | Date of drafting |

**Parties**
- Grantors: full legal name as on vesting deed; marital status; signing capacity (individual, trustee, officer).
- Grantees: full legal name; manner of taking title (joint tenancy, tenancy in common, community property, etc.) with proportional interests if applicable.
- Entities: legal name, jurisdiction of formation, authorized representative and title.
- Mailing addresses for all parties.

**Consideration**
- State consideration (monetary or nominal: "Ten Dollars and other good and valuable consideration").
- Actual purchase price disclosure not required in most jurisdictions.
- Include recitals only where they provide necessary context; avoid creating ambiguity.

**Legal Property Description**
- Primary: lot/block from recorded plat, metes and bounds, or government survey — must match vesting deed exactly.
- Include APN and street address (street address for convenience only; never sufficient as sole description).
- Cross-check against title report and county records for gaps or overlaps.
- If lot line adjustment occurred, reference the recorded instrument.

**Granting Clause**

| Deed Type | Statutory Language | Effect |
| --- | --- | --- |
| Grant Deed | "grants and conveys" | Implies limited statutory warranties |
| Warranty Deed | "grants, bargains, sells, conveys, and warrants" | Invokes full covenants of title |

- Specify estate conveyed (typically fee simple absolute).
- Include any conditions or limitations on the grant.

**Covenants of Title**
- Warranty Deed — include or incorporate by reference: (1) seisin, (2) right to convey, (3) against encumbrances, (4) quiet enjoyment, (5) warranty, (6) further assurances. Specify scope: grantor's acts only vs. all prior holders. Confirm whether express or implied by statute in jurisdiction.
- Grant Deed — limited warranties only: no prior conveyance, no undisclosed encumbrances during grantor's ownership.

**Exceptions, Reservations & Encumbrances**
- Enumerate all exceptions: easements, CC&Rs, tax liens, utility easements.
- Reference recorded instruments by book/page or instrument number.
- Describe reservations (mineral rights, easements, life estates) with same specificity as property description.
- Distinguish permitted exceptions (grantee accepts) from encumbrances grantor warrants against.

**Execution & Acknowledgment**

| Requirement | Details |
| --- | --- |
| Signature blocks | All grantors; capacity specified |
| Execution date | May differ from effective date if held in escrow |
| Witnesses | Per state requirements (number, qualifications) |
| Spousal joinder | Required for homestead property in many states |
| Entity attestation | Secretary or authorized officer if required |
| Notarial acknowledgment | Statutory form; identify each grantor; notary signature, seal, commission expiration |
| Multi-party / out-of-state | Separate certificates if executed at different times/locations; comply with both notarizing and recording jurisdictions |

**Recording Format**
- Paper size per county recorder (letter or legal).
- Margins: 1" sides and bottom; 3" top on first page for recording stamp.
- Attach all referenced exhibits; include cover sheet if required by local practice.

## Guidelines

- Verify jurisdiction before drafting: deed formalities vary significantly by state.
- Party names, property descriptions, and citations must be uniform throughout.
- Never mix Grant Deed and Warranty Deed language — selection drives granting clause and covenant scope.
- Legal description accuracy is the most common cause of recording rejection; triple-check against title report.
- Do not improvise legal descriptions; use only verified descriptions from title documents or surveys.
- Use `[VERIFY]` for any statutory reference or citation not confirmed against current code.
- Final document should require only signatures and notarization before recording.
