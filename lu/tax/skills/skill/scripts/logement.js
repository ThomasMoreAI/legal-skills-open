#!/usr/bin/env node
/**
 * logement.js — CLI du parcours logement & immobilier (Milestone 8).
 *
 * Sous-commandes :
 *   paperasse logement locataire    --loyer 1200
 *   paperasse logement acheteur     --prix 600000 --acquereurs 2 [--lux-ville] [--date-acte 2026-09-01]
 *   paperasse logement proprietaire
 *   paperasse logement vendeur
 *   paperasse logement garantie     --loyer 1200
 *
 * Lecture seule ; réutilise le calculateur Bëllegen Akt existant.
 */

import { parcoursLogement, garantieLocativeMax } from '../lib/logement/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const has = (nom) => process.argv.includes(nom);
const num = (v) => (v == null ? undefined : Number(v));
const sous = process.argv[2];

function afficherParcours(p) {
  console.log(`\nParcours logement — situation : ${p.situation}\n`);
  if (p.avertissement) console.log(`⚠ ${p.avertissement}\n`);
  console.log('Démarches proposées :');
  for (const e of p.etapes) {
    console.log(`  • ${e.titre} — ${e.description}`);
    console.log(`    Source : ${e.source}`);
  }
  if (p.calculs.garantie) {
    console.log('\nGarantie locative (options) :');
    for (const o of p.calculs.garantie.options) console.log(`  ${o.mois} mois = ${o.montant} €`);
    console.log(`  ⚠ ${p.calculs.garantie.provenance.note}`);
  }
  if (p.calculs.acquisition) {
    const a = p.calculs.acquisition;
    console.log('\nAcquisition (estimation) :');
    console.log(`  Droits nets : ${a.frais.droitsNets} € | crédit Bëllegen Akt : ${a.creditBellegenAkt} €`);
    console.log(`  Honoraires notaire : ${a.honorairesNotaire} € | frais totaux : ${a.fraisTotaux} €`);
    console.log(`  ⚠ ${a.provenance.note}`);
  }
}

switch (sous) {
  case 'locataire':
    afficherParcours(parcoursLogement({ statutLogement: 'locataire' }, { projet: 'location', loyerMensuel: num(arg('--loyer')) }));
    break;
  case 'acheteur':
    afficherParcours(parcoursLogement({}, { projet: 'achat', prixAchat: num(arg('--prix')), nbAcquereurs: num(arg('--acquereurs')) || 1, luxVille: has('--lux-ville'), dateActe: arg('--date-acte') }));
    break;
  case 'proprietaire':
    afficherParcours(parcoursLogement({ statutLogement: 'proprietaire' }));
    break;
  case 'vendeur':
    afficherParcours(parcoursLogement({}, { projet: 'vente' }));
    break;
  case 'garantie': {
    const g = garantieLocativeMax(num(arg('--loyer')));
    for (const o of g.options) console.log(`${o.mois} mois = ${o.montant} €`);
    console.log(`⚠ ${g.provenance.note}\nSource : ${g.provenance.source}`);
    break;
  }
  default:
    console.log(`Usage :
  paperasse logement locataire    --loyer 1200
  paperasse logement acheteur     --prix 600000 --acquereurs 2 [--lux-ville] [--date-acte YYYY-MM-DD]
  paperasse logement proprietaire
  paperasse logement vendeur
  paperasse logement garantie     --loyer 1200`);
    process.exit(sous ? 1 : 0);
}
