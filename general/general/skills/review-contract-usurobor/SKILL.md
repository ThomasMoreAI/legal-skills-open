---
name: review-contract-usurobor
title: 'Review — Phase 1: Contract Integrity'
description: Contract integrity preflight — verify the work contract is truthful, consistent, and non-contradictory before reading the diff.
author: usurobor
author_url: https://github.com/usurobor/cnos/tree/main/src/packages/cnos.cdd/skills/cdd/review/contract
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Review — Phase 1: Contract Integrity

**GATE: Complete this phase before reading the diff.** A branch can be locally well-implemented and still not review-ready if the contract it claims to satisfy is contradictory, stale, or overclaims shipped behavior.

Fill the Contract Integrity table. If any row is "no," the review cannot approve unless the row is explicitly out of scope and the reviewer names why it does not affect merge readiness.

```markdown
## §2.0.0 Contract Integrity

| Check | Result | Notes |
|---|---|---|
| Status truth preserved | yes / no / n/a | |
| Canonical sources/paths verified | yes / no / n/a | |
| Scope/non-goals consistent | yes / no / n/a | |
| Constraint strata consistent | yes / no / n/a | |
| Exceptions field-specific/reasoned | yes / no / n/a | |
| Path resolution base explicit | yes / no / n/a | |
| Proof shape adequate | yes / no / n/a | |
| Cross-surface projections updated | yes / no / n/a | |
| No witness theater / false closure | yes / no / n/a | |
| PR body matches branch files | yes / no / n/a | |
```

---

## Checks

### 1. Status truth

Verify that the issue, PR body, branch artifacts, and docs distinguish:
- **shipped:** implemented and enforced today
- **current spec:** normative document currently governing conformance
- **draft target:** proposed or draft spec not yet promoted
- **planned:** accepted direction, not implemented
- **non-goals:** explicitly excluded
- **unknown:** not verified yet

Findings:
- D if the branch claims runtime enforcement that does not exist.
- C if draft/target state is described as current but the diff does not rely on it.
- mechanical if the status label is plainly stale across docs/README/source map.

- ❌ "CTB enforces witnessed close-outs" when only the v0.2 draft defines them.
- ✅ "CTB v0.2 draft defines witnessed close-outs; ctb-check/runtime enforcement is not shipped."

### 2. Source-of-truth map

For every load-bearing claim in the issue or PR body, verify the canonical source. Check:
- exact file path;
- branch/ref if relevant;
- current vs draft status;
- upstream repo links;
- generated vs authored source;
- README/docs/source-map projections.

If paths changed, grep old paths across live docs and code.

- ❌ "Manifesto lives under doctrine/" when canonical path is `docs/alpha/essays/MANIFESTO.md`.
- ✅ Root README, docs README, and source map all point to the same canonical path.

### 3. Scope and non-goal consistency

Check whether any AC, implementation note, PR claim, or output artifact contradicts the non-goals.

Findings:
- D if an out-of-scope behavior is implemented or claimed as shipped.
- C if the PR body implies out-of-scope work but files do not.
- mechanical if the contradiction is textual and deterministic.

- ❌ Non-goal: "do not implement runtime enforcement." PR body: "runtime now enforces CTB v0.2."
- ✅ PR body: "adds structural checker issue; runtime enforcement remains out of scope."

### 4. Constraint strata

If the issue defines required/optional/exception-backed fields or rules, verify that examples and implementation obey the strata. Check:
- hard gates are not exception-backed;
- exception-backed fields have field-specific exceptions;
- optional/defaulted fields name defaults;
- validated-if-present fields are actually checked when present;
- deferred fields are not silently enforced or claimed.

- ❌ Hard gate: `scope`. Exception example: `"allowed_missing": ["scope"]`.
- ✅ Exception example only lists exception-backed fields such as `artifact_class` or `kata_surface`.

### 5. Exception discipline

Exceptions are debt, not blanket permission. Verify:
- exceptions are field-specific;
- each exception has a reason;
- JSON exceptions do not rely on comments;
- exceptions do not exempt hard gates;
- cleanup/removal condition is named where appropriate.

- ❌ `{ "path": "...", "ignore": true }`
- ✅ `{ "path": "...", "allowed_missing": ["artifact_class"], "reason": "legacy skill migration pending" }`

### 6. Path resolution semantics

If the issue or implementation validates paths, verify the resolution base. Check whether paths are:
- repo-root-relative;
- package-root-relative;
- caller-file-relative;
- branch-relative;
- generated-artifact-relative.

Require at least one concrete example when path validation is part of the change.

- ❌ "Validate calls relative to the skill's parent directory" when current skills use package-root-relative calls.
- ✅ `alpha/SKILL.md` with `calls: design/SKILL.md` resolves to `src/packages/cnos.cdd/skills/cdd/design/SKILL.md`.

### 7. Proof shape

For checker, schema, parser, runtime, CI, and validation issues, verify that the branch includes:
- invariant;
- oracle;
- positive case;
- negative case;
- operator-visible projection;
- known gap.

Existing CI passing is the floor, not the proof.

- ❌ "CI passes" but no invalid fixture proves the checker rejects malformed input.
- ✅ Valid fixture passes; missing hard-gate field fails with expected diagnostic.

### 8. Cross-surface projections

When the diff adds or changes a status, checker, command, CI job, source map, schema, or runtime surface, verify every projection that should expose it.

Examples:
- CI job added → notify aggregation updated.
- README source map changed → docs README changed.
- Schema added → schema README / fixtures / CI invocation added.
- Runtime status changed → help / doctor / status / docs agree.
- Upstream formal source added → source map and further-reading sections agree.

- ❌ Add CI job I5 but leave Telegram/notify aggregation unaware of I5.
- ✅ I5 is added and notify job result summary includes I5.

### 9. False closure / witness theater

If the change adds witnesses, close-outs, review artifacts, checker outputs, debt records, or governance structure, verify that the structure is accountable to evidence. Ask:
- What rejects a malformed artifact?
- What preserves failed evidence?
- What prevents accepted closure from hiding active debt?
- What fields are required but non-vacuous?
- What is still only prose discipline?

Findings:
- D if the branch claims enforcement but only adds prose.
- C if the structure is useful but lacks the promised rejection mechanism.
- B if the rejection mechanism is correctly deferred but the deferral could be clearer.

- ❌ 10-field close-out shape exists, but no checker or issue says which fields are required.
- ✅ Spec names required fields; checker issue requires invalid fixtures and diagnostics.

### 10. PR body / branch summary consistency

Verify that the PR description still matches the corrected branch files. After fix rounds, PR bodies can describe an older state.

- ❌ PR body says "nested └─ layer diagram" but branch files now show sibling `├─` architecture.
- ✅ PR body updated after fix to match the branch head state.

---

## After Phase 1

If all rows are "yes" or "n/a," proceed to Phase 2 (implementation review).

If any row is "no," file findings immediately. The implementation review may still proceed, but verdict must account for the contract-level findings.

**Return to orchestrator** (`review/SKILL.md`) → **Load Phase 2** starting with `review/issue-contract/SKILL.md`.
