#!/usr/bin/env node
/**
 * German Bundesanzeiger Company Register Scraper
 *
 * Searches the German Federal Gazette (Bundesanzeiger) for company financial reports
 * and extracts revenue, assets, and earnings using AI.
 *
 * Usage:
 *   node de-bundesanzeiger.js search "Company Name"
 *   node de-bundesanzeiger.js analyze "Company Name" [--index N]
 */

const https = require('https');
const http = require('http');
const fs = require('fs');
const os = require('os');
const path = require('path');
const { spawnSync, spawn } = require('child_process');

// The two LLM steps, reading the Bundesanzeiger CAPTCHA (vision) and extracting the
// financial figures from the report text, run on Claude via the local `claude` CLI
// (headless, native OAuth from ~/.claude/.credentials.json). No OpenRouter, no API key.
const HOME = process.env.HOME || process.env.USERPROFILE || '';
const CLAUDE_BIN = process.env.CLAUDE_BIN ||
  (HOME && fs.existsSync(path.join(HOME, '.local/bin/claude'))
    ? path.join(HOME, '.local/bin/claude')
    : 'claude');

// Cheap vision model for the CAPTCHA; a stronger model for the financial extraction.
// Override via env if the model ids change.
const CAPTCHA_MODEL = process.env.BA_CAPTCHA_MODEL || 'claude-haiku-4-5-20251001';
const EXTRACT_MODEL = process.env.BA_EXTRACT_MODEL || 'claude-sonnet-5';

const TMP = os.tmpdir();

// Session state
let sessionCookies = {};

/**
 * Call the local `claude` CLI (headless, native OAuth, no API key). Returns trimmed
 * stdout, or null on failure. Never inherits ANTHROPIC_* (that would override the
 * subscription auth and hang claude).
 *   opts.stdin      text piped to claude on stdin (used as context)
 *   opts.allowRead  allow the Read tool (needed for image/vision prompts)
 *   opts.timeoutMs  hard timeout (default 120s)
 */
function runClaude(prompt, model, opts = {}) {
  const args = ['-p', prompt, '--model', model, '--output-format', 'text'];
  if (opts.allowRead) {
    args.push('--allowedTools', 'Read', '--max-turns', '6');
  } else {
    args.push('--max-turns', '1');
  }
  const env = { ...process.env };
  delete env.ANTHROPIC_API_KEY;
  delete env.ANTHROPIC_BASE_URL;
  const res = spawnSync(CLAUDE_BIN, args, {
    input: opts.stdin || undefined,
    encoding: 'utf8',
    maxBuffer: 64 * 1024 * 1024,
    timeout: opts.timeoutMs || 120000,
    env
  });
  if (res.error) {
    console.error('claude CLI error:', res.error.message);
    return null;
  }
  if (res.status !== 0) {
    console.error('claude CLI exited', res.status, (res.stderr || '').trim().slice(0, 300));
    return null;
  }
  return (res.stdout || '').trim();
}

/**
 * Solve a CAPTCHA image with Claude (Haiku vision) via the local claude CLI.
 * Writes the image to a temp file and asks Claude to read the characters.
 */
function solveCaptcha(imageBuffer) {
  const imgPath = path.join(TMP, `ba_captcha_${process.pid}.png`);
  fs.writeFileSync(imgPath, imageBuffer);

  const prompt = `Read the CAPTCHA in the image file ${imgPath} . It contains about 6 ` +
    `distorted letters/digits. Output ONLY those characters, no words, no sentence, ` +
    `no punctuation, no quotes, no explanation. If unsure, give your single best guess.`;

  const out = runClaude(prompt, CAPTCHA_MODEL, { allowRead: true, timeoutMs: 90000 });
  try { fs.unlinkSync(imgPath); } catch (e) { /* ignore */ }
  if (!out) return null;

  // Pick a captcha-like token: alphanumeric runs of length 4-8; prefer the last run
  // that has a digit or is all-caps (real codes look like "VF22ER"/"BMUFFG", not a
  // narrated word like "Please"), else the last run, else the whole stripped output.
  // Bundesanzeiger CAPTCHAs are ~6 chars.
  const runs = out.match(/[A-Za-z0-9]{4,8}/g) || [];
  let pick = null;
  for (const r of runs) {
    if (/[0-9]/.test(r) || r === r.toUpperCase()) pick = r;
  }
  if (!pick) pick = runs.length ? runs[runs.length - 1] : out.replace(/[^A-Za-z0-9]/g, '');
  let content = pick.trim();
  if (content.length > 6) content = content.substring(0, 6);
  return content || null;
}

