#!/usr/bin/env node
/**
 * Poland, KRS (Krajowy Rejestr Sądowy / National Court Register).
 *
 * RELIABLE CORE (no key, no browser): the official Ministry-of-Justice API returns the full
 * structured register extract by KRS number:
 *   GET https://api-krs.ms.gov.pl/api/krs/OdpisAktualny/{krs}?rejestr={P|S}&format=json
 * We parse it into: name, legal form, NIP/REGON, seat + address, share capital, purpose (PKD),
 * management board (zarząd) / supervisory board / prokura, and the list of filed annual
 * financial statements (dzial3) with their periods.
 *
 * NAME → KRS: the official API has NO name search, and the public search portal
 * (wyszukiwarka-krs.ms.gov.pl) is behind Incapsula bot-protection. So:
 *   - a NIP (tax id) is resolved to a KRS for free via the MF "biała lista" whitelist API;
 *   - a plain company name is looked up via the stealth-browser helper `pl-browser.py`
 *     (the only path that needs a browser); if that helper/browser isn't available, we return
 *     a clear message to pass a KRS or NIP instead.
 *
 * FINANCIAL FIGURES: KRS only lists THAT statements were filed (period + date). The actual
 * numbers live in the session-gated e-sprawozdania (JPK XML) in the RDF repository
 * (ekrs.ms.gov.pl/rdf/pd), not fetched here; we expose the filing list + the repository link.
 *
 * Usage:
 *   node pl-krs.js company  <krs>            # official extract by KRS number
 *   node pl-krs.js nip      <nip>            # resolve NIP -> KRS -> extract
 *   node pl-krs.js search   "Company Name"   # name -> KRS (stealth browser)
 *   node pl-krs.js financials <krs>          # filed annual-statement list
 *   node pl-krs.js analyze  <krs | nip>      # unified output
 */

const https = require('https');
const { spawnSync } = require('child_process');
const os = require('os');
const path = require('path');
const fs = require('fs');

const KRS_HOST = 'api-krs.ms.gov.pl';
const MF_HOST = 'wl-api.mf.gov.pl';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

function getJson(hostname, pathname, retries = 3) {
  return new Promise((resolve, reject) => {
    const attempt = (n) => {
      const req = https.request({ hostname, port: 443, path: pathname, method: 'GET',
        headers: { 'Accept': 'application/json', 'User-Agent': UA } }, (res) => {
        let data = '';
        res.on('data', (c) => (data += c));
        res.on('end', () => {
          if (res.statusCode === 200) {
            try { resolve(JSON.parse(data)); } catch (e) { reject(new Error(`bad JSON from ${hostname}`)); }
          } else if (res.statusCode === 404) { resolve(null); }
          else { reject(new Error(`HTTP ${res.statusCode} from ${hostname}: ${data.slice(0, 140)}`)); }
        });
      });
      req.on('error', (e) => {
        if (n < retries && /ECONNRESET|ETIMEDOUT|EAI_AGAIN|socket hang up|EPIPE/i.test(e.message)) {
          setTimeout(() => attempt(n + 1), 400 * (n + 1));
        } else { reject(e); }
      });
      req.end();
    };
    attempt(0);
  });
}

/** Polish decimal "1451177561,25" -> 1451177561.25 */
function plNum(s) {
  if (s == null) return null;
  const n = parseFloat(String(s).replace(/\s/g, '').replace(/\./g, '').replace(',', '.'));
  return Number.isFinite(n) ? n : null;
}

const pad10 = (v) => String(v).replace(/\D/g, '').padStart(10, '0');

