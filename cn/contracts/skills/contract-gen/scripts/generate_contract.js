#!/usr/bin/env node
/**
 * 合同 DOCX 生成器
 *
 * 用法: node generate_contract.js <input.json> [output.docx]
 *
 * input.json 结构见下方 SCHEMA 注释
 */

/*
SCHEMA:
{
  "title": "合同标题",
  "type": "合同类型",
  "parties": {
    "甲方": "甲方名称",
    "乙方": "乙方名称"
  },
  "content": "完整的 Markdown 合同正文",
  "date": "生成日期"
}
*/

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

// 自动解析全局 node_modules 路径
try { require.resolve("docx"); } catch {
  try {
    const prefix = execSync("npm config get prefix", { encoding: "utf-8" }).trim();
    const globalPath = path.join(prefix, "lib", "node_modules");
    module.paths.unshift(globalPath);
  } catch { /* ignore */ }
}

let docx;
try {
  docx = require("docx");
} catch {
  console.error("错误: 未找到 docx 依赖。请运行以下命令安装：");
  console.error("  npm install -g docx");
  console.error("  或在项目目录中: npm install docx");
  process.exit(1);
}

const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType,
  ShadingType, VerticalAlign, PageNumber
} = docx;

// ── 常量 ──
const FONT = "仿宋";
const FONT_EN = "Times New Roman";
const SIZE_TITLE = 36;      // 小二 18pt
const SIZE_H1 = 30;         // 小三 15pt
const SIZE_H2 = 28;         // 四号 14pt
const SIZE_BODY = 24;       // 小四 12pt
const SIZE_SMALL = 21;      // 五号 10.5pt
const LINE_SPACING = 360;   // 1.5 倍行距
const COLOR_PRIMARY = "000000";
const COLOR_HEADER_BG = "E8EDF3";

const thinBorder = { style: BorderStyle.SINGLE, size: 1, color: "BBBBBB" };
const cellBorders = { top: thinBorder, bottom: thinBorder, left: thinBorder, right: thinBorder };

// ── 辅助函数 ──
function bodyPara(children, options = {}) {
  return new Paragraph({
    spacing: { line: LINE_SPACING, before: options.before || 0, after: options.after || 0 },
    indent: options.indent,
    alignment: options.alignment || AlignmentType.JUSTIFIED,
    children: Array.isArray(children) ? children : [children],
  });
}

function textRun(text, options = {}) {
  return new TextRun({
    text,
    font: { name: FONT, eastAsia: FONT, ascii: FONT_EN, hAnsi: FONT_EN },
    size: options.size || SIZE_BODY,
    bold: options.bold || false,
    color: options.color || "000000",
    italics: options.italics || false,
  });
}

// ── 输入校验 ──
function validateInput(data) {
  const errors = [];
  if (!data.content || typeof data.content !== "string" || data.content.trim() === "") {
    errors.push("content 字段必须为非空字符串");
  }
  if (!data.title || typeof data.title !== "string") {
    errors.push("title 字段必须为非空字符串");
  }
  if (data.parties && typeof data.parties !== "object") {
    errors.push("parties 字段必须为对象");
  }
  if (errors.length > 0) {
    console.error("输入校验失败：");
    errors.forEach(e => console.error(`  - ${e}`));
    process.exit(1);
  }
}

// ── Markdown 表格解析 ──
function parseMarkdownTable(lines, startIndex) {
  const rows = [];
  let i = startIndex;

  while (i < lines.length && lines[i].trim().startsWith("|")) {
    const line = lines[i].trim();
    // 跳过分隔行 (|---|---|)
    if (/^\|[\s\-:|]+\|$/.test(line)) {
      i++;
      continue;
    }
    const cells = line
      .split("|")
      .filter((_, idx, arr) => idx > 0 && idx < arr.length - 1)
      .map(c => c.trim());
    rows.push(cells);
    i++;
  }

  if (rows.length === 0) return { table: null, endIndex: startIndex };

  const isFirstRowHeader = rows.length > 1;
  const colCount = Math.max(...rows.map(r => r.length));
  // 均分列宽（总宽 9360 DXA ≈ A4 内容区域）
  const colWidth = Math.floor(9360 / colCount);

  const tableRows = rows.map((row, rowIdx) => {
    const isHeader = isFirstRowHeader && rowIdx === 0;
    const tableCells = [];
    for (let c = 0; c < colCount; c++) {
      const cellText = row[c] || "";
      tableCells.push(
        new TableCell({
          borders: cellBorders,
          width: { size: colWidth, type: WidthType.DXA },
          shading: isHeader ? { fill: COLOR_HEADER_BG, type: ShadingType.CLEAR } : undefined,
          verticalAlign: VerticalAlign.CENTER,
          children: [bodyPara(
            parseInlineFormatting(cellText),
            { alignment: isHeader ? AlignmentType.CENTER : AlignmentType.LEFT }
          )],
        })
      );
    }
    return new TableRow({ children: tableCells });
  });

  return {
    table: new Table({ columnWidths: Array(colCount).fill(colWidth), rows: tableRows }),
    endIndex: i,
  };
}

