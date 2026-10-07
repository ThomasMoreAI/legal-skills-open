#!/usr/bin/env node
/**
 * connaissances.js — CLI de la base de connaissances officielle (Milestone 11).
 *
 * Sous-commandes :
 *   paperasse connaissances rapport
 *   paperasse connaissances chercher --terme TVA
 *   paperasse connaissances citer    --id obl_tva_declaration_mensuelle
 *   paperasse connaissances revalider [--seuil 365]
 *   paperasse connaissances sources
 *
 * Aucune règle n'est affichée sans source.
 */

import {
  chargerSources, baseConnaissances, rechercher, reglesARevalider, citer, verifierSourcesConnues, rapport,
  catalogueEnVigueur, chargerGlossaire, expliquer,
  ficheDeVie, revuesDues, verifierGouvernance, tableauQualite,
  chargerCasQA, casQAParRegle, tableauCouverture, metriquesConnaissance,
  tableauMaturite, detteConnaissance,
} from '../lib/connaissances/index.js';
import { etatEditorial, transitionsAutorisees, historiqueEditorial, ETAPES_EDITORIALES } from '../lib/editorial/index.js';
import { chargerCatalogue, ceJourISO } from '../lib/diagnostic/index.js';
import { chargerEvenements } from '../lib/evenements/index.js';

function arg(nom) { const i = process.argv.indexOf(nom); return i !== -1 ? process.argv[i + 1] : undefined; }
const sous = process.argv[2];
const opts = arg('--seuil') ? { seuilJours: Number(arg('--seuil')) } : {};

