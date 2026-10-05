---
name: accessibility-arttuan
title: Accessibility
description: Turn the European Accessibility Act into numbered, testable acceptance criteria against EN 301 549 / WCAG, plus the accessibility statement
author: ArttuAn
author_url: https://github.com/ArttuAn/eu-compliance-skills/tree/main/skills/accessibility
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# Accessibility

The European Accessibility Act is the regime most likely to apply to an ordinary
product and least likely to be scoped. It is not a design preference: for
covered products and services sold in the EU it is market-access law, enforced
by national authorities, with withdrawal from the market as the remedy.

The good news is that it is the only regime in this repo that is **fully
testable**. Every obligation maps to a numbered clause with a pass/fail check,
much of it automatable. So this skill's job is to convert "make it accessible"
into acceptance criteria a developer can close and CI can enforce.

> **Not legal advice.** Scope, the microenterprise exemption and any
> disproportionate-burden claim are legal judgements. This skill produces the
> testable criteria and the gaps.

```
  in scope? ──no──► record the exclusion + expires_if
       │ yes
       ▼
  EN 301 549 clauses that apply to this surface
       │
       ▼
  numbered acceptance criteria ──► automated (~30%) + manual (~70%)
       │
       ▼
  CI gate · accessibility statement · disproportionate-burden file if claimed
```

## Use this when

- The product is e-commerce, consumer banking, e-books, transport, telephony, or
  audiovisual media access — sold to consumers in the EU.
- You are a public sector body in the EU (Web Accessibility Directive
  2016/2102), where the duty is older and the accessibility statement is
  mandatory and formatted.
- Enterprise procurement is asking for a VPAT or an EN 301 549 conformance
  statement, which is increasingly a precondition for selling to anyone large.

**Do not use this when** you are a service microenterprise under both limbs —
fewer than 10 staff **and** turnover or balance-sheet total at or below €2M —
and the product is a service rather than a product. Record the exclusion with
`expires_if: headcount >= 10 or turnover_eur > 2000000`, because it is the
exclusion most likely to expire without anyone noticing.

Build it anyway if you can. Accessibility work done during the build costs a
fraction of accessibility work done under a deadline, and the microenterprise
exemption does not survive growth.

## Ask first

Skip "is it accessible" — nobody can answer it. Ask what can be tested.

1. **"What is the primary task a user comes here to do? Name the top three."**
   Accessibility is assessed on journeys, not pages. This scopes the work to
   something finishable.
2. **"Can each of those be completed with a keyboard only — no mouse — at 200%
   browser zoom, with a screen reader?"**
   The honest triage. If the answer is "I don't know", that is the first task.
3. **"Which surfaces are in scope? Web, native mobile, email, PDF documents,
   video, a kiosk or terminal?"**
   Each has different EN 301 549 clauses. PDFs and video are the two that get
   forgotten and are the most expensive to retrofit.
4. **"Headcount, turnover, balance sheet total?"**
   The exemption needs both limbs.
5. **"Is there any existing audit, VPAT, or accessibility statement?"**
   If yes, its date matters more than its contents. An audit older than the last
   redesign is not evidence of anything.

## What the law requires

**Directive (EU) 2019/882 (EAA)** — applies to covered products and services
placed on the EU market. Applied from 28 June 2025; transposed nationally, so
the binding text is the national law. *Verify the national transposition for
each Member State you sell into.*

**Directive (EU) 2016/2102** — public sector bodies' websites and mobile apps,
with a mandatory, formatted accessibility statement and a feedback mechanism.

**EN 301 549** is the harmonised standard. Conformity with a harmonised standard
gives a **presumption of conformity** — a legal effect, and the cheapest route
to compliance. Version 3.2.1 references WCAG 2.1 Level AA; later versions align
with WCAG 2.2. *Check which version is cited in the current OJ list of
harmonised standards for the EAA before declaring conformity against it.*

