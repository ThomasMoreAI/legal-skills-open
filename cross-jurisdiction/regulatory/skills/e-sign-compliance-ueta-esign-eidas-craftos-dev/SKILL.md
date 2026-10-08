---
name: e-sign-compliance-ueta-esign-eidas-craftos-dev
title: E-sign compliance — UETA / ESIGN / eIDAS / eIDAS 2.0
description: E-signature compliance — UETA (US state), ESIGN Act (US federal), eIDAS Regulation 910/2014 + eIDAS 2.0 / EUDI Wallet (EU), UK Electronic Communications Act, plus industry overlays (21 CFR Part 11 FDA, HIPAA, CMMC, FedRAMP). Pick signature tier (SES / AES / QES); produce per-jurisdiction compliance checklist; recommend Trust List provider for QES. Use when the user says "is this signature legally binding?", "eIDAS QES", "UETA / ESIGN compliance", "21 CFR Part 11 e-signature", "HIPAA-compliant e-sign", "RON statute".
author: CraftOS-dev
author_url: https://github.com/CraftOS-dev/craftbot-agent-bundles/tree/main/agents/docgen-automation/skills/e-sign-compliance-ueta-esign-eidas
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: regulatory
language: en
---

# E-sign compliance — UETA / ESIGN / eIDAS / eIDAS 2.0

This skill produces compliance checklists + tier recommendations. **It does NOT give legal advice.** Every output ends with the consult-an-attorney disclaimer; final legal effect is `legal-counsel`'s territory.

## When to use

User says:

- "Is this signature legally binding?"
- "UETA / ESIGN Act compliance"
- "eIDAS / eIDAS 2.0 / Qualified Electronic Signature (QES)"
- "EUDI Wallet"
- "21 CFR Part 11 (FDA)"
- "HIPAA-compliant signature"
- "CMMC / FedRAMP e-sign"
- "RON (remote online notarization) — which states?"
- "State carve-outs (wills, real estate, UCC)"
- "UK Electronic Communications Act"

Companion skills:
- `e-signature-docusign-adobe-sign-pandadoc` — execution mechanics (this skill picks the tier; that skill builds the envelope).
- `audit-trail-e-sign-versioning` — record retention + Certificate of Completion.
- `redaction-automation-pii` — sometimes required pre-signature for compliance.

## Setup

```bash
# No SDK install required — this is policy + checklist work.
# But for fetching current statutes:
pip install firecrawl    # optional, via firecrawl-mcp

# References on disk (mirror current as of 2026-06):
# - ESIGN Act:   15 USC §§ 7001-7031
# - UETA:        Uniform Law Commission text + state adoption table
# - eIDAS:       Regulation (EU) 910/2014
# - eIDAS 2.0:   Regulation (EU) 2024/1183 — EUDI Wallet
# - 21 CFR §11:  FDA Electronic Records / Electronic Signatures
# - HIPAA:       45 CFR §§ 164.302-318 (Security Rule)
```

## Common recipes

### Recipe 1: Pick a signature tier (decision tree)

```text
Is the document personal (will / divorce / court order / certain UCC)?
├── YES → e-sign generally NOT permitted; use wet ink + traditional notarization.
└── NO  → continue
        Is the counterparty in the EU?
        ├── YES → Apply eIDAS:
        │       Low risk (sales contract, NDA)   → Simple ES (SES) sufficient.
        │       Medium risk (corporate, HR)     → Advanced ES (AES) recommended.
        │       High risk (regulated, gov)      → Qualified ES (QES) — Trust List provider mandatory.
        └── NO  → Apply UETA + ESIGN:
                Did both parties consent to electronic records?
                ├── YES + attribution + retention met → e-sign valid.
                └── NO → capture consent before signing.
```

### Recipe 2: US (ESIGN + UETA) compliance checklist

