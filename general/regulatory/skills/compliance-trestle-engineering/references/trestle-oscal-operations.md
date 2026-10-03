# Trestle OSCAL operations reference

## Catalogs and profiles

- Use catalogs for source control sets.
- Use profiles to tailor or import controls.
- Resolve profiles before you generate SSP implementation statements.
- If a profile cannot be resolved locally, mark dependent mappings `needs_review`.

## Component definitions

Use component definitions for reusable services, platforms, applications, and inherited controls.
Do not hide inherited responsibility in SSP prose.
Model it explicitly when possible.

## SSPs

For SSPs, keep these source-linked sections:

- system name and identifiers
- system characteristics
- authorization boundary
- responsible roles and parties
- inventory and components
- implemented requirements and control statements
- diagrams and evidence references

## Markdown authoring

Trestle markdown is useful for human review.
Treat markdown as a review surface.
Treat OSCAL JSON or YAML as the exchange package.
Keep both synchronized through logged assemble and regenerate commands.

## Validation

Validation means:

- schema and model checks passed
- references resolve where tooling can check them
- known warnings are captured

Validation does not mean:

- controls are effective
- mappings are authoritative
- evidence proves implementation