/**
 * Make an HTTPS request with proper headers and redirect following.
 * Retries on transient network resets, the Bundesanzeiger intermittently drops the
 * connection ("socket hang up" / ECONNRESET), especially on the CAPTCHA POST; a short
 * retry clears it.
 */
async function makeRequest(url, options = {}, redirectCount = 0) {
  const MAX_NET_RETRIES = 5;
  let lastErr;
  for (let attempt = 0; attempt <= MAX_NET_RETRIES; attempt++) {
    try {
      return await _doRequest(url, options, redirectCount);
    } catch (e) {
      lastErr = e;
      const msg = (e && e.message) || '';
      if (/socket hang up|ECONNRESET|EPIPE|ETIMEDOUT|EAI_AGAIN|ECONNREFUSED/i.test(msg) && attempt < MAX_NET_RETRIES) {
        await new Promise(r => setTimeout(r, 500 * (attempt + 1)));
        continue;
      }
      throw e;
    }
  }
  throw lastErr;
}

function _doRequest(url, options = {}, redirectCount = 0) {
  const MAX_REDIRECTS = 10;

  return new Promise((resolve, reject) => {
    if (redirectCount >= MAX_REDIRECTS) {
      reject(new Error('Too many redirects'));
      return;
    }

    const urlObj = new URL(url);
    const isHttps = urlObj.protocol === 'https:';
    const lib = isHttps ? https : http;

    const cookieString = Object.entries(sessionCookies)
      .map(([k, v]) => `${k}=${v}`)
      .join('; ');

    const reqOptions = {
      hostname: urlObj.hostname,
      port: urlObj.port || (isHttps ? 443 : 80),
      path: urlObj.pathname + urlObj.search,
      method: options.method || 'GET',
      headers: {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'identity',
        'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': urlObj.hostname,
        'Referer': 'https://www.bundesanzeiger.de/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        ...(cookieString && { 'Cookie': cookieString }),
        ...options.headers
      }
    };

    const req = lib.request(reqOptions, (res) => {
      // Store cookies from response
      const setCookies = res.headers['set-cookie'] || [];
      for (const cookie of setCookies) {
        const [nameValue] = cookie.split(';');
        const [name, value] = nameValue.split('=');
        if (name && value) {
          sessionCookies[name.trim()] = value.trim();
        }
      }

      // Handle redirects
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        let redirectUrl = res.headers.location;
        // Handle relative URLs
        if (redirectUrl.startsWith('/')) {
          redirectUrl = `${urlObj.protocol}//${urlObj.host}${redirectUrl}`;
        } else if (!redirectUrl.startsWith('http')) {
          redirectUrl = new URL(redirectUrl, url).href;
        }
        // Follow redirect
        resolve(makeRequest(redirectUrl, options, redirectCount + 1));
        return;
      }

      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve({ status: res.statusCode, headers: res.headers, body: data }));
    });

    req.on('error', reject);

    if (options.body) {
      req.write(options.body);
    }

    req.end();
  });
}

/**
 * Initialize session with Bundesanzeiger
 */
async function initSession() {
  sessionCookies = { 'cc': '1628606977-805e172265bfdbde-10' };

  // Get JSESSIONID
  await makeRequest('https://www.bundesanzeiger.de');
  await makeRequest('https://www.bundesanzeiger.de/pub/de/start?0');
}

/**
 * Parse search results HTML
 */
function parseSearchResults(html) {
  const results = [];

  // Find result container - new structure uses "result_container global-search"
  const containerMatch = html.match(/<div class="container result_container[^"]*">([\s\S]*?)<\/div>\s*<div class="result_pager/);
  if (!containerMatch) {
    // Try alternative ending
    const altMatch = html.match(/<div class="container result_container[^"]*">([\s\S]*)/);
    if (!altMatch) return results;
    return parseResultRows(altMatch[1]);
  }

  return parseResultRows(containerMatch[1]);
}

/**
 * Parse individual result rows
 */
