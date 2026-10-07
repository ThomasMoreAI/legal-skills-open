#!/usr/bin/env node
/**
 * generate_docx_memo.js — Produces the formal client-ready DOCX deliverable.
 *
 * Usage:
 *   node generate_docx_memo.js --input memo.json --output deliverable.docx
 *
 * Input JSON shape:
 *   {
 *     "client_name": "string",
 *     "memo_date": "Month Day, AD YYYY",
 *     "prepared_by": "string",
 *     "executive_summary": "string (multi-paragraph; '\\n\\n' separates paragraphs)",
 *     "entity_profile": [{"label": "...", "value": "...", "source": "..."}],
 *     "applicability": [{"state": "CA", "statute": "...", "verdict": "...", "reasoning": "..."}],
 *     "status_determination": [{"data_flow": "...", "ca_status": "...", "other_states_status": "...", "notes": "..."}],
 *     "gaps": [{"id": "01", "states": "CA, CO", "section": "...", "gap": "...", "current": "...", "required": "...", "severity": 4, "likelihood": 4, "score": 16, "lane": "0-30 day", "dependencies": "..."}],
 *     "remediation": {
 *       "immediate": ["..."],
 *       "thirty_day": ["..."],
 *       "ninety_day": ["..."],
 *       "strategic": ["..."]
 *     },
 *     "cross_cutting": ["..."],
 *     "limitations": ["..."],
 *     "next_steps": ["..."]
 *   }
 *
 * Conforms to the docx skill conventions (US Letter 12240×15840 DXA; dual-width
 * tables; LevelFormat.BULLET; ShadingType.CLEAR; Arial 12pt default).
 *
 * Part of the us-state-privacy-navigator skill.
 */

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, PageOrientation, LevelFormat,
  TableOfContents, HeadingLevel, BorderStyle, WidthType, ShadingType,
  PageNumber, PageBreak, ExternalHyperlink,
} = require('docx');

// ---------------------------------------------------------------------------
// Argument parsing
// ---------------------------------------------------------------------------

function parseArgs() {
  const args = process.argv.slice(2);
  const out = { input: null, output: null };
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--input' && args[i + 1]) { out.input = args[i + 1]; i++; }
    else if (args[i] === '--output' && args[i + 1]) { out.output = args[i + 1]; i++; }
  }
  if (!out.input || !out.output) {
    console.error('Usage: node generate_docx_memo.js --input memo.json --output deliverable.docx');
    process.exit(1);
  }
  return out;
}

// ---------------------------------------------------------------------------
// Style helpers
// ---------------------------------------------------------------------------

const BORDER = { style: BorderStyle.SINGLE, size: 4, color: '999999' };
const ALL_BORDERS = { top: BORDER, bottom: BORDER, left: BORDER, right: BORDER };
const CELL_MARGINS = { top: 80, bottom: 80, left: 120, right: 120 };

function p(text, options = {}) {
  if (text === null || text === undefined || text === '') {
    return new Paragraph({ children: [new TextRun('')] });
  }
  return new Paragraph({
    children: [new TextRun({ text: String(text), bold: !!options.bold, italics: !!options.italics })],
    spacing: { after: 120 },
    ...options.paragraphProps,
  });
}

function bullet(text, ref = 'bullets') {
  return new Paragraph({
    numbering: { reference: ref, level: 0 },
    children: [new TextRun(String(text || ''))],
  });
}

function heading(text, level) {
  const map = {
    1: HeadingLevel.HEADING_1,
    2: HeadingLevel.HEADING_2,
    3: HeadingLevel.HEADING_3,
  };
  return new Paragraph({ heading: map[level] || HeadingLevel.HEADING_2, children: [new TextRun(String(text))] });
}

function cell(text, opts = {}) {
  const widthDXA = opts.width || 1872; // default fifth of 9360
  const shading = opts.shading ? { fill: opts.shading, type: ShadingType.CLEAR } : undefined;
  const children = Array.isArray(text)
    ? text.map(t => p(t))
    : [p(text || '', { bold: opts.headerCell })];
  return new TableCell({
    borders: ALL_BORDERS,
    width: { size: widthDXA, type: WidthType.DXA },
    shading,
    margins: CELL_MARGINS,
    children,
  });
}

function table(rows, columnWidths) {
  const totalWidth = columnWidths.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: totalWidth, type: WidthType.DXA },
    columnWidths,
    rows,
  });
}

// ---------------------------------------------------------------------------
// Content composition
// ---------------------------------------------------------------------------

