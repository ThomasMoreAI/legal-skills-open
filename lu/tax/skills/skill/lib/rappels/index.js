/**
 * lib/rappels — Calendrier, rappels & surveillance (Milestone 10).
 *
 * Suivi proactif des dossiers : niveau d'alerte par couleur, rappels avant
 * échéance, rappels pour information/document manquant, calendrier trié.
 * S'appuie sur les `Dossier.echeance` / `Dossier.statut` produits par tous les
 * modules (diagnostic, TVA, entreprise, particulier, documents…).
 *
 * Aucune dépendance externe.
 */

import { ceJourISO } from '../diagnostic/provenance.js';
import { ENUMS } from '../diagnostic/entities.js';

/** Statuts de dossier (repris du modèle d'entités). */
export const STATUTS = ENUMS.statutDossier;

/** Codes couleur d'alerte et leur signification. */
export const COULEURS = Object.freeze({
  rouge: 'Échéance dépassée',
  orange: 'Moins de 7 jours',
  jaune: 'Moins de 30 jours',
  vert: 'Terminé',
  neutre: 'À surveiller',
});

const MS_JOUR = 86_400_000;

function joursEntre(dateISO, aujourdhui) {
  return Math.floor((Date.parse(`${dateISO}T00:00:00Z`) - Date.parse(`${aujourdhui}T00:00:00Z`)) / MS_JOUR);
}

/**
 * Niveau d'alerte d'un dossier.
 *   rouge  : échéance dépassée (ou statut en_retard) ;
 *   orange : échéance dans 7 jours ou moins ;
 *   jaune  : échéance dans 30 jours ou moins ;
 *   vert   : terminé ;
 *   neutre : au-delà de 30 jours ou sans échéance.
 *
 * @returns {{couleur, libelle, joursRestants: number|null}}
 */
export function niveauAlerte(dossier, aujourdhui = ceJourISO()) {
  if (dossier.statut === 'termine') return { couleur: 'vert', libelle: COULEURS.vert, joursRestants: null };
  if (!dossier.echeance) {
    const couleur = dossier.statut === 'en_retard' ? 'rouge' : 'neutre';
    return { couleur, libelle: COULEURS[couleur], joursRestants: null };
  }
  const jours = joursEntre(dossier.echeance, aujourdhui);
  let couleur;
  if (jours < 0 || dossier.statut === 'en_retard') couleur = 'rouge';
  else if (jours <= 7) couleur = 'orange';
  else if (jours <= 30) couleur = 'jaune';
  else couleur = 'neutre';
  return { couleur, libelle: COULEURS[couleur], joursRestants: jours };
}

/** Ordre de tri des couleurs (plus urgent d'abord). */
const RANG_COULEUR = { rouge: 0, orange: 1, jaune: 2, neutre: 3, vert: 4 };

/** Un dossier a-t-il des éléments manquants bloquant l'action ? */
function elementsManquants(dossier) {
  const infos = dossier.informationsManquantes || [];
  const requis = dossier.documentsRequis || [];
  const recus = (dossier.documentsRecus || []).map((d) => String(d).toLowerCase());
  const docsManquants = requis.filter((r) => !recus.some((x) => x.includes(String(r).toLowerCase().slice(0, 12))));
  return { infos, docsManquants };
}

/**
 * Génère les rappels pour une liste de dossiers.
 *
 * @param {object[]} dossiers
 * @param {object} [opts]
 * @param {string} [opts.aujourdhui]
 * @param {number[]} [opts.preavis]   Seuils de préavis en jours (défaut 30/7/1).
 * @returns {object[]} rappels triés (plus urgents d'abord)
 */
