/**
 * lib/diagnostic — Administrative Diagnostic Engine (Milestone 1).
 *
 * Socle technique et modèle de données de l'assistant administratif
 * luxembourgeois. Regroupe :
 *   - le modèle d'entités sourcé (entities.js) ;
 *   - la traçabilité obligatoire des règles (provenance.js) ;
 *   - le moteur profil → obligations → dossiers/échéances (engine.js) ;
 *   - la persistance locale isolée par propriétaire (store.js) ;
 *   - le chargement du catalogue d'obligations sourcé (data/obligations.json).
 *
 * Aucune règle réglementaire n'est codée en dur : elles vivent toutes dans
 * data/obligations.json, chacune avec source + date de vérification + niveau
 * de confiance. Aucune dépendance externe.
 */

import { readFileSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { creerObligation } from './entities.js';

export {
  creerProfilUtilisateur,
  creerProfilSociete,
  creerDossier,
  creerDocument,
  creerObligation,
  ENUMS,
} from './entities.js';

export {
  creerProvenance,
  evaluerFraicheur,
  joursEcoules,
  ceJourISO,
  NIVEAUX_CONFIANCE,
  FRAICHEUR_JOURS_DEFAUT,
} from './provenance.js';

export {
  diagnostiquer,
  obligationApplicable,
  evaluerCondition,
  calculerEcheance,
  dossierDepuisObligation,
  prioriteSelonEcheance,
} from './engine.js';

export { creerStore, creerStoreMemoire } from './store.js';

export {
  QUESTIONS,
  champsPertinents,
  prochaineQuestion,
  questionsRestantes,
  appliquerReponse,
} from './questionnaire.js';

export { construireTableauDeBord } from './dashboard.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const CATALOGUE_PATH = join(__dirname, '..', '..', 'data', 'obligations.json');

/**
 * Charge le catalogue d'obligations sourcé et normalise chaque entrée via
 * creerObligation() (ce qui vérifie qu'aucune n'existe sans source).
 *
 * @param {string} [fichier] Chemin alternatif (tests).
 * @returns {{as_of: string|null, obligations: object[]}}
 */
export function chargerCatalogue(fichier = CATALOGUE_PATH) {
  if (!existsSync(fichier)) return { as_of: null, obligations: [] };
  const brut = JSON.parse(readFileSync(fichier, 'utf8'));
  const obligations = (brut.obligations || []).map((o) => creerObligation(o));
  return { as_of: brut.as_of || null, obligations };
}
