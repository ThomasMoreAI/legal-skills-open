# using-legal-toolkit

> Router skill for legal-toolkit. Identifies user intent across 6 functional clusters and dispatches to the right specialist sub-skill — or returns a clear menu when intent is ambiguous.

Read this in: **English** | [日本語](README.ja.md) | [繁體中文](README.zh-TW.md)

## What this skill does

The entry point. Listens to your natural-language request, identifies which of the 6 functional clusters your task belongs to, and dispatches to the appropriate sub-skill.

The router itself does **no domain work** — never reads contracts, never writes playbook entries, never produces legal findings. It is a pure dispatch primitive.

## 6 clusters

| Cluster | Sub-skill | Phase |
|---|---|---|
| 📋 **Playbook** — contract review / redline / NDA | `legal-contract-review` | **MVP (active)** |
| 🔧 **Cross-cluster utility** — author / extend / revise playbook | `legal-playbook-author` | **MVP (active)** |
| 📝 **Template** — draft privacy / ToS / DPA / NDA | `legal-document-draft` | Phase 2 (not yet) |
| 🚨 **Runbook** — incident response (個資外洩 / 主管機關 / 違約) | `legal-incident-response` | Phase 2 (not yet) |
| 🔍 **IRAC** — issue spotting / legal research | `legal-issue-spot` / `legal-research` | Phase 3 (not yet) |
| 📅 **Tracker** — contract lifecycle / regulation watch | `legal-contract-tracker` / `legal-regulation-watch` | Phase 4 (not yet) |
| 🏛️ **Compliance** — 公司治理 / DD quickscan | `legal-corporate-governance` / `legal-dd-quickscan` | **Phase 5 BLOCKED** on research |

## How dispatch works

The router applies a 7-question decision tree (Q1-Q7) in order, first match wins:

1. **Q1** Contract review / redline / NDA? → `legal-contract-review`
2. **Q7** Build / modify playbook? → `legal-playbook-author`
3. **Q2** Draft privacy / ToS / DPA / NDA? → `legal-document-draft` (not yet)
4. **Q3** Incident response? → `legal-incident-response` (not yet)
5. **Q4** Fact-driven question / legal research? → `legal-issue-spot` / `legal-research` (not yet)
6. **Q5** Contract lifecycle / regulation feed? → `legal-contract-tracker` / `legal-regulation-watch` (not yet)
7. **Q6** Governance / DD? → `legal-corporate-governance` / `legal-dd-quickscan` (Phase 5 BLOCKED)

**Multi-intent**: when the request matches multiple Q's (e.g. "review this and update the playbook for it"), run the main task first; then offer the secondary as a follow-up.

**Ambiguous intent**: don't guess. Present the 6-cluster menu and ask the user to pick.

**Not-yet-available**: when matched intent is Phase 2-5, acknowledge + explain ETA + offer fallback path where one exists (often: "consult a practising lawyer" for incident response).

## When to use

- You have a legal-toolkit-related task but aren't sure which skill
- First-time install: see what's available
- Confirming whether a particular task type is supported

## When NOT to use

- You already know the specific sub-skill — just call it directly (`/legal-contract-review`, `/legal-playbook-author`)
- The task isn't legal — route to the right plugin's `using-*` router

## Cold-start onboarding

If you just installed the plugin and don't know where to start:

```
/using-legal-toolkit
我剛裝好，下一步幹嘛？
```

The router will offer common starting paths (review a contract / build playbook / read the README).

## Reference

- SKILL.md (router instructions): [`SKILL.md`](SKILL.md)
- Plugin spec: [`PRODUCT-SPEC.md`](../../PRODUCT-SPEC.md) / [`TECH-SPEC.md`](../../TECH-SPEC.md)
- Roadmap (Phase 2-5 sub-skill ETA): [`ROADMAP.md`](../../ROADMAP.md)
- Active sub-skills:
  - [`legal-playbook-author`](../legal-playbook-author/SKILL.md)
  - [`legal-contract-review`](../legal-contract-review/SKILL.md)

## License

MIT — see [LICENSE](../../../LICENSE) at the monorepo root.
