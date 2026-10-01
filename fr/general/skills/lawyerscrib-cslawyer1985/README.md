# LawyerScrib

技能（Claude Code / Cursor），用于消除法语法律文本中的 AI 写作痕迹，实现自然、专业的语气。

## 安装

### 推荐（克隆到技能目录）

**Claude Code：**
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/VOTRE_ORG/Lawyer-scrib.git ~/.claude/skills/lawyerscrib
# 或，如果您已克隆该项目：cp /chemin/vers/Lawyer-scrib/SKILL.md ~/.claude/skills/lawyerscrib/
```

**Cursor：**
```bash
mkdir -p ~/.cursor/skills
git clone https://github.com/VOTRE_ORG/Lawyer-scrib.git ~/.cursor/skills/lawyerscrib
# 或：cp /chemin/vers/Lawyer-scrib/SKILL.md ~/.cursor/skills/lawyerscrib/
```

### 手动安装（仅技能文件）

如果仓库已克隆（或您只有 `SKILL.md`），复制该技能：

```bash
# Claude Code
mkdir -p ~/.claude/skills/lawyerscrib
cp SKILL.md ~/.claude/skills/lawyerscrib/

# Cursor
mkdir -p ~/.cursor/skills/lawyerscrib
cp SKILL.md ~/.cursor/skills/lawyerscrib/
```

## 使用

在 Claude Code 或 Cursor 中调用该技能：

```
/lawyerscrib

