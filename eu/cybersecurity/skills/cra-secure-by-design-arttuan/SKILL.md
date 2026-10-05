---
name: cra-secure-by-design-arttuan
title: CRA — Secure by Design
description: 'Cyber Resilience Act: decide whether you place a product on the market, then build the SBOM, vulnerability handling, support period and reporting path'
author: ArttuAn
author_url: https://github.com/ArttuAn/eu-compliance-skills/tree/main/skills/cra-secure-by-design
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: cybersecurity
language: en
---

# CRA — Secure by Design

The Cyber Resilience Act makes cybersecurity a **market-access condition** for
products with digital elements sold in the EU. No CE marking, no sale. And
unlike most of this repo, its core requirements are properties of the build, not
of a document: an SBOM the build produces, a product that ships with no known
exploitable vulnerabilities, a support period you have committed to, and a
disclosure channel someone actually reads.

The first question is not what to build. It is whether you are in scope at all,
because the answer is counterintuitive: **pure SaaS is generally out; monetised
open source is generally in.**

> **Not legal advice.** Scope, product classification and the conformity
> assessment route are legal judgements. This skill produces the technical
> artifacts and the gaps.

```
  in scope? ── commercial activity + placed on the market ── no ──► exclusion + expires_if
       │ yes
       ▼
  Annex I Part I  security requirements  ──► build properties
  Annex I Part II vulnerability handling ──► SBOM · CVD policy · updates
       │
       ▼
  support period (>= 5 years expectation) · reporting path (24h / 72h / 14d)
       │
       ▼
  technical documentation · declaration of conformity · CE marking
```

## Use this when

- You ship software someone runs on their own machine: a desktop app, a CLI, an
  agent, an SDK, a library, a container image, firmware, an on-premise build.
- You sell or monetise open source in any way — a paid tier, paid support,
  hosted-plus-binary. Monetisation is the trigger, not the licence.
- You make a physical product with software in it.
- An enterprise customer's procurement asks for an SBOM and a vulnerability
  disclosure policy, which is now routine and is the same work.

**Do not use this when** the product is purely a hosted service with nothing
distributed. SaaS is generally outside the CRA — though remote data processing
solutions **integral to a product with digital elements** are caught. If you
ship an agent, a desktop client, or a device alongside the service, the CRA
applies to that part. Record the exclusion with
`expires_if: any binary, agent, SDK, container image or device is distributed`.

**Non-monetised free and open-source software is outside scope**, and
"open-source software stewards" have a lighter regime. The moment there is a
commercial activity around it, that changes.

## Ask first

1. **"Is anything you make installed or run on a machine you do not operate?"**
   Binaries, containers, SDKs, agents, firmware. This is the scope question, in
   engineering terms.
2. **"Is it sold, licensed, bundled, or monetised in any way — including a paid
   tier, paid support, or a dual licence?"**
   Decides the commercial-activity limb for open source.
3. **"How long will you ship security updates, starting from when? What happens
   at the end of that period, and how will users know?"**
   The support period has to be a commitment, published, and honoured.
4. **"Can your build produce an SBOM today? Show me."**
   A concrete, closeable finding either way.
5. **"Where does someone report a vulnerability, and who reads that inbox?"**
   If the answer is a general support address nobody triages, that is the
   finding.
6. **"At your last release, did you know of any unpatched exploitable
   vulnerability in it?"**
   Annex I Part I requires products to be delivered without known exploitable
   vulnerabilities. This question usually surfaces a stale transitive dependency.

## What the law requires

> **Dates move.** Regulation (EU) 2024/2847 entered into force in December 2024,
> with vulnerability reporting obligations expected from 11 September 2026 and
> the main obligations from 11 December 2027. **Verify against the consolidated
> text** — and note that the reporting duty arrives more than a year before the
> rest, which changes what you build first.

### Annex I Part I — product security requirements

The essential requirements, in the order they bite in a codebase:

- Delivered **without known exploitable vulnerabilities**.
- Secure by default configuration, with the ability to reset to that state.
- Protection from unauthorised access, with appropriate authentication.
- Confidentiality and integrity of stored, transmitted and processed data —
  state-of-the-art encryption where relevant.
