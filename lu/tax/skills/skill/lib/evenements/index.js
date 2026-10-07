/**
 * lib/evenements — Ontologie des événements de vie (couche « cerveau »).
 *
 * Transforme le catalogue plat d'obligations en GRAPHE : un événement de vie
 * déclenche une chaîne
 *   événement → conséquences → administrations → obligations → documents
 *             → délais → exceptions → checklist.
 *
 * Les obligations référencées sont RELIÉES à data/obligations.json (source de
 * vérité unique) : le graphe ne duplique pas les règles, il les orchestre. Les
 * agents métier (TVA, CNS, Frontaliers…) deviennent des vues sur ce graphe.
 *
 * Aucune dépendance externe.
 */

import { readFileSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { chargerCatalogue } from '../diagnostic/index.js';
import { calculerEcheance } from '../diagnostic/engine.js';
import { ceJourISO } from '../diagnostic/provenance.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const DATA_PATH = join(__dirname, '..', '..', 'data', 'evenements-vie.json');

/** Charge l'ontologie des événements de vie. */
export function chargerEvenements(fichier = DATA_PATH) {
  if (!existsSync(fichier)) return { as_of: null, evenements: [] };
  return JSON.parse(readFileSync(fichier, 'utf8'));
}

/** Liste synthétique des événements (id + nom). */
export function listerEvenements() {
  return chargerEvenements().evenements.map((e) => ({ id: e.id, nom: e.nom }));
}

/**
 * Identifie l'événement de vie évoqué par un texte (score par mots-clés).
 * @returns {string|null} id de l'événement, ou null
 */
export function identifierEvenement(texte) {
  const t = String(texte || '').toLowerCase();
  let meilleur = null;
  for (const e of chargerEvenements().evenements) {
    let score = 0;
    for (const mc of e.motsCles) if (t.includes(mc.toLowerCase())) score++;
    if (score > 0 && (!meilleur || score > meilleur.score)) meilleur = { id: e.id, score };
  }
  return meilleur ? meilleur.id : null;
}

/**
 * Résout un événement en sa chaîne complète, en reliant les obligations au
 * catalogue (nom, autorité, source, échéance calculée).
 *
 * @param {string} idOuTexte      id d'événement ou texte libre.
 * @param {object} [opts]         { aujourdhui, catalogue }
 * @returns {object} chaîne résolue
 */
export function resoudreEvenement(idOuTexte, opts = {}) {
  const aujourdhui = opts.aujourdhui || ceJourISO();
  const data = chargerEvenements();
  const id = data.evenements.some((e) => e.id === idOuTexte) ? idOuTexte : identifierEvenement(idOuTexte);
  const ev = data.evenements.find((e) => e.id === id);
  if (!ev) throw new Error(`Événement de vie inconnu : ${idOuTexte}`);

  const catalogue = opts.catalogue || chargerCatalogue().obligations;
  const parId = new Map(catalogue.map((o) => [o.id, o]));

  const obligations = ev.obligations.map((oid) => {
    const ob = parId.get(oid);
    if (!ob) return { id: oid, nom: null, resolue: false, avertissement: 'Obligation non trouvée dans le catalogue.' };
    return {
      id: ob.id,
      nom: ob.nom,
      resolue: true,
      autorite: ob.autoriteCompetente || null,
      frequence: ob.frequence,
      echeance: calculerEcheance(ob, { aujourdhui }),
      source: ob.provenance ? ob.provenance.source : null,
    };
  });

  return {
    evenement: { id: ev.id, nom: ev.nom },
    consequences: ev.consequences || [],
    administrations: ev.administrations || [],
    obligations,
    obligationsHorsCatalogue: ev.obligationsHorsCatalogue || [],
    documents: ev.documents || [],
    delais: ev.delais || [],
    exceptions: ev.exceptions || [],
    checklist: ev.checklist || [],
    source: ev.source,
  };
}

/**
 * Vérifie l'intégrité du graphe : toute obligation référencée existe dans le
 * catalogue. Utilisé en test et par un contrôle qualité.
 * @returns {{ok: boolean, manquantes: object[]}}
 */
export function verifierIntegrite(opts = {}) {
  const catalogue = opts.catalogue || chargerCatalogue().obligations;
  const ids = new Set(catalogue.map((o) => o.id));
  const manquantes = [];
  for (const ev of chargerEvenements().evenements) {
    for (const oid of ev.obligations) if (!ids.has(oid)) manquantes.push({ evenement: ev.id, obligation: oid });
  }
  return { ok: manquantes.length === 0, manquantes };
}
