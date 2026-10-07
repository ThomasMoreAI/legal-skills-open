/**
 * lib/planification — Moteur de planification (raisonnement multi-événements).
 *
 * Prend PLUSIEURS événements de vie + le profil + la mémoire, et produit un
 * plan ordonné :
 *   - fusionne les démarches issues des événements (dédoublonnage) ;
 *   - exclut ce qui est déjà réalisé (mémoire) ;
 *   - détecte les documents mutualisés (« 9 démarches partagent ces pièces ») ;
 *   - ordonne selon les DÉPENDANCES (« commencer par celles qui débloquent »),
 *     puis l'urgence (échéance) ;
 *   - EXPLIQUE chaque étape (déclenchée par quel événement, source, ce qu'elle
 *     débloque).
 *
 * Les dépendances sont structurelles (ordre des guichets), pas des affirmations
 * réglementaires ; les règles elles-mêmes restent sourcées dans le catalogue.
 *
 * Aucune dépendance externe.
 */

import { resoudreEvenement } from '../evenements/index.js';
import { obligationsRealiseesSet } from '../memoire/index.js';
import { ceJourISO } from '../diagnostic/provenance.js';

/** Précédences structurelles : [avant, après] (clés = ids d'obligation/démarche). */
export const PRECEDENCES = [
  ['obl_commune_declaration_arrivee', 'obl_irpp_declaration_modele100'],
  ['obl_commune_declaration_arrivee', 'obl_allocations_familiales'],
  ['obl_autorisation_etablissement', 'rcs_immatriculation'],
  ['rcs_immatriculation', 'obl_rbe_mise_a_jour'],
  ['rcs_immatriculation', 'tva_immatriculation'],
  ['rcs_immatriculation', 'obl_affiliation_ccss_independant'],
  ['etat_civil_naissance', 'cns_affiliation_enfant'],
  ['etat_civil_naissance', 'obl_allocations_familiales'],
  ['etat_civil_naissance', 'obl_conge_parental'],
];

const STOP = new Set(['de', 'd', 'des', 'du', 'la', 'le', 'les', 'l', 'a', 'au', 'aux', 'et', 'en', 'pour', 'par', 'sur', 'un', 'une']);

function sansAccents(s) {
  return s.normalize('NFD').replace(/[̀-ͯ]/g, '');
}
function motsSignificatifs(label) {
  return sansAccents(String(label)).toLowerCase().replace(/[^a-z0-9\s]/g, ' ').split(/\s+/)
    .filter((w) => w && !STOP.has(w))
    .map((w) => (w.length > 3 && w.endsWith('s') ? w.slice(0, -1) : w));
}
/** Clé de mutualisation d'un document (2 premiers mots significatifs). */
function clefDoc(label) { return motsSignificatifs(label).slice(0, 2).join(' '); }
/** Clé stable d'une démarche hors-catalogue sans id explicite. */
function slug(nom) { return motsSignificatifs(nom).slice(0, 4).join('_'); }

/**
 * Planifie les démarches pour un ensemble d'événements.
 *
 * @param {string[]} evenementIds
 * @param {object} [opts] { profil, memoire, aujourdhui, catalogue }
 * @returns {object} plan
 */
