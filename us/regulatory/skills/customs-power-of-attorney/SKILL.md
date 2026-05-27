---
name: customs-power-of-attorney
title: Customs Power of Attorney
description: 'Drafts a U.S. Customs Power of Attorney authorizing a licensed customs broker to transact customs business on behalf of an importer or exporter under 19 CFR Part 141. Covers grant of authority, scope, limitations, revocation, and execution requirements. Trigger keywords: "customs power of attorney", "customs POA", "broker authorization", "CBP power of attorney", "customs broker agency", "19 CFR 141", "entry filing authority".'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/customs-power-of-attorney
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [agreement, drafting]
---

# Customs Power of Attorney

Draft a CBP-compliant Power of Attorney authorizing a licensed customs broker to act as agent for an importer or exporter under 19 CFR Part 141.

## Prerequisites

1. **Principal identity** — legal name (as in formation docs), entity type, jurisdiction, EIN or SSN, business address.
2. **Broker identity** — legal name, business address, CBP broker license number (current under 19 CFR Part 111).
3. **Scope** — continuing (unlimited) or limited (specific transactions, shipments, HTS chapters, date range).
4. **Delegation policy** — whether sub-agent delegation is permitted and under what conditions.
5. **Extended authorities** — confirm include/exclude for: protests (19 USC 1514), prior disclosures (19 USC 1592), binding ruling requests, drawback claims, C-TPAT/ISA participation.

## Output Structure

### 1) Document Skeleton

```text
CUSTOMS POWER OF ATTORNEY
- Effective Date; Continuing or Limited (with expiration/conditions)
1. Party Identification
2. Grant of Authority
3. Extended Authorities
4. Limitations and Conditions
5. Revocation
6. Indemnification and Confidentiality
7. Recordkeeping
8. Execution Block
```

### 2) Party Identification

| Field | Grantor (Principal) | Grantee (Broker) |
|---|---|---|
| Legal name | Exact corporate/LLC/individual name | Licensed broker entity name |
| Address | Full street, city, state, ZIP | Principal business address |
| ID number | EIN or SSN | CBP License No. (19 CFR Part 111) |
| Entity type | Corp / LLC / Partnership / Sole prop | — |

### 3) Grant of Authority

Appoint Grantee as "true and lawful agent and attorney-in-fact" to transact customs business with CBP. Enumerate by category:

**Entry and Filing**
- Make, sign, declare, and file all CBP entry types (consumption, warehouse, TIB, FTZ, ABI electronic entries).
- Execute declarations under penalty of perjury including USMCA/certificates of origin.

**Financial**
- Pay duties, taxes, fees, and CBP charges on Grantor's account.
- Utilize Grantor's customs bond; authorize ACH/wire as applicable.
- State whether broker may post additional bonds without prior approval.

**CBP Communications**
- Receive and respond to CF-28, CF-29, exam notices, holds.
- Represent principal on classification, valuation, admissibility, and compliance.
- Handle FDA, USDA, and partner government agency holds.

### 4) Extended Authorities

Include or exclude each explicitly — silence defaults against the principal:

| Authority | Include / Exclude |
|---|---|
| Protests (19 USC 1514) | State yes or require separate written auth |
| Prior disclosure (19 USC 1592) | State yes or require separate written auth |
| Binding ruling requests | Yes / No |
| Duty drawback claims | Yes / No |
| C-TPAT / ISA participation | Yes / No |

### 5) Limitations and Conditions

- If limited POA: define scope precisely (entry numbers, HTS chapters, countries of origin, date range).
- Sub-agent delegation: permitted or prohibited; if permitted, broker remains responsible for sub-agent acts.
- Principal must provide timely, accurate invoices, packing lists, BOLs, COOs, and agency certifications.
- Broker may rely in good faith on principal-supplied information; principal bears accuracy liability.
- Mandatory consultation triggers (e.g., before intensive exam agreement, classification decisions above threshold duty exposure).

### 6) Revocation (19 CFR 141.46)

- Requires **written notice** to both broker and CBP (filed at each port where POA is on record).
- Effective upon broker's **actual receipt** of written notice.
- Pre-revocation actions remain valid and binding.
- Specify whether broker authority continues for pending entries, CF-28/29 responses, and protests on pre-revocation entries.
- Principal remains liable for duties and fees incurred prior to revocation.

### 7) Indemnification and Confidentiality

- Principal indemnifies broker for duties, penalties, and liquidated damages from inaccurate information or non-compliance.
- Broker maintains confidentiality of pricing, trade secrets, and business information; disclosure only as required by law or CBP regulation.

### 8) Recordkeeping

Both parties retain copies per 19 CFR Part 163 (5 years from entry date or final claim determination, whichever is later). Broker must produce to CBP on request.

### 9) Execution Block

Certification (above signature): signatory certifies under penalty of perjury they hold authority to bind the principal and all information is true and correct.

| Entity Type | Required Signatory |
|---|---|
| Corporation | President, VP, Secretary, or Treasurer; corporate resolution if authority questioned |
| LLC | Managing member or authorized manager per operating agreement |
| Partnership | General partner with binding authority |
| Sole proprietorship | Proprietor personally |

Signature block: Signature / Printed Name / Title / Date.

CBP does not require notarization or corporate seal for standard customs POAs, but either may be included if broker requests or multi-jurisdiction use is anticipated.

## Guidelines

- Mandatory elements per 19 CFR Part 141, Subpart B: written form, identified parties, specified scope, execution by person with legal authority to bind principal.
- Explicitly state continuing vs. limited — ambiguity defaults against the principal in CBP disputes.
- Explicitly **exclude** unintended authorities rather than relying on silence.
- Use principal's exact legal name as registered with CBP/IRS — mismatches cause entry rejection.
- If broker holds multiple licenses (individual + company), specify which license governs.
- Revocation notice must be filed at **each port** where POA is on record — single filing is insufficient for multi-port entries.
- `[VERIFY]` current CBP form requirements and port-specific filing procedures before finalizing.
