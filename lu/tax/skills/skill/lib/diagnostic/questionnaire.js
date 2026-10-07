/**
 * lib/diagnostic/questionnaire.js — Questionnaire dynamique (Milestone 2).
 *
 * Entrée principale du produit : « Que dois-je faire administrativement ? ».
 * Le questionnaire ne pose QUE les questions nécessaires : il déduit, à partir
 * des `conditionsApplicabilite` du catalogue d'obligations, quels champs de la
 * situation restent à clarifier, et propose la question la plus discriminante.
 *
 * Principe « pas de question inutile » :
 *   un champ n'est demandé que s'il reste au moins une obligation dont
 *   l'applicabilité DÉPEND ENCORE de ce champ — c'est-à-dire dont toutes les
 *   conditions déjà répondues sont vraies. Dès qu'une condition répondue est
 *   fausse, l'obligation est décidée « non applicable » et ses autres champs ne
 *   sont plus demandés.
 *
 * Opère sur un objet « situation » plat (réponses), lu directement par le
 * moteur (engine.lire). Aucune dépendance externe.
 */

import { ENUMS } from './entities.js';

/**
 * Registre des questions : pour chaque champ de profil susceptible d'apparaître
 * dans une condition d'obligation, une formulation claire (français simple,
 * acronymes explicités) et son type de saisie.
 */
export const QUESTIONS = Object.freeze({
  regimeTVA: {
    champ: 'regimeTVA', type: 'enum', options: ENUMS.regimeTVA,
    label: 'Quel est votre régime de TVA ?',
    aide: 'TVA = taxe sur la valeur ajoutée. « non_assujetti » si vous ne facturez pas de TVA.',
    portee: 'societe',
  },
  frequenceTVA: {
    champ: 'frequenceTVA', type: 'enum', options: ENUMS.frequenceTVA,
    label: 'À quelle fréquence déposez-vous vos déclarations de TVA ?',
    aide: 'Dépend du chiffre d\'affaires : mensuelle, trimestrielle ou annuelle.',
    portee: 'societe',
  },
  statut: {
    champ: 'statut', type: 'enum', options: ENUMS.statutSociete,
    label: 'Quel est le statut actuel de la société ?',
    portee: 'societe',
  },
  statutProfessionnel: {
    champ: 'statutProfessionnel', type: 'enum', options: ENUMS.statutProfessionnel,
    label: 'Quel est votre statut professionnel ?',
    portee: 'particulier',
  },
  frontalier: {
    champ: 'frontalier', type: 'boolean',
    label: 'Êtes-vous frontalier (vous résidez hors du Luxembourg mais y travaillez) ?',
    portee: 'particulier',
  },
  dateArriveeLux: {
    champ: 'dateArriveeLux', type: 'date',
    label: 'Quelle est votre date d\'arrivée au Luxembourg ? (laisser vide si vous n\'y résidez pas)',
    portee: 'particulier',
  },
  situationFamiliale: {
    champ: 'situationFamiliale', type: 'enum', options: ENUMS.situationFamiliale,
    label: 'Quelle est votre situation familiale ?',
    portee: 'particulier',
  },
  nombreEnfants: {
    champ: 'nombreEnfants', type: 'number',
    label: 'Combien d\'enfants à charge avez-vous ?',
    portee: 'particulier',
  },
  statutLogement: {
    champ: 'statutLogement', type: 'enum', options: ENUMS.statutLogement,
    label: 'Êtes-vous propriétaire, locataire ou hébergé ?',
    portee: 'particulier',
  },
  paysResidence: {
    champ: 'paysResidence', type: 'text',
    label: 'Dans quel pays résidez-vous ? (code ISO, ex : LU, FR, BE, DE)',
    portee: 'particulier',
  },
});

/** Ordre stable de départage (à égalité de nombre d'obligations gated). */
const ORDRE = [
  'statut', 'regimeTVA', 'statutProfessionnel', 'frontalier', 'paysResidence',
  'frequenceTVA', 'dateArriveeLux', 'situationFamiliale', 'statutLogement', 'nombreEnfants',
];

const estRenseigne = (v) => v !== undefined && v !== null && v !== '';

/**
 * Une condition « passe-t-elle » avec la valeur actuellement connue ?
 * Retourne 'vrai' | 'faux' | 'inconnu'.
 */
