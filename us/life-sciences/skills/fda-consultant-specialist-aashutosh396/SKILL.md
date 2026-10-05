---
name: fda-consultant-specialist-aashutosh396
title: FDA Consultant Specialist
description: Use when planning an FDA medical-device submission (510(k), PMA, De Novo), assessing QMSR/21 CFR 820 compliance, HIPAA for connected devices, or device cybersecurity — picks the pathway and lays out the required submission and quality steps.
author: aashutosh396
author_url: https://github.com/aashutosh396/mindpalace/tree/main/mindpalace/skills/global/compliance/fda-consultant-specialist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: life-sciences
language: en
tags: [fda, 510k, pma, de-novo, qmsr, qsr, iso-13485, hipaa, medical-device, cybersecurity, premarket]
---

# FDA Consultant Specialist

FDA regulatory consulting for medical-device manufacturers: submission pathways, QMSR (21 CFR Part 820, which since 2026-02-02 incorporates ISO 13485:2016 by reference — legacy QSR 820.x subsection numbers are historical), HIPAA, and device cybersecurity.

## 1. Pathway selection

```
Predicate device exists?
├─ YES → Substantially equivalent?
│   ├─ YES → 510(k): no design change → Abbreviated; mfg only → Special; design/perf → Traditional
│   └─ NO  → PMA or De Novo
└─ NO  → Novel device? low-moderate risk → De Novo; high risk (Class III) → PMA
```

| Pathway | Use when | Timeline |
|---|---|---|
| 510(k) Traditional | Predicate exists, design changes | 90 days |
| 510(k) Special | Manufacturing changes only | 30 days |
| 510(k) Abbreviated | Guidance/standard conformance | 30 days |
| De Novo | Novel, low-moderate risk | 150 days |
| PMA | Class III, no predicate | 180+ days |

User fees set annually under MDUFA — verify current FY fees at fda.gov (small-business rates differ). Pre-sub strategy: identify product code + classification → search 510(k) DB for predicates → assess SE feasibility → prepare Q-Sub questions → schedule Pre-Sub meeting if needed.

## 2. 510(k) submission (21 CFR 807.87)

Phases: Planning (identify predicate, compare intended use/tech, determine testing — checkpoint: SE feasible?) → Preparation (testing, device description, SE comparison, labeling) → Submission (assemble pack, submit via eSTAR, track ack) → Review (monitor status, respond to AI requests, get decision).

Required sections: cover letter, Form 3514, device description, indications for use (Form 3881), SE comparison, performance testing (bench/biocompatibility/electrical), software docs (IEC 62304 level of concern + hazard analysis), labeling, 510(k) summary.

Common RTA failures: missing user fee, incomplete Form 3514, no predicate K-number, inadequate SE comparison.

## 3. QMSR compliance (21 CFR 820, ISO 13485:2016 by reference)

Cite ISO 13485 clauses in current docs; legacy QSR numbers are only a familiar index.

| Subsystem | ISO 13485 clause |
|---|---|
| Management responsibility | 5.1, 5.5, 5.6 |
| Design controls | 7.3 |
| Document controls | 4.2.4 |
| Purchasing controls | 7.4 |
| Production controls | 6.3, 6.4, 7.5 |
| CAPA | 8.5.2, 8.5.3 |
| Medical device file (DMR) | 4.2.3 + 21 CFR 820.35 (retained) |

Design controls flow: input (user needs, intended use, reg reqs) → output (specs, drawings, SW arch, traceable to inputs) → review (at each milestone, signed) → verification (test vs specs) → validation (meets user needs in actual use) → transfer (DMR complete).

CAPA: identify → investigate (5 Whys / fishbone) → plan → implement → verify → effectiveness (monitor 30-90 days) → close (management approval).

## 4. HIPAA for devices

Applies to connected devices transmitting patient data, EHR-integrated devices, SaMD storing PHI. Safeguards: Administrative (§164.308 — security officer, risk analysis, training, incident response, BAAs); Physical (§164.310 — facility/workstation access, disposal); Technical (§164.312 — access control, audit logging, integrity, authentication/MFA, TLS 1.2+). Risk steps: inventory ePHI systems → map data flows → identify threats/vulns → assess likelihood/impact → set risk levels → implement controls → document residual.

## 5. Device cybersecurity

Premarket: threat model (STRIDE, attack trees, trust boundaries), security controls, SBOM (CycloneDX/SPDX), security testing (pen test, vuln scan), vulnerability disclosure + patch plan. Tier 1 = network-connected AND incident could cause patient harm; Tier 2 = other connected. Postmarket: monitor NVD + ICS-CERT → assess applicability → develop/test patches → notify customers → report to FDA. Coordinated disclosure: acknowledge (48h) → assess (5d) → fix → coordinated public disclosure.

> Checklists structure assessment; they do not certify compliance. Route classification/submission-record questions to Regulatory Affairs; confirm current 21 CFR 820 / ISO 13485 text at fda.gov.