function parseResultRows(html) {
  const results = [];

  // Find all rows - they can be "row" or "row back"
  const rowRegex = /<div class="row(?:\s+back)?">\s*<div class="col-md-3">([\s\S]*?)<\/div>\s*<\/div>\s*(?=<div class="row|<div class="result_pager|$)/g;
  let rowMatch;

  while ((rowMatch = rowRegex.exec(html)) !== null) {
    const fullRow = rowMatch[0];

    // Check if it's a financial report (Rechnungslegung/Finanzberichte)
    const partMatch = fullRow.match(/<div class="part">\s*([\s\S]*?)\s*<\/div>/);
    const part = partMatch ? partMatch[1].replace(/<br\/?>/g, '').replace(/\s+/g, ' ').trim() : '';

    if (!part.includes('Rechnungslegung') && !part.includes('Finanzberichte')) {
      continue;
    }

    // Extract company name from "first" div
    const companyMatch = fullRow.match(/<div class="first">\s*([\s\S]*?)\s*<br/);
    let companyName = '';
    if (companyMatch) {
      companyName = companyMatch[1].replace(/<[^>]+>/g, '').trim();
    }

    // Extract report info from "info" div
    const linkMatch = fullRow.match(/<div class="info">\s*<a href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/);
    const reportUrl = linkMatch ? linkMatch[1] : '';
    const reportName = linkMatch ? linkMatch[2].replace(/<[^>]+>/g, '').trim() : '';

    // Extract date
    const dateMatch = fullRow.match(/<div class="date">\s*([\d.]+)\s*<\/div>/);
    const date = dateMatch ? dateMatch[1] : '';

    if (companyName && reportUrl) {
      results.push({
        company: companyName,
        report_name: reportName,
        report_url: reportUrl,
        date: date,
        category: part
      });
    }
  }

  return results;
}

/**
 * Search for companies in Bundesanzeiger
 */
async function searchCompanies(companyName) {
  await initSession();

  const searchUrl = `https://www.bundesanzeiger.de/pub/de/start?0-2.-top%7Econtent%7Epanel-left%7Ecard-form=&fulltext=${encodeURIComponent(companyName)}&area_select=&search_button=Suchen`;
  const response = await makeRequest(searchUrl);

  const results = parseSearchResults(response.body);

  // Group by company
  const companies = {};
  for (const result of results) {
    if (!companies[result.company]) {
      companies[result.company] = {
        name: result.company,
        reports: []
      };
    }
    companies[result.company].reports.push({
      name: result.report_name,
      url: result.report_url,
      date: result.date
    });
  }

  return {
    found: Object.keys(companies).length > 0,
    searched_name: companyName,
    companies_count: Object.keys(companies).length,
    companies: Object.values(companies)
  };
}

/**
 * Clean HTML by stripping tags and entities
 */
function cleanHtml(html) {
  return html
    .replace(/<!--[\s\S]*?-->/g, '')                       // HTML comments
    .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
    .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
    .replace(/<(?:head|nav|footer|header|noscript)[^>]*>[\s\S]*?<\/(?:head|nav|footer|header|noscript)>/gi, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#(\d+);/g, (_, n) => String.fromCharCode(+n))       // numeric entities
    .replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCharCode(parseInt(h, 16)))
    .replace(/[ \t ]+/g, ' ')                          // collapse spaces (keep newlines)
    .replace(/\s*\n\s*\n\s*/g, '\n')                        // collapse blank-line runs
    .replace(/\n{2,}/g, '\n')
    .trim();
}

/**
 * Extract the report text from the Bundesanzeiger HTML, then hand it to the extractor.
 * Tries the tightest selector first (just the report body, minimal noise for the LLM) and
 * falls back progressively; the last resort is the whole cleaned page so a layout change
 * never yields 0 characters. Returns null only if the page is genuinely empty.
 */
