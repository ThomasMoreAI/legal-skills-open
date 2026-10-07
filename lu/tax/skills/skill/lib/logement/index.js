/**
 * lib/logement — Logement & immobilier (Milestone 8).
 *
 * Intègre les calculateurs existants dans un parcours global :
 *   - lib/bellegen-akt : droits d'enregistrement, crédit « Bëllegen Akt »,
 *     honoraires de notaire (achat immobilier).
 * et propose automatiquement les démarches associées selon la situation
 * (locataire, propriétaire, acheteur/vendeur).
 *
 * Aucune règle chiffrée n'est affichée sans source. Les plafonds susceptibles
 * d'avoir évolué (garantie locative) sont marqués « à revérifier ».
 *
 * Aucune dépendance externe.
 */

import { calculerBellegenAkt, estimerHonoraires } from '../bellegen-akt/index.js';
import { ceJourISO } from '../diagnostic/provenance.js';

const round2 = (n) => Math.round(n * 100) / 100;

const SRC = {
  bail: 'https://guichet.public.lu/fr/citoyens/logement/location/droits-obligations-locataire.html',
  garantie: 'https://guichet.public.lu/fr/citoyens/logement/location/bail-a-loyer/garantie-locative.html',
  aides: 'https://guichet.public.lu/fr/citoyens/logement/aides-logement.html',
  enregistrement: 'https://guichet.public.lu/fr/citoyens/logement/location/bail-a-loyer.html',
  achat: 'https://guichet.public.lu/fr/citoyens/logement/achat-immobilier.html',
  bellegen: 'https://guichet.public.lu/fr/citoyens/logement/achat-immobilier/credit-impot-bellegen-akt.html',
  revenusLocatifs: 'https://guichet.public.lu/fr/citoyens/impots-taxes/activite-salariee-resident/revenus-locatifs.html',
  impotFoncier: 'https://guichet.public.lu/fr/citoyens/logement/proprietaire.html',
};

/**
 * Montant maximum de la garantie locative selon le loyer mensuel.
 * Le nombre de mois plafond a fait l'objet de réformes récentes : on renvoie
 * les options usuelles (2 et 3 mois) en signalant qu'il faut vérifier la
 * valeur en vigueur, plutôt que d'affirmer un chiffre unique.
 *
 * @param {number} loyerMensuel
 */
export function garantieLocativeMax(loyerMensuel) {
  if (!Number.isFinite(loyerMensuel) || loyerMensuel <= 0) throw new Error('loyerMensuel doit être un nombre > 0');
  return {
    loyerMensuel,
    options: [2, 3].map((mois) => ({ mois, montant: round2(loyerMensuel * mois) })),
    provenance: {
      source: SRC.garantie,
      dateVerification: '2026-06-15',
      niveauConfiance: 'derive',
      note: 'Plafond légal de la garantie locative exprimé en mois de loyer — vérifier la valeur en vigueur (réformes récentes) avant de l\'opposer au bailleur.',
    },
  };
}

/**
 * Analyse d'une acquisition immobilière : réutilise le calculateur Bëllegen Akt
 * (droits d'enregistrement + crédit) et l'estimation des honoraires de notaire.
 *
 * @param {object} input { prix, nbAcquereurs, luxVille, dateActe, bellegenAkt }
 */
export function analyseAcquisition(input) {
  const frais = calculerBellegenAkt(input);
  return {
    prix: input.prix,
    frais,
    honorairesNotaire: estimerHonoraires(input.prix),
    creditBellegenAkt: frais.bellegenAkt.abattementEffectif,
    fraisTotaux: frais.total,
    provenance: {
      source: SRC.bellegen,
      dateVerification: '2026-06-15',
      niveauConfiance: 'derive',
      note: 'Estimation indicative (droits d\'enregistrement + transcription + honoraires). Le crédit Bëllegen Akt suppose l\'affectation à la résidence principale.',
    },
  };
}

function etape(titre, description, source, extra = {}) {
  return { titre, description, source, ...extra };
}

