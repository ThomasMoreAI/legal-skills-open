#!/usr/bin/env node
/**
 * calc.js — Calculs déterministes pour Paperasse Lux.
 *
 * Usage:
 *   node calc.js irc <benefice>
 *   node calc.js icc <benefice> <multiplicateur>
 *   node calc.js if <valeur-unitaire> <total-bilan>
 *   node calc.js if-min <total-bilan>
 *   node calc.js bellegen-akt <prix> <nb-acquereurs> [lux-ville]
 *   node calc.js irpp <revenu-imposable> <classe>
 *   node calc.js tva <ht> <taux>
 *   node calc.js succession-direct <part> <est-bien-lux>
 */

// --- Impôts directs entreprise ---

function calcIRC(benefice) {
  // Barème 2025 (loi du 20 décembre 2024 / paquet fiscal 2025) — taux abaissés.
  // Source : comptable/data/irc-icc-if.json -> irc_impot_revenu_collectivites.tranches_2025
  let irc;
  if (benefice <= 175000) {
    irc = benefice * 0.14; // tranche basse 14 % (avant 2025 : 15 %)
  } else if (benefice <= 200000) {
    // Ramp-up zone : 14 % × 175 000 + 31 % × (R - 175 000)
    irc = 175000 * 0.14 + (benefice - 175000) * 0.31;
  } else {
    irc = benefice * 0.16; // tranche haute 16 % (avant 2025 : 17 %)
  }
  const contributionChomage = irc * 0.07; // majoration 7 % fonds chômage
  return {
    irc,
    contributionChomage,
    total: irc + contributionChomage,
    tauxEffectif: (irc + contributionChomage) / benefice,
  };
}

function calcICC(benefice, multiplicateurCommunal = 2.25) {
  const base = Math.max(0, benefice - 17500);
  const tauxAssiette = 0.03;
  const icc = base * tauxAssiette * multiplicateurCommunal;
  return {
    base,
    tauxEffectif: tauxAssiette * multiplicateurCommunal,
    icc,
  };
}

function calcMinIF(totalBilan) {
  // Barème IF minimum forfaitaire 2025 — strictement aligné sur
  // comptable/data/irc-icc-if.json -> if_impot_fortune.if_minimum_mindest.bareme_2025
  if (totalBilan <= 350000) return 535;
  if (totalBilan <= 2000000) return 1605;
  if (totalBilan <= 10000000) return 5350;
  if (totalBilan <= 15000000) return 10700;
  if (totalBilan <= 20000000) return 16050;
  if (totalBilan <= 30000000) return 21400;
  return 32100;
}

function calcIF(valeurUnitaire, totalBilan) {
  const ifNominal = valeurUnitaire * 0.005; // 0,5 %
  const minIF = calcMinIF(totalBilan);
  return {
    ifNominal,
    minIF,
    ifDu: Math.max(ifNominal, minIF),
  };
}

// --- Notaire ---

function calcBellegenAkt(prix, nbAcquereurs = 1, luxVille = false, primoAccedant = true) {
  const tauxEnreg = luxVille ? 0.06 + 0.03 : 0.06; // 6 % + surtaxe 3 % à Lux-Ville
  const tauxTranscription = 0.01;
  const tauxTotal = tauxEnreg + tauxTranscription;

  const droitsNominaux = prix * tauxTotal;

  let abattementBA = 0;
  if (primoAccedant) {
    // Crédit d'impôt Bëllegen Akt : 40 000 € PAR PERSONNE depuis le 1er oct. 2024
    // (loi du 22 mai 2024). Imputé directement sur les droits dus, plafonné aux droits.
    // Source : notaire/data/droits-enregistrement.json — exemple couple neuf Lux-Ville
    // 800 000 € × 10 % = 80 000 droits ; crédit 2 × 40 000 = 80 000 → 0 € à payer.
    abattementBA = Math.min(droitsNominaux, 40000 * nbAcquereurs);
  }

  const droitsNets = droitsNominaux - abattementBA;

  // Honoraires (estimation dégressive)
  const honoraires = estimHonoraires(prix);
  const tva = honoraires * 0.17;
  const debours = 400;

  const total = droitsNets + honoraires + tva + debours;

  return {
    prix,
    droitsNominaux,
    abattementBA,
    droitsNets,
    honoraires,
    tva,
    debours,
    total,
    ratio: total / prix,
  };
}

function estimHonoraires(prix) {
  // Tarif réglementé (estimation simplifiée, dégressif)
  if (prix <= 100000) return prix * 0.012;
  if (prix <= 300000) return 1200 + (prix - 100000) * 0.009;
  if (prix <= 1000000) return 1200 + 1800 + (prix - 300000) * 0.007;
  return 1200 + 1800 + 4900 + (prix - 1000000) * 0.005;
}

// --- IRPP ---

