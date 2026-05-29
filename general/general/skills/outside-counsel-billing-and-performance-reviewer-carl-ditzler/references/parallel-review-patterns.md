# Parallel Review Patterns

Use this reference when the invoice population is large enough to justify subagent or parallel review.

## Good Split Patterns
- By firm
- By matter
- By invoice batch
- By quarter or month
- By workstream such as compliance, rates, staffing, and benchmarking

## Reconciliation Rules
- Keep a single master issue taxonomy using [issue-taxonomy.md](issue-taxonomy.md)
- Use the same confidence labels across all sub-reviews
- Preserve `source_file`, invoice ID, and line ID to avoid duplicate findings
- Reconcile duplicate issues before reporting challenged value

## Recommended Workflow
1. Normalize the source data once
2. Split the normalized dataset into non-overlapping slices
3. Assign each slice to a sub-reviewer
4. Merge outputs into one master issue log
5. Run a final pass for double counting, comparator mismatch, and savings inflation

## When Not to Parallelize
- Very small invoice populations
- One matter where all conclusions depend on the same budget or staffing context
- Reviews where the environment cannot safely coordinate subagents
