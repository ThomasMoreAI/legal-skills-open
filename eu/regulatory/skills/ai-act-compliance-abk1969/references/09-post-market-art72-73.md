# 09 — Post-Market Monitoring & Serious Incident Reporting (AI Act art. 72, 73)

Articles 72 (post-market monitoring, "PMM") and 73 (serious incident reporting) anchor the **operational lifecycle** of high-risk AI systems. Both flow naturally from ISO 42001 cl. 9 (performance evaluation) and cl. 10 (improvement), and tie together the otherwise-separate compliance domains: risk management (art. 9), data governance (art. 10), accuracy/robustness/cybersecurity (art. 15), and human oversight (art. 14).

> **Commission guidance status**: the Commission published **draft guidance on reporting serious incidents under art. 73, together with a draft reporting template**, on **2025-09-26** (public consultation closed 2025-11-07). Align the incident playbook below with that template; track final adoption under art. 73(7).

## 1. Post-market monitoring (art. 72)

### 1.1 What it is

Providers shall **establish and document a post-market monitoring system** in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system (art. 72(1)).

The PMM system shall **actively and systematically collect, document and analyse relevant data** which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which **allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2** (arts. 8–15) (art. 72(1)).

In short: PMM is the **continuous-conformity loop**.

### 1.2 PMM Plan

Providers must draw up a **post-market monitoring plan**, which is **part of the technical documentation** referred to in Annex IV §9 (art. 72(2)).

The Commission shall adopt an implementing act detailing the form and elements of the PMM plan (art. 72(3)). As of July 2026 this implementing act is still in development.

The PMM plan typically contains:

| Section | Content |
|---------|---------|
| **Purpose & scope** | What this PMM covers (system, version range, geographies) |
| **KPIs** | Performance indicators monitored; thresholds for normal / anomalous / critical |
| **Data sources** | Logs (art. 12), deployer reports (art. 26(4)), complaint channel, drift detection telemetry, social signals, regulatory bulletins |
| **Frequency** | Real-time / daily / weekly / monthly / on-demand for each metric |
| **Roles & responsibilities** | Who collects, who analyses, who escalates, who decides corrective action |
| **Drift detection methodology** | Statistical tests, baselines, alerting thresholds (per ISO 27090 sect. 4.6 + ISO 24029 robustness) |
| **Bias monitoring** | Per-group performance tracking (per ISO TR 24027 + AI Act art. 10(2)(f)(g)) |
| **Cybersecurity monitoring** | AI-specific incident detection per ISO 27090 — adversarial query detection, extraction-rate spikes, jailbreak attempts |
| **Feedback into RMS** | How PMM signals trigger re-execution of art. 9 risk management cycle |
| **Escalation matrix** | When to inform deployers (art. 16); when to suspend/recall (art. 20); when to report serious incident (art. 73) |
| **Reporting format** | Internal reports + format for deployer-facing communications |
| **Review cycle** | Periodic full review of PMM plan itself |

### 1.3 Sources of post-market data (art. 72(2))

(a) Data on the use of the AI system received from deployers, where applicable
(b) Data acquired through other sources

In practice:

- **Deployer-provided** (art. 26(4) flow): incident reports, performance feedback, complaints
- **Logs** (art. 12 + 19, retained ≥6 months)
- **Internal monitoring** of provider's own infrastructure (drift, error rates, latency, etc.)
- **External signals**: social media, security disclosure platforms, news, academic publications
- **Regulatory bulletins**: AI Office, national authorities, EUR-Lex

The Navigator's MCP servers (`server/mcp/eurlex-server.ts`, `cnil-server.ts`, `ec-aioffice-server.ts`) are an example of an automated regulatory-bulletin pipeline feeding PMM.

### 1.4 ISO 42001 anchors

| PMM activity | ISO 42001 anchor |
|--------------|-------------------|
| Continuous monitoring | cl. 9.1 (monitoring, measurement, analysis, evaluation) |
| Internal audit | cl. 9.2 |
| Management review | cl. 9.3 |
| Operation + monitoring control | A.6.2.6 |
| External reporting | A.8.3 |
| Communication of incidents | A.8.4 |
| Continual improvement | cl. 10.1 |
| Nonconformity & corrective action | cl. 10.2 |

