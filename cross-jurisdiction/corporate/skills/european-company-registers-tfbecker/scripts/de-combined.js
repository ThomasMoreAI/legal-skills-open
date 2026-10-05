#!/usr/bin/env node
/**
 * Combined German company register, Unternehmensregister + Bundesanzeiger.
 *
 * The two DE sources are complementary:
 *   - Unternehmensregister (de-unternehmensregister.js): fast, no browser, no CAPTCHA, a
 *     *superset* listing, it aggregates UR-published (GJ 2022+) and Bundesanzeiger-published
 *     (GJ ≤2021) reports, plus register metadata (EUID, HRB, court, legal form). Retrieving
 *     the actual document figures is a separate, partly paid step.
 *   - Bundesanzeiger (de-bundesanzeiger.js): its report pages render as free HTML that the
 *     CAPTCHA+Claude extractor turns into real numbers, but only up to GJ 2021.
 *
 * THREE RETRIEVAL MODES (listing is always CAPTCHA-free):
 *   latest  (default), Unternehmensregister only, newest report per company. Fastest (~0.5 s).
 *   all-ur           , Unternehmensregister only, ALL reports (no CAPTCHA). ~0.5-0.7 s.
 *   all              , Unternehmensregister + Bundesanzeiger in parallel, ALL reports; adds
 *                       the free-extractable Bundesanzeiger URLs for historical figures. ~1.1 s.
 *
 * A CAPTCHA is only ever touched by `analyze` (on-demand figures), never by listing.
 *
 * Usage:
 *   node de-combined.js search  "Company Name"            # mode: latest (default)
 *   node de-combined.js search  "Company Name" --all-ur   # all Unternehmensregister reports
 *   node de-combined.js search  "Company Name" --all      # + Bundesanzeiger (historical)
 *   node de-combined.js analyze "Company Name" [--index N] [--year YYYY]
 *
 * Flags: --verbose/-v keep the raw encrypted payloads/URLs in the printed JSON.
 */

const ur = require('./de-unternehmensregister.js');
const ba = require('./de-bundesanzeiger.js');
const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const norm = (s) => (s || '').toLowerCase().replace(/\s+/g, ' ').replace(/[.,]/g, '').trim();

/** Locate the browser skill's Python (has cloakbrowser). Override with UR_PYTHON. */
function findPython() {
  if (process.env.UR_PYTHON) return process.env.UR_PYTHON;
  const home = process.env.HOME || process.env.USERPROFILE || '';
  const candidates = [
    path.join(home, '.claude/skills/browser/.venv/bin/python'),
    path.join(home, '.claude/skills/browser/.venv/Scripts/python.exe'),
  ];
  for (const c of candidates) { if (fs.existsSync(c)) return c; }
  return 'python3';
}

/**
 * Fetch the checkbox-gated Unternehmensregister documents for the given years (one browser
 * session for all of them) and Claude-extract each into figures. Returns { year -> financial }.
 * Best-effort: on any failure the year simply isn't in the map (caller marks it gated).
 */
function fetchURDocs(companyName, years, index) {
  if (!years.length) return [];
  const script = path.join(__dirname, 'ur_fetch_document.py');
  const py = findPython();
  const res = spawnSync(py, [script, '--company', companyName, '--years', years.join(','),
    '--index', String(index || 0)], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024, timeout: 240000 });
  if (res.status !== 0 || !res.stdout) {
    console.error('UR document fetch failed:', (res.stderr || res.error || '').toString().slice(0, 300));
    return [];
  }
  try { return JSON.parse(res.stdout).results || []; } catch (e) { return []; } // [{year, ok, text}]
}

// ── Full-text persistence ────────────────────────────────────────────────────────────────────
// The document text scraped from either source (the full Jahresabschluss / Lagebericht) used to
// be discarded after the figure extraction. It is now captured on `report`/`analyze` and, by
// default, written to one .txt file per year so nothing has to be re-scraped later.

