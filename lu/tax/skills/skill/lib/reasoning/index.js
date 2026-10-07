/**
 * lib/reasoning — Moteur de raisonnement & Change Impact.
 *
 * Le planificateur répond « que dois-je faire ? ». Le reasoner répond
 * « pourquoi ? » et surtout « qu'est-ce qui change ? ».
 *
 * Principe : on ne réexécute pas les règles à l'aveugle, on PROPAGE les
 * conséquences d'un changement d'état dans le graphe (comme un moteur de
 * dépendances). Quatre capacités transverses :
 *   - computeDelta()      : ce qui change entre deux situations ;
 *   - computeImpact()     : les conséquences d'un changement d'état ;
 *   - simulateScenario()  : un scénario hypothétique, sans toucher le dossier ;
 *   - explainReasoning()  : une explication traçable (conclusion → règle → source).
 * Plus `transition()` : la machine à états (ancien → nouvel état).
 *
 * Déterministe, hors-ligne, aucune dépendance externe.
 */

import { diagnostiquer } from '../diagnostic/engine.js';
import { chargerCatalogue } from '../diagnostic/index.js';
import { determinerClasseImpot } from '../particulier/index.js';
import { resoudreEvenement } from '../evenements/index.js';
import { planifier } from '../planification/index.js';
import { ceJourISO } from '../diagnostic/provenance.js';

const estVide = (v) => v === undefined || v === null || v === '';

/**
 * Différence champ à champ entre deux états (situations).
 * @returns {{champ, avant, apres}[]}
 */
export function computeDelta(avant = {}, apres = {}) {
  const champs = new Set([...Object.keys(avant), ...Object.keys(apres)]);
  const delta = [];
  for (const c of champs) {
    const a = avant[c], b = apres[c];
    if (JSON.stringify(a) !== JSON.stringify(b)) delta.push({ champ: c, avant: a ?? null, apres: b ?? null });
  }
  return delta;
}

/** Événements de vie associés à un delta (mapping changement → événement). */
export function evenementsPourDelta(delta) {
  const evs = new Set();
  for (const d of delta) {
    if (d.champ === 'situationFamiliale' && ['marie', 'partenariat'].includes(d.apres)) evs.add('mariage_partenariat');
    if (d.champ === 'dateArriveeLux' && !estVide(d.apres)) evs.add('arrivee_luxembourg');
    if (d.champ === 'paysResidence' && !estVide(d.apres)) evs.add('arrivee_luxembourg');
    if (d.champ === 'formeJuridique' && !estVide(d.apres)) evs.add('creation_entreprise');
    if (d.champ === 'statut' && d.apres === 'actif') evs.add('creation_entreprise');
    if (d.champ === 'statut' && ['cessation', 'liquidation'].includes(d.apres)) evs.add('cessation_activite');
    if (d.champ === 'nombreEnfants' && Number(d.apres || 0) > Number(d.avant || 0)) evs.add('naissance');
  }
  return [...evs];
}

/** Valeurs dérivées d'un état (aujourd'hui : classe d'impôt). Chacune sourcée. */
function valeursDerivees(etat) {
  const classe = determinerClasseImpot(etat);
  return { classe_impot: { valeur: classe.classe, source: classe.provenance.source } };
}

/** Conditions d'une obligation qui référencent l'un des champs modifiés. */
function conditionsDeclenchantes(obligation, champsModifies) {
  return (obligation.conditionsApplicabilite || [])
    .filter((c) => champsModifies.has(c.champ))
    .map((c) => `${c.champ} ${c.operateur}${c.valeur != null ? ' ' + c.valeur : ''}`);
}

/**
 * Calcule l'impact d'un changement d'état : obligations qui apparaissent /
 * disparaissent, valeurs dérivées qui changent, domaines et événements
 * impactés. On propage — on ne « refait » pas les démarches.
 *
 * @param {object} etat            État courant (profil/situation).
 * @param {object} changement      Champs modifiés { champ: nouvelleValeur }.
 * @param {object} [opts]          { catalogue, aujourdhui }
 * @returns {object} impact
 */
