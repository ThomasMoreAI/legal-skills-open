/**
 * Indice STATEC + SSM (Salaire Social Minimum) — Luxembourg
 *
 * Le Luxembourg applique l'échelle mobile des salaires : dès que l'indice
 * semestriel des prix à la consommation national (IPCN, base 100 = 2015)
 * dépasse un seuil, tous les salaires, pensions et prestations sociales
 * sont automatiquement indexés de +2,5 %.
 *
 * Sources :
 * - STATEC, indice des prix à la consommation : https://statistiques.public.lu/fr/themes/economie-finances/prix.html
 * - Loi modifiée du 25 mars 2015 sur les salaires
 * - Loi du 19 décembre 2024 (revalorisation SSM 2025)
 *
 * ⚠️  Les valeurs ci-dessous sont à jour à la date de publication du module.
 *     Lancer `npm run statec -- --check` pour vérifier la fraîcheur.
 */

// Tranches d'indexation déclenchées (dates effectives, taux cumulé)
// +2,5 % à chaque tranche, appliqué à tous les salaires bruts.
export const TRANCHES_INDEXATION = [
  { date: '2021-10-01', source: 'Mémorial A n° 754 du 23 sept 2021' },
  { date: '2022-04-01', source: 'Mémorial A n° 191 du 30 mars 2022' },
  { date: '2022-08-01', source: 'Mémorial A n° 367 du 22 juil 2022' },
  { date: '2023-02-01', source: 'Mémorial A n° 22 du 23 janv 2023' },
  { date: '2023-09-01', source: 'Mémorial A n° 553 du 24 août 2023' },
  { date: '2025-05-01', source: 'Mémorial A n° 178 du 22 avril 2025' },
];

// Salaire Social Minimum Mensuel (40h/semaine, brut)
// Sources : ITM (Inspection du Travail et des Mines), Mémorial A
export const SSM_HISTORIQUE = [
  { date: '2023-09-01', nonQualifie: 2570.93, qualifie: 3085.11, source: 'Indexation 1er sept 2023' },
  { date: '2024-01-01', nonQualifie: 2570.93, qualifie: 3085.11, source: 'Pas de revalorisation 2024 hors index' },
  { date: '2025-01-01', nonQualifie: 2637.79, qualifie: 3165.35, source: 'Loi du 19 déc 2024 (revalorisation 2,6 %)' },
  { date: '2025-05-01', nonQualifie: 2703.74, qualifie: 3244.49, source: 'Indexation 1er mai 2025 (+2,5 %)' },
];

// SSM réduit jeunes travailleurs (apprentis et < 18 ans)
export const SSM_JEUNES_RATIOS = {
  '17-18': 0.80, // 80 % du SSM non-qualifié
  '15-17': 0.75, // 75 % du SSM non-qualifié
};

/**
 * Renvoie le SSM en vigueur à la date donnée (par défaut aujourd'hui).
 * @param {object} options
 * @param {boolean} [options.qualifie=false] true si travailleur qualifié
 * @param {string} [options.date] date ISO YYYY-MM-DD (défaut : aujourd'hui)
 * @returns {{ ssmMensuel: number, ssmHoraire: number, source: string, dateEntreeVigueur: string }}
 */
export function getSSMCourant({ qualifie = false, date } = {}) {
  const ref = date || new Date().toISOString().slice(0, 10);
  if (!validerDateISOReelle(ref)) throw new Error(`date invalide : ${ref}`);

  const tri = [...SSM_HISTORIQUE].sort((a, b) => a.date.localeCompare(b.date));
  let courant = tri[0];
  for (const e of tri) if (e.date <= ref) courant = e;

  const ssmMensuel = qualifie ? courant.qualifie : courant.nonQualifie;
  // Base 173 heures/mois (40h × 52/12)
  const ssmHoraire = round4(ssmMensuel / 173);
  return {
    ssmMensuel: round2(ssmMensuel),
    ssmHoraire,
    source: courant.source,
    dateEntreeVigueur: courant.date,
  };
}

