# Custom Checklists

Create a `.qc-checklist.md` file in your project directory to override the standard checklist. The file format:

```markdown
# My Custom Checklist

## Core (Quick depth)
1. [Item] — [What to check]
2. [Item] — [What to check]

## Extended (Standard depth)
3. [Item] — [What to check]

## Deep (Deep depth)
4. [Item] — [What to check]
```

## Example: M&A Due Diligence Report

```markdown
# M&A DD Report QC

## Core
1. Target entity correctly identified throughout
2. Financial figures match source documents
3. Material risks identified and categorized
4. Jurisdictions correctly identified
5. Deal structure accurately described

## Extended
6. Regulatory approvals list complete
7. Change of control provisions flagged
8. Employee/pension obligations quantified
9. IP portfolio accurately described
10. Litigation/disputes list matches court records
11. Tax structure implications assessed
12. Environmental liabilities flagged

## Deep
13. Cross-reference financial figures against two independent sources
14. Verify regulatory timeline against published processing times
15. Check target's public filings for consistency with DD findings
16. Stress-test material assumptions
17. Flag any reliance on management representations without independent verification
```

## Example: Contract Review

```markdown
# Contract QC

## Core
1. Parties correctly identified with legal names
2. Defined terms used consistently
3. Commercial terms match term sheet
4. Governing law and jurisdiction specified
5. Termination provisions clear and balanced

## Extended
6. Limitation of liability proportionate
7. IP assignment/license scope appropriate
8. Confidentiality obligations reciprocal or justified
9. Force majeure scope appropriate
10. Assignment/change of control restrictions present
11. Notice provisions complete (addresses, methods, deemed receipt)
12. Boilerplate complete (entire agreement, severability, waiver, amendments)

## Deep
13. Cross-reference against counterparty's standard terms for conflicts
14. Check referenced statutes/regulations are current
15. Verify corporate authority requirements
16. Review against applicable sanctions/compliance requirements
17. Check insurance requirements against market standards
```

## Example: Code/Script Review

```markdown
# Script QC

## Core
1. All file paths valid and accessible
2. Dependencies available
3. Error handling present
4. Safe to run twice (idempotent)
5. No hardcoded secrets or credentials

## Extended
6. Input validation present
7. Logging sufficient for debugging
8. Performance acceptable for expected data size
9. Edge cases handled (empty input, missing files, permissions)
10. Output verified independently after execution

## Deep
11. Security review (injection, path traversal, privilege escalation)
12. Rollback mechanism exists
13. Resource cleanup on failure
14. Concurrent execution safety
15. Documentation matches actual behavior
```
