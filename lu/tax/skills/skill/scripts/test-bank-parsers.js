#!/usr/bin/env node
/**
 * test-bank-parsers.js — Tests déterministes des parseurs bancaires.
 */

import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseBankStatement, aggregate } from '../lib/bank-parsers/index.js';
import { parseAmount, parseDate } from '../lib/bank-parsers/csv.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg || ''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function approx(a, b, eps = 0.01) { if (Math.abs(a - b) > eps) throw new Error(`Δ${a} vs ${b} > ${eps}`); }

console.log('=== Tests parseAmount (formats FR/LU/EN) ===');
test('1.234,56 (européen)', () => approx(parseAmount('1.234,56'), 1234.56));
test('1,234.56 (anglo)', () => approx(parseAmount('1,234.56'), 1234.56));
test('-1234,56', () => approx(parseAmount('-1234,56'), -1234.56));
test('1234,56 €', () => approx(parseAmount('1234,56 €'), 1234.56));
test('vide → null', () => eq(parseAmount(''), null));
test('"-" → null', () => eq(parseAmount('-'), null));

console.log('\n=== Tests parseDate ===');
test('12/03/2025 → ISO', () => eq(parseDate('12/03/2025'), '2025-03-12'));
test('12.03.2025 → ISO', () => eq(parseDate('12.03.2025'), '2025-03-12'));
test('2025-03-12 → inchangé', () => eq(parseDate('2025-03-12'), '2025-03-12'));

console.log('\n=== Tests parseur BCEE ===');
test('BCEE sample : détection format', () => {
  const text = readFileSync(join(ROOT, 'examples/bank-statements/bcee-sample.csv'), 'utf8');
  const r = parseBankStatement(text);
  eq(r.format, 'bcee', 'format');
  eq(r.count, 5, 'nb transactions');
});
test('BCEE sample : 1ère transaction (crédit 1234.56)', () => {
  const text = readFileSync(join(ROOT, 'examples/bank-statements/bcee-sample.csv'), 'utf8');
  const r = parseBankStatement(text);
  const t = r.transactions[0];
  eq(t.date, '2025-03-12');
  approx(t.montant, 1234.56);
  eq(t.sens, 'credit');
  eq(t.devise, 'EUR');
});
test('BCEE sample : agrégation totaux', () => {
  const text = readFileSync(join(ROOT, 'examples/bank-statements/bcee-sample.csv'), 'utf8');
  const r = parseBankStatement(text);
  const t = aggregate(r.transactions);
  approx(t.total_credits, 3234.56); // 1234.56 + 2000.00
  approx(t.total_debits, 4375.50);  // 850 + 3500 + 25.50
  approx(t.flux_net, -1140.94);
});

console.log('\n=== Tests parseur POST ===');
test('POST sample : détection format', () => {
  const text = readFileSync(join(ROOT, 'examples/bank-statements/post-sample.csv'), 'utf8');
  const r = parseBankStatement(text);
  eq(r.format, 'post');
  eq(r.count, 4);
});
test('POST sample : montants signés', () => {
  const text = readFileSync(join(ROOT, 'examples/bank-statements/post-sample.csv'), 'utf8');
  const r = parseBankStatement(text);
  approx(r.transactions[0].montant, -150);
  eq(r.transactions[0].sens, 'debit');
  approx(r.transactions[1].montant, 1200);
  eq(r.transactions[1].sens, 'credit');
});

console.log('\n=== Tests parseur CAMT.053 (ISO 20022) ===');
test('CAMT.053 sample : détection XML', () => {
  const text = readFileSync(join(ROOT, 'examples/bank-statements/camt053-sample.xml'), 'utf8');
  const r = parseBankStatement(text);
  eq(r.format, 'camt053');
  eq(r.count, 3);
});
test('CAMT.053 : crédit 1234.56 EUR avec date ISO', () => {
  const text = readFileSync(join(ROOT, 'examples/bank-statements/camt053-sample.xml'), 'utf8');
  const r = parseBankStatement(text);
  const t = r.transactions[0];
  eq(t.date, '2025-03-12');
  approx(t.montant, 1234.56);
  eq(t.sens, 'credit');
  eq(t.devise, 'EUR');
  eq(t.reference, 'NREF-001');
});
test('CAMT.053 : débit -850.00', () => {
  const text = readFileSync(join(ROOT, 'examples/bank-statements/camt053-sample.xml'), 'utf8');
  const r = parseBankStatement(text);
  const t = r.transactions[1];
  approx(t.montant, -850);
  eq(t.sens, 'debit');
});
test('CAMT.053 : agrégation', () => {
  const text = readFileSync(join(ROOT, 'examples/bank-statements/camt053-sample.xml'), 'utf8');
  const r = parseBankStatement(text);
  const t = aggregate(r.transactions);
  approx(t.total_credits, 1234.56);
  approx(t.total_debits, 875.50);
});

console.log(`\n${passed} passés, ${failed} échoués\n`);
process.exit(failed === 0 ? 0 : 1);