switch (sous) {
  case 'rapport': {
    const r = rapport(opts);
    console.log(`Base de connaissances : ${r.total} règle(s)`);
    console.log(`Par niveau de confiance : ${JSON.stringify(r.parNiveau)}`);
    console.log(`À revérifier : ${r.aRevalider} | sans source : ${r.sansSource}`);
    const inconnues = verifierSourcesConnues();
    console.log(`Sources hors registre : ${inconnues.length}`);
    break;
  }
  case 'chercher': {
    const r = rechercher(arg('--terme') || '', opts);
    console.log(`${r.length} résultat(s) pour « ${arg('--terme')} » :\n`);
    for (const e of r) console.log(`  • [${e.categorie}] ${e.titre}\n    Source : ${e.source} (${e.niveauConfiance}, ${e.dateVerification})${e.fraicheur.aRevalider ? ' ⚠ à revérifier' : ''}`);
    break;
  }
  case 'citer': {
    const c = citer(arg('--id'), opts);
    console.log(c.citation);
    break;
  }
  case 'revalider': {
    const r = reglesARevalider(opts);
    console.log(`${r.length} règle(s) à revérifier${arg('--seuil') ? ` (seuil ${arg('--seuil')} j)` : ''} :\n`);
    for (const e of r) console.log(`  ⚠ ${e.titre} — vérifiée le ${e.dateVerification} (${e.fraicheur.joursDepuisVerification} j)`);
    break;
  }
  case 'envigueur': {
    const date = arg('--date') || ceJourISO();
    const { obligations } = chargerCatalogue();
    const enVigueur = catalogueEnVigueur(obligations, date, arg('--juridiction') ? { juridiction: arg('--juridiction') } : {});
    console.log(`Règles en vigueur au ${date}${arg('--juridiction') ? ` (${arg('--juridiction')})` : ''} : ${enVigueur.length}/${obligations.length}\n`);
    for (const o of enVigueur) console.log(`  • ${o.nom}  [v${o.validite ? o.validite.version : '?'}, depuis ${o.validite ? o.validite.validFrom : '?'}]`);
    console.log(`\n⚠ Réponse valable pour les règles en vigueur au ${date}.`);
    break;
  }
  case 'gouvernance': {
    const date = arg('--date') || ceJourISO();
    const { obligations } = chargerCatalogue();
    if (arg('--id')) {
      const o = obligations.find((x) => x.id === arg('--id'));
      if (!o) { console.log(`Règle inconnue : ${arg('--id')}`); break; }
      const f = ficheDeVie(o, { aujourdhui: date });
      console.log(`Fiche de vie — ${f.nom}`);
      console.log(`  Owner : ${f.owner} | statut : ${f.status}`);
      console.log(`  Vérifié le ${f.lastVerified} | prochaine revue ${f.nextReview}${f.revueDue ? ' ⚠ DUE' : ''} (tous les ${f.reviewFrequency})`);
      console.log('  Historique :');
      for (const c of f.changeLog) console.log(`    - ${c.date} : ${c.reason}${c.author ? ` (${c.author})` : ''}`);
      break;
    }
    const ctrl = verifierGouvernance(obligations, { aujourdhui: date });
    const dues = revuesDues(obligations, { aujourdhui: date });
    console.log(`Gouvernance de la connaissance (au ${date}) :`);
    console.log(`  Règles gouvernées : ${obligations.length} | fiches cohérentes : ${ctrl.ok ? 'oui' : 'non (' + ctrl.problemes.length + ')'}`);
    console.log(`  Revues dues : ${dues.length}`);
    for (const f of dues) console.log(`    ⚠ ${f.nom} — revue prévue le ${f.nextReview}`);
    break;
  }
  case 'couverture': {
    const { obligations } = chargerCatalogue();
    const tc = tableauCouverture(obligations, chargerCasQA().cas, { aujourdhui: arg('--date') || ceJourISO() });
    const m = metriquesConnaissance(obligations, chargerCasQA().cas, { aujourdhui: arg('--date') || ceJourISO() });
    console.log(`Coverage Dashboard — ${m.regles} règles, ${m.casQA} cas QA, ${m.domaines} domaines`);
    console.log(`Couverture réglementaire globale : ${m.couvertureReglementaire} % | fraîcheur moyenne : ${m.fraicheurMoyenneJours} j\n`);
    console.log('Domaine'.padEnd(22) + 'Couv.'.padEnd(8) + 'Règles'.padEnd(8) + 'Cas QA'.padEnd(8) + 'Dern. revue');
    for (const d of tc) {
      console.log(String(d.domaine).padEnd(22) + `${d.couverture}%`.padEnd(8) + String(d.regles).padEnd(8) + String(d.casQA).padEnd(8) + (d.derniereRevue || '—') + (d.ageRevueJours != null ? ` (${d.ageRevueJours} j)` : ''));
    }
    break;
  }
  case 'maturite': {
    const { obligations } = chargerCatalogue();
    const tm = tableauMaturite(obligations, chargerCasQA().cas, { aujourdhui: arg('--date') || ceJourISO() });
    console.log('Score de maturité par domaine (0-100) :\n');
    console.log('Domaine'.padEnd(22) + 'Couv.'.padEnd(7) + 'Frais.'.padEnd(8) + 'QA'.padEnd(6) + 'Maturité');
    for (const d of tm) console.log(String(d.domaine).padEnd(22) + `${d.couverture}`.padEnd(7) + `${d.fraicheur}`.padEnd(8) + `${d.qa}`.padEnd(6) + d.maturite);
    break;
  }
  case 'dette': {
    const { obligations } = chargerCatalogue();
    const dette = detteConnaissance(obligations, { cas: chargerCasQA().cas, evenements: chargerEvenements().evenements, aujourdhui: arg('--date') || ceJourISO() });
    console.log(`Dette de connaissance (backlog) — ${dette.total} élément(s) :\n`);
    for (const i of dette.items) {
      console.log(`  [${i.gravite}] ${i.type} : ${i.total}`);
      console.log(`     ${i.elements.slice(0, 8).join(', ')}${i.elements.length > 8 ? '…' : ''}`);
    }
    break;
  }
  case 'editorial': {
    const { obligations } = chargerCatalogue();
    if (arg('--id')) {
      const o = obligations.find((x) => x.id === arg('--id'));
      if (!o) { console.log(`Règle inconnue : ${arg('--id')}`); break; }
      console.log(`${o.nom}\n  Étape éditoriale : ${etatEditorial(o)}`);
      console.log(`  Transitions possibles : ${transitionsAutorisees(etatEditorial(o)).join(', ') || 'aucune (archivée)'}`);
      const hist = historiqueEditorial(o);
      console.log(`  Historique éditorial (${hist.length}) :`);
      for (const h of hist) console.log(`    - ${h.date} → ${h.etape} : ${h.reason}${h.author ? ` (${h.author})` : ''}`);
    } else {
      console.log('Cycle de vie éditorial d\'une règle :');
      console.log('  ' + ETAPES_EDITORIALES.join(' → '));
      console.log('\nUtilisez --id <obligationId> pour l\'étape et l\'historique d\'une règle.');
    }
    break;
  }
  case 'impact-regle': {
    const impactes = casQAParRegle(arg('--id') || '');
    console.log(`Cas QA à réviser si « ${arg('--id')} » change : ${impactes.length}`);
    for (const c of impactes) console.log(`  • ${c.id} [${c.famille || '?'}] — ${c.description}`);
    break;
  }
  case 'qualite': {
    const { obligations } = chargerCatalogue();
    const q = tableauQualite(obligations, { aujourdhui: arg('--date') || ceJourISO() });
    console.log('Trois niveaux de qualité :');
    console.log(`  1. Moteur       : ${q.moteur.mesure} (${q.moteur.reference})`);
    console.log(`  2. Connaissance : ${q.connaissance.regles} règles, ${q.connaissance.versionnees} versionnées, gouvernance ${q.connaissance.gouvernanceComplete ? 'complète' : 'incomplète'}, ${q.connaissance.revuesDues} revue(s) due(s)`);
    console.log(`  3. Réponses     : ${q.reponses.mesure} — ${q.reponses.statut}`);
    break;
  }
  case 'glossaire': {
    if (arg('--terme')) {
      const t = expliquer(arg('--terme'));
      if (!t) { console.log(`Terme inconnu : ${arg('--terme')}`); break; }
      console.log(`${t.sigle} — ${t.terme}\n${t.definition}\nSource : ${t.source}`);
    } else {
      const g = chargerGlossaire();
      console.log(`Glossaire (${g.termes.length} termes) :\n`);
      for (const t of g.termes) console.log(`  ${t.sigle} — ${t.terme}`);
    }
    break;
  }
  case 'sources': {
    const s = chargerSources();
    console.log(`Registre des sources officielles (mis à jour ${s.lastUpdated}) :\n`);
    for (const x of s.sources) console.log(`  • ${x.id} — ${x.name}\n    ${x.url}`);
    break;
  }
  default:
    console.log(`Usage :
  paperasse connaissances rapport
  paperasse connaissances chercher --terme TVA
  paperasse connaissances citer    --id <obligationId>
  paperasse connaissances revalider [--seuil 365]
  paperasse connaissances envigueur [--date YYYY-MM-DD] [--juridiction LU]
  paperasse connaissances gouvernance [--id <obligationId>] [--date YYYY-MM-DD]
  paperasse connaissances editorial [--id <obligationId>]
  paperasse connaissances couverture [--date YYYY-MM-DD]
  paperasse connaissances maturite
  paperasse connaissances dette
  paperasse connaissances impact-regle --id <obligationId>
  paperasse connaissances qualite
  paperasse connaissances glossaire [--terme CCSS]
  paperasse connaissances sources`);
    process.exit(sous ? 1 : 0);
}
