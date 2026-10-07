#!/usr/bin/env node
/**
 * validate-schemas.js — Valide tous les fichiers data/*.json contre leur schéma.
 *
 * Validateur JSON Schema minimaliste (subset draft-07) sans dépendance externe.
 * Vérifie : type, required, minimum, maximum, minLength, minItems, pattern,
 * const, enum, properties, patternProperties, items.
 *
 * Convention de mapping : pour chaque <skill>/data/<nom>.json, on cherche
 * schemas/<nom>.schema.json (le suffixe -2025 ou similaire est ignoré).
 *
 * Usage : node scripts/validate-schemas.js
 * Exit 0 si tout valide, 1 sinon.
 */

import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join, dirname, basename } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');
const SCHEMAS_DIR = join(ROOT, 'schemas');

function readJson(p) { return JSON.parse(readFileSync(p, 'utf8')); }

function typeOf(v) {
  if (v === null) return 'null';
  if (Array.isArray(v)) return 'array';
  if (Number.isInteger(v)) return 'integer';
  return typeof v;
}

function typesMatch(actual, expected) {
  const list = Array.isArray(expected) ? expected : [expected];
  return list.some(t => t === actual || (t === 'number' && actual === 'integer'));
}

function validate(data, schema, path = '$', errors = []) {
  if (schema.type !== undefined && !typesMatch(typeOf(data), schema.type)) {
    errors.push(`${path}: attendu type ${JSON.stringify(schema.type)}, reçu ${typeOf(data)}`);
    return errors;
  }
  if (schema.const !== undefined && data !== schema.const) {
    errors.push(`${path}: attendu const "${schema.const}", reçu "${data}"`);
  }
  if (schema.enum && !schema.enum.includes(data)) {
    errors.push(`${path}: valeur "${data}" hors enum ${JSON.stringify(schema.enum)}`);
  }
  if (typeof data === 'string') {
    if (schema.minLength !== undefined && data.length < schema.minLength) {
      errors.push(`${path}: longueur ${data.length} < minLength ${schema.minLength}`);
    }
    if (schema.pattern && !new RegExp(schema.pattern).test(data)) {
      errors.push(`${path}: ne correspond pas au pattern ${schema.pattern}`);
    }
  }
  if (typeof data === 'number') {
    if (schema.minimum !== undefined && data < schema.minimum) {
      errors.push(`${path}: ${data} < minimum ${schema.minimum}`);
    }
    if (schema.maximum !== undefined && data > schema.maximum) {
      errors.push(`${path}: ${data} > maximum ${schema.maximum}`);
    }
  }
  if (Array.isArray(data)) {
    if (schema.minItems !== undefined && data.length < schema.minItems) {
      errors.push(`${path}: ${data.length} éléments < minItems ${schema.minItems}`);
    }
    if (schema.items) {
      data.forEach((item, i) => validate(item, schema.items, `${path}[${i}]`, errors));
    }
  }
  if (typeOf(data) === 'object') {
    for (const req of schema.required || []) {
      if (!(req in data)) errors.push(`${path}: champ requis manquant "${req}"`);
    }
    if (schema.properties) {
      for (const [key, sub] of Object.entries(schema.properties)) {
        if (key in data) validate(data[key], sub, `${path}.${key}`, errors);
      }
    }
    if (schema.patternProperties) {
      for (const [re, sub] of Object.entries(schema.patternProperties)) {
        const rx = new RegExp(re);
        for (const key of Object.keys(data)) {
          if (rx.test(key)) validate(data[key], sub, `${path}.${key}`, errors);
        }
      }
    }
  }
  return errors;
}

// Découverte automatique des fichiers data/*.json
function findDataFiles(dir, out = []) {
  for (const name of readdirSync(dir)) {
    const full = join(dir, name);
    const st = statSync(full);
    if (st.isDirectory() && name !== 'node_modules' && name !== '.git' && name !== 'data-sources' && name !== 'schemas') {
      findDataFiles(full, out);
    } else if (st.isFile() && name.endsWith('.json') && full.includes(`/data/`)) {
      out.push(full);
    }
  }
  return out;
}

function schemaForFile(filepath) {
  // Mapping : <name>.json → schemas/<name>.schema.json (en retirant les suffixes -YYYY)
  const base = basename(filepath, '.json').replace(/-(19|20)\d{2}$/, '');
  const candidate = join(SCHEMAS_DIR, `${base}.schema.json`);
  return existsSync(candidate) ? candidate : null;
}

const dataFiles = findDataFiles(ROOT);
let totalErrors = 0;
let totalChecked = 0;
let totalSkipped = 0;

console.log(`Validation de ${dataFiles.length} fichier(s) data/*.json :\n`);
for (const f of dataFiles) {
  const rel = f.replace(ROOT + '/', '');
  const schemaPath = schemaForFile(f);
  if (!schemaPath) {
    console.log(`  ⚠ ${rel} (aucun schéma — passé)`);
    totalSkipped++;
    continue;
  }
  try {
    const data = readJson(f);
    const schema = readJson(schemaPath);
    const errors = validate(data, schema);
    if (errors.length === 0) {
      console.log(`  ✓ ${rel}`);
      totalChecked++;
    } else {
      console.log(`  ✗ ${rel}`);
      for (const e of errors) console.log(`      ${e}`);
      totalErrors += errors.length;
    }
  } catch (e) {
    console.log(`  ✗ ${rel} (erreur : ${e.message})`);
    totalErrors++;
  }
}

console.log(`\n${totalChecked} validé(s), ${totalSkipped} passé(s), ${totalErrors} erreur(s).`);
process.exit(totalErrors === 0 ? 0 : 1);