/** Fetch the current KRS extract by number, trying register P (entrepreneurs) then S. */
async function getCompanyByKRS(krs, rejestr) {
  const num = pad10(krs);
  const registers = rejestr ? [rejestr] : ['P', 'S'];
  let resp = null, usedReg = null;
  for (const r of registers) {
    resp = await getJson(KRS_HOST, `/api/krs/OdpisAktualny/${num}?rejestr=${r}&format=json`);
    if (resp && resp.odpis) { usedReg = r; break; }
  }
  if (!resp || !resp.odpis) return { found: false, krs: num, error: 'Not found in KRS (registers P/S)' };

  const hdr = resp.odpis.naglowekA || {};
  const dane = resp.odpis.dane || {};
  const d1 = dane.dzial1 || {}, d2 = dane.dzial2 || {}, d3 = dane.dzial3 || {};
  const dp = d1.danePodmiotu || {};
  const ident = dp.identyfikatory || {};
  const sa = d1.siedzibaIAdres || {};
  const kap = (d1.kapital && d1.kapital.wysokoscKapitaluZakladowego) || {};

  const board = ((d2.reprezentacja || {}).sklad || []).map((m) => ({
    role: m.funkcjaWOrganie || null,
    // Names are GDPR-masked in the public API (e.g. surname "L********").
    name_masked: [((m.imiona || {}).imie), ((m.nazwisko || {}).nazwiskoICzlon)].filter(Boolean).join(' ') || null,
    suspended: m.czyZawieszona || false,
  }));
  const prokura = (d2.prokurenci || {}).sklad ? (d2.prokurenci.sklad || []).map((m) => ({
    role: m.rodzajProkury || 'Prokura',
    name_masked: [((m.imiona || {}).imie), ((m.nazwisko || {}).nazwiskoICzlon)].filter(Boolean).join(' ') || null,
  })) : [];

  const pkd = ((d3.przedmiotDzialalnosci || {}).przedmiotPrzewazajacejDzialalnosci || [])
    .map((p) => ({ code: [p.kodDzial, p.kodKlasa, p.kodPodklasa].filter(Boolean).join('.'), description: p.opis }));

  return {
    found: true,
    krs: hdr.numerKRS || num,
    register: usedReg,
    name: dp.nazwa || null,
    legal_form: dp.formaPrawna || null,
    nip: ident.nip || null,
    regon: ident.regon || null,
    registration_date: hdr.dataRejestracjiWKRS || null,
    last_entry_date: hdr.dataOstatniegoWpisu || null,
    seat: sa.siedziba ? [sa.siedziba.miejscowosc, sa.siedziba.wojewodztwo].filter(Boolean).join(', ') : null,
    address: sa.adres ? {
      street: [sa.adres.ulica, sa.adres.nrDomu, sa.adres.nrLokalu].filter(Boolean).join(' '),
      postal_code: sa.adres.kodPocztowy || null, city: sa.adres.miejscowosc || null, country: sa.adres.kraj || null,
    } : null,
    share_capital: plNum(kap.wartosc),
    share_capital_currency: kap.waluta || null,
    purpose: pkd.length ? pkd : null,
    management_board: board,
    prokura,
    _dzial3: d3, // internal, consumed by getFinancials
  };
}

/** Resolve a NIP (tax id) to a KRS via the MF whitelist API. */
async function nipToKRS(nip) {
  const clean = String(nip).replace(/\D/g, '');
  // The MF API requires a date; use a fixed recent ISO date passed by the caller via env, else
  // fall back to the endpoint's "today" behaviour by omitting is not allowed, use a wide date.
  const date = process.env.PL_MF_DATE || new Date(Date.now()).toISOString().slice(0, 10);
  const resp = await getJson(MF_HOST, `/api/search/nip/${clean}?date=${date}`);
  const subj = resp && resp.result && resp.result.subject;
  if (!subj) return { found: false, nip: clean, error: 'NIP not found in MF whitelist' };
  return { found: true, nip: clean, krs: subj.krs || null, name: subj.name || null,
    regon: subj.regon || null, vat_status: subj.statusVat || null };
}

/** Filed annual financial statements from dzial3 (list only; figures are in the gated JPK XML). */
function financialsFromDzial3(d3, krs) {
  const wz = (d3 && d3.wzmiankiOZlozonychDokumentach) || {};
  const filings = (wz.wzmiankaOZlozeniuRocznegoSprawozdaniaFinansowego || []).map((f) => ({
    period: f.zaOkresOdDo || null, filed_date: f.dataZlozenia || null,
  }));
  return {
    filings_count: filings.length,
    filings: filings.slice().reverse(),   // newest first
    figures: null,
    figures_note: 'KRS lists only that statements were filed. The actual figures are in the ' +
      'session-gated e-sprawozdania (JPK XML) in the RDF repository, not extracted here.',
    repository: `https://ekrs.ms.gov.pl/rdf/pd/search_df?krs=${pad10(krs)}`,
  };
}

