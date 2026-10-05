#!/usr/bin/env node
/**
 * German Unternehmensregister (unternehmensregister.de) scraper, LISTING path.
 *
 * WHY THIS EXISTS (the crossover the Bundesanzeiger scraper misses):
 *   By the DiRUG reform, the *publication* of Jahresabschlüsse for fiscal years
 *   beginning after 31.12.2021 moved FROM the Bundesanzeiger TO the
 *   Unternehmensregister. So the Bundesanzeiger scraper caps out at GJ 2021 for
 *   most companies; GJ 2022+ lives ONLY here. Each result carries a `sourceName`
 *   ("Unternehmensregister" vs "Bundesanzeiger"/"Elektronischer Bundesanzeiger")
 *   so the two sources can be merged without double-counting.
 *
 * HOW IT WORKS (fast, no browser, no CAPTCHA):
 *   The site is a Next.js App-Router SPA, but the initial HTML is server-rendered:
 *   the search results are embedded as React-Server-Component "flight" chunks
 *   (`self.__next_f.push([1,"..."])`). We
 *     1. GET /api/search-token           -> a short-lived search token
 *     2. GET /de/suche?...&searchToken=  -> full HTML with the flight payload
 *     3. decode the flight stream, pull the `elasticSearchDtos` array(s) and parse
 *        the company + publication DTOs as plain JSON.
 *   No CAPTCHA is involved in listing. (Retrieving the actual PDF *document* behind
 *   a publication, encryptedPayload, is a separate, partly paid step and is NOT
 *   done here.)
 *
 * Usage:
 *   node de-unternehmensregister.js search "Company Name" [--pages N] [--all] [--json]
 *   node de-unternehmensregister.js token         # debug: print a fresh search token
 */

const https = require('https');
const fs = require('fs');
const os = require('os');
const path = require('path');

const BASE = 'https://www.unternehmensregister.de';
const TOKEN_CACHE = path.join(os.tmpdir(), 'ur_search_token.json');
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ' +
  '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const PER_PAGE = 30; // the UR returns 30 result rows per `from` offset

/** GET with a browser-like UA + light retry on transient network resets. */
function httpGet(url, headers = {}, retries = 4) {
  return new Promise((resolve, reject) => {
    const attempt = (n) => {
      const u = new URL(url);
      const req = https.request({
        hostname: u.hostname,
        path: u.pathname + u.search,
        method: 'GET',
        headers: {
          'User-Agent': UA,
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8',
          'Connection': 'keep-alive',
          ...headers,
        },
      }, (res) => {
        // Follow redirects (rare here, but be safe).
        if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          const next = new URL(res.headers.location, url).href;
          res.resume();
          return resolve(httpGet(next, headers, retries));
        }
        let data = '';
        res.on('data', (c) => (data += c));
        res.on('end', () => resolve({ status: res.statusCode, body: data }));
      });
      req.on('error', (e) => {
        if (n < retries && /ECONNRESET|EPIPE|ETIMEDOUT|EAI_AGAIN|socket hang up/i.test(e.message)) {
          setTimeout(() => attempt(n + 1), 400 * (n + 1));
        } else {
          reject(e);
        }
      });
      req.end();
    };
    attempt(0);
  });
}

/**
 * Fetch a search token required by the /de/suche endpoint. Tokens are valid ~8 h, so we
 * cache the latest one to a temp file and reuse it (with a 5-min safety margin) to skip a
 * ~150 ms round-trip on every subsequent call. Set UR_NO_TOKEN_CACHE=1 to disable.
 */
async function getSearchToken() {
  if (!process.env.UR_NO_TOKEN_CACHE) {
    try {
      const c = JSON.parse(fs.readFileSync(TOKEN_CACHE, 'utf8'));
      if (c.token && c.expiresAt && c.expiresAt - Date.now() > 5 * 60 * 1000) return c.token;
    } catch (e) { /* no/stale cache */ }
  }
  const res = await httpGet(`${BASE}/api/search-token`, {
    'Accept': 'application/json,*/*',
    'Referer': `${BASE}/de/suche?areas=all`,
  });
  if (res.status !== 200) throw new Error(`search-token HTTP ${res.status}`);
  const parsed = JSON.parse(res.body);
  if (!parsed.token) throw new Error('search-token: no token in response');
  try {
    fs.writeFileSync(TOKEN_CACHE, JSON.stringify({ token: parsed.token, expiresAt: parsed.expiresAt || 0 }));
  } catch (e) { /* cache write best-effort */ }
  return parsed.token;
}

/**
 * Decode the Next.js flight stream: concatenate every
 * `self.__next_f.push([1,"<js-string>"])` payload, unescaping each JS string
 * literal back into the raw RSC text (which embeds the DTO JSON verbatim).
 */
