/**
 * lib/bellegen-akt — Calculateur des droits d'enregistrement immobiliers
 * et du crédit d'impôt « Bëllegen Akt » (Luxembourg).
 *
 * Sources :
 *   - Loi modifiée du 30 juillet 2002 (droits d'enregistrement et de transcription)
 *   - Loi du 22 mai 2024 portant réforme du crédit d'impôt « Bëllegen Akt »
 *     (entrée en vigueur 1er octobre 2024) : 40 000 € PAR personne acquéreuse
 *     (au lieu des 30 000 € de l'ancien régime), imputé sur les droits dus.
 *   - Communes : surtaxe communale de 3 % à Luxembourg-Ville sur les transactions
 *     immobilières.
 *
 * Périmètre :
 *   - Acquisition d'immeubles bâtis ou non bâtis, à titre onéreux
 *   - Résidence principale (Bëllegen Akt) : abattement 40 000 €/personne
 *   - VEFA (logement neuf) : option TVA logement 3 % gérée à part (cf. lib/calc TVA)
 *
 * Hors périmètre :
 *   - Successions/donations : voir lib/succession (à venir)
 *   - Donations entre vifs : barèmes spécifiques
 */

export const TAUX_DROITS_LU = {
  enregistrement: 0.06,         // 6 % standard
  transcription: 0.01,          // 1 %
  surtaxeLuxVille: 0.03,        // +3 % sur la commune de Luxembourg
};

export const ABATTEMENT_BELLEGEN_AKT_PAR_PERSONNE = 40000;
export const DATE_ENTREE_EN_VIGUEUR = '2024-10-01';

/**
 * Calcule le coût total d'une acquisition immobilière au Luxembourg
 * (droits + honoraires de notaire + TVA + débours).
 *
 * @param {object} input
 * @param {number} input.prix             Prix d'acquisition (TTC ou HT selon le type, voir notes)
 * @param {number} [input.nbAcquereurs=1] Nombre d'acquéreurs (couple = 2)
 * @param {boolean} [input.luxVille=false] Bien situé sur la commune de Luxembourg-Ville
 * @param {boolean} [input.bellegenAkt=true] Application du crédit d'impôt résidence principale
 * @param {string} [input.dateActe]       Date de l'acte (ISO YYYY-MM-DD).
 *                                        Si < 2024-10-01, applique l'ancien plafond (30 000 €).
 *
 * @returns {object} décomposition complète du coût
 */
export function calculerBellegenAkt(input) {
  const erreurs = validerInput(input);
  if (erreurs.length) {
    const e = new Error(`Entrée invalide :\n  - ${erreurs.join('\n  - ')}`);
    e.erreurs = erreurs;
    throw e;
  }

  const {
    prix,
    nbAcquereurs = 1,
    luxVille = false,
    bellegenAkt = true,
    dateActe = null,
  } = input;

  const tauxEnreg = round4(TAUX_DROITS_LU.enregistrement
    + (luxVille ? TAUX_DROITS_LU.surtaxeLuxVille : 0));
  const tauxTranscription = TAUX_DROITS_LU.transcription;
  const tauxTotal = round4(tauxEnreg + tauxTranscription);

  const droitEnregistrement = round2(prix * tauxEnreg);
  const droitTranscription = round2(prix * tauxTranscription);
  const droitsNominaux = round2(droitEnregistrement + droitTranscription);

  // Plafond Bëllegen Akt selon date de l'acte
  const plafondParPersonne = bellegenAktAncien(dateActe) ? 30000 : ABATTEMENT_BELLEGEN_AKT_PAR_PERSONNE;
  const abattementMax = plafondParPersonne * nbAcquereurs;
  const abattement = bellegenAkt ? Math.min(droitsNominaux, abattementMax) : 0;
  const droitsNets = round2(droitsNominaux - abattement);

  const honoraires = estimerHonoraires(prix);
  const tvaHonoraires = round2(honoraires * 0.17);
  const debours = 400; // estimation forfaitaire (extraits cadastraux, certificats…)

  const total = round2(droitsNets + honoraires + tvaHonoraires + debours);

  return {
    prix,
    nbAcquereurs,
    luxVille,
    tauxEnregistrementApplique: tauxEnreg,
    tauxTranscription,
    tauxTotal,
    droitEnregistrement,
    droitTranscription,
    droitsNominaux,
    bellegenAkt: {
      applique: bellegenAkt,
      plafondParPersonne,
      abattementMaximalTheorique: abattementMax,
      abattementEffectif: abattement,
      saturé: bellegenAkt && abattement === abattementMax,
      plafonnéAuxDroits: bellegenAkt && abattement < abattementMax,
    },
    droitsNets,
    honoraires,
    tvaHonoraires,
    debours,
    total,
    fraisHorsPrix: round2(total - 0), // total = frais + 0 (le prix est déjà dans `prix`)
    ratioFraisSurPrix: round2((total / prix) * 1000) / 1000,
  };
}

/**
 * Estimation des honoraires de notaire luxembourgeois (tarif réglementé dégressif).
 * Approximation officielle : règlement grand-ducal du 24 janvier 2003.
 */
export function estimerHonoraires(prix) {
  let h;
  if (prix <= 100000) h = prix * 0.012;
  else if (prix <= 300000) h = 1200 + (prix - 100000) * 0.009;
  else if (prix <= 1000000) h = 1200 + 1800 + (prix - 300000) * 0.007;
  else h = 1200 + 1800 + 4900 + (prix - 1000000) * 0.005;
  return round2(h);
}

function bellegenAktAncien(dateActe) {
  if (!dateActe) return false;
  return dateActe < DATE_ENTREE_EN_VIGUEUR;
}

function validerInput(input) {
  const e = [];
  if (!input || typeof input !== 'object') return ['input absent'];
  if (typeof input.prix !== 'number' || input.prix <= 0) e.push('prix doit être un nombre > 0');
  if (input.nbAcquereurs != null) {
    if (!Number.isInteger(input.nbAcquereurs) || input.nbAcquereurs < 1) {
      e.push('nbAcquereurs doit être un entier ≥ 1');
    }
  }
  if (input.dateActe != null && !validerDateISOReelle(input.dateActe)) {
    e.push('dateActe doit être une date ISO YYYY-MM-DD réelle');
  }
  return e;
}

function validerDateISOReelle(s) {
  if (typeof s !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(s)) return false;
  const [y, m, d] = s.split('-').map(Number);
  const dt = new Date(Date.UTC(y, m - 1, d));
  return dt.getUTCFullYear() === y && dt.getUTCMonth() === m - 1 && dt.getUTCDate() === d;
}

function round2(n) { return Math.round(n * 100) / 100; }
function round4(n) { return Math.round(n * 10000) / 10000; }
