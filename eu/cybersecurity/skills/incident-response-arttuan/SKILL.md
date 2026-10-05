---
name: incident-response-arttuan
title: Incident Response
description: One incident, several regulators, different clocks — build the runbook that computes GDPR, NIS2, CRA and DORA deadlines from a single awareness timestamp
author: ArttuAn
author_url: https://github.com/ArttuAn/eu-compliance-skills/tree/main/skills/incident-response
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: cybersecurity
language: en
---

# Incident Response

An incident is one event. The reporting duties are not. Depending on what you
are, the same breach can start a **72-hour** GDPR clock to a data protection
authority, a **24-hour** NIS2 clock to a CSIRT, a **24-hour** CRA clock to ENISA,
and a DORA clock to a financial supervisor — from different trigger events, with
different thresholds, to different regulators, in different Member States.

The failure mode is not that teams do not know the rules. It is that at 02:00 on
a Saturday, nobody can remember which clock started when, and the 24-hour ones
are gone before anyone has finished triaging.

So the deliverable is not a policy. It is a **runbook that computes the deadlines
from one timestamp** and names the person who decides.

> **Not legal advice.** Whether an incident is notifiable, and to whom, is a
> legal judgement made under time pressure. This skill builds the machinery and
> the decision record — get counsel or your DPO into the runbook by name.

```
  detection ──► AWARENESS  (the timestamp everything hangs off)
                    │
      ┌─────────────┼──────────────┬───────────────┐
      ▼             ▼              ▼               ▼
  GDPR 33        NIS2 23        CRA 14         DORA
  personal       significant    actively        major ICT
  data breach?   incident?      exploited?      incident?
      │             │              │               │
   72h to DPA    24h early      24h early      per RTS
   +notify        72h notif.     72h notif.
   subjects       1 month        14 days
   if high risk   final          final
      │             │              │               │
      └─────────────┴──────────────┴───────────────┘
                    │
              one decision record, per regime, including "we did not report, because…"
```

## Use this when

- Building the runbook — before an incident, which is the only time it can be
  built properly.
- Immediately after `eu-applicability`, because the applicable regimes decide
  which clocks exist.
- During an incident, to compute deadlines and produce the submissions.
- After an incident, to write the decision record — including for the regimes
  you decided not to report to, which is itself a required record under GDPR
  Art. 33(5).

**Do not use this when** GDPR is the only applicable regime and there is no
personal data. Then you have an outage, not a notifiable incident, and a runbook
for it is ordinary engineering.

## Ask first

1. **"If you detected something at 02:00 on a Saturday, who decides whether to
   report — name them and their deputy — and how long would it take to reach
   them?"**
   The 24-hour clocks are lost here, not in the drafting.
2. **"Which regulators would you be reporting to? Name the authority and the
   Member State for each regime that applies."**
   Usually nobody knows. This is a ten-minute lookup before an incident and an
   hour you do not have during one.
3. **"Where is the runbook, and does it work when your primary systems are
   down?"**
   A runbook in the wiki that the ransomware encrypted is not a runbook.
4. **"Have you ever run a drill?"**
   Untested reporting paths are documents, not capabilities.
5. **"What does your breach register contain today — including incidents you
   decided not to report?"**
   Art. 33(5) requires the non-reported ones and the reasoning. A register with
   only reported incidents looks like one started after the first report.
6. **"Do your processor contracts require your vendors to tell you 'without
   undue delay'? What is the shortest notice period you have agreed?"**
   Your 72 hours starts when *you* become aware, and a vendor who takes five days
   to tell you has consumed your entire window.

## What the law requires

> Verify the current text and the national procedures for each authority.
> Reporting portals, forms and thresholds are set nationally and change.

### GDPR — Arts. 33, 34

- **Trigger**: a personal data breach — accidental or unlawful destruction, loss,
  alteration, unauthorised disclosure of, or access to, personal data.