- **Data minimisation** — process only what is adequate, relevant and limited
  to what is necessary. Yes, in a cybersecurity regulation.
- Availability and resilience, including protection against denial of service.
- Minimised attack surfaces and mitigation of the impact of an incident.
- **Security-relevant logging and monitoring**, with an opt-out for the user.
- Secure update mechanism, with automatic updates available by default where
  appropriate and the ability to opt out.

### Annex I Part II — vulnerability handling

- Identify and document components, **including an SBOM covering at least the
  top-level dependencies**, in a commonly used machine-readable format.
- Address and remediate vulnerabilities without delay, including by providing
  **free security updates**.
- Apply effective and regular tests and reviews.
- **Publicly disclose** fixed vulnerabilities once a fix is available, with a
  description, the impact, the severity and remediation information.
- Enforce a **coordinated vulnerability disclosure policy**, published.
- Provide a contact address for reporting.
- Provide a secure distribution mechanism for updates, with prompt delivery and
  the ability to verify integrity.

### Reporting — Art. 14

For an **actively exploited vulnerability** or a **severe incident** affecting
the product's security, to the designated CSIRT and ENISA:

| Stage | Deadline | Content |
| --- | --- | --- |
| Early warning | **24 hours** of becoming aware | That it happened, Member States affected if known |
| Notification | **72 hours** | General information, status, corrective measures |
| Final report | **14 days** (vulnerability) / **1 month** (incident) | Description, severity, impact, remediation |

Twenty-four hours is short, and it starts from awareness, not from triage. Wire
this into the on-call runbook now — see `skills/incident-response`, where this
clock collides with NIS2's and GDPR's.

### Support period

At least five years, or the expected product lifetime if shorter. Must be
stated at the point of sale, and security updates must remain available for at
least ten years after the last unit was placed on the market (or for the support
period, whichever is longer). *Verify the current text; this provision was
amended during negotiation.*

## What to produce

**1. An SBOM the build produces**, never hand-maintained:

```bash
# CycloneDX or SPDX, generated per release, committed with the tag
syft dir:. -o cyclonedx-json > compliance/sbom/$(git describe --tags).cdx.json
grype sbom:compliance/sbom/$(git describe --tags).cdx.json --fail-on high
```

The second line is the Annex I Part I requirement expressed as a build step: if
a known exploitable vulnerability at high severity is present, the release does
not ship. A hand-written SBOM is out of date on the day it is written and is
worse than none, because it looks authoritative.

**2. A published CVD policy and a reachable contact.** The minimum is a
`security.txt` at `/.well-known/security.txt` and `SECURITY.md` in the repo,
naming an inbox that a named person triages, with a stated response time.

```
Contact: mailto:security@example.com
Expires: 2027-01-01T00:00:00.000Z
Policy: https://example.com/security/disclosure
Preferred-Languages: en, fi
```

**3. The support period, in three places**: the product documentation, the
declaration of conformity, and `compliance.yaml`. And a mechanism to tell users
when it ends — an end-of-life notice in the product, not only on a web page.

**4. Vulnerability handling records.** For each: discovery date and source,
affected versions, severity, fix version, disclosure date, and the reporting
decision with its reasoning. Including the ones you decided were not reportable —
the reasoning is the evidence, the same way GDPR Art. 33(5) works.

**5. Technical documentation and the declaration of conformity.** Skeleton now,
filled as you build. It has to describe the design, the risk assessment, the
Annex I requirements and how each is met, and the vulnerability handling
processes.

**6. The 24-hour reporting path, tested.** Who declares, who writes, where it is
sent, and a template with the fields pre-filled. Run it once as a drill; a
reporting path that has never been exercised is a document, not a capability.

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

- **Assuming SaaS is out, while shipping an agent.** The desktop client, the
  CLI, the on-prem connector and the container image are products. The hosted
  part being out of scope does not carry them.

- **Assuming open source is out.** Non-monetised FOSS is out. A paid tier, paid
  support, or a dual licence is a commercial activity.

- **A hand-maintained SBOM.** Stale on day one, and it misrepresents the
  dependency tree to anyone relying on it.

