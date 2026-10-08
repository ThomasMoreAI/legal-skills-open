看起來工具需要授權。我直接根據 SKILL.md 的格式與結構來撰寫範例檔案。

```markdown
# Example: Taiwanese Hardware Startup IP Audit Before Series A

## Scenario

**User prompt:** "We're raising a Series A and our lead investor just asked for an IP audit. We're a 3-year-old Taipei-based startup that makes an AI-powered visual inspection device for PCB manufacturing. We have a core algorithm we developed in-house, our brand name is 'Visionix', we have a mobile app for floor managers, and we have a proprietary training dataset of 2 million labeled defect images. What IP do we have and what should we protect?"

**Company:** Visionix Co., Ltd. (威視科技有限公司), founded 2023, 12 employees, B2B hardware+software

---

## Analysis

### Step 1 — Inventory

| # | Asset | Description |
|---|-------|-------------|
| A | Brand name "Visionix" | Used on devices, website, marketing materials since 2023 |
| B | AI defect-detection algorithm | Core ML model; not published; competitors cannot easily replicate without the dataset |
| C | PCB inspection device (hardware) | Custom optical module + embedded controller; novel fixture design |
| D | Mobile app source code | iOS/Android floor manager dashboard; ~40,000 LOC |
| E | Defect image dataset | 2M labeled images collected from 8 customer factories under NDA; 3-year collection effort |
| F | Customer onboarding workflow | Internal SOP for integrating with factory MES systems |

---

### Step 2 — Classify

| Asset | IP Type | Rationale |
|-------|---------|-----------|
| A — "Visionix" brand | **Trademark** | Source identifier; protects brand recognition, not creative expression |
| B — AI algorithm | **Trade Secret** (primary) + **Patent** (evaluate) | Model weights are not reverse-engineerable from the device output; but the novel training methodology *may* be patentable |
| C — Hardware device | **Patent** | Physical mechanism (optical module, fixture geometry) is novel, non-obvious, industrially applicable; can be reverse-engineered by competitors |
| D — App source code | **Copyright** | Original creative expression; protection is automatic in Taiwan |
| E — Defect dataset | **Trade Secret** | Commercial value derives entirely from secrecy and cost of replication; no registration mechanism exists for datasets |
| F — Onboarding SOP | **Trade Secret** (low priority) | Operational know-how; modest value, easily reconstructed |

**Iron Law check:** "Visionix" → Trademark (not copyright). Algorithm → Trade Secret, not copyright (copyright would protect source code, not the method). ✓

---

### Step 3 — Assess Current Protection

| Asset | Current Status | Problem |
|-------|---------------|---------|
| A — Visionix TM | **Not registered** with TIPO | Vulnerable to name-squatting; cannot enforce TM rights in China/Japan/EU |
| B — AI algorithm | No NDA with all employees; no patent filed | Two engineers left in 2024; no IP assignment clause in their contracts |
| C — Hardware device | No patent filed; product shipped to 8 customers | Prior art clock started at first delivery ~2023-Q3; 12-month grace period (§22 Patent Act) may already be **expired** |
| D — App source code | Copyright automatic ✓ | Employment contracts signed 2023 include IP assignment clause — **OK** |
| E — Defect dataset | Collected under customer NDAs ✓ | But internal access controls are absent; all 12 employees can access raw data |
| F — Onboarding SOP | Shared via Google Drive with no access log | Low risk, low value |

---

### Step 4 — Identify Gaps

1. **Critical:** No trademark registration → investor due diligence red flag; brand squatting risk in target markets (China, Japan)
2. **Critical:** Hardware patent window may have closed — need IP attorney to verify grace period calculation from first public disclosure date
3. **High:** Two former employees left with potential access to algorithm; no signed IP assignment or NDA on exit
4. **High:** Dataset has no internal access controls — "reasonable efforts to maintain secrecy" requirement for trade secret status may not be met
5. **Medium:** Algorithm patent evaluation pending — need to determine if training methodology meets novelty bar

---

### Step 5 — Prioritize

| Asset | Business Value | IP Risk | Priority |
|-------|--------------|---------|----------|
| A — Visionix TM | High (brand = company) | High (squatting) | 🔴 Immediate |
| C — Hardware patent | High (defensible moat) | Critical (window closing) | 🔴 Immediate |
| E — Dataset access controls | High (core competitive advantage) | High (TS status at risk) | 🔴 Immediate |
| B — Algorithm (former employees) | High | High | 🔴 This week |
| B — Algorithm patent evaluation | Medium | Medium | 🟡 30 days |
| D — App copyright | Low (already protected) | Low | 🟢 Verify contracts only |

---

## Result

# IP Analysis: Visionix Co., Ltd.

## IP Asset Inventory

| Asset | Type | Current Protection | Gap | Priority |
|-------|------|-------------------|-----|----------|
| "Visionix" brand name | Trademark | **None** | Register with TIPO (TW) + Madrid Protocol (CN, JP) | 🔴 H |
| AI defect-detection algorithm | Trade Secret | Partial — no exit NDA with 2 former engineers | Retroactive NDA + IP assignment; implement access controls | 🔴 H |
| PCB inspection hardware (optical module + fixture) | Patent | **None** | Consult patent attorney **this week** — grace period may have lapsed | 🔴 H |
| Mobile app source code | Copyright | Automatic ✓; IP assignment in contracts ✓ | Audit 2023 contracts for completeness | 🟢 L |
| Defect image dataset (2M images) | Trade Secret | Customer NDAs ✓; internal controls **absent** | Role-based access controls + audit log immediately | 🔴 H |
| Onboarding SOP | Trade Secret | None | Restrict Google Drive access; low urgency | 🟡 M |

## Recommendations

1. **"Visionix" trademark** — File with TIPO within 2 weeks (Nice Class 9: electronic instruments; Class 42: software/SaaS). Simultaneously file Madrid Protocol designations for China (CNIPA) and Japan (JPO). Cost: ~NT$15,000–25,000 for TW filing; USD 2,000–4,000 for international. Timeline: TW registration ~12–18 months.

2. **Hardware patent** — Engage a patent attorney *this week* to establish exact first-public-disclosure date. Taiwan Patent Act §22 allows a 6-month grace period for inventor disclosures, but customer shipments may count as public disclosure. If window is open, file a provisional application immediately to establish priority date. If closed, pivot to trade secret for any undisclosed improvements.

3. **Former employee IP gap** — Legal counsel to send IP assignment letters to the 2 departed engineers covering work done during employment. Review their departure paperwork. If no exit NDA exists, this is a material risk to disclose to the Series A investor.

4. **Dataset access controls** — Implement role-based access (engineers need model training data; sales does not). Add access logging. Document the controls in writing. This is required to maintain trade secret status under Taiwan Trade Secret Act §2.

5. **Algorithm patent evaluation** — Commission a prior art search for the training methodology (not the model weights) to assess patentability. Budget 30 days. If novel, file patent; if not, maintain as trade secret with strict controls.

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Competitor registers "Visionix" TM in China | High | High — blocked from CN market entry | File CNIPA via Madrid Protocol within 30 days |
| Hardware patent window expired | Medium | High — competitors can copy device freely | Attorney review of disclosure dates immediately |
| Former employee discloses algorithm to competitor | Medium | High — core ML moat destroyed | IP assignment letters + legal counsel assessment |
| Dataset loses trade secret status (no access controls) | High | High — investor due diligence failure | Role-based access controls + audit log this week |
| Investor due diligence uncovers unassigned IP | Medium | High — deal at risk | Proactive disclosure + remediation plan before data room opens |

---

> **Disclaimer:** This analysis is educational guidance based on the facts provided. It does not constitute legal advice. Engage a licensed patent attorney (專利師) and IP specialist before filing or making strategic IP decisions, particularly given the time-sensitive patent grace period issue.
```
