# Source Synthesis

Use this reference when the user asks to integrate reference materials or deepen request-basis catalog coverage.

## Purpose

Source synthesis is the layer between raw references and runtime analysis. It groups sources by request-basis family so the model can reuse legal-method structure without loading books or OCR material wholesale.

## Position

```text
source registry / locator index
  -> atomic source assertions
  -> concept cards and request-basis seeds
  -> rule-obligation groups
  -> request-basis synthesis
  -> lite runtime
```

## What a Synthesis Entry Does

A synthesis entry records:

- claim family or institution module;
- linked request-basis ids;
- linked rule-obligation groups;
- contributing source ids and source roles;
- concept triggers;
- claim goal patterns;
- lifecycle focus;
- element, defense, and evidence axes;
- authority verification questions;
- coverage gaps and next actions.

## Use Rules

- Synthesis entries are not verified law.
- Do not quote source materials through this layer.
- Do not treat a synthesis title as a request basis.
- Use synthesis to choose which request-basis seeds, concept cards, rule groups, and verification tasks to inspect.
- If no synthesis entry fits, create a temporary synthesis with `model_inference` and list the missing catalog coverage.

## Merge Discipline

Merge sources into a synthesis only when they share the same claim goal family, legal effect, trigger facts, and rule function. Preserve conflicting or time-sensitive propositions as verification questions rather than smoothing them into a single conclusion.

## Runtime Discipline

In ordinary legal outputs, show only the operational result: candidate request targets, request bases, elements, defenses, evidence gaps, and verification tasks. Keep source ids, extraction notes, and maintenance gaps in catalog/build mode unless the user asks for them.
