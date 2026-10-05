# AI Agent Regulator Overlap Matrix

The canonical wide table. One row per control area; one column per regime. Cell content: clause ID; shared-evidence artefact name; or divergent-evidence note.

Legend:

- **SOC2** = AICPA Trust Services Criteria (2017/2022).
- **ISO** = ISO/IEC 27001:2022 Annex A; **42001** = ISO/IEC 42001:2023 clause.
- **HIPAA** = 45 CFR §164.
- **AI Act** = EU Regulation 2024/1689.
- **NIST** = AI RMF 1.0 functions (GOVERN / MAP / MEASURE / MANAGE).
- **KE** = Kenya DPA 2019 + ODPC AI guidance 2024.
- **NG** = Nigeria NDP Act 2023 + NDPC advisory 2024.
- **ZA** = South Africa POPIA 2013.
- **UG** = Uganda DPPA 2019.
- **RW** = Rwanda DP Law 2021.

| Control area | SOC2 | ISO / 42001 | HIPAA | AI Act | NIST | KE | NG | ZA | UG | RW |
|---|---|---|---|---|---|---|---|---|---|---|
| Action governance | CC5.1, CC8.1 | A.5.1, A.5.15 / 5.2, 8 | 164.308.a.4 | Art. 9 (high-risk QMS); Art. 14 | GOVERN-2 | s.40 | Art. 29 | s.19 | s.24 | Art. 25 |
| Audit logging — retention | CC7.2 | A.8.15 / A.6 | 164.312.b, 164.316.b | Art. 12 | MEASURE-3 | s.41 | Art. 32 | s.19 | s.19 | Art. 25 |
| Audit logging — integrity | PI1.4 | A.8.15, A.8.24 / A.7 | 164.312.c.1 | Art. 12, Art. 15 | MEASURE-3 | s.41 | Art. 32 | s.19 | s.19 | Art. 25 |
| Access control — agent service principal | CC6.1, CC6.3 | A.5.15, A.8.3, A.8.2 | 164.308.a.4, 164.312.a.1 | Art. 14 (oversight) | MANAGE-1 | s.40 | Art. 29 | s.19 | s.24 | Art. 25 |
| Approval & supervision | CC5.1, PI1.4 | A.5.15, A.8.2 / 42001 8.2 | 164.312.d | Art. 14 (high-risk human oversight) | MEASURE-2 | s.40 | Art. 29 | s.71 (right to object/explain) | s.24 | Art. 26 |
| Kill-switch & containment | CC7.4, A1.3 | A.5.30, A.8.2 / 42001 10 | 164.308.a.7 | (operational; Art. 14 + post-market) | MANAGE-3 | s.41 | Art. 32 | s.19 | s.19 | Art. 25 |
| Incident management | CC7.3, CC7.4 | A.5.25, A.5.27 / 42001 10.1 | 164.308.a.6 | Art. 73 (serious incidents); Art. 20 (corrective) | MANAGE-4 | s.43 | Art. 28 | s.22 | s.23 | Art. 25 |
| Breach notification | n/a (controls only) | (process; A.5.25) | 164.408 (≤ 60 d; ≥ 500 immediate to HHS) | Art. 73 (15 d serious; 2 d critical) | n/a | s.43 (72 h) | Art. 28 (72 h) | s.22 (asap) | s.23 (immediate) | Art. 25 (48 h) |
| Sub-processor management | CC9.1, P6 | A.5.19, A.5.20 | 164.308.b.1, 164.504.e | Art. 25 (deployer); provider-chain | GOVERN-3 | s.40 | Art. 29 | s.20 | s.24 | Art. 26 |
| Data subject rights — access | P5 | A.5.34 | 164.524 | (where personal data; via GDPR) | GOVERN-5 | s.27 | Art. 19 | s.23 | s.16 | Art. 17 |
| Data subject rights — erasure | C1.2, P4 | A.5.34, A.8.10 | 164.502 + state law | (via GDPR Art. 17) | GOVERN-5 | s.31 | Art. 22 | s.24 | s.17 | Art. 18 |
| Data subject rights — explanation | P7 | A.5.34 | n/a | Art. 86 (high-risk explanation) | MEASURE-3 | (ODPC guidance) | (NDPC advisory) | s.71 | n/a (general) | (NCSA guidance) |
| Transparency & disclosure (AI involvement) | CC2.3 | A.6.3 / 42001 7.4 | n/a (operational) | Art. 50 (limited risk) | GOVERN-1 | (ODPC guidance) | (NDPC advisory) | s.18 | s.13 | Art. 16 |
| Cross-border transfer | (in privacy criteria) | A.5.34 | (Privacy Rule § 164.502; state law) | (via GDPR for personal data) | n/a | s.49 | Schedule | s.72 | s.19 | Art. 48 |
| DPIA / impact assessment | P3 | A.5.34 / 42001 6.1.4 | (privacy rule risk analysis) | Art. 27 (fundamental rights) | MAP | s.31 | Art. 28 | s.34 | s.21 | Art. 22 |
| Bias & protected-class outcomes | P7 | A.5.34 / 42001 8.3 | (Title VI/VII; ADA via state) | Art. 10 (data governance) Annex III | MEASURE-2 | (ODPC AI) | (NDPC AI) | s.71 | (general) | (general) |
| Training-data exclusion | C1, P6 | A.5.19 | 164.308.b.1 | Art. 10; Art. 53 (GPAI) | GOVERN-3 | (ODPC AI) | (NDPC AI) | s.20 | s.24 | Art. 26 |
| Memory & erasure SLA | C1.2, P4 | A.5.34, A.8.10 | 164.502 (return/destroy) | (via GDPR Art. 17) | GOVERN-5 | s.31 | Art. 22 | s.24 | s.17 | Art. 18 |
| Red-team & adversarial testing | CC4.1, PI1.2 | A.5.7, A.8.29 / 42001 8.3 | 164.308.a.1 | Art. 15 (accuracy/robustness/cyber); Art. 55 (GPAI systemic) | MEASURE-2 | (ODPC AI) | (NDPC AI) | s.19 | s.19 | Art. 25 |
| Change management | CC8.1 | A.8.9, A.8.32 / 42001 8 | 164.308.a.4 | Art. 14, Art. 16 (post-market) | GOVERN-2 | s.41 | Art. 32 | s.19 | s.19 | Art. 25 |
| Monitoring & SLI | CC4.1, A1.2 | A.8.16 / 42001 9 | 164.308.a.1 | Art. 72 (post-market) | MEASURE-1 | s.41 | Art. 32 | s.19 | s.19 | Art. 25 |
| Documentation retention | CC1.4 | A.5.36, A.5.37 | 164.316.b (6 y) | Annex IV (10 y after placing on market) | GOVERN-2 | s.34 (per category) | (Schedule) | s.14 | s.18 | Art. 21 |

