# Rule Obligation Groups

Rule-obligation groups are the intermediate knowledge unit between raw local materials and final legal analysis.

Use them when a case or research question involves:

- multiple possible claim targets;
- multiple request bases behind one fact pattern;
- defenses or counter-defenses that shape the request;
- cause-of-action labels needed for filing or retrieval;
- recurring evidence targets and proof gaps.

## Runtime Use

1. Start from the claim goal: who seeks what from whom.
2. Find matching claim texts or entry mappings in the rule-obligation seed.
3. Use `entry_mappings` to separate:
   - substantive request-basis paths;
   - backup paths;
   - filing/retrieval/calibration causes of action;
   - excluded or deferred paths.
4. Use `rule_nodes` only according to their function:
   - `main_norm`: request-effect norm or main legal basis;
   - `definition_norm`: characterization rule, especially for legal act type and concept boundaries;
   - `auxiliary_norm`: concretizes elements or effects;
   - `defense_norm`: supports a defense;
   - `case_law_concretization`: only a research prompt unless case-law is retrieved;
   - `scholarly_rule`: method or academic framing, not verified law.
5. Use `elements` and `defenses` to build the issue list.
6. Use `evidence_targets` to build proof tasks.
7. Use `source_assertions` and `supports_rule_ids` to explain where each rule node came from.

## Source Integration

When adding new materials, do not append raw summaries to the group. First extract atomic source assertions, then merge them into existing rule nodes or create narrowly scoped new nodes.

Use the source-integration reference for the full update protocol. The short rule is:

```text
new material -> source assertion -> rule node -> group update -> verification task
```

For materials like the Ninth Civil Minutes, newer judicial interpretations, academic papers, and case-law reports, preserve source identity and effect status separately. A proposition can support a rule node without making that node verified law.

## Coverage Control

A rule-obligation group is a layered rule graph, not an encyclopedia.

For `institution_module` groups, `request_basis_ids` and `cause_of_action` may be empty. They are reusable trigger modules, not standalone claim paths.

Use three rings:

- Core ring: request bases, elements, defenses, counter-defenses, effects, and evidence rules that directly decide the current claim target.
- Conditional ring: rules triggered by specific facts, such as capacity, agency, approval, registration, standard terms, limitation period, or special-law status.
- Reference ring: background doctrine, broad legal institutions, distant auxiliary rules, or case-law matrices. Link them through `related_group_ids` or verification tasks instead of copying them into every group.

For rule nodes, prefer:

- `necessity: core` when the node must be checked every time;
- `necessity: conditional` when facts must trigger it;
- `necessity: background` for academic or explanatory material;
- `necessity: deferred` when it needs MCP/authority verification first.

Use `depth` to stop uncontrolled expansion:

- `0`: direct rules for the current claim target;
- `1`: necessary auxiliary rules;
- `2`: conditional trigger rules;
- avoid automatic `3+` expansion unless the user asks for a research map.

Example: a sale-price group can contain “contract formation” as a core element, but it should link to a contract-formation or juristic-act module for capacity, agency, intent-expression interpretation, approval, or registration issues instead of copying all those rules.

## Output Discipline

- Do not treat the group itself as verified law.
- Do not copy a rule node into the final answer as current law unless MCP/authority verification has been performed.
- Do not collapse statutes, judicial interpretations, minutes, papers, and cases into a single undifferentiated rule.
- Do not put defenses into `claim_texts`; defenses belong in `defenses`.
- Do not invent a cause of action placeholder. If the cause is uncertain, mark the mapping as `deferred` or `needs_human_review`.
- If one claim target maps to several request bases, keep all paths visible until excluded with reasons.
- Do not include every remotely related article. Include core rules, add conditional triggers, and defer broad background to linked modules or verification queue.
- If a group depends on a legal act, link or trigger the legal-act characterization module instead of skipping formation and effectiveness.

## Minimal Runtime Table

```markdown
| 请求目标 | 请求权基础 | 规则义务群 | 候选案由 | 用途 | 不确定性 |
| --- | --- | --- | --- | --- | --- |
```

## Current Seed Groups

- `rog_sale_price_quality_001`: sale price, delayed payment loss, quality-defect defense.
- `rog_lease_property_return_001`: lease return, property return, use fee/unjust enrichment.
- `rog_contract_tort_damage_competition_001`: contract/tort damages competition.
- `rog_unjust_enrichment_payment_return_001`: payment unjust enrichment and failed-contract return.
- `rog_security_obligation_public_place_001`: public-place safety obligation tort.
- `rog_product_liability_contract_consumer_001`: product liability, sale quality defects, consumer special rules.
- `rog_medical_damage_records_consent_001`: medical damage, informed consent, medical records.
- `rog_traffic_accident_insurance_001`: traffic accident damages, insurance order, recoupment.
- `rog_divorce_property_division_001`: divorce and post-divorce property division.
- `rog_reward_advertisement_juristic_act_001`: reward advertisement payment, legal-act characterization, formation, effectiveness, completion, withdrawal/change.
- `module_contract_formation_and_validity`: reusable contract formation, intent, validity, agency, standard terms, and contract interpretation module.
