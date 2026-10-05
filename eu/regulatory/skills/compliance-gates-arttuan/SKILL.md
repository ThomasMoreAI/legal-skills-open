---
name: compliance-gates-arttuan
title: Compliance Gates
description: Wire the brief into CI so the code cannot drift away from it — new vendors, new fields, expired exclusions and overdue findings all fail the build
author: ArttuAn
author_url: https://github.com/ArttuAn/eu-compliance-skills/tree/main/skills/compliance-gates
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# Compliance Gates

Everything else in this repo produces a record of what is true today. This skill
is what keeps it true.

Compliance records rot silently. A dependency is added and a vendor now receives
user data that no DPA covers. A migration adds a field the ROPA does not mention.
The 50th person is hired and the NIS2 exclusion stops being true. A finding's due
date passes. None of that announces itself, and by the time anyone notices, the
brief describes a product that has not existed for a year.

The fix is mechanical: **the brief is a file in the repository, and CI checks
the code against it on every push.** Drift becomes a failed build in the pull
request that caused it, which is the only moment it is cheap to fix.

> **Not legal advice.** A green build means the code matches the record. It does
> not mean the record is right — that is what the review in
> `references/verification.md` Tier 3 is for.

```
  push / PR
     │
     ▼
  read compliance.yaml
     │
     ├─► dependency diff  ──► new runtime vendor with no evidence file?  FAIL
     ├─► schema diff      ──► new personal-data field not in the map?    FAIL
     ├─► exclusions       ──► any expires_if now true?                   FAIL
     ├─► findings         ──► open blocker, or a due date passed?        FAIL
     ├─► accepted risks   ──► review_by passed?                          FAIL
     ├─► live checks      ──► non-essential storage before consent?      FAIL
     └─► generated docs   ──► SBOM missing for the tag? placeholders up? FAIL
     │
     ▼
  annotate the PR with the finding and the citation, not just a red X
```

## Use this when

- Immediately after `eu-grill-me`, in the same session. A brief with no gate has
  a shelf life of about one sprint.
- When adopting this repo on an existing codebase — the gate is what tells you
  how far the code has already drifted from whatever documentation exists.
- Before a release, as a pre-tag check that the release-scoped artifacts exist.

**Do not use this when** there is no brief to check against. And do not turn
every check on at once on a legacy codebase: you will get four hundred failures,
someone will disable the job, and the gate will never come back. Start in
warn-only mode, fix the backlog, then enforce.

## Ask first

1. **"Which checks should fail the build today, and which should only warn?"**
   The honest answer on an existing codebase is "warn on everything for two
   weeks". Say so rather than shipping a red pipeline.
2. **"What is your runtime dependency boundary?"**
   Which of these packages actually receives user data? A dev dependency does
   not need a DPA and flagging it destroys the signal.
3. **"Where is the schema of record — migrations, an ORM, a `schema.sql`?"**
   The field check needs one source of truth.
4. **"Who gets the failure?"**
   A gate failing to nobody is a gate that gets disabled. Name an owner per
   check.
5. **"Do you deploy to an environment I can probe?"**
   The consent and accessibility checks need a live URL to be worth anything.

## What the law requires

No article says "run CI". Three duties make it the practical way to discharge
them:

- **GDPR Art. 5(2) accountability** — continuous, not a point-in-time claim. A
  record that was accurate at signing and inaccurate since does not demonstrate
  anything.
- **GDPR Art. 25 data protection by design and by default** — obligations attach
  at the determination of means, which happens in every pull request that adds a
  field, not only at project kickoff.
- **AI Act Art. 9** — risk management for high-risk systems is explicitly "a
  continuous iterative process … throughout the entire lifecycle", requiring
  regular systematic review.
- **NIS2 Art. 21(2)(f)** — policies to **assess the effectiveness** of the
  measures. A check that runs is evidence; a policy that says you review annually
  is a plan.

## What to produce

**1. The checks.** Each one reads the brief and a fact about the repo.

