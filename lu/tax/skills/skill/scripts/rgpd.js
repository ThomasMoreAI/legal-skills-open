#!/usr/bin/env node
/**
 * rgpd.js — CLI sécurité, confidentialité & conformité (Milestone 12).
 *
 * Sous-commandes :
 *   paperasse rgpd chiffrer   --texte "..." --mdp "phrase"
 *   paperasse rgpd dechiffrer --file paquet.json --mdp "phrase"
 *   paperasse rgpd masquer    --file donnees.json
 *   paperasse rgpd conservation
 *
 * Aucune donnée n'est transmise ; traitement local uniquement.
 */

import { readFileSync } from 'node:fs';
import { chiffrer, dechiffrer, masquer, DUREES_CONSERVATION, CONSERVATION_PROVENANCE } from '../lib/rgpd/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const sous = process.argv[2];

switch (sous) {
  case 'chiffrer':
    console.log(JSON.stringify(chiffrer(arg('--texte') || '', arg('--mdp')), null, 2));
    break;
  case 'dechiffrer':
    console.log(dechiffrer(JSON.parse(readFileSync(arg('--file'), 'utf8')), arg('--mdp')));
    break;
  case 'masquer':
    console.log(JSON.stringify(masquer(JSON.parse(readFileSync(arg('--file'), 'utf8'))), null, 2));
    break;
  case 'conservation':
    console.log('Durées de conservation indicatives (années) :');
    for (const [k, v] of Object.entries(DUREES_CONSERVATION)) console.log(`  ${k} : ${v} an(s)`);
    console.log(`\n⚠ ${CONSERVATION_PROVENANCE.note}\nSource : ${CONSERVATION_PROVENANCE.source}`);
    break;
  default:
    console.log(`Usage :
  paperasse rgpd chiffrer   --texte "..." --mdp "phrase"
  paperasse rgpd dechiffrer --file paquet.json --mdp "phrase"
  paperasse rgpd masquer    --file donnees.json
  paperasse rgpd conservation`);
    process.exit(sous ? 1 : 0);
}
