---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Transfer Document Preparer

Builds a complete closing document checklist, outlines each required transfer document, researches jurisdiction-specific requirements, and coordinates execution logistics for a seamless CRE acquisition closing.

---

## When to Use This Skill

Use this skill when you are approaching closing on a commercial real estate acquisition and need to prepare, track, and organize all transfer documents. It is appropriate when you need to determine which documents are required, outline their content, identify jurisdiction-specific recording and tax requirements, and manage the signing and delivery workflow through closing.

---

## What You'll Need to Provide

- Property address, county, and state (for jurisdiction research)
- Buyer entity name, type (LLC, LP, corporation), and state of formation
- Seller entity name, type, and state of formation
- Deal structure: direct property purchase vs. entity interest purchase
- Financing type (conventional bank, agency, CMBS, bridge, all-cash) — affects lender closing document requirements
- The PSA: deed type specified, assignment of contracts provisions, FIRPTA obligations, personal property included
- Number of parcels and approximate unit count (affects tenant notification scope)
- Any lease or contract summaries from due diligence (for assignment schedules)
- The title commitment Schedule B-I requirements (to cross-reference with document checklist)
- Target closing date

---

## Mission

Prepare all closing and transfer documents for the acquisition. Ensure all documents are complete, properly drafted, and compliant with jurisdiction requirements. Track document status from drafting through execution and delivery, and coordinate signing logistics for a seamless closing.

---

## Strategy

### Step 1: Prepare Document Checklist
- Build a customized document checklist based on:
  - Property type and jurisdiction
  - Deal structure (direct purchase vs. entity purchase)
  - Financing type (conventional, agency, CMBS, bridge)
  - Number of parcels
  - Tenant count (affects tenant notification scope)
  - PSA-specific requirements
- Assign each document a tracking status: `not started` | `drafted` | `under review` | `revised` | `approved` | `executed` | `delivered`

### Step 2: Outline Each Required Document

**Deed:**
- Type per PSA: Warranty Deed, Special Warranty Deed, Quitclaim Deed, Bargain and Sale Deed
- Content: Grantor, grantee, legal description, consideration, exceptions (if any)
- Jurisdiction requirements: format, margins, font size, recording language
- Tax stamps / documentary stamps language (if required on deed)

**Bill of Sale:**
- Personal property conveyed: furniture, appliances, equipment, maintenance supplies
- Warranty of title to personal property
- "As-is" qualification per PSA
- Schedule of personal property items

**Assignment and Assumption of Leases:**
- Assignment of all tenant leases from seller to buyer
- Assumption of landlord obligations under leases from and after closing
- Indemnification: seller for pre-closing obligations, buyer for post-closing
- Schedule of assigned leases (unit, tenant, lease date, term)

**Assignment of Contracts:**
- Service contracts being assumed (per PSA / due diligence review)
- Contracts being terminated at closing (not assumed)
- Assumption of obligations from closing date forward
- Schedule of assumed contracts with vendor, scope, term, monthly cost

**Assignment of Permits and Licenses:**
- Transfer of transferable permits (CO, business license, elevator, pool, etc.)
- Identification of non-transferable permits requiring new applications
- Governmental approvals needed for transfer

**Tenant Notification Letters:**
- New owner/management notice per state law requirements
- Content: new owner entity, new management company, new rent payment address, security deposit transfer notice
- State-specific requirements (timing, content, delivery method)
- Template for each unit (personalized with tenant name, unit number)

**FIRPTA Certificate:**
- Seller's certification of non-foreign person status (IRC Section 1445)
- Seller's TIN and entity information
- Penalties for false certification
- Withholding requirements if seller is a foreign person

**Transfer Tax Declaration:**
- State/county specific transfer tax form
- Consideration amount (may differ from purchase price if personal property allocated)
- Exemptions claimed (if any)
- Signatures required (buyer, seller, or both depending on jurisdiction)

