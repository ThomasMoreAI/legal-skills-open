---
name: nis2-readiness-arttuan
title: NIS2 Readiness
description: Decide whether NIS2 catches the entity under national law, then work the ten Art. 21(2) measures and the 24h/72h/one-month reporting path
author: ArttuAn
author_url: https://github.com/ArttuAn/eu-compliance-skills/tree/main/skills/nis2-readiness
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: cybersecurity
language: en
---

# NIS2 Readiness

NIS2 regulates the **organisation**, not the product. That is why it gets missed
by teams who scope their software carefully: the duty attaches to the entity, it
brings personal accountability for management, and a large number of ordinary
SaaS companies are "cloud computing service providers" or "managed service
providers" under Annex I without ever having thought of themselves that way.

It is also a **Directive**. The binding text is your Member State's
transposition, transpositions differ, and several were late. Anyone quoting the
Directive at you as if it were directly applicable has skipped a step.

> **Not legal advice.** Whether an entity is in scope, and as essential or
> important, is decided by national law. This skill produces the scoping
> questions, the measure-by-measure gaps and the reporting machinery.

```
  sector (Annex I / II) × size cap ──► in scope? ──no──► exclusion + expires_if
        │ yes                                             (the 50th hire)
        ▼
  essential or important ──► supervision regime, penalty ceiling
        │
        ▼
  Art. 20  management approval + training   ──► personal liability
  Art. 21  the ten measures                 ──► policies + evidence
  Art. 23  24h / 72h / one month            ──► runbook, tested
```

## Use this when

- The entity is in an Annex I or II sector, or might be: cloud, data centres,
  CDNs, DNS, managed IT or security services, digital infrastructure, health,
  energy, transport, banking, water, public administration, postal, waste,
  chemicals, food, manufacturing, online marketplaces, search, social platforms,
  research.
- Headcount or turnover has crossed, or is about to cross, the medium-enterprise
  cap.
- An enterprise customer's security questionnaire has started asking about NIS2,
  which is how most companies find out they are in someone's supply chain and
  therefore in their Art. 21(2)(d) assessment.

**Do not use this when** the entity is below the size cap in every Member State
of establishment **and** in no Annex I or II sector — but record that exclusion
with a machine-evaluable `expires_if`, because it is the single most likely
exclusion in this repo to expire silently.

Note two things that override the size cap: Member States may designate specific
entities regardless of size, and certain entity types (DNS service providers,
TLD registries, trust service providers, some public administration) are in
scope irrespective of size. Check the national law, not the Directive.

## Ask first

1. **"Headcount, annual turnover, and balance sheet total — at group level?"**
   The medium-enterprise cap is **OR**: 50 or more staff, **or** turnover above
   €10M, **or** balance sheet above €10M. A subsidiary under the cap inside a
   group above it is usually not exempt.
2. **"Does any part of the business provide cloud computing, data centre
   services, managed IT or security services, a CDN, DNS, or an online
   marketplace, search engine or social network?"**
   Read it as a list. "We're a SaaS company" is often a cloud computing service
   provider under Annex I and the founders do not know it.
3. **"Which Member States are you established in?"**
   Decides which transposition binds and which authority supervises. For some
   digital providers, jurisdiction follows the main establishment.
4. **"Has your board or management body formally approved the cybersecurity risk
   management measures, and have they been trained?"**
   Art. 20. Personal accountability, and usually the first thing a supervisor
   asks for. "The CTO looked at it" is not board approval.
5. **"Who are your critical suppliers, and when did you last assess their
   security?"**
   Art. 21(2)(d) supply chain security, which is also what your own customers
   are now asking you about.
6. **"If you detected a significant incident at 02:00 on a Saturday, who decides
   whether to report, and how long would it take to reach them?"**
   The 24-hour clock is the part of NIS2 most likely to be missed in practice.

## What the law requires

> **Directive (EU) 2022/2555.** Transposition was due 17 October 2024; **several
> Member States were late and the national texts differ**. Verify against the
> national law for each Member State of establishment, and say so where you
> could not read it.

**Essential vs important** does not change the measures. It changes supervision
(proactive for essential, reactive for important) and the penalty ceiling
(€10M/2% versus €7M/1.4%).

### Art. 20 — governance

