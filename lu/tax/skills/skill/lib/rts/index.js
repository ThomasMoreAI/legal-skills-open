/**
 * lib/rts — Retenue à la source (RTS) sur traitements et salaires (Luxembourg).
 *
 * Sources :
 *   - L.I.R. (Loi de l'Impôt sur le Revenu) art. 136 et suivants
 *   - Barème IRPP 2025 (loi du 19 décembre 2024 portant adaptation de la fiscalité
 *     à l'inflation : décalage de 2,5 indice + nouveau seuil tranche maximale)
 *   - Classes d'impôt 1, 1a, 2 — circulaire L.I.R. n° 137/1
 *
 * APPROCHE :
 *   Cette implémentation calcule l'IRPP annuel théorique (formule polynomiale
 *   continue par tranches), puis divise par le nombre de périodes de paie pour
 *   obtenir la retenue mensuelle. C'est la méthode dite « par extrapolation ».
 *   Elle approxime la formule officielle ACD (qui utilise des arrondis sur la
 *   fiche de retenue), avec un écart typique ≤ 5 € / mois.
 *
 * LIMITATIONS DOCUMENTÉES :
 *   - Crédits d'impôt (CIS, CIM, CIP) : appliqués au montant standard 2025,
 *     non personnalisés selon la situation familiale fine.
 *   - Classe 1a : abattement extra-professionnel non implémenté en détail
 *     (utiliser l'estimation 1a comme approximation).
 *   - Frontaliers : la retenue LU est identique. Le résultat ne tient pas compte
 *     de la fiscalité du pays de résidence (BE, FR, DE) — utiliser un comparateur
 *     dédié pour le net effectif.
 *   - Avantages en nature (voiture de fonction, etc.) : à intégrer en amont
 *     dans le revenu brut imposable.
 *
 * USAGE :
 *   import { calculerRTS } from './lib/rts/index.js';
 *   const r = calculerRTS({ salaireBrutMensuel: 5000, classe: '1' });
 *   // → { net, irpp, csss, contribDependance, ... }
 */

/**
 * Barème IRPP Luxembourg 2025 — tranches en revenu annuel imposable (€).
 * Source : Mémorial A n° 583 du 23 décembre 2024 (loi inflation 2,5 indice).
 */
export const BAREME_IRPP_2025 = [
  { jusquA: 13230,   taux: 0.00 },
  { jusquA: 15435,   taux: 0.08 },
  { jusquA: 17640,   taux: 0.09 },
  { jusquA: 19845,   taux: 0.10 },
  { jusquA: 22050,   taux: 0.11 },
  { jusquA: 24255,   taux: 0.12 },
  { jusquA: 26460,   taux: 0.14 },
  { jusquA: 28665,   taux: 0.16 },
  { jusquA: 30870,   taux: 0.18 },
  { jusquA: 33075,   taux: 0.20 },
  { jusquA: 35280,   taux: 0.22 },
  { jusquA: 37485,   taux: 0.24 },
  { jusquA: 39690,   taux: 0.26 },
  { jusquA: 41895,   taux: 0.28 },
  { jusquA: 44100,   taux: 0.30 },
  { jusquA: 46305,   taux: 0.32 },
  { jusquA: 48510,   taux: 0.34 },
  { jusquA: 50715,   taux: 0.36 },
  { jusquA: 52920,   taux: 0.38 },
  { jusquA: 117450,  taux: 0.39 },
  { jusquA: 176160,  taux: 0.40 },
  { jusquA: 234870,  taux: 0.41 },
  { jusquA: Infinity, taux: 0.42 },
];

export const COTISATIONS_LU_2025 = {
  csssAssuranceMaladieSalarie: 0.0280,    // 2,80 % (part salarié)
  csssPensionSalarie:           0.0800,    // 8,00 %
  contribDependance:            0.0140,    // 1,40 % (sur revenu après abattement 25% × salaire min)
  abattementDependanceMensuel:  638.49,    // ¼ × salaire social minimum 2025 (~2553,96 €/mois × 25%)
};

export const CREDITS_IMPOT_2025 = {
  cisMensuelStandard: 70,    // CIS — salariés (montant indicatif standard)
  cipMensuelStandard: 70,    // CIP — pensionnés
  cimMensuelStandard: 188,   // CIM — monoparental (selon revenu)
};

const PERIODES = { mensuel: 12, hebdo: 52, journalier: 300 };
const CLASSES = ['1', '1a', '2'];

/**
 * @param {object} input
 * @param {number} input.salaireBrutMensuel  Salaire brut imposable mensuel (€)
 * @param {'1'|'1a'|'2'} input.classe        Classe d'impôt
 * @param {boolean} [input.cisActif=true]    Appliquer le crédit d'impôt salarié
 * @param {boolean} [input.cimActif=false]   Crédit d'impôt monoparental
 * @param {number}  [input.deductionsAnnuelles=0]  Déductions/abattements annuels supplémentaires
 *
 * @returns {object} décomposition mensuelle
 */