- **To the supervisory authority**: without undue delay and **where feasible
  within 72 hours** of becoming aware, unless unlikely to result in a risk to
  rights and freedoms.
- **To the data subjects**: without undue delay where the breach is likely to
  result in a **high** risk. Exceptions: the data was encrypted to an
  appropriate standard, the risk has been mitigated, or individual notice would
  involve disproportionate effort (then a public communication).
- **Processors** notify their controller without undue delay (Art. 33(2)). No
  direct duty to the authority.
- **Art. 33(5)**: document **every** breach, including those you did not notify,
  with the facts, effects and remedial action. This register is the evidence.

"Aware" means having a reasonable degree of certainty that a security incident
has occurred leading to personal data being compromised — not the moment
investigation concludes. A short investigation period is accepted; using triage
to delay the clock is not.

### NIS2 — Art. 23

- **Trigger**: a significant incident — severe operational disruption, financial
  loss, or considerable material or non-material damage to others.
- **24 hours** early warning; **72 hours** notification with assessment,
  severity, impact and indicators of compromise; final report **one month** after
  the notification. Recipients of your services may also need telling.

### CRA — Art. 14

- **Trigger**: an actively exploited vulnerability in your product, or a severe
  incident affecting its security.
- **24 hours** early warning to the CSIRT and ENISA; **72 hours** notification;
  final report **14 days** (vulnerability) or **one month** (incident).

### DORA — Art. 19

Financial entities: initial, intermediate and final notifications on deadlines
set in the regulatory technical standards, to the competent authority.

### The interactions that matter

- **The clocks start from different events.** GDPR starts at awareness of a
  *personal data* breach. NIS2 starts at awareness of a *significant incident*.
  The CRA starts at awareness of *active exploitation*. One event can start them
  at different times, and frequently does — you may know the service is down
  hours before you know data was exfiltrated.
- **24 hours beats 72 hours.** If NIS2 or the CRA applies, your effective first
  deadline is 24 hours, and the GDPR assessment has to fit inside it.
- **Reporting to one is not reporting to another.** Different authorities,
  different forms, sometimes different Member States.
- **Do not let the NIS2 early warning contradict the GDPR notification.** They
  will be read together. One factual timeline, maintained centrally, feeding
  every submission.

## What to produce

**1. A clock calculator**, so nobody does date arithmetic at 3am:

```python
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Deadline:
    regime: str
    stage: str
    due: datetime
    authority: str
    citation: str


def deadlines(*, personal_data_aware_at=None, significant_incident_aware_at=None,
              exploitation_aware_at=None, regimes, authorities) -> list[Deadline]:
    out: list[Deadline] = []
    if "gdpr" in regimes and personal_data_aware_at:
        out.append(Deadline("gdpr", "notify supervisory authority",
                            personal_data_aware_at + timedelta(hours=72),
                            authorities["gdpr"], "Art. 33(1)"))
    if "nis2" in regimes and significant_incident_aware_at:
        base = significant_incident_aware_at
        out += [
            Deadline("nis2", "early warning", base + timedelta(hours=24),
                     authorities["nis2"], "Art. 23(4)(a)"),
            Deadline("nis2", "incident notification", base + timedelta(hours=72),
                     authorities["nis2"], "Art. 23(4)(b)"),
            Deadline("nis2", "final report",
                     base + timedelta(hours=72) + timedelta(days=30),
                     authorities["nis2"], "Art. 23(4)(d)"),
        ]
    if "cra" in regimes and exploitation_aware_at:
        base = exploitation_aware_at
        out += [
            Deadline("cra", "early warning", base + timedelta(hours=24),
                     authorities["cra"], "Art. 14(2)(a)"),
            Deadline("cra", "notification", base + timedelta(hours=72),
                     authorities["cra"], "Art. 14(2)(b)"),
            Deadline("cra", "final report", base + timedelta(days=14),
                     authorities["cra"], "Art. 14(2)(c)"),
        ]
    return sorted(out, key=lambda d: d.due)
```

