#!/usr/bin/env node
/**
 * frontalier.js — CLI : net réel d'un frontalier FR/BE/DE travaillant au LU.
 *
 * Usage :
 *   paperasse frontalier --brut 5000 --pays FR --classe 1
 *   paperasse frontalier --brut 6500 --pays BE --classe 2 --commune-be 0.08
 *   paperasse frontalier --brut 4500 --pays DE --classe 1a --jours-hors-lu 40
 */

import { calculerNetFrontalier } from '../lib/frontaliers/index.js';

const args = process.argv.slice(2);
function arg(name, def) {
  const i = args.indexOf('--' + name);
  if (i === -1) return def;
  const v = args[i + 1];
  if (v === undefined || v.startsWith('--')) return true;
  return v;
}
function flag(n) { return args.includes('--' + n); }

if (args.length === 0 || flag('help')) {
  console.error(`Usage : paperasse frontalier --brut <€> --pays <FR|BE|DE> --classe <1|1a|2> [options]

Options :
  --brut <€>           Salaire brut mensuel LU (obligatoire)
  --pays <FR|BE|DE>    Pays de résidence (obligatoire)
  --classe <c>         Classe d'impôt LU : 1, 1a ou 2 (obligatoire)
  --no-cis             Désactive le crédit d'impôt salarié LU
  --cim                Active le crédit d'impôt monoparental LU
  --commune-be <taux>  Taux des additionnels communaux BE (défaut : 0,075)
  --jours-hors-lu <n>  Jours travaillés hors LU sur l'année (défaut : 0)

Exemples :
  paperasse frontalier --brut 5000 --pays FR --classe 1
  paperasse frontalier --brut 6500 --pays BE --classe 2 --commune-be 0.08
  paperasse frontalier --brut 4500 --pays DE --classe 1a --jours-hors-lu 40
`);
  process.exit(args.length === 0 ? 1 : 0);
}

try {
  const input = {
    salaireBrutMensuel: Number(arg('brut')),
    paysResidence: String(arg('pays')).toUpperCase(),
    classe: String(arg('classe')),
    cisActif: !flag('no-cis'),
    cimActif: flag('cim'),
  };
  const tc = arg('commune-be');
  if (tc !== undefined) input.tauxCommunalBE = Number(tc);
  const jh = arg('jours-hors-lu');
  if (jh !== undefined) input.joursHorsLU = Number(jh);

  const r = calculerNetFrontalier(input);
  const eur = (n) => n.toLocaleString('fr-LU', { style: 'currency', currency: 'EUR' });

  console.log(`
=== Net frontalier ${r.paysResidence} → LU 2025 ===
  Salaire brut mensuel       : ${eur(r.salaireBrutMensuel)}
  Classe d'impôt LU          : ${r.classe}

  --- Côté Luxembourg ---
  Retenue LU mensuelle       : ${eur(r.retenueLuMensuel)}
    dont CSSS                : ${eur(r.detailRTS.csss.total)}
    dont IRPP (après cred.)  : ${eur(r.detailRTS.irppMensuel)}
    dont dépendance          : ${eur(r.detailRTS.contribDependance)}
  Net LU mensuel             : ${eur(r.netLuMensuel)}

  --- Côté ${r.paysResidence} (résidence) ---
  Méthode                    : ${r.detailsResidence.methode}
  Formulaire                 : ${r.detailsResidence.formulaireResidence}${
  r.paysResidence === 'BE'
    ? `\n  IPP fédéral théorique/an   : ${eur(r.detailsResidence.ippFederalTheoriqueAnnuel)}`
      + `\n  Taux additionnel communal  : ${(r.detailsResidence.tauxCommunalApplique * 100).toFixed(2)} %`
      + `\n  Additionnel communal/an    : ${eur(r.detailsResidence.additionnelCommunalAnnuel)}`
    : ''
}
  Ajustement résidence/mois  : - ${eur(r.ajustementResidenceMensuel)}

  → NET FINAL MENSUEL        : ${eur(r.netFinalMensuel)}
  → NET FINAL ANNUEL         : ${eur(r.netFinalAnnuel)}
  → Taux global de retenue   : ${(r.tauxRetenueGlobal * 100).toFixed(1)} %

  Avertissements :
${r.avertissements.map(a => '    ⚠  ' + a).join('\n')}
`);
} catch (e) {
  console.error(`✗ ${e.message}`);
  process.exit(1);
}
