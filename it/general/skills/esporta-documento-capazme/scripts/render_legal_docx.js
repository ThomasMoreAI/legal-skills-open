/**
 * render_legal_docx.js — rende un deliverable markdown in un file .docx
 * applicando, quando disponibile, il canone tipografico SAPG (Times New Roman 12,
 * interlinea 1,5, rientro prima riga 0,5 cm, corpo giustificato). Se il modulo
 * SAPG non è installato si applica un fallback "plain" (Times/Arial di default
 * di docx-js) senza errori.
 *
 * Esecuzione (docx-js è installato globalmente):
 *   NODE_PATH=$(npm root -g) node render_legal_docx.js \
 *       --input deliverable.md \
 *       [--title "Titolo documento"] \
 *       [--slug nome-file] \
 *       [--dir /percorso/cartella/attiva]
 *
 * In alternativa il markdown può arrivare da stdin:
 *   cat deliverable.md | NODE_PATH=$(npm root -g) node render_legal_docx.js --title "Parere"
 *
 * Output: <dir>/<slug>.docx — il path assoluto viene stampato su stdout.
 *
 * Mappatura markdown -> blocchi docx: vedi references/mapping.md.
 */

'use strict';

const fs = require('fs');
const path = require('path');
const os = require('os');

const docx = require('docx');
const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  HeadingLevel,
  AlignmentType,
  Table,
  TableRow,
  TableCell,
  WidthType,
  BorderStyle,
} = docx;

// ---------------------------------------------------------------------------
// CLI parsing
// ---------------------------------------------------------------------------

function parseArgs(argv) {
  const args = { input: null, title: null, slug: null, dir: null };
  for (let i = 2; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === '--input' || a === '-i') args.input = argv[++i];
    else if (a === '--title' || a === '-t') args.title = argv[++i];
    else if (a === '--slug' || a === '-s') args.slug = argv[++i];
    else if (a === '--dir' || a === '-d') args.dir = argv[++i];
  }
  return args;
}

function readInput(inputPath) {
  if (inputPath) {
    return fs.readFileSync(inputPath, 'utf8');
  }
  // stdin fallback
  try {
    return fs.readFileSync(0, 'utf8');
  } catch (e) {
    return '';
  }
}

// ---------------------------------------------------------------------------
// Slug + active folder rules (mirror references/mapping.md)
// ---------------------------------------------------------------------------

function slugify(value) {
  const base = (value || 'documento')
    .toLowerCase()
    .normalize('NFKD')
    .replace(/[̀-ͯ]/g, '') // strip accents
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 80);
  return base || 'documento';
}

// ---------------------------------------------------------------------------
// SAPG canon — try-require with graceful fallback
// ---------------------------------------------------------------------------

function loadSapg() {
  const candidate = path.join(
    os.homedir(),
    '.claude/skills/docx-sapg/assets/sapg_styles.js'
  );
  try {
    if (fs.existsSync(candidate)) {
      // eslint-disable-next-line global-require, import/no-dynamic-require
      return require(candidate);
    }
  } catch (e) {
    // fall through to null — plain defaults
  }
  return null;
}

// ---------------------------------------------------------------------------
// Markdown parsing — line-based block tokenizer
// ---------------------------------------------------------------------------

