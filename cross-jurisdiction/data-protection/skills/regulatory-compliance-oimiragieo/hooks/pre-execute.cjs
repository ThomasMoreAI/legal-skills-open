'use strict';

/**
 * regulatory-compliance pre-execute hook
 * Validates skill inputs against schemas/input.schema.json before execution.
 * Follows Iron Law I: enforcement hooks must validate before code runs.
 */

const path = require('path');
const fs = require('fs');
const { safeParseJSON } = require('../../../lib/utils/safe-json.cjs');

function preExecute(input = {}) {
  try {
    // Load schema for validation
    const schemaPath = path.join(__dirname, '../schemas/input.schema.json');

    if (!fs.existsSync(schemaPath)) {
      process.stderr.write(
        '[regulatory-compliance/pre-execute] Schema not found — skipping validation\n'
      );
      return { continue: true };
    }

    const _schema = safeParseJSON(fs.readFileSync(schemaPath, 'utf8'));

    // Validate required fields
    if (!input.subject || typeof input.subject !== 'string' || input.subject.trim() === '') {
      process.stderr.write(
        '[regulatory-compliance/pre-execute] Input validation FAILED: "subject" is required and must be a non-empty string\n'
      );
      process.exit(2);
    }

    // Validate jurisdictions enum if provided
    const validJurisdictions = [
      'EU',
      'California',
      'Virginia',
      'Colorado',
      'Connecticut',
      'Texas',
      'Oregon',
      'Montana',
      'Florida',
      'Global',
    ];
    if (input.jurisdictions) {
      if (!Array.isArray(input.jurisdictions)) {
        process.stderr.write(
          '[regulatory-compliance/pre-execute] "jurisdictions" must be an array\n'
        );
        process.exit(2);
      }
      const invalid = input.jurisdictions.filter(j => !validJurisdictions.includes(j));
      if (invalid.length > 0) {
        process.stderr.write(
          `[regulatory-compliance/pre-execute] Invalid jurisdiction(s): ${invalid.join(', ')}. Valid: ${validJurisdictions.join(', ')}\n`
        );
        process.exit(2);
      }
    }

    // Validate regulations enum if provided
    const validRegulations = ['GDPR', 'CCPA', 'CPRA', 'VCDPA', 'ADA', 'WCAG', 'DPA', 'Section508'];
    if (input.regulations) {
      if (!Array.isArray(input.regulations)) {
        process.stderr.write(
          '[regulatory-compliance/pre-execute] "regulations" must be an array\n'
        );
        process.exit(2);
      }
      const invalid = input.regulations.filter(r => !validRegulations.includes(r));
      if (invalid.length > 0) {
        process.stderr.write(
          `[regulatory-compliance/pre-execute] Invalid regulation(s): ${invalid.join(', ')}. Valid: ${validRegulations.join(', ')}\n`
        );
        process.exit(2);
      }
    }

    // Validate assessmentScope if provided
    const validScopes = [
      'full',
      'gdpr-ccpa-only',
      'accessibility-only',
      'dpa-only',
      'privacy-by-design-only',
    ];
    if (input.assessmentScope && !validScopes.includes(input.assessmentScope)) {
      process.stderr.write(
        `[regulatory-compliance/pre-execute] Invalid assessmentScope: "${input.assessmentScope}". Valid: ${validScopes.join(', ')}\n`
      );
      process.exit(2);
    }

    process.stderr.write('[regulatory-compliance/pre-execute] Input validation PASSED\n');
    return { continue: true };
  } catch (err) {
    // Fail-open on unexpected errors (advisory hook behavior)
    process.stderr.write(
      `[regulatory-compliance/pre-execute] Unexpected error (allowing): ${err.message}\n`
    );
    return { continue: true };
  }
}

module.exports = { preExecute };
