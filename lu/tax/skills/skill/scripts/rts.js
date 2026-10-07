#!/usr/bin/env node
/**
 * rts.js — CLI : calcul de la retenue à la source (RTS) sur salaire LU.
 *
 * Usage :
 *   paperasse rts --brut 5000 --classe 1
 *   paperasse rts --brut 8000 --classe 2
 *   paperasse rts --brut 4000 --classe 1a --cim
 */

import { calculerRTS } from '../lib/rts/index.js';

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
  console.error(`Usage : paperasse rts --brut <€> --classe <1|1a|2> [options]

Options :
  --brut <€>      Salaire brut mensuel (obligatoire)
  --classe <c>    Classe d'impôt : 1, 1a, ou 2 (obligatoire)
  --no-cis        Désactive le crédit d'impôt salarié (CIS)
  --cim           Active le crédit d'impôt monoparental (CIM)

Exemples :
  paperasse rts --brut 5000 --classe 1
  paperasse rts --brut 8000 --classe 2
  paperasse rts --brut 4000 --classe 1a --cim
`);
  process.exit(args.length === 0 ? 1 : 0);
}

try {
  const r = calculerRTS({
    salaireBrutMensuel: Number(arg('brut')),
    classe: String(arg('classe')),
    cisActif: !flag('no-cis'),
    cimActif: flag('cim'),
  });
  const eur = (n) => n.toLocaleString('fr-LU', { style: 'currency', currency: 'EUR' });
  console.log(`
=== Retenue à la source LU 2025 ===
  Salaire brut mensuel       : ${eur(r.salaireBrutMensuel)}
  Classe d'impôt             : ${r.classe}

  Cotisations sociales (CSSS):
    - Maladie (2,80 %)       : ${eur(r.csss.maladie)}
    - Pension (8,00 %)       : ${eur(r.csss.pension)}
    - Total                  : ${eur(r.csss.total)}

  Revenu imposable mensuel   : ${eur(r.revenuImposableMensuel)}
  IRPP annuel théorique      : ${eur(r.irppAnnuel)}
  IRPP mensuel avant crédits : ${eur(r.irppMensuelAvantCredits)}
  Crédits d'impôt            : - ${eur(r.creditsImpot.total)}  (CIS ${eur(r.creditsImpot.cis)} + CIM ${eur(r.creditsImpot.cim)})
  IRPP mensuel à retenir     : ${eur(r.irppMensuel)}
  Contribution dépendance    : ${eur(r.contribDependance)}

  → NET MENSUEL              : ${eur(r.netMensuel)}
  → NET ANNUEL               : ${eur(r.netAnnuel)}
  → Taux de retenue effectif : ${(r.tauxRetenueEffectif * 100).toFixed(1)} %
${r.avertissements.length ? '\n  Avertissements :\n' + r.avertissements.map(a => '    ⚠  ' + a).join('\n') : ''}
`);
} catch (e) {
  console.error(`✗ ${e.message}`);
  process.exit(1);
}
