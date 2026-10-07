/**
 * lib/entreprise — Cycle de vie de l'entreprise (Milestone 5).
 *
 * Regroupe et ORDONNE les obligations d'un indépendant ou d'une société selon
 * les phases du cycle de vie (création → vie sociale → fiscalité → employeur →
 * cessation), en réutilisant :
 *   - le catalogue d'obligations sourcé (data/obligations.json, via le moteur) ;
 *   - les checklists et le calendrier de dépôts RCS (lib/lbr).
 *
 * Objectifs (M5) : un dirigeant voit toutes ses obligations, classées par
 * société, avec les pièces manquantes et un ordre chronologique.
 *
 * Aucune dépendance externe.
 */

import { diagnostiquer } from '../diagnostic/engine.js';
import { ceJourISO } from '../diagnostic/provenance.js';
import { CHECKLISTS_LBR, calendrierDepots } from '../lbr/index.js';

/** Phases du cycle de vie, dans l'ordre chronologique naturel. */
export const PHASES = ['creation', 'vie', 'fiscalite', 'employeur', 'cessation', 'autre'];

const CATEGORIE_VERS_PHASE = {
  creation: 'creation',
  social: 'creation',
  societe: 'vie',
  fiscalite_entreprise: 'fiscalite',
  tva: 'fiscalite',
  employeur: 'employeur',
  cessation: 'cessation',
};

/** Phase d'une obligation à partir de sa catégorie. */
export function phasePourCategorie(categorie) {
  return CATEGORIE_VERS_PHASE[categorie] || 'autre';
}

const compareEcheance = (a, b) => {
  if (!a.echeance && !b.echeance) return 0;
  if (!a.echeance) return 1;   // sans échéance → en fin de liste
  if (!b.echeance) return -1;
  return a.echeance.localeCompare(b.echeance);
};

/**
 * Pièces requises non encore fournies pour une obligation.
 * @param {object} obligation
 * @param {string[]} [documentsFournis] libellés de pièces déjà disponibles
 */
function piecesManquantesPour(obligation, documentsFournis = []) {
  const fournis = documentsFournis.map((d) => String(d).toLowerCase());
  return (obligation.piecesRequises || []).filter(
    (p) => !fournis.some((f) => f.includes(String(p).toLowerCase().slice(0, 12))),
  );
}

/**
 * Construit le parcours d'une entreprise (ou d'un indépendant).
 *
 * @param {object} situation        Profil société et/ou champs indépendant.
 * @param {object[]} catalogue      Obligations sourcées.
 * @param {object} [opts]
 * @param {string} [opts.aujourdhui]
 * @param {string} [opts.exerciceFin]      Date de clôture (YYYY-MM-DD) → intègre le calendrier RCS (AG, dépôt).
 * @param {string[]} [opts.documentsFournis] Pièces déjà disponibles (pour le calcul des manquantes).
 * @returns {{parPhase, chronologie, piecesManquantes, aClarifier}}
 */
export function parcoursEntreprise(situation, catalogue, opts = {}) {
  const aujourdhui = opts.aujourdhui || ceJourISO();
  const { applicables, aClarifier } = diagnostiquer(situation, catalogue, { aujourdhui });

  const items = applicables.map((e) => ({
    phase: phasePourCategorie(e.obligation.categorie),
    obligationId: e.obligation.id,
    nom: e.obligation.nom,
    categorie: e.obligation.categorie,
    administration: e.obligation.autoriteCompetente,
    echeance: e.echeance,
    raisons: e.raisons,
    piecesRequises: e.obligation.piecesRequises,
    source: e.obligation.provenance ? e.obligation.provenance.source : null,
  }));

  // Intégration du calendrier de dépôts RCS (réutilise lib/lbr) si la clôture
  // d'exercice est connue : AG ordinaire, dépôt des comptes, eCDF.
  if (opts.exerciceFin) {
    for (const d of calendrierDepots({ exerciceFin: opts.exerciceFin })) {
      items.push({
        phase: 'vie',
        obligationId: null,
        nom: d.nature,
        categorie: 'societe',
        administration: 'LBR / eCDF',
        echeance: d.deadline,
        raisons: [d.base_legale],
        piecesRequises: [],
        source: 'https://www.lbr.lu',
        conseil: d.conseil,
      });
    }
  }

  // Regroupement par phase, chaque phase triée chronologiquement.
  const parPhase = {};
  for (const phase of PHASES) {
    const liste = items.filter((i) => i.phase === phase).sort(compareEcheance);
    if (liste.length) parPhase[phase] = liste;
  }

  // Chronologie globale (toutes phases confondues).
  const chronologie = [...items].sort(compareEcheance);

  // Pièces manquantes par obligation applicable.
  const piecesManquantes = applicables
    .map((e) => ({
      obligationId: e.obligation.id,
      nom: e.obligation.nom,
      manquantes: piecesManquantesPour(e.obligation, opts.documentsFournis),
    }))
    .filter((x) => x.manquantes.length);

  return { parPhase, chronologie, piecesManquantes, aClarifier };
}

/**
 * Échéances classées par société : applique parcoursEntreprise à chaque
 * situation et indexe par identifiant de société.
 *
 * @param {object[]} situations  Chaque objet doit porter un `id` (ou societeId).
 */
export function echeancesParSociete(situations, catalogue, opts = {}) {
  const out = {};
  for (const s of situations) {
    const cle = s.id || s.societeId || s.nom || `societe_${Object.keys(out).length + 1}`;
    out[cle] = parcoursEntreprise(s, catalogue, { ...opts, exerciceFin: s.exerciceFin || opts.exerciceFin }).chronologie;
  }
  return out;
}

/**
 * Checklist de création (réutilise lib/lbr). Ex : 'creation_sarl', 'creation_sa'.
 * @returns {object} { libelle, pieces, delai_jours, cout_indicatif_eur, bases_legales, ... }
 */
export function checklistCreation(operation) {
  const c = CHECKLISTS_LBR[operation];
  if (!c) throw new Error(`Opération inconnue : ${operation} (voir ${Object.keys(CHECKLISTS_LBR).join(', ')})`);
  return c;
}
