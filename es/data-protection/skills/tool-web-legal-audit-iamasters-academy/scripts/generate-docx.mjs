#!/usr/bin/env node
// web-legal-audit :: generate-docx.mjs
// Usage:
//   node generate-docx.mjs --findings evidence.json --output report.docx
//
// Reads the findings JSON produced during the audit and generates a polished .docx
// that follows references/report-structure.md.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);

function resolveDocx() {
  try { return require('docx'); } catch {}
  const candidates = [
    '/opt/homebrew/lib/node_modules/docx',
    '/usr/local/lib/node_modules/docx',
    path.join(process.env.HOME || '', '.npm-global/lib/node_modules/docx'),
  ];
  for (const p of candidates) {
    try { return require(p); } catch {}
  }
  throw new Error('Could not find "docx". Install with `npm install -g docx` or `npm install docx`.');
}

const docx = resolveDocx();
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        Header, Footer, AlignmentType, LevelFormat, HeadingLevel, BorderStyle,
        WidthType, ShadingType, PageNumber, TabStopType, PageBreak } = docx;

// ---- CLI ----
const args = Object.fromEntries(process.argv.slice(2).reduce((acc, v, i, arr) => {
  if (v.startsWith('--')) acc.push([v.slice(2), arr[i + 1]]);
  return acc;
}, []));

const findingsPath = args.findings || 'evidence.json';
const outPath = args.output || 'report.docx';

if (!fs.existsSync(findingsPath)) {
  console.error(`No existe ${findingsPath}. Pasa --findings <path>`);
  process.exit(1);
}

const data = JSON.parse(fs.readFileSync(findingsPath, 'utf8'));

// ---- helpers ----
const border = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
const borders = { top: border, bottom: border, left: border, right: border };
const cellMargins = { top: 100, bottom: 100, left: 140, right: 140 };

const p = (text, opts = {}) => new Paragraph({
  spacing: { after: 120 }, ...opts,
  children: Array.isArray(text) ? text : [new TextRun(text)],
});
const h1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 360, after: 200 },
  children: [new TextRun({ text: t, bold: true, size: 32, color: '1F3864' })] });
const h2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 280, after: 160 },
  children: [new TextRun({ text: t, bold: true, size: 26, color: '2E74B5' })] });
const h3 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 200, after: 120 },
  children: [new TextRun({ text: t, bold: true, size: 22, color: '2E74B5' })] });
const bullet = (t) => new Paragraph({ numbering: { reference: 'bullets', level: 0 },
  spacing: { after: 80 }, children: [new TextRun(t)] });
const quote = (t) => new Paragraph({ spacing: { before: 80, after: 120 }, indent: { left: 360 },
  border: { left: { style: BorderStyle.SINGLE, size: 18, color: 'C00000', space: 8 } },
  children: [new TextRun({ text: t, italics: true, color: '595959' })] });
const pageBreak = () => new Paragraph({ children: [new PageBreak()] });

const cell = (text, { bold = false, fill, width, color } = {}) => new TableCell({
  borders, margins: cellMargins,
  width: { size: width, type: WidthType.DXA },
  shading: fill ? { fill, type: ShadingType.CLEAR } : undefined,
  children: [new Paragraph({ children: [new TextRun({ text: String(text ?? ''), bold, color: color || '000000', size: 20 })] })],
});

const simpleTable = (headers, rows, widths) => {
  const total = widths.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      new TableRow({ tableHeader: true,
        children: headers.map((t, i) => cell(t, { bold: true, fill: '1F3864', color: 'FFFFFF', width: widths[i] })) }),
      ...rows.map(r => new TableRow({
        children: r.map((t, i) => cell(t, { width: widths[i], fill: i === 0 ? 'F2F2F2' : undefined })) })),
    ],
  });
};

// ---- content builders ----
const meta = data.metadata || {};
const urls = Array.isArray(meta.urls) ? meta.urls : [];
const domain = meta.domain || (urls[0] ? new URL(urls[0]).hostname : 'sitio');

const content = [];

