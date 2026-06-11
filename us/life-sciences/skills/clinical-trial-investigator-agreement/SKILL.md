---
name: clinical-trial-investigator-agreement
title: Clinical Trial Investigator Agreement
description: 'Drafts U.S. clinical trial Investigator Agreements between sponsors/CROs and principal investigators or institutions for FDA-regulated drug, biologic, or device studies. Enforces 21 CFR Parts 50, 56, 312/812, ICH GCP E6(R2), HIPAA, IRB requirements, FMV/AKS payment compliance, data integrity, publication rights, IP ownership, indemnity, and audit access. Use when drafting investigator agreements, PI agreements, clinical trial site agreements, or sponsor-PI contracts; trigger keywords: investigator agreement, clinical trial agreement, PI agreement, FDA, IND, IDE, IRB, GCP, clinical research agreement, site agreement.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/clinical-trial-investigator-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: life-sciences
language: en
tags: [agreement, drafting, regulatory]
---

# Clinical Trial Investigator Agreement

Drafts a sponsor–PI/site agreement that operationalizes FDA, IRB, and GCP obligations for a specific clinical trial.

## Prerequisites

1. Protocol number, title, version date, phase, endpoints, enrollment target.
2. Investigator's brochure or device manual; investigational product handling requirements.
3. Sponsor identity, CRO involvement, contracting structure (institution, PI, or both).
4. Site legal name, state law, institutional policies, and any required template language.
5. PI credentials, sub-investigators, study team roles.
6. Budget and payment model (per subject, per visit, milestones); invoicing rules.
7. IRB details, consent/assent forms, recruitment materials, vulnerable population plan.
8. Data ownership, publication expectations, IP posture, sample handling.
9. Insurance positions and indemnity constraints (public entities, academic limits).

## Output Structure / Process

1. **Intake** — targeted questions; confirm drug/biologic (21 CFR 312) vs device (21 CFR 812) track.
2. **Draft** — follow the section order below, incorporating site-specific policies.
3. **Exhibits** — attach and incorporate by reference.
4. **Verify** — run compliance checks using the tables and checklist below.

### Regulatory Baseline

| Topic | Authority |
|---|---|
| Informed consent | 21 CFR Part 50; LAR, assent where required |
| IRB | 21 CFR Part 56; 45 CFR 46 when institution requires |
| Drugs/Biologics | 21 CFR Part 312; IND obligations flow down |
| Devices | 21 CFR Part 812; IDE obligations flow down |
| GCP | ICH GCP E6(R2) |
| Financial disclosure | 21 CFR Part 54 |
| Privacy | HIPAA and state privacy laws |
| Vulnerable populations | 45 CFR 46 Subparts B, C, D |

### Agreement Sections

| Section | Must Include |
|---|---|
| Parties and Definitions | Sponsor, institution, PI; define Study, Protocol, Investigational Product, SAE, Confidential Information |
| Study Description | Protocol incorporated by reference; scope; single vs multi-center |
| Investigator Responsibilities | Conduct per protocol; no deviations except to eliminate immediate hazard; amendment approval workflow |
| IRB and Approvals | No study activities before written IRB approval; continuing review; submissions shared with sponsor |
| Informed Consent | Current IRB-approved forms; qualified designee; no coercion; LAR and assent as applicable |
| Study Personnel | Delegation of authority log; training documentation; PI retains ultimate responsibility |
| Investigational Product | Receipt only from sponsor; storage conditions; accountability logs; no off-protocol use; return/destroy per sponsor |
| Safety Reporting | AE/SAE definitions; sponsor reporting timelines; IRB reporting for unanticipated problems |
| Data Integrity | ALCOA+; source data verification; correction rules; EDC audit trail |
| Records and Retention | Essential documents per ICH GCP § 8; retention per 21 CFR 312.62(c) / 812.140(d), or longer per law/policy |
| Monitoring and Access | Reasonable advance notice; direct source access; HIPAA minimum necessary; corrective actions |
| Regulatory Inspections | Notify sponsor within 24 hours; provide FDA 483 or correspondence within 5 business days |
| Confidentiality | Scope; permitted disclosures to IRB/regulators; term and return/destruction |
| Data and IP Ownership | Sponsor owns study data and results; invention assignment; sample ownership with institutional carve-outs |
| Publications | Sponsor review window; patent delay; multicenter coordination; ICMJE authorship standards |
| Compensation and Budget | FMV/AKS compliance; invoicing; screen fail and early withdrawal rules; startup/closeout costs |
| Financial Disclosure/COI | 21 CFR Part 54 disclosures; update obligations; conflict management |
| Indemnification | Sponsor product liability indemnity; carve-outs for PI/site negligence or noncompliance |
| Insurance | Sponsor clinical trial liability; site professional liability; certificate requirements |
| Term and Termination | For cause and convenience; subject safety wind-down; payment of earned fees |
| Governing Law/Disputes | State law selection; venue or negotiation/mediation steps |
| Compliance | FCPA/UK Bribery Act; export control/OFAC; Sunshine Act reporting |

### Exhibits

- [ ] Protocol and amendments
- [ ] Budget and payment schedule
- [ ] Study team roster and qualifications
- [ ] Financial disclosure forms
- [ ] Informed consent/assent forms
- [ ] Institutional policies incorporated by reference
- [ ] Publication policy (if separate)

### Default Timelines

Adjust to protocol/IRB policy.

| Event | Default |
|---|---|
| Sponsor notification of SAE | Within 24 hours of awareness |
| IRB submission of unanticipated problems | Per IRB policy, prompt reporting |
| Publication review by sponsor | 45–60 days before submission |
| Patent delay after review | Up to 60–90 days |

### Final Checks

- [ ] Parties and governing law match site and sponsor
- [ ] All regulatory citations align with drug/biologic vs device track
- [ ] Consent and privacy requirements align with site policy
- [ ] Payment terms are FMV and AKS compliant
- [ ] Indemnity/insurance reflect institutional limits
- [ ] Every unverified citation marked `[VERIFY]`

## Troubleshooting

| Issue | Resolution |
|---|---|
| Unclear whether drug or device track applies | Confirm IND (21 CFR 312) vs IDE (21 CFR 812) with sponsor; combination products follow primary mode of action |
| Institution requires its own template | Merge sponsor terms into institutional template; flag conflicts for negotiation |
| Public entity cannot indemnify | Carve out sovereign immunity; shift to insurance-only model with higher certificate minimums |
| PI holds multiple roles (e.g., also sponsor-investigator) | Apply 21 CFR 312.50–312.70 sponsor obligations in addition to investigator duties |
| Budget exceeds FMV benchmarks | Document FMV analysis methodology; adjust per AAMC/PhRMA guidelines to avoid AKS risk |

## Guidelines

- Apply the most stringent requirement among federal law, state law, and institutional policy.
- No study activity before IRB approval and full execution if required by the institution.
- Keep confidentiality and publication clauses consistent with multi-center coordination.
- Preserve a clear audit trail for data corrections and monitoring access.
- Flag any unclear regulatory citation with `[VERIFY]`.

---