/** Name → KRS via the stealth-browser helper (Incapsula-protected portal). Best-effort. */
function searchByName(name) {
  const helper = path.join(__dirname, 'pl-browser.py');
  if (!fs.existsSync(helper)) {
    return { found: false, searched_name: name,
      note: 'Name search needs the browser helper (pl-browser.py), pass a KRS number or NIP instead, ' +
            'or search manually at https://wyszukiwarka-krs.ms.gov.pl/' };
  }
  const py = process.env.CLOAK_PYTHON || [
    path.join(os.homedir(), '.claude', 'skills', 'browser', '.venv', 'bin', 'python'),
    path.join(os.homedir(), '.claude', 'skills', 'browser', '.venv', 'Scripts', 'python.exe'),
  ].find((c) => fs.existsSync(c)) || 'python3';
  const res = spawnSync(py, [helper, 'search', name], { encoding: 'utf8', maxBuffer: 32 * 1024 * 1024 });
  const line = (res.stdout || '').split('\n').reverse().find((l) => l.trim().startsWith('{'));
  if (!line) return { found: false, searched_name: name, error: 'browser helper produced no output',
    note: 'Pass a KRS number or NIP instead.' };
  return JSON.parse(line);
}

async function getFinancials(krs) {
  const c = await getCompanyByKRS(krs);
  if (!c.found) return { found: false, krs: pad10(krs), error: c.error };
  return { found: true, krs: c.krs, company_name: c.name, ...financialsFromDzial3(c._dzial3, c.krs) };
}

/** Unified analyze, accepts a KRS (tried first) or a NIP (fallback). */
async function analyzeCompany(input) {
  const clean = String(input).replace(/\D/g, '');
  let company = await getCompanyByKRS(clean);
  let viaNip = null;
  if (!company.found && clean.length === 10) {
    const r = await nipToKRS(clean);
    if (r.found && r.krs) { viaNip = r; company = await getCompanyByKRS(r.krs); }
  }
  if (!company.found) {
    return { company_name: null, country: 'pl', registration_id: clean, found: false,
      error: 'Not found by KRS or NIP' };
  }
  const fin = financialsFromDzial3(company._dzial3, company.krs);
  delete company._dzial3;
  return {
    company_name: company.name, country: 'pl', registration_id: company.krs,
    nip: company.nip, regon: company.regon, found: true,
    legal_form: company.legal_form, seat: company.seat, address: company.address,
    registration_date: company.registration_date, last_entry_date: company.last_entry_date,
    share_capital: company.share_capital, share_capital_currency: company.share_capital_currency,
    purpose: company.purpose, management_board: company.management_board, prokura: company.prokura,
    financial_data: { revenue: null, total_assets: null, earnings: null,
      fiscal_year: fin.filings[0] ? fin.filings[0].period : null, currency: 'PLN' },
    financial_filings: fin.filings, financial_note: fin.figures_note, financial_repository: fin.repository,
    resolved_via_nip: viaNip ? viaNip.nip : undefined,
    source: 'krs (api-krs.ms.gov.pl)',
    vat_status: viaNip ? viaNip.vat_status : undefined,
    board_names_note: company.management_board.length
      ? 'Management/board names are GDPR-masked in the public KRS API.' : undefined,
  };
}

// CLI
async function main() {
  const args = process.argv.slice(2);
  const [command, arg] = args;
  if (!command || (command !== 'search' && !arg)) {
    console.log(`Usage:
  node pl-krs.js company   <krs>
  node pl-krs.js nip       <nip>
  node pl-krs.js search    "Company Name"
  node pl-krs.js financials <krs>
  node pl-krs.js analyze   <krs | nip>

KRS by number is the reliable path (no key). NIP is resolved via the MF whitelist.
Name search uses the stealth browser (portal is bot-protected).`);
    process.exit(command ? 1 : 0);
  }
  let result;
  if (command === 'company') result = await getCompanyByKRS(arg);
  else if (command === 'nip') result = await nipToKRS(arg);
  else if (command === 'search') result = searchByName(arg);
  else if (command === 'financials') result = await getFinancials(arg);
  else if (command === 'analyze') result = await analyzeCompany(arg);
  else { console.error(`Unknown command: ${command}`); process.exit(1); }
  if (result && result._dzial3) delete result._dzial3;
  console.log(JSON.stringify(result, null, 2));
}

module.exports = { getCompanyByKRS, nipToKRS, getFinancials, analyzeCompany, searchByName, plNum };

if (require.main === module) {
  main().catch((e) => { console.error('Error:', e.message); process.exit(1); });
}
