/**
 * lib/extraction — Frontière langage naturel → graphe (contrat LLM).
 *
 * Le LLM (fourni par la couche agent, PAS par cette bibliothèque hors-ligne)
 * traduit une conversation en une STRUCTURE : événements, entités, chronologie,
 * confiance. Ce module définit ce contrat, le VALIDE, et l'INGÈRE dans le
 * graphe (résolution des événements + normalisation d'un profil).
 *
 * Principe : le LLM ne décide d'aucune obligation ; il ne fait que traduire du
 * texte en données. Le graphe et le planificateur décident ensuite. Cette
 * séparation garde le cœur déterministe et testable sans appel réseau.
 *
 * Aucune dépendance externe.
 */

import { identifierEvenement, listerEvenements } from '../evenements/index.js';

/**
 * Schéma attendu de la sortie du LLM (à documenter dans le prompt de l'agent).
 * Exemple :
 *   {
 *     "events": ["arrivee_luxembourg"],
 *     "entities": { "adults": 2, "children": 2,
 *                   "employment": { "user": "Luxembourg", "spouse": "France" },
 *                   "timeline": { "move": "2026-09" } },
 *     "confidence": 0.96
 *   }
 */
export const SCHEMA_EXTRACTION = Object.freeze({
  type: 'object',
  required: ['events'],
  properties: {
    events: { type: 'array', items: { type: 'string' } },
    entities: { type: 'object' },
    confidence: { type: 'number', minimum: 0, maximum: 1 },
  },
});

export const SEUIL_CONFIANCE = 0.6;

/** Valide la structure produite par le LLM (sans dépendance de schéma). */
export function validerExtraction(struct) {
  const erreurs = [];
  if (!struct || typeof struct !== 'object') return { valide: false, erreurs: ['structure absente ou invalide'] };
  if (!Array.isArray(struct.events)) erreurs.push('events doit être un tableau');
  if (struct.entities !== undefined && typeof struct.entities !== 'object') erreurs.push('entities doit être un objet');
  if (struct.confidence !== undefined && (typeof struct.confidence !== 'number' || struct.confidence < 0 || struct.confidence > 1)) {
    erreurs.push('confidence doit être un nombre entre 0 et 1');
  }
  return { valide: erreurs.length === 0, erreurs };
}

const MOIS_VERS_ISO = (v) => {
  if (typeof v !== 'string') return null;
  if (/^\d{4}-\d{2}-\d{2}$/.test(v)) return v;
  if (/^\d{4}-\d{2}$/.test(v)) return `${v}-01`;
  return null;
};

/**
 * Traduit les entités extraites en champs de profil normalisés (mapping
 * explicite et modeste ; le reste est conservé dans `entites`).
 */
export function entitesVersProfil(entities = {}) {
  const profil = {};
  if (Number.isFinite(entities.children)) profil.nombreEnfants = entities.children;
  if (entities.nationalite) profil.nationalite = entities.nationalite;
  if (entities.paysResidence) profil.paysResidence = entities.paysResidence;
  if (entities.situationFamiliale) profil.situationFamiliale = entities.situationFamiliale;
  const emp = entities.employment || {};
  if (emp.user === 'Luxembourg' || emp.user === 'LU') {
    profil.statutProfessionnel = profil.statutProfessionnel || 'salarie';
    profil.paysEmployeur = 'LU';
  }
  // Conjoint travaillant à l'étranger : information de contexte (frontalier du foyer).
  if (emp.spouse && emp.spouse !== 'Luxembourg' && emp.spouse !== 'LU') profil.conjointTravailleEtranger = emp.spouse;
  const move = entities.timeline && MOIS_VERS_ISO(entities.timeline.move);
  if (move) profil.dateArriveeLux = move;
  return profil;
}

/**
 * Ingère une extraction : valide, résout les événements (ids ou texte libre),
 * construit un profil normalisé et signale la confiance.
 *
 * @param {object} struct  Sortie du LLM (voir SCHEMA_EXTRACTION).
 * @returns {{evenements, inconnus, profil, confidence, aValider, avertissement, entites}}
 */
export function ingererExtraction(struct) {
  const { valide, erreurs } = validerExtraction(struct);
  if (!valide) throw new Error(`Extraction invalide : ${erreurs.join('; ')}`);

  const idsConnus = new Set(listerEvenements().map((e) => e.id));
  const evenements = [];
  const inconnus = [];
  for (const brut of struct.events) {
    if (idsConnus.has(brut)) { if (!evenements.includes(brut)) evenements.push(brut); continue; }
    const resolu = identifierEvenement(brut);
    if (resolu) { if (!evenements.includes(resolu)) evenements.push(resolu); }
    else inconnus.push(brut);
  }

  const confidence = typeof struct.confidence === 'number' ? struct.confidence : null;
  const aValider = confidence != null && confidence < SEUIL_CONFIANCE;

  return {
    evenements,
    inconnus,
    profil: entitesVersProfil(struct.entities || {}),
    entites: struct.entities || {},
    confidence,
    aValider,
    avertissement: (aValider ? 'Confiance faible : structure à confirmer avec l\'utilisateur. ' : '')
      + (inconnus.length ? `Événements non reconnus : ${inconnus.join(', ')}.` : '') || null,
  };
}
