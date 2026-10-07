/**
 * lib/documents/lexique.js — Dictionnaires de reconnaissance (Milestone 3).
 *
 * Mots-clés servant à classer un courrier administratif luxembourgeois et à
 * identifier l'administration émettrice. Ce ne sont PAS des affirmations
 * réglementaires (aucune obligation, montant ou délai codé ici) : uniquement
 * de la détection lexicale. Les éléments réglementaires détectés dans un
 * document sont, eux, toujours marqués « incertains » (validation humaine).
 *
 * Aucune dépendance externe.
 */

/** Administrations luxembourgeoises et leurs marqueurs textuels. */
export const ADMINISTRATIONS = [
  { id: 'aed', nom: 'Administration de l\'Enregistrement, des Domaines et de la TVA (AED)', motsCles: ['enregistrement des domaines', 'administration de l\'enregistrement', 'aed', 'bureau d\'imposition tva', 'numéro de tva', 'lu\\d{8}'] },
  { id: 'acd', nom: 'Administration des Contributions Directes (ACD)', motsCles: ['contributions directes', 'acd', 'bureau d\'imposition', 'retenue d\'impôt', 'fiche de retenue', 'décompte'] },
  { id: 'ccss', nom: 'Centre commun de la sécurité sociale (CCSS)', motsCles: ['centre commun', 'sécurité sociale', 'ccss', 'cotisations sociales', 'affiliation'] },
  { id: 'cns', nom: 'Caisse nationale de santé (CNS)', motsCles: ['caisse nationale de santé', 'cns', 'assurance maladie', 'indemnité pécuniaire'] },
  { id: 'commune', nom: 'Administration communale', motsCles: ['administration communale', 'bierger-center', 'déclaration d\'arrivée', 'registre communal', 'commune de'] },
  { id: 'rcs', nom: 'Luxembourg Business Registers (RCS/RBE)', motsCles: ['registre de commerce', 'luxembourg business registers', 'lbr', 'rcs', 'bénéficiaires effectifs', 'rbe', 'b\\d{4,7}'] },
  { id: 'immigration', nom: 'Direction de l\'immigration', motsCles: ['direction de l\'immigration', 'titre de séjour', 'autorisation de séjour', 'regroupement familial', 'ministère des affaires étrangères'] },
  { id: 'zukunftskeess', nom: 'Zukunftskeess (CAE — allocations familiales)', motsCles: ['zukunftskeess', 'caisse pour l\'avenir des enfants', 'allocation familiale', 'allocations familiales'] },
  { id: 'itm', nom: 'Inspection du travail et des mines (ITM)', motsCles: ['inspection du travail', 'itm', 'droit du travail'] },
];

/**
 * Types de documents prioritaires (Milestone 3). L'ordre compte : les types
 * les plus spécifiques (mise en demeure, fiche de retenue) sont évalués avant
 * les plus génériques (courrier). Le score = nombre de mots-clés trouvés.
 */
export const TYPES_DOCUMENT = [
  { id: 'mise_en_demeure', nom: 'Mise en demeure / relance', motsCles: ['mise en demeure', 'dernier rappel', 'rappel', 'relance', 'sommation', 'défaut de paiement', 'à défaut de'] },
  { id: 'declaration_tva', nom: 'Déclaration / courrier TVA', motsCles: ['déclaration tva', 'déclaration de tva', 'décompte tva', 'taxe sur la valeur ajoutée', 'période de déclaration'] },
  { id: 'fiche_retenue', nom: 'Fiche de retenue d\'impôt', motsCles: ['fiche de retenue', 'retenue d\'impôt', 'classe d\'impôt', 'crédit d\'impôt'] },
  { id: 'decompte_fiscal', nom: 'Décompte / bulletin fiscal', motsCles: ['décompte', 'bulletin d\'impôt', 'décompte annuel', 'imposition', 'remboursement d\'impôt'] },
  { id: 'facture_peppol', nom: 'Facture (Peppol / e-invoicing)', motsCles: ['facture', 'peppol', 'montant à payer', 'numéro de facture', 'échéance de paiement', 'iban'] },
  { id: 'contrat_bail', nom: 'Contrat de bail', motsCles: ['contrat de bail', 'bail à loyer', 'loyer', 'garantie locative', 'état des lieux', 'bailleur', 'locataire'] },
  { id: 'extrait_rcs', nom: 'Extrait RCS / RBE', motsCles: ['extrait', 'registre de commerce', 'bénéficiaires effectifs', 'dépôt des comptes'] },
  { id: 'courrier_ccss', nom: 'Courrier CCSS', motsCles: ['centre commun', 'cotisations sociales', 'affiliation', 'décompte de cotisations'] },
  { id: 'courrier_immigration', nom: 'Courrier immigration', motsCles: ['titre de séjour', 'autorisation de séjour', 'immigration', 'regroupement familial'] },
  { id: 'courrier', nom: 'Courrier administratif', motsCles: ['courrier', 'notification', 'veuillez', 'concerne', 'objet'], fallback: true },
];

/** Verbes / tournures signalant une action demandée. */
export const MARQUEURS_ACTION = [
  { motif: /veuillez\s+(?:nous\s+)?(?:faire parvenir|transmettre|fournir|communiquer|régulariser|verser|payer)/i, action: 'Transmettre / régulariser les éléments demandés' },
  { motif: /vous êtes (?:prié|invité|tenu)[e]?s?\s+de\s+([^.]{0,80})/i, action: 'Répondre à la demande' },
  { motif: /(?:à|a)\s+(?:déposer|régulariser|compléter|payer|verser)/i, action: 'Effectuer la démarche indiquée' },
  { motif: /prière de/i, action: 'Répondre à la demande' },
  { motif: /montant à payer|solde (?:dû|restant)|à régler/i, action: 'Procéder au paiement' },
];

/** Tournures signalant une conséquence en cas d'inaction. */
export const MARQUEURS_CONSEQUENCE = [
  { motif: /taxation d['’]office/i, texte: 'Taxation d\'office possible' },
  { motif: /amende|astreinte/i, texte: 'Amende / astreinte' },
  { motif: /int[ée]r[êe]ts de retard|majoration/i, texte: 'Intérêts de retard / majoration' },
  { motif: /mise en demeure|sommation/i, texte: 'Mise en demeure' },
  { motif: /poursuite|contrainte|recouvrement forc[ée]/i, texte: 'Recouvrement forcé / poursuites' },
];

/** Mots précédant une date limite. */
export const MARQUEURS_ECHEANCE = [
  'avant le', 'au plus tard le', 'au plus tard pour le', 'pour le', 'délai', 'date limite',
  'endéans', 'dans un délai de', 'jusqu\'au', 'échéance',
];

export const MOIS_FR = {
  janvier: 1, février: 2, fevrier: 2, mars: 3, avril: 4, mai: 5, juin: 6,
  juillet: 7, août: 8, aout: 8, septembre: 9, octobre: 10, novembre: 11, décembre: 12, decembre: 12,
};