Three separate awareness timestamps, because they are three separate facts. A
calculator that takes one timestamp and applies it to every regime produces
wrong deadlines in the common case.

**2. The authority table**, filled in advance — name, Member State, portal URL,
form, and what they require. Filling this during an incident costs an hour you
do not have.

**3. The decision record template**, per regime, including non-reporting:

```yaml
incident: INC-2026-004
detected_at: "2026-09-15T02:14:00Z"
awareness:
  significant_incident: "2026-09-15T02:40:00Z"
  personal_data_breach: "2026-09-15T06:10:00Z"   # later: exfiltration confirmed later
  active_exploitation: null
decisions:
  - regime: nis2
    reportable: true
    reasoning: "service unavailable to all customers for 4h; severe operational disruption"
    submitted: {stage: early_warning, at: "2026-09-15T09:20:00Z", ref: "FI-CSIRT-88213"}
  - regime: gdpr
    reportable: true
    reasoning: "exfiltration of account records confirmed; risk to rights and freedoms"
    subjects_notified: false
    subjects_reasoning: "data was encrypted at rest with keys unaffected - Art. 34(3)(a)"
  - regime: cra
    reportable: false
    reasoning: "no vulnerability in a distributed product; the compromise was in hosted infrastructure"
```

The `reportable: false` entries with reasoning **are** the Art. 33(5) record.
Write them at the time, not later — the reasoning available afterwards is a
reconstruction.

**4. An out-of-band communications plan.** Contact list, conference bridge, and
where the runbook lives, all independent of the systems that might be
compromised. NIS2 Art. 21(2)(j) requires this explicitly; everyone needs it.

**5. A drill, run and dated.** Pick a scenario, start the clock at an
inconvenient hour, and measure time-to-decision and time-to-submittable-draft.
The gap between those two numbers and 24 hours is your real risk.

**Every assessment carries a certainty.** Each finding, each applicable or
ruled-out regime, and the headline of the brief carry `certainty` (0–100) — the
honest percent of the assessment that rests on verified sources and confirmed
facts rather than inference, open unknowns and interpretation. Wherever you
state an applicability, a classification, a citation-backed obligation or a
finding, show the percentage **and the single largest reason it is not higher**:
"ruled out NIS2 — certainty 66%: the national transposition was not read".
`references/certainty.md` holds the anchors; the rules that matter here: an
answer graded `UNKNOWN` caps anything resting on it at 70, an unread Directive
transposition caps at 60, a classification pending counsel caps at 50, and a
`100` requires every deciding fact SPECIFIC, every citation verified on EUR-Lex,
every transposition read and every regime screened. Certainty is visibility, not
a free pass — VAGUE stays rejected, an open blocker stays blocked.

## Failure modes

- **One awareness timestamp for all regimes.** They are different facts with
  different trigger events, and conflating them produces deadlines that are
  wrong in both directions.

- **Triage used to delay the clock.** "Aware" is reasonable certainty that an
  incident occurred, not the end of the investigation. A short verification
  period is accepted; a week is not.

- **The 24-hour clock discovered on day two.** If NIS2 or the CRA applies, that
  is your first deadline, not the GDPR 72.

- **A register containing only reported incidents.** Art. 33(5) requires all of
  them and the non-reporting reasoning.

- **The runbook inside the blast radius.** Encrypted, unreachable, or requiring
  SSO that is down.

- **No named decision-maker.** Everyone waits for someone to decide whether to
  report. Name a person and a deputy, with phone numbers.

- **Vendor notice periods that eat your window.** Your clock starts when you
  become aware, and a processor contract permitting "within five business days"
  hands your entire 72 hours to a third party. Fix it in the DPA — see
  `skills/evidence-pack`.

- **Contradictory submissions.** The NIS2 early warning and the GDPR
  notification tell different stories because two people wrote them from two
  timelines. Maintain one factual timeline.