## 2. Serious incident reporting (art. 73)

### 2.1 Definition (art. 3(49))

**'Serious incident'** means an incident or malfunctioning of an AI system that directly or indirectly leads to any of the following:

(a) The death of a person, or serious harm to a person's health
(b) A serious and irreversible disruption of the management or operation of critical infrastructure
(c) The infringement of obligations under Union law intended to protect fundamental rights
(d) Serious harm to property or the environment

### 2.2 Reporting obligation (art. 73)

**Providers** shall report any serious incident to the **market surveillance authorities** of the Member States where that incident occurred (art. 73(1)).

**Reporting deadlines** (art. 73(2)–(4)):

| Incident type | Deadline (latest) |
|---------------|-------------------|
| **Default** | **15 days** after the provider (or where applicable, the deployer) has established the causal link between the AI system and the serious incident, OR a reasonable likelihood thereof |
| **Widespread infringement** OR **serious and irreversible disruption of critical infrastructure** (incident type (b) or (c) of definition) | **2 days** |
| **Death of a person** | **10 days** (where evidence is available) |

The report shall include all information necessary, including likelihood and severity of harm, taking into account the criteria referred to in art. 7(2) (the criteria the Commission uses for adding new use cases to Annex III).

### 2.3 Investigation (art. 73(5)(6))

Following the reporting, the provider shall, **without delay**, perform necessary investigations and:
- Take appropriate corrective measures
- Cooperate with competent authorities and any relevant national authorities for sectoral specifics

The provider shall **NOT** perform any investigation that involves alteration of the AI system in a manner that may affect any subsequent evaluation of the causes, **prior to informing the competent authorities** of such action.

### 2.4 GDPR / LED interaction

The serious-incident reporting under art. 73 is **without prejudice** to other reporting obligations:
- GDPR art. 33–34 (personal data breach notification: 72h to supervisory authority + affected persons if high risk)
- LED equivalent
- NIS2 (network and information security incident notification)
- DORA (Digital Operational Resilience Act for finance)
- Sector-specific (medical devices, civil aviation, automotive)

For a single underlying event, multiple reports may be required to multiple authorities under multiple legal bases. **Coordinate** them; do not assume one notification covers all.

### 2.5 Deployer flow into provider

Per art. 26(4), if a deployer has reason to consider that use of an AI system may result in serious risk, **suspend use** and **inform the provider/distributor and competent authority without undue delay**. The provider then assesses whether art. 73 applies and reports.

For Annex III §1 (biometric ID), §6 (law enforcement), §7 (migration/border), §8 (justice/democratic), the deployer may be a public authority bound by **its own** notification regime to oversight bodies — coordinate.

### 2.6 ISO 42001 + 27090 anchors

| Art. 73 activity | ISO 42001 anchor | ISO 27090 anchor |
|------------------|-------------------|------------------|
| Detection of serious incident | A.6.2.6 (operation + monitoring) | sect. 4.6 (operational — anomaly detection, AI-specific incidents) |
| Internal classification (is it a serious incident?) | cl. 10.2 (NC + CA — classification of NC) | sect. 4.6 (incident response playbook) |
| Notification to authority | A.8.3 (external reporting), A.8.4 (incident communication) | sect. 4.6 (operational) |
| Investigation | cl. 10.2 (CA process), 9.1 (monitoring + analysis) | sect. 4.6 (post-incident review); red-team retest after fix |
| Corrective action | cl. 10.2 | sect. 4 (control updates) |
| Communication to affected parties | A.8.4 (incident communication), A.8.5 (info for parties) | sect. 4.6 |

## 3. PMM/incident playbook template

