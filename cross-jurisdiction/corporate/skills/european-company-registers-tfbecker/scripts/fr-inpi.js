#!/usr/bin/env node
/**
 * France, company register (RNE / INPI), via the free government API.
 *
 * PRIMARY SOURCE (no key, no CAPTCHA): recherche-entreprises.api.gouv.fr
 *   The official "Recherche d'entreprises" API aggregates INSEE + RNE (INPI) + the open
 *   financial-ratios dataset. Crucially it returns, for free:
 *     - full company metadata (SIREN/SIRET, address, NAF activity, legal form, headcount band)
 *     - `dirigeants`  → the register's officers (gérant / président / DG / board)
 *     - `finances`    → year-keyed { ca: chiffre d'affaires (revenue), resultat_net (earnings) }
 *   So we get real REVENUE figures with zero setup. (The old data.inpi.fr/api/entreprises
 *   path this file used before is dead, it returned no `results`, so name search always
 *   fell through to an error. Fixed by making recherche-entreprises the primary path.)
 *
 * OPTIONAL ENRICHMENT (needs a free token): the full INPI RNE API adds balance-sheet depth
 *   (total assets, equity) that the open dataset omits. Set INPI_API_TOKEN in keys.json to
 *   enable; without it we still return revenue + earnings + officers + metadata.
 *
 * Usage:
 *   node fr-inpi.js search  "Company Name"
 *   node fr-inpi.js company <siren>
 *   node fr-inpi.js accounts <siren>
 *   node fr-inpi.js analyze <siren|Company Name>
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

// Keys come from an env var or a local config/keys.json (git-ignored). Never hardcode.
const KEYS_PATH = process.env.COMPANY_REGISTERS_KEYS ||
  path.join(__dirname, '..', 'config', 'keys.json');
let config = {};
try {
  config = JSON.parse(fs.readFileSync(KEYS_PATH, 'utf8'));
} catch (e) {
  // No config file, env vars are used instead.
}
const API_TOKEN = config.INPI_API_TOKEN || process.env.INPI_API_TOKEN;

const SEARCH_HOST = 'recherche-entreprises.api.gouv.fr';
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ' +
  '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

/** GET JSON with a browser UA + light retry on transient network resets. */
function getJson(hostname, pathname, retries = 3) {
  return new Promise((resolve, reject) => {
    const attempt = (n) => {
      const req = https.request({
        hostname, port: 443, path: pathname, method: 'GET',
        headers: { 'Accept': 'application/json', 'User-Agent': UA },
      }, (res) => {
        let data = '';
        res.on('data', (c) => (data += c));
        res.on('end', () => {
          if (res.statusCode === 200) {
            try { resolve(JSON.parse(data)); }
            catch (e) { reject(new Error(`bad JSON from ${hostname}: ${e.message}`)); }
          } else if (res.statusCode === 404) {
            resolve(null);
          } else if (res.statusCode === 401) {
            reject(new Error('Unauthorized (token invalid/missing)'));
          } else {
            reject(new Error(`HTTP ${res.statusCode} from ${hostname}: ${data.slice(0, 160)}`));
          }
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

/** Latest year's revenue/earnings from the API's year-keyed `finances` object. */
function latestFinance(finances) {
  if (!finances || typeof finances !== 'object') return null;
  const years = Object.keys(finances).filter((y) => /^\d{4}$/.test(y)).sort();
  if (!years.length) return null;
  const y = years[years.length - 1];
  const f = finances[y] || {};
  return {
    fiscal_year: y,
    revenue: f.ca != null ? f.ca : null,        // chiffre d'affaires
    earnings: f.resultat_net != null ? f.resultat_net : null,
  };
}

/** All years of the `finances` object, newest first. */
function allFinances(finances) {
  if (!finances || typeof finances !== 'object') return [];
  return Object.keys(finances)
    .filter((y) => /^\d{4}$/.test(y))
    .sort((a, b) => b - a)
    .map((y) => ({
      fiscal_year: y,
      revenue: finances[y].ca != null ? finances[y].ca : null,
      earnings: finances[y].resultat_net != null ? finances[y].resultat_net : null,
    }));
}

/** Compact one API result row into our shape. */
function mapResult(r) {
  const siege = r.siege || {};
  return {
    name: r.nom_complet || r.nom_raison_sociale || null,
    siren: r.siren || null,
    siret_siege: siege.siret || null,
    address: siege.adresse || [siege.numero_voie, siege.type_voie, siege.libelle_voie,
      siege.code_postal, siege.libelle_commune].filter(Boolean).join(' ') || null,
    activity: { code: r.activite_principale || null, label: r.section_activite_principale || null },
    legal_form: r.nature_juridique || null,
    employees_band: r.tranche_effectif_salarie || null,
    creation_date: r.date_creation || null,
    is_active: r.etat_administratif === 'A',
    officers: (r.dirigeants || []).map((d) => d.type_dirigeant === 'personne morale'
      ? { type: 'company', name: d.denomination || null, siren: d.siren || null, role: d.qualite || null }
      : { type: 'person', name: [d.prenoms, d.nom].filter(Boolean).join(' ') || null,
          role: d.qualite || null, birth_year: d.annee_de_naissance || null }),
    finance_latest: latestFinance(r.finances),
    finances: allFinances(r.finances),
  };
}

/** Name (or SIREN) search via the free government API. */
async function searchCompanies(query, limit = 20) {
  const resp = await getJson(SEARCH_HOST, `/search?q=${encodeURIComponent(query)}&per_page=${limit}`);
  const results = (resp && resp.results) || [];
  const companies = results.map(mapResult);
  return {
    found: companies.length > 0,
    searched_name: query,
    total_results: resp ? resp.total_results : 0,
    companies_count: companies.length,
    companies,
    source: 'recherche-entreprises.api.gouv.fr',
  };
}

/** Exact-SIREN lookup (falls back to first hit if the exact SIREN isn't in the page). */
async function getCompany(siren) {
  const clean = String(siren).replace(/\s/g, '');
  const resp = await getJson(SEARCH_HOST, `/search?q=${encodeURIComponent(clean)}&per_page=10`);
  const results = (resp && resp.results) || [];
  const hit = results.find((c) => c.siren === clean) || results[0];
  if (!hit) return { found: false, siren: clean, error: 'Company not found' };
  return { found: true, ...mapResult(hit) };
}

/**
 * Financial accounts. Free path: the `finances` block already fetched above. If an
 * INPI_API_TOKEN is configured we additionally try the RNE bilans API for balance-sheet
 * depth (total assets / equity), best-effort, guarded, never fatal.
 */
async function getAccounts(siren) {
  const clean = String(siren).replace(/\s/g, '');
  const company = await getCompany(clean);
  if (!company.found) return { found: false, siren: clean, error: 'Company not found' };

  const out = {
    found: true, siren: clean, company_name: company.name,
    accounts: company.finances,                 // [{fiscal_year, revenue, earnings}, ...]
    source: 'recherche-entreprises.api.gouv.fr',
    balance_sheet: null,
  };

  if (API_TOKEN) {
    try {
      // RNE (INPI) bilans, schema varies; map defensively.
      const bilans = await new Promise((resolve, reject) => {
        const req = https.request({
          hostname: 'registre-national-entreprises.inpi.fr', port: 443,
          path: `/api/companies/${clean}/attachments`, method: 'GET',
          headers: { 'Accept': 'application/json', 'User-Agent': UA, 'Authorization': `Bearer ${API_TOKEN}` },
        }, (res) => { let d = ''; res.on('data', (c) => d += c); res.on('end', () => {
          try { resolve(JSON.parse(d)); } catch (e) { resolve(null); } }); });
        req.on('error', reject); req.end();
      });
      if (bilans) out.inpi_attachments = Array.isArray(bilans.bilans) ? bilans.bilans.length : true;
    } catch (e) { out.inpi_note = `INPI enrichment failed: ${e.message}`; }
  } else {
    out.note = 'Balance-sheet depth (total assets/equity) needs a free INPI_API_TOKEN; ' +
      'revenue + earnings are included free above.';
  }
  return out;
}

/** Pick the best candidate for a name query: exact name > has-revenue > active > API order. */
function pickBest(query, companies) {
  const norm = (s) => (s || '').toLowerCase().replace(/\s*\(.*?\)\s*/g, ' ').replace(/[^a-z0-9]+/g, ' ').trim();
  const nq = norm(query);
  let best = null, bestScore = -1;
  companies.forEach((c, i) => {
    const n = norm(c.name);
    let score = 0;
    if (n === nq) score += 100;
    else if (n.startsWith(nq)) score += 40;
    else if (n.includes(nq)) score += 20;
    if (c.finance_latest && c.finance_latest.revenue) score += 30;
    if (c.is_active) score += 10;
    score += Math.max(0, 10 - i); // gentle nudge toward the API's own ranking
    if (score > bestScore) { bestScore = score; best = c; }
  });
  return best;
}

/** Unified analyze, accepts a SIREN (9 digits) or a company name. */
async function analyzeCompany(input) {
  const clean = String(input).replace(/\s/g, '');
  let company;
  if (/^\d{9}$/.test(clean)) {
    company = await getCompany(clean);
  } else {
    const s = await searchCompanies(input, 20);
    const best = s.companies.length ? pickBest(input, s.companies) : null;
    company = best ? { found: true, ...best } : { found: false };
  }

  if (!company.found) {
    return { company_name: null, country: 'fr', registration_id: clean, found: false, error: 'Company not found' };
  }

  const fin = company.finance_latest;
  return {
    company_name: company.name,
    country: 'fr',
    registration_id: company.siren,
    siret: company.siret_siege,
    found: true,
    address: company.address,
    activity: company.activity,
    legal_form: company.legal_form,
    employees_band: company.employees_band,
    creation_date: company.creation_date,
    is_active: company.is_active,
    officers: company.officers,
    financial_data: fin ? {
      revenue: fin.revenue,
      total_assets: null,        // free dataset omits it; needs INPI token
      earnings: fin.earnings,
      fiscal_year: fin.fiscal_year,
      currency: 'EUR',
    } : null,
    financial_history: company.finances,
    source: 'recherche-entreprises.api.gouv.fr',
    note: company.finances.length ? null
      : 'No financials published for this entity (common for holdings / small SARL). Metadata + officers only.',
  };
}

// CLI
async function main() {
  const args = process.argv.slice(2);
  if (args.length < 2) {
    console.log(`Usage:
  node fr-inpi.js search  "Company Name"
  node fr-inpi.js company <siren>
  node fr-inpi.js accounts <siren>
  node fr-inpi.js analyze <siren | "Company Name">

Examples:
  node fr-inpi.js search  "Carrefour"
  node fr-inpi.js analyze 652014051
  node fr-inpi.js analyze "Danone"

Free path (no key) returns revenue + earnings + officers + metadata.
An optional free INPI_API_TOKEN (keys.json) adds balance-sheet depth.`);
    process.exit(1);
  }
  const [command, arg] = args;
  let result;
  switch (command) {
    case 'search':   result = await searchCompanies(arg); break;
    case 'company':  result = await getCompany(arg); break;
    case 'accounts': result = await getAccounts(arg); break;
    case 'analyze':  result = await analyzeCompany(arg); break;
    default: console.error(`Unknown command: ${command}`); process.exit(1);
  }
  console.log(JSON.stringify(result, null, 2));
}

module.exports = { searchCompanies, getCompany, getAccounts, analyzeCompany, latestFinance, allFinances };

if (require.main === module) {
  main().catch((e) => { console.error('Error:', e.message); process.exit(1); });
}
