#!/usr/bin/env node
/**
 * lbr.js — CLI d'aide LBR : validation RCS, checklists, calendrier, tarifs.
 *
 * Usage :
 *   node scripts/lbr.js valider B12345
 *   node scripts/lbr.js url B12345
 *   node scripts/lbr.js checklist creation_sarl
 *   node scripts/lbr.js operations
 *   node scripts/lbr.js calendrier 2025-12-31
 *   node scripts/lbr.js tarifs
 */

import { fileURLToPath } from 'node:url';
import { validerRCS, urlRechercheLBR, calendrierDepots, TARIFS_LBR_2026, CHECKLISTS_LBR, OPERATIONS } from '../lib/lbr/index.js';

const isCli = process.argv[1] === fileURLToPath(import.meta.url);
if (!isCli) process.exit(0);

const [, , cmd, ...rest] = process.argv;

function help() {
  console.log(`Usage : paperasse lbr <commande> [arguments]

Commandes :
  valider <RCS>          Vérifie le format d'un numéro RCS (B/F/G/E/K/X + chiffres)
  url <RCS|denom>        Renvoie l'URL du portail public LBR + aide à la recherche
  operations             Liste les opérations LBR documentées
  checklist <operation>  Pièces à déposer pour une opération (ex: creation_sarl)
  calendrier <YYYY-MM-DD> Échéances annuelles à partir d'une date de clôture d'exercice
  tarifs                 Tarifs LBR 2026

Exemples :
  paperasse lbr valider b12345
  paperasse lbr checklist creation_sarl
  paperasse lbr calendrier 2025-12-31
`);
}

if (!cmd || cmd === 'help' || cmd === '--help') { help(); process.exit(0); }

if (cmd === 'valider') {
  const r = validerRCS(rest[0]);
  console.log(JSON.stringify(r, null, 2));
  process.exit(r.valide ? 0 : 1);
}

if (cmd === 'url') {
  const arg = rest[0] || '';
  const isRcs = /^[BFGEKXbfgekx]\s*\d/.test(arg);
  console.log(JSON.stringify(urlRechercheLBR(isRcs ? { rcs: arg } : { denomination: arg }), null, 2));
  process.exit(0);
}

if (cmd === 'operations') {
  console.log('Opérations LBR documentées :\n');
  for (const op of OPERATIONS) {
    console.log(`  ${op.padEnd(28)} ${CHECKLISTS_LBR[op].libelle}`);
  }
  console.log('\nUtiliser : paperasse lbr checklist <operation>');
  process.exit(0);
}

if (cmd === 'checklist') {
  const op = rest[0];
  if (!op || !CHECKLISTS_LBR[op]) {
    console.error(`Opération inconnue : ${op}\nUtiliser : paperasse lbr operations pour voir la liste.`);
    process.exit(1);
  }
  const c = CHECKLISTS_LBR[op];
  console.log(`\n=== ${c.libelle} ===\n`);
  if (c.capital_minimum_eur != null) console.log(`Capital minimum   : ${c.capital_minimum_eur} €`);
  console.log(`Délai indicatif   : ${c.delai_jours || c.delai_apres_cloture_mois + ' mois après clôture'} jours`);
  console.log(`Coût indicatif    : ${c.cout_indicatif_eur} €${c.cout_detail ? ' — ' + c.cout_detail : ''}`);
  console.log(`\nPièces à déposer :`);
  c.pieces.forEach((p, i) => console.log(`  ${(i + 1).toString().padStart(2)}. ${p}`));
  if (c.bases_legales) {
    console.log(`\nBases légales :`);
    c.bases_legales.forEach(b => console.log(`  - ${b}`));
  }
  if (c.voir_aussi) console.log(`\nVoir aussi : ${c.voir_aussi}`);
  console.log();
  process.exit(0);
}

if (cmd === 'calendrier') {
  try {
    const cal = calendrierDepots({ exerciceFin: rest[0] });
    console.log(`\n=== Calendrier des dépôts obligatoires (clôture ${rest[0]}) ===\n`);
    cal.forEach(e => {
      console.log(`▸ ${e.nature}`);
      console.log(`  Échéance     : ${e.deadline}`);
      console.log(`  Base légale  : ${e.base_legale}`);
      console.log(`  Conseil      : ${e.conseil}\n`);
    });
  } catch (e) { console.error(e.message); process.exit(1); }
  process.exit(0);
}

if (cmd === 'tarifs') {
  console.log(`\n=== Tarifs LBR ${TARIFS_LBR_2026._as_of.slice(0, 4)} (TVA 17 % incluse) ===\n`);
  for (const [k, v] of Object.entries(TARIFS_LBR_2026)) {
    if (k.startsWith('_')) continue;
    console.log(`  ${k.padEnd(25)} ${(v.montant_eur.toFixed(2) + ' €').padStart(8)}  ${v.libelle}`);
  }
  console.log(`\nSource : ${TARIFS_LBR_2026._source}\n`);
  process.exit(0);
}

console.error(`Commande inconnue : ${cmd}\n`);
help();
process.exit(1);
