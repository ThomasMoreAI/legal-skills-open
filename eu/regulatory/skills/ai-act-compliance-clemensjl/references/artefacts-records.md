# Artefact templates: inventory and classification records

Every generated artefact carries `<!-- DRAFT — not legally cleared -->` as the first line until sign-off is confirmed. Unknown values stay as `[[MISSING: …]]` in the artefact **and** in the report back to the user. Never fill a placeholder with a plausible value.

## 1. AI system inventory entry

One row per AI system. This is the register everything else is scoped from — the literacy programme, the classification records, the registration actions.

```yaml
# <!-- DRAFT — not legally cleared -->
id: [[AIS-0001]]
name: [[internal product or feature name]]
owner: [[named person accountable]]
description: [[one sentence a non-engineer would recognise]]
intended_purpose: [[the wording used in contract, docs and marketing — legal anchor per Art 3(12)]]
status: [[in development | in production | retired]]
first_placed_on_market: [[YYYY-MM-DD or n/a]]

models:
  - name: [[model name]]
    version: [[version or snapshot id]]
    provider: [[upstream provider]]
    hosted_by: [[us | upstream | other]]
    modified_by_us: [[none | prompt only | fine-tune | continued pretraining]]
    training_compute_flop: [[MISSING: only if we trained or continued pretraining]]

roles_we_hold:            # Art 3(3) to (7), Art 25
  provider: [[yes | no]]
  deployer: [[yes | no]]
  importer: [[yes | no]]
  distributor: [[yes | no]]
  authorised_representative: [[yes | no]]
  role_flip_risk: [[Art 25(1)(a)/(b)/(c) assessment — one sentence]]

territorial_trigger: [[Art 2(1)(a) | (b) | (c) — which and why]]

risk_class:               # from decision-tree.md
  prohibited: [[no | yes — feature stopped]]
  high_risk_annex_i: [[no | yes — Annex I point …]]
  high_risk_annex_iii: [[no | yes — Annex III point …]]
  art_6_3_filter_applied: [[n/a | yes — condition (a)/(b)/(c)/(d)]]
  profiling: [[yes | no]]     # yes always defeats the filter, Art 6(3) 3rd subpara
  art_50_triggers: [[50(1) | 50(2) | 50(3) | 50(4) | none]]
  classification_record: [[link to the record in section 2]]

applicable_from:          # from timeline.md
  art_4_literacy: 2025-02-02     # in force
  art_5: [[2025-02-02 | 2026-12-02 for points (ba),(bb)]]
  art_50: [[2026-08-02 | 2026-12-02 for Art 50(2) if placed before 2026-08-02]]
  chapter_iii: [[n/a | 2027-12-02 (Annex III) | 2028-08-02 (Annex I)]]

personal_data:
  processed: [[categories]]
  special_categories_art_9: [[no | yes — basis, incl. Art 4a AI Act if bias detection]]
  dpia: [[not required | done YYYY-MM-DD | MISSING]]
  gdpr_art_22_decision: [[yes | no]]

registrations:
  eu_database_art_49_1: [[n/a | due | done YYYY-MM-DD]]
  eu_database_art_49_2: [[n/a | due | done YYYY-MM-DD]]   # non-high-risk conclusion
  eu_database_art_49_3: [[n/a | due | done]]              # public authority deployer
  national_art_49_5: [[n/a | due | done]]                 # Annex III point 2

open_items:
  - [[MISSING: …]]
```

## 2. Role and risk classification record

The reasoning is the artefact. A conclusion without reasoning is worthless to an authority and worthless to the next engineer.

