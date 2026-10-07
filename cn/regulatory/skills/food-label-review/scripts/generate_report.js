#!/usr/bin/env node
/**
 * 食品标签合规审核报告 DOCX 生成器
 *
 * 用法: node generate_report.js <input.json> [output.docx]
 *
 * input.json 结构见下方 SCHEMA 注释
 */

/*
SCHEMA:
{
  "basicInfo": {
    "食品名称": "XX牌牛奶",
    "审核日期": "2026-02-11",
    "适用标准": "GB 7718-2025 + GB 28050-2025",
    "标签类别": "直接提供给消费者",
    "营养标签": "需审核"
  },
  "conclusion": "通过 | 需修改后通过 | 不予通过",
  "riskLevel": "高 | 中 | 低",
  "issues": [
    {
      "title": "问题简述",
      "type": "违规类型",
      "risk": "高 | 中 | 低",
      "description": "问题描述",
      "quote": "标签原文摘录",
      "violation": "违反条款",
      "suggestion": "修改建议"
    }
  ],
  "suggestions": "合规建议（可选）",
  "disclaimer": "免责声明（可选，有默认值）"
}
*/

const fs = require("fs");
const { execSync } = require("child_process");

// 自动解析全局 node_modules 路径
try { require.resolve("docx"); } catch {
  try {
    const prefix = execSync("npm config get prefix", { encoding: "utf-8" }).trim();
    const globalPath = require("path").join(prefix, "lib", "node_modules");
    module.paths.unshift(globalPath);
  } catch { /* ignore */ }
}

const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType,
  ShadingType, VerticalAlign, PageNumber, LevelFormat, PageBreak
} = require("docx");

// ── 常量 ──
const FONT = "仿宋";
const FONT_EN = "Times New Roman";
const SIZE_TITLE = 36;      // 小二 18pt
const SIZE_H1 = 30;         // 小三 15pt
const SIZE_H2 = 28;         // 四号 14pt
const SIZE_BODY = 24;       // 小四 12pt
const SIZE_SMALL = 21;      // 五号 10.5pt
const LINE_SPACING = 360;   // 1.5 倍行距
const COLOR_PRIMARY = "1A3C6E";
const COLOR_HEADER_BG = "E8EDF3";
const COLOR_RISK_HIGH = "CC0000";
const COLOR_RISK_MED = "CC7700";
const COLOR_RISK_LOW = "337733";
const DEFAULT_DISCLAIMER = "本审核报告基于所提供的食品标签素材内容进行合规分析，不构成正式法律意见。审核依据为 GB 7718 和 GB 28050 的规定，未涵盖其他食品安全标准或行业标准的要求。建议结合产品实际情况及最新法规要求进行综合判断。";

const thinBorder = { style: BorderStyle.SINGLE, size: 1, color: "BBBBBB" };
const cellBorders = { top: thinBorder, bottom: thinBorder, left: thinBorder, right: thinBorder };
const noBorder = { style: BorderStyle.NONE, size: 0 };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };

// ── 辅助函数 ──
function riskColor(risk) {
  if (risk === "高") return COLOR_RISK_HIGH;
  if (risk === "中") return COLOR_RISK_MED;
  return COLOR_RISK_LOW;
}

