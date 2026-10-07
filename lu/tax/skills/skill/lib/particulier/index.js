/**
 * lib/particulier — Particuliers, salariés & frontaliers (Milestone 6).
 *
 * Assistant des démarches fiscales et sociales personnelles. Regroupe les
 * obligations d'un particulier par domaine (fiscalité, famille, frontalier,
 * salarié) et réutilise les calculateurs existants :
 *   - lib/rts        : retenue à la source, net mensuel, classes 1/1a/2 ;
 *   - lib/frontaliers: net réel frontalier FR/BE/DE, seuils de jours.
 *
 * Le module adapte les démarches au pays de résidence et signale l'impact des
 * changements de situation familiale. Aucune action externe déclenchée.
 *
 * Aucune dépendance externe.
 */

import { diagnostiquer } from '../diagnostic/engine.js';
import { ceJourISO } from '../diagnostic/provenance.js';
import { calculerRTS } from '../rts/index.js';
import { calculerNetFrontalier, SEUIL_JOURS_FRONTALIER } from '../frontaliers/index.js';

/** Domaines de démarches personnelles, dans un ordre d'affichage naturel. */
export const DOMAINES = ['fiscalite', 'salarie', 'frontalier', 'famille', 'autre'];

const CATEGORIE_VERS_DOMAINE = {
  fiscalite_personnelle: 'fiscalite',
  fiscalite: 'fiscalite',
  salarie: 'salarie',
  frontalier: 'frontalier',
  famille: 'famille',
  social: 'famille',
  residence: 'autre',
};

export function domainePourCategorie(categorie) {
  return CATEGORIE_VERS_DOMAINE[categorie] || 'autre';
}

const SOURCE_CLASSE = 'https://guichet.public.lu/fr/citoyens/impots-taxes/activite-salariee-resident/fixation-imposition/classe-impot.html';

/**
 * Détermine la classe d'impôt luxembourgeoise à partir de la situation
 * familiale (règles simplifiées 2025). Toujours tracé et à valider.
 *
 * @param {object} profil { situationFamiliale, nombreEnfants }
 * @returns {{classe: '1'|'1a'|'2', raison, provenance}}
 */
export function determinerClasseImpot(profil = {}) {
  const { situationFamiliale, nombreEnfants = 0 } = profil;
  let classe = '1';
  let raison = 'Classe 1 par défaut (célibataire sans enfant).';
  if (situationFamiliale === 'marie' || situationFamiliale === 'partenariat') {
    classe = '2';
    raison = 'Classe 2 : imposition collective des conjoints/partenaires (splitting).';
  } else if (situationFamiliale === 'veuf') {
    classe = '1a';
    raison = 'Classe 1a : maintien transitoire (3 ans) après le décès du conjoint.';
  } else if (nombreEnfants > 0 && (situationFamiliale === 'celibataire' || situationFamiliale === 'divorce' || situationFamiliale === 'separe')) {
    classe = '1a';
    raison = 'Classe 1a : parent isolé avec enfant à charge.';
  }
  return {
    classe,
    raison,
    provenance: {
      source: SOURCE_CLASSE,
      dateVerification: '2026-06-15',
      niveauConfiance: 'derive',
      note: 'Règles simplifiées ; l\'imposition collective sur option et les cas transitoires doivent être vérifiés auprès de l\'ACD.',
    },
  };
}

/**
 * Parcours des démarches personnelles, regroupées par domaine et triées
 * chronologiquement. Enrichit avec la classe d'impôt déduite.
 *
 * @param {object} profil       ProfilUtilisateur ou champs équivalents.
 * @param {object[]} catalogue  Obligations sourcées.
 * @param {object} [opts]       { aujourdhui, documentsFournis }
 */
