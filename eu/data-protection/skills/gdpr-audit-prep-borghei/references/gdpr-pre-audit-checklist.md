# GDPR Pre-Audit Checklist

Detailed pre-audit punch list per GDPR area. For each item: evidence required, common gap, remediation pattern.

---

## ROPA (Records of Processing Activities, Article 30)

For controllers (Article 30.1) AND processors (Article 30.2). Mandatory documentation.

### Per-processing-activity content

| Item | Evidence | Common gap |
|------|----------|------------|
| Name and contact of controller (and DPO if applicable) | ROPA document header | DPO contact missing/stale |
| Purposes of processing | Per activity | Vague ("operations") instead of specific |
| Categories of data subjects | Per activity | Missing some categories (e.g., job applicants, vendors) |
| Categories of personal data | Per activity | Sensitive data categories not flagged separately |
| Recipients (internal + external) | Per activity | External recipients incomplete |
| International transfers + safeguard | Per activity | Transfer mechanism missing or stale post-Schrems II |
| Retention periods | Per activity | "As long as necessary" — not specific |
| Security measures (general description) | Per activity | "Industry standard" — not specific |
| Lawful basis (Article 6) | Per activity | Consent claimed when no consent collected |
| Special-category data processing (Article 9) | Per activity (if applicable) | Special category data not flagged |
| Date of last update | ROPA document | > 12 months stale |

---

## Privacy Notices (Article 13/14)

### Required information per notice (Article 13 / 14)

| Item | Evidence |
|------|----------|
| Identity and contact details of controller | Privacy notice header |
| DPO contact (if appointed) | Notice |
| Purposes of processing + lawful basis | Per processing activity |
| Recipients or categories of recipients | Listed |
| International transfers + safeguards | Disclosed |
| Retention period (or criteria to determine) | Specific |
| Data subject rights (access, rectification, erasure, restriction, portability, object, withdraw consent, complain to authority) | All 8 listed |
| Right to withdraw consent (if consent-based) | Specifically mentioned |
| Right to complain to supervisory authority | With contact info |
| Source of data (if not from subject) | For Article 14 |
| Automated decision-making (Article 22) | If applicable, explained |

### Common gaps

- Generic notice template not reflecting actual processing
- Out-of-date (changes to processing not reflected)
- Hidden behind dark patterns (long scrolls, small text)
- Not translated to local language (member state-specific)
- Different versions exist; no clear current

---

## Data Subject Rights (Articles 12-23)

### Process documentation

| Item | Evidence |
|------|----------|
| Process for handling requests | Documented procedure |
| Identity verification method | Per procedure |
| Response time tracking | Ticketing tool / spreadsheet |
| One-month response deadline observed | Records show compliance |
| Extension (additional 2 months) documented when used | Per ticket |
| Record of request types received | Counts by type (access, deletion, etc.) |

### Common gaps

- Process documented; never tested
- No central intake (requests come via random channels and get lost)
- Identity verification weak (or absent)
- Response times exceeded; no extension notification
- Records of requests not maintained

### Sample audit period evidence

Pull from last 12 months:
- Total request count by type
- Median response time
- Any expedites / extensions
- Any partial / refused requests + reasoning

---

## Data Protection Impact Assessments (DPIA, Article 35)

### When DPIA mandatory (high-risk processing)

- Systematic and extensive evaluation of personal aspects (e.g., profiling)
- Processing on a large scale of special-category data
- Systematic monitoring of publicly accessible areas
- Per supervisory authority's "DPIA list" (member state-specific)
- New technologies (AI, biometrics, IoT) processing personal data

### DPIA content (Article 35.7)

| Item | Required |
|------|----------|
| Description of envisaged processing operations | Yes |
| Purposes of processing | Yes |
| Necessity and proportionality assessment | Yes |
| Risks to rights and freedoms of data subjects | Yes |
| Measures to address risks (mitigation, safeguards, security) | Yes |
| Consultation with DPO (Article 35.2) | If DPO exists, yes |

### Common gaps

- DPIA missing for high-risk processing
- DPIA conducted, never updated as processing changes
- Mitigations identified, never implemented
- DPO not consulted
- New high-risk processing launched without DPIA

---

## Data Processing Agreements (Article 28)

### Required clauses (Article 28.3)

- Processor processes only on documented instructions of controller
- Confidentiality undertakings by personnel
- Article 32 security measures
- Sub-processor restrictions
- Assistance with data subject rights
- Assistance with security obligations
- Deletion or return of data at end
- Information for audits
- Notice if instruction conflicts with EU law

### Common gaps