export function computeImpact(etat = {}, changement = {}, opts = {}) {
  const aujourdhui = opts.aujourdhui || ceJourISO();
  const catalogue = opts.catalogue || chargerCatalogue().obligations;
  const apres = { ...etat, ...changement };
  const delta = computeDelta(etat, apres);
  const champsModifies = new Set(delta.map((d) => d.champ));

  const idsAvant = new Set(diagnostiquer(etat, catalogue, { aujourdhui }).applicables.map((e) => e.obligation.id));
  const diagApres = diagnostiquer(apres, catalogue, { aujourdhui });
  const parId = new Map(diagApres.applicables.map((e) => [e.obligation.id, e]));
  const idsApres = new Set(parId.keys());

  const ligne = (ob) => ({
    id: ob.id, nom: ob.nom, administration: ob.autoriteCompetente || null,
    source: ob.provenance ? ob.provenance.source : null,
    cause: conditionsDeclenchantes(ob, champsModifies),
  });

  const ajoutees = [...idsApres].filter((id) => !idsAvant.has(id)).map((id) => ligne(parId.get(id).obligation));
  const catalogueParId = new Map(catalogue.map((o) => [o.id, o]));
  const retirees = [...idsAvant].filter((id) => !idsApres.has(id)).map((id) => ligne(catalogueParId.get(id)));

  // Valeurs dérivées modifiées (ex. classe d'impôt).
  const dvAvant = valeursDerivees(etat), dvApres = valeursDerivees(apres);
  const valeursModifiees = [];
  for (const k of Object.keys(dvApres)) {
    if (dvAvant[k].valeur !== dvApres[k].valeur) {
      valeursModifiees.push({ nom: k, avant: dvAvant[k].valeur, apres: dvApres[k].valeur, source: dvApres[k].source });
    }
  }

  // Domaines impactés via les événements de vie associés.
  const evenements = evenementsPourDelta(delta);
  const domaines = new Map();
  for (const ev of evenements) {
    for (const a of resoudreEvenement(ev, { aujourdhui, catalogue }).administrations) domaines.set(a.id, a.nom);
  }

  const total = ajoutees.length + retirees.length + valeursModifiees.length;
  return {
    delta,
    evenementsAssocies: evenements,
    domainesImpactes: [...domaines.values()],
    obligations: { ajoutees, retirees },
    valeursModifiees,
    total,
    note: 'Impact propagé dans le graphe (aucune démarche effectuée). Chaque conséquence est reliée à sa source.',
  };
}

/**
 * Simule un scénario hypothétique SANS modifier le dossier utilisateur.
 * Le scénario peut porter des changements d'état et/ou des événements.
 *
 * @param {object} etat
 * @param {object} scenario   { changements?: {...}, evenements?: [ids], libelle? }
 * @param {object} [opts]
 * @returns {object} { hypothetique, libelle, impact?, plan? }
 */
export function simulateScenario(etat = {}, scenario = {}, opts = {}) {
  const gele = JSON.parse(JSON.stringify(etat)); // garantie de non-mutation
  const res = { hypothetique: true, libelle: scenario.libelle || 'Scénario', etatBase: gele };
  if (scenario.changements) res.impact = computeImpact(gele, scenario.changements, opts);
  if (Array.isArray(scenario.evenements) && scenario.evenements.length) {
    res.plan = planifier(scenario.evenements, { profil: { ...gele, ...(scenario.changements || {}) }, aujourdhui: opts.aujourdhui, catalogue: opts.catalogue });
  }
  return res;
}

/**
 * Explication traçable d'un impact : chaque conclusion reliée à sa cause
 * (le champ modifié) et à sa source (la règle).
 * @returns {{conclusion, cause, source}[]}
 */
export function explainReasoning(impact) {
  const out = [];
  for (const v of impact.valeursModifiees) {
    out.push({ conclusion: `${v.nom} : ${v.avant} → ${v.apres}`, cause: 'changement de situation', source: v.source });
  }
  for (const o of impact.obligations.ajoutees) {
    out.push({
      conclusion: `Nouvelle obligation : ${o.nom}`,
      cause: o.cause.length ? `déclenchée car ${o.cause.join(' et ')}` : 'devient applicable',
      source: o.source,
    });
  }
  for (const o of impact.obligations.retirees) {
    out.push({
      conclusion: `Obligation levée : ${o.nom}`,
      cause: o.cause.length ? `car ${o.cause.join(' et ')} n'est plus vérifié` : 'ne s\'applique plus',
      source: o.source,
    });
  }
  return out;
}

/**
 * Machine à états : applique une transition et renvoie l'ancien état, le
 * nouvel état, la date et l'impact propagé.
 *
 * @param {object} etat
 * @param {object} changement
 * @param {object} [opts]   { date, catalogue, aujourdhui }
 */
export function transition(etat = {}, changement = {}, opts = {}) {
  const impact = computeImpact(etat, changement, opts);
  return {
    ancienEtat: { ...etat },
    nouvelEtat: { ...etat, ...changement },
    date: opts.date || ceJourISO(),
    changement,
    impact,
  };
}
