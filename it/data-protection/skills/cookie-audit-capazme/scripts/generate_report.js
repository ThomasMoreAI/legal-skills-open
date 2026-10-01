/*
 * generate_report.js — Report Word dell'audit cookie.
 *
 * Uso:
 *   NODE_PATH="$(npm root -g)" node generate_report.js <audit.json> <output.docx>
 *
 * Richiede il pacchetto npm globale `docx` (npm i -g docx).
 *
 * Schema di <audit.json>:
 * {
 *   "site":  "datrixgroup.com",                 // etichetta breve del sito
 *   "url":   "https://datrixgroup.com/it/home/",
 *   "date":  "9 luglio 2026",                    // data rilevazione (stringa libera)
 *   "method": "…",                               // opz. sovrascrive la riga metodo
 *   "note":   "…",                               // opz. caveat (es. ad-blocker)
 *   "cookies": [                                  // righe della tabella, in ordine
 *     { "name":"_ga", "provider":"Google Analytics 4 · dominio",
 *       "purpose":"…", "duration":"2 anni",
 *       "category":"Statistica / Marketing", "state":"Atteso (post-consenso)" }
 *   ],
 *   "notes": [ "nota di accuratezza 1", "nota 2" ]  // opz. bullet finali
 * }
 *
 * La colonna "state" è libera; le parole chiave Osservato/Atteso/Condizionale
 * determinano un colore. La legenda è fissa e sempre inclusa.
 */
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, PageOrientation, HeadingLevel, BorderStyle, WidthType,
  ShadingType, VerticalAlign
} = require("docx");

const [,, inPath, outPath] = process.argv;
if (!inPath || !outPath) {
  console.error("Uso: NODE_PATH=$(npm root -g) node generate_report.js <audit.json> <output.docx>");
  process.exit(1);
}
const A = JSON.parse(fs.readFileSync(inPath, "utf8"));

const HEADER_FILL = "1F3864", ROW_ALT = "EEF3F8";
const BORDER = { style: BorderStyle.SINGLE, size: 1, color: "BBBBBB" };
const borders = { top: BORDER, bottom: BORDER, left: BORDER, right: BORDER };
const COLS = [2500, 2550, 4058, 1350, 1900, 1600];        // somma = 13958 (A4 landscape, margini 1")
const CONTENT_W = COLS.reduce((a, b) => a + b, 0);
const cellMargins = { top: 60, bottom: 60, left: 110, right: 110 };

const stateColor = s => /osserv/i.test(s) ? "1E7A34" : /attes/i.test(s) ? "9A6700" : /condizion/i.test(s) ? "7A4EAB" : "333333";

function hCell(text, i) {
  return new TableCell({ borders, width: { size: COLS[i], type: WidthType.DXA },
    shading: { fill: HEADER_FILL, type: ShadingType.CLEAR }, margins: cellMargins, verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({ children: [new TextRun({ text, bold: true, color: "FFFFFF", size: 17 })] })] });
}
function dCell(runs, i, fill) {
  return new TableCell({ borders, width: { size: COLS[i], type: WidthType.DXA },
    shading: fill ? { fill, type: ShadingType.CLEAR } : undefined, margins: cellMargins, verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({ children: runs })] });
}
const mono = t => [new TextRun({ text: t, font: "Consolas", size: 16 })];
const txt = (t, o = {}) => [new TextRun({ text: t, size: 16, color: o.color })];

const headerRow = new TableRow({ tableHeader: true,
  children: ["Nome cookie", "Fornitore / Dominio", "Finalità", "Durata", "Categoria", "Stato"].map(hCell) });

const bodyRows = (A.cookies || []).map((c, idx) => {
  const fill = idx % 2 ? ROW_ALT : undefined;
  return new TableRow({ children: [
    dCell(mono(c.name || ""), 0, fill),
    dCell(txt(c.provider || ""), 1, fill),
    dCell(txt(c.purpose || ""), 2, fill),
    dCell(txt(c.duration || ""), 3, fill),
    dCell(txt(c.category || ""), 4, fill),
    dCell(txt(c.state || "", { color: stateColor(c.state || "") }), 5, fill),
  ] });
});

const table = new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: COLS, rows: [headerRow, ...bodyRows] });
const r = (t, o = {}) => new TextRun({ text: t, size: 18, bold: o.bold, italics: o.italics, font: o.font, color: o.color });
const bullet = runs => new Paragraph({ numbering: { reference: "b", level: 0 }, spacing: { after: 60 }, children: runs });

const legend = [
  ["Osservato", "cookie effettivamente presente nel browser durante il test (dopo «Accetta tutto»)."],
  ["Atteso (post-consenso)", "non comparso nel test perché un ad-blocker ha bloccato la libreria, ma confermato dal container reale / policy: presente per l'utente comune."],
  ["Condizionale", "si imposta solo su determinate pagine (form/checkout) o sottodomini, non sulla homepage."],
];

const children = [
  new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(`Analisi cookie — ${A.site || A.url || ""}`)] }),
  new Paragraph({ spacing: { after: 60 }, children: [
    r("Pagina analizzata: ", { bold: true }), r(`${A.url || ""}    `),
    r("Data rilevazione: ", { bold: true }), r(A.date || "") ] }),
  new Paragraph({ spacing: { after: 200 }, children: [
    r("Metodo: ", { bold: true }),
    r(A.method || "ispezione con browser controllato in contesto isolato e pulito; stato pre/post-consenso, rete, storage e DOM del banner; inventario tag verificato sul container GTM reale (lato server). "),
    ...(A.note ? [r("Nota: ", { bold: true, italics: true }), r(A.note, { italics: true })] : []) ] }),
  table,
  new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("Legenda «Stato»")] }),
  ...legend.map(([term, desc]) => bullet([r(term, { bold: true }), r(" — " + desc)])),
];

if (A.notes && A.notes.length) {
  children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("Note di accuratezza")] }));
  A.notes.forEach(n => children.push(bullet([r(n)])));
}
children.push(new Paragraph({ spacing: { before: 200 }, children: [
  new TextRun({ text: "Documento generato a supporto dell'analisi tecnica; non costituisce parere legale né validazione di conformità.", italics: true, size: 15, color: "777777" }) ] }));

const doc = new Document({
  numbering: { config: [{ reference: "b", levels: [{ level: 0, format: "bullet", text: "•", alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 460, hanging: 260 } } } }] }] },
  styles: {
    default: { document: { run: { font: "Calibri", size: 20 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 30, bold: true, font: "Calibri", color: "1F3864" }, paragraph: { spacing: { before: 120, after: 160 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 22, bold: true, font: "Calibri", color: "1F3864" }, paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 1 } },
    ] },
  sections: [{
    properties: { page: {
      size: { width: 11906, height: 16838, orientation: PageOrientation.LANDSCAPE },
      margin: { top: 1080, right: 1440, bottom: 1080, left: 1440 } } },
    children }]
});

Packer.toBuffer(doc).then(buf => { fs.writeFileSync(outPath, buf); console.log(`WROTE ${outPath} (${buf.length} bytes)`); });
