# using-legal-toolkit

> legal-toolkit の router skill。6 つの機能 cluster に対するユーザー意図を識別し、適切な specialist sub-skill へ dispatch する。意図が曖昧なときは明確な menu を返す。

Read this in: [English](README.md) | **日本語** | [繁體中文](README.zh-TW.md)

## この skill の役割

エントリポイント。自然言語の request を受け、6 機能 cluster のどれに属するかを識別、対応する sub-skill へ dispatch する。

Router 自体は**ドメイン処理を行わない** — 契約を読まない、playbook entry を書かない、法的 finding を生成しない。純粋な dispatch primitive。

## 6 cluster

| Cluster | Sub-skill | Phase |
|---|---|---|
| 📋 **Playbook** — 契約 review / redline / NDA | `legal-contract-review` | **MVP (active)** |
| 🔧 **Cross-cluster utility** — playbook author / extend / revise | `legal-playbook-author` | **MVP (active)** |
| 📝 **Template** — privacy / ToS / DPA / NDA 起草 | `legal-document-draft` | Phase 2（未提供）|
| 🚨 **Runbook** — 事件応変（個資外洩 / 主管機関 / 違約）| `legal-incident-response` | Phase 2（未提供）|
| 🔍 **IRAC** — issue spotting / 法律 research | `legal-issue-spot` / `legal-research` | Phase 3（未提供）|
| 📅 **Tracker** — 契約 lifecycle / 法規 watch | `legal-contract-tracker` / `legal-regulation-watch` | Phase 4（未提供）|
| 🏛️ **Compliance** — 公司治理 / DD quickscan | `legal-corporate-governance` / `legal-dd-quickscan` | **Phase 5 BLOCKED** on research |

## Dispatch logic

Router は 7 問の decision tree（Q1-Q7）を順に適用、first match wins：

1. **Q1** 契約 review / redline / NDA？ → `legal-contract-review`
2. **Q7** playbook 建てる / 改修？ → `legal-playbook-author`
3. **Q2** privacy / ToS / DPA / NDA 起草？ → `legal-document-draft`（未提供）
4. **Q3** 事件応変？ → `legal-incident-response`（未提供）
5. **Q4** Fact-driven 問題 / 法律 research？ → `legal-issue-spot` / `legal-research`（未提供）
6. **Q5** 契約 lifecycle / 法規 feed？ → `legal-contract-tracker` / `legal-regulation-watch`（未提供）
7. **Q6** Governance / DD？ → `legal-corporate-governance` / `legal-dd-quickscan`（Phase 5 BLOCKED）

**Multi-intent**：複数 Q マッチ時（例：「review してついでに playbook 更新したい」）、主タスクを先に実行、副タスクは follow-up として提示。

**Ambiguous intent**：推測しない。6-cluster menu を提示し、ユーザーに選んでもらう。

**未提供**: Phase 2-5 マッチ時、意図を acknowledge + ETA 説明 + fallback path 提案（事件応変なら「執業弁護士に相談」など）。

## 使うとき

- legal-toolkit 関連の task があるが、どの skill か不明
- 初回 install 時、何があるか確認したい
- 特定 task が対応されているか確認したい

## 使わないとき

- 既に具体的 sub-skill が分かっている → 直接 call（`/legal-contract-review`、`/legal-playbook-author`）
- 法務タスクではない → 適切な plugin の `using-*` router へ

## Cold-start onboarding

Plugin を install したばかりでどこから始めれば良いか分からない場合：

```
/using-legal-toolkit
インストールしたばかり、次は？
```

Router がよくある起点 path を提示（契約 review / playbook 構築 / README 読む）。

## Reference

- SKILL.md（router instruction）：[`SKILL.md`](SKILL.md)
- Plugin spec：[`PRODUCT-SPEC.md`](../../PRODUCT-SPEC.md) / [`TECH-SPEC.md`](../../TECH-SPEC.md)
- Roadmap（Phase 2-5 sub-skill ETA）：[`ROADMAP.md`](../../ROADMAP.md)
- Active sub-skill：
  - [`legal-playbook-author`](../legal-playbook-author/SKILL.md)
  - [`legal-contract-review`](../legal-contract-review/SKILL.md)

## License

MIT — monorepo root の [LICENSE](../../../LICENSE) 参照。