/** Sanitize a string into a safe filename part. */
function sanitizeFilePart(s) {
  return String(s == null ? '' : s).replace(/[^\w.-]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 80) || 'x';
}

/** Resolve text-saving options (defaults: save ON, dir ./register-texts, no inline text). */
function resolveTextOpts(opts = {}) {
  return {
    save: opts.saveText !== false, // default ON, the point of the feature
    inline: !!opts.inlineText,     // also embed the text in the JSON output
    dir: opts.textDir || process.env.REGISTER_TEXT_DIR || path.join(process.cwd(), 'register-texts'),
  };
}

/**
 * Write a report's full text to <dir>/<court>_<register>_GJ<year>_<source>.txt (with a short
 * provenance header) and return the absolute path. Throws on I/O error (caller records it).
 */
function saveReportText(meta, text, dir) {
  fs.mkdirSync(dir, { recursive: true });
  const fname = [
    sanitizeFilePart(meta.court || 'DE'),
    sanitizeFilePart(meta.register || meta.euid || meta.company_name),
    'GJ' + sanitizeFilePart(meta.fiscal_year || 'x'),
    sanitizeFilePart(meta.source || 'de'),
  ].join('_') + '.txt';
  const fpath = path.join(dir, fname);
  const header = [
    `# ${meta.company_name || ''}`,
    `# Register: ${meta.register || ''}  Court: ${meta.court || ''}  EUID: ${meta.euid || ''}`,
    `# Geschäftsjahr: ${meta.fiscal_year || ''}  Quelle: ${meta.source || ''}`,
    `# Bericht: ${meta.report_name || ''}`,
    `# Zeichen: ${text.length}`,
    '', '',
  ].join('\n');
  fs.writeFileSync(fpath, header + text, 'utf8');
  return fpath;
}

/**
 * Attach the captured full text to a per-year result row: always record `report_chars`; embed
 * `report_text` when inline is on; write the .txt file and record `report_text_file` when saving.
 * A no-op when there is no text (extraction failed / listed-only year).
 */
function applyText(row, text, source, company, T) {
  if (!text) return;
  row.report_chars = text.length;
  if (T.inline) row.report_text = text;
  if (T.save) {
    try {
      row.report_text_file = saveReportText({
        company_name: company.name, register: company.register, court: company.court,
        euid: company.euid, fiscal_year: row.fiscal_year, report_name: row.report_name, source,
      }, text, T.dir);
      console.error('Saved report text →', row.report_text_file);
    } catch (e) {
      row.text_save_error = e.message;
    }
  }
}

