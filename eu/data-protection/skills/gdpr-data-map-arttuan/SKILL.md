---
name: gdpr-data-map-arttuan
title: GDPR Data Map
description: Map every field to a purpose, a lawful basis, a retention period and a deletion path — then generate the Art. 30 record and flag the DPIA trigger
author: ArttuAn
author_url: https://github.com/ArttuAn/eu-compliance-skills/tree/main/skills/gdpr-data-map
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR Data Map

The document everything else in GDPR hangs off. A table of *field → purpose →
lawful basis → retention → deletion path → recipients*, built from the answers
in the brief and checked against the actual schema.

Most privacy work fails here, quietly, in one of two ways: the map is written
from the privacy policy rather than the database, or it has one lawful basis for
the whole product rather than one per purpose. Both produce a document that
looks like an Art. 30 record and would not survive ten minutes of questions.

> **Not legal advice.** Choosing and defending a lawful basis is a legal
> judgement. This skill produces the facts, the gaps and the questions — the
> basis has to be confirmed by someone accountable for it.

```
  schema + code ──► every field that is about a person
        │                        │
        │                        ▼
        │              which purpose does it serve?   (one row per purpose)
        │                        │
        │                        ▼
        │              basis (Art. 6) · Art. 9 condition if special category
        │                        │
        │                        ▼
        │              retention (a number) · deletion path (a code path)
        │                        │
        ▼                        ▼
  recipients + transfers ──► ROPA (Art. 30) · DPIA trigger · DSR endpoints
```

## Use this when

- After `eu-grill-me` and `eu-applicability`, whenever GDPR is in the applicable
  list — which is nearly always.
- Before a migration that adds fields, before integrating a vendor that receives
  user data, before a new product surface.
- When you need an Art. 30 record and do not have one, which is most teams under
  250 people who assumed the exemption applied to them. It rarely does.

**Do not use this when** nothing about a person is stored anywhere — no
accounts, no logs, no analytics, no support inbox. Verify that claim against the
code before accepting it; the web server log is the usual counterexample.

## Ask first

Most fields come from the schema, not from the user. Read first, ask second.

1. **"Point me at the schema, the migrations, and the log configuration."**
   Then enumerate the fields yourself and bring the user a list to correct. A
   list to correct gets a far more accurate answer than a blank prompt.
2. **For each purpose: "if a user told you to stop this tomorrow, what would
   break?"**
   Nothing → it was not necessary, so the basis is weak. They cannot use the
   product → contract (Art. 6(1)(b)), not consent. We lose insight → legitimate
   interests, and you owe a balancing test.
3. **"Which of these fields can contain free text a person typed?"**
   Free text is where special-category data hides. A support ticket body, a CV,
   a bug report. This single question changes the Art. 9 analysis more than any
   other.
4. **"Show me the code that deletes a person. All of it — primary tables,
   backups, logs, the search index, the analytics vendor, the CRM."**
   The most reliable question in the whole repo, because it has a checkable
   answer and the answer is usually "there isn't one."
5. **"Who signs off that a basis is correct?"**
   `basis_confirmed_by` must be a person. The gate cannot reach `clear` without
   one.

See `references/how-to-ask.md` — ask about the system, map to the law yourself.

## What the law requires

| Duty | Citation | What it means in a repo |
| --- | --- | --- |
| Purpose limitation | Art. 5(1)(b) | One row per purpose. A field used for two things is two rows. |
| Data minimisation | Art. 5(1)(c) | A field with no purpose is a finding, not a nice-to-have. |
| Storage limitation | Art. 5(1)(e) | A number of days and a mechanism. "As long as necessary" is not a retention period. |
| Accountability | Art. 5(2) | You must be able to demonstrate all of the above. |
| Lawful basis | Art. 6(1) | Exactly one per purpose, chosen before processing, not swapped later. |
| Special categories | Art. 9(2) | An Art. 9 condition **in addition to** an Art. 6 basis. Not instead of. |
| Children | Art. 8 | Consent for information society services; the age is national, between 13 and 16. |
| Transparency | Arts. 13-14 | The notice must match this map. If they disagree, one of them is a breach. |
| Data subject rights | Arts. 15-22 | Access, rectification, erasure, restriction, portability, objection. One month (Art. 12(3)). |
| Processors | Art. 28(3) | A written contract with the required terms, for every processor. |
| Records of processing | Art. 30 | This document. The under-250 exemption almost never applies — see below. |
| Design and defaults | Art. 25 | Decided at architecture time, which is why this runs before the build. |
| DPIA | Art. 35 | Required *prior to* processing likely to result in a high risk. |

**The Art. 30(5) exemption is a trap.** It excuses organisations under 250
employees only where processing is occasional, is not likely to result in a risk
to rights and freedoms, and involves no special categories or criminal-offence
data. Any product processing user data routinely fails the "occasional" limb on
its own. Assume the record is required, and if you want to rely on the
exemption, document why all three limbs are satisfied.

### Choosing a basis — the engineering version

