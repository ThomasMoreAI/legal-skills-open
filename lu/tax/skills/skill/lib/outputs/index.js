/**
 * lib/outputs — Artefacts métier & adaptateurs (couche « Outputs »).
 *
 * Le moteur ne se connecte pas à des services : il PRODUIT des artefacts métier
 * — Timeline, DocumentPackage, Reminders, Report — et des ADAPTATEURS les
 * exportent vers des formats/services (.ics, Markdown, texte, … demain PDF,
 * email, Peppol, MyGuichet). Ajouter une sortie = ajouter un adaptateur, sans
 * toucher au moteur.
 *
 *   Mission → Outputs → { Timeline, Documents, Notifications, Reports } → adaptateurs
 *
 * Déterministe, hors-ligne, aucune dépendance externe.
 */

import { avancement, prochaineEtape } from '../workflows/index.js';
import { evaluerMission } from '../evaluation/index.js';
import { resoudreEvenement } from '../evenements/index.js';
import { chargerCatalogue } from '../diagnostic/index.js';
import { niveauAlerte } from '../rappels/index.js';
import { ceJourISO } from '../diagnostic/provenance.js';
import { timelineVersICS } from './ics.js';

export { timelineVersICS } from './ics.js';

// ---------------------------------------------------------------------------
// Artefacts métier
// ---------------------------------------------------------------------------

/** Priorité d'une étape (haute si bloquante / échéance proche ou dépassée). */
function prioriteEtape(etape, aujourdhui) {
  if (etape.debloque && etape.debloque.length) return 'high';
  const a = niveauAlerte({ echeance: etape.echeance, statut: etape.statut }, aujourdhui);
  if (a.couleur === 'rouge' || a.couleur === 'orange') return 'high';
  if (a.couleur === 'jaune') return 'medium';
  return 'low';
}

/**
 * Timeline : liste de TimelineEvent (modèle unique, indépendant du format).
 * @returns {{mission, evenements: object[]}}
 */
export function timeline(mission, { aujourdhui = ceJourISO() } = {}) {
  const evenements = mission.etapes.map((e) => ({
    id: e.id,
    title: e.nom,
    date: null,
    deadline: e.echeance || null,
    priority: prioriteEtape(e, aujourdhui),
    blocking: Boolean(e.debloque && e.debloque.length),
    mission: mission.objectif,
    documents: [],
    source: e.source || null,
    status: e.statut === 'fait' ? 'done' : 'todo',
  }));
  return { mission: mission.objectif, evenements };
}

/**
 * DocumentPackage : les pièces à réunir pour la mission (modèle unique).
 * @returns {{mission, pieces: object[]}}
 */
export function documentPackage(mission, { aujourdhui = ceJourISO(), catalogue } = {}) {
  const cat = catalogue || chargerCatalogue().obligations;
  const vues = new Map();
  for (const ev of mission.evenements) {
    const c = resoudreEvenement(ev, { catalogue: cat, aujourdhui });
    for (const doc of c.documents) {
      const cle = doc.toLowerCase();
      if (!vues.has(cle)) vues.set(cle, { nom: doc, requisPour: new Set([c.evenement.nom]), source: c.source });
      else vues.get(cle).requisPour.add(c.evenement.nom);
    }
  }
  const pieces = [...vues.values()].map((p) => ({ nom: p.nom, requisPour: [...p.requisPour], source: p.source }));
  return { mission: mission.objectif, pieces };
}

/**
 * Reminders : rappels avant échéance (modèle unique).
 * @returns {{mission, rappels: object[]}}
 */
export function reminders(mission, { aujourdhui = ceJourISO(), preavisJours = 7 } = {}) {
  const rappels = [];
  for (const e of mission.etapes) {
    if (e.statut === 'fait' || !e.echeance) continue;
    const base = Date.parse(`${e.echeance}T00:00:00Z`);
    const when = new Date(base - preavisJours * 86_400_000).toISOString().slice(0, 10);
    rappels.push({ title: `À préparer : ${e.nom}`, when, deadline: e.echeance, mission: mission.objectif, priority: prioriteEtape(e, aujourdhui), source: e.source || null });
  }
  return { mission: mission.objectif, rappels: rappels.sort((a, b) => a.when.localeCompare(b.when)) };
}