function decodeFlight(html) {
  const re = /self\.__next_f\.push\(\[1,\s*"((?:[^"\\]|\\.)*)"\]\)/g;
  let m, stream = '';
  while ((m = re.exec(html)) !== null) {
    try { stream += JSON.parse('"' + m[1] + '"'); } catch (e) { /* skip malformed chunk */ }
  }
  return stream;
}

/**
 * From a string, extract every balanced JSON array that immediately follows the
 * given key (e.g. `"elasticSearchDtos":[ ... ]`), string/escape aware.
 */
function extractArraysAfterKey(text, key) {
  const marker = `"${key}":[`;
  const out = [];
  let searchFrom = 0;
  while (true) {
    const at = text.indexOf(marker, searchFrom);
    if (at === -1) break;
    const start = at + marker.length - 1; // position of '['
    let depth = 0, inStr = false, esc = false, end = -1;
    for (let i = start; i < text.length; i++) {
      const c = text[i];
      if (inStr) {
        if (esc) { esc = false; continue; }
        if (c === '\\') { esc = true; continue; }
        if (c === '"') inStr = false;
        continue;
      }
      if (c === '"') { inStr = true; continue; }
      if (c === '[') depth++;
      else if (c === ']') { depth--; if (depth === 0) { end = i; break; } }
    }
    if (end === -1) break;
    out.push(text.slice(start, end + 1));
    searchFrom = end + 1;
  }
  return out;
}

/** "Jahresabschluss zum Geschäftsjahr vom 01.01.2024 bis zum 31.12.2024" -> "2024". */
function fiscalYearFromTitle(title) {
  if (!title) return null;
  // Prefer the "bis zum DD.MM.YYYY" end date, else the last 4-digit year in the title.
  const bis = title.match(/bis(?:\s+zum)?\s+\d{2}\.\d{2}\.(\d{4})/i);
  if (bis) return bis[1];
  const zum = title.match(/zum\s+\d{2}\.\d{2}\.(\d{4})/i);
  if (zum) return zum[1];
  const years = title.match(/\b(19|20)\d{2}\b/g);
  return years ? years[years.length - 1] : null;
}

/** Normalise a sourceName to a compact tag. */
function sourceTag(name) {
  if (!name) return 'unknown';
  if (/unternehmensregister/i.test(name)) return 'unternehmensregister';
  if (/bundesanzeiger/i.test(name)) return 'bundesanzeiger';
  return name;
}

/**
 * Parse one page of UR search HTML into { companies:{euid->company}, publications:[] }.
 * Companies (1-company) and publications (2-publication) arrive as a flat DTO list;
 * publications are linked to companies by (companyName, location) since a publication
 * DTO doesn't carry the company's euid.
 */
function parsePage(html) {
  const stream = decodeFlight(html);
  const arrays = extractArraysAfterKey(stream, 'elasticSearchDtos');
  const companies = [];
  const publications = [];
  for (const arrStr of arrays) {
    let dtos;
    try { dtos = JSON.parse(arrStr); } catch (e) { continue; }
    for (const dto of dtos) {
      if (dto.entityType === '1-company' && dto.companyDto) {
        const c = dto.companyDto;
        // EUID's last segment concatenates register type + number, e.g.
        // "DER3306.HRB37497" -> seg "HRB37497", type "HRB", number "37497".
        const seg = (c.euid || '').split('.').pop() || '';
        const rtName = c.registerType ? (c.registerType.name || '') : '';
        const num = rtName && seg.toUpperCase().startsWith(rtName.toUpperCase())
          ? seg.slice(rtName.length) : seg;
        companies.push({
          name: c.name || null,
          location: c.location || null,
          euid: c.euid || null,
          register: rtName ? `${rtName} ${num}`.trim() : (seg || null),
          register_number: num || null,
          court: c.registerCourt ? c.registerCourt.name : null,
          state: c.state ? c.state.name : null,
          encrypted_id: c.encryptedId || null,
        });
      } else if (dto.entityType === '2-publication' && dto.publicationDto) {
        const p = dto.publicationDto;
        publications.push({
          company: p.companyNameAtTimeOfPublication || null,
          location: p.companyLocation || null,
          name: p.title || null,
          fiscal_year: fiscalYearFromTitle(p.title),
          date: p.sourceDate || null,
          source: sourceTag(p.sourceName),
          source_raw: p.sourceName || null,
          category: p.publicationCategory ? p.publicationCategory.i18n_key : null,
          encrypted_payload: p.encryptedPayload || null,
        });
      }
    }
  }
  // total result count, if the flight exposes it
  const totalMatch = stream.match(/"(?:totalHits|numberOfResults|totalCount|hits)":\s*(\d+)/);
  const total = totalMatch ? parseInt(totalMatch[1], 10) : null;
  return { companies, publications, total };
}

