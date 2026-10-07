/**
 * checklists.js — Pièces à déposer au LBR selon l'opération.
 *
 * Source : Luxembourg Business Registers — guides publics et formulaires officiels.
 */

export const OPERATIONS = [
  'creation_sarl',
  'creation_sa',
  'creation_asbl',
  'modification_statuts',
  'changement_dirigeant',
  'transfert_siege',
  'depot_comptes_annuels',
  'dissolution_liquidation',
];

export const CHECKLISTS_LBR = {
  creation_sarl: {
    libelle: 'Création d\'une SARL (Société à Responsabilité Limitée)',
    capital_minimum_eur: 12000,
    pieces: [
      'Acte constitutif notarié (statuts) — original + 2 copies certifiées',
      'Liste des associés avec parts détenues',
      'Justificatif du dépôt du capital sur compte bancaire bloqué (attestation banque LU)',
      'Pièce d\'identité de chaque associé personne physique (copie certifiée)',
      'Extrait LBR récent (< 3 mois) pour chaque associé personne morale',
      'Désignation du ou des gérants avec acceptation écrite',
      'Adresse du siège social (justificatif : bail, titre de propriété ou domiciliation agréée)',
      'Formulaire de réquisition LBR signé',
      'Avis de publication au RESA (Recueil électronique des sociétés et associations)',
    ],
    delai_jours: 15,
    cout_indicatif_eur: 1500,
    cout_detail: 'Frais de notaire (≈ 1 200 €) + LBR 22 € + RESA + capital 12 000 €',
    bases_legales: ['Loi modifiée du 10 août 1915 sur les sociétés commerciales, Titre IV'],
  },

  creation_sa: {
    libelle: 'Création d\'une SA (Société Anonyme)',
    capital_minimum_eur: 30000,
    pieces: [
      'Acte constitutif notarié (statuts)',
      'Liste des actionnaires fondateurs',
      'Justificatif du dépôt du capital (libération min. 25 % à la souscription)',
      'Désignation des administrateurs et du commissaire aux comptes',
      'Pièces d\'identité des fondateurs',
      'Adresse du siège social',
      'Formulaire de réquisition LBR signé',
    ],
    delai_jours: 15,
    cout_indicatif_eur: 2500,
    bases_legales: ['Loi modifiée du 10 août 1915, Titre III'],
  },

  creation_asbl: {
    libelle: 'Création d\'une ASBL (Association Sans But Lucratif)',
    capital_minimum_eur: 0,
    pieces: [
      'Statuts signés par au moins 3 membres fondateurs',
      'Liste des membres fondateurs (nom, prénom, profession, domicile, nationalité)',
      'Désignation des administrateurs et du président',
      'Adresse du siège social',
      'Formulaire de réquisition LBR (catégorie X)',
      'Demande de publication au RESA',
    ],
    delai_jours: 30,
    cout_indicatif_eur: 50,
    bases_legales: ['Loi modifiée du 7 août 2023 sur les ASBL et fondations'],
  },

  modification_statuts: {
    libelle: 'Modification des statuts (objet social, dénomination, capital, durée…)',
    pieces: [
      'PV d\'AG extraordinaire (notarié pour SA/SARL si modification non-mineure)',
      'Statuts coordonnés mis à jour',
      'Formulaire de réquisition modificative LBR',
      'Avis de publication au RESA',
    ],
    delai_jours: 15,
    cout_indicatif_eur: 800,
    bases_legales: ['Loi du 10 août 1915, art. 100-2 et suivants'],
  },

  changement_dirigeant: {
    libelle: 'Changement de gérant, administrateur ou commissaire',
    pieces: [
      'PV d\'AG ou décision de l\'organe compétent actant la nomination/révocation',
      'Acceptation écrite du nouveau dirigeant',
      'Pièce d\'identité du nouveau dirigeant',
      'Formulaire de réquisition modificative LBR',
      'Avis de publication au RESA',
    ],
    delai_jours: 15,
    cout_indicatif_eur: 100,
    cout_detail: 'LBR 11 € + RESA ≈ 80 €',
  },

  transfert_siege: {
    libelle: 'Transfert du siège social (à l\'intérieur du Luxembourg)',
    pieces: [
      'Décision de l\'organe compétent (gérance/conseil/AG selon statuts)',
      'Justificatif de la nouvelle adresse (bail ou domiciliation)',
      'Formulaire de réquisition modificative LBR',
      'Avis de publication au RESA',
    ],
    delai_jours: 15,
    cout_indicatif_eur: 100,
  },

  depot_comptes_annuels: {
    libelle: 'Dépôt des comptes annuels',
    pieces: [
      'Bilan',
      'Compte de profits et pertes',
      'Annexe aux comptes',
      'Rapport de gestion (si non-petite entité)',
      'Rapport du réviseur d\'entreprises agréé (si audit obligatoire)',
      'PV d\'AG d\'approbation des comptes + affectation du résultat',
      'Fichier eCDF (format CA-A pour schéma abrégé)',
    ],
    delai_apres_cloture_mois: 7,
    cout_indicatif_eur: 19,
    cout_detail: 'Tarif LBR forfaitaire 2026 : 19 € par exercice déposé',
    bases_legales: ['Loi du 10 août 1915, art. 79', 'Loi du 19 décembre 2002 (LSC)'],
    voir_aussi: 'paperasse ecdf <input.json>',
  },

  dissolution_liquidation: {
    libelle: 'Dissolution et mise en liquidation',
    pieces: [
      'PV d\'AG extraordinaire prononçant la dissolution (acte notarié pour SA/SARL)',
      'Désignation du ou des liquidateurs',
      'Rapport du commissaire à la liquidation (si applicable)',
      'Comptes de liquidation finaux',
      'PV d\'AG de clôture de liquidation',
      'Formulaire de réquisition LBR (radiation)',
      'Avis de publication au RESA',
    ],
    delai_jours: 30,
    cout_indicatif_eur: 1500,
    cout_detail: 'Honoraires liquidateur + frais notariés + LBR 11 €',
    bases_legales: ['Loi du 10 août 1915, art. 1100-1 à 1100-15'],
  },
};