```python
from dataclasses import dataclass


@dataclass
class GateResult:
    check: str
    passed: bool
    severity: str            # "fail" | "warn"
    message: str
    citation: str = ""
    fix: str = ""            # what to do, concretely


def check_new_vendors(brief, repo) -> list[GateResult]:
    """A runtime dependency that receives user data needs an evidence file."""
    known = {v["name"].lower() for v in brief.vendors()}
    out = []
    for package in runtime_dependencies(repo):
        if package.lower() in known or not package.receives_user_data:
            continue
        out.append(GateResult(
            "new-vendor", False, "fail",
            f"{package} is a runtime dependency that can receive user data, "
            f"and has no file in compliance/vendors/.",
            citation="Art. 28 GDPR",
            fix=f"Run `eu-evidence-pack vendor add {package}`, attach the DPA, "
                f"and record the transfer mechanism."))
    return out


def check_expired_exclusions(brief) -> list[GateResult]:
    """The most valuable check here: an exclusion that stopped being true."""
    facts = brief.facts()                    # headcount, turnover, features, surfaces
    out = []
    for exclusion in brief.regimes["ruled_out"]:
        condition = exclusion.get("expires_if")
        if not condition:
            out.append(GateResult(
                "exclusion-expiry", False, "warn",
                f"{exclusion['regime']} exclusion has no machine-evaluable expires_if.",
                fix="Add a condition over brief facts so this can be checked."))
            continue
        if evaluate(condition, facts):
            out.append(GateResult(
                "exclusion-expiry", False, "fail",
                f"{exclusion['regime']} was ruled out because "
                f"{exclusion['reason']!r}. That is no longer true: {condition}.",
                fix=f"Re-run eu-applicability; the {exclusion['regime']} duties may now apply."))
    return out


def check_findings(brief, today) -> list[GateResult]:
    out = []
    for finding in brief.findings:
        if finding.status == "open" and finding.severity == "blocker":
            out.append(GateResult("open-blocker", False, "fail",
                                  f"{finding.id}: {finding.statement}",
                                  citation=finding.citation, fix=finding.needs))
        elif finding.status == "open" and finding.due and finding.due < today:
            out.append(GateResult("overdue-finding", False, "fail",
                                  f"{finding.id} was due {finding.due} "
                                  f"(owner: {finding.owner}).",
                                  citation=finding.citation, fix=finding.needs))
    for accepted in brief.accepted_risks:
        if accepted["review_by"] < today:
            out.append(GateResult("accepted-risk-expired", False, "fail",
                                  f"{accepted['finding']} was accepted by "
                                  f"{accepted['accepted_by']} for review by "
                                  f"{accepted['review_by']}. That date has passed.",
                                  fix="Re-review, then extend with a new date or resolve it."))
    return out
```

The other checks follow the same shape: new personal-data fields absent from the
data map; a privacy notice changed without a consent version bump; an SBOM
missing for a release tag; placeholder markers increasing in the AI Act technical
documentation; a live probe for non-essential storage before consent.

**2. A warn-only mode, and a migration path.** On an existing codebase,
everything starts as `warn`, with a dated plan to promote checks to `fail`:

```yaml
# compliance/gates.yaml
mode: warn                      # warn | enforce
promote:
  - {check: open-blocker, enforce_from: "2026-09-20"}
  - {check: new-vendor, enforce_from: "2026-10-01"}
  - {check: exclusion-expiry, enforce_from: "2026-10-01"}
  - {check: unmapped-field, enforce_from: "2026-11-01"}
owners:
  new-vendor: "@priya"
  exclusion-expiry: "@dana"
```

A dated promotion schedule is the difference between a gate that gets adopted
and one that gets disabled on day two. The promotion dates themselves are then
checked by the gate, which is the only way they hold.

**3. The workflow:**

```yaml
name: compliance
on: [push, pull_request]
jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: {fetch-depth: 0}          # the diff checks need history
      - run: pip install -e ".[dev]"
      - run: <command> gate --brief compliance/compliance.yaml --annotate
      - run: <command> gate report --out compliance/GATE.md
      - uses: actions/upload-artifact@v4
        with: {name: compliance-gate, path: compliance/GATE.md}
```

**4. PR annotations, not a red X.** A failure must say what broke, cite the
article, and give the fix:

```
::error file=package.json,line=34::[compliance] `@segment/analytics-node` is a new
runtime dependency that can receive user data and has no file in compliance/vendors/.
Art. 28 GDPR requires a written processor contract. Fix: run
`eu-evidence-pack vendor add @segment/analytics-node`, attach the DPA, and record
the transfer mechanism. Owner: @priya
```

A gate that says "compliance check failed" teaches people to re-run it. A gate
that says exactly what to do gets fixed in the same pull request.

**5. A scheduled run**, not only on push. Some conditions become true with the
passage of time rather than with a commit: a due date passes, an accepted risk's
review date arrives, a document goes stale. Run the gate nightly and open an
issue rather than failing a build nobody triggered.

**6. The hard constraint runs first.** Before any drift check, the brief must
prove its own numbers: `python3 tools/hard_gate.py --brief compliance.yaml`
derives every certainty from the `trace` and exits 2 on a number the trace
cannot support. This is the deterministic back-end — the skill is the soft
instruction; the tool is the gate. The user picks the policy each run:
`--policy block` (default, CI), `--policy record` (agent, pre-build: appends an
append-only finding per violation and normalizes the numbers), `--policy warn`
(onboarding). `EU_COMPLIANCE_POLICY` can set the default. Whatever the policy,
an inflated certainty, a no-trace brief, a fabricated article, a Directive
without a Member State, and a recorded `VAGUE` are violations — not opinions.

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