function buildEntityProfileTable(profile) {
  if (!profile || !profile.length) return null;
  const cw = [3120, 3120, 3120]; // sums to 9360
  const headerRow = new TableRow({
    children: [
      cell('Input', { headerCell: true, shading: 'D5E8F0', width: cw[0] }),
      cell('Value', { headerCell: true, shading: 'D5E8F0', width: cw[1] }),
      cell('Source / Assumption', { headerCell: true, shading: 'D5E8F0', width: cw[2] }),
    ],
  });
  const rows = [headerRow].concat(profile.map(item => new TableRow({
    children: [
      cell(item.label || '', { width: cw[0] }),
      cell(item.value || '', { width: cw[1] }),
      cell(item.source || '', { width: cw[2] }),
    ],
  })));
  return table(rows, cw);
}

function buildApplicabilityTable(rows) {
  if (!rows || !rows.length) return null;
  const cw = [780, 2580, 1500, 4500]; // 9360
  const headerRow = new TableRow({
    children: [
      cell('State', { headerCell: true, shading: 'D5E8F0', width: cw[0] }),
      cell('Statute', { headerCell: true, shading: 'D5E8F0', width: cw[1] }),
      cell('Verdict', { headerCell: true, shading: 'D5E8F0', width: cw[2] }),
      cell('Reasoning', { headerCell: true, shading: 'D5E8F0', width: cw[3] }),
    ],
  });
  const verdictColor = (v) => {
    if (!v) return undefined;
    const s = v.toLowerCase();
    if (s.includes('applies') && !s.includes('not') && !s.includes('insufficient')) return 'F8D7DA';
    if (s.includes('likely')) return 'FFF3CD';
    if (s.includes('does not')) return 'D4EDDA';
    return undefined;
  };
  const data = rows.map(r => new TableRow({
    children: [
      cell(r.state || '', { width: cw[0] }),
      cell(r.statute || '', { width: cw[1] }),
      cell(r.verdict || '', { width: cw[2], shading: verdictColor(r.verdict) }),
      cell(r.reasoning || '', { width: cw[3] }),
    ],
  }));
  return table([headerRow].concat(data), cw);
}

function buildStatusTable(rows) {
  if (!rows || !rows.length) return null;
  const cw = [2340, 2340, 2340, 2340]; // 9360
  const header = new TableRow({
    children: [
      cell('Data flow', { headerCell: true, shading: 'D5E8F0', width: cw[0] }),
      cell('CA status', { headerCell: true, shading: 'D5E8F0', width: cw[1] }),
      cell("Other states' status", { headerCell: true, shading: 'D5E8F0', width: cw[2] }),
      cell('Notes', { headerCell: true, shading: 'D5E8F0', width: cw[3] }),
    ],
  });
  const data = rows.map(r => new TableRow({
    children: [
      cell(r.data_flow || '', { width: cw[0] }),
      cell(r.ca_status || '', { width: cw[1] }),
      cell(r.other_states_status || '', { width: cw[2] }),
      cell(r.notes || '', { width: cw[3] }),
    ],
  }));
  return table([header].concat(data), cw);
}

function buildGapTable(rows) {
  if (!rows || !rows.length) return null;
  const cw = [600, 1200, 2880, 720, 720, 600, 1080, 1560]; // = 9360
  const header = new TableRow({
    children: [
      cell('ID', { headerCell: true, shading: 'D5E8F0', width: cw[0] }),
      cell('State(s)', { headerCell: true, shading: 'D5E8F0', width: cw[1] }),
      cell('Gap', { headerCell: true, shading: 'D5E8F0', width: cw[2] }),
      cell('Sev', { headerCell: true, shading: 'D5E8F0', width: cw[3] }),
      cell('Lik', { headerCell: true, shading: 'D5E8F0', width: cw[4] }),
      cell('Score', { headerCell: true, shading: 'D5E8F0', width: cw[5] }),
      cell('Lane', { headerCell: true, shading: 'D5E8F0', width: cw[6] }),
      cell('Dependencies', { headerCell: true, shading: 'D5E8F0', width: cw[7] }),
    ],
  });
  const laneColor = (lane) => {
    if (!lane) return undefined;
    const s = lane.toLowerCase();
    if (s.includes('immediate') || s.includes('critical')) return 'F8D7DA';
    if (s.includes('0-30') || s.includes('30 day') || s.includes('high')) return 'FFE5D0';
    if (s.includes('31') || s.includes('90 day') || s.includes('medium')) return 'FFF3CD';
    if (s.includes('strategic') || s.includes('low')) return 'D4EDDA';
    return undefined;
  };
  const data = rows.map(r => new TableRow({
    children: [
      cell(r.id || '', { width: cw[0] }),
      cell(r.states || '', { width: cw[1] }),
      cell([r.gap || '', r.section ? `(${r.section})` : ''].filter(Boolean), { width: cw[2] }),
      cell(String(r.severity ?? ''), { width: cw[3] }),
      cell(String(r.likelihood ?? ''), { width: cw[4] }),
      cell(String(r.score ?? ''), { width: cw[5] }),
      cell(r.lane || '', { width: cw[6], shading: laneColor(r.lane) }),
      cell(r.dependencies || '', { width: cw[7] }),
    ],
  }));
  return table([header].concat(data), cw);
}

