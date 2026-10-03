# 调用 docx 外部 skill 的典型模式

本文件列示 `ecm-draft-format-adjust` 执行 Word 操作时，调用 `docx` 外部 skill 的标准模式。

---

## 一、前置说明

本 skill 依赖外部 `docx` skill（由 Anthropic 官方或 `anthropic-skills:docx` 提供）。调用方式分两种：

1. **通过 Claude 的工具链**：用户若已安装 `docx` skill，本 skill 的指令会被 docx skill 自动执行
2. **通过 Python 代码脚本**：本 skill 的 `scripts/` 下可放直接使用 `python-docx` 的脚本（当前仅示例，不在 skill 打包中）

---

## 二、典型调用模式

### 2.1 Markdown → Word 初步转换

推荐流程：

```
# 伪代码（由 Claude 在运行时组装）

# Step 1: 把 Markdown 转为 Word（基础版本）
调用 docx skill: "读取这份 Markdown {路径}，转为 Word 文档 {输出路径}，
                    按标准样式表（Heading 1/2/3、Normal）应用样式"

# Step 2: 应用章节编号（自动编号样式）
调用 docx skill: "在 Word {路径} 中，把所有 Heading 1 样式绑定到列表样式 '章节编号'，
                    从'第一部分'开始自动编号"

# Step 3: 插入 TOC
调用 docx skill: "在 Word {路径} 的封面页后插入目录，深度 2 级，
                    使用 TOC 域代码"

# Step 4: 页眉页脚
调用 docx skill: "为 Word {路径} 设置页眉页脚：
                    - 奇偶页不同
                    - 奇数页页眉右对齐 '律师工作报告'
                    - 偶数页页眉左对齐 '{律所全称}'
                    - 页脚中央 '第 X 页，共 Y 页'
                    - 封面和目录不显示页码
                    - 从引言起算页码，阿拉伯数字"

# Step 5: 表格样式
调用 docx skill: "为 Word {路径} 中所有表格应用样式：
                    - 外框 0.5 磅
                    - 内框 0.25 磅
                    - 表头加粗 + 浅灰底（#F2F2F2）
                    - 跨页自动重复表头"

# Step 6: 刷新 TOC 和交叉引用
调用 docx skill: "更新 Word {路径} 的所有域（TOC、REF、PAGE）"
```

### 2.2 样式注入（律所自定义模板）

若用户提供律所 `.dotx` 模板：

```
调用 docx skill: "把 {本地 Markdown} 的内容应用到 {律所.dotx} 的样式表上，
                    生成 Word 文档 {输出路径}。
                    样式映射：
                    - Markdown `#` → Word 样式 '章标题'（律所定义）
                    - Markdown `##` → Word 样式 '一级小节'（律所定义）
                    - Markdown 正文 → Word 样式 '正文'（律所定义）
                    未在律所 .dotx 中定义的样式，回退到标准 work-report-format.md 规范。"
```

### 2.3 交叉引用处理

Markdown 中的 `{{XREF: 第N部分.小节M}}` 占位符：

```
# 扫描 Markdown 文本，识别所有 {{XREF: ...}} 占位符
patterns = find_all(r'\{\{XREF:\s*(.+?)\}\}', markdown_text)

# 对每个占位符，在 Word 中找到对应标题，插入 REF 域代码
for pattern, target in patterns:
    调用 docx skill: "在 Word {路径} 中，
                        找到文本 '{pattern}'，
                        替换为指向标题 '{target}' 的 REF 域代码，
                        域开关 '\\h \\w'（超链接 + 保留编号与段落序号）"
```

### 2.4 签字页

```
调用 docx skill: "在 Word {路径} 末尾（最后一页）插入签字盖章页：
                    1. 独立分页
                    2. 律所全称（居中，三号宋体加粗，段前 36 磅）
                    3. '（盖章）：' 右侧留 4cm 空白（盖章位）
                    4. 空白 4 行
                    5. '{律所负责人姓名}（签字）：' + 下划线（签字栏）
                    6. 空白 2 行
                    7. '经办律师（签字）：'
                    8. 缩进 4 字符 + '{律师 A 姓名}：' + 下划线
                    9. 缩进 4 字符 + '{律师 B 姓名}：' + 下划线
                    10. 空白 2 行
                    11. '{YYYY 年 MM 月 DD 日}'（左对齐，小四宋体）
                    所有签字栏的下划线长度一致（7cm）"
```

### 2.5 跨页处理

```
# 封面页后的分页符
调用 docx skill: "在 Word {路径} 的封面最末段落后插入分页符（Page Break）"

# 附件起始页的分节符（便于页码重置）
调用 docx skill: "在 Word {路径} 的正文末 → 附件一起始之间，
                    插入分节符（下一页，Section Break - Next Page），
                    附件一所在 section 的页码重新从 1 开始，格式 '附件 X 第 Y 页'"
