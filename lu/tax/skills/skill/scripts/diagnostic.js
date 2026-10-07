#!/usr/bin/env node
/**
 * diagnostic.js — CLI du moteur de diagnostic administratif (Milestone 1).
 *
 * Sous-commandes :
 *   paperasse diagnostic obligations                 Liste le catalogue sourcé.
 *   paperasse diagnostic profil --json '<...>'        Diagnostique un profil utilisateur.
 *   paperasse diagnostic societe --json '<...>'       Diagnostique un profil société.
 *
 * Le JSON passé décrit le profil (mêmes clés que creerProfilUtilisateur /
 * creerProfilSociete). En l'absence de --json, un exemple société est utilisé.
 *
 * Ne déclenche aucune action externe : lecture seule + affichage.
 */

import {
  chargerCatalogue,
  creerProfilUtilisateur,
  creerProfilSociete,
  diagnostiquer,
  dossierDepuisObligation,
  evaluerFraicheur,
  ceJourISO,
  prochaineQuestion,
  questionsRestantes,
  appliquerReponse,
  construireTableauDeBord,
} from '../lib/diagnostic/index.js';
import { analyserDocument } from '../lib/documents/index.js';
import { traduire } from '../lib/i18n/index.js';
import { readFileSync } from 'node:fs';

function arg(nom) {
  const i = process.argv.indexOf(nom);
  return i !== -1 ? process.argv[i + 1] : undefined;
}

const sousCommande = process.argv[2];
const aujourdhui = arg('--date') || ceJourISO();

function afficherObligation(entree, indent = '  ') {
  const { obligation: ob, raisons, echeance } = entree;
  const fr = evaluerFraicheur(ob.provenance, { aujourdhui });
  console.log(`${indent}• ${ob.nom}  [${ob.categorie}]`);
  if (echeance) console.log(`${indent}  Échéance : ${echeance}`);
  if (raisons.length) console.log(`${indent}  Pourquoi : ${raisons.join(' ; ')}`);
  console.log(`${indent}  Autorité : ${ob.autoriteCompetente || '—'}`);
  console.log(`${indent}  Source   : ${ob.provenance.source} (vérifié le ${ob.provenance.dateVerification}, ${ob.provenance.niveauConfiance})`);
  if (fr.aRevalider) console.log(`${indent}  ⚠ ${fr.message}`);
}

function diagnostic(cible, type) {
  const { obligations, as_of } = chargerCatalogue();
  console.log(`\nCatalogue d'obligations : ${obligations.length} entrée(s), as_of ${as_of}\n`);
  const { applicables, aClarifier, nonApplicables } = diagnostiquer(cible, obligations, { aujourdhui });

  console.log(`=== Obligatoire / à faire (${applicables.length}) ===`);
  for (const e of applicables) afficherObligation(e);

  if (aClarifier.length) {
    console.log(`\n=== Informations manquantes (${aClarifier.length}) ===`);
    for (const e of aClarifier) {
      console.log(`  • ${e.obligation.nom} — manque : ${e.manquantes.join(', ')}`);
    }
  }

  console.log(`\n=== Non applicable (${nonApplicables.length}) ===`);
  for (const e of nonApplicables) console.log(`  • ${e.obligation.nom}`);

  // Dossiers générés (aperçu) — aucun n'est envoyé, tout reste local.
  console.log(`\n=== Dossiers générés (${applicables.length}) ===`);
  for (const e of applicables) {
    const d = dossierDepuisObligation(e, { [type === 'societe' ? 'societeId' : 'profilId']: cible.id || 'local', aujourdhui });
    console.log(`  • [${d.priorite}] ${d.typeDemarche} → statut ${d.statut}`);
  }
}

