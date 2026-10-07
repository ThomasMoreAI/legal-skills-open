/**
 * lib/diagnostic/engine.js — Administrative Diagnostic Engine (cœur, Milestone 1).
 *
 * Relie un profil (utilisateur ou société) au catalogue d'obligations sourcées
 * et produit :
 *   - la liste des obligations applicables, avec la RAISON de leur application ;
 *   - une échéance calculée par obligation (déterministe) ;
 *   - un Dossier prêt à l'emploi (source incluse) pour chaque obligation.
 *
 * Le moteur n'invente jamais une obligation : il ne fait qu'évaluer les
 * conditions déclaratives portées par le catalogue data/obligations.json.
 *
 * Aucune dépendance externe.
 */

import { ceJourISO } from './provenance.js';
import { creerDossier } from './entities.js';

/** Valeur d'un champ, avec support d'un chemin pointé simple (« a.b »). */
function lire(cible, champ) {
  if (champ.includes('.')) {
    return champ.split('.').reduce((o, k) => (o == null ? undefined : o[k]), cible);
  }
  return cible ? cible[champ] : undefined;
}

/**
 * Évalue une condition déclarative contre un profil.
 * @returns {boolean}
 */
export function evaluerCondition(cible, cond) {
  const v = lire(cible, cond.champ);
  switch (cond.operateur) {
    case 'egal': return v === cond.valeur;
    case 'different': return v !== cond.valeur;
    case 'vrai': return v === true;
    case 'faux': return v === false || v == null;
    case 'present': return v !== undefined && v !== null && v !== '' && !(Array.isArray(v) && v.length === 0);
    case 'absent': return v === undefined || v === null || v === '' || (Array.isArray(v) && v.length === 0);
    case 'superieur': return typeof v === 'number' && v > cond.valeur;
    case 'inferieur': return typeof v === 'number' && v < cond.valeur;
    case 'contient': return Array.isArray(v) ? v.includes(cond.valeur) : typeof v === 'string' && v.includes(cond.valeur);
    default: return false;
  }
}

/**
 * Une obligation s'applique si TOUTES ses conditions sont vraies (ET logique).
 * Une obligation sans condition s'applique universellement (à sa population).
 *
 * @returns {{applicable: boolean, raisons: string[], manquantes: string[]}}
 *   - raisons   : conditions satisfaites (justification affichable) ;
 *   - manquantes: champs du profil non renseignés qui empêchent de conclure.
 */
export function obligationApplicable(cible, obligation) {
  const raisons = [];
  const manquantes = [];
  let applicable = true;
  for (const cond of obligation.conditionsApplicabilite || []) {
    const valeur = lire(cible, cond.champ);
    const renseigne = valeur !== undefined && valeur !== null && valeur !== '';
    const ok = evaluerCondition(cible, cond);
    if (!renseigne && cond.operateur !== 'absent' && cond.operateur !== 'faux') {
      manquantes.push(cond.champ);
      applicable = false;
      continue;
    }
    if (ok) {
      raisons.push(descriptionCondition(cond));
    } else {
      applicable = false;
    }
  }
  return { applicable, raisons, manquantes };
}

function descriptionCondition(cond) {
  const map = {
    egal: `${cond.champ} = ${cond.valeur}`,
    different: `${cond.champ} ≠ ${cond.valeur}`,
    vrai: `${cond.champ}`,
    faux: `absence de ${cond.champ}`,
    present: `${cond.champ} renseigné`,
    absent: `${cond.champ} non renseigné`,
    superieur: `${cond.champ} > ${cond.valeur}`,
    inferieur: `${cond.champ} < ${cond.valeur}`,
    contient: `${cond.champ} contient ${cond.valeur}`,
  };
  return map[cond.operateur] ?? `${cond.champ} ${cond.operateur} ${cond.valeur}`;
}

/**
 * Diagnostique un profil contre un catalogue d'obligations.
 *
 * @param {object} cible                 ProfilUtilisateur ou ProfilSociete.
 * @param {object[]} catalogue           Tableau d'Obligation (statut 'actif').
 * @param {object} [opts]
 * @param {string} [opts.aujourdhui]     Date de référence (déterminisme des échéances).
 * @returns {{applicables, aClarifier, nonApplicables}}
 *   Chaque entrée applicable/aClarifier contient { obligation, raisons, manquantes, echeance }.
 */
export function diagnostiquer(cible, catalogue, { aujourdhui = ceJourISO() } = {}) {
  const applicables = [];
  const aClarifier = [];
  const nonApplicables = [];
  for (const ob of catalogue) {
    if (ob.statut === 'obsolete') continue;
    const { applicable, raisons, manquantes } = obligationApplicable(cible, ob);
    const echeance = calculerEcheance(ob, { aujourdhui });
    const entree = { obligation: ob, raisons, manquantes, echeance };
    if (applicable) applicables.push(entree);
    else if (manquantes.length) aClarifier.push(entree);
    else nonApplicables.push(entree);
  }
  return { applicables, aClarifier, nonApplicables };
}

