#!/usr/bin/env node
/**
 * test-templates-de.js — Tests du moteur de rendu et des templates DE.
 */

import { readFileSync, readdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { renderTemplate } from '../lib/templates-de/render.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');
const TPL_DIR = join(ROOT, 'templates', 'de');

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n      ${e.message}`); failed++; }
}
function eq(a, b, msg) { if (a !== b) throw new Error(`${msg||''}: attendu ${JSON.stringify(b)}, reçu ${JSON.stringify(a)}`); }
function truthy(v, msg) { if (!v) throw new Error(msg || 'attendu truthy'); }

console.log('=== Tests moteur de rendu ===');
test('Substitution simple', () => eq(renderTemplate('Hallo {{ name }}!', { name: 'Welt' }), 'Hallo Welt!'));
test('Chemin pointé', () => eq(renderTemplate('{{ a.b.c }}', { a: { b: { c: 'X' } } }), 'X'));
test('Variable manquante → vide', () => eq(renderTemplate('A{{ inconnu }}B', {}), 'AB'));
test('Filtre default', () => eq(renderTemplate('{{ x | default(\'fallback\') }}', {}), 'fallback'));
test('Filtre default ignoré si valeur présente', () => eq(renderTemplate('{{ x | default(\'F\') }}', { x: 'V' }), 'V'));
test('Boucle for simple', () => {
  const t = '{% for item in liste %}- {{ item }}\n{% endfor %}';
  eq(renderTemplate(t, { liste: ['a', 'b', 'c'] }), '- a\n- b\n- c\n');
});
test('Boucle avec loop.index (1-based)', () => {
  const t = '{% for x in l %}{{ loop.index }}.{{ x }} {% endfor %}';
  eq(renderTemplate(t, { l: ['a', 'b'] }), '1.a 2.b ');
});
test('Boucle sur objets avec sous-propriétés', () => {
  const t = '{% for p in items %}{{ p.nom }}={{ p.val }};{% endfor %}';
  eq(renderTemplate(t, { items: [{ nom: 'A', val: 1 }, { nom: 'B', val: 2 }] }), 'A=1;B=2;');
});
test('Condition if true', () => eq(renderTemplate('{% if ok %}OUI{% endif %}', { ok: true }), 'OUI'));
test('Condition if false', () => eq(renderTemplate('{% if ok %}OUI{% endif %}', { ok: false }), ''));
test('Condition if avec variable dans le bloc', () => {
  eq(renderTemplate('{% if x %}val={{ x }}{% endif %}', { x: 42 }), 'val=42');
});

console.log('\n=== Tests rendu des templates DE complets ===');
const examples = {
  'mahnung': 'mahnung-input.json',
  'rechnung-luxemburg': 'rechnung-input.json',
  'einberufung-gesellschafterversammlung': 'sarl-ag-input.json',
};

for (const [tpl, ex] of Object.entries(examples)) {
  test(`Template "${tpl}" : rendu sans variable non-substituée`, () => {
    const t = readFileSync(join(TPL_DIR, tpl + '.md'), 'utf8');
    const ctx = JSON.parse(readFileSync(join(ROOT, 'examples/de/' + ex), 'utf8'));
    const out = renderTemplate(t, ctx);
    // Aucune syntaxe {{ ... }} ou {% ... %} ne doit subsister
    const restes = out.match(/\{\{[^}]+\}\}|\{%[^%]+%\}/g);
    if (restes) throw new Error(`Restes non substitués : ${restes.slice(0, 3).join(', ')}`);
    truthy(out.length > 200, 'sortie trop courte');
  });
}

test('Mahnung : montant et IBAN présents dans la sortie', () => {
  const t = readFileSync(join(TPL_DIR, 'mahnung.md'), 'utf8');
  const ctx = JSON.parse(readFileSync(join(ROOT, 'examples/de/mahnung-input.json'), 'utf8'));
  const out = renderTemplate(t, ctx);
  truthy(out.includes('1234.56 EUR'), 'montant manquant');
  truthy(out.includes('LU28 0019 4006 4475 0000'), 'IBAN manquant');
  truthy(out.includes('40 EUR'), 'pénalité 40 € manquante');
});

test('Rechnung : positions multi-lignes rendues', () => {
  const t = readFileSync(join(TPL_DIR, 'rechnung-luxemburg.md'), 'utf8');
  const ctx = JSON.parse(readFileSync(join(ROOT, 'examples/de/rechnung-input.json'), 'utf8'));
  const out = renderTemplate(t, ctx);
  truthy(out.includes('Beratungsleistung April 2026'));
  truthy(out.includes('Reisekostenpauschale'));
  truthy(out.includes('1895.40 EUR'));
});

test('Convocation SARL : tagesordnung numérotée', () => {
  const t = readFileSync(join(TPL_DIR, 'einberufung-gesellschafterversammlung.md'), 'utf8');
  const ctx = JSON.parse(readFileSync(join(ROOT, 'examples/de/sarl-ag-input.json'), 'utf8'));
  const out = renderTemplate(t, ctx);
  truthy(out.includes('1. Vorlage'));
  truthy(out.includes('5. Sonstiges'));
  truthy(out.includes('710-15'));  // référence légale présente
});

console.log('\n=== Tests présence des templates ===');
test('6 templates allemands présents', () => {
  const files = readdirSync(TPL_DIR).filter(f => f.endsWith('.md') && f !== 'README.md');
  eq(files.length, 6);
});

console.log(`\n${passed} passés, ${failed} échoués\n`);
process.exit(failed === 0 ? 0 : 1);