```markdown
## ESIGN Act (15 USC §7001) — federal
- [ ] Consumer consent to electronic records — separately captured + reasonable demonstration the consumer can access the format
- [ ] Disclosure of right to receive paper copy
- [ ] Disclosure of hardware/software requirements + whether consent applies only to current transaction or future records

## UETA (47 states + DC) — state-level
- [ ] Each party intends to conduct the transaction electronically
- [ ] Intent to sign — signature ceremony captures it
- [ ] Association of signature with the record — envelope binding (tab) ties signer to specific doc
- [ ] Record retention — record + signature accessible + retrievable for the statutory period
- [ ] Attribution — signature attributable to a person (auth method documented)

## Carve-outs (e-sign generally NOT valid for):
- [ ] Wills, codicils, testamentary trusts
- [ ] Adoption, divorce, family law matters
- [ ] Court orders, notices, official court documents
- [ ] Certain UCC Articles (specifically 3 negotiable instruments, 4 bank deposits, 5 letters of credit)
- [ ] Cancellation / termination of utility services
- [ ] Cancellation / termination of health / life insurance benefits
- [ ] Recall notices of products that risk health or safety
- [ ] Documents required to accompany the transportation of hazardous materials

## Non-UETA states
- New York (not full UETA, but has Electronic Signatures and Records Act, ESRA)
- Illinois (Electronic Commerce Security Act)
- Washington (state-specific provisions)
- → Verify state-specific requirements separately
```

### Recipe 3: EU (eIDAS Regulation 910/2014) compliance checklist

```markdown
## eIDAS three tiers
| Tier | Definition | Use case | Verification |
|---|---|---|---|
| SES (Simple ES) | Data in electronic form attached to or logically associated with other electronic data | Internal docs, sales contracts, NDAs | Any reasonable method (typed name, scanned signature, click-to-sign) |
| AES (Advanced ES) | Uniquely linked + capable of identifying signer + signer control + linked to data so any change is detectable | HR docs, corporate, mid-risk contracts | Strong identification + cryptographic signature; control over signing device |
| QES (Qualified ES) | AES + Qualified Certificate from EU Trust List provider + Qualified Signature Creation Device (QSCD) | Regulated, government, high-stakes | Trust List provider's audited identity verification + QSCD |

## Article 25 — legal effect (cannot be denied solely because electronic)
- [ ] Document not denied legal effect or admissibility solely because of electronic form
- [ ] QES has equivalent legal effect as handwritten signature in all member states

## eIDAS 2.0 (Regulation 2024/1183) — EUDI Wallet
- [ ] EU Digital Identity Wallet (EUDI Wallet) operational; member states roll out 2024-2026
- [ ] Qualified Electronic Attestation (QEA) for verified credentials
- [ ] Cross-border interoperability mandated

## Choosing QES provider — EU Trust List
Sample QES providers (verify current via https://webgate.ec.europa.eu/tl-browser/):
- Adobe Sign Trust Services (QES via partner Qualified Trust Service Providers)
- DocuSign EU Advanced + Qualified (via partners e.g., InfoCert, IDnow)
- OneSpan Sign Qualified (banking-friendly)
- Skribble (EU Qualified)
- D-Trust (German Trust Service Provider)
- InfoCert (Italian TSP)
```

### Recipe 4: UK compliance (Electronic Communications Act 2000 + Post-Brexit eIDAS)

```markdown
## UK Electronic Communications Act 2000 + UK eIDAS (retained EU law as of 2021)
- [ ] Electronic signatures admissible in UK courts (Law Commission report 2019 + court precedent)
- [ ] Different tiers as in EU eIDAS: SES, AES, QES
- [ ] UK Trust Services — UK adopted its own UK Trust Mark (post-Brexit)
- [ ] Cross-border: UK QES recognized in EU and vice versa per UK-EU MoU
- [ ] Statutory exceptions: same as EU (wills, certain land transactions require wet ink + witness)
```

### Recipe 5: Industry overlay — 21 CFR Part 11 (FDA / pharma)

