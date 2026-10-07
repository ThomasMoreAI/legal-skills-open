/**
 * lib/diagnostic/provenance.js — Traçabilité des informations réglementaires.
 *
 * Principe produit central : le système ne doit JAMAIS afficher une règle,
 * un délai, un montant ou une obligation sans y attacher :
 *   - une source officielle (`source`) ;
 *   - une date de dernière vérification (`dateVerification`) ;
 *   - un niveau de confiance (`niveauConfiance`) ;
 *   - une mention claire lorsqu'une validation humaine est nécessaire
 *     (`validationHumaineRequise`).
 *
 * Ce module fournit la structure `Provenance` commune à toutes les entités
 * du moteur de diagnostic, ainsi que les helpers de fraîcheur.
 *
 * Aucune dépendance externe.
 */

/**
 * Niveaux de confiance, du plus fiable au moins fiable.
 *   - officiel   : repris tel quel d'une source officielle vérifiée.
 *   - derive     : calculé/déduit à partir d'une règle officielle.
 *   - estimation : approximation (barème simplifié, moyenne, ordre de grandeur).
 *   - incertain  : n'a pas pu être vérifié — nécessite une validation humaine.
 */
export const NIVEAUX_CONFIANCE = Object.freeze(['officiel', 'derive', 'estimation', 'incertain']);

/**
 * Délai (en jours) au-delà duquel une information sourcée est considérée
 * comme « à revérifier avant utilisation ». La réglementation luxembourgeoise
 * (barèmes, seuils, SSM, taux TVA) évolue au moins annuellement.
 */
export const FRAICHEUR_JOURS_DEFAUT = 365;

const RE_DATE = /^\d{4}-\d{2}-\d{2}$/;

function estDateISO(v) {
  return typeof v === 'string' && RE_DATE.test(v) && !Number.isNaN(Date.parse(`${v}T00:00:00Z`));
}

/**
 * Construit un objet de provenance normalisé et validé.
 *
 * @param {object} p
 * @param {string} p.source                URL ou libellé de la source officielle (obligatoire).
 * @param {string} p.dateVerification       Date de dernière vérification (YYYY-MM-DD, obligatoire).
 * @param {string} [p.niveauConfiance]      Un des NIVEAUX_CONFIANCE (défaut : 'officiel').
 * @param {boolean} [p.validationHumaineRequise] Défaut : false, forcé à true si niveau 'incertain'.
 * @param {string} [p.note]                 Précision libre (ex : « barème 2025 simplifié »).
 * @returns {{source, dateVerification, niveauConfiance, validationHumaineRequise, note?}}
 */
export function creerProvenance({
  source,
  dateVerification,
  niveauConfiance = 'officiel',
  validationHumaineRequise = false,
  note,
} = {}) {
  if (!source || typeof source !== 'string') {
    throw new Error('provenance.source est obligatoire (URL ou libellé de la source officielle)');
  }
  if (!estDateISO(dateVerification)) {
    throw new Error('provenance.dateVerification est obligatoire (format YYYY-MM-DD valide)');
  }
  if (!NIVEAUX_CONFIANCE.includes(niveauConfiance)) {
    throw new Error(`provenance.niveauConfiance invalide : "${niveauConfiance}" (attendu : ${NIVEAUX_CONFIANCE.join(', ')})`);
  }
  const prov = {
    source,
    dateVerification,
    niveauConfiance,
    // Une information incertaine impose toujours une validation humaine.
    validationHumaineRequise: Boolean(validationHumaineRequise) || niveauConfiance === 'incertain',
  };
  if (note) prov.note = String(note);
  return prov;
}

/**
 * Nombre de jours écoulés entre deux dates ISO (YYYY-MM-DD).
 */
export function joursEcoules(depuis, jusqua) {
  const a = Date.parse(`${depuis}T00:00:00Z`);
  const b = Date.parse(`${jusqua}T00:00:00Z`);
  return Math.floor((b - a) / 86_400_000);
}

/**
 * Indique si une provenance doit être revérifiée avant usage.
 *
 * @param {object} provenance          Objet issu de creerProvenance().
 * @param {object} [opts]
 * @param {string} [opts.aujourdhui]   Date de référence (YYYY-MM-DD). Défaut : aujourd'hui (UTC).
 * @param {number} [opts.seuilJours]   Seuil de fraîcheur. Défaut : FRAICHEUR_JOURS_DEFAUT.
 * @returns {{aRevalider: boolean, joursDepuisVerification: number, message: string|null}}
 */
export function evaluerFraicheur(provenance, { aujourdhui = ceJourISO(), seuilJours = FRAICHEUR_JOURS_DEFAUT } = {}) {
  if (!provenance || !estDateISO(provenance.dateVerification)) {
    return { aRevalider: true, joursDepuisVerification: Infinity, message: 'Aucune date de vérification : information à revérifier avant utilisation.' };
  }
  const jours = joursEcoules(provenance.dateVerification, aujourdhui);
  const aRevalider = jours > seuilJours || provenance.niveauConfiance === 'incertain';
  return {
    aRevalider,
    joursDepuisVerification: jours,
    message: aRevalider ? 'Cette information doit être revérifiée avant utilisation.' : null,
  };
}

/**
 * Date du jour au format YYYY-MM-DD (UTC). Injectable partout via un paramètre
 * `aujourdhui` pour garder les tests déterministes.
 */
export function ceJourISO() {
  return new Date().toISOString().slice(0, 10);
}