switch (sousCommande) {
  case 'obligations': {
    const { obligations, as_of } = chargerCatalogue();
    console.log(`Catalogue d'obligations (as_of ${as_of}) — ${obligations.length} entrée(s) :\n`);
    for (const ob of obligations) afficherObligation({ obligation: ob, raisons: [], echeance: null });
    break;
  }
  case 'profil': {
    const p = arg('--json') ? creerProfilUtilisateur(JSON.parse(arg('--json'))) : creerProfilUtilisateur({ statutProfessionnel: 'independant', paysResidence: 'LU', dateArriveeLux: '2026-01-15' });
    diagnostic(p, 'profil');
    break;
  }
  case 'societe': {
    const c = arg('--json') ? creerProfilSociete(JSON.parse(arg('--json'))) : creerProfilSociete({ nom: 'Exemple SARL-S', regimeTVA: 'normal', frequenceTVA: 'mensuelle', statut: 'actif' });
    diagnostic(c, 'societe');
    break;
  }
  case 'questionnaire': {
    // « Que dois-je faire administrativement ? » — parcours de questions restantes
    // à partir d'une situation partielle (--json), sans rien demander d'inutile.
    const { obligations } = chargerCatalogue();
    const situation = arg('--json') ? JSON.parse(arg('--json')) : {};
    const restantes = questionsRestantes(situation, obligations);
    const suivante = prochaineQuestion(situation, obligations);
    if (!suivante) {
      console.log('Diagnostic complet : aucune question supplémentaire nécessaire.\n');
    } else {
      console.log(`Prochaine question (conditionne ${suivante.gated} obligation(s)) :`);
      console.log(`  › ${suivante.label}`);
      if (suivante.options) console.log(`    Réponses possibles : ${suivante.options.join(', ')}`);
      if (suivante.aide) console.log(`    Aide : ${suivante.aide}`);
    }
    if (restantes.length) {
      console.log(`\nQuestions restantes (${restantes.length}) :`);
      for (const q of restantes) console.log(`  • [${q.gated}] ${q.champ} — ${q.label}`);
    }
    console.log('\nComplétez la situation puis relancez, ex :');
    console.log(`  paperasse diagnostic dashboard --json '{"regimeTVA":"normal","frequenceTVA":"mensuelle","statut":"actif"}'`);
    break;
  }
  case 'document': {
    // Analyse d'un courrier officiel à partir de son TEXTE (fichier .txt).
    // L'extraction PDF/OCR sera une couche optionnelle ultérieure.
    const fichier = arg('--file');
    if (!fichier) { console.error('Usage : paperasse diagnostic document --file courrier.txt'); process.exit(1); }
    const texte = readFileSync(fichier, 'utf8');
    const a = analyserDocument(texte, { nom: fichier.split('/').pop(), aujourdhui });
    console.log(`\n=== Analyse : ${a.nom} ===\n`);
    if (a.avertissement) console.log(`⚠ ${a.avertissement}\n`);
    console.log(`Ce document signifie : ${a.resume}\n`);
    console.log(`Émetteur   : ${a.administration ? a.administration.nom : 'non identifié'}`);
    console.log(`Type       : ${a.type ? a.type.nom : 'non identifié'}`);
    console.log(`Période    : ${a.periode ? a.periode.libelle : '—'}`);
    console.log(`Échéance   : ${a.echeance.iso || (a.echeance.relatif ? a.echeance.relatif + ' (à confirmer)' : '—')}`);
    console.log(`Action     : ${a.action || '—'}`);
    console.log(`Références  : ${a.references.map((r) => r.valeur).join(', ') || '—'}`);
    console.log(`Montants   : ${a.montants.map((m) => m.brut).join(', ') || '—'}`);
    console.log(`Risques    : ${a.consequences.join(', ') || '—'}`);
    console.log(`Confiance  : ${a.niveauConfiance}${a.incertitudes.length ? ` (${a.incertitudes.join(', ')})` : ''}`);
    console.log(`\nChecklist :`);
    for (const c of a.checklist) console.log(`  ☐ ${c}`);
    if (a.reponseProposee) {
      console.log(`\nProjet de réponse (${a.reponseProposee.avertissement}) :`);
      console.log(`  Objet : ${a.reponseProposee.objet}`);
      console.log(a.reponseProposee.corps.split('\n\n').map((l) => '  ' + l).join('\n'));
    }
    break;
  }
  case 'dashboard': {
    const { obligations, as_of } = chargerCatalogue();
    const situation = arg('--json') ? JSON.parse(arg('--json')) : {};
    const { colonnes, compteurs } = construireTableauDeBord(situation, obligations, { aujourdhui });
    const langue = arg('--langue') || 'fr';
    console.log(`\nTableau de bord des obligations (catalogue as_of ${as_of})\n`);
    const ordre = ['obligatoire_maintenant', 'a_faire_prochainement', 'a_surveiller', 'informations_manquantes', 'non_applicable'];
    const titres = Object.fromEntries(ordre.map((c) => [c, traduire('colonnes', c, langue).toUpperCase()]));
    for (const [cle, titre] of Object.entries(titres)) {
      const items = colonnes[cle];
      console.log(`=== ${titre} (${compteurs[cle]}) ===`);
      for (const c of items) {
        console.log(`  • ${c.nom}${c.echeance ? `  ⏱ ${c.echeance}` : ''}`);
        if (c.raison) console.log(`    Pourquoi : ${c.raison}`);
        if (c.administration) console.log(`    Autorité : ${c.administration}`);
        if (c.risque) console.log(`    Risque : ${c.risque}`);
        if (c.manquantes) console.log(`    À renseigner : ${c.manquantes.join(', ')}`);
        if (c.source && c.source.url) {
          console.log(`    Source : ${c.source.url} (${c.source.niveauConfiance}, vérifié ${c.source.dateVerification})`);
          if (c.source.aRevalider) console.log('    ⚠ Cette information doit être revérifiée avant utilisation.');
        }
        if (c.actions) console.log(`    Actions : ${c.actions.join(' | ')}`);
      }
      console.log('');
    }
    break;
  }
  default:
    console.log(`Usage :
  paperasse diagnostic obligations              Liste le catalogue sourcé
  paperasse diagnostic questionnaire [--json '{...}']  Prochaine question utile
  paperasse diagnostic dashboard     [--json '{...}']  Tableau de bord (5 colonnes)
  paperasse diagnostic document      --file c.txt      Analyse un courrier officiel
  paperasse diagnostic profil        [--json '{...}']  Diagnostique un particulier
  paperasse diagnostic societe       [--json '{...}']  Diagnostique une société
  Option commune : --date YYYY-MM-DD (échéances déterministes)`);
    process.exit(sousCommande ? 1 : 0);
}
