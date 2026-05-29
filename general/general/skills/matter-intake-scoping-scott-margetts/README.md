# matter-intake-scoping

Matter scoping across the full pre-execution arc — from unstructured client data to a structured brief, through to the agreed baseline that every other LPM discipline references, with a mid-matter recovery mode for when the LPM inherits with no documented baseline.

## What this skill does

Four operating modes:

**Mode 1 — Pre-engagement:** Takes whatever the client has sent — emails, org charts, data room indexes, call notes — and organises it into a structured brief the partner can write a proposal from. Detects conflicts across sources, applies confidence labels to every data point, flags external knowledge considerations, and produces a prioritised open questions list. Does not write the proposal; makes writing it fast.

**Mode 2 — Quick intake:** Runs immediately after engagement is confirmed. Captures the agreed scope baseline — inclusions, exclusions, assumptions, constraints, milestones, fee basis — in a structured format that scope-change-controller manages for the life of the matter. Produces an LPM involvement definition for agreement with the partner.

**Mode 3 — Full intake:** Mode 2 plus full stakeholder matrix, comprehensive assumptions log, success criteria, preliminary risk register, and kickoff agenda. For large or complex matters.

**Mode 4 — Mid-matter recovery:** Works backwards from billing data and correspondence to reconstruct the original scope baseline, identify what has changed and how, and produce a structured delta table and handoff to scope-change-controller. The most common actual entry point.

## Folder structure

```
matter-intake-scoping/
├── SKILL.md                                  # Core methodology — install this
├── README.md                                 # This file
└── references/
    ├── standing-assumptions.md               # Assumption performance register — populate this
    └── matter-type-profiles/
        └── template.md                       # Matter type profile template — duplicate and populate
```

## What is and isn't provided

**Provided:** The methodology — modes, workflows, confidence labelling system, conflict detection logic, output formats, cross-skill handoff points, M365 connected mode guidance.

**Not provided:** Legal and operational content. The `references/` files are intentionally empty scaffolding. Their structure is defined; their content belongs to the firm deploying the skill.

This distinction is deliberate. The methodology for organising client data and capturing a scope baseline is generic and transferable. The specific knowledge about what assumptions typically hold on German dissolution programmes, what regulatory filings are required across which jurisdictions, and what a compliant entity structure looks like in Austria — that is the firm's accumulated practice expertise. It should stay with the firm, not be encoded by a third party.

## What your firm needs to populate

**`references/standing-assumptions.md`**

A performance register of assumptions by matter type — which assumptions hold consistently, which breach, and with what consequence. Populated over time from matter retrospectives. The skill's Mode 1 and Mode 2 consume this file to produce a calibrated assumptions candidate list rather than importing last matter's list uncritically.

Start by capturing the three most common failure modes on your highest-volume matter type. Build from there.

**`references/matter-type-profiles/[type].md`**

One file per matter type (e.g. `corporate-dissolution.md`, `cross-border-merger.md`). Each profile identifies which knowledge domains are typically relevant for that matter type — which regulatory thresholds apply, what execution requirements arise, what assumptions commonly appear. Duplicate `template.md` and populate.

The skill routes to these profiles in Step 1 of Mode 1. Without populated profiles, the skill still works — it falls back on general knowledge and flags the gap. With populated profiles, it surfaces matter-type-specific flags automatically.

## v2 architecture note

This skill is designed to reference a `shared-knowledge/` layer at the plugin root level — legal and jurisdictional knowledge files (execution requirements, entity types, regulatory thresholds) that are populated by the deploying firm and consumed by both LPM and attorney skills. That layer is not yet built. When it is, this skill's routing mechanism is already designed to use it. The `matter-type-profiles/` files in `references/` are the bridge — they point to shared-knowledge domains rather than containing legal content directly.

## Cross-skill handoffs

- **To scope-change-controller:** Mode 2/3 scope summary is the baseline SCC manages. Pass it with "set up the scope baseline using this scope summary."
- **To risk-and-issues-manager:** Initial assumptions log becomes A-entries in the RAID log.
- **To budget-and-fee-manager:** Scope parameters are inputs for bottom-up budget construction.
- **From continuous-improvement-engine:** Assumption performance data at matter close feeds `references/standing-assumptions.md`. Without this, the learning loop has no re-entry point.