/** Merge the UR + BA search results into one per-company, per-fiscal-year view. */
function mergeSearch(searchedName, urRes, baRes, urError, baError) {
  const companies = new Map();

  const ensure = (name, meta = {}) => {
    const k = norm(name);
    if (!companies.has(k)) {
      companies.set(k, {
        name, location: null, euid: null, register: null, register_number: null,
        court: null, state: null, reports: new Map(),
      });
    }
    const co = companies.get(k);
    for (const f of ['location', 'euid', 'register', 'register_number', 'court', 'state']) {
      if (meta[f] != null && co[f] == null) co[f] = meta[f];
    }
    return co;
  };

  const addReport = (co, { fiscal_year, name, date, source, ba_url, ur_payload }) => {
    const key = fiscal_year || `${source}:${date}:${name}`;
    if (!co.reports.has(key)) {
      co.reports.set(key, {
        fiscal_year: fiscal_year || null,
        report_name: name || null,
        date: date || null,
        sources: [],
        free_extract: false, // true => a free Bundesanzeiger figure extraction is available
        _ba_url: null,        // internal: consumed by analyze, stripped from printed output
        _ur_payload: null,    // internal
      });
    }
    const r = co.reports.get(key);
    if (source && !r.sources.includes(source)) r.sources.push(source);
    if (ba_url && !r._ba_url) { r._ba_url = ba_url; r.free_extract = true; }
    if (ur_payload && !r._ur_payload) r._ur_payload = ur_payload;
    if (!r.report_name && name) r.report_name = name;
    if (!r.date && date) r.date = date;
  };

  if (urRes && urRes.found) {
    for (const c of urRes.companies) {
      const co = ensure(c.name, c);
      for (const rep of c.reports) {
        addReport(co, {
          fiscal_year: rep.fiscal_year, name: rep.name, date: rep.date, source: rep.source,
          ur_payload: rep.source === 'unternehmensregister' ? rep.encrypted_payload : null,
        });
      }
    }
  }

  if (baRes && baRes.found) {
    for (const c of baRes.companies) {
      const co = ensure(c.name);
      for (const rep of c.reports) {
        addReport(co, {
          fiscal_year: ur.fiscalYearFromTitle(rep.name),
          name: rep.name,
          date: rep.date ? rep.date.split('.').reverse().join('-') : null, // DD.MM.YYYY -> ISO
          source: 'bundesanzeiger',
          ba_url: rep.url,
        });
      }
    }
  }

  // Relevance of a company name to the search term: exact > prefix > contains > token overlap.
  const nq = norm(searchedName);
  const qTokens = nq.split(' ').filter(Boolean);
  const relevance = (name) => {
    const n = norm(name);
    if (n === nq) return 100;
    if (n.startsWith(nq)) return 80;
    if (n.includes(nq)) return 60;
    const hits = qTokens.filter((t) => t.length > 2 && n.includes(t)).length;
    return qTokens.length ? Math.round((hits / qTokens.length) * 40) : 0;
  };

  const out = [];
  for (const co of companies.values()) {
    const reports = [...co.reports.values()].sort((a, b) => {
      const fy = (parseInt(b.fiscal_year, 10) || 0) - (parseInt(a.fiscal_year, 10) || 0);
      if (fy !== 0) return fy;
      return String(b.date || '').localeCompare(String(a.date || ''));
    });
    out.push({
      name: co.name, location: co.location, euid: co.euid,
      register: co.register, register_number: co.register_number,
      court: co.court, state: co.state,
      _relevance: relevance(co.name),
      report_count: reports.length,
      newest_fiscal_year: reports.length ? reports[0].fiscal_year : null,
      reports,
    });
  }
  // Best name match first; ties broken by how many reports the company has.
  out.sort((a, b) => (b._relevance - a._relevance) || (b.report_count - a.report_count));

  return {
    country: 'de', searched_name: searchedName, found: out.length > 0,
    sources_queried: baRes || baError ? ['unternehmensregister', 'bundesanzeiger'] : ['unternehmensregister'],
    source_errors: { unternehmensregister: urError || null, bundesanzeiger: baError || null },
    companies_count: out.length, companies: out,
  };
}

/**
 * Fast combined listing. Never triggers a CAPTCHA.
 * opts.mode: 'latest' (default) | 'all-ur' | 'all'
 */
async function combinedSearch(companyName, opts = {}) {
  const mode = opts.mode || 'latest';
  const runBA = mode === 'all';

  const t0 = Date.now();
  let urRes = null, baRes = null, urError = null, baError = null;
  const timing = {};

  const urP = (async () => {
    const s = Date.now();
    // 1 UR page by default (complete for a precise name); --deep paginates for fuzzy search.
    try { urRes = await ur.searchUR(companyName, { deep: !!opts.deep }); }
    catch (e) { urError = e.message; }
    timing.unternehmensregister_ms = Date.now() - s;
  })();

  const baP = runBA ? (async () => {
    const s = Date.now();
    try { baRes = await ba.searchCompanies(companyName); }
    catch (e) { baError = e.message; }
    timing.bundesanzeiger_ms = Date.now() - s;
  })() : Promise.resolve();

  await Promise.all([urP, baP]);

  const merged = mergeSearch(companyName, urRes, baRes, urError, baError);

  // latest: keep only the newest report per company.
  if (mode === 'latest') {
    for (const co of merged.companies) {
      co.reports = co.reports.slice(0, 1);
      co.report_count = co.reports.length;
    }
  }

  merged.mode = mode;
  merged.timing_ms = { ...timing, total_ms: Date.now() - t0 };
  return merged;
}