- DPA missing entirely (just MSA)
- Old DPA pre-GDPR (2016 or earlier; doesn't meet Article 28.3)
- DPA missing required clauses
- Sub-processor list not maintained
- Audit rights ignored

---

## Security Measures (Article 32)

### Technical and organizational measures (TOMs)

| Item | Standard |
|------|----------|
| Encryption of personal data (at rest + transit) | Industry-standard cipher suites |
| Pseudonymization (where appropriate) | For analytical / development use |
| Confidentiality | Access controls, segregation |
| Integrity | Change management, validation |
| Availability | Backup, DR |
| Resilience | High availability, redundancy |
| Restoration capacity | Tested backup/restore |
| Regular testing | Pen tests, vuln scans, audits |
| Process for evaluating effectiveness | Annual review |

### Common gaps

- Encryption inconsistent
- Backup configured; never restore-tested
- Access controls outdated (terminated users still have access)
- No regular review of measures

---

## Breach Notification (Article 33/34)

### Process requirements

| Item | Evidence |
|------|----------|
| Breach detection capability | Monitoring + alerting |
| Breach response process documented | Runbook |
| 72-hour authority notification capability | Tested communication channels |
| Records of all breaches (Article 33.5) | Breach register |
| Past-period breach notifications | Per breach: timing, content, communications |
| Subject notification (Article 34, when required) | Communication evidence |

### Common gaps

- No breach response runbook
- No 72-hour SLA process — breach reported late
- Subject notification skipped when required (high risk to subjects)
- Breach register missing / incomplete

---

## International Transfers (Chapter V)

### Mechanism per transfer

| Mechanism | When | Evidence |
|-----------|------|----------|
| Adequacy decision | EU Commission adequacy (UK, Switzerland, Canada-commercial, etc.) | List of countries + dates |
| Standard Contractual Clauses (SCCs) | Most common for vendors | Signed SCCs per transfer |
| Binding Corporate Rules (BCRs) | Large multinationals | Approved BCRs |
| Derogations (Article 49) | Specific situations | Per Article 49 conditions |

### Schrems II compliance (post-2020, US transfers)

- Transfer Impact Assessment (TIA) for non-adequacy transfers
- Supplementary measures (encryption, contractual restrictions)
- Documentation of analysis
- Updated when surveillance environment changes

### Common gaps

- SCCs signed but old 2010 version (not new 2021)
- TIA not conducted for US transfers
- No documentation of safeguards beyond SCCs
- New US vendor onboarded without transfer review

---

## DPO (Data Protection Officer, Article 37)

### When DPO required

- Public authority / body
- Core activities consist of regular and systematic monitoring of data subjects on a large scale
- Core activities consist of processing on a large scale of special-category data

### Documentation

- DPO appointment letter
- DPO contact published (notice + ROPA)
- DPO independent (not reporting to controller for DPO duties)
- DPO consulted on high-risk processing

---

## Consent (Article 7)

### Validity criteria

- Freely given (no bundling, no harm if refused)
- Specific (per purpose)
- Informed (provide notice before consent)
- Unambiguous (clear affirmative action — not pre-ticked boxes)
- Withdrawable (easy to withdraw)
- Documented (proof of consent per subject)

### Common gaps

- Cookie banner with pre-ticked boxes
- Bundle consent ("agree to use the service" + "marketing emails")
- Withdraw process burdensome
- Consent records missing or weak

---

## Pre-audit walkthrough preparation

### For the DPO

```
- ROPA walkthrough: pick 2-3 processing activities, walk through ROPA entry
- DPIA walkthrough: pick a high-risk activity, walk through DPIA
- Past-period breach walkthrough: any breach in last 12 months
- DSR walkthrough: most recent request, response, timing
```

### For technical lead

```
- Encryption: show key management
- Backup: show last restore test
- Access control: show how data subject's data is restricted
- Audit log: show how data access is recorded
```

### For business lead

```
- New processing activity: how was it assessed before launch (DPIA?)
- Vendor onboarding: DPA + transfer mechanism
- Subject rights: tickets from last quarter
```

---

## Cheat sheet

| Question | Answer |
|----------|--------|
| Single most-cited gap? | ROPA incomplete or stale |
| Biggest risk-of-fine area? | DPIA missing for AI / large-scale monitoring |
| Easiest quick win? | Update privacy notice; sign DPAs with all processors |
| What does DPO do during audit? | Coordinate response; lead walkthroughs; legal/regulatory communications |
| Common surprise finding? | Sub-processor list out-of-date |
| Time to fix typical gap? | Policy: days; DPIA: weeks; process change: weeks-months |
