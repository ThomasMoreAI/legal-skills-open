---
name: evidence-pack-arttuan
title: Evidence Pack
description: Assemble the documents a regulator, auditor or acquirer actually asks for — generated from the brief and the build, with placeholders counted rather than hidden
author: ArttuAn
author_url: https://github.com/ArttuAn/eu-compliance-skills/tree/main/skills/evidence-pack
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# Evidence Pack

Compliance is a claim you have to prove, to someone who was not there, months or
years later. This skill assembles the proof: the documents, the contracts, the
generated artifacts, and the one thing most packs are missing — a record of what
you decided **not** to do and why.

The property that matters is that evidence has to exist **before** you need it.
Every document here is trivial to produce while building and nearly impossible
to reconstruct honestly eighteen months later, when the people have left and the
vendor has changed their terms. So this skill runs alongside the build, not
after it.

> **Not legal advice.** A complete pack is not a compliance opinion. It is the
> material a lawyer, auditor or supervisor needs in order to form one.

```
  compliance.yaml + the repo
        │
        ▼
  per applicable regime: which documents are owed?
        │
   ┌────┴────┐
   ▼         ▼
 generate  collect   ──► SBOM, ROPA, erasure test, consent log, ADRs
 (build)   (people)      DPAs, SCCs, TIAs, board minutes, audits
        │
        ▼
  completeness report ──► placeholders COUNTED, never shipped as prose
```

## Use this when

- Enterprise procurement or a security questionnaire has arrived, which is the
  usual trigger and is already slightly late.
- Due diligence is starting — fundraising or acquisition. The ruled-out list and
  the decision records are what diligence reads most closely.
- A supervisory authority has written to you. Then the register of what you
  decided and when is the whole game.
- Continuously, as a build step, which is the only version of this that works.

**Do not use this when** the brief is empty. This skill assembles; it does not
decide. Run `eu-grill-me` and the regime skills first, or you will produce a
folder of headings.

## Ask first

1. **"Who is asking, and what for?"**
   A customer questionnaire, a diligence data room and a supervisory authority
   want different subsets, at different depths. Assembling everything for a
   questionnaire wastes a week.
2. **"What already exists, and when was it last true?"**
   A policy dated three years ago describes software that no longer exists.
   Dates matter more than contents.
3. **"Name every processor, and tell me where the signed DPA for each one is."**
   The gap between the vendor list and the DPA folder is usually the largest
   single finding.
4. **"Who can sign? Who is the accountable owner for each document?"**
   An unowned document does not get maintained.
5. **"Is there anything in here you would not want read aloud?"**
   Ask it directly. An evidence pack containing a candid internal memo about a
   known gap is a different artifact from one that does not, and the time to
   discover that is now.

## What the law requires

The duties that make a pack necessary, by regime. `references/evidence.md` has
the full list and the practical notes.

| Regime | The documentation duty | Citation |
| --- | --- | --- |
| GDPR | Demonstrate compliance; records of processing; processor contracts; breach register including non-notified | Arts. 5(2), 30, 28(3), 33(5) |
| AI Act | Technical documentation; logs; instructions for use; declaration of conformity; registration | Arts. 11-12, 13, 47-49, Annex IV |
| CRA | Technical documentation; SBOM; vulnerability handling records; declaration of conformity | Annex I Part II, Annex VII |
| NIS2 | Policies for each Art. 21(2) measure; management approval; incident records | Arts. 20, 21, 23 |
| EAA | Conformity assessment; accessibility statement; disproportionate-burden assessment | Directive 2019/882 |
| DSA | Terms and conditions; statements of reasons; transparency report | Arts. 14, 17, 15 |

## What to produce

```
compliance/
├── compliance.yaml              # the brief - the spine
├── COMPLIANCE-BRIEF.md          # generated
├── ropa.yaml                    # Art. 30, generated from the data map
├── decisions/                   # ADRs: bases chosen and rejected, classifications, exclusions
│   └── 0004-li-for-training-data.md
├── vendors/                     # one file per processor
│   └── openai.md                # DPA, sub-processors, location, notice period, TIA
├── dpia/                        # per-processing assessments
├── ai/
│   ├── technical-documentation.md   # Annex IV skeleton, filled as you build
│   └── logs-design.md               # Art. 12: what an event is, retention, minimisation
├── sbom/                        # per release tag, generated
├── incidents/                   # register, including non-notified, with reasoning
├── statements/                  # privacy notice (versioned), accessibility statement, CVD policy
├── tests/                       # erasure test results, restore test, a11y reports
└── COMPLETENESS.md              # generated: what is missing, and how much
```

