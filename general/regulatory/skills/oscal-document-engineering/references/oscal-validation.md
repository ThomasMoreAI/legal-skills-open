# OSCAL Validation

Validation proves structure and schema conformance.
It does not prove that the system is compliant or authorized.

## Recommended validation layers

1. JSON, XML, or YAML syntax validation.
2. OSCAL schema validation with `oscal-cli` or equivalent.
3. Compliance Trestle validation for workspace consistency.
4. Source traceability review.
5. Human review of all `needs_review` mappings.

## Commands

```bash
trestle validate -f <oscal-file>
trestle validate -a
oscal-cli validate --disable-constraint-validation <oscal-file>
```

## Report fields

A validation report must include:

- file validated
- validator command
- validator version if available
- status: pass, fail, partial, or not_run
- errors and warnings
- validation timestamp
- reviewer notes

## Common failures

- Missing UUIDs.
- Wrong OSCAL document root.
- Invalid enum values.
- Incorrect resource references.
- Missing parties or responsible roles.
- Control IDs that do not match the selected profile.