- **Everything enforced on day one.** Four hundred failures, the job gets
  disabled, and the gate never returns. Warn first, with a dated promotion plan.

- **Flagging dev dependencies.** A linter does not need a DPA. Scope to runtime
  dependencies that can actually receive user data, or the signal drowns.

- **Exclusions with no machine-evaluable condition.** Then the most valuable
  check in the gate degrades to a reminder nobody reads. `expires_if` should be
  an expression over brief facts wherever it can be.

- **A gate with no owner.** It fails, the pipeline is red, someone adds
  `continue-on-error: true`. Name an owner per check and route the failure.

- **Push-only.** Time-based conditions never fire, and overdue findings
  accumulate invisibly. Schedule it.

- **Failure messages with no fix.** "Compliance check failed" gets re-run. Give
  the article, the reason, and the command.

- **The gate treated as the review.** Green means the code matches the record.
  Whether the record is right is a question for a human, and the gate should say
  so in its own output.

- **The brief edited to make the gate pass.** The most corrosive failure. Derive
  `status` rather than reading it, require a named human and a review date for
  acceptances, and treat a brief diff in a PR as requiring review from the
  compliance owner — a CODEOWNERS entry on `compliance/` costs one line.

## Verify

Follow `references/verification.md`. For this skill specifically:

1. **Tier 0** — install, `--help`, run the gate against a fixture repo and brief.

2. **Tier 1** — `pytest -q`, offline:

```python
def test_new_runtime_vendor_fails(repo_with_new_dep, brief):
    results = check_new_vendors(brief, repo_with_new_dep)
    assert any(not r.passed and r.severity == "fail" for r in results)
    assert "Art. 28" in results[0].citation
    assert results[0].fix


def test_dev_dependency_does_not_fail(repo_with_new_dev_dep, brief):
    assert check_new_vendors(brief, repo_with_new_dev_dep) == []


def test_expired_exclusion_fails(brief):
    brief.subject["headcount"] = 60          # nis2 exclusion said >= 50
    results = check_expired_exclusions(brief)
    assert any(r.check == "exclusion-expiry" and not r.passed for r in results)
    assert "no longer true" in results[0].message


def test_exclusion_without_a_condition_warns(brief_loose_exclusion):
    results = check_expired_exclusions(brief_loose_exclusion)
    assert results[0].severity == "warn"


def test_open_blocker_fails(brief_with_blocker):
    assert any(r.check == "open-blocker" for r in check_findings(brief_with_blocker, today()))


def test_overdue_finding_fails(brief):
    brief.findings[0].due = "2026-01-01"
    results = check_findings(brief, today="2026-09-15")
    assert any(r.check == "overdue-finding" for r in results)
    assert brief.findings[0].owner in results[0].message


def test_expired_acceptance_fails(brief_with_accepted_risk):
    brief_with_accepted_risk.accepted_risks[0]["review_by"] = "2026-01-01"
    results = check_findings(brief_with_accepted_risk, today="2026-09-15")
    assert any(r.check == "accepted-risk-expired" for r in results)


def test_unmapped_schema_field_fails(repo_with_migration, brief):
    results = check_fields(brief, repo_with_migration)
    assert any("users.phone_number" in r.message for r in results)


def test_warn_mode_never_exits_nonzero(brief_with_blocker, gates_config_warn):
    assert run_gate(brief_with_blocker, gates_config_warn).exit_code == 0


def test_promotion_date_moves_a_check_to_fail(gates_config):
    gates_config.promote[0]["enforce_from"] = "2026-01-01"
    assert effective_severity("open-blocker", gates_config, today="2026-09-15") == "fail"


def test_status_is_recomputed_not_read(brief_file_claiming_clear):
    assert load(brief_file_claiming_clear).status == "blocked"


def test_every_failure_carries_a_fix(all_results):
    for result in all_results:
        if not result.passed:
            assert result.fix, f"{result.check} has no fix instruction"


def test_gate_output_makes_no_compliance_claim(report):
    text = report.lower()
    assert "compliant" not in text or "does not mean" in text
```

3. **Tier 2** — report: checks enabled, checks in warn versus enforce, failures
   by check, and the promotion schedule with dates. On an existing codebase also
   report the initial backlog size — that number is the honest measure of how far
   the code had already drifted.

4. **Tier 3** — introduce real drift deliberately. Add a dependency that
   receives user data, add a field, bump headcount past the cap. Confirm each one
   fails with a message someone could act on without asking what it means. A gate
   that has never been shown to fail has not been shown to work.

Then tell the user which checks are enforcing and which are warning, when each
promotes, and — plainly — that a green gate means the code matches the record,
not that the record is right.
