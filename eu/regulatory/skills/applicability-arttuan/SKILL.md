---
name: applicability-arttuan
title: Applicability
description: Decide which EU regimes apply from the facts in the brief, and record the ruled-out ones with the fact that decides each and the condition that would revive it
author: ArttuAn
author_url: https://github.com/ArttuAn/eu-compliance-skills/tree/main/skills/applicability
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# Applicability

Which regimes actually apply. Run this immediately after `eu-grill-me`, from the
answers it recorded, before any regime-specific skill.

The output people expect is a list of what applies. The output that matters is
**the other list**: what does not apply, the fact that decides it, and the
condition that would make it apply again. That second list is what diligence
reads, what stops the next engineer re-litigating the question every quarter,
and what `eu-compliance-gates` watches for expiry.

> **Not legal advice.** Applicability turns on facts and on national
> implementations. This skill produces a defensible first pass and a list of
> what counsel needs to confirm — not a scoping opinion.

```
  compliance.yaml (facts)
        │
        ▼
  for each regime: evaluate the trigger against the facts
        │
   ┌────┴─────┐
   ▼          ▼
applies   does not apply
   │          │
   │          ├─► reason  (the rule)
   │          ├─► deciding_fact  (the answer, cited by question id)
   │          └─► expires_if  (what would flip it) ──► watched in CI
   ▼
 duties list ──► hand to the regime skill
```

## Use this when

- Straight after `eu-grill-me`, always. It is the routing step for every other
  skill in this repo.
- When a fact changes that could cross a threshold: a hire that takes you past
  50 staff, a new market, a new feature category, a first paid tier on an
  open-source project.
- When someone asks "does the AI Act apply to us" and you want an answer with a
  reason attached rather than a vibe.

**Do not use this when** the brief is empty or stale. This skill reads facts; it
does not gather them. Run the grill first.

## Ask first

Most of what this needs is already in the brief. Ask only for what is missing,
and only these:

1. **"Headcount and annual turnover or balance sheet total?"**
   Three regimes have size thresholds and they use different ones. Get real
   numbers, and get the group-level number if there is a parent company.
2. **"Which Member States are you established in, and which do you sell into?"**
   Establishment decides which supervisory authority and which national
   transposition. Selling into decides the extraterritorial triggers.
3. **"Is any part of the group in a regulated sector — finance, health, energy,
   transport, telecoms, public administration?"**
   Sectoral regimes (DORA, MDR, NIS2) stack on top of everything else and are
   easy to miss when scoping a product rather than an entity.
4. **"Has anyone — counsel, a DPO, an auditor — already scoped this?"**
   If yes, read theirs. Your job becomes checking it against current facts, not
   producing a competing document that disagrees with it.

## What the law requires

There is no "applicability assessment" obligation by that name. There are three
duties that make one necessary:

- **GDPR Art. 5(2) accountability** — you must be able to demonstrate
  compliance, which presupposes knowing what you are complying with.
- **GDPR Art. 30** — the record of processing is itself a scoping document, and
  it must exist before you can claim to know your obligations.
- **AI Act Art. 6 and Annex III** — classification is a duty placed on the
  provider, and Art. 6(3)'s derogation is only available if you *document the
  assessment* before placing the system on the market. An undocumented
  conclusion that you are not high-risk is not a derogation.

And commercially: an unscoped product is one that cannot answer a security
questionnaire, survive diligence, or price its own compliance work.

## The trigger table

Evaluate each in order. `references/regime-map.md` has the dates, the penalties
and the primary sources.

| Regime | Applies if | Decisive facts from the brief |
| --- | --- | --- |
| **GDPR** | Established in the EU, **or** offering goods/services to, or monitoring, people in the Union (Art. 3) | `subject.eu_establishment`, `subject.targets_eu_users`, `data.categories` non-empty |
| **ePrivacy** | Anything is stored on or read from a user's terminal equipment that is not strictly necessary (Art. 5(3)) | Branch C answers |
| **AI Act** | An AI system is placed on the market, put into service, or its output is used in the Union | `ai.uses_ai`, `roles.ai_act` |
| **EAA** | Covered consumer product or service, sold in the EU, and not a service microenterprise | Branch G, `subject.headcount`, `subject.turnover_eur` |
| **CRA** | A product with digital elements is placed on the EU market in the course of a commercial activity | Branch D, `roles.cra` |
| **NIS2** | Medium-or-larger entity in an Annex I or II sector, **per national transposition** | Branch E, size, sector, Member States |
| **DSA** | Hosting information supplied by a user, at any layer | Branch F, `roles.dsa` |
| **Data Act** | Connected product or related service; or a data-processing service provider | Product type |
| **DORA** | Regulated financial entity, or a critical ICT provider to one | Sector |
| **PLD** | Supplying software as a product | Almost always, once transposed |
| **MDR** | The software has a medical purpose | Intended purpose, as stated in marketing |

