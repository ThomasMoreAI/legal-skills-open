# Norm Decomposition

Use this reference when an answer needs academic precision or when a request basis contains abstract concepts that must be unpacked.

## Purpose

Norm decomposition is the layer below rule-obligation groups. It turns a request-basis path into a recursive check tree:

```text
main norm
  -> positive element
    -> auxiliary norm
      -> lower auxiliary norm
  -> defense norm
    -> counter-defense norm
  -> extinguishment
  -> exercisability
```

## Function Vocabulary

Treat local source labels as vocabulary, not as verified legal conclusions. Common
norm functions include:

- `main_norm`: directly supports a request.
- `incomplete_main_norm`: can support a request only after another norm or
  transaction fills the legal effect.
- `auxiliary_norm`: defines an element, legal status, time point, scope, or
  consequence used by another norm.
- `defense_norm`: blocks right arising, changes/extinguishes the right, or
  blocks exercisability.
- `counter_defense_norm`: defeats a defense or restores the claimant's path.
- `denial_norm`: attacks the factual or normative premise of the opposing path.
- `defense_exclusion_norm`: says a defense does not apply in a triggered case.
- `referral_norm` / `analogy_referral_norm`: points to another rule directly or
  by analogy; do not collapse it into the target rule without saying why.
- `principle_norm`: states a principle or declaration; it usually guides an
  auxiliary or defense analysis rather than serving as the request basis.
- `burden_norm` / `evidence_norm`: controls proof responsibility or evidence
  treatment, especially in litigation mode.
- `scope_norm` / `consequence_norm`: controls remedy range, restitution,
  damages, fruits, expenses, or other follow-on effects.

## Runtime Rule

Use a decomposition program only for the selected detailed request basis. Do not expand the whole civil-law tree.

Minimum output when triggered:

- the main norm or legal transaction basis;
- the immediate elements;
- the auxiliary norms needed to define those elements;
- defenses and counter-defenses at the correct level;
- extinguishment and exercisability checks.

## Precision Switch

- `lite`: name only the element and the decisive fact.
- `standard`: show element, auxiliary norm, defense, and fact.
- `academic`: show the tree and mark each node as satisfied, not satisfied, or uncertain.
- `litigation`: show the tree plus burden, evidence, dispute, proof gap, and verification task.

## Extraction Priorities

When digesting books and case examples, extract in this order:

1. legal characterization nodes, such as unilateral/bilateral/multilateral legal
   act, contract type, possession type, enrichment type, or tort type;
2. formation, validity, effect, scope, extinguishment, and exercisability gates;
3. defenses, counter-defenses, denial norms, and defense exclusions;
4. proof burden, evidence target, and verification tasks;
5. writing rubrics and failure patterns for evals.

## Source Discipline

Norm atoms and analysis programs are not verified law. They are method scaffolds extracted from local references and user feedback. Current law, judicial interpretations, and case-law paths still require authority verification.

## Failure Patterns

- Citing an article but skipping its auxiliary norms.
- Treating an abstract element, such as contract formation, fault, causation, no legal basis, or possession without right, as self-explanatory.
- Listing defenses without saying whether they attack the main norm, an auxiliary norm, an extinguishment gate, or exercisability.
- Expanding every possible auxiliary norm when the facts do not trigger it.

## Reading the Data (verification status — what to trust)

The norm decomposition seed entries carry verification signals at two levels.
Read both before relying on any node:

- **Entry level** (`source_status` / `verification_status`): most atoms and all
  analysis programs are `model_inference` / `pending_mcp`. This means the
  **element decomposition itself is a method scaffold** (通说/学理 framing), not a
  certified legal conclusion. Treat the *structure* as a checklist, not as a
  holding.
- **Citation level** (`legal_basis[].verification_status`): individual statute
  citations may be upgraded independently:
  - `mcp_verified` — the article number → content mapping was checked against an
    authoritative source (e.g., 最高人民法院公报 / 国家法律法规数据库 flk.npc.gov.cn).
    The **条号 is reliable**; the surrounding analysis is still scaffold.
  - `unverified` / `pending_mcp` — not yet checked; do not present as settled law.
  - `conflict_detected` — the local citation disagrees with the authoritative
    source; resolve before use.
- **Version sensitivity**: some citations carry a note (e.g., 公司法担保决议条号
  旧16 → 2023修订后第15条). Always apply the version effective at the relevant time.

So a defensible runtime answer: trust `mcp_verified` 条号, walk the decomposition
tree as a *逐要件检视清单*, and surface every `verification_task` node plus any
`model_inference` framing as "待核", never as certified law.

## Navigating the Programs

- Each `analysis_program` declares `concept_triggers`; match the user's concept
  to a program by trigger, then expand only the branches the facts touch.
- The tree is `program_nodes` + `program_edges`. Follow `decomposes_to` edges down
  to leaf nodes; each leaf carries `check_question` / `fact_target` /
  `burden_holder` — a single fact question you can answer yes/no.
- A node whose label contains `〔委托→…程式〕` is a **delegation leaf**: it is the
  root of another concept's tree (e.g., 意思表示成立与生效, 撤销权行使). Do not
  re-expand it inline; follow `related_atom_ids` to that program.
- The repository's norm-decomposition coverage report tool prints an index of all
  programs and atoms when a coverage overview is needed.
