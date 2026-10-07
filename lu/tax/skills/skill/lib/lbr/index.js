/**
 * lib/lbr — Helpers Registre de Commerce et des Sociétés (LBR) Luxembourg.
 *
 * Ne fait PAS de scraping du portail lbr.lu (JSP avec session, instable).
 * Fournit à la place :
 *   - validation du format des numéros RCS
 *   - construction d'URL de recherche profonde (que l'utilisateur ouvre dans son navigateur)
 *   - checklists de pièces à déposer selon le type d'opération
 *   - calendrier des dépôts obligatoires
 *
 * Source : Luxembourg Business Registers (lbr.lu), tarifs 2026.
 */

import { CHECKLISTS_LBR, OPERATIONS } from './checklists.js';

export { CHECKLISTS_LBR, OPERATIONS };

/**
 * Valide un numéro RCS luxembourgeois.
 * Format : lettre de catégorie + chiffres.
 *   B = sociétés commerciales (SARL, SA, SCS, SCA, etc.)
 *   F = fonds d'investissement
 *   G = GIE (Groupement d'intérêt économique)
 *   E = sociétés européennes
 *   K = succursales
 *   X = associations sans but lucratif (ASBL) et fondations
 *
 * @param {string} rcs ex: "B12345" ou "b12345" ou "B 12345"
 * @returns {{valide: boolean, normalise: string|null, categorie: string|null, raison?: string}}
 */
export function validerRCS(rcs) {
  if (!rcs || typeof rcs !== 'string') {
    return { valide: false, normalise: null, categorie: null, raison: 'RCS vide ou invalide' };
  }
  const clean = rcs.toUpperCase().replace(/\s+/g, '');
  const m = clean.match(/^([BFGEKX])(\d{1,7})$/);
  if (!m) {
    return {
      valide: false,
      normalise: null,
      categorie: null,
      raison: 'Format attendu : lettre (B/F/G/E/K/X) + 1 à 7 chiffres (ex: B12345)',
    };
  }
  const CATEGORIES = {
    B: 'Société commerciale (SARL, SA, SCS, SCA, ...)',
    F: 'Fonds d\'investissement (FCP, SICAV)',
    G: 'Groupement d\'intérêt économique (GIE)',
    E: 'Société européenne (SE)',
    K: 'Succursale d\'entité étrangère',
    X: 'Association sans but lucratif (ASBL) ou fondation',
  };
  return {
    valide: true,
    normalise: clean,
    categorie: CATEGORIES[m[1]],
  };
}

/**
 * Construit l'URL de recherche LBR pour un RCS ou une dénomination.
 * L'utilisateur clique pour ouvrir le portail officiel.
 *
 * NOTE : le portail lbr.lu utilise des sessions JSP, donc on ne peut pas
 * pré-remplir une recherche profonde garantie. Cette fonction renvoie l'URL
 * de la page de recherche publique (gratuite, sans login).
 */
export function urlRechercheLBR({ rcs, denomination } = {}) {
  const base = 'https://www.lbr.lu/mjrcs/jsp/IndexActionNotSecured.action';
  return {
    portail_recherche: base,
    aide: rcs
      ? `Sur le portail, sélectionner "Recherche par numéro RCS" et saisir : ${validerRCS(rcs).normalise || rcs}`
      : denomination
        ? `Sur le portail, sélectionner "Recherche par dénomination" et saisir : ${denomination}`
        : 'Sur le portail, choisir le type de recherche souhaité.',
    note: 'La consultation des fiches publiques (dénomination, siège, gérants, dépôts) est gratuite. Les extraits certifiés et copies d\'actes sont payants.',
  };
}

/**
 * Tarifs LBR 2026 (TVA 17 % comprise).
 * Source : barème officiel publié sur lbr.lu (à actualiser annuellement).
 */
export const TARIFS_LBR_2026 = {
  inscription_societe: { libelle: 'Inscription d\'une nouvelle société commerciale', montant_eur: 22.00 },
  modification: { libelle: 'Modification statuts ou inscription modificative', montant_eur: 11.00 },
  depot_comptes: { libelle: 'Dépôt des comptes annuels (par exercice)', montant_eur: 19.00 },
  extrait_simple: { libelle: 'Extrait simple (téléchargement immédiat)', montant_eur: 4.40 },
  extrait_certifie: { libelle: 'Extrait certifié conforme (avec sceau LBR)', montant_eur: 6.60 },
  copie_acte: { libelle: 'Copie d\'un acte déposé (par acte)', montant_eur: 6.60 },
  radiation: { libelle: 'Inscription de radiation (clôture liquidation)', montant_eur: 11.00 },
  _source: 'Barème LBR 2026 — vérifier sur lbr.lu pour la dernière version',
  _as_of: '2026-01-01',
};

/**
 * Calendrier annuel des dépôts obligatoires LBR pour une société commerciale.
 * Renvoie la liste des prochaines échéances pour l'année donnée.
 *
 * @param {Object} params
 * @param {string} params.exerciceFin  Date de clôture de l'exercice (ISO yyyy-mm-dd)
 * @returns {Array<{nature, deadline, base_legale, conseil}>}
 */
export function calendrierDepots({ exerciceFin }) {
  if (!exerciceFin) throw new Error('exerciceFin (date de clôture) requise');
  const cloture = new Date(exerciceFin);
  if (isNaN(cloture)) throw new Error('exerciceFin invalide (format ISO attendu)');

  // Helper : ajoute N mois sans déborder (clamp au dernier jour du mois cible).
  const addMonths = (date, n) => {
    const y = date.getUTCFullYear();
    const m = date.getUTCMonth();
    const d = date.getUTCDate();
    // Dernier jour du mois cible (m + n + 1, jour 0 = dernier jour du mois précédent)
    const lastDayOfTarget = new Date(Date.UTC(y, m + n + 1, 0)).getUTCDate();
    const day = Math.min(d, lastDayOfTarget);
    return new Date(Date.UTC(y, m + n, day));
  };

  const ag = addMonths(cloture, 6);
  const depotLBR = addMonths(cloture, 7);
  const ecdf = addMonths(cloture, 7);

  const fmt = (d) => d.toISOString().slice(0, 10);

  return [
    {
      nature: 'Tenue de l\'Assemblée Générale ordinaire',
      deadline: fmt(ag),
      base_legale: 'Loi modifiée du 10 août 1915, art. 450-8',
      conseil: 'Convoquer les associés/actionnaires au moins 8 jours avant la date prévue (15 jours pour SA).',
    },
    {
      nature: 'Dépôt des comptes annuels au LBR',
      deadline: fmt(depotLBR),
      base_legale: 'Loi modifiée du 10 août 1915, art. 79',
      conseil: `Tarif LBR : ${TARIFS_LBR_2026.depot_comptes.montant_eur} €. Fichier eCDF + bilan + compte de résultat + annexe + rapport de gestion (si applicable). Voir paperasse ecdf.`,
    },
    {
      nature: 'Dépôt eCDF des comptes annuels',
      deadline: fmt(ecdf),
      base_legale: 'Règlement grand-ducal du 28 mai 2009 (PCN/eCDF)',
      conseil: 'Format CA-A pour les petites entités. Validation préalable sur https://ecdf.b2g.etat.lu/ avant dépôt LBR.',
    },
  ];
}