## Divergent evidence notes

- **EU AI Act high-risk Annex IV** — technical documentation must include design, monitoring, post-market plan; cross-link to `15-ai-act-and-regulatory-compliance-doc` Annex IV index.
- **HIPAA admin-only constraint** — clinical PHI agents require BAA addendum clauses that are not implied by SOC 2 / ISO; explicit admin-only declaration required.
- **POPIA s.71** — automated decision-making restriction is stronger than GDPR Art. 22 in some respects; explicit explanation and objection rights for affected data subjects.
- **Uganda DPPA "immediate" breach** — does not specify hours; cite operational standard ≤ 24 h to PDPO.
- **Kenya residency expectation** — ODPC guidance favours local processing where feasible; document the residency posture.
- **Nigeria NDPC AI advisory (2024)** — specific guidance on automated processing; cite and apply where personal data is processed by agents.
- **EU AI Act serious-incident reporting (Art. 73)** — distinct from GDPR Art. 33; both apply when personal data is implicated; the addendum names both paths.
- **NIST AI RMF** — not regulatory but referenced by US sectoral regulators and procurement; map for trust-center use.

## Reuse summary — "one evidence, many regimes"

| Evidence artefact | Regimes satisfied |
|---------------------|---------------------|
| Hash-chain integrity report | SOC2 PI1.4 + ISO A.8.15/A.8.24 + HIPAA 164.312.c + AI Act Art. 12 + NIST MEASURE-3 + KE s.41 + NG Art. 32 + ZA s.19 + UG s.19 + RW Art. 25 |
| Kill-switch drill report | SOC2 CC7.4/A1.3 + ISO A.5.30 + HIPAA 164.308.a.7 + NIST MANAGE-3 |
| Approval event sample (signed) | SOC2 CC5.1/PI1.4 + ISO A.5.15/A.8.2 + HIPAA 164.312.d + AI Act Art. 14 + NIST MEASURE-2 + KE s.40 + NG Art. 29 + ZA s.71 + UG s.24 + RW Art. 26 |
| DPIA addendum | SOC2 P3 + ISO A.5.34 + HIPAA 164.502 + AI Act Art. 27 + NIST MAP + KE s.31 + NG Art. 28 + ZA s.34 + UG s.21 + RW Art. 22 |
| Sub-processor list + change log | SOC2 CC9.1/P6 + ISO A.5.19/A.5.20 + HIPAA 164.308.b.1 + AI Act Art. 25 + NIST GOVERN-3 + all regional DPAs |
| Red-team weekly results | SOC2 CC4.1/PI1.2 + ISO A.5.7/A.8.29 + AI Act Art. 15 + NIST MEASURE-2 |
| Audit-log retention configuration | SOC2 CC7.2 + ISO A.8.15 + HIPAA 164.312.b/164.316.b + AI Act Art. 12 + NIST MEASURE-3 + all regional DPAs |

## Update triggers

- Any change to a regime version, advisory, or guidance.
- Annual review.
- New sub-processor in a new jurisdiction.
- New agent feature with a different EU AI Act tier.