/**
 * Calcule la prochaine échéance (YYYY-MM-DD) d'une obligation à partir de sa
 * fréquence et de son motif `dateLimite`. Déterministe (dépend uniquement de
 * `aujourdhui`). Retourne null si non calculable.
 *
 * Motifs `dateLimite` supportés :
 *   - 'MM-JJ'                 → prochaine occurrence annuelle de ce jour.
 *   - 'J+N'                   → N jours après la période courante (fréquence).
 *   - 'jour:N'               → le N du mois/trimestre suivant.
 * Fréquences : 'mensuelle', 'trimestrielle', 'annuelle', 'ponctuelle'.
 */
export function calculerEcheance(obligation, { aujourdhui = ceJourISO() } = {}) {
  const [Y, M, D] = aujourdhui.split('-').map(Number);
  const dl = obligation.dateLimite;
  const iso = (y, m, d) => `${y}-${String(m).padStart(2, '0')}-${String(d).padStart(2, '0')}`;
  const dernierJour = (y, m) => new Date(Date.UTC(y, m, 0)).getUTCDate(); // m = 1..12

  const jourMotif = dl && /^jour:(\d{1,2})$/.exec(dl);

  switch (obligation.frequence) {
    case 'mensuelle': {
      const jour = jourMotif ? Number(jourMotif[1]) : 15;
      // Échéance = `jour` du mois suivant (déclaration de la période écoulée).
      let y = Y, m = M + 1;
      if (m > 12) { m = 1; y += 1; }
      return iso(y, m, Math.min(jour, dernierJour(y, m)));
    }
    case 'trimestrielle': {
      const jour = jourMotif ? Number(jourMotif[1]) : 15;
      // Fin du trimestre courant → échéance le `jour` du mois suivant la fin.
      const finTrimestreMois = Math.ceil(M / 3) * 3; // 3,6,9,12
      let y = Y, m = finTrimestreMois + 1;
      if (m > 12) { m = 1; y += 1; }
      return iso(y, m, Math.min(jour, dernierJour(y, m)));
    }
    case 'annuelle': {
      const mmjj = dl && /^(\d{2})-(\d{2})$/.exec(dl);
      const mm = mmjj ? Number(mmjj[1]) : 3;
      const jj = mmjj ? Number(mmjj[2]) : 31;
      // Prochaine occurrence : cette année si encore à venir, sinon l'an prochain.
      const candidat = iso(Y, mm, Math.min(jj, dernierJour(Y, mm)));
      if (candidat >= aujourdhui) return candidat;
      return iso(Y + 1, mm, Math.min(jj, dernierJour(Y + 1, mm)));
    }
    default:
      // 'ponctuelle' ou fréquence inconnue : pas d'échéance récurrente calculable.
      return dl && /^\d{4}-\d{2}-\d{2}$/.test(dl) ? dl : null;
  }
}

/**
 * Transforme une obligation applicable en Dossier prêt à suivre.
 * Reprend la provenance de l'obligation (jamais de dossier réglementaire
 * sans source). La priorité découle de la proximité de l'échéance.
 *
 * @param {object} entree  Élément renvoyé par diagnostiquer() (applicables[]).
 * @param {object} [opts]  { profilId, societeId, aujourdhui, id, maintenant }
 * @returns {object} Dossier
 */
export function dossierDepuisObligation(entree, opts = {}) {
  const { obligation: ob, raisons = [], echeance } = entree;
  const aujourdhui = opts.aujourdhui || ceJourISO();
  return creerDossier({
    id: opts.id,
    maintenant: opts.maintenant || aujourdhui,
    categorie: ob.categorie,
    administration: ob.autoriteCompetente,
    typeDemarche: ob.nom,
    priorite: prioriteSelonEcheance(echeance, aujourdhui),
    echeance,
    documentsRequis: ob.piecesRequises,
    prochainesActions: raisons.length ? [`S'applique car : ${raisons.join(' ; ')}`] : [],
    risques: ob.penalites ? [ob.penalites] : [],
    provenance: ob.provenance,
    obligationId: ob.id,
    profilId: opts.profilId ?? null,
    societeId: opts.societeId ?? null,
  });
}

/** Déduit la colonne de priorité du tableau de bord selon l'échéance. */
export function prioriteSelonEcheance(echeance, aujourdhui = ceJourISO()) {
  if (!echeance) return 'a_surveiller';
  const jours = Math.floor((Date.parse(`${echeance}T00:00:00Z`) - Date.parse(`${aujourdhui}T00:00:00Z`)) / 86_400_000);
  if (jours < 0) return 'obligatoire_maintenant'; // dépassée → à traiter d'urgence
  if (jours <= 30) return 'obligatoire_maintenant';
  if (jours <= 90) return 'a_faire_prochainement';
  return 'a_surveiller';
}