function extractReportText(html) {
  const MIN = 200; // below this the match is almost certainly a mis-hit → try the next strategy
  const strategies = [
    // 1. tightest: the publication content block up to the pager
    () => (html.match(/<div[^>]*class="publicationcontent[^"]*"[^>]*>([\s\S]*?)<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<div class="result_pager/) || [])[1],
    // 2. the begin_pub table up to the pager
    () => (html.match(/<table id="begin_pub">([\s\S]*?)<div class="result_pager/) || [])[1],
    // 3. publication content block, greedy to end of page
    () => (html.match(/<div[^>]*class="publicationcontent[^"]*"[^>]*>([\s\S]*)/) || [])[1],
    // 4. last resort: the whole page (cleanHtml drops head/nav/footer/script/style)
    () => html,
  ];
  let best = '';
  for (const s of strategies) {
    let raw;
    try { raw = s(); } catch (e) { raw = null; }
    if (!raw) continue;
    const txt = cleanHtml(raw);
    if (txt.length >= MIN) return txt;      // good enough, minimal noise, done
    if (txt.length > best.length) best = txt; // remember the longest short match
  }
  return best || null;                       // never spam, but never silently return nothing
}

/**
 * Check if CAPTCHA is needed and try to solve
 */
function needsCaptcha(html) {
  return html.includes('captcha_wrapper') && !html.includes('publication_container');
}

/**
 * Extract the first balanced {...} JSON object from a string.
 * Skips strings (handles escapes) so braces inside string values don't fool it.
 */
function extractFirstJsonObject(text) {
  const start = text.indexOf('{');
  if (start === -1) return null;
  let depth = 0;
  let inString = false;
  let escape = false;
  for (let i = start; i < text.length; i++) {
    const c = text[i];
    if (inString) {
      if (escape) { escape = false; continue; }
      if (c === '\\') { escape = true; continue; }
      if (c === '"') inString = false;
      continue;
    }
    if (c === '"') { inString = true; continue; }
    if (c === '{') depth++;
    else if (c === '}') {
      depth--;
      if (depth === 0) return text.substring(start, i + 1);
    }
  }
  return null;
}

// Shared extraction prompt, used identically by the sync and async runners so both the
// Bundesanzeiger and Unternehmensregister paths extract with the same schema.
const EXTRACT_PROMPT = `You are an accounting specialist focused on German financial reports. Extract financial data in EUR. Only respond with JSON.

Extract financial data from the German company report provided on standard input. Return ONLY a JSON object with these fields (all amounts in EUR, use null if not found):
- revenue (Umsatzerlöse)
- total_assets (Bilanzsumme/Summe Aktiva)
- earnings (Jahresüberschuss/Jahresfehlbetrag; negative if Fehlbetrag)
- inventory (Vorräte: Roh-/Hilfs-/Betriebsstoffe + unfertige + fertige Erzeugnisse + Waren, total)
- inventory_finished_goods (fertige Erzeugnisse und Waren, the sub-line if shown)
- receivables (Forderungen aus Lieferungen und Leistungen)
- cash (Kassenbestand/Guthaben bei Kreditinstituten)
- fixed_assets (Anlagevermögen total)
- equity (Eigenkapital)
- liabilities (Verbindlichkeiten total)
- gross_profit (Rohergebnis, if shown)
- material_expenses (Materialaufwand)
- personnel_expenses (Personalaufwand)
- operating_result (Betriebsergebnis/EBIT, if derivable)
- employees (durchschnittliche Zahl der Mitarbeiter, integer)
- fiscal_year (Geschäftsjahr end, e.g. "2022")
- is_group_report (true if Konzernabschluss/consolidated)

Use full EUR values (e.g. report stating "TEUR 1.234" -> 1234000). German number format uses "." for thousands and "," for decimals. Only return the JSON object, nothing else.`;

function _clampReport(reportText) {
  const maxLength = 100000;
  return reportText.length > maxLength ? reportText.substring(0, maxLength) + '...' : reportText;
}

function _parseExtract(out) {
  if (!out) {
    console.error('Warning: claude returned no output for extraction.');
    return { revenue: null, total_assets: null, earnings: null };
  }
  try {
    const content = out.replace(/```json\n?/g, '').replace(/```\n?/g, '').trim();
    const jsonStr = extractFirstJsonObject(content);
    if (!jsonStr) throw new Error('No JSON object found in response');
    const d = JSON.parse(jsonStr);
    return { ...d, revenue: d.revenue, total_assets: d.total_assets,
      earnings: d.earnings != null ? d.earnings : d.earnings_current_year, fiscal_year: d.fiscal_year };
  } catch (e) {
    console.error('Failed to parse Claude extraction response:', e.message);
    console.error('Raw:', out.substring(0, 500));
    return { revenue: null, total_assets: null, earnings: null };
  }
}

/** Extract financial figures from report text via Claude (blocking spawnSync). */
async function extractFinancialData(reportText) {
  const out = runClaude(EXTRACT_PROMPT, EXTRACT_MODEL, { stdin: `Report text:\n${_clampReport(reportText)}`, timeoutMs: 120000 });
  return _parseExtract(out);
}

/**
 * Async, non-blocking variant, spawns `claude` without blocking the event loop, so several
 * extractions can run concurrently via Promise.all (used to extract multiple UR years at once).
 */
function extractFinancialDataAsync(reportText) {
  return new Promise((resolve) => {
    const env = { ...process.env };
    delete env.ANTHROPIC_API_KEY;
    delete env.ANTHROPIC_BASE_URL;
    const cp = spawn(CLAUDE_BIN,
      ['-p', EXTRACT_PROMPT, '--model', EXTRACT_MODEL, '--output-format', 'text', '--max-turns', '1'],
      { env });
    let out = '';
    const timer = setTimeout(() => cp.kill('SIGKILL'), 120000);
    cp.stdout.on('data', (d) => (out += d));
    cp.stderr.on('data', () => {});
    cp.on('error', () => { clearTimeout(timer); resolve({ revenue: null, total_assets: null, earnings: null }); });
    cp.on('close', () => { clearTimeout(timer); resolve(_parseExtract(out.trim())); });
    cp.stdin.write(`Report text:\n${_clampReport(reportText)}`);
    cp.stdin.end();
  });
}

/**
 * Make binary request (for images)
 */
function makeBinaryRequest(url) {
  return new Promise((resolve, reject) => {
    const urlObj = new URL(url);
    const cookieString = Object.entries(sessionCookies)
      .map(([k, v]) => `${k}=${v}`)
      .join('; ');

    https.request({
      hostname: urlObj.hostname,
      port: 443,
      path: urlObj.pathname + urlObj.search,
      method: 'GET',
      headers: {
        'Accept': 'image/*',
        'Cookie': cookieString,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      }
    }, (res) => {
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => resolve(Buffer.concat(chunks)));
    }).on('error', reject).end();
  });
}

/**
 * Handle CAPTCHA challenge
 */
async function handleCaptcha(html) {
  // Extract CAPTCHA image URL
  const imgMatch = html.match(/<div class="captcha_wrapper"[^>]*>[\s\S]*?<img[^>]*src="([^"]+)"/);
  if (!imgMatch) {
    console.error('Could not find CAPTCHA image');
    return null;
  }

  let captchaUrl = imgMatch[1];
  if (!captchaUrl.startsWith('http')) {
    captchaUrl = 'https://www.bundesanzeiger.de' + captchaUrl;
  }

  console.error('Downloading CAPTCHA image...');
  const imageBuffer = await makeBinaryRequest(captchaUrl);

  console.error('Solving CAPTCHA with Claude (Haiku vision)...');
  const solution = solveCaptcha(imageBuffer);
  if (!solution) {
    console.error('Failed to solve CAPTCHA');
    return null;
  }
  console.error('CAPTCHA solution:', solution);

  // Find form action URL - look for forms where "captcha" is IN the action URL
  const formMatch = html.match(/<form[^>]*action="([^"]*captcha[^"]*)"/i);
  let formUrl = formMatch ? formMatch[1] : null;

  // Try alternative pattern - look for form with solution input
  if (!formUrl) {
    const altFormMatch = html.match(/<form[^>]*action="([^"]+)"[^>]*>[\s\S]*?name="solution"/i);
    formUrl = altFormMatch ? altFormMatch[1] : null;
  }

  if (!formUrl) {
    console.error('Could not find CAPTCHA form action');
    return null;
  }

  if (!formUrl.startsWith('http')) {
    formUrl = 'https://www.bundesanzeiger.de' + formUrl;
  }

  console.error('Form URL:', formUrl);

  // Submit CAPTCHA solution
  const postData = `solution=${encodeURIComponent(solution)}&confirm-button=OK`;
  console.error('POST data:', postData);
  const response = await makeRequest(formUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Content-Length': Buffer.byteLength(postData)
    },
    body: postData
  });

  return response;
}