// Inline emphasis: **bold**, __bold__, *italic*, _italic_, `code`.
// Returns an array of docx TextRun for a single line of text.
function inlineRuns(text, runOpts) {
  const opts = runOpts || {};
  const runs = [];
  const re = /(\*\*|__)(.+?)\1|(\*|_)(.+?)\3|`([^`]+)`/g;
  let last = 0;
  let m;
  const push = (chunk, extra) => {
    if (chunk === '') return;
    runs.push(new TextRun(Object.assign({ text: chunk }, opts, extra || {})));
  };
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) push(text.slice(last, m.index));
    if (m[2] !== undefined) push(m[2], { bold: true });
    else if (m[4] !== undefined) push(m[4], { italics: true });
    else if (m[5] !== undefined) push(m[5], { font: 'Courier New' });
    last = re.lastIndex;
  }
  if (last < text.length) push(text.slice(last));
  if (runs.length === 0) push(text);
  return runs;
}

function isTableSeparator(line) {
  // | --- | :---: | ---: |
  return /^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$/.test(line);
}

function splitTableRow(line) {
  let s = line.trim();
  if (s.startsWith('|')) s = s.slice(1);
  if (s.endsWith('|')) s = s.slice(0, -1);
  return s.split('|').map((c) => c.trim());
}

/**
 * Tokenise markdown into a flat list of block descriptors:
 *   { type: 'heading', level, text }
 *   { type: 'paragraph', text }
 *   { type: 'list', ordered, items: [text...] }
 *   { type: 'quote', text }
 *   { type: 'table', rows: [[cell...]...] }
 *   { type: 'spacer' }
 */
function tokenize(md) {
  const lines = md.replace(/\r\n/g, '\n').split('\n');
  const blocks = [];
  let i = 0;

  const flushParagraph = (buf) => {
    if (buf.length) blocks.push({ type: 'paragraph', text: buf.join(' ').trim() });
  };

  let paraBuf = [];

  while (i < lines.length) {
    const line = lines[i];
    const trimmed = line.trim();

    // Blank line -> paragraph boundary
    if (trimmed === '') {
      flushParagraph(paraBuf);
      paraBuf = [];
      i += 1;
      continue;
    }

    // Horizontal rule -> spacer
    if (/^(\*\s*){3,}$|^(-\s*){3,}$|^(_\s*){3,}$/.test(trimmed)) {
      flushParagraph(paraBuf);
      paraBuf = [];
      blocks.push({ type: 'spacer' });
      i += 1;
      continue;
    }

    // ATX heading
    const h = /^(#{1,6})\s+(.*)$/.exec(trimmed);
    if (h) {
      flushParagraph(paraBuf);
      paraBuf = [];
      blocks.push({
        type: 'heading',
        level: Math.min(h[1].length, 3),
        text: h[2].trim(),
      });
      i += 1;
      continue;
    }

    // Blockquote (consume consecutive > lines)
    if (/^>\s?/.test(trimmed)) {
      flushParagraph(paraBuf);
      paraBuf = [];
      const qbuf = [];
      while (i < lines.length && /^\s*>\s?/.test(lines[i])) {
        qbuf.push(lines[i].replace(/^\s*>\s?/, '').trim());
        i += 1;
      }
      blocks.push({ type: 'quote', text: qbuf.join(' ').trim() });
      continue;
    }

    // Table (header row + separator row)
    if (
      trimmed.includes('|') &&
      i + 1 < lines.length &&
      isTableSeparator(lines[i + 1])
    ) {
      flushParagraph(paraBuf);
      paraBuf = [];
      const rows = [splitTableRow(lines[i])];
      i += 2; // skip header + separator
      while (i < lines.length && lines[i].trim().includes('|') && lines[i].trim() !== '') {
        rows.push(splitTableRow(lines[i]));
        i += 1;
      }
      blocks.push({ type: 'table', rows });
      continue;
    }

    // List (unordered or ordered) — consume consecutive items
    const ulItem = /^\s*[-*+]\s+(.*)$/.exec(line);
    const olItem = /^\s*\d+[.)]\s+(.*)$/.exec(line);
    if (ulItem || olItem) {
      flushParagraph(paraBuf);
      paraBuf = [];
      const ordered = !!olItem;
      const items = [];
      while (i < lines.length) {
        const u = /^\s*[-*+]\s+(.*)$/.exec(lines[i]);
        const o = /^\s*\d+[.)]\s+(.*)$/.exec(lines[i]);
        if (ordered && o) items.push(o[1].trim());
        else if (!ordered && u) items.push(u[1].trim());
        else break;
        i += 1;
      }
      blocks.push({ type: 'list', ordered, items });
      continue;
    }

    // Otherwise: accumulate into the current paragraph
    paraBuf.push(trimmed);
    i += 1;
  }

  flushParagraph(paraBuf);
  return blocks;
}

// ---------------------------------------------------------------------------
// Renderers — SAPG variant and plain variant share the same block model
// ---------------------------------------------------------------------------

const PLAIN_FONT = 'Times New Roman';
const PLAIN_SIZE = 24; // 12pt half-points
const PLAIN_LINE = 360; // 1.5 spacing
const PLAIN_FIRST_LINE = 283; // 0.5 cm twips

function plainHeadingLevel(level) {
  return { 1: HeadingLevel.HEADING_1, 2: HeadingLevel.HEADING_2, 3: HeadingLevel.HEADING_3 }[
    level
  ];
}

function buildPlainParagraphs(blocks) {
  const children = [];
  for (const b of blocks) {
    if (b.type === 'heading') {
      children.push(
        new Paragraph({
          heading: plainHeadingLevel(b.level),
          spacing: { before: 200, after: 120, line: PLAIN_LINE, lineRule: 'auto' },
          children: inlineRuns(b.text, { bold: true, font: PLAIN_FONT }),
        })
      );
    } else if (b.type === 'paragraph') {
      children.push(
        new Paragraph({
          alignment: AlignmentType.JUSTIFIED,
          indent: { firstLine: PLAIN_FIRST_LINE },
          spacing: { line: PLAIN_LINE, lineRule: 'auto' },
          children: inlineRuns(b.text, { font: PLAIN_FONT, size: PLAIN_SIZE }),
        })
      );
    } else if (b.type === 'list') {
      b.items.forEach((it) => {
        children.push(
          new Paragraph({
            bullet: b.ordered ? undefined : { level: 0 },
            numbering: b.ordered ? { reference: 'plain-numbers', level: 0 } : undefined,
            spacing: { line: PLAIN_LINE, lineRule: 'auto' },
            children: inlineRuns(it, { font: PLAIN_FONT, size: PLAIN_SIZE }),
          })
        );
      });
    } else if (b.type === 'quote') {
      children.push(
        new Paragraph({
          indent: { left: 567, right: 567 },
          spacing: { before: 120, after: 120, line: PLAIN_LINE, lineRule: 'auto' },
          children: inlineRuns(b.text, { italics: true, font: PLAIN_FONT, size: PLAIN_SIZE }),
        })
      );
    } else if (b.type === 'table') {
      children.push(buildTable(b.rows, { font: PLAIN_FONT, size: PLAIN_SIZE }));
      children.push(new Paragraph({ children: [] }));
    } else if (b.type === 'spacer') {
      children.push(new Paragraph({ children: [] }));
    }
  }
  return children;
}

function buildSapgParagraphs(blocks, sapg) {
  const { FONT, SIZE_BODY } = sapg.constants;
  const children = [];
  for (const b of blocks) {
    if (b.type === 'heading') {
      const styleId = { 1: 'SAPGHeading1', 2: 'SAPGHeading2', 3: 'SAPGHeading3' }[b.level];
      children.push(
        new Paragraph({
          style: styleId,
          children: inlineRuns(b.text, { font: FONT, bold: true, color: '000000' }),
        })
      );
    } else if (b.type === 'paragraph') {
      children.push(
        new Paragraph({
          style: 'SAPGBody',
          children: inlineRuns(b.text, { font: FONT, size: SIZE_BODY, color: '000000' }),
        })
      );
    } else if (b.type === 'list') {
      b.items.forEach((it) => {
        children.push(
          new Paragraph({
            style: 'SAPGBody',
            indent: { left: 720, hanging: 360, firstLine: undefined },
            numbering: {
              reference: b.ordered ? 'sapg-numbers' : 'sapg-bullets',
              level: 0,
            },
            children: inlineRuns(it, { font: FONT, size: SIZE_BODY, color: '000000' }),
          })
        );
      });
    } else if (b.type === 'quote') {
      children.push(
        new Paragraph({
          style: 'SAPGQuote',
          children: inlineRuns(b.text, { font: FONT, size: SIZE_BODY, color: '000000', italics: true }),
        })
      );
    } else if (b.type === 'table') {
      children.push(buildTable(b.rows, { font: FONT, size: SIZE_BODY }));
      children.push(new Paragraph({ style: 'SAPGBody', children: [] }));
    } else if (b.type === 'spacer') {
      children.push(new Paragraph({ children: [] }));
    }
  }
  return children;
}

function buildTable(rows, runOpts) {
  const border = { style: BorderStyle.SINGLE, size: 4, color: '999999' };
  const borders = {
    top: border,
    bottom: border,
    left: border,
    right: border,
    insideHorizontal: border,
    insideVertical: border,
  };
  const tableRows = rows.map((cells, rowIdx) =>
    new TableRow({
      children: cells.map(
        (cell) =>
          new TableCell({
            children: [
              new Paragraph({
                children: inlineRuns(cell, Object.assign({}, runOpts, rowIdx === 0 ? { bold: true } : {})),
              }),
            ],
          })
      ),
    })
  );
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    borders,
    rows: tableRows,
  });
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

function main() {
  const args = parseArgs(process.argv);
  const md = readInput(args.input);
  if (!md || md.trim() === '') {
    console.error('FAIL: nessun contenuto markdown fornito (usa --input o stdin).');
    process.exit(1);
  }

  const blocks = tokenize(md);
  const sapg = loadSapg();

  // Derive title: explicit --title, else first H1, else "Documento".
  let title = args.title;
  if (!title) {
    const firstHeading = blocks.find((b) => b.type === 'heading');
    title = firstHeading ? firstHeading.text : 'Documento';
  }

  const slug = slugify(args.slug || title);
  const outDir = args.dir ? path.resolve(args.dir) : process.cwd();
  const outputPath = path.join(outDir, `${slug}.docx`);

  let doc;
  if (sapg) {
    doc = new Document({
      creator: 'mcp-legal-it',
      title,
      description: 'Deliverable generato da esporta-documento (canone SAPG)',
      styles: {
        default: sapg.sapgDefaults(),
        paragraphStyles: sapg.sapgParagraphStyles(),
      },
      numbering: sapg.sapgNumbering(),
      sections: [
        {
          properties: sapg.sapgPageProperties(),
          children: buildSapgParagraphs(blocks, sapg),
        },
      ],
    });
  } else {
    doc = new Document({
      creator: 'mcp-legal-it',
      title,
      description: 'Deliverable generato da esporta-documento (stile predefinito)',
      numbering: {
        config: [
          {
            reference: 'plain-numbers',
            levels: [
              { level: 0, format: 'decimal', text: '%1.', alignment: AlignmentType.LEFT },
            ],
          },
        ],
      },
      sections: [
        {
          children: buildPlainParagraphs(blocks),
        },
      ],
    });
  }

  Packer.toBuffer(doc)
    .then((buffer) => {
      fs.mkdirSync(outDir, { recursive: true });
      fs.writeFileSync(outputPath, buffer);
      // Echo the absolute path so the skill can report it.
      console.log(outputPath);
    })
    .catch((err) => {
      console.error('FAIL:', err && err.message ? err.message : err);
      process.exit(1);
    });
}

main();
