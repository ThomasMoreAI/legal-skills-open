/**
 * generator.js — Générateur de fichier eCDF "Comptes annuels — schéma abrégé".
 *
 * Produit un document XML structuré dont les rubriques correspondent au
 * formulaire eCDF CA-A, alimenté à partir d'une balance des comptes PCN.
 *
 * Usage :
 *   import { generateECDF } from './lib/ecdf/generator.js';
 *   const xml = generateECDF({
 *     societe: { rcs: 'B12345', tva: 'LU12345678', denomination: 'ACME SARL', forme: 'SARL' },
 *     exercice: { debut: '2025-01-01', fin: '2025-12-31', devise: 'EUR' },
 *     balance: { '101': -10000, '20': 500, '21': 30000, ... }  // soldes par compte PCN
 *   });
 *
 * IMPORTANT : ce fichier est une représentation conforme à la structure du
 * formulaire eCDF CA-A. Pour un dépôt légal réel, charger le fichier dans le
 * tester officiel https://ecdf.b2g.etat.lu/ pour validation finale.
 */

import { BILAN_ACTIF, BILAN_PASSIF, COMPTE_RESULTAT, META_FORM } from './mappings.js';

/**
 * Agrège les soldes de comptes PCN selon une liste de préfixes.
 * Ex : prefixes=['21','22'] additionne tous les comptes commençant par 21 ou 22.
 */
function sumByPrefixes(balance, prefixes) {
  if (!prefixes || prefixes.length === 0) return 0;
  let total = 0;
  for (const [compte, solde] of Object.entries(balance)) {
    if (prefixes.some(p => compte.startsWith(p))) total += Number(solde) || 0;
  }
  return total;
}

/**
 * Calcule la valeur d'une rubrique en appliquant le signe.
 * - Actif (signe +1) : solde débiteur attendu, valeur eCDF = +solde
 * - Passif/produits (signe -1) : solde créditeur attendu (négatif au PCN), valeur eCDF = -solde (donc positif)
 */
function valueOf(rubrique, balance) {
  const raw = sumByPrefixes(balance, rubrique.pcn);
  return Math.round(raw * rubrique.signe * 100) / 100;
}

function calculerResultat(balance) {
  // Résultat = produits (classe 7) - charges (classe 6, hors impôts non opérationnels traités à part)
  // Convention PCN : classe 7 créditrice (négatif), classe 6 débitrice (positif).
  // Résultat positif = bénéfice si produits > charges → solde créditeur (négatif au PCN).
  const produits = -sumByPrefixes(balance, ['70', '71', '72', '74', '75', '76', '77', '78']);
  const charges = sumByPrefixes(balance, ['60', '61', '62', '63', '64', '65', '66', '67', '68', '69']);
  return Math.round((produits - charges) * 100) / 100;
}

function escapeXML(s) {
  return String(s ?? '').replace(/[<>&"']/g, c => ({'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;',"'":'&apos;'}[c]));
}

function fmt(n) { return (Math.round(n * 100) / 100).toFixed(2); }

/**
 * Génère un objet structuré (utile pour tests + JSON debug).
 */
export function buildECDFData({ societe, exercice, balance }) {
  if (!societe?.rcs) throw new Error('societe.rcs manquant');
  if (!exercice?.debut || !exercice?.fin) throw new Error('exercice.debut et exercice.fin requis');

  const resultat = calculerResultat(balance);
  const enrichi = { ...balance, __resultat: resultat };

  const buildSection = (rubriques) => rubriques.map(r => ({
    code: r.code,
    libelle: r.libelle,
    valeur: r.calcule === 'resultat' ? Math.round(resultat * 100) / 100 : valueOf(r, enrichi),
    agregat: !!r.agregat,
    total: !!r.total,
  }));

  const actif = buildSection(BILAN_ACTIF);
  const passif = buildSection(BILAN_PASSIF);
  const cr = buildSection(COMPTE_RESULTAT);

  // Calcul des totaux (rubriques marquées total:true)
  const totalActif = actif.filter(r => !r.total && !r.agregat).reduce((a, b) => a + b.valeur, 0);
  const totalPassif = passif.filter(r => !r.total && !r.agregat).reduce((a, b) => a + b.valeur, 0);
  actif.find(r => r.total).valeur = Math.round(totalActif * 100) / 100;
  passif.find(r => r.total).valeur = Math.round(totalPassif * 100) / 100;

  const ecart = Math.round((totalActif - totalPassif) * 100) / 100;

  return {
    meta: META_FORM,
    societe,
    exercice,
    bilan: { actif, passif, total_actif: totalActif, total_passif: totalPassif, ecart },
    compte_resultat: cr,
    resultat_calcule: resultat,
    coherence: {
      bilan_equilibre: Math.abs(ecart) < 1,
      ecart_actif_passif: ecart,
      remarque: Math.abs(ecart) >= 1
        ? 'Bilan déséquilibré — vérifier la balance PCN avant dépôt eCDF.'
        : 'Bilan équilibré.',
    },
  };
}

/**
 * Génère le document XML eCDF (CA-A).
 */
export function generateECDF(input) {
  const data = buildECDFData(input);
  const { societe, exercice, bilan, compte_resultat: cr } = data;

  const renderRubriques = (rubriques, indent = '    ') => rubriques.map(r =>
    `${indent}<Rubrique code="${r.code}"${r.total ? ' total="true"' : ''}${r.agregat ? ' agregat="true"' : ''}>
${indent}  <Libelle>${escapeXML(r.libelle)}</Libelle>
${indent}  <Valeur>${fmt(r.valeur)}</Valeur>
${indent}</Rubrique>`).join('\n');

  return `<?xml version="1.0" encoding="UTF-8"?>
<!--
  Fichier eCDF — Comptes annuels schéma abrégé (CA-A)
  Généré par paperasse-lux v0.5.0 le ${new Date().toISOString()}
  ATTENTION : à valider sur le tester officiel https://ecdf.b2g.etat.lu/ avant dépôt légal.
  ${data.coherence.bilan_equilibre ? '' : 'AVERTISSEMENT : ' + data.coherence.remarque}
-->
<DeclarationECDF type="${META_FORM.type_formulaire}" version="1.0">
  <Identification>
    <RCS>${escapeXML(societe.rcs)}</RCS>
    <MatriculeTVA>${escapeXML(societe.tva || '')}</MatriculeTVA>
    <Denomination>${escapeXML(societe.denomination)}</Denomination>
    <FormeJuridique>${escapeXML(societe.forme || '')}</FormeJuridique>
  </Identification>
  <Exercice>
    <Debut>${escapeXML(exercice.debut)}</Debut>
    <Fin>${escapeXML(exercice.fin)}</Fin>
    <Devise>${escapeXML(exercice.devise || 'EUR')}</Devise>
  </Exercice>
  <Bilan>
    <Actif>
${renderRubriques(bilan.actif, '      ')}
    </Actif>
    <Passif>
${renderRubriques(bilan.passif, '      ')}
    </Passif>
    <Coherence equilibre="${data.coherence.bilan_equilibre}" ecart="${fmt(bilan.ecart)}"/>
  </Bilan>
  <CompteDeResultat>
${renderRubriques(cr, '    ')}
  </CompteDeResultat>
</DeclarationECDF>
`;
}
