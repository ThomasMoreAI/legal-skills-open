# OSCAL SSP authoring examples

## Example: AC-2 implementation statement

Source text: "User accounts are requested through the ticketing system and approved by the system owner. Privileged access requires MFA."

Draft:

- Control ID: AC-2
- OSCAL target: `system-security-plan.control-implementation.implemented-requirements[AC-2]`
- Statement: User account provisioning starts through the ticketing system and requires system owner approval. Privileged account access requires MFA.
- Source IDs: SRC-014
- Status: mapped
- Confidence: medium
- Reviewer notes: Validate account removal and periodic review procedures from additional evidence.

## Example: unsupported mapping

Source text: "Access is managed securely."

Draft:

- Control ID: AC-2
- Status: needs_review
- Reason: The source does not identify account request, approval, removal, privileged access, or review procedures.

Do not turn generic policy language into specific implementation claims.
