---
name: esi-protocol
title: ESI Protocol
description: Drafts stipulated ESI protocols for federal e-discovery. Produces court-ready agreements governing preservation, collection, processing, review, and production of electronically stored information under FRCP Rules 26, 34, 37 and Sedona Principles. Trigger when formalizing ESI procedures between parties during the discovery phase.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/esi-protocol
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [agreement, drafting]
---

# ESI Protocol

Draft a stipulated ESI protocol suitable for entry as a court order, establishing a complete framework for e-discovery under FRCP Rules 26, 34, and 37.

## Prerequisites

Gather before drafting:

1. **Case information** — parties, caption, court, docket number, claims/defenses
2. **Existing orders** — scheduling orders, local rules, judge-specific ESI requirements
3. **Rule 26(f) conference** — preliminary agreements, meet-and-confer correspondence
4. **Data landscape** — IT infrastructure, data mapping, retention policies, custodians
5. **Prior ESI disputes** — correspondence or orders on ESI issues
6. **Vendor information** — e-discovery vendors, technical recommendations

## Quick Start

1. Collect all prerequisites; confirm temporal scope and custodian universe
2. Draft definitions and preamble anchored to FRCP 26(f)
3. Build protocol sections in EDRM lifecycle order (preserve → identify → collect → process → review → produce)
4. Add privilege protection with FRE 502(d) clawback
5. Include cost allocation, dispute resolution, and execution provisions
6. Validate against the checks below

## Protocol Sections

### 1. Preamble and Definitions

- Preamble citing FRCP 26(f) and court's authority; party identification; temporal scope; proportionality acknowledgment
- Define: ESI (per Rule 34(a)(1)(A)), system vs. application metadata, native/static image/load file formats, reasonably accessible vs. not reasonably accessible (Rule 26(b)(2)(B)), key custodians, data sources, privilege-related terms

### 2. Preservation Obligations

- Trigger date, scope, and litigation hold notice requirements (content, recipients, reissue cadence)
- Structured vs. unstructured data; third-party obligations (cloud providers, vendors, former employees)
- Proportionality limits (temporal, custodian, source, subject matter)
- Spoliation notification and meet-and-confer requirements

### 3. Identification and Collection

- Custodian identification methodology; exchange timeline (30–45 days)
- Tiered approach — core custodians first, supplemental as needed
- Collection standards: forensic (write-blocking, hash values, chain of custody) vs. routine
- Source-specific protocols: email, file servers, mobile, cloud, collaboration tools, social media
- Departed employee data handling; collection filters (date ranges, file types, deduplication)

### 4. Search Methodology

- **Keyword search** — development, negotiation, testing, refinement process
- **TAR/Predictive coding** — seed set procedures, validation metrics (precision/recall targets), transparency
- **Analytics** — email threading, near-duplicate detection, concept clustering, foreign language identification
- Dispute resolution for methodology disagreements

### 5. Processing and Review

- Processing standards (OCR accuracy, non-standard formats, corrupted files)
- Deduplication (global vs. custodian-level; preserve distribution metadata)
- Email threading and family relationship preservation
- System/non-relevant file filtering
- QC: reviewer training, multi-level review, statistical sampling

### 6. Production Format

- Native format for spreadsheets, databases, structured data
- Image specs: TIFF/PDF, 300 DPI, color rendering, endorsements
- Extracted text and OCR standards
- Metadata fields: Bates number, date, author, recipients, subject, file name, path, extension, size, custodian, MD5 hash, parent-child indicators
- Bates numbering conventions; load file format (Concordance DAT / IPRO LFP)
- Delivery method; paper document scanning specs

### 7. Privilege Protection

- Privilege log per Rule 26(b)(5)(A) — categorical vs. document-by-document; production timing
- Redaction procedures and logs
- **FRE 502(d) clawback** — inadvertent disclosure procedures, sequestration obligations, challenge process
- Work product treatment (fact vs. opinion); protective order for confidential information

### 8. Cost Allocation

- Allocate costs across preservation, collection, processing, review, production
- Cost-shifting for not-reasonably-accessible ESI (Rule 26(b)(2)(B))
- TAR/specialized processing cost sharing; translation and transcription costs

### 9. Cooperation and Dispute Resolution

- Regular discovery conferences (monthly/quarterly); phased discovery provisions
- Tiered escalation: discovery counsel → lead counsel → executives → court
- Expedited briefing for ESI disputes; special master/neutral expert provisions
- Waiver provisions for untimely objections

### 10. Execution and Modification

- Signature blocks for all parties
- Amendment procedures (technical vs. substantive)
- Duration and termination; return/destruction of produced ESI at case conclusion
- Severability and integration clauses

## Checks

- Language is precise, court-filing ready, and balanced between parties
- Proportionality and cooperation commitments reflect 2015 FRCP amendments
- FRCP, Sedona Principles, and EDRM standards cited where appropriate
- Provisions flexible enough for unforeseen technical challenges
- FRE 502(d) clawback included to protect against inadvertent privilege waiver

---

Key changes from the original:

- **Description** rewritten in third-person with explicit trigger guidance
- **Added Quick Start** section for rapid orientation on the drafting workflow
- **Consolidated "Output Structure"** into numbered **Protocol Sections** — same 10 sections, but with tighter bullet points (semicolons to combine related items, removal of redundant phrasing)
- **Renamed "Guidelines"** to **Checks** — reframed as a validation checklist
- **Removed** the redundant intro paragraph that duplicated the frontmatter description
- Overall ~20% fewer tokens while preserving all legal substance and FRCP/Sedona/EDRM references