/**
 * Fetch a Bundesanzeiger report page, solving the image CAPTCHA if present, and return the
 * cleaned report text (the full Jahresabschluss/Lagebericht body), or null on failure.
 *
 * Split out from analyzeReport so callers can KEEP the full text, not just the extracted figures:
 * the text is the raw material the combined runner now persists (see de-combined.js saveReportText).
 */
async function fetchReportText(reportUrl, maxRetries = 10) {
  let response = await makeRequest(reportUrl);
  let retries = 0;

  // Handle CAPTCHA if needed with retries
  while (needsCaptcha(response.body) && retries < maxRetries) {
    console.error(`CAPTCHA required, attempt ${retries + 1}/${maxRetries}...`);
    response = await handleCaptcha(response.body);

    if (!response) {
      console.error('Failed to process CAPTCHA');
      // Re-fetch the page to get a new CAPTCHA
      response = await makeRequest(reportUrl);
      retries++;
      continue;
    }

    // Check if we still have CAPTCHA (wrong solution)
    if (needsCaptcha(response.body)) {
      console.error('CAPTCHA solution was incorrect, retrying...');
      // Fetch page again to get new CAPTCHA
      response = await makeRequest(reportUrl);
      retries++;
    } else {
      // Success!
      break;
    }
  }

  if (needsCaptcha(response.body)) {
    console.error(`Failed to solve CAPTCHA after ${maxRetries} attempts`);
    return null;
  }

  const reportText = extractReportText(response.body);
  if (!reportText) {
    console.error('Could not extract report text');
    // Save response for debugging
    const debugPath = path.join(TMP, 'ba_debug_response.html');
    fs.writeFileSync(debugPath, response.body);
    console.error('Saved response to:', debugPath);
    return null;
  }

  console.error(`Extracted ${reportText.length} characters of report text`);
  return reportText;
}