// ── 解析行内格式（加粗、占位符） ──
function parseInlineFormatting(text) {
  const runs = [];
  const regex = /(\*\*(.+?)\*\*)|(\[____\])/g;
  let lastIndex = 0;
  let match;

  while ((match = regex.exec(text)) !== null) {
    if (match.index > lastIndex) {
      runs.push(textRun(text.slice(lastIndex, match.index)));
    }
    if (match[1]) {
      runs.push(textRun(match[2], { bold: true }));
    } else if (match[3]) {
      runs.push(textRun("________", { color: "999999" }));
    }
    lastIndex = match.index + match[0].length;
  }

  if (lastIndex < text.length) {
    runs.push(textRun(text.slice(lastIndex)));
  }

  return runs.length > 0 ? runs : [textRun(text)];
}

// ── 计算列表缩进层级 ──
function getIndentLevel(line) {
  const leadingSpaces = line.match(/^(\s*)/)[1].length;
  // 每 2-4 个空格算一级缩进
  return Math.floor(leadingSpaces / 2);
}

// ── Markdown 解析 ──
function parseMarkdown(content) {
  const lines = content.split("\n");
  const paragraphs = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // 空行
    if (line.trim() === "") continue;

    // 分隔线
    if (/^---+$/.test(line.trim())) continue;

    // 表格（以 | 开头的行）
    if (line.trim().startsWith("|")) {
      const { table, endIndex } = parseMarkdownTable(lines, i);
      if (table) {
        paragraphs.push(table);
        i = endIndex - 1; // -1 因为 for 循环会 i++
        continue;
      }
    }

    // 一级标题 → 合同标题（居中、加粗）
    if (/^# [^#]/.test(line)) {
      const text = line.replace(/^# /, "").trim();
      paragraphs.push(new Paragraph({
        spacing: { before: 400, after: 300, line: LINE_SPACING },
        alignment: AlignmentType.CENTER,
        children: [textRun(text, { size: SIZE_TITLE, bold: true })],
      }));
      continue;
    }

    // 二级标题 → 章节标题
    if (/^## [^#]/.test(line)) {
      const text = line.replace(/^## /, "").trim();
      paragraphs.push(new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 300, after: 200, line: LINE_SPACING },
        children: [textRun(text, { size: SIZE_H1, bold: true })],
      }));
      continue;
    }

    // 三级标题
    if (/^### [^#]/.test(line)) {
      const text = line.replace(/^### /, "").trim();
      paragraphs.push(new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 200, after: 100, line: LINE_SPACING },
        children: [textRun(text, { size: SIZE_H2, bold: true })],
      }));
      continue;
    }

    // 四级标题
    if (/^#### [^#]/.test(line)) {
      const text = line.replace(/^#### /, "").trim();
      paragraphs.push(bodyPara(
        [textRun(text, { bold: true })],
        { before: 160, after: 80 }
      ));
      continue;
    }

    // 有序列表项（支持嵌套）
    if (/^\s*\d+[.)]\s/.test(line)) {
      const indentLevel = getIndentLevel(line);
      const text = line.trim();
      paragraphs.push(bodyPara(parseInlineFormatting(text), {
        indent: { left: 480 + indentLevel * 360 },
        before: 60,
      }));
      continue;
    }

    // 无序列表项（支持嵌套）
    if (/^\s*[-*]\s/.test(line)) {
      const indentLevel = getIndentLevel(line);
      const text = line.trim().replace(/^[-*]\s/, "");
      paragraphs.push(bodyPara(parseInlineFormatting(text), {
        indent: { left: 480 + indentLevel * 360 },
        before: 60,
      }));
      continue;
    }

    // 普通段落
    paragraphs.push(bodyPara(parseInlineFormatting(line.trim()), { before: 60 }));
  }

  return paragraphs;
}