```

---

## 三、python-docx 直接操作（兜底）

对于 docx skill 不支持或支持不完善的特殊操作，本 skill 可以直接用 python-docx 写脚本。以下是示例模板（**仅供参考，不在本仓库的 scripts/ 中打包；运行时由 Claude 即时生成**）：

### 3.1 应用段落字体

```python
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn

doc = Document("input.docx")
for paragraph in doc.paragraphs:
    if paragraph.style.name == "Normal":
        for run in paragraph.runs:
            run.font.size = Pt(10.5)  # 小四
            run.font.name = "宋体"
            # 中文字体需额外设置
            run._element.rPr.rFonts.set(qn("w:eastAsia"), "宋体")
doc.save("output.docx")
```

### 3.2 设置页边距

```python
from docx.shared import Cm

for section in doc.sections:
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)
```

### 3.3 设置奇偶页不同的页眉

```python
section = doc.sections[0]
section.different_first_page_header_footer = True
section.different_odd_and_even_pages_header_footer = True

odd_header = section.header
even_header = section.even_page_header

odd_header.paragraphs[0].text = "律师工作报告"
odd_header.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT

even_header.paragraphs[0].text = "某某律师事务所"
even_header.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
```

### 3.4 插入 TOC 域代码

python-docx 对 TOC 支持有限；推荐用 XML 直接插入：

```python
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# 在指定位置插入 TOC 域
toc_para = doc.add_paragraph()
run = toc_para.add_run()

fldChar_begin = OxmlElement("w:fldChar")
fldChar_begin.set(qn("w:fldCharType"), "begin")

instrText = OxmlElement("w:instrText")
instrText.set(qn("xml:space"), "preserve")
instrText.text = 'TOC \\o "1-2" \\h \\z \\u'

fldChar_separate = OxmlElement("w:fldChar")
fldChar_separate.set(qn("w:fldCharType"), "separate")

fldChar_end = OxmlElement("w:fldChar")
fldChar_end.set(qn("w:fldCharType"), "end")

run._element.append(fldChar_begin)
run._element.append(instrText)
run._element.append(fldChar_separate)
run._element.append(fldChar_end)
```

打开文档后 Word 会提示"更新域"，用户按 F9 刷新即可。

### 3.5 设置标题自动编号

```python
# 律师工作报告的"第一部分、第二部分、……"自动编号
# 通过 numbering.xml 定义多级列表，然后 Heading 1 样式绑定到该列表

# python-docx 对此支持较弱，推荐直接修改 numbering.xml
# 或用 docx-template 工具（Jinja2 + docx）
```

---

## 四、工具链选择

在实际运行时，本 skill 按以下优先级选择工具：

1. **docx skill（Anthropic 官方）** —— 首选。大多数标准操作（Heading、段落属性、表格、页眉页脚、TOC、REF 域）都支持
2. **pandoc + reference.docx** —— 用于复杂的 Markdown → Word 转换（docx skill 处理不动的情况）
3. **python-docx 直接脚本** —— 用于高度自定义的 XML 级别操作（如复杂的域代码、多级列表定义）

本 skill 在 Step 3 做"规范化转换"时，按元素类型选择工具：

| 元素 | 首选工具 |
|------|--------|
| Heading / Normal 样式 | docx skill |
| 段落属性（字体 / 字号 / 行距） | docx skill |
| 表格 | docx skill |
| 页眉页脚 | docx skill |
| TOC | docx skill（支持插入）+ python-docx（支持细调） |
| 交叉引用 REF 域 | python-docx（支持更精细） |
| 自动编号绑定 | python-docx（需修改 numbering.xml） |
| 律所 `.dotx` 样式注入 | pandoc --reference-doc 或 docx-template |

---

## 五、错误处理

docx skill 调用失败时的回退：

1. 记录失败的具体操作（哪一步 / 哪个元素）
2. 尝试用 python-docx 替代（若本 skill 内置了对应脚本）
3. 若 python-docx 也失败，在格式检查清单中列明"未处理项"，提示用户手工调整
4. 不得静默失败 —— 所有失败必须在清单中可见

---

## 六、性能考虑

- 大文档（>100 页）：分阶段处理，每个 section 独立操作，避免单次调用处理全文档
- 大量表格（>50 张）：批量应用样式而非逐张设置
- TOC 刷新：仅在所有内容和样式都设置完后执行一次（避免多次刷新）

---

## 七、与 ecm-qc 模块的交互

QC skill 的输出是带 tracked changes 的 Word（`w:author="内核"`）。本 skill **不处理**带 tracked changes 的 Word：

- 本 skill 的输入假设是"干净"的 Markdown / Word（无修订痕迹）
- 若用户把带 tracked changes 的 Word 交给本 skill，会警告"本 skill 不处理修订痕迹文档；请先接受 / 拒绝修订后再套版"

QC 的修订痕迹应在**已套版**的 Word 上做（即 qc skill 的输入是本 skill 的输出），这样修订痕迹直接显示在已排版的文档上，方便内核看排版效果。