/**
 * On-demand figure extraction for one fiscal year of one company. Runs in 'all' mode so the
 * free Bundesanzeiger URLs are available; extracts via the free CAPTCHA+Claude path when a
 * Bundesanzeiger source exists (≤2021), else reports the UR-only (partly paid) limitation.
 */
async function combinedAnalyze(companyName, opts = {}) {
  // A requested year ≥2022 is post-DiRUG → definitely Unternehmensregister-only (gated),
  // so skip the Bundesanzeiger call entirely. Otherwise run 'all' to get the free BA URL.
  const gatedOnly = opts.year && parseInt(opts.year, 10) >= 2022;
  const listing = await combinedSearch(companyName, { mode: gatedOnly ? 'all-ur' : 'all', deep: opts.deep });
  if (!listing.found) return { ...listing, error: 'Company not found in either register' };

  const company = listing.companies[opts.index || 0];
  if (!company) {
    return { country: 'de', found: true, error: `Index ${opts.index} out of range (${listing.companies_count} companies)` };
  }

  let target = company.reports[0];
  if (opts.year) target = company.reports.find((r) => r.fiscal_year === String(opts.year)) || null;
  if (!target) {
    return {
      country: 'de', found: true, company_name: company.name,
      error: `No report for fiscal year ${opts.year}. Available: ${company.reports.map((r) => r.fiscal_year).filter(Boolean).join(', ')}`,
    };
  }

  const base = {
    country: 'de', company_name: company.name, euid: company.euid, register: company.register,
    court: company.court, fiscal_year: target.fiscal_year, report_name: target.report_name,
    report_date: target.date, sources: target.sources,
  };
  const T = resolveTextOpts(opts);

  if (target._ba_url) {
    const text = await ba.fetchReportText(target._ba_url);
    const financial = text ? await ba.extractFinancialData(text) : null;
    const out = { ...base, extraction_source: 'bundesanzeiger',
      financial_data: financial ? { ...financial, currency: 'EUR' } : null };
    applyText(out, text, 'bundesanzeiger', company, T);
    if (T.save) out.text_dir = T.dir;
    return out;
  }

  // Unternehmensregister-only year (post-DiRUG): free but behind a checkbox → browser extract.
  if (!opts.noUR) {
    const docs = fetchURDocs(company.name, [target.fiscal_year], opts.index || 0);
    const d = docs.find((x) => String(x.year) === target.fiscal_year);
    if (d && d.ok && d.text) {
      const financial = await ba.extractFinancialData(d.text);
      const out = { ...base, extraction_source: 'unternehmensregister',
        financial_data: financial ? { ...financial, currency: 'EUR' } : null };
      applyText(out, d.text, 'unternehmensregister', company, T);
      if (T.save) out.text_dir = T.dir;
      return out;
    }
    return { ...base, extraction_source: 'unternehmensregister', financial_data: null,
      note: 'Unternehmensregister document fetch/extraction failed (browser or checkbox issue). Retry, or use --no-ur to skip.' };
  }
  return { ...base, extraction_source: 'unternehmensregister', financial_data: null,
    note: 'UR-only year; browser extraction skipped (--no-ur).' };
}

/**
 * One-shot multi-year company report: ONE search, then extract every free (Bundesanzeiger)
 * fiscal year in a single process, the efficient path for "analyse company X over all years".
 * Gated (Unternehmensregister-only, post-DiRUG) years are listed with a note, not re-searched.
 * Extraction is sequential (the Bundesanzeiger session is shared) and capped by --max-extract.
 */