/**
 * Get and analyze a specific report → financial figures (or null). Thin wrapper over
 * fetchReportText + the Claude extractor. `BA_DUMP_RAW` still dumps the raw text to that path.
 */
async function analyzeReport(reportUrl, maxRetries = 10) {
  const reportText = await fetchReportText(reportUrl, maxRetries);
  if (!reportText) return null;

  if (process.env.BA_DUMP_RAW) {
    fs.writeFileSync(process.env.BA_DUMP_RAW, reportText);
    console.error('Dumped raw report text to:', process.env.BA_DUMP_RAW);
    return { found: true, raw_dumped: process.env.BA_DUMP_RAW, report_chars: reportText.length };
  }
  const financialData = await extractFinancialData(reportText);
  return financialData;
}

/**
 * Analyze company - get financial data from latest report
 */
async function analyzeCompany(companyName, companyIndex = 0, reportIndex = 0) {
  // First search for the company
  const searchResults = await searchCompanies(companyName);

  if (!searchResults.found || searchResults.companies.length === 0) {
    return {
      company_name: companyName,
      country: 'de',
      found: false,
      error: 'Company not found in Bundesanzeiger'
    };
  }

  if (companyIndex >= searchResults.companies.length) {
    return {
      company_name: companyName,
      country: 'de',
      found: true,
      error: `Index ${companyIndex} out of range. Found ${searchResults.companies.length} companies: ${searchResults.companies.map((c, i) => `[${i}] ${c.name}`).join(', ')}`
    };
  }

  // Get the selected company's latest report
  const company = searchResults.companies[companyIndex];
  const latestReport = company.reports[reportIndex];

  if (!latestReport) {
    return {
      company_name: company.name,
      country: 'de',
      found: true,
      error: 'No financial reports found'
    };
  }

  console.error(`Analyzing report: ${latestReport.name} (${latestReport.date})`);

  const financialData = await analyzeReport(latestReport.url);

  return {
    company_name: company.name,
    country: 'de',
    registration_id: null, // Bundesanzeiger doesn't expose HRB directly
    found: true,
    financial_data: financialData ? {
      ...financialData,
      currency: 'EUR'
    } : null,
    report_date: latestReport.date,
    report_name: latestReport.name,
    source: 'bundesanzeiger'
  };
}

// CLI
async function main() {
  const args = process.argv.slice(2);

  if (args.length < 2) {
    console.log(`Usage:
  node de-bundesanzeiger.js search "Company Name"
  node de-bundesanzeiger.js analyze "Company Name" [--index N]

Options:
  --index N    Select company from search results (0-based, default: 0)
    `);
    process.exit(1);
  }

  const command = args[0];
  const companyName = args[1];
  const indexFlag = args.indexOf('--index');
  const companyIndex = indexFlag !== -1 ? parseInt(args[indexFlag + 1], 10) : 0;
  const reportFlag = args.indexOf('--report');
  const reportIndex = reportFlag !== -1 ? parseInt(args[reportFlag + 1], 10) : 0;

  try {
    let result;

    switch (command) {
      case 'search':
        result = await searchCompanies(companyName);
        break;
      case 'analyze':
        result = await analyzeCompany(companyName, companyIndex, reportIndex);
        break;
      default:
        console.error(`Unknown command: ${command}`);
        process.exit(1);
    }

    console.log(JSON.stringify(result, null, 2));
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

// Exported so the combined DE runner can call the Bundesanzeiger path in-process
// (no extra `node` startup) and reuse the free CAPTCHA+Claude figure extractor.
module.exports = { searchCompanies, analyzeCompany, analyzeReport, fetchReportText, extractFinancialData, extractFinancialDataAsync };

if (require.main === module) {
  main();
}