/**
 * Détermine la situation logement à traiter.
 * opts.projet ('achat'|'location'|'vente') prime, sinon profil.statutLogement.
 */
function situationLogement(profil, opts) {
  if (opts.projet === 'achat') return 'acheteur';
  if (opts.projet === 'vente') return 'vendeur';
  if (opts.projet === 'location') return 'locataire';
  if (profil.statutLogement === 'proprietaire') return 'proprietaire';
  if (profil.statutLogement === 'locataire') return 'locataire';
  return 'inconnu';
}

/**
 * Parcours logement complet, avec démarches proposées et calculs intégrés
 * quand les montants sont fournis.
 *
 * @param {object} profil       { statutLogement, ... }
 * @param {object} [opts]       { projet, loyerMensuel, prixAchat, nbAcquereurs, luxVille, dateActe, aujourdhui }
 * @returns {{situation, etapes, calculs, avertissement}}
 */
export function parcoursLogement(profil = {}, opts = {}) {
  const situation = situationLogement(profil, opts);
  const etapes = [];
  const calculs = {};

  if (situation === 'locataire') {
    etapes.push(etape('Vérifier le contrat de bail', 'Mentions obligatoires, durée, montant du loyer et des charges.', SRC.bail));
    etapes.push(etape('État des lieux d\'entrée', 'À établir contradictoirement à l\'entrée dans le logement.', SRC.bail));
    etapes.push(etape('Constituer la garantie locative', 'Plafonnée en mois de loyer (à vérifier).', SRC.garantie));
    etapes.push(etape('Enregistrer le bail', 'Formalité d\'enregistrement du bail auprès de l\'AED.', SRC.enregistrement));
    etapes.push(etape('Vérifier l\'éligibilité aux aides au logement', 'Subvention de loyer et autres aides selon revenus.', SRC.aides));
    etapes.push(etape('Déclarer le changement d\'adresse', 'À la commune du nouveau lieu de résidence.', SRC.bail));
    if (Number.isFinite(opts.loyerMensuel)) calculs.garantie = garantieLocativeMax(opts.loyerMensuel);
  } else if (situation === 'acheteur') {
    etapes.push(etape('Signer le compromis de vente', 'Engagement réciproque avant l\'acte notarié.', SRC.achat));
    etapes.push(etape('Boucler le financement', 'Prêt immobilier ; vérifier l\'éligibilité à la subvention d\'intérêt.', SRC.aides));
    etapes.push(etape('Acte notarié et droits d\'enregistrement', 'Calcul des droits et du crédit Bëllegen Akt (résidence principale).', SRC.bellegen));
    etapes.push(etape('Souscrire une assurance habitation', 'Généralement exigée par la banque.', SRC.achat));
    etapes.push(etape('Déclarer le changement d\'adresse', 'À la commune du nouveau lieu de résidence.', SRC.achat));
    if (Number.isFinite(opts.prixAchat)) {
      calculs.acquisition = analyseAcquisition({
        prix: opts.prixAchat,
        nbAcquereurs: opts.nbAcquereurs || 1,
        luxVille: Boolean(opts.luxVille),
        dateActe: opts.dateActe || null,
      });
    }
  } else if (situation === 'proprietaire' || situation === 'vendeur') {
    etapes.push(etape('Déclarer les revenus locatifs', 'Si le bien est mis en location, revenus à déclarer à l\'ACD.', SRC.revenusLocatifs));
    etapes.push(etape('Impôt foncier communal', 'Taxe foncière due à la commune.', SRC.impotFoncier));
    etapes.push(etape('Assurance du bien', 'Assurance propriétaire / propriétaire non occupant.', SRC.achat));
    if (situation === 'vendeur') {
      etapes.push(etape('Anticiper la plus-value immobilière', 'Régime de la plus-value selon la durée de détention et l\'affectation.', SRC.revenusLocatifs));
    }
  }

  return {
    situation,
    etapes,
    calculs,
    avertissement: situation === 'inconnu'
      ? 'Situation logement non déterminée : précisez le statut (locataire/propriétaire) ou le projet (achat/location/vente).'
      : null,
  };
}