[在此粘贴您的文本]
```

或直接要求：

```
Humanise / révisé ce texte juridique : [votre texte]
（将这段法律文本人性化 / 修订：[您的文本]）
```

## 概览

该技能基于与 [Humanizer](https://github.com/blader/humanizer)（维基百科《AI 写作的标志》）相同的原理，并适用于法语法律写作：法律意见书、咨询意见、备忘录、邮件和法律文书。

它包含一道**"反 AI"收尾工序**：识别仍暴露 AI 痕迹之处，然后改写出一版最终文本。

### 核心理念

> 经过法律文本训练的 LLM 会再现*形式上的习癖*（拉丁文引用、客套用语、分章结构），却没有执业律师的*论证实质*。目标不是中性文本，而是**有立场且精准**的文本。

## 检测到的 17 种模式（摘要）

### 内容

| # | 模式 | 之前（典型 AI） | 之后 |
|---|--------|---------------------|--------|
| 1 | **范围膨胀** | "s'inscrit dans le cadre plus large de..."（属于……的更广泛框架） | 事实陈述 + 真实范围 |
| 2 | **模糊归因** | "La doctrine majoritaire s'accorde..."（主流学说一致认为……） | 精确引用（作者、著作、编号） |
| 3 | **修辞赘语** | "Il convient de noter... Force est de constater..."（应当指出……不得不承认……） | 直接表达或删除 |
| 4 | **回避"être"动词** | "revêt un caractère... se traduit par..."（具有……性质、体现为……） | "est..."（是……）、"constitue..."（构成……） |
| 5 | **过度被动化** | "Il a été soutenu par la demanderesse que..."（原告曾主张……） | "La demanderesse soutient que..."（原告主张……） |
| 6 | **滥用名词化** | "La mise en œuvre de la procédure de résiliation..."（解除程序的实施……） | "Pour résilier le bail..."（为解除租赁合同……） |
| 7 | **三法则** | "pour trois raisons : d'abord... ensuite... enfin..."（出于三个原因：首先……其次……最后……） | 自然数量的论点 |
| 8 | **"问题与展望"章节** | "Des défis persistent. La solution pourrait évoluer."（挑战仍然存在。解决方案可能会演变。） | 具体结论或删除 |

### 语言

| # | 模式 | 之前 | 之后 |
|---|--------|--------|--------|
| 9 | **法律文本上的 AI 词汇** | "problématique fondamentale, enjeux cruciaux"（根本性问题、关键议题） | 精确术语、适用的法律规则 |
| 10 | **AI 客套用语** | "J'espère que ce message vous trouve... N'hésitez pas..."（希望此信送达时您……请随时……） | 简短专业的措辞 |
| 11 | **通用结论** | "La situation est complexe... Il conviendra d'apprécier..."（情况很复杂……应加以评估……） | 明确立场 + 带日期的建议 |
| 12 | **滥用"上述"类用语** | "Ledit contrat... lesdites parties... ladite clause"（上述合同……上述各方……上述条款） | "Le contrat du 3 janvier 2023..."（2023 年 1 月 3 日的合同……） |
| 13 | **否定式排比** | "Il ne s'agit pas seulement de X ; il s'agit de Y"（这不只是 X 的问题；而是 Y 的问题） | 直接陈述 |

### 风格与沟通

| # | 模式 | 之前 | 之后 |
|---|--------|--------|--------|
| 14 | **滥用长破折号（—）** | "La clause est nulle — c'est indiscutable — et ce pour..."（该条款无效——这无可争辩——且……） | 逗号或冒号 |
| 15 | **机械加粗** | **responsabilité contractuelle**（合同责任）、**manquement**（违约） | 不做系统性加粗 |
| 16 | **过度模糊表达** | "Il semblerait que... pourrait potentiellement..."（似乎……可能……） | "Cette position est contestable :..."（这一立场可予质疑：……） |
| 17 | **奉承式开场** | "Excellente question ! Vous avez tout à fait raison..."（好问题！您完全正确……） | "Voici l'analyse."（以下为分析。） |

## 完整示例

**之前（AI 痕迹饱和）：**
> Comme il a été souligné supra, la problématique de la validité de la clause de non-concurrence revêt un caractère fondamental dans le cadre du présent litige. Il convient, à cet égard, de rappeler que la doctrine majoritaire s'accorde à reconnaître que ladite clause doit, pour être valide, répondre à des conditions cumulatives que la jurisprudence a progressivement précisées. Force est de constater que ces conditions ne semblent pas réunies en l'espèce. Il s'agit non seulement d'une question de droit, mais d'une question de justice contractuelle. En conclusion, la situation est complexe et nécessite une analyse approfondie. Je reste à votre entière disposition pour tout complément.
> （如前所述，竞业限制条款的效力问题在本争议中具有根本性。就此应当指出，主流学说一致认为，该条款要有效须满足判例逐渐明确的累积条件。不得不承认，本案中这些条件似乎并未满足。这不仅是一个法律问题，更是一个合同正义问题。总之，情况复杂，需要深入分析。我随时为您提供任何补充。）

**之后（已人性化）：**
> La clause de non-concurrence est nulle faute de contrepartie financière, condition que la chambre sociale exige depuis 2002 (Cass. soc., 10 juill. 2002, n° 00-45.135). La nullité est relative : votre client peut s'en prévaloir ou y renoncer. S'il entend se réinstaller immédiatement, une lettre de renonciation adressée à l'employeur avant la fin du préavis est suffisante.
> （竞业限制条款因缺少经济对价而无效，这是社会庭自 2002 年起要求满足的条件（Cass. soc.，2002 年 7 月 10 日，第 00-45.135 号）。该无效是相对的：您的客户可以主张无效，也可以放弃主张。如果其打算立即重新开业，在预告期届满前向雇主发出放弃函即已足够。）

## 个性化定制

要使技能适配您的法律写作风格（语域、措辞、文件类型）：见**[个性化指南](GUIDE_PERSONNALISATION.md)**，其中详述关键概念并提供规则模板。

## 参考

- [Humanizer](https://github.com/blader/humanizer) —— 源技能（英文，通用用途）
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) —— 模式的基础

## 版本历史

- **1.0.0** —— 初始版本：法语法律人性化工具（17 种模式、律师口吻、反 AI 收尾工序）

## 许可

MIT © LegalFab