export function parcoursParticulier(profil, catalogue, opts = {}) {
  const aujourdhui = opts.aujourdhui || ceJourISO();
  const { applicables, aClarifier } = diagnostiquer(profil, catalogue, { aujourdhui });

  const items = applicables.map((e) => ({
    domaine: domainePourCategorie(e.obligation.categorie),
    obligationId: e.obligation.id,
    nom: e.obligation.nom,
    categorie: e.obligation.categorie,
    administration: e.obligation.autoriteCompetente,
    echeance: e.echeance,
    raisons: e.raisons,
    source: e.obligation.provenance ? e.obligation.provenance.source : null,
  }));

  const compareEcheance = (a, b) => {
    if (!a.echeance && !b.echeance) return 0;
    if (!a.echeance) return 1;
    if (!b.echeance) return -1;
    return a.echeance.localeCompare(b.echeance);
  };

  const parDomaine = {};
  for (const d of DOMAINES) {
    const liste = items.filter((i) => i.domaine === d).sort(compareEcheance);
    if (liste.length) parDomaine[d] = liste;
  }

  return {
    classeImpot: determinerClasseImpot(profil),
    parDomaine,
    chronologie: [...items].sort(compareEcheance),
    aClarifier,
  };
}

/**
 * Analyse frontalière : adapte au pays de résidence, calcule le net réel
 * (réutilise lib/frontaliers) et surveille le seuil de jours de télétravail /
 * déplacement hors Luxembourg.
 *
 * @param {object} p
 * @param {'FR'|'BE'|'DE'} p.paysResidence
 * @param {number} [p.salaireBrutMensuel]
 * @param {'1'|'1a'|'2'} [p.classe]
 * @param {number} [p.joursHorsLU]
 */
export function analyseFrontalier({ paysResidence, salaireBrutMensuel, classe = '1', joursHorsLU = 0 } = {}) {
  const seuil = SEUIL_JOURS_FRONTALIER[paysResidence];
  if (!seuil) throw new Error(`Pays de résidence non pris en charge : ${paysResidence} (attendu FR/BE/DE)`);
  const depassementSeuil = joursHorsLU > seuil.actuel;
  let net = null;
  if (Number.isFinite(salaireBrutMensuel)) {
    const r = calculerNetFrontalier({ salaireBrutMensuel, paysResidence, classe, joursHorsLU });
    net = { netLuMensuel: r.netLuMensuel, retenueLuMensuel: r.retenueLuMensuel, netFinalMensuel: r.netFinalMensuel ?? r.netApresResidenceMensuel ?? r.netLuMensuel };
  }
  return {
    paysResidence,
    seuilJours: seuil.actuel,
    joursHorsLU,
    depassementSeuil,
    alerte: depassementSeuil
      ? `Seuil de ${seuil.actuel} jours dépassé (${joursHorsLU}) : risque d'imposition partielle dans le pays de résidence et/ou de bascule d'affiliation sécurité sociale.`
      : null,
    net,
    provenance: {
      source: 'https://guichet.public.lu/fr/citoyens/impots-taxes/activite-salariee-non-resident.html',
      dateVerification: '2026-06-15',
      niveauConfiance: 'derive',
      note: `Seuil fiscal ${seuil.actuel} jours (${seuil.sourceActuel}). Seuil sécurité sociale distinct (< 25 % du temps dans le pays de résidence).`,
    },
  };
}

/**
 * Lecture / contrôle d'une fiche de paie : recalcule le net mensuel via lib/rts
 * (calcul traçable) et le compare au net affiché.
 *
 * @param {object} p { salaireBrutMensuel, classe, netAffiche, deductionsAnnuelles }
 */
export function analyseFichePaie({ salaireBrutMensuel, classe = '1', netAffiche, deductionsAnnuelles = 0 } = {}) {
  const r = calculerRTS({ salaireBrutMensuel, classe, deductionsAnnuelles });
  const netRecalcule = r.netMensuel;
  const anomalies = [];
  if (Number.isFinite(netAffiche)) {
    const ecart = Math.round((netAffiche - netRecalcule) * 100) / 100;
    if (Math.abs(ecart) > 1) {
      anomalies.push({
        code: 'net_incoherent',
        gravite: 'moyenne',
        message: `Net affiché (${netAffiche}) ≠ net recalculé (${netRecalcule}), écart ${ecart} €.`,
      });
    }
  }
  return {
    netRecalcule,
    retenueMensuelle: r.retenueMensuelle ?? r.irppMensuel ?? null,
    coherent: anomalies.length === 0,
    anomalies,
    details: r,
    provenance: {
      source: 'https://impotsdirects.public.lu',
      dateVerification: '2026-06-15',
      niveauConfiance: 'derive',
      note: 'Recalcul indicatif (barème IRPP 2025 + cotisations) ; les avantages en nature et primes ne sont pas modélisés.',
    },
  };
}