```markdown
## Subpart B — Electronic Records (§11.10)
- [ ] Validation of systems to ensure accuracy, reliability, consistent intended performance
- [ ] Ability to generate accurate and complete copies of records in human-readable and electronic form
- [ ] Protection of records to enable accurate and ready retrieval throughout retention period
- [ ] Limit system access to authorized individuals
- [ ] Use of secure, computer-generated time-stamped audit trails
- [ ] Use of operational system checks to enforce permitted sequencing of steps + events
- [ ] Use of authority checks
- [ ] Use of device (terminal) checks
- [ ] Determination that persons who develop, maintain, or use systems are qualified
- [ ] Establishment of written policies that hold individuals accountable for actions

## Subpart C — Electronic Signatures (§11.50 + §11.70 + §11.100 + §11.200 + §11.300)
- [ ] Signed records contain printed name of signer, date/time, meaning (review, approval, responsibility)
- [ ] Electronic signature linked to its respective electronic record (cannot be excised, copied, transferred to falsify)
- [ ] Identity of individual verified at signature
- [ ] Each electronic signature is unique to one individual + not reused
- [ ] Two distinct identification components (e.g., user ID + password)
- [ ] When session resumed after timeout, both components required

## Validated systems for 21 CFR Part 11
- DocuSign Life Sciences edition
- Adobe Sign for pharma
- Veeva Vault (pharma-native)
- IQVIA Signatures
```

### Recipe 6: HIPAA — PHI-related signatures

```markdown
## HIPAA Security Rule (45 CFR § 164.302-318)
- [ ] Access controls (§164.312(a)) — unique user identification, automatic logoff, encryption + decryption
- [ ] Audit controls (§164.312(b)) — hardware, software, procedural mechanisms to record + examine activity
- [ ] Integrity (§164.312(c)) — electronic PHI cannot be improperly altered or destroyed
- [ ] Person or entity authentication (§164.312(d)) — verify identity of person seeking access to ePHI
- [ ] Transmission security (§164.312(e)) — encrypt PHI in transit + at rest

## E-signature platforms with HIPAA BAA
- DocuSign for Healthcare
- Adobe Sign HIPAA-compliant tier
- PandaDoc HIPAA-compliant plan
- Formstack HIPAA-eligible workspace
```

### Recipe 7: CMMC / FedRAMP signature compliance

```markdown
## CMMC (Cybersecurity Maturity Model Certification — DoD contractors)
- [ ] Use e-sign platform at the required CMMC level (1-3 as of CMMC 2.0)
- [ ] FedRAMP Moderate or High authorized provider for federal contracts
- [ ] DocuSign Federal (FedRAMP Moderate + High)
- [ ] Adobe Sign Government (FedRAMP)

## ITAR / EAR considerations
- [ ] Don't store ITAR-controlled docs with non-US-citizen-accessible services
- [ ] Use FedRAMP US-only data residency confirmed
```

### Recipe 8: RON (Remote Online Notarization)

```markdown
## RON state adoption (as of 2026 — 40+ states + DC)
**Adopting:**
AK, AL, AR, AZ, CO, CT, DC, FL, GA, HI, IA, ID, IL, IN, KS, KY, LA, MD, MI, MN, MO, MS, MT, NC, ND, NE, NJ, NM, NV, NY, OH, OK, PA, RI, SD, TN, TX, UT, VA, VT, WA, WI, WV, WY

**Pending / partial:**
California (2027 effective per AB 1093)
Mississippi (limited)

**Statutory model:**
- RULONA (Revised Uniform Law on Notarial Acts) — version 2018 update with RON provisions
- MBA (Mortgage Bankers Association) Model RON Act
- State-specific (e.g., FL, VA, TX have pioneer statutes)

## RON requirements (typical, varies by state)
- [ ] Commissioned notary physically located in commissioning state
- [ ] Audio + video session, recorded + retained (5-10 years typically)
- [ ] ID verification — credential analysis + KBA (knowledge-based authentication)
- [ ] Tamper-evident technology with audit trail
- [ ] Electronic seal + signature
- [ ] Signer + notary digitally sign

## RON providers
- Proof.com (formerly Notarize.com)
- NotaryCam
- Notarize
- DocVerify (eNotaryLog)
- BlueNotary
```

