#!/usr/bin/env node
/**
 * particulier.js — CLI des démarches personnelles (Milestone 6).
 *
 * Sous-commandes :
 *   paperasse particulier parcours   --json '{"statutProfessionnel":"salarie","situationFamiliale":"marie","nombreEnfants":2,"frontalier":true,"paysResidence":"FR"}'
 *   paperasse particulier classe     --situation marie [--enfants 2]
 *   paperasse particulier frontalier --pays FR --brut 5000 --classe 1 --jours 40
 *   paperasse particulier fiche-paie --brut 5000 --classe 1 [--net 3600]
 *
 * Lecture seule.
 */

import { chargerCatalogue, creerProfilUtilisateur, ceJourISO } from '../lib/diagnostic/index.js';
import {
  parcoursParticulier, determinerClasseImpot, analyseFrontalier, analyseFichePaie,
} from '../lib/particulier/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const aujourdhui = arg('--date') || ceJourISO();
const sous = process.argv[2];
const num = (v) => (v == null ? undefined : Number(v));

switch (sous) {
  case 'parcours': {
    const { obligations } = chargerCatalogue();
    const profil = arg('--json')
      ? creerProfilUtilisateur(JSON.parse(arg('--json')))
      : creerProfilUtilisateur({ statutProfessionnel: 'salarie', situationFamiliale: 'marie', nombreEnfants: 2, frontalier: true, paysResidence: 'FR' });
    const p = parcoursParticulier(profil, obligations, { aujourdhui });
    console.log(`\nDémarches personnelles (au ${aujourdhui})`);
    console.log(`Classe d'impôt déduite : ${p.classeImpot.classe} — ${p.classeImpot.raison}\n`);
    const titres = { fiscalite: 'FISCALITÉ', salarie: 'SALARIÉ', frontalier: 'FRONTALIER', famille: 'FAMILLE', autre: 'AUTRE' };
    for (const d of Object.keys(titres)) {
      const liste = p.parDomaine[d];
      if (!liste) continue;
      console.log(`=== ${titres[d]} ===`);
      for (const i of liste) {
        console.log(`  • ${i.nom}${i.echeance ? `  ⏱ ${i.echeance}` : ''}`);
        if (i.source) console.log(`    Source : ${i.source}`);
      }
      console.log('');
    }
    break;
  }
  case 'classe': {
    const c = determinerClasseImpot({ situationFamiliale: arg('--situation'), nombreEnfants: num(arg('--enfants')) || 0 });
    console.log(`Classe d'impôt : ${c.classe}`);
    console.log(`Raison : ${c.raison}`);
    console.log(`Source : ${c.provenance.source} (${c.provenance.niveauConfiance})`);
    break;
  }
  case 'frontalier': {
    const a = analyseFrontalier({ paysResidence: arg('--pays'), salaireBrutMensuel: num(arg('--brut')), classe: arg('--classe') || '1', joursHorsLU: num(arg('--jours')) || 0 });
    console.log(`Frontalier ${a.paysResidence} — seuil ${a.seuilJours} j, jours hors LU : ${a.joursHorsLU}`);
    if (a.alerte) console.log(`⚠ ${a.alerte}`); else console.log('✓ Sous le seuil de tolérance.');
    if (a.net) console.log(`Net LU mensuel : ${a.net.netLuMensuel} € | retenue : ${a.net.retenueLuMensuel} € | net final : ${a.net.netFinalMensuel} €`);
    console.log(`Source : ${a.provenance.source}`);
    break;
  }
  case 'fiche-paie': {
    const c = analyseFichePaie({ salaireBrutMensuel: num(arg('--brut')), classe: arg('--classe') || '1', netAffiche: num(arg('--net')) });
    console.log(`Net mensuel recalculé : ${c.netRecalcule} €`);
    if (!c.coherent) for (const a of c.anomalies) console.log(`  ⚠ ${a.message}`); else console.log('✓ Cohérent (dans la tolérance).');
    console.log(`${c.provenance.note}`);
    break;
  }
  default:
    console.log(`Usage :
  paperasse particulier parcours   [--json '{...profil...}'] [--date YYYY-MM-DD]
  paperasse particulier classe     --situation celibataire|marie|partenariat|divorce|separe|veuf [--enfants N]
  paperasse particulier frontalier --pays FR|BE|DE [--brut 5000 --classe 1 --jours 40]
  paperasse particulier fiche-paie --brut 5000 --classe 1 [--net 3600]`);
    process.exit(sous ? 1 : 0);
}
