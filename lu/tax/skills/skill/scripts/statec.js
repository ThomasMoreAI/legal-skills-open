#!/usr/bin/env node
import {
  getSSMCourant,
  getSSMJeune,
  derniereTranche,
  indexerSalaire,
  TRANCHES_INDEXATION,
  SSM_HISTORIQUE,
} from '../lib/indice-statec/index.js';

const args = process.argv.slice(2);
const cmd = args[0];

function usage() {
  console.log(`paperasse statec — Indice STATEC + Salaire Social Minimum LU

Usage :
  paperasse statec ssm [--qualifie] [--date YYYY-MM-DD]
  paperasse statec ssm-jeune --tranche 15-17|17-18 [--date YYYY-MM-DD]
  paperasse statec tranches [--depuis YYYY-MM-DD]
  paperasse statec indexer --brut 5000 --depuis 2023-01-01 [--cible YYYY-MM-DD]
  paperasse statec historique
`);
}

function flag(name, def) {
  const i = args.indexOf(`--${name}`);
  if (i === -1) return def;
  return args[i + 1];
}
function bool(name) { return args.includes(`--${name}`); }

try {
  switch (cmd) {
    case 'ssm': {
      const r = getSSMCourant({ qualifie: bool('qualifie'), date: flag('date') });
      console.log(`SSM ${bool('qualifie') ? 'qualifié' : 'non qualifié'} au ${r.dateEntreeVigueur}`);
      console.log(`  Mensuel : ${r.ssmMensuel.toFixed(2)} € (40h/sem)`);
      console.log(`  Horaire : ${r.ssmHoraire.toFixed(4)} €`);
      console.log(`  Source  : ${r.source}`);
      break;
    }
    case 'ssm-jeune': {
      const r = getSSMJeune({ tranche: flag('tranche'), date: flag('date') });
      console.log(`SSM jeune travailleur (${r.tranche} ans) au ${r.dateEntreeVigueur}`);
      console.log(`  Ratio   : ${(r.ratio * 100).toFixed(0)} % du SSM non-qualifié`);
      console.log(`  Mensuel : ${r.ssmMensuel.toFixed(2)} €`);
      console.log(`  Horaire : ${r.ssmHoraire.toFixed(4)} €`);
      console.log(`  Source  : ${r.source}`);
      break;
    }
    case 'tranches': {
      const depuis = flag('depuis');
      const r = derniereTranche();
      if (depuis) {
        const n = r.nbTranchesDepuis(depuis);
        console.log(`${n} tranche(s) d'indexation déclenchée(s) depuis ${depuis} :`);
      } else {
        console.log(`Tranches d'indexation déclenchées (à ce jour) :`);
      }
      const liste = depuis
        ? TRANCHES_INDEXATION.filter((t) => t.date > depuis)
        : TRANCHES_INDEXATION;
      for (const t of liste) console.log(`  ${t.date} — ${t.source}`);
      console.log(`\nDernière tranche : ${r.derniere?.date || '(aucune)'}`);
      break;
    }
    case 'indexer': {
      const brut = parseFloat(flag('brut'));
      const depuis = flag('depuis');
      const cible = flag('cible');
      const r = indexerSalaire({ brutReference: brut, dateReference: depuis, dateCible: cible });
      console.log(`Indexation de ${brut.toFixed(2)} € (référence ${depuis}) :`);
      console.log(`  → Brut indexé : ${r.brutIndexe.toFixed(2)} €`);
      console.log(`  → ${r.nbTranches} tranche(s) appliquée(s) (facteur ${r.facteur})`);
      for (const t of r.tranchesAppliquees) console.log(`     • ${t.date} (+2,5 %)`);
      break;
    }
    case 'historique': {
      console.log(`SSM — historique des revalorisations :\n`);
      console.log(`Date         Non qualifié   Qualifié      Source`);
      for (const s of SSM_HISTORIQUE) {
        console.log(
          `${s.date}   ${s.nonQualifie.toFixed(2).padStart(10)} €   ${s.qualifie
            .toFixed(2)
            .padStart(8)} €   ${s.source}`,
        );
      }
      break;
    }
    default:
      usage();
      process.exit(cmd ? 1 : 0);
  }
} catch (e) {
  console.error(`Erreur : ${e.message}`);
  process.exit(1);
}