```
PMM PLAN — <SYSTEM NAME>
Provider:                 <name>
System ID:                <as registered in EU database, art. 49>
Version range covered:    <semver range>
Effective from:           <YYYY-MM-DD>
Plan owner:               <name, role>
Approval signature:       <name, date>

═══════════════════════════════════════════════════════════════
1. KPIs MONITORED
═══════════════════════════════════════════════════════════════

| Category | KPI | Source | Frequency | Normal | Warning | Critical | Owner |
|----------|-----|--------|-----------|--------|---------|----------|-------|
| Accuracy | <metric per ISO TS 4213> | logs, eval set | daily | ... | ... | ... | ... |
| Robustness | adversarial accuracy @ ε | red-team CI | weekly | ... | ... | ... | ... |
| Bias | demographic-parity gap | logs by group | daily | ... | ... | ... | ... |
| Drift | feature drift JSD | feature pipeline | daily | ... | ... | ... | ... |
| Drift | label drift KL | label pipeline | weekly | ... | ... | ... | ... |
| Latency | p50/p95/p99 | telemetry | real-time | ... | ... | ... | ... |
| Error rate | 5xx, model errors | telemetry | real-time | ... | ... | ... | ... |
| Security | extraction-rate (queries/identity) | inference logs | real-time | ... | ... | ... | ... |
| Security | jailbreak attempts | content classifier | real-time | ... | ... | ... | ... |
| Complaints | rate per 1000 inferences | complaint channel | weekly | ... | ... | ... | ... |
| Override rate | % deployer overrides | logs | weekly | ... | ... | ... | ... |

═══════════════════════════════════════════════════════════════
2. DATA SOURCES
═══════════════════════════════════════════════════════════════
- Inference logs (art. 12 + 19, retention 6mo+)
- Complaint channel (art. 26(10), 86)
- Deployer reports (art. 26(4))
- Provider's eval set re-runs (continuous V&V)
- Drift telemetry
- Security incident channel (red-team, SIEM, OWASP scanners)
- Regulatory bulletin feed (EUR-Lex, AI Office, national authorities)
- Social/news monitoring (light, contextual)

═══════════════════════════════════════════════════════════════
3. ESCALATION MATRIX
═══════════════════════════════════════════════════════════════

| Trigger | Action | Authority involvement |
|---------|--------|----------------------|
| KPI in WARNING zone | Internal review; root-cause analysis | None |
| KPI in CRITICAL zone (single metric) | Internal review; consider hotfix; inform deployer if material | None unless escalates |
| Performance degradation likely affecting safety/rights | Inform deployer (art. 16); consider suspension | Possible art. 73 if serious incident |
| Detected serious incident (art. 3(49)) | Initiate art. 73 reporting; suspend if necessary | YES — market surveillance authority |
| Cybersecurity incident with personal-data breach | art. 73 + GDPR art. 33 + GDPR art. 34 if high risk | Multiple authorities |
| Substantial modification needed (art. 25) | New conformity assessment | Notified body if Annex VII |

═══════════════════════════════════════════════════════════════
4. INCIDENT-CLASSIFICATION DECISION TREE
═══════════════════════════════════════════════════════════════

Q1: Did the event involve the AI system functioning or malfunctioning?
    NO → not in scope of art. 73.
    YES → continue.

Q2: Did it cause / contribute to:
    (a) Death or serious harm to person's health → SERIOUS, deadline 10d (death) or 15d (other harm)
    (b) Serious + irreversible disruption of critical infrastructure → SERIOUS, deadline 2d
    (c) Infringement of fundamental-rights obligations under Union law → SERIOUS, deadline 2d
    (d) Serious harm to property or environment → SERIOUS, deadline 15d
    NONE → not "serious incident" under art. 73 — handle internally per cl. 10.2.

Q3: Is causation established or reasonably likely?
    YES → start clock.
    NO → continue investigating; if causation later confirmed, clock starts then.

═══════════════════════════════════════════════════════════════
5. SERIOUS-INCIDENT REPORTING SOP
═══════════════════════════════════════════════════════════════

T+0     Detection (PMM signal, complaint, deployer report, internal investigation)
T+0..2h Triage: classify severity per art. 3(49) per Q1-Q3 above
T+2..24h Initial assessment: scope, affected parties, causation hypothesis
T+24..48h If serious incident type (b)/(c): NOTIFY market surveillance authority (deadline 2d)
T+24..240h If type (a) — death: NOTIFY (deadline 10d)
T+24..360h If type (a) — health harm or (d): NOTIFY (deadline 15d)
        + GDPR art. 33 (72h) if personal-data breach
        + GDPR art. 34 to data subjects (without undue delay) if high risk
        + Sector reports (NIS2, DORA, MDR vigilance, etc.) per applicable schedules

PARALLEL: investigation
       — preserve forensic state
       — do NOT alter AI system before informing competent authority (art. 73(6))
       — root-cause analysis
       — corrective measures planning
       — cross-team comms (legal, security, AI ethics, executive)

OUTCOME: corrective measures + lessons learned + RMS update + PMM thresholds review
        + technical documentation update (Annex IV §6 lifecycle changes)
        + notify deployers (art. 16, 20)
        + customer/affected-party communication if appropriate

═══════════════════════════════════════════════════════════════
6. PMM REVIEW CYCLE
═══════════════════════════════════════════════════════════════

Monthly:    KPI dashboard review; review of warnings; minor threshold adjustments
Quarterly:  PMM plan effectiveness review; major threshold adjustments; coordination with RMS (art. 9)
Annually:   Full PMM plan review + management review (ISO 42001 cl. 9.3) + PMM scope re-evaluation
On change:  Substantial modification of system → PMM plan revisited + AISIA re-executed
On regulatory change: PMM plan re-aligned to new obligations or thresholds
```

