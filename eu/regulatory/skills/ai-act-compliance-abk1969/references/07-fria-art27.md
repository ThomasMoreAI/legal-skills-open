# 07 — Fundamental Rights Impact Assessment (AI Act art. 27)

The FRIA is **deployer-bound** — not provider-bound — and is the primary mechanism by which the AI Act extends accountability beyond the supplier to the operational user. It is **distinct from but coordinated with** the GDPR DPIA (art. 35) and the AIMS-level AISIA (ISO 42001 cl. 6.1.4 + ISO 42005).

## 1. Who must conduct a FRIA

Three trigger conditions (art. 27(1)) — meet **any** of them:

1. The deployer is a **body governed by public law** AND deploys an Annex III high-risk AI system (any Annex III §1–§8 use case).
2. The deployer is a **private entity providing public services** AND deploys an Annex III high-risk AI system.
3. The deployer is **any** entity (public or private) deploying high-risk AI under:
   - Annex III §5(b) — **creditworthiness/credit-scoring** (except detecting financial fraud)
   - Annex III §5(c) — **risk assessment and pricing in life and health insurance**

**Excluded**: deployers of Annex I (product-safety) high-risk AI are not bound by FRIA — only Annex III triggers it.

**Timing**: FRIA must be performed **prior to first use** of a high-risk AI system, and updated if any of the elements change (art. 27(2)).

## 2. What the FRIA must cover (art. 27(1))

Six required elements:

(a) **Description of the deployer's processes** in which the system will be used in line with intended purpose

(b) **Description of the period of time and frequency** in which each high-risk AI system is intended to be used

(c) **Categories of natural persons and groups likely to be affected** by use in the specific context

(d) **Specific risks of harm** likely to impact the categories of natural persons or groups identified per (c), taking into account the information given by provider per art. 13

(e) **Description of the implementation of human oversight measures**, according to the instructions for use

(f) **Measures to be taken in case of materialisation of these risks**, including arrangements for internal governance and complaint mechanisms

## 3. Notification and integration

**Notification (art. 27(3))**: deployer notifies the **market surveillance authority** of the FRIA's results, by submitting the filled-out template referred to in art. 27(5) (Commission to provide template via implementing act).

**DPIA coordination (art. 27(4))**: where any of the obligations laid down in this article have already been met through the DPIA conducted under art. 35 GDPR or art. 27 LED, the FRIA referred to in this article shall **complement that DPIA**.

In practice: DPIA covers personal-data processing risks; FRIA covers the broader fundamental-rights surface (non-discrimination, dignity, freedom of expression, access to justice, social rights, etc.). They overlap on data-protection-as-fundamental-right. A coordinated FRIA + DPIA produces a single artefact addressing both regimes.

## 4. ISO 42001 + ISO 42005 alignment

The FRIA maps directly onto the AIMS impact-assessment family:

| AI Act art. 27 element | ISO 42001 anchor | ISO 42005 elaboration |
|------------------------|------------------|------------------------|
| (a) Deployer's processes | cl. 4.1 (context), 4.3 (scope), A.9.4 (intended use) | clause 5 (context establishment) |
| (b) Period and frequency of use | A.9.4 (intended use) | clause 5 (context) |
| (c) Categories of affected persons | cl. 4.2 (interested parties), A.5.4 (impact on individuals) | clause 6 (scope of assessment) |
| (d) Specific risks of harm | cl. 6.1.2 (AI risk assessment), 6.1.4 (AISIA), A.5.2-A.5.5 | clause 7 (impact identification + analysis) |
| (e) Human oversight implementation | cl. 5.3 (roles), 7.2 (competence), A.9.2 (responsible use processes) | clause 8 (treatment) |
| (f) Mitigation + governance + complaint | cl. 8.4 (operational AISIA), 10.2 (NC + CA), A.3.3 (reporting concerns), A.8.4 (incident comm) | clause 9 (treatment + monitoring) |

