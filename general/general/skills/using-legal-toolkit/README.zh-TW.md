# using-legal-toolkit

> legal-toolkit 的 router skill。識別跨 6 個 cluster 的使用者意圖，dispatch 到對的 specialist sub-skill；意圖不明時回明確的選單。

Read this in: [English](README.md) | [日本語](README.ja.md) | **繁體中文**

## 這個 skill 做什麼

入口點。聽你的自然語言請求，識別屬於 6 個 cluster 哪一個，dispatch 到對應的 sub-skill。

Router 本身**不做任何 domain 工作** —— 不讀合約、不寫 playbook entry、不產生法律 finding。純粹的 dispatch primitive。

## 6 個 cluster

| Cluster | Sub-skill | Phase |
|---|---|---|
| 📋 **Playbook** — 合約 review / redline / NDA | `legal-contract-review` | **MVP（已上線）** |
| 🔧 **Cross-cluster utility** — playbook author / extend / revise | `legal-playbook-author` | **MVP（已上線）** |
| 📝 **Template** — 起草 privacy / ToS / DPA / NDA | `legal-document-draft` | Phase 2（尚未提供）|
| 🚨 **Runbook** — 事件應變（個資外洩 / 主管機關 / 違約）| `legal-incident-response` | Phase 2（尚未提供）|
| 🔍 **IRAC** — issue spotting / 法律研究 | `legal-issue-spot` / `legal-research` | Phase 3（尚未提供）|
| 📅 **Tracker** — 合約 lifecycle / 法規追蹤 | `legal-contract-tracker` / `legal-regulation-watch` | Phase 4（尚未提供）|
| 🏛️ **Compliance** — 公司治理 / DD 快速 scan | `legal-corporate-governance` / `legal-dd-quickscan` | **Phase 5 BLOCKED** 等獨立 research |

## Dispatch 邏輯

Router 跑 7 題 decision tree（Q1-Q7），first match wins：

1. **Q1** 合約 review / redline / NDA？ → `legal-contract-review`
2. **Q7** 建 / 改 playbook？ → `legal-playbook-author`
3. **Q2** 起草 privacy / ToS / DPA / NDA？ → `legal-document-draft`（尚未提供）
4. **Q3** 事件應變？ → `legal-incident-response`（尚未提供）
5. **Q4** Fact-driven 問題 / 法律研究？ → `legal-issue-spot` / `legal-research`（尚未提供）
6. **Q5** 合約 lifecycle / 法規 feed？ → `legal-contract-tracker` / `legal-regulation-watch`（尚未提供）
7. **Q6** Governance / DD？ → `legal-corporate-governance` / `legal-dd-quickscan`（Phase 5 BLOCKED）

**多意圖**：請求同時 match 多個 Q（例如「review 完順便更新 playbook」），先跑主任務，副任務當 follow-up 提示。

**意圖模糊**：不亂猜。列 6-cluster 選單請使用者選。

**Phase 2-5 尚未提供**：認可意圖 + 解釋 ETA + 提供 fallback path（例如 incident response 通常會回 「請諮詢執業律師」）。

## 何時用

- 你有 legal-toolkit 相關需求但不確定該用哪個 skill
- 第一次裝、想看什麼可以用
- 確認某個任務類型是否被支援

## 何時不用

- 你已經知道要呼叫哪個 sub-skill → 直接 call（`/legal-contract-review`、`/legal-playbook-author`）
- 任務不是法務 → routed 到對應 plugin 的 `using-*` router

## Cold-start onboarding

剛裝完 plugin 不知道從哪開始？

```
/using-legal-toolkit
剛裝好，下一步幹嘛？
```

Router 會列常見起手 path（review 合約 / 建 playbook / 讀 README）。

## Reference

- SKILL.md（router instruction）：[`SKILL.md`](SKILL.md)
- Plugin spec：[`PRODUCT-SPEC.md`](../../PRODUCT-SPEC.md) / [`TECH-SPEC.md`](../../TECH-SPEC.md)
- Roadmap（Phase 2-5 sub-skill ETA）：[`ROADMAP.md`](../../ROADMAP.md)
- Active sub-skill：
  - [`legal-playbook-author`](../legal-playbook-author/SKILL.md)
  - [`legal-contract-review`](../legal-contract-review/SKILL.md)

## License

MIT — 詳見 monorepo root 的 [LICENSE](../../../LICENSE)。
