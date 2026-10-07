/**
 * lib/diagnostic/dashboard.js — Tableau de bord des obligations (Milestone 2).
 *
 * Transforme la sortie du moteur en un tableau de bord à cinq colonnes :
 *   - obligatoire_maintenant
 *   - a_faire_prochainement
 *   - a_surveiller
 *   - non_applicable
 *   - informations_manquantes
 *
 * Chaque obligation affichée porte : nom, raison de son application,
 * administration, échéance, documents requis, risque en cas d'inaction,
 * source officielle (avec statut de fraîcheur), et les actions proposées
 * (« Commencer », « Créer un rappel »). Aucune action n'est déclenchée ici :
 * le tableau de bord est une vue, pas un exécuteur.
 */

import { diagnostiquer } from './engine.js';
import { evaluerFraicheur, ceJourISO } from './provenance.js';
import { QUESTIONS } from './questionnaire.js';

function sourceAffichable(ob, aujourdhui) {
  const p = ob.provenance || {};
  const fr = evaluerFraicheur(p, { aujourdhui });
  return {
    url: p.source || null,
    dateVerification: p.dateVerification || null,
    niveauConfiance: p.niveauConfiance || null,
    validationHumaineRequise: Boolean(p.validationHumaineRequise) || fr.aRevalider,
    aRevalider: fr.aRevalider,
    message: fr.message,
  };
}

function carte(entree, aujourdhui) {
  const { obligation: ob, raisons = [], echeance } = entree;
  return {
    id: ob.id,
    nom: ob.nom,
    categorie: ob.categorie,
    raison: raisons.length ? raisons.join(' ; ') : null,
    administration: ob.autoriteCompetente || null,
    echeance: echeance || null,
    documentsRequis: ob.piecesRequises || [],
    risque: ob.penalites || null,
    source: sourceAffichable(ob, aujourdhui),
    actions: ['commencer', 'creer_rappel'],
  };
}

/**
 * Construit le tableau de bord complet pour une situation.
 *
 * @param {object} situation        Réponses / profil (lu par le moteur).
 * @param {object[]} catalogue      Obligations sourcées.
 * @param {object} [opts]
 * @param {string} [opts.aujourdhui] Date de référence (déterminisme).
 * @returns {{colonnes, compteurs}}
 */
export function construireTableauDeBord(situation, catalogue, { aujourdhui = ceJourISO() } = {}) {
  const { applicables, aClarifier, nonApplicables } = diagnostiquer(situation, catalogue, { aujourdhui });

  const colonnes = {
    obligatoire_maintenant: [],
    a_faire_prochainement: [],
    a_surveiller: [],
    non_applicable: [],
    informations_manquantes: [],
  };

  for (const e of applicables) {
    const c = carte(e, aujourdhui);
    const col = e.echeance ? colonneEcheance(e.echeance, aujourdhui) : 'a_surveiller';
    colonnes[col].push(c);
  }

  for (const e of aClarifier) {
    colonnes.informations_manquantes.push({
      ...carte(e, aujourdhui),
      manquantes: e.manquantes,
      questions: e.manquantes.map((champ) => (QUESTIONS[champ] ? QUESTIONS[champ].label : `Renseigner : ${champ}`)),
    });
  }

  for (const e of nonApplicables) {
    colonnes.non_applicable.push({ id: e.obligation.id, nom: e.obligation.nom, categorie: e.obligation.categorie });
  }

  const compteurs = Object.fromEntries(Object.entries(colonnes).map(([k, v]) => [k, v.length]));
  return { colonnes, compteurs };
}

/** Colonne selon la proximité de l'échéance (aligné sur prioriteSelonEcheance). */
function colonneEcheance(echeance, aujourdhui) {
  const jours = Math.floor((Date.parse(`${echeance}T00:00:00Z`) - Date.parse(`${aujourdhui}T00:00:00Z`)) / 86_400_000);
  if (jours <= 30) return 'obligatoire_maintenant';
  if (jours <= 90) return 'a_faire_prochainement';
  return 'a_surveiller';
}
