# 05 — Crosswalk: AI Act ↔ ISO/IEC 42001 ↔ ISO/IEC 27090

This is the **canonical mapping table** linking each AI Act obligation to its ISO 42001 clauses, Annex A controls, ISO 27090 sections, and companion ISO standards. Use this when answering "which ISO controls satisfy art. X?" or "what evidence supports this article?".

**Coverage assessment overall**: ISO/IEC 42001 + 23894 + 42005 + 5259 + 27090 + 24029-2 collectively cover **80–85% of AI Act arts. 5–17, 26, 27, 50, 72, 73, 95** at the **process/control level**. Gaps requiring additional measures: art. 43 conformity assessment procedures (procedural, not management-system), art. 49 EU database registration (procedural), art. 53–55 GPAI-specific provisions (model cards, copyright policies, systemic-risk evaluations) — these need supplementary frameworks.

## 1. Master crosswalk (provider obligations)

| AI Act provision | Subject | Primary 42001 clauses | Primary Annex A controls | ISO 27090 sections | Companion standards | Coverage |
|------------------|---------|----------------------|-------------------------|-------------------|----------------------|----------|
| **Art. 5** | Prohibited practices | cl. 4.1 (context), 5.2 (AI policy) | A.2.2 (AI policy), A.5.4–A.5.5 (impact) | — | TR 24368 (ethics) | Process: detect via AISIA; treatment: avoid (no controls operationalize a prohibition) |
| **Art. 6 + Annex III** | High-risk classification | cl. 4.3 (scope), 6.1.4 (AISIA) | A.5.2 (AISIA process) | — | 22989, TR 5339 | Strong: AISIA documents classification rationale |
| **Art. 8** | Compliance with requirements | cl. 4.4, 8 (operation), 9 (perf eval), 10 (improvement) | All Annex A | — | All companions | Full lifecycle backbone |
| **Art. 9** | **Risk management system** | **cl. 6.1.2, 6.1.3, 8.2, 8.3** | A.2.2, A.6.1.2 | sect. 7 (risk modeling for AI) | **ISO/IEC 23894:2023** (depth standard) | Strong: 23894 is harmonised candidate |
| **Art. 10** | **Data and data governance** | cl. 7.1 (resources), 8.1 | A.4.3, A.7.2, A.7.3, A.7.4, A.7.5, A.7.6 | sect. 4.1 (data hygiene), supply-chain (LLM03) | **ISO/IEC 5259-1 to -5**, **ISO/IEC 8183**, TR 24027 (bias) | Strong: 5259 series is depth standard; 27090 covers data security |
| **Art. 11 + Annex IV** | **Technical documentation** | cl. 7.5 (documented info), 8.1 | A.4.2, A.6.2.3, A.6.2.7 | sect. 9 (output template) | **ISO/IEC 5338** (lifecycle), TR 24028 | Strong: A.6.2.7 is direct counterpart |
| **Art. 12** | **Record-keeping (logs)** | cl. 7.5 (documented info), 9.1 (monitoring) | **A.6.2.8** (event logs) | sect. 4.6 (operational logging) | ISO/IEC 27002 cl. 8.15 (baseline logging) | Strong |
| **Art. 13** | **Transparency to deployers** | cl. 7.4 (communication) | A.8.2, A.8.5, A.6.2.7 | sect. 6 (LLM disclosure) | — | Strong |
| **Art. 14** | **Human oversight** | cl. 5.3 (roles), 7.2 (competence), 7.3 (awareness), 8.1 | **A.9.2, A.9.3, A.9.4**, A.6.2.5, A.6.2.6 | sect. 4.5 (human-in-the-loop for agentic) | TR 24028 | Strong: A.9 family is direct |
| **Art. 15(1)(3)** | **Accuracy** | cl. 6.2 (objectives), 9.1 | A.6.2.4 (V&V) | sect. 5.1 (eval-set integrity) | **ISO/IEC TS 4213**, **25059**, **24029-1** | Strong: 4213 + 25059 are depth standards |
| **Art. 15(4)** | **Robustness** | cl. 8.1, 9.1 | A.6.2.4, A.6.2.6 | sect. 4.2 (training-time defenses), 5.2 | **ISO/IEC 24029-2** (depth), 24029-3 (forthcoming) | Strong: 24029-2 is harmonised candidate |
| **Art. 15(5)** + Recital 76 | **Cybersecurity** | cl. 8.1, A.6.2.4 | A.6.2.4, A.6.2.6, A.10.3 (suppliers) | **All sections** (whole standard) | **ISO/IEC 27090:2025** (depth), 27001/27002 baseline, NIST AI 100-2, OWASP LLM Top 10 | Strong: 27090 is depth standard for Recital 76 named threats |
| **Art. 16** | Provider obligations (general) | cl. 5 (leadership), 8, 10 | All Annex A | — | — | Strong: an AIMS satisfies art. 16 |
| **Art. 17** | **Quality Management System** | **All clauses 4–10** (the AIMS *is* the QMS for AI) | All Annex A | — | ISO 9001 (integrable via Annex SL) | **Strong: 42001 = art. 17 QMS, when scope appropriate** |
| **Art. 18** | Documentation kept 10 years | cl. 7.5 (documented info — retention) | A.4.2 (resource doc) | — | — | Procedural: 10-year retention requires explicit doc-control policy |
| **Art. 19** | Logs kept ≥6 months | cl. 7.5 + 9.1 | A.6.2.8 | — | ISO 27002 cl. 8.15 | Procedural: log-retention policy |
| **Art. 20** | Corrective actions | cl. 10.2 (NC + CA) | A.8.4 (incident comm) | sect. 4.6 (incident response) | — | Strong: 10.2 is the direct hook |
| **Art. 21** | Cooperation with authorities | cl. 5.1 (leadership), 7.4 (communication) | A.3.3 (reporting concerns) | — | — | Procedural |
| **Art. 22** | Authorised representatives (third-country providers) | cl. 4.2 (interested parties) | A.3.2 (roles), A.10.2 (allocation) | — | — | Procedural: contract + delegation structure |
| **Art. 23** | Importer obligations | cl. 4.2, 8 | A.10.3 (suppliers) | — | — | Procedural |
| **Art. 24** | Distributor obligations | cl. 4.2, 8 | A.10.3 (suppliers) | — | — | Procedural |
| **Art. 25** | Substantial modification → provider role flip | cl. 6.3 (planning of changes), 8.4 (operational AISIA) | A.5.2 (AISIA process — re-execute) | — | — | Strong: substantial-modification trigger maps to clause 6.3 + re-AISIA |

