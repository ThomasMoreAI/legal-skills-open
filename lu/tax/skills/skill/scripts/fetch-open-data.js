#!/usr/bin/env node
/**
 * fetch-open-data.js — Interrogation de l'API udata de data.public.lu
 *
 * Le portail open data luxembourgeois (https://data.public.lu) tourne sous
 * udata (etalab) et expose son API sur /api/1/. Ce script permet de :
 *   1. Découvrir les jeux de données pertinents (recherche par mot-clé)
 *   2. Inspecter un jeu de données précis (liste des ressources)
 *   3. Télécharger toutes les ressources d'un jeu de données dans un dossier
 *      de staging (data-sources/<slug>/) pour revue manuelle
 *
 * AUCUNE donnée du dépôt n'est écrasée automatiquement. Les fichiers
 * téléchargés vont en staging ; vous devez ensuite intégrer manuellement
 * les valeurs pertinentes dans les data/*.json après validation.
 *
 * Usage :
 *   node scripts/fetch-open-data.js search "<mots-clés>"
 *   node scripts/fetch-open-data.js dataset <slug>
 *   node scripts/fetch-open-data.js fetch   <slug>
 *
 * Exemples :
 *   node scripts/fetch-open-data.js search "impôt"
 *   node scripts/fetch-open-data.js search communes
 *   node scripts/fetch-open-data.js dataset statistiques-par-niveau-geographique-communes
 *   node scripts/fetch-open-data.js fetch   statistiques-par-niveau-geographique-communes
 */

import { writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');
const STAGING = join(ROOT, 'data-sources');
const API = 'https://data.public.lu/api/1';
const UA = { 'User-Agent': 'paperasse-lux/0.2.0 (+https://github.com/gregherbe76/Luxembourg-Paperasse)' };

async function api(path, params = {}) {
  const url = new URL(`${API}${path}`);
  for (const [k, v] of Object.entries(params)) url.searchParams.set(k, String(v));
  const res = await fetch(url, { headers: UA });
  if (!res.ok) throw new Error(`API ${path} → HTTP ${res.status}`);
  return res.json();
}

async function search(query) {
  const r = await api('/datasets/', { q: query, page_size: 20 });
  console.log(`\n${r.total} jeu(x) de données trouvé(s) pour "${query}" (top ${r.data.length}) :\n`);
  for (const ds of r.data) {
    const org = ds.organization?.name || '—';
    const upd = (ds.last_update || ds.last_modified || '').slice(0, 10) || '?';
    console.log(`  • ${ds.slug}`);
    console.log(`    Titre   : ${ds.title}`);
    console.log(`    Org     : ${org}`);
    console.log(`    MAJ     : ${upd}`);
    console.log(`    Ressources : ${ds.resources?.length || 0}`);
    console.log(`    URL     : ${ds.page || `https://data.public.lu/fr/datasets/${ds.slug}/`}`);
    console.log('');
  }
  if (r.total > r.data.length) {
    console.log(`(${r.total - r.data.length} résultat(s) supplémentaire(s) — affinez la requête pour les voir)`);
  }
}

async function showDataset(slug) {
  const ds = await api(`/datasets/${slug}/`);
  console.log(`\n=== ${ds.title} ===`);
  console.log(`Slug     : ${ds.slug}`);
  console.log(`Org      : ${ds.organization?.name}`);
  console.log(`Licence  : ${ds.license}`);
  console.log(`MAJ      : ${(ds.last_update || ds.last_modified || '').slice(0, 10)}`);
  console.log(`URL      : ${ds.page || `https://data.public.lu/fr/datasets/${ds.slug}/`}`);
  console.log(`\nDescription :\n${(ds.description || '').replace(/\s+/g, ' ').slice(0, 500)}${(ds.description?.length || 0) > 500 ? '…' : ''}`);
  console.log(`\nRessources (${ds.resources?.length || 0}) :`);
  for (const r of ds.resources || []) {
    console.log(`  • [${r.format || '?'}] ${r.title || r.description || '(sans nom)'}`);
    console.log(`    ${r.url}`);
  }
}

async function fetchDataset(slug) {
  const ds = await api(`/datasets/${slug}/`);
  const outDir = join(STAGING, slug);
  mkdirSync(outDir, { recursive: true });

  writeFileSync(
    join(outDir, '_metadata.json'),
    JSON.stringify(
      {
        fetched_at: new Date().toISOString(),
        source: ds.page || `https://data.public.lu/fr/datasets/${ds.slug}/`,
        slug: ds.slug,
        title: ds.title,
        organization: ds.organization?.name,
        license: ds.license,
        last_updated: ds.last_update || ds.last_modified,
      },
      null,
      2,
    ),
  );

  const resources = ds.resources || [];
  console.log(`\nTéléchargement de ${resources.length} ressource(s) → ${outDir}/`);
  let ok = 0, ko = 0;
  for (const r of resources) {
    if (!r.url) { ko++; continue; }
    const ext = (r.format || 'bin').toLowerCase().replace(/[^a-z0-9]/g, '') || 'bin';
    const safe = (r.title || r.id || `resource`).replace(/[^\w.-]+/g, '_').slice(0, 80);
    const filename = `${safe}.${ext}`;
    const filepath = join(outDir, filename);
    try {
      const res = await fetch(r.url, { headers: UA, redirect: 'follow' });
      if (!res.ok) { console.log(`  ✗ ${filename} (HTTP ${res.status})`); ko++; continue; }
      const buf = Buffer.from(await res.arrayBuffer());
      writeFileSync(filepath, buf);
      console.log(`  ✓ ${filename} (${(buf.length / 1024).toFixed(1)} KB)`);
      ok++;
    } catch (e) {
      console.log(`  ✗ ${filename} (${e.message})`);
      ko++;
    }
  }
  console.log(`\nTerminé : ${ok} succès, ${ko} échec(s).`);
  console.log(`Métadonnées de traçabilité : ${outDir}/_metadata.json`);
  console.log(`\nIMPORTANT : ces fichiers sont en staging (data-sources/ est dans .gitignore).`);
  console.log(`Après revue manuelle, intégrez les valeurs pertinentes dans data/*.json.`);
}

const [, , cmd, ...args] = process.argv;
const usage = `Usage :
  node scripts/fetch-open-data.js search "<mots-clés>"
  node scripts/fetch-open-data.js dataset <slug>
  node scripts/fetch-open-data.js fetch   <slug>

Exemples :
  node scripts/fetch-open-data.js search "impôt"
  node scripts/fetch-open-data.js search communes
  node scripts/fetch-open-data.js dataset statistiques-par-niveau-geographique-communes
  node scripts/fetch-open-data.js fetch   statistiques-par-niveau-geographique-communes`;

try {
  if (cmd === 'search' && args.length) await search(args.join(' '));
  else if (cmd === 'dataset' && args[0]) await showDataset(args[0]);
  else if (cmd === 'fetch' && args[0]) await fetchDataset(args[0]);
  else { console.log(usage); process.exit(1); }
} catch (e) {
  console.error(`ERREUR : ${e.message}`);
  process.exit(2);
}
