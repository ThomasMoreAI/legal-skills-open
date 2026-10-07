/**
 * lib/diagnostic/store.js — Persistance locale des entités du diagnostic.
 *
 * Dépôt (repository) minimaliste, zéro-dépendance, adossé à un unique fichier
 * JSON. Chaque collection (profils, societes, dossiers, documents) est isolée.
 * Les ids sont attribués de façon déterministe (`<prefixe>_<n>`) à partir de
 * l'état de la collection — aucun Date.now / Math.random requis.
 *
 * Deux fabriques :
 *   - creerStore({ fichier })  : persistance sur disque (CLI, app).
 *   - creerStoreMemoire()      : purement en mémoire (tests).
 *
 * Séparation stricte par propriétaire : chaque entité stockée porte les clés
 * profilId / societeId. `listerPour(collection, { profilId })` filtre dessus,
 * ce qui prépare la conformité RGPD (Milestone 12).
 */

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { dirname } from 'node:path';

const COLLECTIONS = ['profils', 'societes', 'dossiers', 'documents'];
const PREFIXES = { profils: 'usr', societes: 'soc', dossiers: 'dos', documents: 'doc' };

function etatVide() {
  return { version: 1, profils: [], societes: [], dossiers: [], documents: [] };
}

function fabrique(charger, sauver) {
  let etat = charger();

  function prochainId(collection) {
    const prefixe = PREFIXES[collection];
    let max = 0;
    for (const e of etat[collection]) {
      const m = e.id && new RegExp(`^${prefixe}_(\\d+)$`).exec(e.id);
      if (m) max = Math.max(max, Number(m[1]));
    }
    return `${prefixe}_${max + 1}`;
  }

  return {
    /** Ajoute une entité (id attribué s'il manque). Retourne l'entité stockée. */
    ajouter(collection, entite) {
      if (!COLLECTIONS.includes(collection)) throw new Error(`Collection inconnue : ${collection}`);
      const stocke = { ...entite };
      if (!stocke.id) stocke.id = prochainId(collection);
      if (etat[collection].some((e) => e.id === stocke.id)) {
        throw new Error(`${collection} : id déjà présent (${stocke.id})`);
      }
      etat[collection].push(stocke);
      sauver(etat);
      return stocke;
    },

    /** Remplace une entité existante (par id). */
    mettreAJour(collection, id, patch) {
      const i = etat[collection].findIndex((e) => e.id === id);
      if (i === -1) throw new Error(`${collection} : id introuvable (${id})`);
      etat[collection][i] = { ...etat[collection][i], ...patch, id };
      sauver(etat);
      return etat[collection][i];
    },

    obtenir(collection, id) {
      return etat[collection].find((e) => e.id === id) || null;
    },

    lister(collection) {
      return etat[collection].slice();
    },

    /** Liste filtrée par propriétaire (RGPD : séparation stricte des données). */
    listerPour(collection, { profilId, societeId } = {}) {
      return etat[collection].filter(
        (e) => (profilId ? e.profilId === profilId : true) && (societeId ? e.societeId === societeId : true),
      );
    },

    /** Supprime une entité (droit à l'effacement). */
    supprimer(collection, id) {
      const avant = etat[collection].length;
      etat[collection] = etat[collection].filter((e) => e.id !== id);
      sauver(etat);
      return etat[collection].length < avant;
    },

    /** Export intégral (portabilité RGPD). */
    exporter() {
      return JSON.parse(JSON.stringify(etat));
    },
  };
}

/** Store adossé à un fichier JSON sur disque. */
export function creerStore({ fichier }) {
  if (!fichier) throw new Error('creerStore : chemin de fichier requis');
  const charger = () => {
    if (!existsSync(fichier)) return etatVide();
    try {
      return { ...etatVide(), ...JSON.parse(readFileSync(fichier, 'utf8')) };
    } catch {
      return etatVide();
    }
  };
  const sauver = (etat) => {
    mkdirSync(dirname(fichier), { recursive: true });
    writeFileSync(fichier, JSON.stringify(etat, null, 2));
  };
  return fabrique(charger, sauver);
}

/** Store en mémoire (tests, prévisualisation). */
export function creerStoreMemoire(initial) {
  let etat = { ...etatVide(), ...(initial || {}) };
  return fabrique(
    () => etat,
    (nouvel) => { etat = nouvel; },
  );
}
