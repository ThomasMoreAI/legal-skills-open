/**
 * lib/conversation — Intelligence conversationnelle (Milestone 14).
 *
 * Orchestrateur qui, à partir d'une demande en langage naturel, identifie
 * l'intention, consulte le profil, recherche les obligations applicables,
 * demande les informations manquantes, répond AVEC ses sources, propose une
 * checklist et une action.
 *
 * GARDE-FOU : l'assistant ne prétend JAMAIS avoir réalisé une démarche. Toute
 * réponse rappelle qu'il s'agit d'une aide et que rien n'a été envoyé.
 *
 * Aucune dépendance externe.
 */

import { chargerCatalogue } from '../diagnostic/index.js';
import { diagnostiquer } from '../diagnostic/engine.js';
import { prochaineQuestion } from '../diagnostic/questionnaire.js';
import { analyserDocument } from '../documents/index.js';
import { parcoursEntreprise } from '../entreprise/index.js';
import { parcoursParticulier, analyseFrontalier } from '../particulier/index.js';
import { parcoursInstallation } from '../residence/index.js';
import { identifierEvenement, resoudreEvenement } from '../evenements/index.js';
import { ceJourISO } from '../diagnostic/provenance.js';

const DISCLAIMER = 'Je vous aide à comprendre et à préparer vos démarches. Je n\'ai effectué aucune démarche ni envoyé aucun document : toute action nécessite votre validation.';

/** Intentions reconnues et leurs marqueurs lexicaux. */
export const INTENTIONS = [
  { id: 'analyser_courrier', motsCles: ['reçu cette lettre', 'reçu un courrier', 'cette lettre', 'ce courrier', 'que dois-je faire de', 'lettre de', 'mise en demeure'] },
  { id: 'tva', motsCles: ['tva', 'déclaration de tva', 'déclarer la tva', 'assujetti'] },
  { id: 'creer_societe', motsCles: ['créer ma société', 'créer une société', 'monter ma boîte', 'créer mon entreprise', 'lancer mon activité', 'devenir indépendant'] },
  { id: 'frontalier', motsCles: ['frontalier', 'télétravail', 'je travaille au luxembourg', 'je réside en france', 'je réside en belgique', 'je réside en allemagne'] },
  { id: 'achat_immobilier', motsCles: ['acheté un appartement', 'acheter un appartement', 'acheté une maison', 'acheter une maison', 'acheter un bien', 'acquisition immobilière', 'devenir propriétaire'] },
  { id: 'comptes_non_deposes', motsCles: ['pas déposé ses comptes', 'comptes annuels', 'déposer les comptes', 'dépôt des comptes'] },
  { id: 'cessation', motsCles: ['arrêter mon activité', 'cesser mon activité', 'fermer ma société', 'cessation', 'liquidation'] },
  { id: 'declaration_fiscale', motsCles: ['déclaration fiscale', 'déclaration d\'impôt', 'modèle 100', 'ma déclaration'] },
  { id: 'installation', motsCles: ['je m\'installe', 'je viens d\'arriver', 'nouvel arrivant', 'je déménage au luxembourg'] },
  { id: 'diagnostic', motsCles: ['que dois-je faire', 'mes obligations', 'quelles démarches', 'suis-je en règle'] },
];

/** Identifie l'intention principale d'un texte (score par mots-clés). */
export function classifierIntention(texte) {
  const t = String(texte || '').toLowerCase();
  let meilleur = null;
  for (const intent of INTENTIONS) {
    let score = 0;
    for (const mc of intent.motsCles) if (t.includes(mc)) score++;
    if (score > 0 && (!meilleur || score > meilleur.score)) meilleur = { id: intent.id, score };
  }
  return meilleur ? meilleur.id : 'diagnostic';
}

function citation(entree) {
  const ob = entree.obligation;
  const p = ob.provenance || {};
  return `${ob.nom} — ${ob.autoriteCompetente || 'autorité à préciser'}. Source : ${p.source} (${p.niveauConfiance}, vérifié ${p.dateVerification}).`;
}

/**
 * Répond à une demande en langage naturel.
 *
 * @param {string} texte
 * @param {object} [contexte] { profil, texteDocument, aujourdhui, catalogue }
 * @returns {object} réponse structurée
 */
