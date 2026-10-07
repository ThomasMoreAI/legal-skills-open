#!/usr/bin/env node
/**
 * entreprise.js — CLI du cycle de vie de l'entreprise (Milestone 5).
 *
 * Sous-commandes :
 *   paperasse entreprise parcours --json '{"nom":"Acme","formeJuridique":"SARL","statut":"actif","regimeTVA":"normal","frequenceTVA":"mensuelle","nbSalaries":2}' [--exercice 2025-12-31]
 *   paperasse entreprise creation --op creation_sarl
 *
 * Lecture seule : liste et ordonne les obligations, ne déclenche aucune démarche.
 */

import { chargerCatalogue, creerProfilSociete, ceJourISO } from '../lib/diagnostic/index.js';
import { parcoursEntreprise, checklistCreation } from '../lib/entreprise/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const aujourdhui = arg('--date') || ceJourISO();
const sous = process.argv[2];

switch (sous) {
  case 'parcours': {
    const { obligations } = chargerCatalogue();
    const situation = arg('--json')
      ? creerProfilSociete(JSON.parse(arg('--json')))
      : creerProfilSociete({ nom: 'Exemple SARL', formeJuridique: 'SARL', statut: 'actif', regimeTVA: 'normal', frequenceTVA: 'mensuelle', nbSalaries: 1 });
    const p = parcoursEntreprise(situation, obligations, { aujourdhui, exerciceFin: arg('--exercice') });
    console.log(`\nParcours administratif — ${situation.nom} (au ${aujourdhui})\n`);
    const titres = { creation: 'CRÉATION', vie: 'VIE SOCIALE', fiscalite: 'FISCALITÉ', employeur: 'EMPLOYEUR', cessation: 'CESSATION', autre: 'AUTRE' };
    for (const phase of Object.keys(titres)) {
      const liste = p.parPhase[phase];
      if (!liste) continue;
      console.log(`=== ${titres[phase]} ===`);
      for (const i of liste) {
        console.log(`  • ${i.nom}${i.echeance ? `  ⏱ ${i.echeance}` : ''}`);
        if (i.administration) console.log(`    Autorité : ${i.administration}`);
        if (i.source) console.log(`    Source : ${i.source}`);
      }
      console.log('');
    }
    if (p.piecesManquantes.length) {
      console.log('=== PIÈCES MANQUANTES ===');
      for (const x of p.piecesManquantes) console.log(`  • ${x.nom} : ${x.manquantes.join(', ')}`);
    }
    break;
  }
  case 'creation': {
    const op = arg('--op') || 'creation_sarl';
    const c = checklistCreation(op);
    console.log(`\n${c.libelle}\n`);
    if (c.capital_minimum_eur != null) console.log(`Capital minimum : ${c.capital_minimum_eur} €`);
    if (c.delai_jours) console.log(`Délai indicatif : ${c.delai_jours} jours`);
    if (c.cout_indicatif_eur) console.log(`Coût indicatif : ${c.cout_indicatif_eur} €`);
    console.log('\nPièces :');
    for (const p of c.pieces) console.log(`  ☐ ${p}`);
    if (c.bases_legales) console.log(`\nBases légales : ${c.bases_legales.join(' ; ')}`);
    break;
  }
  default:
    console.log(`Usage :
  paperasse entreprise parcours [--json '{...société...}'] [--exercice YYYY-MM-DD] [--date YYYY-MM-DD]
  paperasse entreprise creation --op creation_sarl|creation_sa|creation_asbl|...`);
    process.exit(sous ? 1 : 0);
}