Management bodies must **approve** the risk-management measures, **oversee**
their implementation, and can be **held liable** for infringements. They must
follow training, and are required to offer similar training to staff. This is
not delegable to the security team, and evidence of it — a dated board minute —
is the artifact.

### Art. 21(2) — the ten measures

Work them as a checklist with an owner and evidence for each. "All-hazards" is
the stated standard, so this is broader than cyber.

| # | Measure | Evidence that satisfies it |
| --- | --- | --- |
| a | Risk analysis and information system security policies | A current risk register and an approved policy set |
| b | Incident handling | A runbook, a register, and drill records |
| c | Business continuity: backup, disaster recovery, crisis management | A **tested** restore, dated |
| d | Supply chain security, including supplier relationships | Per-supplier assessments and contractual security terms |
| e | Security in acquisition, development and maintenance, including vulnerability handling and disclosure | SDLC controls, dependency scanning, a CVD policy |
| f | Policies to assess the effectiveness of the measures | Internal audit, pentest, metrics with dates |
| g | Cyber hygiene and security training | Completion records, not a slide deck |
| h | Cryptography and encryption policy | A policy naming algorithms and key management |
| i | HR security, access control, asset management | Joiner/mover/leaver process, access reviews, an asset inventory |
| j | MFA, secure voice/video/text, secured emergency communications | MFA coverage figures; an out-of-band comms channel |

Two that get skipped: **(c) requires the restore to have been tested** — an
untested backup is not business continuity — and **(j) requires emergency
communications that work when your primary systems are down**, which means not
the Slack that the ransomware encrypted.

### Art. 23 — reporting

To the CSIRT or competent authority, for a **significant incident**:

| Stage | Deadline | Content |
| --- | --- | --- |
| Early warning | **24 hours** of becoming aware | Whether it may be unlawful/malicious, cross-border impact |
| Incident notification | **72 hours** | Assessment, severity, impact, indicators of compromise |
| Intermediate report | On request | Status updates |
| Final report | **1 month** after the notification | Detailed description, root cause, mitigation, cross-border impact |

An incident is significant if it has caused or is capable of causing severe
operational disruption or financial loss, or considerable material or
non-material damage to others. **Recipients of your services may also have to be
told** where the incident could adversely affect them.

## What to produce

**1. The scoping decision**, with the arithmetic shown:

```yaml
nis2:
  in_scope: true
  sector: "Annex I - digital infrastructure / cloud computing service provider"
  sector_reasoning: "multi-tenant hosted platform with self-service provisioning"
  size: {headcount: 74, turnover_eur: 11200000, balance_sheet_eur: 8400000}
  size_rule: "headcount >= 50 OR turnover > 10M OR balance sheet > 10M"
  classification: "important"          # essential vs important: national criteria
  member_states: [FI, DE]
  national_law_checked: {FI: "2026-09-12", DE: null}   # be honest about the gap
  source: {kind: answered, question: E-02}
```

**2. A measure register**, one row per Art. 21(2) point, with an owner, an
evidence path and a status. `deferred` is an allowed status **only** with an
owner and a date — a measure with no owner is not deferred, it is absent.

**3. The reporting runbook**, with the clocks pre-computed and the decision
authority named:

```python
from datetime import datetime, timedelta

def nis2_clocks(aware_at: datetime) -> dict[str, datetime]:
    """From awareness, not from triage, not from confirmation."""
    return {
        "early_warning": aware_at + timedelta(hours=24),
        "notification": aware_at + timedelta(hours=72),
        "final_report": aware_at + timedelta(hours=72) + timedelta(days=30),
    }
```

Put the decision authority and their deputy in the runbook by name, with phone
numbers, and put the runbook somewhere reachable when the network is down. See
`skills/incident-response` for how this clock interacts with GDPR's 72 hours and
the CRA's 24 — they run concurrently, from different trigger events, to
different regulators.

**4. Board evidence.** A dated minute recording approval of the measures and the
training completed. One paragraph, and it is the first thing asked for.

**5. A supplier register** with the last assessment date per critical supplier.
This doubles as the answer to your own customers' questionnaires, which is the
easiest internal justification for doing it.

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

- **"We're a SaaS company, not critical infrastructure."** Cloud computing
  service providers are Annex I. So are managed service providers, data centres,
  CDNs and DNS providers. The sector list decides, not self-image.

