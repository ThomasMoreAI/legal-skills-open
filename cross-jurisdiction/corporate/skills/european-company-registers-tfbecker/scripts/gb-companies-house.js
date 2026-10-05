#!/usr/bin/env node
/**
 * UK Companies House API Client
 *
 * Free API access to UK company data including financial accounts.
 * API docs: https://developer.company-information.service.gov.uk/
 *
 * Usage:
 *   node gb-companies-house.js search "Company Name"
 *   node gb-companies-house.js company <company_number>
 *   node gb-companies-house.js filings <company_number>
 *   node gb-companies-house.js accounts <company_number>
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

const API_KEY = config.COMPANIES_HOUSE_API_KEY || process.env.COMPANIES_HOUSE_API_KEY;
const BASE_URL = 'api.company-information.service.gov.uk';

/**
 * Make API request to Companies House
 */
function apiRequest(endpoint) {
  return new Promise((resolve, reject) => {
    if (!API_KEY) {
      reject(new Error('COMPANIES_HOUSE_API_KEY not set. Get a free key at https://developer.company-information.service.gov.uk/'));
      return;
    }

    const auth = Buffer.from(`${API_KEY}:`).toString('base64');

    const options = {
      hostname: BASE_URL,
      port: 443,
      path: endpoint,
      method: 'GET',
      headers: {
        'Authorization': `Basic ${auth}`,
        'Accept': 'application/json'
      }
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        if (res.statusCode === 200) {
          try {
            resolve(JSON.parse(data));
          } catch (e) {
            reject(new Error(`Failed to parse response: ${e.message}`));
          }
        } else if (res.statusCode === 404) {
          resolve(null);
        } else if (res.statusCode === 401) {
          reject(new Error('Invalid API key'));
        } else if (res.statusCode === 429) {
          reject(new Error('Rate limit exceeded. Wait and retry.'));
        } else {
          reject(new Error(`API error: ${res.statusCode} - ${data}`));
        }
      });
    });

    req.on('error', reject);
    req.end();
  });
}

/**
 * Search for companies by name
 */
async function searchCompanies(query, limit = 20) {
  const endpoint = `/search/companies?q=${encodeURIComponent(query)}&items_per_page=${limit}`;
  const response = await apiRequest(endpoint);

  if (!response || !response.items) {
    return {
      found: false,
      searched_name: query,
      companies_count: 0,
      companies: []
    };
  }

  const companies = response.items.map(item => ({
    name: item.title,
    company_number: item.company_number,
    company_status: item.company_status,
    company_type: item.company_type,
    date_of_creation: item.date_of_creation,
    address: item.address_snippet
  }));

  return {
    found: companies.length > 0,
    searched_name: query,
    companies_count: companies.length,
    total_results: response.total_results,
    companies: companies
  };
}

/**
 * Get company profile by registration number
 */
async function getCompany(companyNumber) {
  const endpoint = `/company/${companyNumber}`;
  const company = await apiRequest(endpoint);

  if (!company) {
    return {
      found: false,
      company_number: companyNumber,
      error: 'Company not found'
    };
  }

  return {
    found: true,
    company_name: company.company_name,
    company_number: company.company_number,
    company_status: company.company_status,
    company_type: company.type,
    date_of_creation: company.date_of_creation,
    registered_office_address: company.registered_office_address,
    sic_codes: company.sic_codes,
    accounts: company.accounts ? {
      next_due: company.accounts.next_due,
      last_accounts: company.accounts.last_accounts,
      accounting_reference_date: company.accounts.accounting_reference_date
    } : null,
    confirmation_statement: company.confirmation_statement,
    has_charges: company.has_charges,
    has_insolvency_history: company.has_insolvency_history
  };
}

/**
 * Get filing history for a company
 */
