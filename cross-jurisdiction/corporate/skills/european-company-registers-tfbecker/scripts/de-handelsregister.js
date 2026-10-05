#!/usr/bin/env node
/**
 * German Handelsregister (handelsregister.de), STRUCTURED register data.
 *
 * Complements the financial-statement paths (de-combined.js = Unternehmensregister +
 * Bundesanzeiger). Those give the Jahresabschluss figures; THIS gives the register content:
 * Rechtsform, Sitz + Geschäftsanschrift, Gegenstand des Unternehmens, Stamm-/Grundkapital,
 * Vertretungsregelung, Geschäftsführer / Vorstand, Prokura, and the former names (history).
 *
 * Since the DiRUG reform (1 Aug 2022) the AD ("Aktueller Abdruck" / current extract) is FREE.
 *
 * HOW IT WORKS
 *   handelsregister.de is a stateful JSF/PrimeFaces app (no bot-protection, but ViewState +
 *   partial-AJAX). The search + AD download are driven by the stealth browser via the Python
 *   helper `hr-browser.py` (the only part that needs a browser); this file owns the JSON
 *   contract and parses the AD:
 *     search  -> hr-browser.py search  -> structured result rows (name, HRB, court, seat, …)
 *     details -> hr-browser.py ad      -> downloads the AD PDF -> pdftotext -> parse sections
 *
 * Requirements: the `browser` skill venv (cloakbrowser) + `pdftotext` (poppler) on PATH.
 *
 * Usage:
 *   node de-handelsregister.js search  "Company Name"
 *   node de-handelsregister.js details "Company Name" [--hrb 37497] [--court Köln]
 */

const { spawnSync } = require('child_process');
const os = require('os');
const path = require('path');
const fs = require('fs');

/** Locate the browser skill's venv python (cross-platform), overridable via CLOAK_PYTHON. */
function pythonBin() {
  if (process.env.CLOAK_PYTHON) return process.env.CLOAK_PYTHON;
  const home = os.homedir();
  const candidates = [
    path.join(home, '.claude', 'skills', 'browser', '.venv', 'bin', 'python'),
    path.join(home, '.claude', 'skills', 'browser', '.venv', 'Scripts', 'python.exe'),
  ];
  return candidates.find((c) => fs.existsSync(c)) || 'python3';
}

const HELPER = path.join(__dirname, 'hr-browser.py');

/** Run the Python browser helper and parse its JSON stdout. */
function runHelper(argsArr) {
  const res = spawnSync(pythonBin(), [HELPER, ...argsArr], {
    encoding: 'utf8', maxBuffer: 64 * 1024 * 1024,
  });
  if (res.error) throw new Error(`browser helper failed: ${res.error.message}`);
  // The helper prints one JSON line; ignore any cloakbrowser update notices on stderr/stdout.
  const line = (res.stdout || '').split('\n').reverse().find((l) => l.trim().startsWith('{'));
  if (!line) throw new Error(`browser helper: no JSON output. stderr: ${(res.stderr || '').slice(0, 300)}`);
  return JSON.parse(line);
}

// ---------- AD (Aktueller Abdruck) text parsing ----------

/** Strip the running page headers/footers that repeat on every AD page. */
function stripBoilerplate(text) {
  return text.split('\n').filter((l) => {
    const t = l.trim();
    if (!t) return true;
    return !/^Handelsregister [AB] des\b/.test(t)
      && !/^Amtsgerichts?\b.*Registerinhalts?/.test(t)
      && !/^Abruf vom /.test(t)
      && !/^Abdruck\s+Seite \d+ von \d+/.test(t)
      && !/^Seite \d+ von \d+/.test(t)
      && !/Nummer der Firma:/.test(t)
      && !/^Abteilung [AB]\b/.test(t);
  }).join('\n');
}

/**
 * Split an AD into its labelled sections by scanning lines. The AD is numbered 1..7 with
 * lettered sub-labels; sub-labels b)/c) DON'T repeat the item number, and some headers wrap
 * across two lines (e.g. "b) Vorstand, …, Geschäftsführer, / Vertretungsberechtigte …:").
 * We locate each known header's start line, find where its (possibly wrapped) colon-terminated
 * header ends, and take everything up to the next header as that section's content.
 */