export function repondre(texte, contexte = {}) {
  const aujourdhui = contexte.aujourdhui || ceJourISO();
  const profil = contexte.profil || {};
  const catalogue = contexte.catalogue || chargerCatalogue().obligations;
  const intention = classifierIntention(texte);

  const reponse = {
    intention,
    comprehension: null,
    obligations: [],
    sources: [],
    checklist: [],
    prochaineQuestion: null,
    action: null,
    evenementVie: null,
    disclaimer: DISCLAIMER,
  };

  // Couche « événement de vie » : si un événement est identifié, on attache sa
  // chaîne (conséquences → administrations → obligations → checklist) — vue
  // transverse sur le graphe, en plus de la réponse par intention.
  const idEvenement = identifierEvenement(texte);
  if (idEvenement) {
    const c = resoudreEvenement(idEvenement, { aujourdhui, catalogue });
    reponse.evenementVie = {
      id: c.evenement.id,
      nom: c.evenement.nom,
      administrations: c.administrations.map((a) => a.nom),
      obligations: c.obligations.map((o) => o.nom).filter(Boolean),
      checklist: c.checklist,
      source: c.source,
    };
  }

  const remonterDiagnostic = (cible, libelle) => {
    const { applicables } = diagnostiquer(cible, catalogue, { aujourdhui });
    reponse.comprehension = libelle;
    reponse.obligations = applicables.map((e) => ({ nom: e.obligation.nom, echeance: e.echeance, administration: e.obligation.autoriteCompetente }));
    reponse.sources = applicables.map(citation);
    reponse.checklist = applicables.flatMap((e) => e.obligation.piecesRequises || []);
    const q = prochaineQuestion(cible, catalogue);
    reponse.prochaineQuestion = q ? q.label : null;
  };

  switch (intention) {
    case 'analyser_courrier': {
      if (contexte.texteDocument) {
        const a = analyserDocument(contexte.texteDocument, { aujourdhui });
        reponse.comprehension = a.resume;
        reponse.checklist = a.checklist;
        reponse.sources = a.administration ? [a.administration.nom] : [];
        reponse.action = a.action ? `Préparer : ${a.action}` : 'Analyser le document et préparer une réponse';
        if (a.avertissement) reponse.avertissement = a.avertissement;
      } else {
        reponse.comprehension = 'Vous évoquez un courrier administratif.';
        reponse.action = 'Importez le texte du courrier pour une analyse détaillée.';
        reponse.prochaineQuestion = 'Pouvez-vous coller le texte du courrier reçu ?';
      }
      break;
    }
    case 'frontalier': {
      reponse.comprehension = 'Vous êtes (ou envisagez d\'être) frontalier travaillant au Luxembourg.';
      if (profil.paysResidence && ['FR', 'BE', 'DE'].includes(profil.paysResidence)) {
        const af = analyseFrontalier({ paysResidence: profil.paysResidence, joursHorsLU: profil.joursHorsLU || 0, salaireBrutMensuel: profil.salaireBrutMensuel });
        reponse.action = af.alerte || `Sous le seuil de ${af.seuilJours} jours : situation standard.`;
        reponse.sources = [af.provenance.source];
      } else {
        reponse.prochaineQuestion = 'Dans quel pays résidez-vous (FR, BE ou DE) et combien de jours par an travaillez-vous hors du Luxembourg ?';
      }
      remonterDiagnostic({ ...profil, frontalier: true }, reponse.comprehension);
      break;
    }
    case 'creer_societe': {
      remonterDiagnostic({ ...profil, statut: 'actif', formeJuridique: profil.formeJuridique || 'SARL' }, 'Vous souhaitez créer une société / démarrer une activité.');
      reponse.action = 'Suivre le parcours de création (autorisation d\'établissement → RCS → RBE → TVA → CCSS).';
      break;
    }
    case 'comptes_non_deposes': {
      const p = parcoursEntreprise({ ...profil, statut: 'actif' }, catalogue, { aujourdhui, exerciceFin: profil.exerciceFin });
      reponse.comprehension = 'Votre société n\'a pas déposé ses comptes annuels.';
      reponse.obligations = (p.parPhase.vie || []).map((i) => ({ nom: i.nom, echeance: i.echeance, administration: i.administration }));
      reponse.sources = (p.parPhase.vie || []).map((i) => i.source).filter(Boolean);
      reponse.action = 'Préparer et déposer les comptes annuels au RCS (voir échéance) ; régulariser sans tarder.';
      break;
    }
    case 'cessation': {
      remonterDiagnostic({ ...profil, statut: profil.statut && profil.statut !== 'actif' ? profil.statut : 'cessation' }, 'Vous souhaitez arrêter votre activité.');
      reponse.action = 'Suivre l\'enchaînement de cessation : clôture TVA, radiation CCSS, réquisition de radiation RCS.';
      break;
    }
    case 'achat_immobilier': {
      reponse.comprehension = 'Vous venez d\'acheter (ou envisagez d\'acheter) un bien immobilier.';
      reponse.checklist = ['Compromis de vente', 'Financement / subvention d\'intérêt', 'Acte notarié + crédit Bëllegen Akt', 'Assurance habitation', 'Changement d\'adresse'];
      reponse.action = 'Estimer les frais d\'acquisition (droits + Bëllegen Akt) et souscrire l\'assurance.';
      reponse.sources = ['https://guichet.public.lu/fr/citoyens/logement/achat-immobilier.html'];
      break;
    }
    case 'installation': {
      const p = parcoursInstallation(profil, { aujourdhui });
      reponse.comprehension = 'Vous vous installez au Luxembourg.';
      reponse.checklist = p.chronologie.map((e) => e.titre);
      reponse.sources = [...new Set(p.chronologie.map((e) => e.source))];
      reponse.action = 'Suivre le parcours d\'installation chronologique.';
      if (p.avertissement) reponse.avertissement = p.avertissement;
      break;
    }
    case 'declaration_fiscale': {
      const p = parcoursParticulier(profil, catalogue, { aujourdhui });
      reponse.comprehension = `Votre classe d'impôt estimée : ${p.classeImpot.classe}. ${p.classeImpot.raison}`;
      reponse.obligations = (p.parDomaine.fiscalite || []).map((i) => ({ nom: i.nom, echeance: i.echeance, administration: i.administration }));
      reponse.sources = (p.parDomaine.fiscalite || []).map((i) => i.source).filter(Boolean);
      reponse.action = 'Rassembler les pièces de la déclaration (certificat de rémunération, déductions).';
      break;
    }
    case 'tva':
    case 'diagnostic':
    default: {
      remonterDiagnostic(profil, intention === 'tva' ? 'Vous vous interrogez sur vos obligations de TVA.' : 'Vous voulez connaître vos obligations administratives.');
      if (intention === 'tva') {
        reponse.obligations = reponse.obligations.filter((o) => /tva/i.test(o.nom));
      }
      break;
    }
  }

  return reponse;
}
