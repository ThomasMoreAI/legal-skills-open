/**
 * lib/courriers — Génération de courriers et dossiers (Milestone 9).
 *
 * Transforme les diagnostics en documents concrets : réponse à une
 * administration, demande de délai, demande d'information, contestation,
 * transmission de pièces, déclaration de changement, courriers à un
 * propriétaire / employeur / comptable, et dossier récapitulatif.
 *
 * Chaque courrier contient : expéditeur, destinataire, objet, références,
 * faits, demande, pièces jointes, date, formule de politesse.
 *
 * RÈGLE STRICTE : tout courrier est produit à l'état de PROJET. Aucun envoi
 * n'est déclenché ; la validation humaine est explicitement rappelée.
 *
 * Aucune dépendance externe.
 */

import { ceJourISO } from '../diagnostic/provenance.js';

const AVERTISSEMENT = 'PROJET — à relire, compléter et signer. Aucun envoi automatique.';

/** Présélections par type de courrier (objet et corps par défaut). */
export const TYPES_COURRIER = {
  reponse_administration: {
    objet: 'Réponse à votre courrier',
    demande: 'Vous trouverez ci-joint les éléments demandés en réponse à votre courrier.',
  },
  demande_delai: {
    objet: 'Demande de délai',
    demande: 'Je sollicite un délai supplémentaire pour donner suite à votre demande.',
  },
  demande_information: {
    objet: 'Demande d\'information',
    demande: 'Je vous prie de bien vouloir me communiquer les informations et précisions nécessaires.',
  },
  contestation: {
    objet: 'Réclamation / contestation',
    demande: 'Je conteste la décision et sollicite le réexamen de ma situation au vu des éléments exposés.',
  },
  transmission_pieces: {
    objet: 'Transmission de pièces',
    demande: 'Vous trouverez ci-joint les pièces demandées.',
  },
  declaration_changement: {
    objet: 'Déclaration de changement',
    demande: 'Je vous informe du changement suivant afin que mon dossier soit mis à jour.',
  },
  courrier_proprietaire: {
    objet: 'Courrier relatif au logement',
    demande: 'Je me permets de vous solliciter concernant le logement objet de notre bail.',
  },
  courrier_employeur: {
    objet: 'Courrier à l\'employeur',
    demande: 'Je me permets de vous adresser la présente concernant ma situation.',
  },
  courrier_comptable: {
    objet: 'Note à destination du comptable / de la fiduciaire',
    demande: 'Voici les éléments et questions à traiter pour la prochaine échéance.',
  },
};

function bloc(entite) {
  if (!entite) return null;
  if (typeof entite === 'string') return { nom: entite };
  return entite;
}

/**
 * Génère un courrier structuré (projet).
 *
 * @param {string} type      Une clé de TYPES_COURRIER.
 * @param {object} donnees
 * @param {object|string} donnees.expediteur
 * @param {object|string} donnees.destinataire
 * @param {string[]}      [donnees.references]
 * @param {string}        [donnees.objet]        Remplace l'objet par défaut.
 * @param {string}        [donnees.faits]        Exposé des faits.
 * @param {string}        [donnees.demande]      Remplace la demande par défaut.
 * @param {string[]}      [donnees.piecesJointes]
 * @param {string}        [donnees.formuleAppel]
 * @param {string}        [donnees.date]         YYYY-MM-DD (défaut : aujourd'hui).
 * @param {string}        [donnees.lieu]
 * @returns {object} courrier structuré + `texte` rendu
 */
export function genererCourrier(type, donnees = {}) {
  const preset = TYPES_COURRIER[type];
  if (!preset) throw new Error(`Type de courrier inconnu : ${type} (attendu : ${Object.keys(TYPES_COURRIER).join(', ')})`);

  const courrier = {
    type,
    statut: 'projet',
    avertissement: AVERTISSEMENT,
    date: donnees.date || ceJourISO(),
    lieu: donnees.lieu || 'Luxembourg',
    expediteur: bloc(donnees.expediteur) || { nom: '[Expéditeur]' },
    destinataire: bloc(donnees.destinataire) || { nom: '[Destinataire]' },
    references: Array.isArray(donnees.references) ? donnees.references : (donnees.references ? [donnees.references] : []),
    objet: donnees.objet || preset.objet,
    formuleAppel: donnees.formuleAppel || 'Madame, Monsieur,',
    faits: donnees.faits || null,
    demande: donnees.demande || preset.demande,
    piecesJointes: Array.isArray(donnees.piecesJointes) ? donnees.piecesJointes : [],
    formulePolitesse: donnees.formulePolitesse || 'Veuillez agréer, Madame, Monsieur, l\'expression de mes salutations distinguées.',
  };
  courrier.texte = rendreCourrier(courrier);
  return courrier;
}