**ISO/IEC 42005:2025** is the depth standard for AISIA. It elaborates clause 6.1.4 + 8.4 of 42001 with:
- Methodology guidance (qualitative, quantitative, hybrid)
- Stakeholder engagement requirements
- Documentation templates
- Continuous re-assessment triggers
- Integration with risk management (ISO 23894) + AIMS

A FRIA following 42005 methodology automatically satisfies AI Act art. 27(1)(a)–(f) + art. 27(2) update requirements.

## 5. FRIA template (art. 27 + 42005-aligned)

```
FUNDAMENTAL RIGHTS IMPACT ASSESSMENT (FRIA)
Per AI Act art. 27 + ISO/IEC 42005:2025

═══════════════════════════════════════════════════════════════
0. ADMINISTRATIVE
═══════════════════════════════════════════════════════════════
Deployer organisation:        <name, address, registration>
Deployer role:                <public body | private public-service | Annex III §5(b) | §5(c)>
AI system name:               <as registered>
AI system EU database ID:     <art. 49 registration ID>
Provider:                     <name>
FRIA reference number:        FRIA-<YYYY>-<deployer>-<system>-vN
FRIA version:                 <semver>
FRIA performed by:            <names + roles>
FRIA approved by:             <name + title> on <date>
Effective from:               <YYYY-MM-DD>
Coordinated DPIA reference:   <DPIA-YYYY-...> (per art. 27(4))
Market surveillance authority notified: <yes/no, date, ref>

═══════════════════════════════════════════════════════════════
1. DEPLOYER'S PROCESSES (art. 27(1)(a))
═══════════════════════════════════════════════════════════════
1.1 Process(es) in which AI system used:
1.2 Decision points where AI output influences action:
1.3 Workflow integration (mermaid diagram or narrative):
1.4 Alignment with intended purpose declared by provider (art. 13):
1.5 Departures from intended purpose (none should be present):

═══════════════════════════════════════════════════════════════
2. PERIOD & FREQUENCY (art. 27(1)(b))
═══════════════════════════════════════════════════════════════
2.1 Operational period:           <e.g., 2026-09 onwards, indefinite>
2.2 Daily/weekly volume:          <inferences per day, peak/avg>
2.3 Coverage:                     <% of decisions in scope, % cases handled by AI>
2.4 Hours of operation:           <24/7, business hours, on-demand>
2.5 Geographical scope:           <jurisdictions, regions>

═══════════════════════════════════════════════════════════════
3. AFFECTED PERSONS AND GROUPS (art. 27(1)(c))
═══════════════════════════════════════════════════════════════
3.1 Direct subjects of decisions:
    - Profile (age, status, role):
    - Volume:
    - Vulnerability factors:
3.2 Indirect affected persons:
3.3 Specific vulnerable groups:
    - Children (<18):
    - Persons with disabilities:
    - Migrants/refugees:
    - Specific socio-economic situation:
    - Other protected categories under EU law:
3.4 Protected characteristics in scope (per Charter of Fundamental Rights of the EU):
    [ ] Dignity (Art. 1)
    [ ] Right to life (Art. 2)
    [ ] Physical/mental integrity (Art. 3)
    [ ] Privacy (Art. 7)
    [ ] Data protection (Art. 8)
    [ ] Freedom of expression (Art. 11)
    [ ] Non-discrimination (Art. 21)
    [ ] Children's rights (Art. 24)
    [ ] Workers' rights (Art. 27, 31)
    [ ] Right to good administration (Art. 41)
    [ ] Right to effective remedy (Art. 47)
    [ ] Other:

═══════════════════════════════════════════════════════════════
4. SPECIFIC RISKS OF HARM (art. 27(1)(d))
═══════════════════════════════════════════════════════════════
For each affected group × harm dimension, document:

| Group | Harm dimension | Plausible scenario | Likelihood | Severity | Reversibility | Combined risk |
|-------|----------------|--------------------|-----------|----------|----------------|----------------|
| ...   | Discrimination | ...                | H/M/L     | H/M/L    | rev/irrev      | H/M/L          |
| ...   | Privacy        | ...                | ...       | ...      | ...            | ...            |
| ...   | Autonomy       | ...                | ...       | ...      | ...            | ...            |
| ...   | Access to remedy | ...              | ...       | ...      | ...            | ...            |
| ...   | Dignity        | ...                | ...       | ...      | ...            | ...            |
| ...   | Other          | ...                | ...       | ...      | ...            | ...            |

Information from provider art. 13 instructions for use considered:
- Declared accuracy by group:
- Declared limitations:
- Foreseeable circumstances of risk:

═══════════════════════════════════════════════════════════════
5. HUMAN OVERSIGHT IMPLEMENTATION (art. 27(1)(e))
═══════════════════════════════════════════════════════════════
5.1 Oversight model: <human-in-the-loop | on-the-loop | over-the-loop>
5.2 Oversight roles:
    - Operator role:
    - Reviewer role:
    - Escalation owner:
5.3 Competence requirements:
5.4 Training delivered:
5.5 Override capability:
    - How to override:
    - Audit of overrides:
5.6 Stop function:
    - How to invoke:
    - Recovery procedure:
5.7 Automation-bias mitigations:
5.8 Coverage rate:
    - % decisions reviewed:
    - Random sampling protocol:

═══════════════════════════════════════════════════════════════
6. MITIGATION MEASURES (art. 27(1)(f))
═══════════════════════════════════════════════════════════════
6.1 Pre-deployment measures:
    - Adjustments to deployer's processes:
    - Input data quality controls:
    - Tested fallback (deterministic rule, manual review):
    
6.2 Operational measures:
    - Monitoring KPIs:
    - Drift detection:
    - Bias monitoring per group:
    - Performance thresholds for suspension:

6.3 Internal governance:
    - AI governance committee:
    - Reporting line:
    - Periodic review (frequency, owner):

6.4 Complaint mechanism:
    - Channel for affected persons:
    - SLA for response:
    - Escalation to provider/authority:
    - Right to explanation interface (per art. 86):

6.5 Incident response:
    - Trigger thresholds:
    - Notification to provider (art. 26(4)):
    - Notification to authority for serious incidents (art. 73):
    - Notification to affected persons (case-by-case):

═══════════════════════════════════════════════════════════════
7. RESIDUAL RISK ACCEPTANCE
═══════════════════════════════════════════════════════════════
After mitigations, the residual fundamental-rights risks have been
evaluated as <ACCEPTABLE / ACCEPTABLE WITH CONDITIONS / NOT ACCEPTABLE>.

Acceptance signature: <name, role, date, signature>
Conditions (if applicable):
Re-assessment trigger conditions:
    - Significant change to use:
    - Performance threshold breach:
    - Provider issues new version:
    - Regulatory change:
    - Periodic review (every <X> months):

═══════════════════════════════════════════════════════════════
8. NOTIFICATION TO MARKET SURVEILLANCE AUTHORITY (art. 27(3))
═══════════════════════════════════════════════════════════════
Authority notified:           <competent national authority>
Notification date:            <YYYY-MM-DD>
Template version used:        <Commission template ID>
Notification reference:       <ref>
Authority response received:  <yes/no, date, content>

═══════════════════════════════════════════════════════════════
9. DPIA COORDINATION (art. 27(4))
═══════════════════════════════════════════════════════════════
DPIA reference:               <DPIA-YYYY-...>
DPIA scope:                   <personal data processing activities covered>
Overlap with FRIA:            <data protection rights covered jointly>
Joint or separate document:   <combined / separate but cross-referenced>
DPO consulted:                <name, date>

═══════════════════════════════════════════════════════════════
10. SUPPORTING MATERIALS
═══════════════════════════════════════════════════════════════
- Provider's instructions for use (art. 13)
- Provider's Annex IV technical documentation (relevant excerpts)
- Internal policies (AI policy, oversight procedures, complaint procedure)
- Training materials for oversight personnel
- Stakeholder engagement records (per ISO 42005 cl. 6)
- Test reports (provider-supplied + deployer-conducted on input data)
```

