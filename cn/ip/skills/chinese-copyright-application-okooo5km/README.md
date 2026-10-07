# 中国软件著作权申请材料生成 Skill

当前版本：**v1.1.0**

自动分析项目代码，生成符合中国版权保护中心要求的软件著作权申请材料。申请表直接输出 Markdown 提交，其余三份材料生成 LaTeX 后用 XeLaTeX 编译为 PDF。

## 生成的文档

1. **著作权登记申请表**（Markdown） — 完整的申请信息，含企业工商信息；直接以 `.md` 提交，不参与编译
2. **源程序**（PDF） — 前30页 + 后30页，**正好60页**，自然分页
3. **用户手册**（PDF） — 含界面截图占位，不少于10页
4. **设计说明书**（PDF） — §4 详细设计按 6 段结构展开，与源代码模块双向对应，含界面截图占位
5. **build_all.sh** — 一键编译脚本（只编译 3 份 PDF）

## 特点

- 申请表 Markdown 直接提交，规避 PDF 文本提取换行问题
- LaTeX 三份精确控制页眉页脚、段首缩进、分页
- 页眉：软件全称V版本号 + 文档类型；页脚：第 X 页 共 XX 页
- **版本号一致性核验**：扫描项目内所有 version 字符串，与申请表/截图三方比对
- **遗留代码识别**：mockData / util.js 默认模板 / pages/logs 等不进入鉴别材料
- **设计说明书 6 段结构**：模块职责 / 输入输出 / 关键算法 / 状态缓存 / 模块依赖 / 处理流程
- **模块覆盖双向校验**：源代码 ↔ 设计说明书 §4
- 自动校验字数限制（主要功能 500–1000 字）、日期逻辑、信息一致性
- 自动生成截图清单
- 支持微信小程序、Web应用、移动App、桌面应用等

## 前置条件

申请表是 Markdown，**不需要 LaTeX 环境**。
源程序、用户手册、设计说明书三份 PDF 需要安装 XeLaTeX 环境和中文宏包。详见 SKILL.md 中的「LaTeX 环境依赖」章节。

## 文件结构

```
chinese-copyright-application/
├── SKILL.md                              # 主 Skill 文件
├── README.md
├── scripts/
│   └── analyze_and_generate_source.py    # 项目分析 + 源程序 .tex 生成
└── references/
    ├── requirements.md                   # 详细申请要求
    ├── application-form-template.md      # 申请表 Markdown 模板（v1.1 新）
    ├── source-code-template.tex          # 源程序 LaTeX 模板
    ├── user-manual-template.tex          # 用户手册 LaTeX 模板
    ├── design-doc-template.tex           # 设计说明书 LaTeX 模板（v1.1 §4 改 6 段结构）
    └── build-script-template.sh          # 编译脚本模板
```

## Changelog

### v1.1.0（2026-05-06）

> 来源：集享软件 V1.0 软著流水号 2026R11L0626727 补正经验。

- 申请表载体：LaTeX→PDF 改为 Markdown（PDF 文本提取带换行造成的录入问题）
- 主要功能字数：200 字 → **500–1000 字**（建议 500–600，官方要求调整）
- 新增**版本号一致性核验**：信息收集阶段就要查项目里的 version 字符串与目标版本号是否一致；常见踩坑：config.js 写 1.1.1 但申请表填 V1.0
- 新增**遗留代码识别**（`legacy_candidates`）：mockData / util.js 模板 / logs 等，工具列出，由 Claude+用户确认后通过 `--exclude-pattern` 排除
- 设计说明书 §4 详细设计：旧版「模块功能 + 处理流程」两段 → **6 段结构**（职责 / 输入输出 / 关键算法 / 状态管理 / 模块依赖 / 处理流程）
- 新增**模块覆盖双向校验**：源代码 ↔ 设计说明书 §4，每个出现在源代码鉴别材料中的模块都必须在 §4 有对应小节，反之亦然
- 新增 `--front-lines` / `--back-lines` 参数：方便编译后微调到正好 60 页
- 一致性校验首项改为版本号一致性
- README、SKILL.md 同步描述变更

### v1.0.0

- 初版四份材料 LaTeX 模板 + 编译脚本
