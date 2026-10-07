# SELF_CHECK — policy-application-checker

## 1. 规范检查

- [x] Skill 为独立文件夹
- [x] 包含 `SKILL.md`
- [x] `SKILL.md` 使用 YAML frontmatter
- [x] frontmatter 含 `name`、`description`、`version`
- [x] 运行依赖声明在 `metadata.openclaw.requires`
- [x] 包含 `README.md`
- [x] 包含 `scripts/` 且至少 1 个脚本
- [x] 包含 `resources/` 且至少 1 个资源文件
- [x] 包含 `examples/example-prompt.md`
- [x] 包含 `tests/smoke-test.md`

## 2. 路径与引用检查

- [x] `SKILL.md` 中引用了 `scripts/checklist_builder.py`
- [x] `SKILL.md` 中引用了 `resources/checklist_template.md`
- [x] `README.md`、`SELF_CHECK.md`、`tests/smoke-test.md` 路径与当前目录一致
- [x] 打包后无需依赖绝对路径

## 3. 依赖与脚本检查

- [x] 仅声明 `python3` 作为运行依赖
- [x] 脚本为明文、可审计、本地执行
- [x] 脚本参数通过 CLI 显式传入
- [x] 无未声明环境变量依赖
- [x] 无未声明安装动作

## 4. 资源检查

- [x] 资源文件存在且为真实内容
- [x] 资源用途与 skill 目标一致
- [x] 资源已在说明中被引用

## 5. 安全检查

- [x] 未发现 `curl|bash`
- [x] 未发现远程下载后直接执行
- [x] 未发现 base64/混淆载荷执行
- [x] 未发现越权监控、盗号、破解、恶意抓取设计
- [x] 文件读写范围应由用户明确指定

## 6. 热门度与实用性复核

- 高频需求：是
- 低理解门槛：是
- 易传播：是
- 可二次定制：是
- 维护成本：低到中

## 7. 评分

- 规范完整度：9.5/10
- 可用性：9.0/10
- 安全性：9.5/10
- 可维护性：9.0/10
- 综合评分：9.3/10

## 8. 结论

该 skill 已补齐交付级目录结构，适合纳入统一 bundle 分发。后续若要继续增强，优先方向是增加更贴近真实场景的样例输入与回归测试数据。