// ---------------------------------------------------------------------------
// Document construction
// ---------------------------------------------------------------------------

function buildDoc(memo) {
  const children = [];

  // Cover
  children.push(new Paragraph({
    children: [new TextRun({ text: memo.client_name || '[Client Name]', bold: true, size: 48 })],
    alignment: AlignmentType.CENTER,
    spacing: { before: 1200, after: 240 },
  }));
  children.push(new Paragraph({
    children: [new TextRun({ text: 'US State Privacy Compliance Memorandum', bold: true, size: 36 })],
    alignment: AlignmentType.CENTER,
    spacing: { after: 480 },
  }));
  children.push(new Paragraph({
    children: [new TextRun({ text: memo.memo_date || '', size: 24 })],
    alignment: AlignmentType.CENTER,
  }));
  if (memo.prepared_by) {
    children.push(new Paragraph({
      children: [new TextRun({ text: `Prepared by: ${memo.prepared_by}`, size: 24 })],
      alignment: AlignmentType.CENTER,
      spacing: { after: 240 },
    }));
  }
  children.push(new Paragraph({ children: [new PageBreak()] }));

  // Disclaimer
  children.push(heading('Disclaimer', 1));
  children.push(p(
    'This memorandum provides legal analysis and drafts based on information supplied by the client and on the state of US state consumer privacy law as of the date above. It does not constitute legal advice. Reliance on this memorandum should occur only after review by qualified counsel admitted in the relevant jurisdiction(s) and verification that controlling law has not changed since the date above. The analysis is constrained by the assumptions and facts identified in the Limitations and Assumptions section. Material changes to the underlying facts may render conclusions inapplicable.',
  ));
  children.push(new Paragraph({ children: [new PageBreak()] }));

  // TOC
  children.push(heading('Contents', 1));
  children.push(new TableOfContents('Contents', {
    hyperlink: true,
    headingStyleRange: '1-3',
  }));
  children.push(new Paragraph({ children: [new PageBreak()] }));

  // 1 Executive summary
  children.push(heading('1. Executive Summary', 1));
  const exec = memo.executive_summary || '';
  exec.split(/\n\s*\n/).forEach(para => { if (para.trim()) children.push(p(para.trim())); });
  if (!exec.trim()) children.push(p('[Executive summary to be drafted.]'));

  // 2 Scope and methodology
  children.push(heading('2. Scope and Methodology', 1));
  children.push(p(memo.scope_and_methodology
    || `This memorandum covers the indicated US state consumer privacy laws as applied to ${memo.client_name || '[client]'}. The analysis is based on inputs provided by the client and on the cited state statutes, implementing regulations, and Attorney General / agency guidance.`));

  // 3 Entity profile
  children.push(heading('3. Entity Profile and Threshold Inputs', 1));
  const profileTable = buildEntityProfileTable(memo.entity_profile);
  if (profileTable) {
    children.push(profileTable);
  } else {
    children.push(p('[Entity profile inputs to be supplied.]'));
  }

  // 4 Applicability
  children.push(heading('4. Applicability Analysis', 1));
  const appTable = buildApplicabilityTable(memo.applicability);
  if (appTable) {
    children.push(appTable);
  } else {
    children.push(p('[Applicability table to be populated from the threshold analysis.]'));
  }

  // 5 Status determination
  children.push(heading('5. Status Determination', 1));
  const statusTable = buildStatusTable(memo.status_determination);
  if (statusTable) {
    children.push(statusTable);
  } else {
    children.push(p('[Status determination by data flow to be supplied.]'));
  }

  // 6 Gap analysis
  children.push(heading('6. Gap Analysis', 1));
  children.push(p(
    'The gap analysis below applies the standard methodology. Severity (1–5) reflects regulatory and litigation exposure; Likelihood (1–5) reflects probability of surfacing; Score = Severity × Likelihood. Lanes: Critical (20–25); High (13–19); Medium (7–12); Low (1–6).',
  ));
  const gapTable = buildGapTable(memo.gaps);
  if (gapTable) {
    children.push(gapTable);
  } else {
    children.push(p('[Gap log to be supplied.]'));
  }

  // 7 Remediation roadmap
  children.push(heading('7. Remediation Roadmap', 1));
  const lanes = [
    { title: '7.1 Immediate (within 7 days, where feasible)', items: memo.remediation && memo.remediation.immediate },
    { title: '7.2 0–30 days', items: memo.remediation && memo.remediation.thirty_day },
    { title: '7.3 31–90 days', items: memo.remediation && memo.remediation.ninety_day },
    { title: '7.4 >90 days / strategic', items: memo.remediation && memo.remediation.strategic },
  ];
  for (const lane of lanes) {
    children.push(heading(lane.title, 2));
    if (lane.items && lane.items.length) {
      lane.items.forEach(item => children.push(bullet(item)));
    } else {
      children.push(p('[None identified at this lane, or to be supplied.]'));
    }
  }

  // 8 Cross-cutting
  children.push(heading('8. Cross-Cutting Recommendations', 1));
  if (memo.cross_cutting && memo.cross_cutting.length) {
    memo.cross_cutting.forEach(item => children.push(bullet(item)));
  } else {
    children.push(p('[Cross-cutting fixes to be identified.]'));
  }

  // 9 Limitations
  children.push(heading('9. Limitations and Assumptions', 1));
  const defaultLimitations = [
    'The revenue, consumer count, and processing activity figures provided by the client are accurate and complete for the relevant calendar year.',
    'The data categories, vendors, and channels described constitute the entirety of the client\u2019s PD processing relevant to US state consumer privacy laws. Undisclosed processing has not been analyzed.',
    'The state statutes, regulations, and AG/agency guidance cited reflect the law in effect as of the date above. Material changes may post-date this memorandum.',
    'This memorandum does not address: federal sectoral laws standalone (HIPAA, GLBA, FCRA, COPPA, FERPA); non-US laws; state biometric laws standalone; state AI-specific laws; consumer-health-data laws; state social media laws; state wiretap statutes; UCL claims; VPPA / TCPA / CAN-SPAM / breach notification.',
    'Current AG enforcement priorities and active litigation may shift the practical risk profile.',
  ];
  const limitations = (memo.limitations && memo.limitations.length) ? memo.limitations : defaultLimitations;
  limitations.forEach(item => children.push(bullet(item, 'numbers')));

  // 10 Next steps
  children.push(heading('10. Recommended Next Steps', 1));
  if (memo.next_steps && memo.next_steps.length) {
    memo.next_steps.forEach(item => children.push(bullet(item, 'numbers')));
  } else {
    children.push(p('[Next steps to be drafted.]'));
  }

  // Document
  return new Document({
    creator: 'us-state-privacy-navigator',
    title: `${memo.client_name || 'Privacy Memo'} — US State Privacy Compliance`,
    styles: {
      default: { document: { run: { font: 'Arial', size: 24 } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 32, bold: true, font: 'Arial' },
          paragraph: { spacing: { before: 320, after: 200 }, outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 28, bold: true, font: 'Arial' },
          paragraph: { spacing: { before: 240, after: 160 }, outlineLevel: 1 } },
        { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 26, bold: true, font: 'Arial' },
          paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 2 } },
      ],
    },
    numbering: {
      config: [
        { reference: 'bullets',
          levels: [{ level: 0, format: LevelFormat.BULLET, text: '\u2022', alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
        { reference: 'numbers',
          levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      ],
    },
    sections: [{
      properties: {
        page: {
          size: { width: 12240, height: 15840 }, // US Letter
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
        },
      },
      headers: {
        default: new Header({
          children: [new Paragraph({
            children: [new TextRun({ text: `${memo.client_name || ''} — US State Privacy Compliance Memorandum`, size: 18, color: '666666' })],
            alignment: AlignmentType.RIGHT,
          })],
        }),
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            children: [
              new TextRun({ text: 'Page ', size: 18, color: '666666' }),
              new TextRun({ children: [PageNumber.CURRENT], size: 18, color: '666666' }),
              new TextRun({ text: ' of ', size: 18, color: '666666' }),
              new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 18, color: '666666' }),
            ],
            alignment: AlignmentType.CENTER,
          })],
        }),
      },
      children,
    }],
  });
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  const { input, output } = parseArgs();
  const memoRaw = fs.readFileSync(path.resolve(input), 'utf8');
  let memo;
  try {
    memo = JSON.parse(memoRaw);
  } catch (e) {
    console.error('Failed to parse input JSON:', e.message);
    process.exit(1);
  }
  const doc = buildDoc(memo);
  const buf = await Packer.toBuffer(doc);
  fs.writeFileSync(path.resolve(output), buf);
  console.log(`Wrote ${output} (${buf.length} bytes).`);
}

main().catch(err => { console.error(err); process.exit(1); });