- **An SBOM with no vulnerability gate.** Producing the document without using
  it satisfies the paperwork and not the requirement to ship free of known
  exploitable vulnerabilities.

- **`security@` routed to a support queue nobody triages.** A CVD policy with no
  reader is worse than no policy: you now have a documented channel through
  which reports demonstrably arrived and were ignored.

- **No support period, or a vague one.** "We support current versions" is not a
  period. It has to have a start, a length, and an end-of-life notification.

- **Discovering the 24-hour clock during an incident.** It starts at awareness.
  Build the path before you need it.

- **Confusing CRA with NIS2.** CRA regulates the product you ship; NIS2
  regulates the organisation running services. Many companies are under both,
  for different things, with different regulators and different clocks.

## Verify

Follow `references/verification.md`. For this skill specifically:

1. **Tier 0** — install, `--help`, generate an SBOM and validate it.

2. **Tier 1** — `pytest -q`, offline:

```python
def test_saas_only_is_out_of_scope_with_an_expiry(brief_saas):
    exclusion = assess(brief_saas).ruled_out[0]
    assert exclusion["regime"] == "cra"
    assert "agent" in exclusion["expires_if"] or "binary" in exclusion["expires_if"]


def test_shipping_an_agent_puts_saas_in_scope(brief_saas_with_agent):
    assert "cra" in {r["regime"] for r in assess(brief_saas_with_agent).applicable}


def test_monetised_open_source_is_in_scope(brief_oss_paid_tier):
    assert "cra" in {r["regime"] for r in assess(brief_oss_paid_tier).applicable}


def test_non_monetised_oss_is_out(brief_oss_free):
    assert "cra" in {r["regime"] for r in assess(brief_oss_free).ruled_out}


def test_sbom_is_generated_not_committed_by_hand(repo):
    assert "sbom" in build_steps(repo)
    assert not hand_edited(repo / "compliance/sbom")


def test_sbom_parses_and_covers_top_level_dependencies(sbom, manifest):
    parsed = parse_cyclonedx(sbom)
    assert set(top_level(manifest)) <= {c.name for c in parsed.components}


def test_known_exploitable_dependency_blocks_the_release(repo_with_cve):
    result = release_gate(repo_with_cve)
    assert result.blocked
    assert result.finding.citation.startswith("Annex I Part I")


def test_support_period_is_recorded_and_non_zero(brief):
    assert brief.cra["support_period_months"] >= 1
    assert brief.cra["support_starts"]


def test_missing_support_period_is_a_condition(brief_without_period):
    finding = assess(brief_without_period).finding_for("support period")
    assert finding.severity == "condition"


def test_cvd_contact_exists_and_is_owned(repo):
    assert (repo / ".well-known/security.txt").exists()
    assert parse_security_txt(repo).contact
    assert brief.cra["cvd_owner"]           # a person, not an alias


def test_reporting_clocks_are_computed_from_awareness(incident):
    plan = reporting_plan(incident, aware_at="2026-09-15T08:00:00Z")
    assert plan.early_warning_due == "2026-09-16T08:00:00Z"     # 24h
    assert plan.notification_due == "2026-09-18T08:00:00Z"      # 72h
    assert plan.final_due == "2026-09-29T08:00:00Z"             # 14d


def test_non_reported_vulnerabilities_record_their_reasoning(register):
    for entry in register:
        if not entry.reported:
            assert entry.reasoning


def test_dates_carry_a_verification_note():
    text = render(assess(brief))
    for line in dates_in(text):
        assert "verify" in line.lower() or "Art." in line
```

3. **Tier 2** — report: SBOM component count and format, open known-exploitable
   findings at the current HEAD, the support period, whether the CVD contact
   resolves to a named owner, and whether the reporting drill has ever been run.

4. **Tier 3** — run the disclosure path end to end. Send a report to the
   published address from outside the company and time how long it takes to
   reach a human who can act. That number is the honest measure of the control,
   and it is usually a surprise.

Then tell the user which dates you could not verify against the consolidated
text, and flag that the reporting obligations and the main obligations have
different start dates — that gap changes what to build first.