## 2. Deployer obligations crosswalk

| AI Act provision | Subject | Primary 42001 clauses | Primary Annex A controls | ISO 27090 sections | Companion standards | Coverage |
|------------------|---------|----------------------|-------------------------|-------------------|----------------------|----------|
| **Art. 26(1)** | Use per instructions | cl. 8.1 | A.9.2, A.9.4 | — | — | Strong |
| **Art. 26(2)** | Assign trained humans | cl. 5.3, 7.2 | A.3.2 (roles), A.9.2 | — | — | Strong |
| **Art. 26(3)** | Input data relevance | cl. 8.1 | A.7.4 (data quality) | sect. 4.1 (validation) | 5259-2 | Strong |
| **Art. 26(4)** | Monitor + suspend on risk | cl. 9.1 | A.6.2.6 (operation/monitoring) | sect. 4.6 (operational) | — | Strong |
| **Art. 26(5)** | Retain logs ≥6 months | cl. 7.5 | A.6.2.8 | — | ISO 27002 cl. 8.15 | Procedural |
| **Art. 26(6)** | Inform workers' reps | cl. 7.4 | A.8.5 (info for parties) | — | — | Procedural |
| **Art. 26(7)** | Public authorities register use | — | — | — | — | Procedural (EU database) |
| **Art. 26(8)** | DPIA coordination | cl. 6.1.4 + 8.4 (AISIA) | A.5.2, A.5.4 | — | **ISO/IEC 42005** (AISIA depth) | Strong: AISIA + DPIA can be combined |
| **Art. 26(9)** | Judicial auth for LE/migration/justice | — | — | — | — | Procedural (national law) |
| **Art. 26(10)** | Right to explanation interface | cl. 7.4, 8.1 | A.8.2, A.8.5 | — | TR 24028 | Strong |
| **Art. 26(11)** | Cooperate with surveillance | cl. 5.1, 7.4 | A.3.3 | — | — | Procedural |
| **Art. 26(12)** | Inform persons exposed (emotion/biometric) | cl. 7.4 | A.8.5 | — | — | Procedural |
| **Art. 27** | **FRIA** | **cl. 6.1.4, 8.4** | **A.5.2, A.5.3, A.5.4, A.5.5** | — | **ISO/IEC 42005:2025** (depth) | Strong: AISIA + 42005 = FRIA when contextualized |

## 3. Transparency, post-market, GPAI crosswalk