Target **WCAG 2.2 AA** in practice. It is a superset, the extra criteria are
cheap (focus appearance, dragging alternatives, consistent help, accessible
authentication), and it future-proofs against the standard moving under you.

### The clause groups that matter

| Group | EN 301 549 | What it covers |
| --- | --- | --- |
| Web | § 9 | WCAG A + AA applied to web content |
| Non-web documents | § 10 | PDFs, Office documents, e-books |
| Software | § 11 | Native and desktop applications |
| Support services | § 12 | Help desks, documentation — must itself be accessible |
| ICT with two-way comms | § 6 | Real-time text, video quality |
| Hardware / terminals | § 8 | Kiosks, ATMs, ticket machines |

**§ 12 catches people out.** Your support channel and your documentation are in
scope. A perfectly accessible product whose only help route is an inaccessible
chat widget fails.

### Disproportionate burden

The derogation exists and it is narrow. It must be **assessed, documented,
quantified** — the cost of compliance against the organisation's size and
resources, and the benefit to people with disabilities — and **reassessed
periodically**. It cannot be claimed because the work is inconvenient, and a
claim resting on the cost of a redesign you wanted anyway will not hold.

An undocumented claim of disproportionate burden is not a derogation; it is a
written admission of non-conformity. Treat any claim as a `condition` with a
required document and a review date.

## What to produce

**1. Numbered acceptance criteria**, one per applicable clause, in a form a
developer can close:

```yaml
- id: AC-014
  clause: "EN 301 549 § 9.1.4.3 (WCAG 1.4.3 Contrast Minimum)"
  surface: web
  journey: checkout
  criterion: >
    All text and images of text have a contrast ratio of at least 4.5:1
    (3:1 for text at 18pt / 14pt bold or larger) against their background.
  test: automated
  tool: "axe-core rule color-contrast"
  status: fail
  evidence: "reports/axe/checkout-2026-09-15.json"

- id: AC-021
  clause: "EN 301 549 § 9.2.4.3 (WCAG 2.4.3 Focus Order)"
  surface: web
  journey: checkout
  criterion: >
    Tabbing through the checkout reaches every interactive element in an order
    that preserves meaning, and focus never enters a hidden region.
  test: manual
  method: "keyboard-only walkthrough, documented in reports/manual/checkout.md"
  status: pass
```

**Automated tooling catches roughly a third of WCAG failures.** That is worth
having and it is not a conformance claim. axe-core, Lighthouse and pa11y find
missing alt text, contrast, form labels and landmark issues; they cannot tell
you whether the alt text is *right*, whether focus order preserves meaning, or
whether an error message is understandable. Mark each criterion `automated` or
`manual` honestly, and never report an automated pass as conformance.

**2. A CI gate**, on the journeys only:

```yaml
- name: accessibility
  run: |
    npx playwright test tests/a11y --reporter=json
    npx axe-ci --exit-one-on-violation \
        --include "$(cat compliance/a11y/journeys.txt)"
```

Gate the primary journeys, not every page. A gate that fails on a marketing page
typo gets disabled, and then the checkout regresses unnoticed.

**3. The accessibility statement**, published and reachable:

- Which standard and version you conform to, and the conformance level.
- **What is not accessible**, specifically, with the reason and the date it will
  be fixed. This section is what makes the statement credible; a statement
  claiming full conformity with no exceptions is read as a statement nobody
  tested.
- Any disproportionate-burden claim, with the assessment referenced.
- A feedback mechanism, and what happens to feedback.
- The date of the last assessment and the method used.

For public sector bodies the statement has a **prescribed model format** in
Commission Implementing Decision (EU) 2018/1523 — use it rather than writing
your own.

**4. Manual test evidence.** A dated walkthrough per journey: keyboard only,
screen reader (NVDA or VoiceOver named, with version), 200% zoom, 320px
viewport. Store it with the report. A manual criterion marked `pass` with no
evidence file is a finding.

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

- **Automated pass reported as conformance.** axe returns zero violations, the
  team declares WCAG AA. Roughly two-thirds of the criteria were never tested.

