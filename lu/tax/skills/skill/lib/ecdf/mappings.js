/**
 * mappings.js — Correspondance Plan Comptable Normalisé → rubriques eCDF.
 *
 * Sources :
 *   - Loi modifiée du 19 décembre 2002 (LSC) — schéma abrégé bilan + compte de résultat
 *   - Règlement grand-ducal du 10 juin 2009 — Plan Comptable Normalisé luxembourgeois
 *   - Documentation formulaires eCDF : https://ecdf.b2g.etat.lu/
 *
 * NOTE : les codes de rubriques eCDF (101, 105, 1101, ...) sont ceux du formulaire
 * "Comptes annuels — schéma abrégé" publié par la CNC. Vérifier le mapping après
 * import dans le tester eCDF officiel avant tout dépôt légal.
 */

/**
 * BILAN ABRÉGÉ — Actif (codes eCDF + agrégation des comptes PCN).
 * Format : { code, libelle, classes_pcn (préfixes), signe }
 * signe : +1 si actif (solde débiteur attendu), -1 si à inverser
 */
export const BILAN_ACTIF = [
  { code: '101', libelle: 'A. Capital souscrit non versé',                    pcn: ['109'],                 signe: +1 },
  { code: '105', libelle: 'B. Frais d\'établissement',                        pcn: ['20'],                  signe: +1 },
  { code: '1101', libelle: 'C. Actif immobilisé',                             pcn: ['21', '22', '23', '26', '27'], signe: +1, agregat: true },
  { code: '1103', libelle: 'C.I Immobilisations incorporelles',               pcn: ['21'],                  signe: +1 },
  { code: '1115', libelle: 'C.II Immobilisations corporelles',                pcn: ['22', '23'],            signe: +1 },
  { code: '1131', libelle: 'C.III Immobilisations financières',               pcn: ['26', '27'],            signe: +1 },
  { code: '1151', libelle: 'D. Actif circulant',                              pcn: ['3', '40', '41', '42', '43', '44', '45', '46', '47', '50', '51'], signe: +1, agregat: true },
  { code: '1153', libelle: 'D.I Stocks',                                      pcn: ['3'],                   signe: +1 },
  { code: '1163', libelle: 'D.II Créances',                                   pcn: ['41'],                  signe: +1 },
  { code: '1183', libelle: 'D.III Valeurs mobilières',                        pcn: ['50'],                  signe: +1 },
  { code: '1191', libelle: 'D.IV Avoirs en banque, CCP, caisse',              pcn: ['51', '53', '54'],      signe: +1 },
  { code: '1201', libelle: 'E. Comptes de régularisation',                    pcn: ['486'],                 signe: +1 },
  { code: '1999', libelle: 'TOTAL ACTIF',                                     pcn: [],                      signe: +1, total: true },
];

/**
 * BILAN ABRÉGÉ — Passif.
 * Note : les classes 1, 4 (40-48 dettes), 6, 7 sont créditrices au PCN.
 */
export const BILAN_PASSIF = [
  { code: '1301', libelle: 'A. Capitaux propres',                             pcn: ['10', '11', '12', '13', '14'], signe: -1, agregat: true },
  { code: '1303', libelle: 'A.I Capital souscrit',                            pcn: ['101'],                 signe: -1 },
  { code: '1305', libelle: 'A.II Primes d\'émission',                         pcn: ['11'],                  signe: -1 },
  { code: '1311', libelle: 'A.IV Réserves',                                   pcn: ['13'],                  signe: -1 },
  { code: '1313', libelle: 'A.V Résultats reportés',                          pcn: ['14'],                  signe: -1 },
  { code: '1321', libelle: 'A.VI Résultat de l\'exercice',                    pcn: [],                      signe: -1, calcule: 'resultat' },
  { code: '1401', libelle: 'B. Provisions',                                   pcn: ['15', '16'],            signe: -1 },
  { code: '1501', libelle: 'C. Dettes',                                       pcn: ['40', '42', '43', '44', '46', '47'], signe: -1, agregat: true },
  { code: '1521', libelle: 'C.4 Dettes sur achats et prestations de services',pcn: ['40'],                  signe: -1 },
  { code: '1561', libelle: 'C.8 Dettes fiscales et sociales',                 pcn: ['42', '43', '44'],      signe: -1 },
  { code: '1581', libelle: 'C.9 Autres dettes',                               pcn: ['46'],                  signe: -1 },
  { code: '1601', libelle: 'D. Comptes de régularisation',                    pcn: ['487'],                 signe: -1 },
  { code: '2999', libelle: 'TOTAL PASSIF',                                    pcn: [],                      signe: -1, total: true },
];

/**
 * COMPTE DE RÉSULTAT ABRÉGÉ — codes eCDF 3xxx.
 * Convention PCN : classe 7 = produits (créditrice, signe -1), classe 6 = charges (débitrice, signe +1).
 * Rubriques eCDF en valeur absolue avec sens explicite.
 */
export const COMPTE_RESULTAT = [
  { code: '3001', libelle: '1. Chiffre d\'affaires net',                                    pcn: ['70'],            signe: -1, sens: 'produit' },
  { code: '3003', libelle: '2. Variation des stocks de produits finis et en cours',         pcn: ['71'],            signe: -1, sens: 'produit' },
  { code: '3005', libelle: '3. Travaux effectués pour soi-même portés à l\'actif',          pcn: ['72'],            signe: -1, sens: 'produit' },
  { code: '3007', libelle: '4. Autres produits d\'exploitation',                            pcn: ['74', '75'],      signe: -1, sens: 'produit' },
  { code: '3013', libelle: '5.a Coût des marchandises vendues, matières et fournitures',    pcn: ['60'],            signe: +1, sens: 'charge' },
  { code: '3015', libelle: '5.b Autres charges externes',                                   pcn: ['61', '62'],      signe: +1, sens: 'charge' },
  { code: '3017', libelle: '6. Frais de personnel',                                         pcn: ['64'],            signe: +1, sens: 'charge' },
  { code: '3019', libelle: '7. Corrections de valeur',                                      pcn: ['68'],            signe: +1, sens: 'charge' },
  { code: '3023', libelle: '8. Autres charges d\'exploitation',                             pcn: ['65'],            signe: +1, sens: 'charge' },
  { code: '3025', libelle: '9. Produits provenant de participations',                       pcn: ['76'],            signe: -1, sens: 'produit' },
  { code: '3033', libelle: '11. Autres intérêts et produits financiers',                    pcn: ['77'],            signe: -1, sens: 'produit' },
  { code: '3045', libelle: '13. Intérêts et autres charges financières',                    pcn: ['66'],            signe: +1, sens: 'charge' },
  { code: '3055', libelle: '14. Impôts sur le résultat',                                    pcn: ['691', '692'],    signe: +1, sens: 'charge' },
  { code: '3061', libelle: '16. Autres impôts',                                             pcn: ['63'],            signe: +1, sens: 'charge' },
  { code: '3063', libelle: '17. Résultat de l\'exercice',                                   pcn: [],                signe: +1, sens: 'calcule', total: true },
];

export const META_FORM = {
  type_formulaire: 'CA-A',  // Comptes Annuels — Schéma Abrégé
  taxonomie: 'eCDF Comptes annuels - schéma abrégé',
  source_doc: 'https://ecdf.b2g.etat.lu/ecdf/displayHelp.action?context=BUSINESS_FORMS',
  remarque: 'Codes de rubriques sur la base du formulaire eCDF "CA-A". Vérifier sur le tester officiel avant dépôt légal.',
};