## 4. Worked example: drift-detection trigger to art. 73

Scenario: A high-risk credit-scoring system (Annex III §5(b)) operated by a bank-deployer detects a sudden 12% accuracy drop on the protected-group cohort over 7 days. The drop is statistically significant and persistent.

```
T+0   PMM dashboard: bias-gap KPI in CRITICAL.
T+1h  Provider's MLOps + AI ethics team triage.
T+24h Root cause: upstream data-source change (third-party data provider altered schema).
      Hypothesis: data-quality regression. Not yet a serious incident — accuracy drop
      affects ~3% of decisions; no individual harm verified.
T+48h Provider notifies deployer (art. 16) of degraded performance + suggests pause for
      affected cohort.
T+72h Deployer suspends use for affected cohort (art. 26(4)).
T+96h Provider rolls out hotfix.
T+1w  Investigation reveals one applicant from the affected cohort was wrongly denied
      a loan during the 7-day window; this denial cascaded into eviction proceedings.
      → Serious incident under art. 3(49)(c) (infringement of fundamental rights —
        non-discrimination + access to housing).
T+1w+0d Clock starts on art. 73 reporting (causation reasonably established).
T+1w+15d (or sooner if (c) trigger) Provider files art. 73 report to market surveillance
        authority. Deployer files separately if applicable.
T+...  Investigation, corrective measures, lessons-learned. Update Annex IV §6 lifecycle
        changes log; update RMS (art. 9). Communicate corrective action to deployers.
```

## 5. Common pitfalls

1. **Treating PMM as a project, not a continuous program.** PMM is a perpetual operational obligation. Outsource the data-collection plumbing if needed; never the analysis or decision authority.

2. **Insufficient deployer-feedback channel.** Providers often build PMM around their own infrastructure logs and forget that material signal flows from deployer use. Build a structured feedback channel; require it contractually.

3. **Deferring incident classification.** Some providers wait for "absolute certainty" of causation before art. 73 clock. The legal threshold is **causal link OR reasonable likelihood**. When in doubt, notify; under-reporting risk is high.

4. **Altering the system before informing authorities.** Art. 73(6) explicitly prohibits investigation that alters the system in a way affecting subsequent evaluation, prior to informing competent authorities. Hot-fixes during forensics need authority awareness.

5. **Forgetting GDPR/NIS2/sector overlap.** A single incident triggers multiple parallel notifications. Have a coordinated playbook.

6. **Not feeding PMM signals back into the RMS.** Art. 9(2)(c) explicitly requires the RMS to evaluate risks emerging from PMM data. The loop: PMM detects → RMS updates → controls strengthened → Annex IV updated → deployer informed.

7. **PMM plan stale relative to system version.** When the system materially changes (new model, new data source), the PMM plan must be revisited. Include this trigger in change-management gate (cl. 6.3).
