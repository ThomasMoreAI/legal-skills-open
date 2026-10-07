/**
 * lib/frontaliers — Comparateur de net réel pour frontaliers travaillant au Luxembourg.
 *
 * Couvre les trois conventions fiscales bilatérales applicables aux résidents
 * FR / BE / DE qui exercent une activité salariée au Luxembourg :
 *
 *   - Convention LU–FR : Convention du 20 mars 1958, refondue par la nouvelle
 *     convention du 20 mars 2018 (entrée en vigueur fiscale au 1er janvier 2020).
 *   - Convention LU–BE : Convention du 17 septembre 1970, modifiée par l'avenant
 *     du 5 décembre 2017 (relevé à 34 jours par avenant du 31 août 2021).
 *   - Convention LU–DE : Convention du 23 avril 2012 (en vigueur 2014), avec
 *     accord amiable sur le télétravail relevé à 34 jours (avenant signé 2023,
 *     en vigueur fiscale 2024).
 *
 * MÉTHODE COMMUNE :
 *   Les trois conventions attribuent au Luxembourg le droit d'imposer le salaire
 *   du frontalier (article 14/15 selon convention). Le pays de résidence applique
 *   ensuite la « méthode d'exonération avec réserve de progressivité » : le
 *   revenu LU est exonéré, mais pris en compte pour calculer le taux moyen
 *   d'imposition applicable aux autres revenus du foyer dans le pays de résidence.
 *
 * AJUSTEMENT « RÉSIDENCE » modélisé :
 *   - FR : 0 € (exonération avec progressivité, sans impact si pas d'autres
 *     revenus français à imposer).
 *   - DE : 0 € (Progressionsvorbehalt, idem).
 *   - BE : taxe communale additionnelle (centimes additionnels) calculée sur
 *     l'IPP belge théorique du revenu LU. Spécificité belge : malgré l'exonération
 *     fédérale, les communes prélèvent un additionnel d'environ 7 à 8,5 % calculé
 *     comme si l'impôt fédéral avait été dû. Taux par défaut : 7,5 %.
 *
 * LIMITATIONS :
 *   - Calcul indicatif. Ne remplace pas la déclaration officielle dans le pays
 *     de résidence (déclaration 2042 pour FR, IPP pour BE, ESt 1 A pour DE).
 *   - Ne tient pas compte des autres revenus du foyer (qui modifient le taux
 *     effectif via la réserve de progressivité).
 *   - L'IPP belge utilisé pour la base communale est une approximation par
 *     barème 2025 simplifié, sans abattements personnels au-delà de la quotité
 *     exemptée standard.
 *
 * USAGE :
 *   import { calculerNetFrontalier } from './lib/frontaliers/index.js';
 *   const r = calculerNetFrontalier({
 *     salaireBrutMensuel: 5000, paysResidence: 'FR', classe: '1'
 *   });
 *   // → { netLuMensuel, retenueLuMensuel, ajustementResidenceMensuel,
 *   //     netFinalMensuel, netFinalAnnuel, avertissements, ... }
 */

import { calculerRTS } from '../rts/index.js';

const PAYS = ['FR', 'BE', 'DE'];

/**
 * Tolérances de jours travaillés hors LU sans perdre le statut « salaire LU ».
 *
 * Les seuils HISTORIQUES (avant les avenants successifs) étaient :
 *   - FR : 19 jours (avenant 2014, en vigueur jusqu'à fin 2022)
 *   - BE : 24 jours (avenant 2015, en vigueur jusqu'à fin 2021)
 *   - DE : 19 jours (convention 2012, en vigueur jusqu'à fin 2023)
 *
 * Les seuils ACTUELS sont harmonisés à 34 jours pour les trois pays :
 *   - FR : 34 jours (avenant signé 7 nov. 2022, applicable 2023)
 *   - BE : 34 jours (avenant signé 31 août 2021, applicable 2022)
 *   - DE : 34 jours (accord amiable signé 2023, applicable 2024)
 *
 * Au-delà du seuil, la part de salaire correspondant aux jours travaillés
 * dans le pays de résidence (ou dans un État tiers) bascule dans la fiscalité
 * locale du pays concerné.
 */
export const SEUIL_JOURS_FRONTALIER = {
  FR: { actuel: 34, historique: 19, sourceActuel: 'Avenant LU-FR du 7 novembre 2022 (applicable 2023)' },
  BE: { actuel: 34, historique: 24, sourceActuel: 'Avenant LU-BE du 31 août 2021 (applicable 2022)' },
  DE: { actuel: 34, historique: 19, sourceActuel: 'Accord amiable LU-DE 2023 (applicable 2024)' },
};