async function combinedReport(companyName, opts = {}) {
  const listing = await combinedSearch(companyName, { mode: 'all', deep: opts.deep });
  if (!listing.found) return { ...listing, error: 'Company not found in either register' };

  const company = listing.companies[opts.index || 0];
  if (!company) {
    return { country: 'de', found: true, error: `Index ${opts.index} out of range (${listing.companies_count} companies)` };
  }

  let reports = company.reports;
  if (opts.years && opts.years.length) reports = reports.filter((r) => opts.years.includes(r.fiscal_year));

  const maxExtract = opts.maxExtract != null ? opts.maxExtract : 5;
  const toExtract = reports.slice(0, maxExtract);        // newest-first
  const extractSet = new Set(toExtract);
  // Route each target year: Bundesanzeiger URL => free HTTP path; else Unternehmensregister browser.
  const urTargets = opts.noUR ? [] : toExtract.filter((r) => !r._ba_url && r.fiscal_year);

  const T = resolveTextOpts(opts);

  // 1) Unternehmensregister documents, all target years in ONE browser session, then Claude-extract
  //    them CONCURRENTLY (independent `claude` processes) instead of one-after-another. Keep the
  //    full document text (urTexts) so it can be persisted below, not just the extracted figures.
  const urFigures = {}; // fiscal_year -> financial | null
  const urTexts = {};   // fiscal_year -> full document text
  if (urTargets.length) {
    const docs = fetchURDocs(company.name, urTargets.map((r) => r.fiscal_year), opts.index || 0);
    const byYear = {};
    for (const d of docs) byYear[String(d.year)] = d;
    await Promise.all(urTargets.map(async (r) => {
      const d = byYear[r.fiscal_year];
      if (d && d.ok && d.text) {
        urTexts[r.fiscal_year] = d.text;
        urFigures[r.fiscal_year] = await ba.extractFinancialDataAsync(d.text);
      } else {
        urFigures[r.fiscal_year] = null;
      }
    }));
  }

  // 2) Build per-year rows (Bundesanzeiger years extracted sequentially, the session is shared).
  const years = [];
  for (const r of reports) {
    const row = { fiscal_year: r.fiscal_year, report_name: r.report_name, date: r.date, sources: r.sources };
    if (!extractSet.has(r)) {
      row.status = 'listed_only'; // beyond the --max-extract window
      row.financial_data = null;
    } else if (r._ba_url) {
      const text = await ba.fetchReportText(r._ba_url);
      const fin = text ? await ba.extractFinancialData(text) : null;
      row.status = fin ? 'extracted' : 'extraction_failed';
      row.extraction_source = 'bundesanzeiger';
      row.financial_data = fin ? { ...fin, currency: 'EUR' } : null;
      applyText(row, text, 'bundesanzeiger', company, T);
    } else if (r.fiscal_year in urFigures) {
      const fin = urFigures[r.fiscal_year];
      row.status = fin ? 'extracted' : 'extraction_failed';
      row.extraction_source = 'unternehmensregister';
      row.financial_data = fin ? { ...fin, currency: 'EUR' } : null;
      applyText(row, urTexts[r.fiscal_year], 'unternehmensregister', company, T);
    } else {
      row.status = 'gated_skipped'; // --no-ur: UR-only year, browser extraction skipped
      row.financial_data = null;
    }
    years.push(row);
  }

  const extracted = years.filter((y) => y.status === 'extracted').length;
  const savedTexts = years.filter((y) => y.report_text_file).length;
  return {
    country: 'de',
    company_name: company.name,
    location: company.location,
    euid: company.euid,
    register: company.register,
    court: company.court,
    state: company.state,
    report_count: company.report_count,
    extracted_count: extracted,
    text_dir: T.save && savedTexts ? T.dir : undefined,
    saved_text_count: T.save ? savedTexts : undefined,
    note: reports.length > maxExtract
      ? `Extracted the newest ${maxExtract} of ${reports.length} years. Raise --max-extract for more.`
      : undefined,
    years,
  };
}