```python
BASIS_TESTS = {
    "6(1)(b) contract": "The user asked for this service and it cannot be delivered without it.",
    "6(1)(c) legal obligation": "An EU or Member State law requires it. Name the law.",
    "6(1)(f) legitimate interests": "Needed for a real interest, no less intrusive way, "
                                    "and it does not override what the person would expect.",
    "6(1)(a) consent": "Genuinely optional. Refusing changes nothing else. "
                       "Withdrawable as easily as given.",
    "6(1)(d) vital interests": "Life or death. Rare.",
    "6(1)(e) public task": "Public authority or official function.",
}
```

Three rules that catch most of the real errors:

- **Consent is usually the wrong choice.** It is the weakest basis: it must be
  freely given, it can be withdrawn at any time, and it is invalid where there
  is a power imbalance — which includes employment. If the service does not work
  without the processing, consent is not available because refusing is not a
  real option. Use contract.
- **Legitimate interests owes a balancing test (an LIA).** Purpose, necessity,
  balance — written down, dated, attached. `lia_required: true` with no document
  is a finding.
- **The basis cannot be swapped later.** You cannot rely on consent, have it
  withdrawn, and fall back to legitimate interests for the same processing.
  Choose once, document why.

### The DPIA trigger

Art. 35(3) plus the national supervisory authority's published list. Screen with
a checklist and escalate anything that scores:

```python
DPIA_TRIGGERS = [
    ("systematic and extensive evaluation based on automated processing, "
     "including profiling, with legal or similarly significant effects", "Art. 35(3)(a)"),
    ("large-scale processing of special categories or criminal-offence data", "Art. 35(3)(b)"),
    ("systematic monitoring of a publicly accessible area on a large scale", "Art. 35(3)(c)"),
    ("new technologies", "Art. 35(1)"),
    ("data about vulnerable people, including children or employees", "WP248 criterion"),
    ("matching or combining datasets from different sources", "WP248 criterion"),
    ("preventing data subjects from exercising a right or using a service", "WP248 criterion"),
]


def dpia_required(brief) -> tuple[bool, list[str]]:
    """Two or more WP248 criteria is the conventional threshold; any Art. 35(3)
    limb is sufficient on its own."""
    hits = [c for c, _ in DPIA_TRIGGERS if brief.matches(c)]
    statutory = [c for c, art in DPIA_TRIGGERS if art.startswith("Art. 35(3)") and brief.matches(c)]
    return (bool(statutory) or len(hits) >= 2), hits
```

If a DPIA is required and the risk cannot be mitigated, Art. 36 requires prior
consultation with the supervisory authority *before* processing. That is a
**blocker**, not a condition — it has a statutory clock attached and cannot be
done after launch.

## What to produce

Four artifacts, all in the repository.

**1. The map itself**, in `compliance.yaml` under `data`, one row per
`(field, purpose)` pair:

```yaml
- field: "applicants.cv_text"
  purpose: "assess fit for the role applied to"
  personal: true
  special_category: possible          # free text - may contain Art. 9 data
  art_9_condition: null               # a blocker while special_category is possible
  lawful_basis: "6(1)(b) contract"
  basis_confirmed_by: null            # must be a person before the gate can clear
  retention_days: 180
  deletion_path: "jobs/purge_applicants.py::purge (cron, daily)"
  recipients: ["cv-parser-vendor"]
  source: {kind: answered, question: A-01}
```

`special_category: possible` for free-text fields is deliberate. You cannot know
what a person typed into a support ticket, so the honest options are to treat it
as possible and put an Art. 9 condition or a redaction control in place, or to
stop storing free text. Marking it `false` because you did not intend to collect
health data is not one of the options.

**2. `compliance/ropa.yaml`** — the Art. 30 record, generated from the map, not
written by hand. Controller and DPO contact, purposes, categories of data
subjects and data, categories of recipients, third-country transfers with the
safeguard, retention, and a general description of security measures.

**3. Deletion and DSR code**, actually wired up:

```python
def erase_subject(subject_id: str) -> dict[str, int]:
    """Art. 17. Every store, including the ones that are easy to forget."""
    removed = {}
    removed["primary"] = db.delete_person(subject_id)
    removed["search_index"] = search.delete_by_subject(subject_id)
    removed["object_store"] = blobs.delete_prefix(f"users/{subject_id}/")
    removed["analytics"] = analytics.delete_subject(subject_id)     # vendor API
    removed["crm"] = crm.delete_contact(subject_id)
    removed["logs"] = logs.redact_subject(subject_id)               # redact, not delete
    audit.record("erasure", subject_id, removed)                    # keep the receipt
    return removed
```

Two details that are usually wrong. **Logs get redacted, not deleted** — you
generally need the log for security, so redact the identifier and keep the
event. And **backups**: you normally cannot rewrite them, so document the
approach (the deletion is applied on restore, backups age out in N days) rather
than claiming an erasure that did not happen.