/** Report : rapport d'évaluation de la mission (réutilise lib/evaluation). */
export function report(mission, opts = {}) {
  return evaluerMission(mission, opts);
}

// ---------------------------------------------------------------------------
// Adaptateurs (format d'export) — registre extensible
// ---------------------------------------------------------------------------

function timelineVersTexte(tl) {
  const l = [`Timeline — ${tl.mission}`, ''];
  for (const e of tl.evenements) l.push(`  ${e.deadline ? e.deadline : '——'}  [${e.priority}]${e.blocking ? ' ⛓' : ''} ${e.title}`);
  return l.join('\n');
}

function documentsVersMarkdown(pkg) {
  const l = [`# Dossier de pièces — ${pkg.mission}`, ''];
  for (const p of pkg.pieces) l.push(`- [ ] **${p.nom}**${p.requisPour.length ? ` _(pour : ${p.requisPour.join(', ')})_` : ''}`);
  return l.join('\n');
}

function remindersVersTexte(r) {
  const l = [`Rappels — ${r.mission}`, ''];
  for (const x of r.rappels) l.push(`  ${x.when} → ${x.title} (échéance ${x.deadline})`);
  return l.join('\n');
}

function reportVersMarkdown(rep) {
  const l = [`# Rapport de mission — ${rep.mission}`, '',
    `**Confiance globale : ${rep.confianceGlobale} %** — complète : ${rep.complete ? 'oui' : 'non'} (${rep.avancement.pourcentage} %)`, ''];
  const bloc = (t, a) => { l.push(`## ${t}`); if (!a.length) l.push('_—_'); for (const x of a) l.push(`- ${x}`); l.push(''); };
  bloc('Informations manquantes', rep.informationsManquantes);
  bloc('Hypothèses', rep.hypotheses);
  bloc('Risques', rep.risques);
  bloc('Points bloquants', rep.pointsBloquants);
  bloc('Sources', rep.sources);
  return l.join('\n');
}

/** Registre `type:format` → adaptateur. Ajouter un format = enregistrer ici. */
export const ADAPTATEURS = new Map([
  ['timeline:ics', (art, opts) => timelineVersICS(art.evenements, opts)],
  ['timeline:texte', (art) => timelineVersTexte(art)],
  ['documents:markdown', (art) => documentsVersMarkdown(art)],
  ['notifications:texte', (art) => remindersVersTexte(art)],
  ['reports:markdown', (art) => reportVersMarkdown(art)],
]);

export function enregistrerAdaptateur(type, format, fn) {
  ADAPTATEURS.set(`${type}:${format}`, fn);
}

const BUILDERS = { timeline, documents: documentPackage, notifications: reminders, reports: report };

/**
 * Produit un artefact d'une mission et l'exporte dans un format.
 *
 * @param {object} mission
 * @param {object} opts { type: 'timeline'|'documents'|'notifications'|'reports', format, ...builderOpts }
 * @returns {{type, format, artefact, sortie}}
 */
export function produire(mission, opts = {}) {
  const type = opts.type;
  const builder = BUILDERS[type];
  if (!builder) throw new Error(`Type d'output inconnu : ${type} (attendu : ${Object.keys(BUILDERS).join(', ')})`);
  const artefact = builder(mission, opts);
  let sortie = null;
  if (opts.format) {
    const adaptateur = ADAPTATEURS.get(`${type}:${opts.format}`);
    if (!adaptateur) throw new Error(`Adaptateur inconnu : ${type}:${opts.format} (disponibles : ${[...ADAPTATEURS.keys()].join(', ')})`);
    sortie = adaptateur(artefact, opts);
  }
  return { type, format: opts.format || null, artefact, sortie };
}