- **Reading the Directive instead of the national law.** Transpositions differ
  on registration deadlines, on which entities are designated regardless of size,
  and on penalties. Name the Member State and say when you could not read its law.

- **Size cap as AND.** It is OR. Fifty staff alone puts you over, whatever the
  turnover.

- **Group-level figures ignored.** A 20-person subsidiary of a 2,000-person
  group is usually not exempt.

- **No board approval.** Art. 20 is not delegable and carries personal liability.
  A security team that has done all ten measures without a board minute has
  missed the article the supervisor will ask about first.

- **Untested backups counted as continuity.** Measure (c) needs a dated,
  successful restore test.

- **Emergency comms that depend on the compromised system.** Measure (j)
  specifically contemplates communications that survive the incident.

- **Discovering the 24-hour clock during the incident.** It starts at awareness.
  Name the decision-maker in advance and drill it.

- **Confusing NIS2 with the CRA.** NIS2 is the organisation and its services;
  the CRA is the product you ship. Many companies owe both, to different
  regulators.

## Verify

Follow `references/verification.md`. For this skill specifically:

1. **Tier 0** — install, `--help`, scope a fixture entity and emit the measure
   register.

2. **Tier 1** — `pytest -q`, offline:

```python
def test_size_cap_is_or_not_and():
    assert in_scope_size(50, 0, 0) is True
    assert in_scope_size(10, 10_000_001, 0) is True
    assert in_scope_size(49, 9_999_999, 9_999_999) is False


def test_group_figures_are_used_when_present(entity_in_group):
    assert scope(entity_in_group).in_scope is True


def test_saas_is_classified_as_cloud_computing(brief_multitenant_saas):
    result = scope(brief_multitenant_saas)
    assert "Annex I" in result.sector
    assert "cloud" in result.sector.lower()


def test_exclusion_records_a_machine_evaluable_expiry(brief_small):
    exclusion = scope(brief_small).exclusion
    assert "headcount >= 50" in exclusion["expires_if"]
    assert evaluate(exclusion["expires_if"], {"headcount": 50}) is True


def test_all_ten_measures_are_present(register):
    assert len(register) == 10
    assert {row.point for row in register} == set("abcdefghij")


def test_a_measure_without_an_owner_is_not_deferred(register):
    row = register.by_point("d")
    row.status, row.owner = "deferred", None
    assert validate(row)[0].severity == "condition"
    assert "owner" in validate(row)[0].needs


def test_untested_backup_fails_continuity(register):
    row = register.by_point("c")
    row.evidence = {"backups_configured": True, "last_restore_test": None}
    assert validate(row)[0].statement.startswith("No successful restore test")


def test_clocks_are_computed_from_awareness():
    clocks = nis2_clocks(datetime(2026, 9, 15, 2, 0))
    assert clocks["early_warning"] == datetime(2026, 9, 16, 2, 0)
    assert clocks["notification"] == datetime(2026, 9, 18, 2, 0)
    assert clocks["final_report"] == datetime(2026, 10, 18, 2, 0)


def test_missing_board_approval_is_a_condition(brief_no_board_minute):
    finding = assess(brief_no_board_minute).finding_for("Art. 20")
    assert finding.severity == "condition"
    assert "management body" in finding.statement


def test_national_law_gap_is_reported_not_assumed(brief_two_states):
    report = render(scope(brief_two_states))
    assert "could not verify the national transposition for DE" in report


def test_no_legal_conclusion_about_scope(brief):
    text = render(scope(brief)).lower()
    assert "you are not in scope" not in text
    assert "candidate" in text or "must be confirmed" in text
```

3. **Tier 2** — report: sector and size arithmetic, essential/important, the
   ten measures by status, suppliers assessed versus total, and whether a
   reporting drill has ever been run. The measure count at `deferred` with no
   owner is the number that predicts trouble.

4. **Tier 3** — run a reporting drill. Pick a scenario, start the clock at 02:00,
   and measure how long it actually takes to reach the named decision-maker and
   produce a submittable early warning. Twenty-four hours is less time than it
   sounds like when it starts on a Friday night.

Then tell the user which national transpositions you could not read, and that
scope and classification need confirming under national law rather than from the
Directive.