function etatCondition(situation, cond) {
  const v = situation[cond.champ];
  // Opérateurs satisfaits par l'absence : la condition est décidable même vide.
  if (cond.operateur === 'absent') return v == null || v === '' || (Array.isArray(v) && v.length === 0) ? 'vrai' : 'faux';
  if (cond.operateur === 'faux') return v === false || v == null ? 'vrai' : 'faux';
  if (!estRenseigne(v)) return 'inconnu';
  switch (cond.operateur) {
    case 'egal': return v === cond.valeur ? 'vrai' : 'faux';
    case 'different': return v !== cond.valeur ? 'vrai' : 'faux';
    case 'vrai': return v === true ? 'vrai' : 'faux';
    case 'present': return 'vrai';
    case 'superieur': return typeof v === 'number' && v > cond.valeur ? 'vrai' : 'faux';
    case 'inferieur': return typeof v === 'number' && v < cond.valeur ? 'vrai' : 'faux';
    case 'contient': return (Array.isArray(v) ? v.includes(cond.valeur) : String(v).includes(cond.valeur)) ? 'vrai' : 'faux';
    default: return 'faux';
  }
}

/**
 * Champs encore pertinents à demander, avec le nombre d'obligations que chacun
 * conditionne encore. Un champ n'est retenu que si, pour au moins une
 * obligation, toutes les conditions déjà répondues sont vraies (l'obligation
 * reste « possible ») et ce champ est inconnu.
 *
 * @returns {Map<string, number>} champ → nombre d'obligations concernées
 */
export function champsPertinents(situation, catalogue) {
  const compte = new Map();
  for (const ob of catalogue) {
    if (ob.statut === 'obsolete') continue;
    const conditions = ob.conditionsApplicabilite || [];
    const etats = conditions.map((c) => ({ c, etat: etatCondition(situation, c) }));
    // Obligation déjà décidée non applicable → on ne demande plus rien pour elle.
    if (etats.some((e) => e.etat === 'faux')) continue;
    for (const { c, etat } of etats) {
      if (etat === 'inconnu') compte.set(c.champ, (compte.get(c.champ) || 0) + 1);
    }
  }
  return compte;
}

/**
 * Prochaine question à poser, ou null si le diagnostic est complet
 * (plus aucune obligation ne dépend d'un champ inconnu qu'on sait formuler).
 *
 * @returns {object|null} entrée de QUESTIONS enrichie de { champ, gated }
 */
export function prochaineQuestion(situation, catalogue) {
  const compte = champsPertinents(situation, catalogue);
  let meilleur = null;
  for (const [champ, gated] of compte) {
    if (!QUESTIONS[champ]) continue; // champ non formulable → laissé en « informations manquantes »
    if (
      meilleur === null ||
      gated > meilleur.gated ||
      (gated === meilleur.gated && ORDRE.indexOf(champ) < ORDRE.indexOf(meilleur.champ))
    ) {
      meilleur = { ...QUESTIONS[champ], gated };
    }
  }
  return meilleur;
}

/**
 * Liste ordonnée de toutes les questions restantes (aperçu du parcours).
 */
export function questionsRestantes(situation, catalogue) {
  const compte = champsPertinents(situation, catalogue);
  return [...compte.entries()]
    .filter(([champ]) => QUESTIONS[champ])
    .sort((a, b) => b[1] - a[1] || ORDRE.indexOf(a[0]) - ORDRE.indexOf(b[0]))
    .map(([champ, gated]) => ({ ...QUESTIONS[champ], gated }));
}

/**
 * Applique une réponse à la situation (immuable) avec coercition de type.
 * Permet la correction : réappliquer un champ écrase la valeur précédente.
 */
export function appliquerReponse(situation, champ, valeur) {
  const q = QUESTIONS[champ];
  let v = valeur;
  if (q) {
    if (q.type === 'boolean') v = valeur === true || valeur === 'oui' || valeur === 'true';
    else if (q.type === 'number') v = Number(valeur);
    else if (q.type === 'enum' && valeur !== null && !q.options.includes(valeur)) {
      throw new Error(`Réponse invalide pour ${champ} : "${valeur}" (attendu : ${q.options.join(', ')})`);
    }
  }
  return { ...situation, [champ]: v };
}