/**
 * Barème IPP belge 2025 — tranches en revenu annuel imposable (€).
 * Source : SPF Finances, exercice d'imposition 2026 (revenus 2025).
 */
export const BAREME_IPP_BE_2025 = [
  { jusquA: 15820,   taux: 0.25 },
  { jusquA: 27920,   taux: 0.40 },
  { jusquA: 48320,   taux: 0.45 },
  { jusquA: Infinity, taux: 0.50 },
];

/** Quotité du revenu exemptée d'impôt en Belgique (revenus 2025). */
export const QUOTITE_EXEMPTEE_BE_2025 = 10570;

/** Taux moyen de centimes additionnels communaux en Belgique (indicatif). */
export const TAUX_COMMUNAL_BE_DEFAUT = 0.075;

/**
 * @param {object} input
 * @param {number} input.salaireBrutMensuel        Salaire brut mensuel LU (€)
 * @param {'FR'|'BE'|'DE'} input.paysResidence     Pays de résidence du frontalier
 * @param {'1'|'1a'|'2'} input.classe              Classe d'impôt LU
 * @param {boolean} [input.cisActif=true]          Crédit d'impôt salarié LU
 * @param {boolean} [input.cimActif=false]         Crédit d'impôt monoparental LU
 * @param {number}  [input.deductionsAnnuelles=0]  Déductions LU annuelles
 * @param {number}  [input.tauxCommunalBE]         Taux d'additionnel communal BE (défaut 7,5 %)
 * @param {number}  [input.joursHorsLU=0]          Jours travaillés hors LU sur l'année
 * @returns {object}
 */
export function calculerNetFrontalier(input) {
  const erreurs = validerInput(input);
  if (erreurs.length) {
    const e = new Error(`Entrée invalide :\n  - ${erreurs.join('\n  - ')}`);
    e.erreurs = erreurs;
    throw e;
  }

  const {
    salaireBrutMensuel,
    paysResidence,
    classe,
    cisActif = true,
    cimActif = false,
    deductionsAnnuelles = 0,
    tauxCommunalBE = TAUX_COMMUNAL_BE_DEFAUT,
    joursHorsLU = 0,
  } = input;

  const lu = calculerRTS({
    salaireBrutMensuel,
    classe,
    cisActif,
    cimActif,
    deductionsAnnuelles,
    frontalier: true,
  });

  const retenueLuMensuel = round2(lu.csss.total + lu.irppMensuel + lu.contribDependance);

  let ajustementResidenceMensuel = 0;
  const detailsResidence = { pays: paysResidence };

  if (paysResidence === 'FR') {
    // Convention LU-FR 2018, art. 14 : salaire imposé au LU.
    // Méthode d'élimination (art. 22) : exonération avec progressivité côté FR.
    // Net effectif = net LU si pas d'autres revenus FR du foyer.
    ajustementResidenceMensuel = 0;
    detailsResidence.methode = 'exonération avec progressivité (taux effectif)';
    detailsResidence.formulaireResidence = 'Déclaration 2042 + 2047 (revenus de source étrangère)';
  } else if (paysResidence === 'DE') {
    // Convention LU-DE 2012, art. 14 : salaire imposé au LU.
    // Méthode d'élimination (art. 22) : Freistellung mit Progressionsvorbehalt.
    ajustementResidenceMensuel = 0;
    detailsResidence.methode = 'Freistellung mit Progressionsvorbehalt';
    detailsResidence.formulaireResidence = 'Anlage N-AUS (revenus salariés étrangers)';
  } else if (paysResidence === 'BE') {
    // Convention LU-BE 1970/2017, art. 15 : salaire imposé au LU.
    // Méthode d'élimination (art. 23) : exonération avec réserve de progressivité.
    // SPÉCIFICITÉ BELGE : malgré l'exonération fédérale, les communes prélèvent
    // un additionnel calculé sur l'IPP fédéral théorique du revenu exonéré.
    const baseIppAnnuelle = Math.max(0, lu.revenuImposableAnnuel - QUOTITE_EXEMPTEE_BE_2025);
    const ippFederalTheorique = round2(impotBaremeBE(baseIppAnnuelle));
    const additionnelCommunalAnnuel = round2(ippFederalTheorique * tauxCommunalBE);
    ajustementResidenceMensuel = round2(additionnelCommunalAnnuel / 12);
    detailsResidence.methode = 'exonération avec progressivité + additionnels communaux';
    detailsResidence.formulaireResidence = 'Déclaration IPP, code 1250/2250 (revenus exonérés étrangers)';
    detailsResidence.ippFederalTheoriqueAnnuel = ippFederalTheorique;
    detailsResidence.tauxCommunalApplique = tauxCommunalBE;
    detailsResidence.additionnelCommunalAnnuel = additionnelCommunalAnnuel;
  }

  const netFinalMensuel = round2(lu.netMensuel - ajustementResidenceMensuel);
  const netFinalAnnuel = round2(netFinalMensuel * 12);
  const tauxRetenueGlobal = round2((1 - netFinalMensuel / salaireBrutMensuel) * 1000) / 1000;

  return {
    salaireBrutMensuel,
    paysResidence,
    classe,
    netLuMensuel: lu.netMensuel,
    netLuAnnuel: lu.netAnnuel,
    retenueLuMensuel,
    ajustementResidenceMensuel,
    ajustementResidenceAnnuel: round2(ajustementResidenceMensuel * 12),
    netFinalMensuel,
    netFinalAnnuel,
    tauxRetenueGlobal,
    detailRTS: lu,
    detailsResidence,
    seuilJours: SEUIL_JOURS_FRONTALIER[paysResidence],
    joursHorsLU,
    avertissements: avertissements({ paysResidence, joursHorsLU }),
  };
}