/**
 * Renvoie la dernière tranche d'indexation déclenchée à la date donnée.
 * @param {string} [date] ISO YYYY-MM-DD
 * @returns {{ date: string, source: string, nbTranchesDepuis: (since: string) => number }}
 */
export function derniereTranche(date) {
  const ref = date || new Date().toISOString().slice(0, 10);
  if (!validerDateISOReelle(ref)) throw new Error(`date invalide : ${ref}`);

  const tri = [...TRANCHES_INDEXATION].sort((a, b) => a.date.localeCompare(b.date));
  const passees = tri.filter((t) => t.date <= ref);
  const courante = passees[passees.length - 1] || null;

  return {
    derniere: courante,
    toutes: passees,
    nbTranchesDepuis(since) {
      if (!validerDateISOReelle(since)) throw new Error(`date invalide : ${since}`);
      return tri.filter((t) => t.date > since && t.date <= ref).length;
    },
  };
}

/**
 * Calcule le brut indexé d'un salaire à partir d'une date de référence.
 * Ajoute +2,5 % par tranche déclenchée entre la date de référence et aujourd'hui.
 *
 * @param {object} options
 * @param {number} options.brutReference brut au moment de la signature du contrat
 * @param {string} options.dateReference date du brut de référence (ISO)
 * @param {string} [options.dateCible] date à laquelle on veut le brut indexé (défaut aujourd'hui)
 * @returns {{ brutIndexe: number, nbTranches: number, facteur: number, tranchesAppliquees: Array }}
 */
export function indexerSalaire({ brutReference, dateReference, dateCible } = {}) {
  if (!Number.isFinite(brutReference) || brutReference <= 0) {
    throw new Error('brutReference doit être un nombre fini > 0');
  }
  if (!validerDateISOReelle(dateReference)) {
    throw new Error(`dateReference invalide : ${dateReference}`);
  }
  const cible = dateCible || new Date().toISOString().slice(0, 10);
  if (!validerDateISOReelle(cible)) throw new Error(`dateCible invalide : ${cible}`);
  if (cible < dateReference) throw new Error('dateCible doit être ≥ dateReference');

  const tranches = TRANCHES_INDEXATION.filter(
    (t) => t.date > dateReference && t.date <= cible,
  );
  const facteur = Math.pow(1.025, tranches.length);
  return {
    brutIndexe: round2(brutReference * facteur),
    nbTranches: tranches.length,
    facteur: round4(facteur),
    tranchesAppliquees: tranches,
  };
}

/**
 * Calcule le SSM jeune travailleur (apprenti ou moins de 18 ans).
 * @param {object} options
 * @param {'15-17'|'17-18'} options.tranche
 * @param {string} [options.date]
 */
export function getSSMJeune({ tranche, date } = {}) {
  if (!SSM_JEUNES_RATIOS[tranche]) {
    throw new Error(`tranche invalide : ${tranche} (attendu '15-17' ou '17-18')`);
  }
  const adulte = getSSMCourant({ qualifie: false, date });
  const ratio = SSM_JEUNES_RATIOS[tranche];
  return {
    tranche,
    ratio,
    ssmMensuel: round2(adulte.ssmMensuel * ratio),
    ssmHoraire: round4(adulte.ssmHoraire * ratio),
    source: `${adulte.source} × ${(ratio * 100).toFixed(0)} %`,
    dateEntreeVigueur: adulte.dateEntreeVigueur,
  };
}

// --- Helpers ---

function validerDateISOReelle(s) {
  if (typeof s !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(s)) return false;
  const [y, m, d] = s.split('-').map(Number);
  const dt = new Date(Date.UTC(y, m - 1, d));
  return dt.getUTCFullYear() === y && dt.getUTCMonth() === m - 1 && dt.getUTCDate() === d;
}

function round2(n) { return Math.round(n * 100) / 100; }
function round4(n) { return Math.round(n * 10000) / 10000; }