**Entity Documents:**
- **Certificate of Good Standing**: Current (within 30 days) for buyer and seller entities from state of formation and state where property is located (foreign qualification)
- **Authorization Resolution**: Board/member/manager resolution authorizing the transaction, identifying authorized signers
- **Incumbency Certificate**: Certifying identity and authority of persons signing on behalf of entity
- **Operating Agreement / Bylaws**: Excerpts showing signing authority
- **Formation Documents**: Articles/Certificate of Organization or Incorporation (if required by title company)

### Step 3: Track Document Status
Build and maintain a document status tracker:

| Document | Responsible Party | Draft Date | Review Date | Approval Date | Execution Date | Delivery Date | Status |
|----------|-------------------|------------|-------------|---------------|----------------|---------------|--------|
| {doc} | {party} | {date} | {date} | {date} | {date} | {date} | {status} |

Update status as documents progress through the workflow.

### Step 4: Identify Jurisdiction-Specific Requirements
Research and document:
- **Recording Requirements**: Document format (paper size, margins, font), recording fees per page/document, e-recording availability
- **Transfer Taxes**: State transfer tax rate, county transfer tax rate (if applicable), city transfer tax (if applicable), exemptions available, who pays (buyer/seller/split per PSA)
- **Disclosure Requirements**: Seller disclosures required by state (property condition, lead paint, mold, environmental)
- **Notarization Requirements**: Which documents require notarization, notary format (jurat vs. acknowledgment), remote online notarization permitted
- **Witness Requirements**: Which documents require witnesses, number of witnesses required
- **State-Specific Forms**: Mandatory state forms (e.g., TP-584 in New York, PCOR in California)

### Step 5: Coordinate Execution Logistics
- **Signing Authority**: Confirm authorized signers for each entity; verify authority matches resolutions
- **Notarization**: Identify all documents requiring notarization; coordinate notary availability; determine if RON (remote online notarization) is permitted and preferred
- **Witnesses**: Identify witness requirements; arrange witnesses for signing
- **Counterparts**: Determine if documents can be signed in counterparts
- **Electronic Signatures**: Determine which documents accept e-signatures vs. wet signatures (deeds typically require wet signatures)
- **Signing Schedule**: Build timeline for pre-signing, signing day, and post-closing deliveries
- **Power of Attorney**: If any signer unavailable, prepare POA with specific authority

---

## Output Format

