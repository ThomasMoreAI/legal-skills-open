/**
 * lib/i18n — Internationalisation de l'interface (Milestone 13).
 *
 * Français par défaut ; anglais, allemand et luxembourgeois prévus. Traduit
 * les libellés d'interface (navigation, colonnes du tableau de bord, statuts,
 * couleurs d'alerte). Le contenu réglementaire, lui, reste en français avec sa
 * source (la traduction porte sur l'habillage, pas sur le droit).
 *
 * Les traductions LB (Lëtzebuergesch) sont fournies à titre indicatif.
 * Aucune dépendance externe.
 */

export const LANGUES = ['fr', 'en', 'de', 'lb'];
export const LANGUE_DEFAUT = 'fr';

/** Dictionnaire : domaine → clé → { fr, en, de, lb }. */
export const DICT = Object.freeze({
  navigation: {
    tableau_de_bord: { fr: 'Tableau de bord', en: 'Dashboard', de: 'Übersicht', lb: 'Iwwersiicht' },
    obligations: { fr: 'Mes obligations', en: 'My obligations', de: 'Meine Pflichten', lb: 'Meng Flichten' },
    documents: { fr: 'Mes documents', en: 'My documents', de: 'Meine Dokumente', lb: 'Meng Dokumenter' },
    echeances: { fr: 'Mes échéances', en: 'My deadlines', de: 'Meine Fristen', lb: 'Meng Fristen' },
    demarches: { fr: 'Mes démarches', en: 'My procedures', de: 'Meine Verfahren', lb: 'Meng Demarchen' },
    entreprises: { fr: 'Mes entreprises', en: 'My companies', de: 'Meine Unternehmen', lb: 'Meng Betriber' },
    courrier: { fr: 'Générer un courrier', en: 'Generate a letter', de: 'Brief erstellen', lb: 'Bréif erstellen' },
    question: { fr: 'Poser une question', en: 'Ask a question', de: 'Eine Frage stellen', lb: 'Eng Fro stellen' },
    parametres: { fr: 'Paramètres', en: 'Settings', de: 'Einstellungen', lb: 'Astellungen' },
  },
  colonnes: {
    obligatoire_maintenant: { fr: 'Obligatoire maintenant', en: 'Required now', de: 'Jetzt erforderlich', lb: 'Elo obligatoresch' },
    a_faire_prochainement: { fr: 'À faire prochainement', en: 'Coming up', de: 'Demnächst', lb: 'Geschwënn ze maachen' },
    a_surveiller: { fr: 'À surveiller', en: 'To monitor', de: 'Zu beobachten', lb: 'Am A behalen' },
    non_applicable: { fr: 'Non applicable', en: 'Not applicable', de: 'Nicht zutreffend', lb: 'Net applicabel' },
    informations_manquantes: { fr: 'Informations manquantes', en: 'Missing information', de: 'Fehlende Angaben', lb: 'Fehlend Informatiounen' },
  },
  statuts: {
    a_preparer: { fr: 'À préparer', en: 'To prepare', de: 'Vorzubereiten', lb: 'Virzebereeden' },
    en_attente_information: { fr: 'En attente d\'information', en: 'Awaiting information', de: 'Warten auf Informationen', lb: 'Waart op Informatioun' },
    pret_a_envoyer: { fr: 'Prêt à envoyer', en: 'Ready to send', de: 'Sendebereit', lb: 'Prett fir ze schécken' },
    envoye: { fr: 'Envoyé', en: 'Sent', de: 'Gesendet', lb: 'Geschéckt' },
    en_attente_reponse: { fr: 'En attente de réponse', en: 'Awaiting reply', de: 'Warten auf Antwort', lb: 'Waart op Äntwert' },
    termine: { fr: 'Terminé', en: 'Done', de: 'Erledigt', lb: 'Fäerdeg' },
    en_retard: { fr: 'En retard', en: 'Overdue', de: 'Überfällig', lb: 'Am Retard' },
    bloque: { fr: 'Bloqué', en: 'Blocked', de: 'Blockiert', lb: 'Blockéiert' },
  },
  couleurs: {
    rouge: { fr: 'Échéance dépassée', en: 'Overdue', de: 'Frist überschritten', lb: 'Frist iwwerschratt' },
    orange: { fr: 'Moins de 7 jours', en: 'Less than 7 days', de: 'Weniger als 7 Tage', lb: 'Manner wéi 7 Deeg' },
    jaune: { fr: 'Moins de 30 jours', en: 'Less than 30 days', de: 'Weniger als 30 Tage', lb: 'Manner wéi 30 Deeg' },
    vert: { fr: 'Terminé', en: 'Done', de: 'Erledigt', lb: 'Fäerdeg' },
    neutre: { fr: 'À surveiller', en: 'To monitor', de: 'Zu beobachten', lb: 'Am A behalen' },
  },
});

/** Valide/normalise un code langue (repli sur le français). */
export function normaliserLangue(langue) {
  return LANGUES.includes(langue) ? langue : LANGUE_DEFAUT;
}

/**
 * Traduit une clé d'un domaine dans la langue demandée (repli FR puis clé brute).
 */
export function traduire(domaine, cle, langue = LANGUE_DEFAUT) {
  const l = normaliserLangue(langue);
  const entree = DICT[domaine] && DICT[domaine][cle];
  if (!entree) return cle;
  return entree[l] || entree[LANGUE_DEFAUT] || cle;
}

/** Renvoie un traducteur lié à une langue : t('colonnes','a_surveiller'). */
export function traducteur(langue = LANGUE_DEFAUT) {
  const l = normaliserLangue(langue);
  return (domaine, cle) => traduire(domaine, cle, l);
}

/** Tous les libellés d'un domaine dans une langue (pour construire un menu). */
export function libelles(domaine, langue = LANGUE_DEFAUT) {
  const l = normaliserLangue(langue);
  const d = DICT[domaine] || {};
  return Object.fromEntries(Object.keys(d).map((cle) => [cle, traduire(domaine, cle, l)]));
}