### Recipe 9: Per-jurisdiction compliance memo template

```markdown
# E-signature compliance memo — [DOCUMENT TYPE] for [COUNTERPARTY]
Date: {YYYY-MM-DD}
Prepared by: docgen-automation agent (NOT legal advice)

## Jurisdiction analysis
- Signer 1: [name], located in [state/country]
- Signer 2: [name], located in [state/country]
- Governing law: [state/country]

## Applicable framework
- US ESIGN Act + UETA in [state] ☐
- EU eIDAS in [country] ☐
- UK Electronic Communications Act ☐
- Industry overlay: [21 CFR Part 11 / HIPAA / CMMC / FedRAMP / None]

## Recommended signature tier
- [ ] SES — sufficient
- [ ] AES — recommended (medium risk)
- [ ] QES — required (regulated, high risk)
- [ ] Wet ink + notarization (carve-out applies)

## Recommended platform configuration
- Platform: [DocuSign / Adobe Sign / Dropbox Sign / OneSpan / Skribble / ...]
- Auth method: [Email link / SMS / KBA / ID Verification / Photo ID + Bio]
- Tier add-on: [Trust List provider for QES if applicable]
- Retention: [7 / 10 / 25 years per applicable statute]

## Hand-off
**This memo is informational. Consult a licensed attorney in the governing jurisdiction before executing.**
```

### Recipe 10: Fetch current regulator text via firecrawl

```bash
# When statute may have changed (eIDAS 2.0 rollout, state RON adoption)
# Use firecrawl-mcp:
firecrawl scrape https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation
firecrawl scrape https://www.uniformlaws.org/committees/community-home?CommunityKey=2c04b76c-2b7d-4399-977e-d5876ba7e034
```

### Recipe 11: Record retention checklist

```markdown
## Retention obligations by type
- Tax-related docs: IRS 7-year rule (US)
- Employment: 4-7 years per state + EEOC
- HIPAA-related: 6 years from creation
- 21 CFR Part 11: lifetime of product + 10 years (varies)
- Commercial contracts: typically statute of limitations + 1 year (6-10 years)
- EU GDPR: only as long as necessary + clear retention schedule
- UK: 6 years (Limitation Act 1980)

## Storage requirements
- [ ] Encrypted at rest + in transit
- [ ] Access logged + audited
- [ ] Hashed + tamper-evident (OpenTimestamps optional but recommended for high-stakes)
- [ ] Backup + DR plan
```

## Examples

### Example 1: B2B SaaS MSA — US customer in California

**Goal:** Determine signature tier + platform for an MSA between US vendor and CA-based customer.
**Steps:**
1. Recipe 1 — decision tree → US → UETA + ESIGN apply.
2. Recipe 2 — checklist; California is full UETA state.
3. Memo (Recipe 9): SES sufficient; DocuSign default; email link auth.
4. Carve-outs (Recipe 2): MSA not in carve-out list; e-sign valid.
5. Disclaimer + hand off to `legal-counsel`.

**Result:** Memo recommending DocuSign SES.

### Example 2: EU regulated insurance product — QES needed

**Goal:** Insurance policy issued to German consumer; insurer is French.
**Steps:**
1. Recipe 1 — counterparty in EU → eIDAS applies; insurance is regulated → QES recommended.
2. Recipe 3 — choose Trust List provider; e.g., InfoCert + DocuSign EU Qualified.
3. Memo: QES required; provider InfoCert; expected cost ~€5-10/signature.
4. Hand off to French regulatory counsel for confirmation.

**Result:** QES configuration recommendation + provider shortlist.

### Example 3: Real estate transaction — RON via Proof.com

**Goal:** Florida property sale; both parties remote.
**Steps:**
1. Recipe 1 — real estate often has carve-outs; check FL RON statute.
2. Recipe 8 — FL is a RON state with §117.225 et seq. statute.
3. Use Proof.com RON; signer + notary audio/video session; KBA + ID verification.
4. Output: notarized deed + audit trail + recording per FL law.
5. Hand off to real-estate counsel for closing.

