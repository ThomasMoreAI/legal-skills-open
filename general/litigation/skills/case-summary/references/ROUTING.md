# Routing — Defer to Sibling Skills

When the corpus contains a cluster of specialized documents — a set of deposition transcripts, a dense medical-records set, a lien correspondence folder — there is probably a sibling skill designed specifically for that cluster. Route to the sibling skill, consume its output, and slot the consumed artifact into the memo via `OUTPUT-TEMPLATE.md`.

Routing is advisory. Use judgment: a single deposition in an otherwise small corpus is fine to summarize inline. Five 200-page transcripts get routed.

---

## Routing contract per target

| Cluster signal | Route to | Consume back | Slots into memo section |
|---|---|---|---|
| Deposition transcripts (≥1 full transcript) | `deposition-summary` | page:line summary + exhibit index | V Evidence inventory |
| Dense medical-records set (≥3 providers) | `medical-record-chronology` | provider index + chronological encounter entries | V Evidence inventory (via PLAYBOOK-PI-TORT Medical Summary) |
| Causation-narrative request | `medical-treatment-summary` | 8–20 page treatment narrative | V Evidence inventory |
| Discovery responses (ROGs, RFPs, RFAs) | `discovery-summary` | findings-by-type + cross-reference analysis | IV Claims & theories; VII Defenses |
| Lien correspondence (≥2 lienholders) | `lien-resolution-summary` | lien-by-lien detail table | VI Exposure/remedies (via PLAYBOOK-PI-TORT Liens) |
| Pre-existing chronology deliverable requested | `case-chronology` | ISO-dated table + gap analysis | III Factual summary |
| Go/no-go screening deliverable | `case-viability-report` | viability assessment with rationale | VIII Strengths / weaknesses / red flags |
| Demand-prep deliverable | `pi-demand-summary` or `demand-letter` | packaged demand | (stand-alone output, not this memo) |
| Plaintiff-side liability element breakdown | `evidence-liability-summary` | element-mapped tables | IV Claims & theories |
| Strategy-roadmap deliverable | `legal-strategy-summary` | motion + discovery + settlement plan | IX Next steps |
| Patent-infringement per-claim deep-dive | `patent-infringement-analysis` | per-claim chart | IV Claims & theories (via PLAYBOOK-IP-INFRINGEMENT) |
| Settlement package summarization | `settlement-summarization` | terms + compliance obligations | Post-memo (not factual memo) |

---

## Decision heuristic

Route to a sibling skill when **any** of the following is true:

1. **Volume.** The cluster has enough documents that a generic search-driven pass won't do them justice (e.g., five depositions, a 500-page medical set, a 200-page discovery response production).
2. **Specialized format.** The document type has a well-understood summary shape that the sibling skill enforces (page:line for depositions, provider-and-encounter for medicals, cross-reference for discovery).
3. **User objective alignment.** The user's stated objective matches the sibling skill's output shape (they want a chronology → `case-chronology`; a viability screen → `case-viability-report`; a demand → `pi-demand-summary`).
4. **Attorney-grade artifact needed.** The memo needs to cite or attach the sibling's output as an exhibit, not paraphrase it.

Do **not** route when:

- The cluster is trivial in size (a single short document).
- The sibling skill would duplicate the core memo's coverage without adding rigor.
- The user explicitly asked for a single unified case-summary memo without chaining.

---

## How to invoke a sibling

Sibling skills are other skills in `skills/legal/`. The case-summary agent either:

1. Runs the sibling skill in-session against the scoped cluster and captures its output as an artifact (preferred when the user has authorized chaining).
2. Records a **routing recommendation** in `IX Next steps` of the memo, so the attorney (or a follow-up session) can run the sibling skill against the cluster (fallback when chaining isn't available).

Either way, the memo should make the routing decision visible: which sibling was called, what cluster it consumed, and where its output is attached.

---

## Merge-back: how the sibling's output enters the memo

Most siblings produce a standalone artifact (table, narrative, index). The case-summary memo references the artifact as an exhibit and cites to it:

> See Exhibit A — `deposition-summary` output for the deposition of Dr. Patel. Key admissions at Ex. A, p. 4 (impeachment on prior inconsistent statement).

For artifacts that fit naturally into a memo section (e.g., `medical-record-chronology`'s provider index → `V Evidence inventory`), extract the relevant table/list and place it inline, with attribution to the sibling skill.

A skill that was invoked but returned nothing useful is still named in the memo header (`Sibling skills invoked`) with a note ("no actionable findings"). The attorney should see the full tree of skills that were run, not just the ones that produced output.