// Portada
content.push(
  new Paragraph({ spacing: { before: 1800, after: 200 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: 'AUDITORÍA LEGAL Y DE CUMPLIMIENTO', bold: true, size: 40, color: '1F3864' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 400 },
    children: [new TextRun({ text: 'RGPD · LSSI-CE · Cookies · Accesibilidad · Seguridad', bold: true, size: 28, color: '2E74B5' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 },
    children: [new TextRun({ text: domain, size: 26 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 1200 },
    children: [new TextRun({ text: 'Documento técnico-jurídico para asesoramiento legal', size: 22, italics: true, color: '595959' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
    children: [new TextRun({ text: `Fecha de la auditoría: ${meta.auditDate || new Date().toISOString().slice(0, 10)}`, size: 22 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
    children: [new TextRun({ text: `Jurisdicción principal: ${meta.jurisdiction || 'España / UE'}`, size: 22 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
    children: [new TextRun({ text: 'Metodología: análisis black-box', size: 22 })] }),
  pageBreak()
);

// 1. Resumen ejecutivo
content.push(h1('1. Resumen ejecutivo'));
content.push(p('Este informe documenta los hallazgos de una auditoría de cumplimiento legal sobre las siguientes URLs:'));
urls.forEach(u => content.push(bullet(u)));

if (data.revenue && data.revenue.reported) {
  content.push(p(''));
  content.push(p([
    new TextRun({ text: 'Agravante económico documentado: ', bold: true, color: 'C00000' }),
    new TextRun(`${data.revenue.reported.toLocaleString('es-ES')} € facturados vinculados al tratamiento auditado. ${data.revenue.relevance || ''}`),
  ]));
}

content.push(h2('Valoración global por URL'));
const bySeverity = (fs) => {
  const order = ['critical', 'high', 'medium', 'low'];
  const worst = fs.reduce((a, f) => Math.min(a, order.indexOf(f.severity || 'low')), 3);
  return ['CRÍTICO', 'ALTO', 'MEDIO', 'BAJO'][worst] || 'BAJO';
};
const findingsByUrl = new Map();
(data.findings || []).forEach(f => {
  const u = f.url || 'general';
  if (!findingsByUrl.has(u)) findingsByUrl.set(u, []);
  findingsByUrl.get(u).push(f);
});
const summaryRows = urls.map(u => [u, bySeverity(findingsByUrl.get(u) || []), String((findingsByUrl.get(u) || []).length)]);
if (summaryRows.length) {
  content.push(simpleTable(['URL', 'Nivel de riesgo', '# hallazgos'], summaryRows, [6400, 1600, 1360]));
}

content.push(pageBreak());

// 2. Metodología
content.push(h1('2. Metodología y alcance'));
content.push(p('Auditoría black-box sobre las URLs declaradas, sin acceso al código fuente ni documentación interna del responsable.'));
content.push(p('Herramientas utilizadas:'));
bullet('Navegador real (Chromium) con interceptación de red XHR/Fetch/Document').split; // just to hint
[
  'Navegador real con interceptación de peticiones (Claude in Chrome / Firecrawl)',
  'Extracción de DOM, accesibilidad y árbol semántico',
  'Validación de enlaces legales y contenido de políticas publicadas',
  'Matcheo de red contra base de datos de trackers conocidos',
  'Aplicación de checklists RGPD, LSSI-CE, Cookies-AEPD, WCAG, seguridad, publicidad',
].forEach(t => content.push(bullet(t)));
content.push(p('Limitaciones: no se ha podido verificar el RAT interno, contratos de encargo del tratamiento, ni flujos internos de doble opt-in. Esos aspectos quedan marcados como "Requiere verificación humana".'));

content.push(pageBreak());

// 3+. Hallazgos por URL
let sectionN = 3;
for (const u of urls) {
  const fs = findingsByUrl.get(u) || [];
  content.push(h1(`${sectionN}. URL ${sectionN - 2} — ${u}`));
  sectionN++;

  if (fs.length === 0) {
    content.push(p('No se han registrado hallazgos asociados a esta URL.'));
    content.push(pageBreak());
    continue;
  }
  content.push(h2('Hallazgos de cumplimiento'));
  content.push(simpleTable(
    ['ID', 'Categoría', 'Severidad', 'Título', 'Norma'],
    fs.map(f => [f.id || '-', f.category || '-', (f.severity || '').toUpperCase(), f.title || '-', f.norm || '-']),
    [1200, 1400, 1200, 4160, 1400]
  ));

  content.push(h2('Evidencias literales'));
  fs.filter(f => f.evidence).forEach(f => {
    content.push(p([new TextRun({ text: `[${f.id || ''}] ${f.title}: `, bold: true })]));
    content.push(quote(String(f.evidence).slice(0, 800)));
  });

  content.push(pageBreak());
}

// Trackers detectados
if ((data.trackers || []).length) {
  content.push(h1(`${sectionN}. Trackers detectados sin consentimiento`));
  sectionN++;
  content.push(p('Peticiones interceptadas en la primera carga, sin acción del usuario ni banner de consentimiento previo:'));
  content.push(simpleTable(
    ['Tracker', 'URL observada', 'País', 'Norma'],
    data.trackers.map(t => [t.name, (t.urls || [t.url]).join(', ').slice(0, 200), t.country || '-', (t.normCited || []).join(', ')]),
    [2200, 3600, 1800, 1760]
  ));
  content.push(pageBreak());
}

// Riesgo
if (data.exposureScenarios) {
  content.push(h1(`${sectionN}. Riesgo sancionador`));
  sectionN++;
  const e = data.exposureScenarios;
  const fmt = (v) => v ? `${v.min?.toLocaleString('es-ES') || ''} – ${v.max?.toLocaleString('es-ES') || ''} €` : '-';
  content.push(simpleTable(
    ['Escenario', 'Horquilla', 'Descripción'],
    [
      ['Conservador', fmt(e.conservative), e.conservative?.description || ''],
      ['Medio', fmt(e.medium), e.medium?.description || ''],
      ['Agravado', fmt(e.aggravated) || (e.aggravated?.description || ''), e.aggravated?.description || ''],
    ],
    [1800, 2800, 4760]
  ));
  content.push(p('Horquillas orientativas basadas en precedentes AEPD y la escala del art. 83 RGPD. La cuantía final depende de la modulación por la autoridad según los criterios del art. 83.2 RGPD.'));
  content.push(pageBreak());
}

// Recomendaciones
content.push(h1(`${sectionN}. Recomendaciones y plan de acción`));
sectionN++;
const critical = (data.findings || []).filter(f => f.severity === 'critical');
const high = (data.findings || []).filter(f => f.severity === 'high');
if (critical.length) {
  content.push(h2('Críticas — acción inmediata'));
  critical.forEach(f => content.push(bullet(`[${f.id}] ${f.title}: ${f.recommendation || 'Consultar checklist correspondiente.'}`)));
}
if (high.length) {
  content.push(h2('Altas — acción urgente'));
  high.forEach(f => content.push(bullet(`[${f.id}] ${f.title}: ${f.recommendation || 'Consultar checklist correspondiente.'}`)));
}

content.push(pageBreak());

// Alerta legal consolidada
if ((data.findings || []).length) {
  content.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 200 },
    children: [new TextRun({ text: '⚠ ALERTA LEGAL ⚠', bold: true, size: 48, color: 'C00000' })] }));
  content.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 360 },
    children: [new TextRun({ text: 'Normas incumplidas y exposición sancionadora', bold: true, size: 28, color: 'C00000' })] }));

  const norms = new Map();
  (data.findings || []).forEach(f => {
    if (f.norm) {
      if (!norms.has(f.norm)) norms.set(f.norm, []);
      norms.get(f.norm).push(f);
    }
  });
  if (norms.size) {
    content.push(simpleTable(
      ['Norma', 'Infracción', 'Severidad'],
      Array.from(norms.entries()).map(([norm, fs]) => [
        norm,
        fs.map(x => x.title).join('; ').slice(0, 400),
        bySeverity(fs),
      ]),
      [3200, 4800, 1360]
    ));
  }
}

content.push(pageBreak());

// Nota final
content.push(h1(`${sectionN}. Nota final`));
content.push(p('Este informe se ha elaborado a partir de observación externa en la fecha indicada. La cuantificación de la exposición sancionadora es orientativa y no constituye dictamen jurídico. Se recomienda contrastar los hallazgos con asesoría legal y aportar la siguiente documentación, no verificable externamente, para completar el análisis:'));
[
  'Registro de Actividades del Tratamiento (RAT), art. 30 RGPD',
  'Contratos de encargo del tratamiento con proveedores (art. 28)',
  'Evaluaciones de impacto (EIPD) cuando apliquen (art. 35)',
  'Procedimiento interno de ejercicio de derechos y notificación de brechas',
  'Acreditación documental de los claims publicitarios cuantificados',
].forEach(t => content.push(bullet(t)));

// Document build
const doc = new Document({
  styles: {
    default: { document: { run: { font: 'Calibri', size: 22 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 32, bold: true, font: 'Calibri', color: '1F3864' },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 26, bold: true, font: 'Calibri', color: '2E74B5' },
        paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 22, bold: true, font: 'Calibri', color: '2E74B5' },
        paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 2 } },
    ],
  },
  numbering: {
    config: [{ reference: 'bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•',
      alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] }],
  },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 },
      margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT,
      children: [new TextRun({ text: `Auditoría Legal · ${domain} · Confidencial`, size: 18, color: '808080', italics: true })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: 9000 }],
      children: [
        new TextRun({ text: `Preparado ${new Date().toISOString().slice(0, 10)}`, size: 18, color: '808080' }),
        new TextRun({ text: '\tPágina ', size: 18, color: '808080' }),
        new TextRun({ children: [PageNumber.CURRENT], size: 18, color: '808080' }),
        new TextRun({ text: ' de ', size: 18, color: '808080' }),
        new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 18, color: '808080' }),
      ],
    })] }) },
    children: content,
  }],
});

Packer.toBuffer(doc).then(buffer => {
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, buffer);
  console.log(`OK ${outPath} (${buffer.length} bytes)`);
}).catch(err => {
  console.error('Error generando docx:', err);
  process.exit(1);
});
