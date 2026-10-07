# Changelog

All notable changes to this skill are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) · Versioning: [SemVer](https://semver.org/)

## [1.1.1] - 2026-09-25

### Added

- 合并本地未提交改动到上游 1.1.0 之上
- 本地改动：统一展示名为「合同精修」，保持调用 ID 与能力契约。

## [1.1.0] - 2026-08-24

### Added

- add the shared feedback-classification and approval-invalidation gate used by every LovStudio Skill

## [1.0.0] - 2026-07-17

### Added

- Add seven-pass expert contract review covering deal structure, obligations, risk allocation, lifecycle, compliance, disputes, evidence, and operability
- Add risk severity, negotiation priority, replacement wording, fallback positions, signing recommendation, and structured review report
- Add contract-specific playbooks and a current-law verification baseline for Mainland China
- Add stable DOCX anchors across body paragraphs, tables, headers, and footers
- Add preflight validation that rejects ambiguous or format-damaging revisions

### Changed

- Replace the lightweight paragraph scan with professional contract analysis as the default workflow
- Upgrade the primary DOCX interface to `scripts/contract_docx.py`

### Compatibility

- Keep `scripts/annotate_docx.py` as a compatibility adapter for 0.x paragraph-index JSON

## [0.3.1] - 2026-04-16

### Fixed

- Fix comment ID collision and tracked-changes text extraction
- extract: include text inside <w:ins> (tracked changes) — SCHEDULE A etc. now visible
- annotate: auto-detect max comment ID to avoid overwriting pre-existing comments
- annotate: anchor comments inside <w:ins> for tracked-changes paragraphs
- annotate: use CommentsPart._element instead of _blob for reliable persistence

## [0.3.0] - 2026-04-16

### Added

- i18n: bilingual description, triggers, review labels, and annotation tags (EN/ZH)
- Add category: business (商务)
- Expand trigger phrases: annotate document, check contract, 合同审查, 文档批注
- Annotation language now follows document language

## [0.2.0] - 2026-04-15

### Added

- 重命名 review-docx → review-doc，技能名称不再绑定文件格式
- 更新触发词：增加「批阅」「审查合同」等中文触发
- SKILL.md description 重写，突出合同审查核心场景
- README 增加版本 badge
