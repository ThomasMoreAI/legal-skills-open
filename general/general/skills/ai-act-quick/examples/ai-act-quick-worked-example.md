# Worked Example — AI Act Quick Assessment (CV-screening tool)

An end-to-end triage run: context intake → 6-gate classification → preliminary output. Inputs are
illustrative; every determination is marked "Likely" and would require a full assessment + counsel.

---

## User prompt

> "We're a German Mittelstand company (~180 staff). We bought a SaaS CV-screening tool that ranks job
> applicants for our recruiters. We run it as-is. Does the EU AI Act apply, and how exposed are we?"

---

## Phase 1 — Quick context (1 batch; no follow-up needed)

The single answer covers all 8 fields (generous extraction):

| Field | Value |
|---|---|
| System description | SaaS tool that ranks job applicants |
| Deployment context | EU/EEA market (Germany) |
| Organization role | Purchased/licensed, run as-is → **Deployer** |
| Sector | HR / employment |
| Affected persons | Job applicants |
| Modifications | None (used within intended purpose) |
| Organization size | Medium (180) |
| Jurisdiction | Germany |

→ All fields covered → proceed directly to classification.

## Phase 2 — 6-gate classification (internal)

| Gate | Result |
|---|---|
| 1. Scope (Art. 2) | **In scope** — deployer established in the EU |
| 2. AI system (Art. 3(1)) | **Likely YES** — infers a ranking beyond a fixed rule set |
| 3. Prohibited (Art. 5) | No Art. 5 trigger (not emotion recognition in the workplace as defined; confirm in full assessment) |
| 4. High-risk (Annex III) | **Likely High-Risk** — Annex III(4)(a): AI for recruitment/selection, incl. filtering applications and evaluating candidates. Art. 6(3) exception unlikely (it materially influences the hiring decision). |
| 5. GPAI | Possibly built on a GPAI model upstream, but the org is a **deployer**, not the GPAI provider |
| 6. Transparency (Art. 50) | Applicants should be informed they are subject to an AI system |

## Phase 3 — Preliminary output (excerpt)

```
## AI Act Quick Assessment — PRELIMINARY
⚠ PRELIMINARY — Full analysis required for compliance decisions

System:        Third-party CV-screening / applicant-ranking SaaS
Risk Tier:     Likely High-Risk
Basis:         Likely Annex III(4)(a) (recruitment)
Role:          Likely Deployer (run as-is, no modification)
Confidence:    Medium

TOP DEPLOYER OBLIGATIONS (if confirmed high-risk)
| # | Obligation | Article | Urgency |
| 1 | Use per provider instructions; ensure human oversight | Art. 26 | Short-term |
| 2 | Ensure input data is relevant/representative for the purpose | Art. 26(4) | Short-term |
| 3 | Inform affected workers/applicants + worker reps | Art. 26(7) | Short-term |
| 4 | Monitor operation; log-keeping; report serious incidents | Art. 26(5)/72 | Ongoing |
| - | AI literacy of staff operating the system | Art. 4 | Immediate (since Feb 2025) |

COMPLIANCE TIMELINE
Annex III high-risk obligations: 2 Dec 2027 (AI Omnibus postponement) — verify current status.

JURISDICTION FLAGS
[DE] Works-council co-determination likely (BetrVG § 87(1) Nr. 6 — monitoring of employees);
     applicant data also engages § 26 BDSG.

FINANCIAL EXPOSURE (Art. 99)
High-risk breach: up to €15M or 3% of worldwide annual turnover (Art. 99(4));
SME/start-up proportionality may apply (Art. 99(6)).

FLAGS & WARNINGS
[GDPR OVERLAP — likely Art. 35 DPIA; Art. 22 automated-decision considerations]
[DEPLOYER, not provider — but a substantial modification or own-branding could flip you to
 quasi-provider under Art. 25]
```

## Recommended next steps (self-contained)

1. **Full classification** — confirm Annex III(4)(a) and run the Art. 6(3) exception analysis at depth.
2. **Role determination** — confirm deployer status; check for any Art. 25 quasi-provider trigger.
3. **Obligation mapping (RACI)** — Art. 26 deployer duties + Art. 4 literacy + Art. 50 transparency.
4. **Documentation** — classification record + compliance register + management briefing.
5. **Counsel** — works-council process (BetrVG), § 26 BDSG / Art. 35 GDPR interaction, contract terms
   with the SaaS provider (instructions, logs, incident cooperation).

> ⚠ Directional guidance only. "Likely High-Risk" is a prompt to investigate, not a final
> classification — validate via a full assessment and legal review before relying on it.

---

*This example shows the deployer / Annex III path. Provider, GPAI, prohibited-practice, and
limited-risk (Art. 50) cases run through the same six gates with different outputs (see `SKILL.md`).*