| AI Act provision | Subject | 42001 clauses | Annex A | 27090 | Companions | Coverage |
|------------------|---------|---------------|---------|-------|-----------|----------|
| **Art. 50** | Transparency for chatbots, generative content, deepfakes, public-interest text | cl. 7.4, 8.1 | A.8.2, A.8.4, A.8.5 | sect. 4.5 (output watermarking), sect. 6 (LLM) | C2PA spec, ISO/IEC TS 22237 (watermarking emerging) | Partial: watermarking technical needs supplementary |
| **Art. 53** | GPAI provider obligations | cl. 4 (context), 7.5 (doc), 8 | A.4.2, A.6.2.7, A.8.2, A.8.5, A.10.3, A.10.4 | sect. 6 (foundation model annex) | **GPAI Code of Practice** (published 2025-07-10; adequacy 2025-08-01); training-data-summary template (2025-07-24); ML-BOM | Partial — the Code of Practice is the operative instrument |
| **Art. 54** | Authorised reps for GPAI | cl. 4.2 | A.10.2 | — | — | Procedural |
| **Art. 55** | Systemic-risk GPAI obligations | cl. 6.1.2, 6.1.4, 8.4, 9.1 | A.5.5 (societal), A.6.2.4 (V&V), A.6.2.6 | **All sections — esp. red teaming, supply chain** | NIST AI 100-2, MITRE ATLAS, **AI Safety Institute frameworks** | Strong on security; procedural on systemic-risk eval |
| **Art. 61** | Conformity assessment institutional | cl. 9.2 (internal audit), 9.3 (mgmt review), 10.2 | — | — | **ISO/IEC 17021-1, ISO/IEC 42006** | Strong via 42006 |
| **Art. 72** | Post-market monitoring | cl. 9.1, 10.1 | A.6.2.6, A.8.3 (external reporting) | sect. 4.6 (operational) | — | Strong |
| **Art. 73** | Serious incident reporting | cl. 10.2 | **A.8.3, A.8.4** | sect. 4.6 (incident response) | — | Strong |
| **Art. 86** | Right to explanation | cl. 7.4 | A.8.5 | — | TR 24028 | Strong |
| **Art. 95** | Codes of conduct (voluntary minimal-risk) | cl. 5.2 (AI policy) | A.2.2 | — | — | Strong: code of conduct = AIMS-derived policy |
| **Art. 99** | Sanctions | — | — | — | — | Out of scope (institutional) |

## 4. Quick-reference compact table (one-line crosswalks)

For fast lookup. Use the master tables above for nuance.

```
art. 5         → 42001 cl.4.1, 5.2 + A.2.2; treatment = avoid
art. 6         → 42001 cl.6.1.4 + A.5.2; AISIA documents classification
art. 9 RMS     → 42001 cl.6.1.2-3, 8.2-3 + A.2.2, A.6.1.2 + ISO 23894
art. 10 data   → 42001 A.4.3, A.7.2-7.6 + ISO 5259 series
art. 11 doc    → 42001 cl.7.5 + A.4.2, A.6.2.3, A.6.2.7
art. 12 logs   → 42001 A.6.2.8 + ISO 27002 cl.8.15
art. 13 trans  → 42001 A.8.2, A.8.5, A.6.2.7
art. 14 over   → 42001 cl.5.3, 7.2 + A.9.2-9.4, A.6.2.5-6
art. 15 acc    → ISO TS 4213 + ISO 25059 (24029-1)
art. 15 rob    → ISO 24029-2
art. 15 cyb    → ISO 27090 (whole) + 27001/27002 baseline + Recital 76 mapping
art. 17 QMS    → ISO 42001 entire AIMS
art. 26 dep    → 42001 A.9 family + A.5 (FRIA via 42005)
art. 27 FRIA   → 42001 cl.6.1.4, 8.4 + A.5 + ISO 42005
art. 50 trans  → 42001 A.8 + C2PA + watermarking techniques
art. 51-55 GPAI → Code of Practice + ML-BOM + 27090 sect.6
art. 72 PMM    → 42001 cl.9.1, 10.1 + A.6.2.6, A.8.3
art. 73 inc    → 42001 cl.10.2 + A.8.3, A.8.4 + 27090 sect.4.6
art. 86 explain → 42001 A.8.5 + TR 24028
```

## 5. Statement of Applicability (SoA) implications

When drafting the AIMS Statement of Applicability for a high-risk AI system provider, the **38 Annex A controls** typically classify as:

| SoA classification | Control count | Rationale |
|--------------------|---------------|-----------|
| **Implemented** | ~32–36 | Most controls map directly to AI Act obligations and are mandatory by regulatory necessity |
| **Implemented but partial** | ~2–4 | Often A.10.3 supplier (depending on supply chain complexity), A.4.5 environmental footprint (if not yet measured) |
| **Not applicable** | ~0–2 | Very rare for high-risk providers. Could include A.10.4 customers if no end-user disclosure (B2B-only no-exposure model) — but this is the exception |
| **Excluded with justification** | 0 | Excluding any A.5–A.9 control on a high-risk system is essentially incompatible with AI Act conformity |

For **deployer-only** scopes, A.6 (lifecycle) and A.7 (data) may have reduced scope (deployer doesn't develop or train), but A.5 (impacts), A.8 (information for parties), A.9 (use), A.10 (third parties) are core.

For **GPAI providers** (especially systemic-risk), all 38 controls apply, and the SoA must additionally address Code-of-Practice obligations under arts. 53–55.

## 6. Conformity-evidence index

When a high-risk provider needs to demonstrate art. 8–15 conformity, this is the typical evidence chain:

| Art. essential req. | Evidence artefact | Where in AIMS |
|---------------------|--------------------|---------------|
| Art. 9 RMS | Risk register; risk treatment plan; residual-risk acceptance | cl. 6.1 outputs + 8.2-3 records |
| Art. 10 data | Datasheet (per 5259-1 example), bias evaluation report, data quality measures, provenance log, data acquisition contracts | A.7 records |
| Art. 11 + Annex IV | Annex IV technical file (sectioned); model card; system card; data card | A.4.2, A.6.2.3, A.6.2.7 |
| Art. 12 logs | Logging design spec; log retention policy; sample log dump | A.6.2.8 |
| Art. 13 transparency | Instructions for use document (per art. 13(3) checklist) | A.8.2 |
| Art. 14 oversight | Oversight measures design; operator training records; intervention/override procedures; automation-bias awareness materials | A.9, A.6.2.5-6 |
| Art. 15 accuracy | Test plan, test report, declared metrics, ISO TS 4213 alignment | A.6.2.4 |
| Art. 15 robustness | Robustness test plan + report (ISO 24029-2); adversarial-robustness report; feedback-loop mitigation design | A.6.2.4, A.6.2.6 |
| Art. 15 cybersecurity | Threat model (per ISO 27090 template); control implementation evidence; red-team report; incident response playbook; ML-BOM; supplier security review | A.6.2.4, A.6.2.6, A.10.3 |
| Art. 17 QMS | AIMS scope statement; AI policy; SoA; internal audit reports; management review minutes; (ideally) ISO 42001 certification | All clauses + Annex A |

## 7. The presumption-of-conformity ladder

What level of legal protection does each instrument confer?

| Instrument | Protection conferred | Status (July 2026) |
|------------|---------------------|---------------|
| **Harmonised standard cited in OJEU** (per art. 40) | **Presumption of conformity** with corresponding essential requirements — strongest | **None cited yet.** CEN-CENELEC adopted acceleration measures (Oct 2025: direct publication after positive Enquiry vote); key JTC 21 deliverables — **prEN 18228** (risk management, art. 9), **prEN 18284** (data quality & governance, art. 10) — targeted for Q4 2026. The 2026 AI Omnibus deferred the high-risk deadline to 2027-12-02 largely because these standards were late |
| **Common specifications** adopted by Commission (per art. 41) | Presumption of conformity (where used) | Not yet adopted as of July 2026 |
| **EN ISO/IEC 42001 / 23894 / 5259 / 24029-2 / 42005** (forthcoming European adaptations) | Will trigger art. 40 once cited in OJEU | Drafting / adoption phase under JTC 21 |
| **ISO/IEC 42001 certification** | **Strong evidentiary support**; **due diligence demonstration**; streamlines conformity assessment but does not by itself satisfy art. 8–15 | Available now; mature |
| **ISO/IEC 27090, 24029-2, TS 4213, 5259, 23894, 42005 alignment** (without certification) | **Substantive evidence** that essential requirements are addressed; foundation for notified-body conformity assessment | Available now |
| **NIST AI RMF, ISO 23894, internal frameworks** | Useful internal practice; less weight in EU conformity assessment than ISO/EN equivalents | Use as supplementary |

**Operational guidance**: until OJEU citations land, build the AIMS to **EN-equivalent** standards (effectively, current ISO standards) so that when EN versions are cited, the gap to certification is minimal. Do not wait for OJEU citations to start.