function bodyPara(children, options = {}) {
  return new Paragraph({
    spacing: { line: LINE_SPACING, before: options.before || 0, after: options.after || 0 },
    indent: options.indent,
    alignment: options.alignment || AlignmentType.JUSTIFIED,
    children: Array.isArray(children) ? children : [children],
    ...(options.numbering ? { numbering: options.numbering } : {})
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

function makeInfoTable(info) {
  const keys = Object.keys(info);
  return new Table({
    columnWidths: [2200, 7160],
    rows: keys.map(key =>
      new TableRow({
        children: [
          new TableCell({
            borders: cellBorders,
            width: { size: 2200, type: WidthType.DXA },
            shading: { fill: COLOR_HEADER_BG, type: ShadingType.CLEAR },
            verticalAlign: VerticalAlign.CENTER,
            children: [bodyPara(textRun(key, { bold: true }), { alignment: AlignmentType.CENTER })]
          }),
          new TableCell({
            borders: cellBorders,
            width: { size: 7160, type: WidthType.DXA },
            verticalAlign: VerticalAlign.CENTER,
            children: [bodyPara(textRun(info[key]))]
          })
        ]
      })
    )
  });
}

function makeIssueBlock(issue, index) {
  const items = [];
  // 问题标题
  items.push(new Paragraph({
    spacing: { line: LINE_SPACING, before: 200, after: 100 },
    children: [
      textRun(`${index + 1}. ${issue.title}`, { size: SIZE_H2, bold: true }),
    ]
  }));

  const riskTag = issue.risk || "中";
  const fields = [
    ["违规类型", issue.type],
    ["风险等级", riskTag],
    ["问题描述", issue.description],
    ["标签原文", issue.quote ? `"${issue.quote}"` : null],
    ["违反条款", issue.violation],
    ["修改建议", issue.suggestion],
  ];

  for (const [label, value] of fields) {
    if (!value) continue;
    const isRisk = label === "风险等级";
    items.push(bodyPara([
      textRun(`${label}：`, { bold: true }),
      textRun(value, {
        color: isRisk ? riskColor(riskTag) : "000000",
        bold: isRisk,
      }),
    ], { indent: { left: 480 }, before: 40 }));
  }
  return items;
}

// ── 主函数 ──
async function generate(inputPath, outputPath) {
  const data = JSON.parse(fs.readFileSync(inputPath, "utf-8"));
  const children = [];

  // ═══ 标题 ═══
  children.push(new Paragraph({
    spacing: { before: 400, after: 300, line: LINE_SPACING },
    alignment: AlignmentType.CENTER,
    children: [textRun("食品标签合规审核报告", { size: SIZE_TITLE, bold: true, color: COLOR_PRIMARY })]
  }));

  // ═══ 一、基本信息 ═══
  children.push(new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 300, after: 200, line: LINE_SPACING },
    children: [textRun("一、基本信息", { size: SIZE_H1, bold: true, color: COLOR_PRIMARY })]
  }));
  children.push(makeInfoTable(data.basicInfo));

  // ═══ 二、审核结论 ═══
  children.push(new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 300, after: 200, line: LINE_SPACING },
    children: [textRun("二、审核结论", { size: SIZE_H1, bold: true, color: COLOR_PRIMARY })]
  }));

  const conclusionColor = data.conclusion === "通过" ? COLOR_RISK_LOW :
    data.conclusion === "不予通过" ? COLOR_RISK_HIGH : COLOR_RISK_MED;

  children.push(bodyPara([
    textRun("总体结论：", { bold: true }),
    textRun(data.conclusion, { bold: true, color: conclusionColor, size: SIZE_H2 }),
  ], { before: 60 }));
  children.push(bodyPara([
    textRun("风险等级：", { bold: true }),
    textRun(data.riskLevel, { bold: true, color: riskColor(data.riskLevel), size: SIZE_H2 }),
  ], { before: 60 }));

  // ═══ 三、问题清单 ═══
  children.push(new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 300, after: 100, line: LINE_SPACING },
    children: [textRun("三、问题清单", { size: SIZE_H1, bold: true, color: COLOR_PRIMARY })]
  }));

  if (data.issues && data.issues.length > 0) {
    children.push(bodyPara(
      textRun("（按风险等级从高到低排列）", { size: SIZE_SMALL, color: "666666", italics: true }),
      { before: 0, after: 100 }
    ));
    for (let i = 0; i < data.issues.length; i++) {
      children.push(...makeIssueBlock(data.issues[i], i));
    }
  } else {
    children.push(bodyPara(textRun("未发现合规问题。", { color: COLOR_RISK_LOW })));
  }

  // ═══ 四、合规建议 ═══
  if (data.suggestions) {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_1,
      spacing: { before: 300, after: 200, line: LINE_SPACING },
      children: [textRun("四、合规建议", { size: SIZE_H1, bold: true, color: COLOR_PRIMARY })]
    }));
    // 支持多段落（用 \n 分割）
    const paragraphs = data.suggestions.split("\n").filter(s => s.trim());
    for (const p of paragraphs) {
      children.push(bodyPara(textRun(p), { before: 60 }));
    }
  }

  // ═══ 五、免责声明 ═══
  children.push(new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 300, after: 200, line: LINE_SPACING },
    children: [textRun("五、免责声明", { size: SIZE_H1, bold: true, color: COLOR_PRIMARY })]
  }));
  children.push(bodyPara(
    textRun(data.disclaimer || DEFAULT_DISCLAIMER, { size: SIZE_SMALL, color: "666666" }),
    { before: 60 }
  ));

  // ═══ 构建文档 ═══
  const doc = new Document({
    styles: {
      default: {
        document: {
          run: { font: FONT, size: SIZE_BODY }
        }
      },
      paragraphStyles: [
        {
          id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: SIZE_H1, bold: true, color: COLOR_PRIMARY, font: FONT },
          paragraph: { spacing: { before: 300, after: 200 }, outlineLevel: 0 }
        },
        {
          id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: SIZE_H2, bold: true, color: COLOR_PRIMARY, font: FONT },
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
            alignment: AlignmentType.RIGHT,
            children: [textRun("食品标签合规审核报告", { size: SIZE_SMALL, color: "999999" })]
          })]
        })
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              textRun("第 ", { size: SIZE_SMALL, color: "999999" }),
              new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: SIZE_SMALL, color: "999999" }),
              textRun(" 页 / 共 ", { size: SIZE_SMALL, color: "999999" }),
              new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: SIZE_SMALL, color: "999999" }),
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
  console.log(`报告已生成: ${outputPath}`);
}

// ── 入口 ──
const args = process.argv.slice(2);
if (args.length < 1) {
  console.error("用法: node generate_report.js <input.json> [output.docx]");
  process.exit(1);
}
const inputFile = args[0];
const outputFile = args[1] || inputFile.replace(/\.json$/, "") + "_report.docx";

generate(inputFile, outputFile).catch(err => {
  console.error("生成失败:", err.message);
  process.exit(1);
});