const AD_HEADERS = [
  ['anzahl',     /Anzahl der bisherigen Eintragungen/i],
  ['firma',      /\ba\)\s*Firma\b/i],
  ['sitz',       /\bb\)\s*Sitz\b/i],
  ['gegenstand', /\bc\)\s*Gegenstand des Unternehmens/i],
  ['kapital',    /Grund-?\s*oder\s*Stammkapital/i],
  ['vertretung', /\ba\)\s*Allgemeine Vertretungsregelung/i],
  ['organ',      /\bb\)\s*Vorstand\b/i],
  ['prokura',    /\d\.\s+Prokura\b/i],
  ['rechtsform', /\ba\)\s*Rechtsform\b/i],
  ['sonstige',   /\bb\)\s*Sonstige Rechtsverh/i],
  ['letzte',     /\ba\)\s*Tag der letzten Eintragung/i],
];

function splitSections(text) {
  const lines = text.split('\n');
  // 1) locate each header's start line (first line that matches its pattern)
  const marks = [];
  for (const [key, re] of AD_HEADERS) {
    const idx = lines.findIndex((l) => re.test(l));
    if (idx !== -1) marks.push({ key, start: idx });
  }
  marks.sort((a, b) => a.start - b.start);
  // 2) for each, content = after the header's colon-terminated end, up to the next header start
  const out = {};
  for (let i = 0; i < marks.length; i++) {
    const { key, start } = marks[i];
    const nextStart = i + 1 < marks.length ? marks[i + 1].start : lines.length;
    // header may wrap: advance until the line that ends with ':' (the header terminator)
    let headerEnd = start;
    while (headerEnd < nextStart && !/:\s*$/.test(lines[headerEnd])) headerEnd++;
    const body = lines.slice(headerEnd + 1, nextStart)
      .map((l) => l.trim()).filter((l) => l && l !== '---');
    out[key] = body;
  }
  return out;
}

/** Parse a person line: "Richter, Anita, Lindlar, *21.08.1959" / "Dr. Richter, Markus, …, Köln". */
function parsePerson(line) {
  const birth = line.match(/\*\s*(\d{2}\.\d{2}\.\d{4})/);
  const cleaned = line.replace(/,?\s*\*\s*\d{2}\.\d{2}\.\d{4}\s*$/, '').trim();
  const parts = cleaned.split(',').map((s) => s.trim()).filter(Boolean);
  // Heuristic: [surname, given, <optional profession/qualifiers…>, location]
  let surname = parts[0] || null;
  const given = parts[1] || null;
  const location = parts.length > 2 ? parts[parts.length - 1] : null;
  const middle = parts.slice(2, -1); // professions/qualifiers (e.g. "Dipl.-Kaufmann")
  // Academic titles prefix the surname in the AD ("Dr. Richter, Markus"): split them off.
  let title = null;
  if (surname) {
    const tm = surname.match(/^((?:(?:Prof|Dr|Mag|Dipl|Ing)\.?(?:-?[A-Za-zÄÖÜäöü]+\.?)*)\s+)+/);
    if (tm) { title = tm[0].trim(); surname = surname.slice(tm[0].length).trim(); }
  }
  const name = [title, given, surname].filter(Boolean).join(' ');
  return {
    name: name || cleaned,
    title: title || undefined,
    surname, given,
    location: location || null,
    birth_date: birth ? birth[1] : null,
    qualifiers: middle.length ? middle : undefined,
    raw: line,
  };
}

/** Extract officers (Geschäftsführer / Vorstand / Inhaber / persönlich haftende Ges.) + roles. */
function parseOfficers(lines) {
  const roleRe = /^(Geschäftsführer|Vorstand|Inhaber|Persönlich haftender Gesellschafter|Liquidator|Vertretungsberechtigter|Prokurist|Geschäftsführender Direktor|Vertretungsberechtigte Person)\s*:/i;
  const out = [];
  for (const line of lines) {
    const rm = line.match(roleRe);
    if (rm) {
      const person = parsePerson(line.replace(roleRe, '').trim());
      out.push({ role: rm[1], ...person });
    }
  }
  return out;
}