**4. A `test_erasure_leaves_nothing` test in CI.** Create a subject, write to
every store, erase, assert each store is clean. This is the single most
convincing piece of evidence in the entire pack, because it is generated, dated,
and cannot have been written the week the letter arrived.

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

- **One basis for the whole product.** "We rely on legitimate interests" across
  twelve purposes. The moment a regulator asks about one purpose specifically,
  the record collapses.

- **The map written from the privacy policy.** It describes what someone
  intended to collect. Build it from the schema, the migrations and the log
  format, then reconcile — and treat any divergence from the notice as a finding
  on the notice.

- **Free text marked `special_category: false`.** CVs, support tickets and bug
  reports contain health, religion and union membership regularly. Nobody
  intended to collect it, and intention is not the test.

- **"As long as necessary."** Not a retention period. Re-ask for a number and
  the job that enforces it. A retention period with no mechanism is a wish.

- **A deletion path that misses a store.** The search index, the object store,
  the analytics vendor and the CRM are the four that get missed. The test is how
  you find out.

- **Consent where contract belongs.** The product does not work without the
  processing, so refusal is not real, so the consent is invalid — and now you
  also have a withdrawal mechanism you cannot honour.

- **Legitimate interests with no LIA.** The basis that requires the most
  documentation, chosen because it feels like the one that requires the least.

- **Assuming the Art. 30(5) exemption.** Three limbs, all required, and
  "occasional" excludes nearly every product.

- **A DPIA written after launch.** It is required *prior to* the processing.
  Written after, it is evidence of the breach.

## Verify

Follow `references/verification.md`. For this skill specifically:

1. **Tier 0** — install, `--help`, generate a ROPA from a fixture brief and
   validate it against the schema.

2. **Tier 1** — `pytest -q`, offline:

```python
def test_every_field_in_the_schema_appears_in_the_map(repo_fixture):
    missing = set(schema_fields(repo_fixture)) - set(mapped_fields(brief))
    assert not missing, f"unmapped fields: {missing}"


def test_every_purpose_has_exactly_one_basis(brief):
    for row in brief.data["purposes"]:
        assert row["lawful_basis"], f"{row['name']} has no basis"
        assert isinstance(row["lawful_basis"], str)      # not a list


def test_special_category_without_an_art_9_condition_is_a_blocker(brief):
    finding = analyse(brief).finding_for("applicants.cv_text")
    assert finding.severity == "blocker"
    assert finding.citation.startswith("Art. 9")


def test_free_text_is_never_marked_not_special(brief):
    for row in brief.data["categories"]:
        if row.get("free_text"):
            assert row["special_category"] != False


def test_vague_retention_is_rejected():
    with pytest.raises(ValueError, match="retention must be a number of days"):
        Row(field="x", purpose="y", retention_days="as long as necessary")


def test_every_field_has_a_deletion_path(brief):
    for row in brief.data["categories"]:
        assert row["deletion_path"], f"{row['field']} cannot be erased"


def test_erasure_leaves_nothing(stores):
    subject = seed_subject_everywhere(stores)
    erase_subject(subject.id)
    for name, store in stores.items():
        assert store.find(subject.id) is None, f"{name} still holds the subject"


def test_consent_basis_is_rejected_when_the_service_requires_it(brief):
    row = brief.purpose("deliver the core service")
    row["lawful_basis"] = "6(1)(a) consent"
    finding = analyse(brief).finding_for(row)
    assert "refusing is not a real option" in finding.statement


def test_legitimate_interests_requires_an_lia(brief):
    row = brief.purpose("product analytics")
    row["lawful_basis"] = "6(1)(f) legitimate interests"
    assert analyse(brief).finding_for(row).needs.startswith("Documented balancing test")


def test_dpia_trigger_fires_on_a_statutory_limb(brief_profiling):
    required, hits = dpia_required(brief_profiling)
    assert required and any("automated processing" in h for h in hits)


def test_prior_consultation_is_a_blocker(brief_unmitigable_high_risk):
    finding = analyse(brief_unmitigable_high_risk).finding_for("dpia")
    assert finding.severity == "blocker" and "Art. 36" in finding.citation


def test_ropa_generates_and_validates(brief):
    ropa = generate_ropa(brief)
    assert validate_ropa(ropa) == []
    for required in ("purposes", "categories_of_recipients", "retention",
                     "transfers", "security_measures"):
        assert required in ropa


def test_basis_confirmed_by_is_required_for_clear(brief):
    brief.resolve_all_findings()
    assert brief.gate["decision"] != "clear"        # nobody has signed off a basis
```

3. **Tier 2** — report: fields in the schema versus fields in the map (the gap
   is the finding), purposes with an unconfirmed basis, fields with no deletion
   path, and whether the erasure test passes. Those four numbers are the state
   of your GDPR posture in one line each.

4. **Tier 3** — a DPO or counsel reviews the basis column specifically. That
   column is the one that is wrong most often and the one that is cheapest to
   fix before the product exists.

Then tell the user what ran, and name every basis that is your reading rather
than a confirmed decision. Do not report that the product is compliant; report
which purposes have a confirmed basis and which do not.