## 6. Triggering re-assessment (art. 27(2))

The FRIA must be updated when **any of the elements change**. Operationalize as triggers:

| Trigger | Re-assessment scope |
|---------|--------------------|
| Provider releases new version with changed performance characteristics | Full re-assessment |
| Deployer's process changes (new decision point, new affected group) | Sections 1, 3, 4 |
| Frequency or coverage changes materially | Section 2 |
| Performance KPI breaches threshold (drift, bias) | Sections 4, 6 |
| Affected-group composition changes | Sections 3, 4 |
| Regulatory change (e.g., delegated act under art. 7) | Full re-assessment |
| Periodic (recommended **annual** at minimum) | Full re-assessment |
| Substantial modification by deployer (art. 25 — flips role to provider) | Full re-assessment + provider obligations attach |

## 7. Common pitfalls

1. **Treating FRIA as a privacy compliance task delegated to the DPO.** FRIA is broader than DPIA. Charter rights covered include non-discrimination, dignity, access to remedy, workers' rights — not solely privacy/data protection. Engage HR, legal, line-of-business, AI ethics in addition to DPO.

2. **One-shot at deployment without update process.** Art. 27(2) requires update on change. Without an update governance, the FRIA goes stale and the deployer is non-compliant.

3. **Missing notification to market surveillance authority.** Art. 27(3) is mandatory. Some deployers complete the FRIA but never submit to the authority.