/** Full AD parse into structured JSON. Keeps `raw_sections` for transparency. */
function parseAD(rawText) {
  const text = stripBoilerplate(rawText);
  const s = splitSections(text);
  const firma = s.firma || [];
  const sitzBlock = s.sitz || [];
  const gegenstand = s.gegenstand || [];
  const kapital = s.kapital || [];
  const vertretung = s.vertretung || [];
  const organBlock = s.organ || [];
  const prokuraBlock = s.prokura || [];
  const rechtsform = s.rechtsform || [];
  const letzteEintragung = s.letzte || [];
  const anzahl = s.anzahl || [];

  // Sitz vs. Geschäftsanschrift
  let sitz = null, anschrift = null;
  for (const l of sitzBlock) {
    const a = l.match(/^Geschäftsanschrift:\s*(.+)/i);
    if (a) anschrift = a[1].trim();
    else if (!sitz) sitz = l;
  }

  // Kapital amount + currency
  let stammkapital = null, currency = null;
  const kj = kapital.join(' ');
  const km = kj.match(/([\d.]+,\d{2}|\d[\d.]*)\s*(EUR|DM|€)/);
  if (km) {
    stammkapital = parseFloat(km[1].replace(/\./g, '').replace(',', '.'));
    currency = km[2] === '€' ? 'EUR' : km[2];
  }

  const officers = parseOfficers(organBlock);
  // Prokura: skip the "Einzelprokura:/Gesamtprokura:" qualifier lines, parse person lines.
  const prokura = prokuraBlock
    .filter((l) => !/^(Einzel|Gesamt)prokura/i.test(l) && /\d|,/.test(l) && !/^---$/.test(l))
    .map((l) => parsePerson(l));

  return {
    name: firma[0] || null,
    seat: sitz || null,
    business_address: anschrift || null,
    purpose: gegenstand.join(' ') || null,
    share_capital: stammkapital,
    share_capital_currency: currency,
    legal_form: rechtsform[0] || null,
    articles_of_association: rechtsform.slice(1).join('; ') || null,
    representation_rule: vertretung.join(' ') || null,
    managing_directors: officers,
    prokura,
    entries_total: anzahl[0] ? parseInt(anzahl[0], 10) : null,
    last_entry_date: letzteEintragung[0] || null,
    raw_sections: {
      gegenstand: gegenstand.join(' ') || null,
      vertretungsregelung: vertretung.join(' ') || null,
    },
  };
}

// ---------- commands ----------

function search(name, max = 25) {
  const res = runHelper(['search', name, '--max', String(max)]);
  return { country: 'de', source: 'handelsregister.de', ...res };
}

function details(name, { hrb, court } = {}) {
  const out = path.join(os.tmpdir(), `hr_AD_${Date.now()}.pdf`);
  const args = ['ad', name, '--out', out];
  if (hrb) args.push('--hrb', String(hrb));
  if (court) args.push('--court', court);
  const dl = runHelper(args);
  if (!dl.downloaded) {
    return { country: 'de', source: 'handelsregister.de', found: false,
      reason: dl.reason || null,
      error: dl.error || 'AD document could not be retrieved', matched: dl.matched || null };
  }
  const txt = spawnSync('pdftotext', ['-layout', out, '-'], { encoding: 'utf8', maxBuffer: 32 * 1024 * 1024 });
  try { fs.unlinkSync(out); } catch (e) { /* best effort */ }
  if (txt.error) {
    return { country: 'de', source: 'handelsregister.de', found: false,
      error: `pdftotext not available (${txt.error.message}). Install poppler.` };
  }
  const parsed = parseAD(txt.stdout || '');
  return {
    country: 'de', source: 'handelsregister.de', document: 'AD (Aktueller Abdruck)',
    found: true, register: dl.matched ? dl.matched.register : null,
    court: dl.matched ? dl.matched.court : null, state: dl.matched ? dl.matched.state : null,
    ...parsed,
  };
}

// CLI
function main() {
  const args = process.argv.slice(2);
  const command = args[0];
  const name = args[1];
  const hrbFlag = args.indexOf('--hrb');
  const courtFlag = args.indexOf('--court');
  const hrb = hrbFlag !== -1 ? args[hrbFlag + 1] : null;
  const court = courtFlag !== -1 ? args[courtFlag + 1] : null;

  if (!command || !name || !['search', 'details', 'analyze'].includes(command)) {
    console.log(`Usage:
  node de-handelsregister.js search  "Company Name"
  node de-handelsregister.js details "Company Name" [--hrb 37497] [--court Köln]

Returns the STRUCTURED Handelsregister content (Rechtsform, Sitz, Gegenstand, Stammkapital,
Geschäftsführer, Prokura, former names). Free (post-DiRUG). Needs the browser skill + pdftotext.`);
    process.exit(command ? 1 : 0);
  }

  let result;
  if (command === 'search') result = search(name);
  else result = details(name, { hrb, court }); // details | analyze
  console.log(JSON.stringify(result, null, 2));
}

module.exports = { search, details, parseAD, parsePerson, parseOfficers };

if (require.main === module) {
  try { main(); }
  catch (e) { console.error('Error:', e.message); process.exit(1); }
}