/** Rend un courrier structuré en texte prêt à relire. */
export function rendreCourrier(c) {
  const lignes = [];
  const adresse = (b) => [b.nom, b.adresse, b.codePostalVille].filter(Boolean);

  lignes.push(...adresse(c.expediteur));
  lignes.push('');
  lignes.push(...adresse(c.destinataire).map((l) => `\t\t\t${l}`));
  lignes.push('');
  lignes.push(`${c.lieu}, le ${c.date}`);
  lignes.push('');
  if (c.references.length) lignes.push(`Réf. : ${c.references.join(' / ')}`);
  lignes.push(`Objet : ${c.objet}`);
  lignes.push('');
  lignes.push(c.formuleAppel);
  lignes.push('');
  if (c.faits) { lignes.push(c.faits); lignes.push(''); }
  lignes.push(c.demande);
  lignes.push('');
  if (c.piecesJointes.length) {
    lignes.push('Pièces jointes :');
    for (const p of c.piecesJointes) lignes.push(`  - ${p}`);
    lignes.push('');
  }
  lignes.push(c.formulePolitesse);
  lignes.push('');
  lignes.push(c.expediteur.nom);
  return lignes.join('\n');
}

/**
 * Pré-remplit un courrier de réponse à partir d'une analyse de document (M3).
 *
 * @param {object} analyse   Sortie de analyserDocument().
 * @param {object} [donnees] Complément (expediteur, type, demande…).
 */
export function courrierDepuisAnalyse(analyse, donnees = {}) {
  const type = donnees.type || 'reponse_administration';
  const references = (analyse.references || []).map((r) => (typeof r === 'string' ? r : r.valeur));
  const faits = [
    `Je fais suite à votre courrier${analyse.type ? ` (${analyse.type.nom})` : ''}${references.length ? ` référencé ${references.join(', ')}` : ''}`
      + `${analyse.periode ? ` concernant la période ${analyse.periode.libelle}` : ''}.`,
    analyse.echeance && analyse.echeance.iso ? `J'ai bien noté l'échéance du ${analyse.echeance.iso}.` : null,
  ].filter(Boolean).join(' ');

  return genererCourrier(type, {
    ...donnees,
    destinataire: donnees.destinataire || (analyse.administration ? { nom: analyse.administration.nom } : undefined),
    references: donnees.references || references,
    objet: donnees.objet || `Réponse à votre courrier${analyse.type ? ` — ${analyse.type.nom}` : ''}`,
    faits: donnees.faits || faits,
  });
}

/**
 * Checklist de préparation d'un rendez-vous (administration, notaire, banque…).
 */
export function checklistRendezVous(type = 'administration') {
  const base = [
    'Pièce d\'identité',
    'Courrier ou convocation reçu',
    'Références du dossier',
    'Justificatifs demandés',
    'Liste des questions à poser',
  ];
  const specifiques = {
    notaire: ['Compromis de vente', 'Justificatif de financement', 'Preuve de l\'affectation à la résidence principale (Bëllegen Akt)'],
    banque: ['Contrat de travail / justificatifs de revenus', 'Relevés bancaires récents'],
    comptable: ['Factures de vente et d\'achat', 'Relevés bancaires de la période', 'Déclarations TVA antérieures'],
  };
  return [...base, ...(specifiques[type] || [])];
}

/**
 * Dossier récapitulatif au format Markdown (le PDF reste une couche
 * optionnelle, via `paperasse pdfs`).
 *
 * @param {object} p { titre, profil, dossiers, documents, courriers, aujourdhui }
 */
export function genererDossierRecap({ titre = 'Dossier administratif', profil, dossiers = [], documents = [], courriers = [], aujourdhui } = {}) {
  const date = aujourdhui || ceJourISO();
  const l = [];
  l.push(`# ${titre}`, '', `_Généré le ${date} — document de travail, à vérifier._`, '');

  if (profil) {
    l.push('## Profil', '');
    for (const [k, v] of Object.entries(profil)) {
      if (v == null || v === '' || (Array.isArray(v) && !v.length) || k === 'type') continue;
      l.push(`- **${k}** : ${Array.isArray(v) ? v.join(', ') : v}`);
    }
    l.push('');
  }

  l.push('## Dossiers / démarches', '');
  if (!dossiers.length) l.push('_Aucun dossier._', '');
  for (const d of dossiers) {
    l.push(`- **${d.typeDemarche || d.categorie}** — statut : ${d.statut}${d.echeance ? `, échéance ${d.echeance}` : ''}`);
    if (d.administration) l.push(`  - Administration : ${d.administration}`);
    if (d.provenance && d.provenance.source) l.push(`  - Source : ${d.provenance.source}`);
  }
  l.push('');

  l.push('## Documents', '');
  if (!documents.length) l.push('_Aucun document._', '');
  for (const doc of documents) {
    l.push(`- ${doc.nom}${doc.typeDocument ? ` (${doc.typeDocument})` : ''}${doc.echeanceDetectee ? ` — échéance ${doc.echeanceDetectee}` : ''}`);
    if (doc.validationHumaineRequise) l.push('  - ⚠ Validation humaine requise');
  }
  l.push('');

  if (courriers.length) {
    l.push('## Courriers (projets)', '');
    for (const c of courriers) l.push(`- ${c.objet} — ${c.statut}`);
    l.push('');
  }

  l.push('---', '', '⚠ Ce dossier est un document de travail. Aucune démarche n\'a été envoyée automatiquement.');
  return l.join('\n');
}
