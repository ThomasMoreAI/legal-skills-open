#!/usr/bin/env node
/**
 * calc-tva-declaration.js — Déclaration TVA luxembourgeoise (CA3 équivalent).
 *
 * Calcule la TVA due nette pour une période (mois, trimestre ou année) à partir
 * d'opérations ventilées par taux. Format directement compatible avec les rubriques
 * de la déclaration TVA luxembourgeoise déposée via eCDF.
 *
 * Source : Loi modifiée du 12 février 1979 concernant la TVA
 * URL : https://pfi.public.lu/fr/professionnels/tva.html
 * Taux 2025 : 17 % (normal), 14 % (intermédiaire), 8 % (réduit), 3 % (super-réduit)
 *
 * Usage programmatique :
 *   import { calcDeclarationTVA } from './scripts/calc-tva-declaration.js';
 *   const result = calcDeclarationTVA({
 *     periode: '2025-T3',
 *     operations: {
 *       livraisons_normal_17: 50000,        // HT taxé à 17 %
 *       livraisons_intermediaire_14: 0,
 *       livraisons_reduit_8: 0,
 *       livraisons_super_reduit_3: 12000,    // HT taxé à 3 %
 *       livraisons_intracommunautaires: 8000, // exonérées art. 43
 *       acquisitions_intracommunautaires_17: 5000, // auto-liquidation 17 %
 *       achats_deductibles_17: 20000,        // TVA déductible sur achats
 *       achats_deductibles_3: 1000,
 *     },
 *   });
 *
 * Usage CLI :
 *   node scripts/calc-tva-declaration.js examples/tva-trimestre.json
 */

import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const TAUX_2025 = { normal: 17, intermediaire: 14, reduit: 8, super_reduit: 3 };

const round2 = (n) => Math.round(n * 100) / 100;

/**
 * Calcule la déclaration TVA pour une période.
 *
 * @param {object} input
 * @param {string} input.periode - identifiant lisible (ex : '2025-T3', '2025-09')
 * @param {object} input.operations - montants HT/TVA par rubrique
 * @returns {object} { periode, collectee, deductible, due_nette, lignes_declaration }
 */
export function calcDeclarationTVA({ periode, operations = {} }) {
  const get = (k) => Number(operations[k] || 0);

  // --- TVA collectée (sur livraisons et prestations imposables) ---
  const ht_normal = get('livraisons_normal_17');
  const ht_inter = get('livraisons_intermediaire_14');
  const ht_reduit = get('livraisons_reduit_8');
  const ht_super = get('livraisons_super_reduit_3');
  const ht_intracom = get('livraisons_intracommunautaires'); // exonérées
  const ht_export = get('livraisons_export'); // exonérées hors UE

  const tva_normal = round2((ht_normal * TAUX_2025.normal) / 100);
  const tva_inter = round2((ht_inter * TAUX_2025.intermediaire) / 100);
  const tva_reduit = round2((ht_reduit * TAUX_2025.reduit) / 100);
  const tva_super = round2((ht_super * TAUX_2025.super_reduit) / 100);

  // --- Acquisitions intracommunautaires (auto-liquidation : collectée + déductible) ---
  const aic_ht_17 = get('acquisitions_intracommunautaires_17');
  const aic_ht_14 = get('acquisitions_intracommunautaires_14');
  const aic_ht_8 = get('acquisitions_intracommunautaires_8');
  const aic_ht_3 = get('acquisitions_intracommunautaires_3');
  const aic_tva_17 = round2((aic_ht_17 * 17) / 100);
  const aic_tva_14 = round2((aic_ht_14 * 14) / 100);
  const aic_tva_8 = round2((aic_ht_8 * 8) / 100);
  const aic_tva_3 = round2((aic_ht_3 * 3) / 100);
  const aic_tva_total = round2(aic_tva_17 + aic_tva_14 + aic_tva_8 + aic_tva_3);

  const tva_collectee = round2(tva_normal + tva_inter + tva_reduit + tva_super + aic_tva_total);

  // --- TVA déductible (sur achats et frais professionnels) ---
  const ach_17 = get('achats_deductibles_17');
  const ach_14 = get('achats_deductibles_14');
  const ach_8 = get('achats_deductibles_8');
  const ach_3 = get('achats_deductibles_3');
  const tva_deductible_achats = round2(
    (ach_17 * 17 + ach_14 * 14 + ach_8 * 8 + ach_3 * 3) / 100
  );
  // En auto-liquidation, la TVA acquise sur AIC est aussi déductible
  const tva_deductible = round2(tva_deductible_achats + aic_tva_total);

  // --- Solde ---
  const due_nette = round2(tva_collectee - tva_deductible);

  // --- Lignes prêtes pour le formulaire eCDF (numéros indicatifs) ---
  const lignes_declaration = [
    { code: '012', libelle: 'CA imposable au taux normal 17 %', ht: ht_normal, tva: tva_normal },
    { code: '013', libelle: 'CA imposable au taux intermédiaire 14 %', ht: ht_inter, tva: tva_inter },
    { code: '014', libelle: 'CA imposable au taux réduit 8 %', ht: ht_reduit, tva: tva_reduit },
    { code: '015', libelle: 'CA imposable au taux super-réduit 3 %', ht: ht_super, tva: tva_super },
    { code: '037', libelle: 'Livraisons intracommunautaires exonérées (art. 43)', ht: ht_intracom, tva: 0 },
    { code: '038', libelle: 'Exportations hors UE exonérées', ht: ht_export, tva: 0 },
    { code: '041', libelle: 'Acquisitions intracom. — auto-liquidation', ht: aic_ht_17 + aic_ht_14 + aic_ht_8 + aic_ht_3, tva: aic_tva_total },
    { code: '093', libelle: 'TVA déductible sur achats et frais', ht: ach_17 + ach_14 + ach_8 + ach_3, tva: tva_deductible_achats },
    { code: '700', libelle: 'TVA collectée totale', ht: null, tva: tva_collectee },
    { code: '701', libelle: 'TVA déductible totale', ht: null, tva: tva_deductible },
    { code: '702', libelle: due_nette >= 0 ? 'TVA due au Trésor' : 'Crédit de TVA reportable / restituable', ht: null, tva: Math.abs(due_nette) },
  ];

  return {
    periode,
    taux_appliques: TAUX_2025,
    collectee: tva_collectee,
    deductible: tva_deductible,
    due_nette,
    sens: due_nette >= 0 ? 'à payer au Trésor' : 'crédit en faveur du contribuable',
    lignes_declaration,
    rappel: 'Déclaration à déposer via eCDF. Échéances : mensuelle (15 du mois M+1), trimestrielle (15 du mois suivant le trimestre), annuelle (1er mars). Régime selon CA annuel. Source : pfi.public.lu',
  };
}

// CLI : lit un fichier JSON d'opérations en argument
const isCli = process.argv[1] === fileURLToPath(import.meta.url);
if (isCli) {
  const file = process.argv[2];
  if (!file) {
    console.log('Usage : node scripts/calc-tva-declaration.js <operations.json>');
    console.log('Format du fichier : { "periode": "2025-T3", "operations": { "livraisons_normal_17": 50000, ... } }');
    process.exit(1);
  }
  const input = JSON.parse(readFileSync(file, 'utf8'));
  const result = calcDeclarationTVA(input);
  console.log(JSON.stringify(result, null, 2));
}
