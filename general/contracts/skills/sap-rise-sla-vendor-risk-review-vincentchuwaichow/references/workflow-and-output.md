# Workflow and output contract — RISE with SAP SLA and Vendor Risk Review

Use this reference for contract domain classification, responsibility layer assessment, SLA evaluation, and output formatting.

## Contract domain taxonomy

| Contract domain | Scope | Typical findings |
|-----------------|-------|-----------------|
| `responsibility-split` | Who manages what across infrastructure, platform, application, and data layers (SAP vs customer vs partner) | Customer assumes responsibility for application configuration that SAP actually manages; partner obligations not captured in a tripartite agreement; data layer ownership ambiguous |
| `sla-and-credits` | SLA tier definitions, availability targets, credit calculation, credit request process, credit caps | Credit cap insufficient to compensate for downtime cost; credit request window too short (e.g., 30 days vs 90 days); SLA exclusions broad enough to negate most credits |
| `availability-and-dr` | System availability commitments, planned maintenance windows, disaster recovery RTO/RPO, business continuity | DR RTO/RPO not specified in contract; maintenance windows not aligned with customer business hours; no contractual obligation to notify before maintenance |
| `data-residency` | Data processing location, cross-border transfer mechanisms, data residency options, processing sub-processors | Contractual residency clause without audit evidence; cross-border transfer mechanism (SCC, BCR) not specified; sub-processor list not disclosed or not current |
| `exit-and-portability` | Data export provisions, export format and timeline, contract exit obligations, post-termination data retention and deletion | Export format not specified; export timeline too short for a large data volume; export billed at unreasonable cost; post-termination retention period not defined |
| `security-responsibilities` | Shared security model, customer security obligations, SAP security obligations, incident response, vulnerability disclosure | Customer security obligations not documented; SAP incident notification SLA not contractually bound; no contractual obligation to perform penetration testing on the customer's instance |
| `audit-rights` | Customer audit rights, third-party certification, SAP-provided audit reports, regulator access | Audit right limited to SAP-provided reports only with no independent audit option; certification scope does not cover the customer's deployed configuration; regulator access not addressed |

## Risk severity classification

| Risk level | Criteria |
|-----------|---------|
| `critical` | Contractual gap that creates unmanaged regulatory non-compliance (e.g., GDPR data residency breach, no data processing agreement), business continuity exposure with no contractual remedy, or complete absence of an SLA for a production system |
| `high` | Ambiguous responsibility boundary for a critical function (e.g., backup and restore ownership unclear), SLA credit mechanism that is practically unusable (cap below cost of downtime, request window too short), or exit provision that does not guarantee data return |
| `medium` | Missing provision that is negotiable but currently absent (e.g., no maintenance window notification obligation), SLA exclusion that is broad but the risk is manageable with compensating controls, or data residency clause without audit evidence |
| `low` | Best practice deviation in contract structure (SLA definitions are present but not referenced from the operational runbook, portability clause present but format not specified) |

## Responsibility layer classification

For each finding, classify the responsibility layer:

- `sap-managed`: SAP is solely responsible per the published shared responsibility model and contract
- `customer-managed`: The customer is solely responsible per the published shared responsibility model and contract
- `partner-managed`: A system integrator or implementation partner holds the obligation per a separate engagement agreement
- `shared`: Both SAP and customer hold obligations — define the split explicitly
- `ambiguous`: The contract or published model does not clearly assign responsibility — this is itself a risk finding

## Workflow

1. **Receive artifacts** — contract excerpts, SLA schedules, order forms, SAP Trust Center references, or written descriptions of contractual obligations.
2. **Classify each finding** by contract domain.
3. **Classify responsibility layer** for each finding (SAP-managed / customer-managed / partner-managed / shared / ambiguous).
4. **Assign risk level** (critical / high / medium / low).
5. **Assess against SAP published baseline** — compare user-provided terms against SAP Trust Center published standards and shared responsibility model.
6. **Prioritize** — critical compliance and business continuity gaps first; then high responsibility and SLA issues; then medium missing provisions; then low best-practice items.
7. **Return output** per the output contract below.

## Output contract

Return:

1. Contract domain and specific finding
2. Responsibility layer (SAP-managed / customer-managed / partner-managed / shared / ambiguous)
3. Evidence label (documentation-based / user-provided evidence / inference)
4. Risk level per finding (critical / high / medium / low)
5. Recommended action (renegotiate clause, request SLA addendum, obtain certification evidence, implement compensating control, engage legal counsel)
6. Business impact (regulatory exposure, business continuity gap, vendor lock-in risk, audit finding risk)
7. Escalation trigger if legal interpretation or live contract access is required