### Generate what can be generated

The most credible parts of a pack are the parts nobody wrote:

| Artifact | Generated by | Why it convinces |
| --- | --- | --- |
| SBOM | `syft` / `cdxgen` at build | Timestamped, tied to a commit |
| ROPA | From the data map | Cannot drift from the schema |
| Erasure test result | CI | Proves Art. 17 works rather than describing it |
| Restore test result | CI or a scheduled job | NIS2 Art. 21(2)(c) needs a *tested* restore |
| Consent log | The consent mechanism | Art. 7(1) demonstrability, per user, per notice version |
| Accessibility report | axe + manual walkthrough | Dated against a named tool version |
| Decision records | git | Dated, attributed, diffable |

A generated artifact with a commit hash cannot have been written the week the
letter arrived. A polished PDF can.

### The vendor file

One per processor, and the fields are chosen so the gaps are visible:

```yaml
vendor: OpenAI
role: processor
purpose: "generate screening notes from application text"
data_sent: ["applicant.cv_text", "applicant.answers"]
dpa: {signed: true, path: "vendors/openai/dpa-2026-03-11.pdf", date: "2026-03-11"}
subprocessors: {named: false, url: null}          # a finding: Art. 28(2)
location: {primary: US, support_access: US}
transfer: {mechanism: scc, module: 2, tia: null}  # a finding: no TIA
breach_notice_period: "72 hours"                  # consumes your whole GDPR window
audit_rights: true
deletion_on_termination: "30 days"
reviewed: {by: "Priya", on: "2026-09-12"}
```

`subprocessors.named: false` and `tia: null` are findings the moment the file is
written. That is the point of the schema — the shape makes the hole obvious.

`breach_notice_period` is the field teams never think about and is the one that
matters most operationally: a processor permitted 72 hours to tell you has
consumed your entire GDPR window before you knew anything happened.

### The decision record

The section diligence reads most closely, and almost nobody writes:

```markdown
# ADR-0004: Lawful basis for training on historical applicant data

Date: 2026-09-14 · Owner: Priya Nair · Confirmed by: counsel (M. Laine)

## Context
We want to fine-tune the ranker on 3 years of historical applications.

## Options considered
1. Consent (Art. 6(1)(a)) — rejected: applicants applied for a job, not to
   train a model; refusal must be costless and here it is not credible.
2. Contract (Art. 6(1)(b)) — rejected: training is not necessary to perform the
   contract with the applicant whose data it is.
3. Legitimate interests (Art. 6(1)(f)) — chosen, with a balancing test.

## Decision
Art. 6(1)(f), limited to applications from the last 24 months, with free-text
fields redacted for Art. 9 categories before training. LIA at dpia/lia-0004.md.

## Consequences
Applicants get an Art. 21 objection route in the privacy notice. Retention for
this purpose is capped at 24 months, enforced by jobs/purge_training_set.py.
```

Options **rejected**, with reasons, is what makes this survive scrutiny. A record
that states only the outcome reads as a decision reverse-engineered afterwards.

### Completeness, counted

```python
def completeness(pack) -> dict:
    required = documents_required(pack.brief)      # from the applicable regimes
    present = [d for d in required if pack.exists(d) and pack.size(d) > MIN_BYTES]
    placeholders = [d for d in present if pack.has_placeholder_markers(d)]
    stale = [d for d in present if pack.age_days(d) > d.max_age_days]
    return {
        "required": len(required),
        "present": len(present),
        "placeholders": len(placeholders),
        "stale": len(stale),
        "missing": [d.name for d in required if d not in present],
    }
```

**Ship the counts, not a completeness percentage.** "37 of 41 documents present,
4 contain unfilled placeholders, 2 are older than their review period" is
actionable. "90% compliant" is a number that means nothing and that someone will
quote back to you.

**Never ship a placeholder as prose.** A technical documentation file where
`[to be completed: training data provenance]` has been replaced by a plausible
paragraph nobody verified is a fabricated record. Keep the markers, count them,
and let the count be uncomfortable.

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

