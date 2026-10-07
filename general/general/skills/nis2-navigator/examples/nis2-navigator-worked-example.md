# Worked Example — NIS2 Navigator end-to-end

A representative, end-to-end run of the skill on a single organisation: scope classification →
Art. 21 gap analysis → compliance roadmap → final report. Inputs are illustrative; citations and
thresholds reflect the skill's reference material at authoring time and should be re-verified before
reliance (the skill prompts a web search on activation for exactly this reason).

---

## User prompt

> "We're a managed IT services provider in Germany — about 120 employees, €25M annual turnover,
> €18M balance sheet. We run monitoring and patch management for mid-size clients. A new customer
> just sent us a contract clause requiring 'NIS2 compliance'. Do we actually fall under NIS2, and
> if so, where do we stand? Focus on Germany."

---

## Session initialization

*Disclaimer shown (not blocking). Jurisdiction focus: **Germany** → `references/germany-nis2umsucg.md`
loaded. A web search for current BSIG-neu transposition and BSI guidance is run before answering.*

---

## Phase 1 — Scope & Classification

Intake (asked one at a time; answers consolidated here):

| Field | Answer |
|---|---|
| Sector | ICT service management (B2B) |
| Services | Managed services: monitoring, patch management, remote administration |
| Size | 120 employees · €25M turnover · €18M balance sheet |
| Group | Independent GmbH, not part of a group |
| Special status | None of DNS / TLD / trust service / public comms / sole-provider |

**Reasoning:**

1. **Sector** → "Managed service provider" is named in **Annex I** (ICT service management). Note: MSPs
   are listed *regardless of size* for the essential/important split that follows.
2. **Size test** → 120 employees ⇒ ≥50 ⇒ at least **medium**; below the 250-employee / €50M large
   threshold ⇒ **medium enterprise**.
3. **Category** → Managed service providers are treated as **essential entities** under the MSP
   provisions even at medium size. → **Essential entity.**
4. **DORA check** → Not a financial entity; DORA carve-out does not apply.
5. **CIR check** → As a managed service provider / digital-infrastructure-adjacent entity, **CIR
   2024/2690** technical requirements apply on top of Art. 21 — flagged early.
6. **Germany** → **BSI registration is required.** Per the reference file, the MSP registration
   window has already opened; treat registration as **overdue** and a P1 item.

> **SCOPE DETERMINATION**
> - Sector: Annex I — ICT service management (managed service provider)
> - Size classification: Medium
> - Entity category: **Essential**
> - Basis: NIS2 Art. 3(1) (essential) + Annex I; § 28/§ 30 BSIG-neu
> - Special flags: **CIR 2024/2690 applies**; MSP-regardless-of-size
> - Germany: BSI registration **required — treat as overdue**

**Answer to the customer-clause question:** Yes — you are in scope as an **essential entity**, so the
contractual "NIS2 compliance" requirement aligns with a direct statutory obligation, not just a
flow-down. Proceed to gap analysis.

---

## Phase 2 — Art. 21 Gap Analysis

Each measure scored 0–4 after one targeted question. Illustrative results:

| # | Measure (Art. 21(2)) | Maturity | Status | Note |
|---|---|---|---|---|
| a | Risk analysis & IS policies | 2 | 🟡 | ISMS policy exists; last reviewed >12 months ago |
| b | Incident handling | 2 | 🟡 | Runbook exists; no tested 24h/72h NIS2 reporting path |
| c | Business continuity & crisis mgmt | 1 | 🔴 | Backups run; no tested recovery / crisis plan |
| d | Supply chain security | 1 | 🔴 | No supplier security clauses or assessment process |
| e | Acquisition, dev & maintenance security | 2 | 🟡 | Patch process strong for clients; weaker internally |
| f | Effectiveness assessment | 1 | 🔴 | No measurement of control effectiveness |
| g | Cyber hygiene & training | 2 | 🟡 | Annual awareness training; no role-based depth |
| h | Cryptography & encryption | 3 | 🟢 | TLS + disk encryption enforced |
| i | HR security & access control | 2 | 🟡 | Joiner/leaver process; access reviews ad hoc |
| j | MFA & secure communications | 3 | 🟢 | MFA enforced for remote + privileged access |

**Overall Score: 19 / 40 — 🟡 Needs Improvement**

Reasoning is shown to the user per measure so scores can be challenged. ISO 27001:2022 anchors are
cited where the entity already has controls (e.g., measure (a) ↔ A.5.1/A.5.2) so existing work is
credited rather than re-done.

**Top gaps (maturity ≤ 1):** business continuity (c), supply chain security (d), effectiveness
assessment (f).

---

## Phase 3 — Compliance Roadmap

Essential entity ⇒ proactive supervision ⇒ low-maturity gaps are urgent.

| Measure | Current → Target | Key actions | Effort | Priority |
|---|---|---|---|---|
| **BSI registration** | Overdue → Filed | Complete § 28/§ 30 BSIG registration; assign contact point | S | **P1 (0–1 mo)** |
| (d) Supply chain | 1 → 3 | Supplier security baseline; contractual security clauses; risk-tier suppliers | M | **P1 (0–3 mo)** |
| (c) Business continuity | 1 → 3 | Document + test recovery; crisis-management plan; tabletop exercise | M | **P1 (0–3 mo)** |
| (b) Incident handling | 2 → 3 | Build + test the 24h early-warning / 72h notification / 1-month report path to the national authority | S | **P1 (0–3 mo)** |
| (f) Effectiveness assessment | 1 → 2 | Define metrics; schedule control-effectiveness review | S | **P2 (3–6 mo)** |
| (a) Risk analysis | 2 → 3 | Refresh ISMS policy; annual review cadence | S | **P2 (3–6 mo)** |
| CIR 2024/2690 | Gap → Conformant | Map CIR technical measures; close deltas vs Art. 21 baseline | L | **P2 (3–6 mo)** |

### Management Briefing (Art. 20 / § 38 BSIG)

> - Approve the risk-management measures (Art. 20(1) / § 38(1) BSIG)
> - Complete cybersecurity training — **not delegable** (Art. 20(2) / § 38(3) BSIG)
> - Oversight of implementation cannot be delegated, even where execution is
> - **Germany:** management body bears **personal liability** for damages from non-compliance (§ 38(2) BSIG)

---

## Output — Final Assessment Report (executive summary excerpt)

> **NIS2 Assessment — [MSP GmbH], Germany**
> **Scope:** Essential entity (Annex I, managed service provider). CIR 2024/2690 applies. BSI
> registration overdue.
> **Maturity:** 19/40 — Needs Improvement.
> **Top 3 priorities:** (1) File the overdue BSI registration; (2) stand up supply-chain security
> (baseline + contractual clauses); (3) document and test business continuity / incident reporting.
> **Management action:** board approval + non-delegable training; note § 38(2) personal-liability
> exposure.
> **Caveat:** This is structured guidance, not legal advice — confirm classification and the
> registration deadline with counsel and verify current BSI guidance before filing.

---

*This example demonstrates the full Session-Init → Phase 1 → Phase 2 → Phase 3 → Report flow on one
representative entity. For a non-German entity, the same flow runs with the relevant
`references/eu-jurisdiction-profiles.md` profile and a recommendation to confirm transposition status
with local counsel.*
