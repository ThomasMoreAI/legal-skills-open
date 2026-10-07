#!/usr/bin/env node
/**
 * bellegen-akt.js — CLI : calcul des droits d'enregistrement et du crédit
 * d'impôt « Bëllegen Akt » pour une acquisition immobilière au Luxembourg.
 *
 * Usage :
 *   paperasse bellegen-akt --prix 600000 --acquereurs 2 --lux-ville
 *   paperasse bellegen-akt --prix 800000 --acquereurs 2 --lux-ville --date 2024-09-30
 */

import { calculerBellegenAkt } from '../lib/bellegen-akt/index.js';

const args = process.argv.slice(2);
function arg(name, def) {
  const i = args.indexOf('--' + name);
  if (i === -1) return def;
  const v = args[i + 1];
  if (v === undefined || v.startsWith('--')) return true;
  return v;
}
function flag(name) { return args.includes('--' + name); }

if (args.length === 0 || flag('help') || flag('h')) {
  console.error(`Usage : paperasse bellegen-akt --prix <€> [options]

Options :
  --prix <€>          Prix d'acquisition (obligatoire)
  --acquereurs <n>    Nombre d'acquéreurs (défaut : 1)
  --lux-ville         Bien situé sur la commune de Luxembourg-Ville (+3 % surtaxe)
  --no-bellegen-akt   Désactive le crédit d'impôt résidence principale
  --date <YYYY-MM-DD> Date de l'acte (avant 2024-10-01 = ancien plafond 30 000 €/pers.)

Exemples :
  paperasse bellegen-akt --prix 600000 --acquereurs 2
  paperasse bellegen-akt --prix 800000 --acquereurs 2 --lux-ville
  paperasse bellegen-akt --prix 350000 --no-bellegen-akt
`);
  process.exit(args.length === 0 ? 1 : 0);
}

const input = {
  prix: Number(arg('prix')),
  nbAcquereurs: Number(arg('acquereurs', 1)),
  luxVille: flag('lux-ville'),
  bellegenAkt: !flag('no-bellegen-akt'),
  dateActe: arg('date', null),
};

try {
  const r = calculerBellegenAkt(input);
  const eur = (n) => n.toLocaleString('fr-LU', { style: 'currency', currency: 'EUR' });
  console.log(`
=== Calcul Bëllegen Akt ===
  Prix d'acquisition         : ${eur(r.prix)}
  Nombre d'acquéreurs        : ${r.nbAcquereurs}
  Commune                    : ${r.luxVille ? 'Luxembourg-Ville (+3 % surtaxe)' : 'autre'}
  Taux total                 : ${(r.tauxTotal * 100).toFixed(0)} %

  Droits d'enregistrement    : ${eur(r.droitEnregistrement)}
  Droits de transcription    : ${eur(r.droitTranscription)}
  Droits nominaux            : ${eur(r.droitsNominaux)}
  Crédit Bëllegen Akt        : - ${eur(r.bellegenAkt.abattementEffectif)}  (plafond ${eur(r.bellegenAkt.plafondParPersonne)} × ${r.nbAcquereurs})
  Droits NETS à payer        : ${eur(r.droitsNets)}

  Honoraires de notaire      : ${eur(r.honoraires)}
  TVA 17 % sur honoraires    : ${eur(r.tvaHonoraires)}
  Débours estimés            : ${eur(r.debours)}

  TOTAL frais (hors prix)    : ${eur(r.total)}
  Ratio frais / prix         : ${(r.ratioFraisSurPrix * 100).toFixed(2)} %
`);
} catch (e) {
  console.error(`✗ ${e.message}`);
  process.exit(1);
}