/** Remove heavy/internal fields (encrypted blobs, long URLs) from the printed JSON. */
function cleanForPrint(result, verbose) {
  if (verbose || !result || !result.companies) return result;
  const clone = JSON.parse(JSON.stringify(result));
  for (const co of clone.companies) {
    delete co.encrypted_id;
    delete co._relevance;
    for (const r of co.reports || []) {
      delete r._ba_url;
      delete r._ur_payload;
      delete r.source_raw;
    }
  }
  return clone;
}

// CLI
async function main() {
  const args = process.argv.slice(2);
  const command = args[0];
  const companyName = args[1];
  const verbose = args.includes('--verbose') || args.includes('-v');
  const deep = args.includes('--deep');
  const noUR = args.includes('--no-ur');
  const saveText = !args.includes('--no-save-text'); // full text is saved to files by default
  const inlineText = args.includes('--inline-text');  // also embed the text in the JSON output

  let mode = 'latest';
  if (args.includes('--all')) mode = 'all';
  else if (args.includes('--all-ur') || args.includes('--ur')) mode = 'all-ur';

  const flagVal = (name) => { const i = args.indexOf(name); return i !== -1 ? args[i + 1] : null; };
  const index = parseInt(flagVal('--index') || '0', 10);
  const year = flagVal('--year');
  const maxExtractRaw = flagVal('--max-extract');
  const maxExtract = maxExtractRaw != null ? parseInt(maxExtractRaw, 10) : undefined;
  const years = (flagVal('--years') || '').split(',').map((s) => s.trim()).filter(Boolean);
  const textDir = flagVal('--text-dir');

  if (!command || !companyName) {
    console.log(`Usage:
  node de-combined.js search  "Company Name"            # latest report only (default, fastest ~0.4s)
  node de-combined.js search  "Company Name" --all-ur   # all Unternehmensregister reports (~0.5s)
  node de-combined.js search  "Company Name" --all      # + Bundesanzeiger, free-extract URLs (~0.9s)
  node de-combined.js report  "Company Name" [--max-extract N] [--years 2021,2020]
                                                        # ONE search + extract all free years' figures
  node de-combined.js analyze "Company Name" [--index N] [--year YYYY]  # one year's figures
  Flags: --deep (paginate UR for fuzzy names) · --index N (pick company) · -v (raw payloads)
  Full text (report/analyze): the scraped Jahresabschluss/Lagebericht text is saved to one .txt
    per year by DEFAULT. --text-dir <dir> (default ./register-texts) · --no-save-text (figures
    only) · --inline-text (also embed the text in the JSON). Env: REGISTER_TEXT_DIR.`);
    process.exit(command ? 1 : 0);
  }

  let result;
  if (command === 'search') result = await combinedSearch(companyName, { mode, deep });
  else if (command === 'analyze') result = await combinedAnalyze(companyName, { index, year, deep, noUR, saveText, inlineText, textDir });
  else if (command === 'report') result = await combinedReport(companyName, { index, years, maxExtract, deep, noUR, saveText, inlineText, textDir });
  else { console.error(`Unknown command: ${command}`); process.exit(1); }

  // Flush stdout, then exit hard: the HTTP keep-alive sockets otherwise idle ~5 s.
  process.stdout.write(JSON.stringify(cleanForPrint(result, verbose), null, 2) + '\n', () => process.exit(0));
}

module.exports = { combinedSearch, combinedAnalyze, combinedReport, mergeSearch, cleanForPrint,
  saveReportText, resolveTextOpts, sanitizeFilePart };

if (require.main === module) {
  main().catch((e) => { console.error('Error:', e.message); process.exit(1); });
}