/**
 * Calcule l'IPP fédéral belge annuel selon le barème 2025 (revenus 2025).
 * @param {number} revenuAnnuel  Revenu net imposable annuel (€), après quotité exemptée.
 * @returns {number} IPP fédéral en €
 */
export function impotBaremeBE(revenuAnnuel) {
  if (revenuAnnuel <= 0) return 0;
  let impot = 0, prev = 0;
  for (const { jusquA, taux } of BAREME_IPP_BE_2025) {
    const tranche = Math.min(revenuAnnuel, jusquA) - prev;
    if (tranche <= 0) break;
    impot += tranche * taux;
    prev = jusquA;
    if (revenuAnnuel <= jusquA) break;
  }
  return impot;
}

function validerInput(input) {
  const e = [];
  if (!input || typeof input !== 'object') return ['input absent'];
  if (!Number.isFinite(input.salaireBrutMensuel) || input.salaireBrutMensuel <= 0) {
    e.push('salaireBrutMensuel doit être un nombre fini > 0');
  }
  if (!PAYS.includes(input.paysResidence)) {
    e.push(`paysResidence doit être 'FR', 'BE' ou 'DE' (reçu : ${JSON.stringify(input.paysResidence)})`);
  }
  if (!['1', '1a', '2'].includes(input.classe)) {
    e.push(`classe doit être '1', '1a' ou '2' (reçu : ${JSON.stringify(input.classe)})`);
  }
  if (input.tauxCommunalBE !== undefined &&
      (!Number.isFinite(input.tauxCommunalBE) || input.tauxCommunalBE < 0 || input.tauxCommunalBE > 0.5)) {
    e.push('tauxCommunalBE doit être un nombre fini entre 0 et 0,5');
  }
  if (input.joursHorsLU !== undefined &&
      (!Number.isFinite(input.joursHorsLU) || input.joursHorsLU < 0 || input.joursHorsLU > 366)) {
    e.push('joursHorsLU doit être un nombre fini entre 0 et 366');
  }
  return e;
}

function avertissements({ paysResidence, joursHorsLU }) {
  const a = [
    "Calcul indicatif. Ne remplace pas la déclaration officielle dans le pays de résidence.",
  ];
  const seuil = SEUIL_JOURS_FRONTALIER[paysResidence];
  a.push(
    `Régime ${paysResidence} : tolérance actuelle de ${seuil.actuel} jours travaillés hors LU/an `
    + `(seuil historique : ${seuil.historique} jours). Source : ${seuil.sourceActuel}.`
  );
  if (joursHorsLU > seuil.actuel) {
    a.push(
      `⚠ Vous déclarez ${joursHorsLU} jours hors LU, au-delà du seuil de ${seuil.actuel} jours : `
      + `la part proportionnelle du salaire bascule dans la fiscalité de ${paysResidence}. `
      + `Ce calcul ne modélise pas ce reversement — consulter un conseiller fiscal.`
    );
  }
  if (paysResidence === 'BE') {
    a.push(
      "Belgique : malgré l'exonération fédérale, les centimes additionnels communaux "
      + "restent dus sur l'IPP théorique. Le taux par défaut (7,5 %) varie selon votre commune (de 0 à 9 %)."
    );
  }
  if (paysResidence === 'FR') {
    a.push(
      "France : la part LU est prise en compte pour le taux effectif d'imposition "
      + "des autres revenus français du foyer (méthode du taux effectif)."
    );
  }
  if (paysResidence === 'DE') {
    a.push(
      "Allemagne : Progressionsvorbehalt — le revenu LU augmente le taux moyen "
      + "appliqué aux autres revenus allemands du foyer."
    );
  }
  return a;
}

function round2(n) { return Math.round(n * 100) / 100; }
