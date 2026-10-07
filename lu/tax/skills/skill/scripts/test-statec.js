import {
  getSSMCourant,
  getSSMJeune,
  derniereTranche,
  indexerSalaire,
  TRANCHES_INDEXATION,
  SSM_HISTORIQUE,
} from '../lib/indice-statec/index.js';

let passed = 0, failed = 0;
function test(name, fn) {
  try { fn(); passed++; console.log(`  ✓ ${name}`); }
  catch (e) { failed++; console.log(`  ✗ ${name} : ${e.message}`); }
}
function eq(a, b, msg = '') { if (a !== b) throw new Error(`${msg} attendu ${b}, reçu ${a}`); }
function close(a, b, tol = 0.01) { if (Math.abs(a - b) > tol) throw new Error(`${a} ≠ ${b} (tol ${tol})`); }
function truthy(x) { if (!x) throw new Error('falsy'); }

console.log('Tests indice-statec :\n');

test('SSM_HISTORIQUE est un tableau non vide', () => {
  truthy(Array.isArray(SSM_HISTORIQUE) && SSM_HISTORIQUE.length >= 3);
});

test('TRANCHES_INDEXATION est triée chronologiquement', () => {
  for (let i = 1; i < TRANCHES_INDEXATION.length; i++) {
    truthy(TRANCHES_INDEXATION[i].date >= TRANCHES_INDEXATION[i - 1].date);
  }
});

test('SSM courant à 2025-06-01 = 2703,74 € (non qualifié)', () => {
  const r = getSSMCourant({ date: '2025-06-01' });
  close(r.ssmMensuel, 2703.74);
});

test('SSM qualifié à 2025-06-01 = 3244,49 €', () => {
  const r = getSSMCourant({ qualifie: true, date: '2025-06-01' });
  close(r.ssmMensuel, 3244.49);
});

test('SSM 2024 = SSM 2023 (pas de loi de revalorisation)', () => {
  const a = getSSMCourant({ date: '2024-06-01' });
  const b = getSSMCourant({ date: '2023-12-01' });
  eq(a.ssmMensuel, b.ssmMensuel);
});

test('SSM avant 2025 < SSM après 2025-01', () => {
  const avant = getSSMCourant({ date: '2024-12-31' });
  const apres = getSSMCourant({ date: '2025-01-01' });
  truthy(apres.ssmMensuel > avant.ssmMensuel);
});

test('SSM horaire = SSM mensuel / 173', () => {
  const r = getSSMCourant({ date: '2025-06-01' });
  close(r.ssmHoraire, r.ssmMensuel / 173, 0.001);
});

test('SSM date invalide rejetée', () => {
  let ok = false; try { getSSMCourant({ date: '2025-99-99' }); } catch { ok = true; }
  truthy(ok);
});

test('SSM jeune 17-18 = 80 % du non-qualifié', () => {
  const r = getSSMJeune({ tranche: '17-18', date: '2025-06-01' });
  const adulte = getSSMCourant({ date: '2025-06-01' });
  close(r.ssmMensuel, adulte.ssmMensuel * 0.80);
});

test('SSM jeune 15-17 = 75 % du non-qualifié', () => {
  const r = getSSMJeune({ tranche: '15-17', date: '2025-06-01' });
  const adulte = getSSMCourant({ date: '2025-06-01' });
  close(r.ssmMensuel, adulte.ssmMensuel * 0.75);
});

test('SSM jeune tranche inconnue rejetée', () => {
  let ok = false; try { getSSMJeune({ tranche: '12-14' }); } catch { ok = true; }
  truthy(ok);
});

test('Dernière tranche à 2024-06-01 est 2023-09-01', () => {
  const r = derniereTranche('2024-06-01');
  eq(r.derniere.date, '2023-09-01');
});

test('Tranches déclenchées 2022→2024 ≥ 3', () => {
  const r = derniereTranche('2024-01-01');
  truthy(r.nbTranchesDepuis('2022-01-01') >= 3);
});

test('Indexation salaire signé 2022-01-01 jusqu\'à 2024-01-01', () => {
  const r = indexerSalaire({
    brutReference: 5000,
    dateReference: '2022-01-01',
    dateCible: '2024-01-01',
  });
  truthy(r.nbTranches >= 3);
  truthy(r.brutIndexe > 5000);
  close(r.brutIndexe, 5000 * Math.pow(1.025, r.nbTranches), 0.01);
});

test('Indexation sans tranche déclenchée → brut inchangé', () => {
  const r = indexerSalaire({
    brutReference: 5000,
    dateReference: '2024-01-01',
    dateCible: '2024-06-01',
  });
  eq(r.nbTranches, 0);
  close(r.brutIndexe, 5000);
  eq(r.facteur, 1);
});

test('Indexation brut 0 ou négatif rejetée', () => {
  let ok1 = false, ok2 = false;
  try { indexerSalaire({ brutReference: 0, dateReference: '2022-01-01' }); } catch { ok1 = true; }
  try { indexerSalaire({ brutReference: -100, dateReference: '2022-01-01' }); } catch { ok2 = true; }
  truthy(ok1 && ok2);
});

test('Indexation cible antérieure à référence rejetée', () => {
  let ok = false;
  try { indexerSalaire({ brutReference: 5000, dateReference: '2024-01-01', dateCible: '2023-01-01' }); }
  catch { ok = true; }
  truthy(ok);
});

test('Indexation date référence invalide rejetée', () => {
  let ok = false;
  try { indexerSalaire({ brutReference: 5000, dateReference: '2024-13-01' }); } catch { ok = true; }
  truthy(ok);
});

test('Indexation brut NaN rejeté', () => {
  let ok = false;
  try { indexerSalaire({ brutReference: NaN, dateReference: '2022-01-01' }); } catch { ok = true; }
  truthy(ok);
});

test('Cohérence : SSM 2025-05 > SSM 2025-01 (indexation mai)', () => {
  const janv = getSSMCourant({ date: '2025-01-15' });
  const mai = getSSMCourant({ date: '2025-05-15' });
  truthy(mai.ssmMensuel > janv.ssmMensuel);
  close(mai.ssmMensuel / janv.ssmMensuel, 1.025, 0.001);
});

console.log(`\n${passed} passé(s), ${failed} échec(s)`);
process.exit(failed === 0 ? 0 : 1);