```markdown
<!-- DRAFT — not legally cleared -->
# Classification record — [[system name]] ([[AIS-0001]])

Date: [[YYYY-MM-DD]] · Author: [[name]] · Legal review: [[name | MISSING]]
Basis: Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744.

## 1. Is it an AI system? — Art 3(1)
Machine-based: [[…]] · Autonomy: [[…]] · Adaptiveness: [[…]] · Objectives: [[…]]
Inference from input to output: [[the decisive element — describe it]]
Output types: [[predictions | content | recommendations | decisions]]
**Conclusion:** [[is / is not]] an AI system. Reasoning: [[…]]

## 2. Scope — Art 2
Territorial trigger: [[Art 2(1)(a)/(b)/(c)]] because [[…]]
Exclusions tested: 2(3) [[…]] · 2(6) [[…]] · 2(8) [[…]] · 2(10) [[…]] · 2(12) [[…]]
**Conclusion:** in scope / out of scope because [[…]]

## 3. Role — Art 3(3) to (7), Art 25
Placed on the market under whose name or trademark: [[…]]
Do we rebrand, substantially modify, or repurpose a third-party system? [[…]]
Upstream terms: does the initial provider state the system is not to be changed
into a high-risk system (Art 25(2) last sentence)? [[yes — no cooperation duty | no | MISSING]]
Written agreement under Art 25(4) with upstream suppliers: [[in place | MISSING]]
**Conclusion:** we are [[provider | deployer | …]] of this system, because [[…]]

## 4. Prohibitions — Art 5
(a) [[no]] · (b) [[no]] · (ba) [[no — from 2026-12-02]] · (bb) [[no — from 2026-12-02]]
(c) [[no]] · (d) [[no]] · (e) [[no]] · (f) [[no]] · (g) [[no]] · (h) [[n/a]]
For generative image or video: safeguards against the Art 5(1a)(a)(ii)
reasonably-foreseeable-and-reproducible test: [[describe | MISSING]]
**Conclusion:** [[not prohibited | STOP — prohibited under Art 5(1)(…)]]

## 5. High-risk — Art 6
Annex I route: safety component under Art 3(14) as amended? [[…]]
  Art 6(1a) exclusion (user assistance, optimisation, efficiency, automation,
  convenience, quality control)? [[…]]  Art 6(1b) health-and-safety override? [[…]]
  Third-party conformity assessment required for the product? [[…]]
  Section A or Section B of Annex I: [[…]]
Annex III route: area and sub-point: [[…]] or none
  Art 6(3) chapeau — significant risk of harm / material influence on the
  decision outcome: [[…]]
  Condition relied on: [[(a) narrow procedural | (b) improve completed human
  activity | (c) detect patterns without replacing or influencing | (d) preparatory]]
  **Profiling of natural persons (GDPR Art 4(4))?** [[yes → high-risk regardless |
  no — reasoning]]
**Conclusion:** [[not high-risk | high-risk under Annex III point … | high-risk under Annex I]]
If not high-risk under Art 6(3): Art 6(4) documented assessment is this record,
and Art 49(2) registration is [[due | done YYYY-MM-DD]].

## 6. Art 50 transparency
50(1) directly interactive: [[yes/no]] — obvious exception relied on? [[no | yes, with reasoning]]
50(2) synthetic output: [[modalities]] — out-of-scope categories claimed: [[…]]
50(3) emotion recognition / biometric categorisation: [[yes/no]]
50(4) deep fakes / published text: [[yes/no]]
**Conclusion:** obligations [[…]], applicable from [[2026-08-02 | 2026-12-02]]

## 7. Resulting obligation list
[[table: obligation | article | owner | due date | status]]

## 8. Open items
- [[MISSING: …]]

## 9. Sign-off
Classification near a boundary: [[yes/no]]. Legal sign-off [[obtained on … | REQUIRED, not yet obtained]].
```

## Checkpoints

- [ ] Draft marker present as the first line of every generated artefact
- [ ] No placeholder silently filled with a plausible value
- [ ] Inventory entry exists for every AI system, not only the high-risk ones
- [ ] Role recorded per system and tested against the Art 25(1) flip
- [ ] Classification record carries reasoning, not just a conclusion, and names the profiling answer
- [ ] Any Art 6(3) "not high-risk" record is paired with an Art 49(2) registration action
- [ ] Applicable dates attached per obligation, from `timeline.md`
- [ ] Boundary classifications marked as requiring legal sign-off, and the sign-off line left unsigned until obtained
- [ ] Open items repeated in the report back to the user

Disclosure, documentation, oversight and logging templates are in `artefacts-disclosures.md`.