- **Assembled after the fact.** The decisions cannot be honestly reconstructed;
  the pack becomes a creative-writing exercise under time pressure.

- **Placeholders filled with plausible text.** The worst failure here. A
  fabricated provenance paragraph is a false record in a document you are
  legally required to keep accurate.

- **A completeness percentage.** Invites a target, and the target gets met by
  loosening the definition of "present".

- **Vendor list shorter than the dependency manifest.** Cross-check, always;
  the gap is the finding.

- **No ruled-out list.** The section diligence reads first, absent. See
  `eu-applicability`.

- **Decision records that state only the outcome.** Without the rejected
  options, it reads as reverse-engineered.

- **Stale documents with no review date.** Age is the first thing a reviewer
  checks. Every document gets a `max_age_days` and shows up as stale past it.

- **Everything in a drive folder.** Unversioned, unreviewable, un-CI-able. The
  pack lives in the repository, next to the code it describes.

- **A pack that claims compliance.** It is evidence. The conclusion is someone
  else's to draw, and a pack that draws it for them reads as advocacy.

## Verify

Follow `references/verification.md`. For this skill specifically:

1. **Tier 0** — install, `--help`, assemble from a fixture brief and print the
   completeness counts.

2. **Tier 1** — `pytest -q`, offline:

```python
def test_required_documents_follow_the_applicable_regimes(brief):
    required = {d.name for d in documents_required(brief)}
    assert "ropa.yaml" in required                       # gdpr applicable
    assert "ai/technical-documentation.md" in required   # ai_act applicable
    assert "sbom/" not in required                       # cra ruled out in this fixture


def test_every_claimed_document_exists_and_is_non_empty(pack):
    for document in pack.manifest:
        assert pack.exists(document) and pack.size(document) > MIN_BYTES


def test_placeholders_are_counted_not_hidden(pack_with_placeholders):
    result = completeness(pack_with_placeholders)
    assert result["placeholders"] > 0
    assert "placeholder" in render(result).lower()


def test_no_completeness_percentage_is_reported(pack):
    text = render(completeness(pack))
    assert "%" not in text


def test_vendor_list_is_reconciled_with_the_manifest(pack, repo):
    missing = set(runtime_vendors(repo)) - set(pack.vendors())
    assert not missing, f"vendors with no evidence file: {missing}"


def test_vendor_without_a_dpa_is_a_blocker(pack):
    pack.vendor("openai").dpa = {"signed": False}
    finding = assess(pack).finding_for("vendor:openai")
    assert finding.severity == "blocker" and finding.citation == "Art. 28(3)"


def test_long_vendor_notice_period_is_a_finding(pack):
    pack.vendor("openai").breach_notice_period = "5 business days"
    assert any("reporting window" in f.statement for f in assess(pack))


def test_decision_records_include_rejected_options(pack):
    for adr in pack.decisions():
        assert "Options considered" in adr.text
        assert adr.rejected_options, f"{adr.id} records no rejected option"


def test_stale_documents_are_flagged(pack):
    pack.touch("statements/privacy-notice.md", days_ago=800)
    assert "statements/privacy-notice.md" in [d.name for d in completeness(pack)["stale_docs"]]


def test_ruled_out_regimes_are_rendered_in_full(pack):
    text = pack.render_markdown()
    for exclusion in pack.brief.regimes["ruled_out"]:
        assert exclusion["regime"] in text
        assert exclusion["expires_if"] in text


def test_pack_makes_no_compliance_claim(pack):
    text = pack.render_markdown().lower()
    for phrase in ("is compliant", "fully compliant", "meets all requirements"):
        assert phrase not in text


def test_generated_artifacts_carry_a_commit_and_a_date(pack):
    for artifact in pack.generated():
        assert artifact.commit and artifact.generated_at
```

3. **Tier 2** — report the counts: required, present, placeholders, stale,
   missing by name. Plus vendors with no DPA, vendors with no TIA where a
   transfer exists, and the longest breach notice period. Those three are the
   highest-value findings in a typical pack.

4. **Tier 3** — hand the pack to someone who was not interviewed and ask them to
   find a claim they know is wrong. Then hand it to counsel and ask whether it
   saved them time or created work. That answer is the measure of the pack.

Then tell the user the counts, the named gaps, and — explicitly — that a
complete pack is material for an opinion and not the opinion itself.