- **Scoping to pages instead of journeys.** An accessibility programme that
  never finishes because the page count grows faster than the fixes. Pick the
  top three tasks and make those complete.

- **Forgetting documents, video and support.** PDFs (§ 10), captions and audio
  description (§ 7), and the help channel (§ 12). All in scope, all commonly
  omitted, all expensive to retrofit.

- **The microenterprise exemption assumed and never re-checked.** Both limbs
  required, and it expires with the tenth hire. `expires_if` in the brief.

- **Disproportionate burden claimed without an assessment.** Not a derogation;
  an admission.

- **An accessibility statement with no known issues.** Reads as untested,
  because it is. List the gaps with dates.

- **A stale audit.** An assessment older than the last redesign is evidence
  about software that no longer exists. Date everything and re-test on redesign.

- **Overlays sold as compliance.** Third-party accessibility overlay widgets do
  not make a site conformant and are the subject of significant litigation and
  negative guidance. If one is in the codebase, that is a finding.

## Verify

Follow `references/verification.md`. For this skill specifically:

1. **Tier 0** — install, `--help`, generate criteria for a fixture and render
   the statement.

2. **Tier 1** — `pytest -q`, offline:

```python
def test_every_criterion_cites_a_numbered_clause(criteria):
    for ac in criteria:
        assert re.match(r"EN 301 549 § \d+\.\d+", ac.clause)
        assert "WCAG" in ac.clause


def test_manual_and_automated_are_labelled_honestly(criteria):
    automated = [ac for ac in criteria if ac.test == "automated"]
    assert len(automated) / len(criteria) < 0.5      # tooling covers ~1/3, not most


def test_automated_pass_is_not_reported_as_conformance(report):
    text = render(report).lower()
    assert "conforms to wcag" not in text or report.manual_complete


def test_microenterprise_exemption_needs_both_limbs():
    assert exempt_service(9, 1_000_000) is True
    assert exempt_service(10, 1_000_000) is False
    assert exempt_service(9, 3_000_000) is False


def test_exemption_records_an_expiry(brief_micro):
    exclusion = assess(brief_micro).ruled_out[0]
    assert "headcount >= 10" in exclusion["expires_if"]


def test_support_and_documents_are_in_scope(criteria_for_web_with_pdfs):
    clauses = {ac.clause for ac in criteria_for_web_with_pdfs}
    assert any("§ 10" in c for c in clauses)         # non-web documents
    assert any("§ 12" in c for c in clauses)         # support services


def test_disproportionate_burden_requires_a_document(brief_claiming_burden):
    finding = assess(brief_claiming_burden).finding_for("disproportionate burden")
    assert finding.severity == "condition"
    assert "quantified assessment" in finding.needs


def test_statement_lists_known_gaps(statement, criteria_with_failures):
    assert "not accessible" in statement.lower()
    for failing in [ac for ac in criteria_with_failures if ac.status == "fail"]:
        assert failing.clause in statement


def test_manual_pass_without_evidence_is_a_finding(criteria):
    ac = criteria.by_id("AC-021")
    ac.status, ac.evidence = "pass", None
    assert validate(ac)[0].severity == "condition"


def test_ci_gate_covers_journeys_not_every_page(config):
    assert config.include == read_journeys()
    assert "*" not in config.include


def test_overlay_dependency_is_a_finding(repo_with_overlay):
    assert any("overlay" in f.statement.lower() for f in scan(repo_with_overlay))
```

3. **Tier 2** — report: criteria total, split automated/manual, pass rate on
   each, and journeys fully covered. Lead with the **manual** pass rate, because
   the automated one flatters.

4. **Tier 3** — a person who uses a screen reader daily completes the primary
   journey. No tool and no checklist substitutes for this, and it finds things
   the standard does not describe. Budget for it once before launch.

Then tell the user which EN 301 549 version you assessed against, that you could
not verify which version is currently cited in the OJ, and exactly which
criteria were never tested rather than implying full coverage.
