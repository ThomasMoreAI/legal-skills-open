# AI DPIA Addendum Template

## 1. Identification

- Processing operation: AI features in <Product>.
- Controller: <Customer> (joint with us where contracted).
- Processor: <Our Company>.
- Sub-processors: see sub-processor list.
- Date: YYYY-MM-DD.
- Owner: <DPO>.

## 2. Nature, Scope, Context, Purpose

- Nature: AI features (RAG, generative, agentic) that process user inputs and tenant-scoped content through hosted model providers and a per-tenant vector store.
- Scope: workspaces enabled for the AI features; data classes in §3.
- Context: SaaS multi-tenant; B2B; regulated and non-regulated tenants.
- Purpose: aid users in summarisation, drafting, analysis, and approved automated workflows.

## 3. Data Categories

| Category | Examples | Classification | Volume |
|----------|----------|----------------|--------|
| Account data | user id, email | PII | low |
| Customer content | uploaded docs, threads | confidential, may contain PII / SPI | high |
| Conversation logs | prompt + response | confidential | medium |
| Telemetry | aggregate metrics | aggregate / anonymised | medium |

## 4. Data Flows

See diagram. Key flows:

1. User -> our service (TLS).
2. Our service -> retrieval store (tenant-scoped query).
3. Our service -> model gateway -> model provider (TLS; no-training endpoint).
4. Model provider -> gateway -> our service.
5. Gateway -> conversation log (per-tenant partition; 90 d hot / 13 mo cold).
6. Gateway -> billing event (per-tenant; usage-only fields).
7. Nightly eval -> judge-LLM provider (sample of redacted responses).

## 5. Lawful Basis

| Activity | Basis (GDPR Art. 6) | Notes |
|----------|-----------------------|-------|
| Processing user inputs to fulfil the AI feature | Art. 6(1)(b) contractual necessity OR (f) legitimate interest with balancing test |  |
| Processing PII in retrieved content | Art. 6(1)(b) | controller's underlying basis |
| Conversation log retention for QA, security, troubleshooting | Art. 6(1)(f) legitimate interest |  |
| Eval sample replay | Art. 6(1)(f) legitimate interest with anonymisation pre-pass |  |
| Special category data (Art. 9) | only if controller has Art. 9(2) basis | we do not process Art. 9 data unless controller declares |

## 6. Necessity and Proportionality

- Minimum data: prompts limited to needed context; PII redacted pre-prompt where feasible.
- Retention: shortest viable, per region and per data class.
- Purpose limitation: data used for the AI feature only.
- Accuracy: hallucination SLO + flagging mechanism; abstain rules.

## 7. Risks to Data Subjects (AI-specific)

| Risk | Likelihood | Severity | Mitigation |
|------|-----------|----------|------------|
| Opacity of automated decision | -- | M | Right to explanation copy + human-in-the-loop |
| Hallucination misattributes facts to a data subject | M | H | factuality SLO + flagging + retraction process |
| Prompt-injection extracts data | M | H | system-message guards + red-team scenarios + content filter |
| Cross-tenant retrieval leak | L | H | per-tenant index + tenant-claim enforcement + isolation evidence |
| Conversation log surfaces PII unintentionally | M | M | PII redaction pre-processor + tenant-partitioned logs |
| Training-data exclusion lapse | L | H | contract clause + endpoint flag + quarterly audit |
| Sub-processor change | M | M | 30-day notice + right of objection |

## 8. Measures and Residual Risk

After mitigations, residual risk is: <low / medium>. If medium or high, Art. 36 consultation is required for EU.

## 9. Cross-Border Transfers

- EU -> US: <DPF certification | SCCs + TIA + supplementary measures>.
- Within EEA: no additional mechanism required.
- Kenya: data-residency commitment in <region> per DPA s.49.
- Nigeria: per NDP Act 2023 Schedule.
- South Africa: per POPIA s.72.

## 10. Consent Capture

- Surface: first-use modal per region.
- Storage: per-tenant settings with timestamp + admin id.
- Revocation: workspace settings toggle.
- Re-prompt rule: any regulatory tier change or new region launch.

## 11. Sign-off

- DPO: <name>, date.
- Legal: <name>, date.
- AI Lead: <name>, date.
- Security Lead: <name>, date.

## 12. Review Cadence

Quarterly + on regulatory change + on feature change + on sub-processor change.
