# Verification Queue

Use this reference when a local rule, request basis, article number, judicial interpretation, or case-law path needs authority checking.

## Core Rule

Do not upgrade local material into current law directly.

Instead:

1. Identify the exact target: request basis, rule group, rule node, source assertion, cause of action, or eval rule.
2. Write a concrete verification question.
3. Record required source types: current law, judicial interpretation, official court document, case-law database, administrative regulation, department rule, local rule, or original PDF.
4. Add or update a verification-queue entry when the package has one; otherwise list the task in the output.
5. After MCP/authority search, update only the verified target fields.

## Status Updates

Local extraction starts as:

```yaml
source_status: source_extracted
verification_status: unverified
mcp_verification_required: true
```

Pending verification task:

```yaml
source_status: model_inference
verification_status: pending_mcp
mcp_verification_required: true
```

Authority-confirmed law node:

```yaml
source_status: verified_law
verification_status: mcp_verified
```

Conflict:

```yaml
verification_status: conflict_detected
```

## Partial Verification

If a statute is verified but case-law is not, only mark the statute rule node as verified. Do not mark the whole rule-obligation group as verified.

If current law is verified but OCR/source text is suspicious, keep the source assertion flagged for human review.

## High-Priority Queue

First consume tasks about:

- product liability and consumer/food special rules;
- medical damage, informed consent, and medical records;
- traffic accident insurance order and recourse;
- sale quality defect and price payment defenses;
- divorce property division and period limits.