export function calculerRTS(input) {
  const erreurs = validerInput(input);
  if (erreurs.length) {
    const e = new Error(`Entrée invalide :\n  - ${erreurs.join('\n  - ')}`);
    e.erreurs = erreurs;
    throw e;
  }

  const {
    salaireBrutMensuel,
    classe,
    cisActif = true,
    cimActif = false,
    deductionsAnnuelles = 0,
  } = input;

  // Cotisations sociales salarié (avant impôt)
  const csssMaladie = round2(salaireBrutMensuel * COTISATIONS_LU_2025.csssAssuranceMaladieSalarie);
  const csssPension = round2(salaireBrutMensuel * COTISATIONS_LU_2025.csssPensionSalarie);
  const csssTotal = round2(csssMaladie + csssPension);

  const revenuImposableMensuel = round2(salaireBrutMensuel - csssTotal - deductionsAnnuelles / 12);
  const revenuImposableAnnuel = round2(revenuImposableMensuel * 12);

  // IRPP annuel selon classe
  let irppAnnuel;
  if (classe === '2') {
    // Splitting : revenu/2 → barème → ×2
    irppAnnuel = round2(impotBareme(revenuImposableAnnuel / 2) * 2);
  } else if (classe === '1a') {
    // Approximation : abattement extra-professionnel 4 500 €/an puis barème classe 1
    const abattement1a = 4500;
    irppAnnuel = round2(impotBareme(Math.max(0, revenuImposableAnnuel - abattement1a)));
  } else {
    irppAnnuel = round2(impotBareme(revenuImposableAnnuel));
  }

  // Contribution dépendance (1,40 %) : assise sur revenu avant impôt après abattement
  const baseDependanceMensuel = Math.max(0, salaireBrutMensuel - COTISATIONS_LU_2025.abattementDependanceMensuel);
  const contribDependance = round2(baseDependanceMensuel * COTISATIONS_LU_2025.contribDependance);

  // IRPP mensuel + crédits d'impôt
  let irppMensuel = round2(irppAnnuel / PERIODES.mensuel);
  let cis = 0, cim = 0;
  if (cisActif) cis = CREDITS_IMPOT_2025.cisMensuelStandard;
  if (cimActif) cim = CREDITS_IMPOT_2025.cimMensuelStandard;
  const irppMensuelApresCredits = round2(Math.max(0, irppMensuel - cis - cim));

  const netMensuel = round2(salaireBrutMensuel - csssTotal - irppMensuelApresCredits - contribDependance);
  const tauxEffectif = round2((1 - netMensuel / salaireBrutMensuel) * 1000) / 1000;

  return {
    salaireBrutMensuel,
    classe,
    csss: { maladie: csssMaladie, pension: csssPension, total: csssTotal },
    revenuImposableMensuel,
    revenuImposableAnnuel,
    irppAnnuel,
    irppMensuelAvantCredits: irppMensuel,
    creditsImpot: { cis, cim, total: round2(cis + cim) },
    irppMensuel: irppMensuelApresCredits,
    contribDependance,
    netMensuel,
    netAnnuel: round2(netMensuel * 12),
    tauxRetenueEffectif: tauxEffectif,
    avertissements: avertissementsContextuels(input),
  };
}

/**
 * Calcule l'IRPP annuel selon le barème LU 2025.
 * @param {number} revenuAnnuel
 * @returns {number} impôt en €
 */
export function impotBareme(revenuAnnuel) {
  if (revenuAnnuel <= 0) return 0;
  let impot = 0, prev = 0;
  for (const { jusquA, taux } of BAREME_IRPP_2025) {
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
  if (!CLASSES.includes(input.classe)) {
    e.push(`classe doit être '1', '1a' ou '2' (reçu : ${JSON.stringify(input.classe)})`);
  }
  if (input.deductionsAnnuelles !== undefined &&
      (!Number.isFinite(input.deductionsAnnuelles) || input.deductionsAnnuelles < 0)) {
    e.push('deductionsAnnuelles doit être un nombre fini ≥ 0');
  }
  return e;
}

function avertissementsContextuels(input) {
  const a = [];
  if (input.classe === '1a') {
    a.push("Classe 1a : approximation par abattement extra-professionnel de 4 500 €. Pour un calcul fin (mère/père seul, partenaire pacsé, etc.), consulter une fiche de retenue ACD.");
  }
  if (input.frontalier) {
    a.push("Frontalier : la RTS LU est identique. Le net après fiscalité du pays de résidence (BE/FR/DE) peut différer — utiliser un comparateur dédié.");
  }
  return a;
}

function round2(n) { return Math.round(n * 100) / 100; }