export function genererRappels(dossiers, { aujourdhui = ceJourISO(), preavis = [30, 7, 1] } = {}) {
  const rappels = [];
  for (const d of dossiers) {
    if (d.statut === 'termine') continue;
    const alerte = niveauAlerte(d, aujourdhui);
    const messages = [];

    if (alerte.joursRestants != null) {
      if (alerte.joursRestants < 0) messages.push(`En retard de ${Math.abs(alerte.joursRestants)} jour(s) (échéance ${d.echeance}).`);
      else {
        const seuilAtteint = preavis.filter((p) => alerte.joursRestants <= p).sort((a, b) => a - b)[0];
        if (seuilAtteint != null) messages.push(`Échéance dans ${alerte.joursRestants} jour(s) (le ${d.echeance}).`);
      }
    }

    const { infos, docsManquants } = elementsManquants(d);
    if (infos.length) messages.push(`Informations manquantes : ${infos.join(', ')}.`);
    if (docsManquants.length) messages.push(`Documents à fournir : ${docsManquants.join(', ')}.`);
    if (d.statut === 'en_attente_information') messages.push('En attente d\'information — relancer si nécessaire.');
    if (d.statut === 'pret_a_envoyer') messages.push('Prêt à envoyer — valider puis transmettre.');
    if (d.recurrence) messages.push(`Rappel récurrent (${d.recurrence}).`);

    if (!messages.length) continue;
    rappels.push({
      dossierId: d.id || null,
      intitule: d.typeDemarche || d.categorie,
      echeance: d.echeance || null,
      statut: d.statut,
      couleur: alerte.couleur,
      joursRestants: alerte.joursRestants,
      messages,
      actionRequise: alerte.couleur === 'rouge' || alerte.couleur === 'orange' || docsManquants.length > 0 || infos.length > 0,
    });
  }
  return rappels.sort((a, b) =>
    (RANG_COULEUR[a.couleur] - RANG_COULEUR[b.couleur])
    || ((a.joursRestants ?? Infinity) - (b.joursRestants ?? Infinity)),
  );
}

/**
 * Calendrier trié des dossiers, groupé par couleur d'alerte, avec compteurs.
 */
export function calendrierDossiers(dossiers, { aujourdhui = ceJourISO() } = {}) {
  const enrichis = dossiers.map((d) => ({ ...d, alerte: niveauAlerte(d, aujourdhui) }));
  const parCouleur = { rouge: [], orange: [], jaune: [], neutre: [], vert: [] };
  for (const d of enrichis) parCouleur[d.alerte.couleur].push(d);
  const chronologie = enrichis
    .filter((d) => d.echeance)
    .sort((a, b) => a.echeance.localeCompare(b.echeance));
  const compteurs = Object.fromEntries(Object.entries(parCouleur).map(([k, v]) => [k, v.length]));
  return { parCouleur, chronologie, compteurs };
}

/** Dossiers dont l'échéance tombe dans les `dans` prochains jours (hors terminés). */
export function prochainesEcheances(dossiers, { aujourdhui = ceJourISO(), dans = 30 } = {}) {
  return dossiers
    .filter((d) => d.echeance && d.statut !== 'termine')
    .map((d) => ({ ...d, joursRestants: joursEntre(d.echeance, aujourdhui) }))
    .filter((d) => d.joursRestants <= dans)
    .sort((a, b) => a.joursRestants - b.joursRestants);
}

/** Filtre les dossiers par statut (valide le statut). */
export function filtrerParStatut(dossiers, statut) {
  if (!STATUTS.includes(statut)) throw new Error(`Statut inconnu : ${statut} (attendu : ${STATUTS.join(', ')})`);
  return dossiers.filter((d) => d.statut === statut);
}

/**
 * Date de prochain rappel pour un dossier (échéance moins le préavis).
 * @returns {string|null} date ISO ou null
 */
export function prochainRappel(dossier, { preavisJours = 7 } = {}) {
  if (!dossier.echeance) return null;
  const base = Date.parse(`${dossier.echeance}T00:00:00Z`);
  return new Date(base - preavisJours * MS_JOUR).toISOString().slice(0, 10);
}