### Thresholds that need arithmetic, not judgement

Get these exactly right; they are where scoping is most often wrong, and they
are testable at the boundary.

```python
def nis2_size_cap(headcount: int, turnover_eur: float, balance_sheet_eur: float) -> bool:
    """Medium enterprise or above: the trigger is OR, not AND."""
    return headcount >= 50 or turnover_eur > 10_000_000 or balance_sheet_eur > 10_000_000


def eaa_service_microenterprise(headcount: int, turnover_eur: float,
                                balance_sheet_eur: float) -> bool:
    """Exempt for SERVICES only, and only when BOTH limbs are satisfied."""
    return headcount < 10 and (turnover_eur <= 2_000_000 or balance_sheet_eur <= 2_000_000)


def dsa_section3_exempt(headcount: int, turnover_eur: float) -> bool:
    """Micro and small enterprises are exempt from the online-platform duties in
    Section 3. Hosting duties (Arts. 16-18) still apply."""
    return headcount < 50 and turnover_eur <= 10_000_000
```

Three traps in those three functions, and each has cost somebody a scoping
error:

- **NIS2 uses OR**; the EAA microenterprise test uses **AND**. Swapping them
  gets the answer backwards.
- **The DSA exemption is partial.** A small startup hosting user content is
  exempt from Section 3 and still owes notice-and-action under Art. 16. "We are
  too small for the DSA" is wrong.
- **Use group-level figures** where the relevant law says to. A subsidiary under
  the cap inside a group over it is usually not exempt.

### The AI Act Art. 6(3) derogation, done honestly

The most commonly abused provision in current practice. A system listed in
Annex III is *not* high-risk if it performs a narrow procedural task, improves
the result of a prior human activity, detects decision patterns without
replacing human assessment, or performs a preparatory task — **unless it
profiles natural persons**, in which case the derogation is unavailable.

```python
def art_6_3_available(system) -> tuple[bool, str]:
    if system.profiles_natural_persons:
        return False, ("Art. 6(3) third subparagraph: the derogation is not "
                       "available where the system performs profiling of natural persons")
    if not system.derogation_ground:
        return False, "no Art. 6(3) ground asserted"
    return True, f"asserted ground: {system.derogation_ground} - requires documented assessment"
```

Two things to carry into the brief:

- **Profiling kills it.** Scoring, ranking or categorising individuals is
  profiling. Most Annex III candidates people want to except are exactly this.
- **Relying on it is not free.** The assessment must be documented before the
  system is placed on the market, and the system must still be registered in the
  EU database. A derogation you did not write down is a conclusion, not a
  derogation.

## What to produce

Fill both lists in `compliance.yaml`. The exclusion entries are the valuable
part and every field is load-bearing:

```yaml
regimes:
  applicable:
    - regime: gdpr
      trigger: "Art. 3(2) - offers a service to applicants in DE, FI, NL"
      deciding_facts: [A-01, orient-2]
      duties_skill: eu-gdpr-data-map
    - regime: ai_act
      trigger: "provider of an AI system placed on the EU market"
      deciding_facts: [B-07]
      open_question: "Annex III(4)(a) classification - counsel to confirm"
      duties_skill: eu-ai-act

  ruled_out:
    - regime: nis2
      reason: "below the size cap in every Member State of establishment"
      deciding_fact: "E-01: 28 staff, EUR 4.2M turnover, EUR 3.1M balance sheet"
      rule: "medium enterprise = headcount >= 50 OR turnover > 10M OR balance sheet > 10M"
      confirmed_by: "counsel, 2026-09-10"
      expires_if: "headcount >= 50 or turnover_eur > 10000000 or balance_sheet_eur > 10000000"
    - regime: dsa
      reason: "stores no information provided by a recipient of the service"
      deciding_fact: "F-01: no user-visible content from other users"
      expires_if: "any feature lets one user publish content another user can see"
    - regime: cra
      reason: "hosted SaaS only; nothing is placed on the market as a product"
      deciding_fact: "orient-4"
      expires_if: "an on-premise build, agent, SDK or device is distributed"
```

Rules for the ruled-out list:

- **`expires_if` is mandatory and must be machine-evaluable** where possible.
  `eu-compliance-gates` evaluates it on every push; a prose-only condition
  degrades to a reminder, which is better than nothing and much worse than a
  check.
- **`deciding_fact` cites a question id.** An exclusion whose basis is not
  traceable to an answer is an assertion.
- **`confirmed_by` is optional but changes the weight.** "Counsel confirmed on
  this date" and "the agent's read of the size cap" are different artifacts;
  render both honestly rather than flattening them.
- **Never rule out GDPR on "we're not in the EU."** Art. 3(2) exists. If you
  are genuinely outside it, say which limb fails and why.

Then write, in the Markdown brief, a short **"what we are not doing and why"**
section. It is the most-read section of the document.

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

- **Only the applicable list is produced.** The brief reads as thorough and
  answers none of the questions diligence asks. Half a document.

- **Exclusions with no expiry condition.** True on the day, silently false six
  months later, and nothing notices. The 50th hire is the classic.

- **Scoping the product, not the entity.** NIS2, DORA and the management duties
  attach to the organisation. A perfect product scope misses them entirely.

- **Swapping AND for OR** in the size caps. NIS2 is OR; the EAA microenterprise
  test is AND. Test both at the boundary.

- **"We're too small for the DSA."** The hosting duties have no size exemption.
  Only Section 3 does.

- **Claiming Art. 6(3) because the output is advisory.** If it profiles people,
  the derogation is unavailable regardless of how advisory the output is.

- **Treating a Directive as settled by its own text.** NIS2, ePrivacy, the EAA
  and the PLD bind through national law, which differs and is sometimes late.
  Name the Member State and say when you could not read its transposition.

- **Producing a conclusion where a question belongs.** "The AI Act does not
  apply" is a legal conclusion. "No AI system was identified in the answers to
  orient-3 and B-01; if that changes, the AI Act applies" is a finding.

## Verify

Follow `references/verification.md`. For this skill specifically:

1. **Tier 0** — install, `--help`, run against a fixture brief and get both
   lists.

2. **Tier 1** — `pytest -q`, offline:

```python
def test_both_lists_are_produced(brief):
    result = assess(brief)
    assert result.applicable and result.ruled_out


def test_every_exclusion_has_an_expiry_and_a_deciding_fact(brief):
    for exclusion in assess(brief).ruled_out:
        assert exclusion["expires_if"]
        assert exclusion["deciding_fact"]


def test_nis2_size_cap_at_the_boundary():
    assert nis2_size_cap(49, 9_000_000, 9_000_000) is False
    assert nis2_size_cap(50, 0, 0) is True                  # OR, not AND
    assert nis2_size_cap(10, 10_000_001, 0) is True


def test_eaa_microenterprise_needs_both_limbs():
    assert eaa_service_microenterprise(9, 1_000_000, 1_000_000) is True
    assert eaa_service_microenterprise(11, 1_000_000, 1_000_000) is False
    assert eaa_service_microenterprise(9, 5_000_000, 5_000_000) is False


def test_dsa_exemption_is_partial(brief_small_host):
    duties = assess(brief_small_host).duties_for("dsa")
    assert "Art. 16" in duties                              # hosting duties survive
    assert "Art. 20" not in duties                          # Section 3 does not


def test_exclusion_flips_when_the_deciding_fact_changes(brief):
    brief.subject["headcount"] = 60
    assert "nis2" in {r["regime"] for r in assess(brief).applicable}


def test_gdpr_is_not_ruled_out_on_non_establishment(brief_us_company):
    result = assess(brief_us_company)
    assert "gdpr" in {r["regime"] for r in result.applicable}


def test_profiling_blocks_the_art_6_3_derogation():
    available, reason = art_6_3_available(system(profiles_natural_persons=True,
                                                 derogation_ground="preparatory task"))
    assert available is False and "profiling" in reason


def test_no_legal_conclusions_in_the_rendered_output(brief):
    text = render(assess(brief)).lower()
    assert "does not apply to you" not in text
    assert "you are compliant" not in text
```

3. **Tier 2** — report the counts: regimes applicable, ruled out, and how many
   exclusions have a machine-evaluable `expires_if`. That last ratio is the one
   that predicts whether the scoping survives contact with a growing company.

4. **Tier 3** — counsel reviews the ruled-out list specifically. That is where a
   scoping error hides, and it is cheap to check and expensive to get wrong.

Then tell the user which exclusions rest on your reading rather than on
confirmed advice, and name every national transposition you could not read.