4. **Confusing FRIA with the AIMS AISIA.** The AIMS AISIA (ISO 42001 cl. 6.1.4 + 42005) is the deployer's *internal management* artefact for any AI system. The FRIA is the *AI Act-specific* artefact for *certain* high-risk uses by *certain* deployers. The AISIA should serve as the substrate from which a FRIA is generated when triggers fire — not duplicated work.

5. **No stakeholder engagement.** ISO 42005 elevates stakeholder engagement (cl. 6) as a requirement; the AI Act art. 27 is silent but engagement is the only credible way to identify "categories of natural persons likely to be affected" (art. 27(1)(c)) and "specific risks of harm" (art. 27(1)(d)). Conduct workshops, surveys, civil-society consultation when appropriate.

6. **Failing to coordinate with workplace consultation.** If deployer is an employer using AI for HR/management decisions (Annex III §4), additional obligations flow from art. 26(6) (inform workers' representatives) — surface this in FRIA section 5 + section 6.3.

## 8. Output template (compact, when scope unclear)

When asked "do we need a FRIA?":

```
FRIA APPLICABILITY ASSESSMENT
─────────────────────────────────────────
Deployer role:        <public body | private public-service provider | private — neither>
AI system tier:       <high | other>
Annex III subcase:    <§1 ... §8 | not Annex III>
Special triggers:     [ ] §5(b) credit
                      [ ] §5(c) life/health insurance

DECISION:
  IF Annex III high-risk AND (public-body OR private-public-service):
    → FRIA REQUIRED
  IF §5(b) credit OR §5(c) insurance, ANY deployer:
    → FRIA REQUIRED
  ELSE (Annex I high-risk, or non-high-risk, or non-triggering Annex III for private non-public-service deployer):
    → FRIA NOT REQUIRED under art. 27.
    Note: AIMS AISIA (ISO 42001 cl. 6.1.4) is still recommended best practice;
    DPIA per art. 35 GDPR may apply independently.

NEXT STEPS (if required):
  1. Schedule FRIA workshop (sponsor, sponsor's manager, line-of-business, DPO, AI ethics, legal)
  2. Coordinate with DPIA per art. 27(4)
  3. Use template in §5 of this reference
  4. Submit notification to market surveillance authority per art. 27(3)
  5. Establish update triggers per art. 27(2)
```