async function getFilingHistory(companyNumber, category = null, limit = 25) {
  let endpoint = `/company/${companyNumber}/filing-history?items_per_page=${limit}`;
  if (category) {
    endpoint += `&category=${category}`;
  }

  const response = await apiRequest(endpoint);

  if (!response || !response.items) {
    return {
      found: false,
      company_number: companyNumber,
      filings: []
    };
  }

  const filings = response.items.map(item => ({
    type: item.type,
    description: item.description,
    date: item.date,
    category: item.category,
    barcode: item.barcode,
    links: item.links
  }));

  return {
    found: true,
    company_number: companyNumber,
    filings_count: filings.length,
    total_count: response.total_count,
    filings: filings
  };
}

/**
 * Get accounts filing (annual accounts contain financial data)
 */
async function getAccounts(companyNumber) {
  // Get filing history filtered to accounts
  const filings = await getFilingHistory(companyNumber, 'accounts', 5);

  if (!filings.found || filings.filings.length === 0) {
    return {
      found: false,
      company_number: companyNumber,
      error: 'No accounts filings found'
    };
  }

  // Get company info for context
  const company = await getCompany(companyNumber);

  // Note: Companies House API provides metadata about filings but not the actual
  // financial figures. To get actual numbers, you need to:
  // 1. Download the XBRL/iXBRL file and parse it, OR
  // 2. Use a third-party service like DataLedger

  return {
    found: true,
    company_name: company.found ? company.company_name : null,
    company_number: companyNumber,
    country: 'gb',
    accounts_info: company.found ? company.accounts : null,
    recent_filings: filings.filings.slice(0, 5),
    note: 'Companies House API provides filing metadata. For parsed financial figures (revenue, P&L), the XBRL files need to be downloaded and parsed separately.'
  };
}

/**
 * Analyze company - get available financial info
 */
async function analyzeCompany(companyNumber) {
  const company = await getCompany(companyNumber);

  if (!company.found) {
    return {
      company_name: null,
      country: 'gb',
      registration_id: companyNumber,
      found: false,
      error: 'Company not found'
    };
  }

  const accounts = await getAccounts(companyNumber);

  return {
    company_name: company.company_name,
    country: 'gb',
    registration_id: company.company_number,
    found: true,
    company_status: company.company_status,
    company_type: company.company_type,
    date_of_creation: company.date_of_creation,
    sic_codes: company.sic_codes,
    address: company.registered_office_address,
    financial_data: {
      // Note: Actual figures require XBRL parsing
      revenue: null,
      total_assets: null,
      earnings: null,
      fiscal_year: accounts.accounts_info?.last_accounts?.made_up_to,
      currency: 'GBP'
    },
    accounts_info: accounts.accounts_info,
    recent_accounts_filings: accounts.found ? accounts.recent_filings : [],
    source: 'companies-house',
    note: 'UK Companies House does not expose parsed financial figures via API. Values require XBRL file parsing.'
  };
}

// CLI
async function main() {
  const args = process.argv.slice(2);

  if (args.length < 2) {
    console.log(`Usage:
  node gb-companies-house.js search "Company Name"
  node gb-companies-house.js company <company_number>
  node gb-companies-house.js filings <company_number>
  node gb-companies-house.js accounts <company_number>
  node gb-companies-house.js analyze <company_number>

Examples:
  node gb-companies-house.js search "Tesco"
  node gb-companies-house.js company 00445790
  node gb-companies-house.js analyze 00445790

Note: Get a free API key at https://developer.company-information.service.gov.uk/
    `);
    process.exit(1);
  }

  const command = args[0];
  const arg = args[1];

  try {
    let result;

    switch (command) {
      case 'search':
        result = await searchCompanies(arg);
        break;
      case 'company':
        result = await getCompany(arg);
        break;
      case 'filings':
        result = await getFilingHistory(arg);
        break;
      case 'accounts':
        result = await getAccounts(arg);
        break;
      case 'analyze':
        result = await analyzeCompany(arg);
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

main();