// ── 检测签字盖章区域 ──
function hasSignatureSection(content) {
  // 检测独立的签字盖章区域标题或格式化的签字盖章结构
  // 而非合同条文中偶然提及"签字""盖章"
  const signaturePatterns = [
    /^#{1,3}\s*.*签字.*盖章/m,           // ## 签字盖章
    /^#{1,3}\s*.*签章/m,                 // ## 签章部分
    /（签字[/／]?盖章）/,                 // （签字/盖章）
    /签字[（(]盖章[）)]/,                 // 签字(盖章)
    /（以下无正文）/,                     // （以下无正文）
    /甲方[：:]\s*$/m,                    // 独立行的 "甲方："
    /乙方[：:]\s*$/m,                    // 独立行的 "乙方："
  ];
  return signaturePatterns.some(p => p.test(content));
}

// ── 生成签字盖章区域 ──
function makeSignatureBlock(parties) {
  const blocks = [];
  const partyNames = Object.keys(parties);

  blocks.push(new Paragraph({
    spacing: { before: 600, after: 200, line: LINE_SPACING },
    children: [textRun("（以下无正文）", { size: SIZE_BODY, color: "666666" })],
    alignment: AlignmentType.CENTER,
  }));

  for (const role of partyNames) {
    blocks.push(new Paragraph({ spacing: { before: 400, line: LINE_SPACING }, children: [] }));

    blocks.push(bodyPara([
      textRun(`${role}（签字/盖章）：`, { bold: true }),
    ], { before: 200 }));

    blocks.push(bodyPara([textRun("")], { before: 200 }));

    blocks.push(bodyPara([
      textRun("法定代表人/授权代表：", { bold: true }),
    ], { before: 100 }));

    blocks.push(bodyPara([textRun("")], { before: 200 }));

    blocks.push(bodyPara([
      textRun("日期：    年    月    日", { bold: true }),
    ], { before: 100 }));
  }

  return blocks;
}

// ── 主函数 ──
async function generate(inputPath, outputPath) {
  const raw = fs.readFileSync(inputPath, "utf-8");
  let data;
  try {
    data = JSON.parse(raw);
  } catch (e) {
    console.error("错误: 输入文件不是有效的 JSON 格式。");
    console.error(`  解析错误: ${e.message}`);
    process.exit(1);
  }

  validateInput(data);

  const children = [];

  // 解析 Markdown 内容
  const contentParagraphs = parseMarkdown(data.content);
  children.push(...contentParagraphs);

  // 如果内容中没有独立的签字盖章区域，自动添加
  if (!hasSignatureSection(data.content) && data.parties && Object.keys(data.parties).length > 0) {
    children.push(...makeSignatureBlock(data.parties));
  }

  // 免责声明
  children.push(new Paragraph({ spacing: { before: 400, line: LINE_SPACING }, children: [] }));
  children.push(bodyPara(
    textRun("免责声明：本合同由 AI 辅助生成，仅供参考，不构成正式法律意见。建议在签署前由专业律师审核。具体条款应根据实际情况和当地法律法规进行调整。", {
      size: SIZE_SMALL,
      color: "999999",
      italics: true,
    }),
    { before: 200 }
  ));

  // 构建文档
  const doc = new Document({
    styles: {
      default: {
        document: {
          run: { font: { name: FONT }, size: SIZE_BODY }
        }
      },
      paragraphStyles: [
        {
          id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: SIZE_H1, bold: true, color: COLOR_PRIMARY, font: { name: FONT } },
          paragraph: { spacing: { before: 300, after: 200 }, outlineLevel: 0 }
        },
        {
          id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: SIZE_H2, bold: true, color: COLOR_PRIMARY, font: { name: FONT } },
          paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 1 }
        }
      ]
    },
    sections: [{
      properties: {
        page: {
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
        }
      },
      headers: {
        default: new Header({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [textRun(data.title || "合同", { size: SIZE_SMALL, color: "999999" })]
          })]
        })
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              textRun("第 ", { size: SIZE_SMALL, color: "999999" }),
              new TextRun({ children: [PageNumber.CURRENT], font: { name: FONT }, size: SIZE_SMALL, color: "999999" }),
              textRun(" 页 / 共 ", { size: SIZE_SMALL, color: "999999" }),
              new TextRun({ children: [PageNumber.TOTAL_PAGES], font: { name: FONT }, size: SIZE_SMALL, color: "999999" }),
              textRun(" 页", { size: SIZE_SMALL, color: "999999" }),
            ]
          })]
        })
      },
      children
    }]
  });

  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync(outputPath, buffer);
  console.log(`合同文档已生成: ${outputPath}`);
}

// ── 入口 ──
const args = process.argv.slice(2);
if (args.length < 1) {
  console.error("用法: node generate_contract.js <input.json> [output.docx]");
  process.exit(1);
}
const inputFile = args[0];
const outputFile = args[1] || inputFile.replace(/\.json$/, "") + ".docx";

generate(inputFile, outputFile).catch(err => {
  console.error("生成失败:", err.message);
  process.exit(1);
});
