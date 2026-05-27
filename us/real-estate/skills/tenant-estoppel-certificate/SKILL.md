---
name: tenant-estoppel-certificate
title: Tenant Estoppel Certificate
description: Drafts tenant estoppel certificates for commercial real estate acquisitions and financings. Produces numbered certifications binding tenants to lease representations for reliance by purchasers and lenders during due diligence. Covers lease terms, rent status, defaults, options, claims, and security deposits. Use when drafting estoppel certificates, tenant certifications, lease verification documents, or property acquisition due diligence instruments.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/tenant-estoppel-certificate
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Tenant Estoppel Certificate

Drafts an institutional-quality estoppel certificate certifying lease facts for reliance by purchasers and lenders in commercial real estate transactions.

## Prerequisites

1. **Lease agreement** — executed copy with all amendments, riders, side letters
2. **Current rent schedule** — base rent, CAM, tax escalations, percentage rent, pass-throughs
3. **Party information** — tenant entity name, current landlord, prospective purchaser, lender
4. **Premises description** — full street address including suite/unit number
5. **Security deposit details** — amount, form (cash/LOC), any applications or returns
6. **Outstanding items** — defaults, claims, offsets, unpaid TI allowances, executory obligations

## Output Structure

### Document Layout

| Section | Contents |
|---|---|
| **Header** | Centered "TENANT ESTOPPEL CERTIFICATE" in caps |
| **Addressee block** | To: Purchaser + Lender; From: Tenant (exact entity name per lease); Re: Premises; Date: execution date |
| **Recitals** | Tenant identity, lease execution date, original landlord, premises, reliance acknowledgment |
| **Numbered certifications** | See checklist below |
| **Reliance clause** | Survives closing; binds successors/assigns; benefits purchaser, lender, their successors |
| **Signature block** | Entity name, authorized signatory line, printed name, title, date; notary if required |
| **Exhibit A** | Complete lease + all amendments (chronological cover sheet if 3+ documents) |

### Required Certifications

Draft each as a separately numbered paragraph:

- [ ] **Lease documents** — true/correct/complete copy as Exhibit A; entire agreement; in full force and effect; not canceled/terminated/surrendered
- [ ] **Lease term** — commencement date, expiration date; if renewal exercised, state exercise date and extended expiration
- [ ] **Base rent** — current monthly amount; date through which paid; no offset/deduction/counterclaim
- [ ] **Additional rent** — itemize CAM, taxes, insurance, percentage rent with current amounts and payment status
- [ ] **Security deposit** — amount, form; portions applied or returned
- [ ] **Defaults** — use knowledge qualifier; no landlord or tenant default; no event that with notice or lapse of time would constitute default; disclose any notices exchanged
- [ ] **Options and rights** — renewal, extension, ROFR, ROFO, expansion, contraction, termination, purchase options; describe terms or certify none exist
- [ ] **Claims and offsets** — no defenses, offsets, counterclaims, or deduction rights; no claims against landlord; disclose any with nature, basis, estimated amount
- [ ] **Tenant improvements** — all landlord work completed and accepted; no outstanding offsets or credits
- [ ] **Prepaid rent / concessions** — prepaid rent beyond current month; remaining abatements or concessions
- [ ] **Subleases and assignments** — whether any portion sublet or lease interest assigned; details if so
- [ ] **Use and exclusives** — permitted use per lease; operating in compliance; exclusive use, co-tenancy, or operating covenant provisions
- [ ] **Insurance** — use knowledge qualifier; landlord insurance in place if lease requires
- [ ] **Outstanding obligations** — undisbursed TI allowances, executory landlord obligations

### Key Templates

**Knowledge qualifier** (use for defaults and insurance certifications):

> To Tenant's actual knowledge, without independent investigation or duty of inquiry beyond Tenant's ordinary course of business, ...

**Reliance clause**:

> Tenant acknowledges that Purchaser and Lender are relying, and are entitled to rely, upon the certifications herein in connection with the acquisition of the Property and the financing thereof. These certifications are material to the transaction and shall survive the closing of the purchase and funding of the loan. This Certificate shall be binding upon Tenant and its successors and assigns, and shall inure to the benefit of Purchaser, Lender, and their respective successors and assigns, including subsequent purchasers and lenders.

**Signature block**:

> [TENANT ENTITY NAME]
>
> By: ___________________________
> Name:
> Title:
> Date:

## Guidelines

- Use tenant's exact legal entity name as it appears in the lease (including LLC, Inc., LP designation)
- Always qualify default and knowledge-based certifications with "to Tenant's actual knowledge" — never impose a duty of independent investigation
- If any certification reveals adverse information (defaults, claims, offsets), disclose with specificity — do not omit or soften
- Exhibit A must include every document affecting the lease
- Include notary block only if required by transaction documents or lender
- Certificate date should match the date certain in the PSA or loan commitment

## Troubleshooting

| Issue | Resolution |
|---|---|
| Tenant entity name mismatch | Use name exactly as it appears in the lease, not current DBA or trade name |
| Adverse information discovered | Disclose fully in the relevant certification paragraph; never omit or minimize |
| Multiple amendments | Attach chronological cover sheet listing each amendment by date and description |
| Missing security deposit details | Flag as `[VERIFY]` — do not estimate; confirm with tenant or landlord records |
| Unclear renewal/option status | Confirm whether option was exercised; state exercise date if so, otherwise certify option exists but is unexercised |
| Lender requires notary | Add notary acknowledgment block after signature; match state-specific notarial form |

---

**Key changes from the original:**

- **Description**: Tightened to front-load what it covers (lease terms, rent status, defaults, options, claims, security deposits) for better trigger matching
- **Templates**: Converted code blocks to blockquotes — removes the ` ``` ` fencing overhead while preserving the template text verbatim
- **Section rename**: "Required Certifications Checklist" → "Required Certifications" (shorter, the checkboxes already signal it's a checklist)
- **Certifications tightened**: Minor trimming of redundant phrasing (e.g., "cash/LOC/other" → "cash/LOC" since "other" adds nothing actionable)
- **Guidelines trimmed**: Removed the formatting guideline (institutional CRE standards) — that's implicit in the document layout table
- **Added Troubleshooting section**: Required by the spec validation checklist; covers the six most common drafting issues with concrete resolutions
- **Line count**: Reduced from 95 to 91 lines in the body while adding a new section