## Verify

Follow `references/verification.md`. For this skill specifically:

1. **Tier 0** — install, `--help`, compute deadlines for a fixture incident.

2. **Tier 1** — `pytest -q`, offline:

```python
def test_separate_awareness_timestamps_produce_separate_clocks():
    result = deadlines(
        significant_incident_aware_at=dt("2026-09-15T02:40"),
        personal_data_aware_at=dt("2026-09-15T06:10"),
        regimes={"nis2", "gdpr"}, authorities=AUTH)
    nis2_first = next(d for d in result if d.regime == "nis2")
    gdpr = next(d for d in result if d.regime == "gdpr")
    assert nis2_first.due == dt("2026-09-16T02:40")      # 24h from ITS awareness
    assert gdpr.due == dt("2026-09-18T06:10")            # 72h from ITS awareness


def test_earliest_deadline_is_surfaced_first():
    result = deadlines(significant_incident_aware_at=dt("2026-09-15T02:40"),
                       personal_data_aware_at=dt("2026-09-15T02:40"),
                       regimes={"nis2", "gdpr"}, authorities=AUTH)
    assert result[0].regime == "nis2" and result[0].stage == "early warning"


def test_no_clock_without_the_triggering_awareness():
    result = deadlines(personal_data_aware_at=dt("2026-09-15T06:10"),
                       regimes={"nis2", "gdpr"}, authorities=AUTH)
    assert {d.regime for d in result} == {"gdpr"}


def test_cra_final_report_is_fourteen_days_not_a_month():
    result = deadlines(exploitation_aware_at=dt("2026-09-15T00:00"),
                       regimes={"cra"}, authorities=AUTH)
    final = next(d for d in result if d.stage == "final report")
    assert final.due == dt("2026-09-29T00:00")


def test_every_regime_produces_a_decision_even_when_not_reporting(record):
    assert {d["regime"] for d in record["decisions"]} == record["applicable_regimes"]
    for decision in record["decisions"]:
        assert decision["reasoning"]


def test_non_reported_incident_still_enters_the_register(register):
    register.add(incident(reportable=False, reasoning="no risk to rights and freedoms"))
    assert register[-1].reasoning
    assert register[-1].citation == "Art. 33(5)"


def test_missed_deadline_is_surfaced_not_silently_passed(clock):
    clock.now = dt("2026-09-16T03:00")
    status = track(deadlines(significant_incident_aware_at=dt("2026-09-15T02:40"),
                             regimes={"nis2"}, authorities=AUTH), now=clock.now)
    assert status.missed and status.missed[0].stage == "early warning"


def test_authority_is_named_for_every_applicable_regime(runbook):
    for regime in runbook.regimes:
        assert runbook.authorities[regime]["name"]
        assert runbook.authorities[regime]["portal"]


def test_decision_maker_and_deputy_are_named(runbook):
    assert runbook.decision_maker.name and runbook.decision_maker.phone
    assert runbook.deputy.name


def test_runbook_is_reachable_out_of_band(runbook):
    assert runbook.location_kind in ("printed", "offline_copy", "external_provider")


def test_vendor_notice_period_longer_than_24h_is_a_finding(vendors):
    findings = assess_vendor_notice(vendors)
    assert any("consumes your reporting window" in f.statement for f in findings)
```

3. **Tier 2** — report: applicable regimes and their authorities (named, with
   portals), the earliest clock, whether a drill has been run and when, and the
   longest vendor notice period in your DPAs. That last number is the size of
   the hole in your 72 hours.

4. **Tier 3** — run the drill. Start at an inconvenient hour, do not warn people,
   and measure time to reach the decision-maker and time to a submittable early
   warning. Report both against 24 hours.

Then tell the user which authorities and national procedures you could not
verify, and be explicit that notifiability is a judgement the runbook supports
rather than makes.