**Result:** Compliant RON ceremony + e-notary seal.

## Edge cases / gotchas

- **State carve-outs evolve.** Wills + estate planning generally still wet-ink; but Nevada + Indiana + Arizona permit e-wills under specific statutes. Always check current.
- **California's CUETA.** CA adopted UETA as California Uniform Electronic Transactions Act (Civil Code §1633.1 et seq.). Same effect as UETA.
- **NY ESRA is not UETA.** New York has Electronic Signatures and Records Act — substantially similar but not identical.
- **eIDAS QES requires QSCD.** Qualified Signature Creation Device — often a HSM at the Trust Service Provider. Not all DocuSign plans include QES; requires partner integration.
- **eIDAS 2.0 EUDI Wallet rollout uneven.** Member states roll out 2024-2026; cross-border interop still maturing.
- **21 CFR Part 11 validation burden.** Implementing 21 CFR Part 11 e-sign is not just turning on a feature; full system validation + IQ/OQ/PQ documentation + change control required.
- **HIPAA BAA not implicit.** Just because a platform "supports HIPAA" doesn't make you compliant — sign the BAA + configure the workspace correctly.
- **RON jurisdiction = notary location.** The notary must be commissioned in a state that permits RON + be physically in that state during the session. Signer can be anywhere with internet.
- **Document type vs signature type mismatch.** A QES platform doesn't make a will valid; it just makes the signature qualified.
- **Cross-border recognition.** EU-US e-sign mutual recognition not automatic; courts may still inquire. UK-EU MoU provides framework.
- **Don't rely on this skill as legal advice.** Always cite "consult an attorney" + jurisdiction.
- **eIDAS levels are not hierarchical for all purposes.** QES > AES > SES for legal weight, but a sales contract using SES is fine; using QES is "overengineering" for low-risk docs.
- **Auth method matters.** Email-link is SES; SMS adds factor toward AES; ID verification + photo + bio toward AES/QES.
- **Audit certificate ≠ legal effect.** DocuSign Certificate of Completion is evidentiary, not constitutive. Legal effect comes from statute + ceremony.
- **Statutes change.** RON adoption + eIDAS 2.0 + state e-sign carve-outs evolve frequently. Use `firecrawl-mcp` to confirm current.

> **CRITICAL DISCLAIMER:** This skill provides informational guidance only. It is NOT legal advice. The legal effect of an e-signature depends on the specific document, jurisdiction, parties, and circumstances. Always consult a licensed attorney before relying on an electronic signature for a binding legal document, especially for regulated industries, cross-border transactions, real estate, or high-stakes contracts.

## Sources

- [ESIGN Act (15 USC §7001)](https://www.law.cornell.edu/uscode/text/15/chapter-96) — US federal.
- [UETA (Uniform Law Commission)](https://www.uniformlaws.org/committees/community-home?CommunityKey=2c04b76c-2b7d-4399-977e-d5876ba7e034) — US state-level.
- [eIDAS Regulation 910/2014](https://eur-lex.europa.eu/eli/reg/2014/910/oj) — EU framework.
- [eIDAS 2.0 + EUDI Wallet (EU Digital Strategy)](https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation) — 2024 update.
- [EU Trust List Browser](https://webgate.ec.europa.eu/tl-browser/) — current QES providers.
- [21 CFR Part 11 (FDA)](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application) — pharma/life sciences.
- [HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html) — PHI signatures.
- [RULONA + RON Model Law](https://www.uniformlaws.org/committees/community-home?CommunityKey=2e36ec39-cea2-4ab8-bb74-6cf0ce5dfcf5) — Uniform Law Commission RON.
- [DocuSign Trust](https://www.docusign.com/trust) — compliance certifications.
- [Adobe Sign compliance](https://www.adobe.com/sign/compliance.html) — certifications.
- Sister skills: `e-signature-docusign-adobe-sign-pandadoc`, `audit-trail-e-sign-versioning`.
