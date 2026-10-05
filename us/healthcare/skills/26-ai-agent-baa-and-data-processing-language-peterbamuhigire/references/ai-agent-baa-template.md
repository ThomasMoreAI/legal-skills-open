# AI Agent BAA Addendum — Template

**Notice:** this is a drop-in template for the parent Business Associate Agreement. Legal review is required before execution. Adapt by replacing `{placeholder}` values.

---

## Agent Processing Addendum to the Business Associate Agreement

**Covered Entity:** {covered entity legal name}
**Business Associate:** {processor legal name}
**Effective Date:** {YYYY-MM-DD}
**Version:** v{n.m}
**Parent BAA reference:** {document id, date}

This Addendum supplements the parent Business Associate Agreement with obligations specific to agent processing — autonomous and semi-autonomous AI software that plans, calls tools, and acts on behalf of Covered Entity workforce. Capitalised terms not defined here have the meaning given in the parent BAA, HIPAA, or HITECH.

### 1. Scope

This Addendum applies to every Agent Feature operated by Business Associate where the planner may emit tool calls that access, create, modify, or transmit Protected Health Information (PHI) of Covered Entity.

### 2. Definitions

- **Agent Feature** — an autonomous or semi-autonomous software function that plans and executes tool calls on the user's behalf.
- **Agent Service Principal** — the named identity under which the Agent Feature acts within Covered Entity systems.
- **Action Catalogue** — the enumerated set of tools the Agent Feature may invoke.
- **Reversibility Class** — `idempotent`, `compensable`, or `irreversible` per the Action Catalogue.
- **Approval Event** — a signed record of human approval for an irreversible tool call.
- **Kill-switch** — operator-only control that refuses tool calls globally, per tenant, or per feature.

### 3. Permitted uses and disclosures of PHI

Business Associate shall use or disclose PHI processed by the Agent Feature only as permitted by the parent BAA or required by law, and only for purposes documented in the Covered Entity's engagement scope. The Agent Feature shall not be used to train provider models with Covered Entity PHI.

### 4. Agent service-principal access (§164.308(a)(4); §164.312(a)(1))

- The Agent Feature shall act under a named Agent Service Principal scoped to Covered Entity.
- Least-privilege scope shall be enforced at the dispatcher; tool allow-list per Agent Service Principal shall be the operative control.
- Quarterly access review shall be conducted; the review record shall be available to Covered Entity on request within 10 business days.
- Termination of Covered Entity workforce members shall result in revocation of any user-scoped Agent Service Principal access within 24 hours.

### 5. Reversibility, approval, and supervision (§164.312(d))

- Every tool call in the `irreversible` Reversibility Class touching PHI shall be gated by an Approval Event signed by a named Covered Entity workforce member with appropriate role.
- Clinical-PHI Agent Features shall be admin-only: no autonomous external-write actions on systems containing PHI. The L0/L1 admin-only constraint shall apply.
- Supervision Matrix per Agent Feature is provided in Annex A.

### 6. Audit controls (§164.312(b))

- Business Associate shall maintain an append-only, hash-chain integrity-verified audit log of every Agent Feature tool call touching PHI.
- Audit-log retention shall meet or exceed the parent Audit-Log Retention Policy and shall be no less than 6 years from creation or last effective date for PHI-touching records.
- Covered Entity shall have the right to receive a tenant-scoped audit export within 14 days of written request, in CSV or signed JSON format.

### 7. Integrity (§164.312(c)(1))

- Hash-chain integrity of the audit log shall be verified at least daily; integrity reports available to Covered Entity on request.
- Approval Events shall be cryptographically signed.

### 8. Transmission security (§164.312(e)(1))

- All in-transit PHI shall be encrypted using TLS 1.2 or later.
- Tool calls to systems containing PHI shall carry a signed claim on the tenant identity.

### 9. Reporting of incidents and breaches (§164.410)

- Business Associate shall notify Covered Entity of any Breach of Unsecured PHI without unreasonable delay and in any event within sixty (60) calendar days of discovery.
- For Breaches affecting 500 or more individuals, notification shall be immediate (within 24 hours of discovery) to enable Covered Entity to meet its HHS notification obligations.
- Business Associate shall provide all information required for Covered Entity to issue notifications per §164.404 and §164.408 within 5 business days of discovery.
- Agent-specific incident scenarios — cross-tenant retrieval leak, prompt-injection-driven disclosure, audit-log integrity compromise, memory-tier leak — are subject to this clause.

### 10. Subcontractors (§164.308(b)(1); §164.314(a)(2))

- Business Associate shall ensure every subcontractor that creates, receives, maintains, or transmits PHI on behalf of Business Associate executes a Business Associate Agreement.
- For model providers: Business Associate shall either (a) execute a BAA with the provider including a zero-retention configuration verified by contract clause, or (b) de-identify PHI per 45 CFR §164.514 (Safe Harbor or Expert Determination) before transmission to the provider, or (c) host inference on infrastructure controlled by Covered Entity or by Business Associate within Covered Entity's authorisation boundary.
- Sub-processor change notice: Business Associate shall provide 30 calendar days' notice of any material change to subcontractor list; Covered Entity may object in writing during that period.

### 11. Access by individuals (§164.524)

- Where Covered Entity receives a §164.524 request for access, Business Associate shall make available the relevant Agent Feature action history and memory contents within 10 business days of Covered Entity's written request.

### 12. Amendment of PHI (§164.526)

- Business Associate shall make agreed amendments to PHI in Agent Feature memory and downstream systems within 10 business days of Covered Entity's written instruction.

### 13. Accounting of disclosures (§164.528)

- The Agent Feature action audit log shall support the production of an accounting of disclosures per §164.528 within 30 days of written request.

### 14. Memory erasure

- Business Associate shall provide tenant-controlled opt-in for any long-term Agent Feature memory tier.
- On Covered Entity's written request, Business Associate shall erase the relevant memory contents within 30 days and provide a Certificate of Erasure naming the tier, scope, operator, and verification timestamp.

### 15. Kill-switch SLA

- Business Associate shall maintain a per-tenant Kill-switch invocable by Business Associate operations or by Covered Entity admin role, with propagation ≤ 5 seconds.

### 16. Documentation and retention (§164.316(b))

- Business Associate shall retain the documentation supporting this Addendum for 6 years from the date of its creation or the date when it was last in effect, whichever is later.

### 17. Termination

- On termination of the parent BAA, Business Associate shall return or destroy all PHI in Agent Feature memory and shall produce a Certificate of Destruction within 30 days.
- Where return or destruction is infeasible, Business Associate shall extend the protections of this Addendum and limit further use to those purposes that make return or destruction infeasible.

### 18. Cooperation with HHS

- Business Associate shall make its internal practices, books, and records relating to the use and disclosure of PHI available to HHS for purposes of determining compliance with HIPAA.

### 19. Annexes

- Annex A — Supervision Matrix per Agent Feature.
- Annex B — Sub-processor list and verification status.
- Annex C — Audit-log retention schedule.

### 20. Signatures

| Party | Signatory | Title | Date |
|-------|-----------|-------|------|
| Covered Entity | | | |
| Business Associate | | | |

---

**End of Addendum.**