/** Group publications under their company (by name+location), keep company metadata. */
function groupByCompany(companies, publications) {
  const key = (name, loc) => `${(name || '').toLowerCase().trim()}|${(loc || '').toLowerCase().trim()}`;
  const map = new Map();

  for (const c of companies) {
    map.set(key(c.name, c.location), { ...c, reports: [] });
  }
  for (const p of publications) {
    const k = key(p.company, p.location);
    if (!map.has(k)) {
      // publication whose company row wasn't in this page, synthesise a stub
      map.set(k, {
        name: p.company, location: p.location, euid: null, register: null,
        register_number: null, court: null, state: null, encrypted_id: null, reports: [],
      });
    }
    map.get(k).reports.push({
      name: p.name,
      fiscal_year: p.fiscal_year,
      date: p.date,
      source: p.source,
      source_raw: p.source_raw,
      encrypted_payload: p.encrypted_payload,
    });
  }

  // Sort each company's reports newest fiscal year first, then by date desc.
  for (const co of map.values()) {
    co.reports.sort((a, b) => {
      const fy = (parseInt(b.fiscal_year, 10) || 0) - (parseInt(a.fiscal_year, 10) || 0);
      if (fy !== 0) return fy;
      return String(b.date || '').localeCompare(String(a.date || ''));
    });
  }
  return [...map.values()];
}

/**
 * Search the Unternehmensregister for a company name.
 * opts.pages: how many 30-row pages to fetch (default 1). opts.all: fetch until exhausted (cap 7).
 */
async function searchUR(companyName, opts = {}) {
  const token = await getSearchToken();
  // 1 page (30 rows) holds a precise-name company's full report history, verified. Only
  // fuzzy/multi-company discovery needs more, via opts.deep (or the legacy opts.all).
  const maxPages = (opts.deep || opts.all) ? 7 : Math.max(1, opts.pages || 1);

  const q = encodeURIComponent(companyName);
  const pageUrl = (from) =>
    `${BASE}/de/suche?areas=all&companySearchTerm=${q}&companyName=${q}&searchToken=${token}&from=${from}`;

  // First page.
  const first = await httpGet(pageUrl(0), { 'Referer': `${BASE}/de/suche?areas=all` });
  if (first.status !== 200) throw new Error(`UR search HTTP ${first.status}`);
  let { companies, publications, total } = parsePage(first.body);

  // Additional pages in parallel (only if requested and there is more).
  const totalPages = total ? Math.min(maxPages, Math.ceil(total / PER_PAGE)) : maxPages;
  if (totalPages > 1) {
    const froms = [];
    for (let p = 1; p < totalPages; p++) froms.push(p * PER_PAGE);
    const pages = await Promise.all(
      froms.map((f) => httpGet(pageUrl(f), { 'Referer': `${BASE}/de/suche?areas=all` })
        .then((r) => (r.status === 200 ? parsePage(r.body) : { companies: [], publications: [] }))
        .catch(() => ({ companies: [], publications: [] })))
    );
    for (const pg of pages) {
      companies = companies.concat(pg.companies);
      publications = publications.concat(pg.publications);
    }
  }

  const grouped = groupByCompany(companies, publications)
    // Keep only companies that actually have financial publications, most-reports first.
    .filter((c) => c.reports.length > 0)
    .sort((a, b) => b.reports.length - a.reports.length);

  return {
    found: grouped.length > 0,
    searched_name: companyName,
    source: 'unternehmensregister',
    total_hits: total,
    pages_fetched: totalPages,
    companies_count: grouped.length,
    companies: grouped,
  };
}

// CLI
async function main() {
  const args = process.argv.slice(2);
  const command = args[0];
  const companyName = args[1];

  if (command === 'token') {
    console.log(await getSearchToken());
    return;
  }

  if (command !== 'search' || !companyName) {
    console.log(`Usage:
  node de-unternehmensregister.js search "Company Name" [--pages N] [--all] [--json]
  node de-unternehmensregister.js token`);
    process.exit(command ? 1 : 0);
  }

  const pagesFlag = args.indexOf('--pages');
  const pages = pagesFlag !== -1 ? parseInt(args[pagesFlag + 1], 10) : 1;
  const all = args.includes('--all');

  const result = await searchUR(companyName, { pages, all });
  // Flush then exit hard so lingering keep-alive sockets don't hold the process ~5 s.
  process.stdout.write(JSON.stringify(result, null, 2) + '\n', () => process.exit(0));
}

module.exports = { searchUR, getSearchToken, parsePage, fiscalYearFromTitle, sourceTag };

if (require.main === module) {
  main().catch((e) => { console.error('Error:', e.message); process.exit(1); });
}