```json
{
  "transfer_document_package": {
    "metadata": {
      "preparation_date": "{date}",
      "property": "{property name/address}",
      "jurisdiction": "{county, state}",
      "closing_date": "{date}"
    },
    "document_checklist": {
      "total_documents": "{N}",
      "completed": "{N}",
      "in_progress": "{N}",
      "not_started": "{N}",
      "documents": [
        {
          "document": "{name}",
          "type": "conveyance / assignment / notice / entity / tax / lender",
          "responsible_party": "buyer / seller / buyer's counsel / seller's counsel / title company",
          "status": "not started / drafted / under review / revised / approved / executed / delivered",
          "draft_date": "{date or pending}",
          "target_date": "{date}",
          "requires_notarization": "yes/no",
          "requires_witnesses": "yes/no",
          "requires_recording": "yes/no",
          "notes": "{additional details}"
        }
      ]
    },
    "document_outlines": {
      "deed": {
        "type": "{warranty / special warranty / quitclaim / bargain and sale}",
        "grantor": "{seller entity}",
        "grantee": "{buyer entity}",
        "legal_description_source": "title commitment / survey",
        "consideration": "{amount}",
        "exceptions": "{list or none}",
        "jurisdiction_format": "{requirements}"
      },
      "bill_of_sale": {
        "personal_property_schedule": "{attached / to be prepared}",
        "warranty_type": "{with warranty / as-is}",
        "estimated_pp_value": "{amount}"
      },
      "lease_assignment": {
        "total_leases_assigned": "{N}",
        "lease_schedule_status": "prepared / pending",
        "indemnification_structure": "{description}"
      },
      "contract_assignment": {
        "contracts_assumed": "{N}",
        "contracts_terminated": "{N}",
        "contract_schedule_status": "prepared / pending"
      },
      "tenant_notifications": {
        "total_notices": "{N}",
        "state_requirements": "{description}",
        "delivery_method": "{mail type / hand delivery}",
        "template_status": "drafted / approved"
      },
      "firpta_certificate": {
        "seller_type": "US person / foreign person",
        "withholding_required": "yes/no",
        "certificate_status": "drafted / executed"
      },
      "transfer_tax_declaration": {
        "state_form": "{form number/name}",
        "consideration_amount": "{amount}",
        "tax_rate": "{rate}",
        "estimated_tax": "{amount}",
        "payor": "buyer / seller / split"
      },
      "entity_documents": {
        "buyer_good_standing": "ordered / received / current",
        "seller_good_standing": "ordered / received / current",
        "buyer_resolution": "drafted / executed",
        "seller_resolution": "drafted / executed",
        "buyer_incumbency": "drafted / executed",
        "seller_incumbency": "drafted / executed"
      }
    },
    "jurisdiction_requirements": {
      "recording": {
        "format_requirements": "{description}",
        "recording_fee_per_page": "{amount}",
        "recording_fee_per_document": "{amount}",
        "e_recording_available": "yes/no",
        "estimated_total_recording_fees": "{amount}"
      },
      "transfer_taxes": {
        "state_rate": "{rate}",
        "county_rate": "{rate or N/A}",
        "city_rate": "{rate or N/A}",
        "total_rate": "{combined rate}",
        "estimated_transfer_tax": "{amount}",
        "payor": "buyer / seller / split ({X%}/{Y%})",
        "exemptions_available": "{description or none}"
      },
      "disclosures": {
        "required_disclosures": [
          {
            "disclosure": "{name}",
            "responsible_party": "seller",
            "status": "received / pending / N/A"
          }
        ]
      },
      "notarization": {
        "documents_requiring_notarization": [
          "{document name}"
        ],
        "notary_format": "jurat / acknowledgment",
        "ron_permitted": "yes/no"
      },
      "state_specific_forms": [
        {
          "form": "{name/number}",
          "purpose": "{description}",
          "status": "prepared / pending"
        }
      ]
    },
    "execution_logistics": {
      "signing_schedule": {
        "pre_signing_date": "{date}",
        "signing_date": "{date}",
        "post_closing_delivery_date": "{date}"
      },
      "authorized_signers": {
        "buyer": "{name(s) and title(s)}",
        "seller": "{name(s) and title(s)}"
      },
      "notary_arrangements": "{description}",
      "e_signature_permitted": [
        {
          "document": "{name}",
          "e_sig_ok": "yes/no"
        }
      ],
      "power_of_attorney": "needed / not needed",
      "counterparts_permitted": "yes/no"
    },
    "outstanding_items": [
      {
        "item": "{description}",
        "responsible_party": "{party}",
        "deadline": "{date}",
        "priority": "critical / important / routine",
        "blocking_closing": "yes/no"
      }
    ],
    "estimated_costs": {
      "recording_fees": "{amount}",
      "transfer_taxes": "{amount}",
      "notary_fees": "{amount}",
      "total_transfer_costs": "{amount}"
    },
    "risk_flags": [
      {
        "flag": "{description}",
        "severity": "low / medium / high / critical",
        "recommendation": "{action}"
      }
    ],
    "uncertainty_flags": [
      {
        "field_name": "",
        "reason": "estimated | assumed | unverified | stale_data | interpolated",
        "impact": "Description of what downstream analysis this affects"
      }
    ]
  }
}
```

---

## Quality Checks

Before finalizing output, verify:

1. **Schema Compliance** — All required output fields are present, non-null, and correctly typed
2. **Numeric Sanity** — Transfer tax calculations, recording fees, and cost totals are arithmetically correct and positive
3. **Cross-Reference Validation** — Grantor name matches seller entity; grantee name matches buyer entity; property address and jurisdiction match details provided
4. **Completeness Assessment** — Every strategy step produced output or a noted data gap
5. **Confidence Scoring** — Set `confidence_level` and populate `uncertainty_flags` for any estimated or assumed values

**Self-Validation field checks:**

| Field | Valid Range | Flag If |
|-------|-----------|---------|
| documentsRequired | At least: deed, bill of sale, assignment of leases | Missing critical documents |
| entityDocsStatus | Each entity must have good standing ordered/received | Missing good standing |
| firptaCompliance | Must be addressed | Not addressed |
| grantorName | Must match seller entity | Mismatch |
| granteeName | Must match buyer entity | Mismatch |

**Validation checks:**

| Check | Method |
|-------|--------|
| All required docs on checklist | Compare against standard CRE closing document list for the deal type |
| All docs have responsible party | No document missing assignment |
| All docs have target date | No document missing deadline |
| Jurisdiction research complete | Recording, taxes, notarization, disclosures all addressed |
| Transfer tax calculated | Rate applied correctly to consideration |
| Recording fees estimated | Per-page/per-document fees applied to all recorded docs |
| Entity docs current | Good standing certificates within 30 days of closing |
| Signing authority confirmed | Authorized signers match entity resolutions |
| Outstanding items actionable | Every item has party, deadline, and priority |

---

## Red Flags & Dealbreakers

Treat the following as CRITICAL findings requiring immediate escalation:

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| Dissolved entity ownership | Entity documents reveal seller entity is dissolved, revoked, or not in good standing |

If a dealbreaker is detected: set severity to "CRITICAL", add to `risk_flags` with category "dealbreaker", note it prominently in the report, and continue tracking all other documents.

Additional high-severity flags:
- Seller entity has no authority to convey (missing or invalid authorization resolution)
- FIRPTA withholding required but buyer unprepared to withhold (creates IRS liability for buyer)
- Deed type specified in PSA is not available or customary in the jurisdiction
- Recording deadline conflicts with closing date (e.g., recorder closed on closing day)
- State-specific mandatory forms not identified until late in the process

---

## When Data is Missing

When entity documents, jurisdiction requirements, or PSA terms are incomplete:

1. **Attempt a workaround** — Research jurisdiction requirements from county recorder/assessor websites, state department of revenue, or state bar association resources; use standard form checklists for the deal type
2. **Note the assumption** — Document any assumed document requirement or transfer tax rate, including its source
3. **Mark in output** — Add an entry to `uncertainty_flags` with the field name, reason, and impact on the closing timeline
4. **Continue analysis** — Do not halt for missing individual document details; complete the checklist and flag missing items as outstanding
5. **Flag for attorney review** — Jurisdiction-specific requirements and entity authority questions should be reviewed by qualified local counsel

---

## Confidence Scoring

Apply confidence levels to all findings:

| Level | Criteria |
|-------|----------|
| **HIGH** | Based on verified entity documents, confirmed jurisdiction requirements, and PSA text; no assumptions |
| **MEDIUM** | Based on available entity summaries and researched jurisdiction requirements; minor assumptions made |
| **LOW** | Based on general assumptions about deal structure or jurisdiction; entity documents not yet reviewed |

Set `confidence_level` in the output and populate `uncertainty_flags` for any finding rated MEDIUM or LOW.

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- [Legal Checklist](knowledge/legal-checklist.md) for the master CRE closing document checklist and standard document requirements by deal type
- [CRE Risk Scoring Framework](knowledge/risk-scoring.md) for severity rating guidance on missing documents and entity authority issues
- [Lender Criteria](knowledge/lender-criteria.md) for lender-specific closing document requirements and delivery timelines

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