export function planifier(evenementIds, opts = {}) {
  const aujourdhui = opts.aujourdhui || ceJourISO();
  const realisees = opts.memoire ? obligationsRealiseesSet(opts.memoire) : new Set();

  // 1. Collecte + fusion des démarches, et index documents → événements.
  const demarches = new Map();     // clé → démarche
  const docsIndex = new Map();     // clefDoc → { exemple, evenements:Set }
  const nomsEvenements = {};

  for (const evId of evenementIds) {
    const c = resoudreEvenement(evId, { aujourdhui, catalogue: opts.catalogue });
    nomsEvenements[evId] = c.evenement.nom;

    const ajouterDemarche = (cle, nom, { echeance = null, source = null }) => {
      if (realisees.has(cle)) return;
      if (!demarches.has(cle)) demarches.set(cle, { cle, nom, evenements: new Set(), echeance, source });
      const d = demarches.get(cle);
      d.evenements.add(c.evenement.nom);
      if (echeance && (!d.echeance || echeance < d.echeance)) d.echeance = echeance;
      if (source && !d.source) d.source = source;
    };

    for (const o of c.obligations) ajouterDemarche(o.id, o.nom, { echeance: o.echeance, source: o.source });
    for (const o of c.obligationsHorsCatalogue) ajouterDemarche(o.id || slug(o.nom), o.nom, { source: o.source });

    for (const doc of c.documents) {
      const k = clefDoc(doc);
      if (!k) continue;
      if (!docsIndex.has(k)) docsIndex.set(k, { exemple: doc, evenements: new Set() });
      docsIndex.get(k).evenements.add(c.evenement.nom);
    }
  }

  // 2. Graphe de précédence limité aux démarches présentes.
  const present = new Set(demarches.keys());
  const successeurs = new Map([...present].map((k) => [k, new Set()]));
  const predecesseurs = new Map([...present].map((k) => [k, new Set()]));
  for (const [avant, apres] of PRECEDENCES) {
    if (present.has(avant) && present.has(apres)) {
      successeurs.get(avant).add(apres);
      predecesseurs.get(apres).add(avant);
    }
  }

  // 3. Niveau topologique (longueur de la plus longue chaîne de prérequis).
  const niveauMemo = new Map();
  const niveau = (cle, pile = new Set()) => {
    if (niveauMemo.has(cle)) return niveauMemo.get(cle);
    if (pile.has(cle)) return 0; // garde anti-cycle
    pile.add(cle);
    let n = 0;
    for (const p of predecesseurs.get(cle)) n = Math.max(n, niveau(p, pile) + 1);
    pile.delete(cle);
    niveauMemo.set(cle, n);
    return n;
  };

  // 4. Tri : niveau croissant → plus de successeurs (débloque) → échéance → nom.
  const liste = [...demarches.values()].map((d) => ({
    ...d,
    evenements: [...d.evenements],
    niveau: niveau(d.cle),
    debloque: [...successeurs.get(d.cle)].map((k) => demarches.get(k).nom),
  }));
  liste.sort((a, b) =>
    a.niveau - b.niveau
    || b.debloque.length - a.debloque.length
    || ((a.echeance || '9999') < (b.echeance || '9999') ? -1 : (a.echeance || '9999') > (b.echeance || '9999') ? 1 : 0)
    || a.nom.localeCompare(b.nom),
  );

  // 5. Explication + documents mutualisés.
  const demarchesPlan = liste.map((d, i) => ({
    ordre: i + 1,
    cle: d.cle,
    nom: d.nom,
    echeance: d.echeance,
    declenchePar: d.evenements,
    prerequis: [...predecesseurs.get(d.cle)],
    debloque: d.debloque,
    source: d.source,
    explication: `Déclenchée par : ${d.evenements.join(', ')}.`
      + (d.debloque.length ? ` Débloque : ${d.debloque.join(', ')}.` : '')
      + (d.echeance ? ` Échéance ${d.echeance}.` : ''),
  }));

  const documentsMutualises = [...docsIndex.values()]
    .filter((v) => v.evenements.size >= 2)
    .map((v) => ({ document: v.exemple, evenements: [...v.evenements], count: v.evenements.size }))
    .sort((a, b) => b.count - a.count);

  const premiers = demarchesPlan.filter((d) => d.debloque.length).slice(0, 3).map((d) => d.nom);
  const resume = `${demarchesPlan.length} démarche(s) pour ${evenementIds.length} événement(s)`
    + (documentsMutualises.length ? `, dont ${documentsMutualises.length} pièce(s) mutualisée(s)` : '')
    + (premiers.length ? `. Commencer par : ${premiers.join(', ')} (débloquent les suivantes).` : '.');

  return {
    evenements: evenementIds.map((id) => ({ id, nom: nomsEvenements[id] })),
    total: demarchesPlan.length,
    demarches: demarchesPlan,
    documentsMutualises,
    resume,
    note: 'Plan indicatif : l\'ordre reflète des dépendances usuelles entre guichets ; chaque règle reste à vérifier via sa source. Aucune démarche n\'a été effectuée.',
  };
}
