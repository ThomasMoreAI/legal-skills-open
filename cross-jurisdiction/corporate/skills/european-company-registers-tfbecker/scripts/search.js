#!/usr/bin/env node
/**
 * Unified Company Register Search
 *
 * Search for company financial data across multiple European registers.
 *
 * Usage:
 *   node search.js --country <code> --name "Company Name"
 *   node search.js --country <code> --id <registration_id>
 *
 * Supported countries:
 *   de - Germany (Bundesanzeiger)
 *   gb - UK (Companies House)
 *   fr - France (INPI/RNE)
 *   pl - Poland (KRS)
 */

const { spawn } = require('child_process');
const path = require('path');

const SCRIPTS_DIR = __dirname;

const COUNTRY_SCRIPTS = {
  // Germany: combined Unternehmensregister + Bundesanzeiger (parallel, CAPTCHA-free listing).
  de: 'de-combined.js',
  germany: 'de-combined.js',
  gb: 'gb-companies-house.js',
  uk: 'gb-companies-house.js',
  fr: 'fr-inpi.js',
  france: 'fr-inpi.js',
  pl: 'pl-krs.js',
  poland: 'pl-krs.js'
};

const COUNTRY_NAMES = {
  de: 'Germany',
  gb: 'United Kingdom',
  fr: 'France',
  pl: 'Poland'
};

/**
 * Parse command line arguments
 */
function parseArgs(args) {
  const result = {
    country: null,
    name: null,
    id: null,
    json: false,
    help: false
  };

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];

    if (arg === '--country' || arg === '-c') {
      result.country = args[++i]?.toLowerCase();
    } else if (arg === '--name' || arg === '-n') {
      result.name = args[++i];
    } else if (arg === '--id' || arg === '-i') {
      result.id = args[++i];
    } else if (arg === '--json' || arg === '-j') {
      result.json = true;
    } else if (arg === '--help' || arg === '-h') {
      result.help = true;
    }
  }

  return result;
}

/**
 * Run a country-specific script
 */
function runScript(script, command, arg) {
  return new Promise((resolve, reject) => {
    const scriptPath = path.join(SCRIPTS_DIR, script);
    const proc = spawn('node', [scriptPath, command, arg], {
      stdio: ['pipe', 'pipe', 'pipe']
    });

    let stdout = '';
    let stderr = '';

    proc.stdout.on('data', data => stdout += data);
    proc.stderr.on('data', data => stderr += data);

    proc.on('close', code => {
      if (code === 0) {
        try {
          resolve(JSON.parse(stdout));
        } catch (e) {
          resolve({ raw: stdout, error: 'Failed to parse output' });
        }
      } else {
        resolve({
          error: stderr || `Script exited with code ${code}`,
          found: false
        });
      }
    });

    proc.on('error', err => {
      resolve({
        error: err.message,
        found: false
      });
    });
  });
}

/**
 * Print usage help
 */
function printHelp() {
  console.log(`
Company Register Search - Find company financial data across Europe

USAGE:
  node search.js --country <code> --name "Company Name"
  node search.js --country <code> --id <registration_id>

OPTIONS:
  -c, --country <code>   Country code (required)
  -n, --name <name>      Company name to search
  -i, --id <id>          Registration ID (KRS, company number, SIREN, etc.)
  -j, --json             Output raw JSON
  -h, --help             Show this help

SUPPORTED COUNTRIES:
  de, germany    Germany - Unternehmensregister + Bundesanzeiger combined, parallel
                 (GJ 2022+ from the Unternehmensregister; free figure extraction via
                 Claude for GJ <=2021). CAPTCHA-free listing.
  gb, uk         United Kingdom - Companies House API
  fr, france     France - INPI/RNE (api.gouv.fr)
  pl, poland     Poland - KRS

EXAMPLES:
  # Search German company by name
  node search.js --country de --name "BMW AG"

  # Get UK company by registration number
  node search.js --country gb --id 00445790

  # Search French company
  node search.js --country fr --name "Carrefour"

  # Get Polish company by KRS
  node search.js --country pl --id 0000019193

SETUP:
  Germany needs NO API key, the CAPTCHA and the financial-figure extraction run on
  Claude via the local \`claude\` CLI (headless, native OAuth subscription). Other
  countries read their keys from env vars or a local config/keys.json:
  {
    "COMPANIES_HOUSE_API_KEY": "...", // UK (free at developer.company-information.service.gov.uk)
    "INPI_API_TOKEN": "..."           // France (optional, basic search works without)
  }

NOTE:
  Financial data availability varies by country:
  - Germany: Full (revenue, assets, P&L) via Claude extraction
  - UK: Limited (balance sheet only, P&L often missing)
  - France: Full if INPI token provided
  - Poland: Metadata only (financials require manual download)
`);
}

/**
 * Main entry point
 */
async function main() {
  const args = parseArgs(process.argv.slice(2));

  if (args.help || (!args.country && !args.name && !args.id)) {
    printHelp();
    process.exit(0);
  }

  // Validate country
  if (!args.country) {
    console.error('Error: --country is required');
    console.error('Run with --help for usage information');
    process.exit(1);
  }

  const script = COUNTRY_SCRIPTS[args.country];
  if (!script) {
    console.error(`Error: Unknown country code '${args.country}'`);
    console.error('Supported: de, gb, fr, pl');
    process.exit(1);
  }

  // Determine command and argument
  let command, argument;

  if (args.id) {
    // Use ID-based lookup (analyze)
    command = 'analyze';
    argument = args.id;
  } else if (args.name) {
    // Use name search
    command = 'search';
    argument = args.name;
  } else {
    console.error('Error: Either --name or --id is required');
    process.exit(1);
  }

  // Run the appropriate script
  const result = await runScript(script, command, argument);

  // Add metadata
  result.query = {
    country: args.country,
    country_name: COUNTRY_NAMES[args.country.substring(0, 2)] || args.country,
    search_type: command,
    search_value: argument
  };

  // Output
  console.log(JSON.stringify(result, null, 2));
}

main();