const BAREME_2025 = [
  [12438, 0],
  [14508, 0.08],
  [16578, 0.09],
  [18648, 0.10],
  [20718, 0.11],
  [22788, 0.12],
  [24939, 0.14],
  [27090, 0.16],
  [29241, 0.18],
  [31392, 0.20],
  [33543, 0.22],
  [35694, 0.24],
  [37845, 0.26],
  [39996, 0.28],
  [42147, 0.30],
  [44298, 0.32],
  [46449, 0.34],
  [48600, 0.36],
  [50751, 0.38],
  [110403, 0.39],
  [165600, 0.40],
  [220788, 0.41],
  [Infinity, 0.42],
];

function impotBareme(revenu) {
  let impot = 0;
  let reste = revenu;
  let prev = 0;
  for (const [seuil, taux] of BAREME_2025) {
    const tranche = Math.min(reste, seuil - prev);
    if (tranche <= 0) break;
    impot += tranche * taux;
    reste -= tranche;
    prev = seuil;
  }
  return impot;
}

function calcIRPP(revenuImposable, classe = 1) {
  let impot;
  if (classe === 2) {
    // Splitting
    impot = impotBareme(revenuImposable / 2) * 2;
  } else {
    // Classe 1 et 1a (1a a un sous-barème — approximation ici)
    impot = impotBareme(revenuImposable);
  }
  const tauxContrib = revenuImposable > (classe === 2 ? 300000 : 150000) ? 0.09 : 0.07;
  const contribChomage = impot * tauxContrib;
  const contribDependance = revenuImposable * 0.014; // approximation
  return {
    impotBareme: impot,
    contribChomage,
    contribDependance,
    total: impot + contribChomage + contribDependance,
    tauxEffectif: (impot + contribChomage + contribDependance) / revenuImposable,
  };
}

// --- TVA ---

function calcTVA(ht, taux) {
  const tva = ht * (taux / 100);
  return { ht, tva, ttc: ht + tva };
}

// --- Succession ligne directe ---

function calcSuccessionDirect(part, biensSituesAuLux = true) {
  // Exonération en ligne directe sur biens lux
  if (biensSituesAuLux) return { droits: 0, exoneration: true };
  return { droits: null, exoneration: false, note: "Vérifier convention internationale + droits du pays de situation" };
}

// --- CLI ---

function main() {
  const [, , cmd, ...args] = process.argv;
  switch (cmd) {
    case "irc":
      console.log(JSON.stringify(calcIRC(+args[0]), null, 2));
      break;
    case "icc":
      console.log(JSON.stringify(calcICC(+args[0], +args[1]), null, 2));
      break;
    case "if": {
      // IF nominal (0,5 % × valeur unitaire) vs IF minimum forfaitaire (selon total bilan)
      // Usage : node calc.js if <valeur-unitaire> <total-bilan>
      const valeurUnitaire = +args[0];
      const totalBilan = args[1] !== undefined ? +args[1] : valeurUnitaire;
      if (args[1] === undefined) {
        console.warn("[avertissement] total-bilan non fourni, on suppose total-bilan = valeur-unitaire (cas d'une société sans dettes).");
      }
      console.log(JSON.stringify(calcIF(valeurUnitaire, totalBilan), null, 2));
      break;
    }
    case "if-min":
      // IF minimum forfaitaire seul, sans IF nominal
      console.log(JSON.stringify({ totalBilan: +args[0], minIF: calcMinIF(+args[0]) }, null, 2));
      break;
    case "bellegen-akt":
      console.log(
        JSON.stringify(
          calcBellegenAkt(+args[0], +args[1], args[2] === "lux-ville", true),
          null,
          2,
        ),
      );
      break;
    case "irpp":
      console.log(JSON.stringify(calcIRPP(+args[0], +args[1]), null, 2));
      break;
    case "tva":
      console.log(JSON.stringify(calcTVA(+args[0], +args[1]), null, 2));
      break;
    case "succession-direct":
      console.log(JSON.stringify(calcSuccessionDirect(+args[0], args[1] !== "false"), null, 2));
      break;
    default:
      console.log(`Usage:
  node calc.js irc <benefice>
  node calc.js icc <benefice> <multiplicateur>          (ex. Lux-Ville: 2.25)
  node calc.js if <valeur-unitaire> <total-bilan>       (IF nominal vs IF minimum)
  node calc.js if-min <total-bilan>                     (IF minimum forfaitaire seul)
  node calc.js bellegen-akt <prix> <nb-acquereurs> [lux-ville]
  node calc.js irpp <revenu-imposable> <classe>         (1 ou 2)
  node calc.js tva <ht> <taux>                          (17, 14, 8, 3)
  node calc.js succession-direct <part> [biens-lux]
`);
      process.exit(1);
  }
}

// Exports pour permettre des tests unitaires depuis test-deterministic-calculations.js
export { calcIRC, calcICC, calcIF, calcMinIF, calcBellegenAkt, calcIRPP, calcTVA, calcSuccessionDirect };

// Exécute le CLI uniquement si le fichier est lancé directement (pas importé)
import { fileURLToPath } from "node:url";
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  main();
}
