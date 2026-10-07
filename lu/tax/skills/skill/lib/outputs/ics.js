/**
 * lib/outputs/ics.js — Sérialiseur iCalendar (RFC 5545) minimal, zéro dépendance.
 *
 * Un adaptateur parmi d'autres : il transforme des TimelineEvent en flux .ics.
 * Le moteur ne « se connecte » pas à un calendrier ; il produit un artefact
 * Timeline, et cet adaptateur l'exporte.
 */

const escape = (s) => String(s == null ? '' : s)
  .replace(/\\/g, '\\\\').replace(/;/g, '\\;').replace(/,/g, '\\,').replace(/\r?\n/g, '\\n');

/** YYYY-MM-DD → YYYYMMDD (date « toute la journée »). */
const jour = (iso) => String(iso || '').replace(/-/g, '');
/** YYYY-MM-DD → YYYYMMDDT000000Z (horodatage UTC). */
const stamp = (iso) => `${jour(iso)}T000000Z`;

/**
 * Produit un flux VCALENDAR à partir de TimelineEvent (ceux ayant une échéance).
 *
 * @param {object[]} evenements  TimelineEvent[]
 * @param {object} [opts] { dtstamp (YYYY-MM-DD), nomCalendrier, prodId, alarmeJours }
 * @returns {string} contenu .ics (CRLF)
 */
export function timelineVersICS(evenements, opts = {}) {
  const dtstamp = stamp(opts.dtstamp || '2026-01-01');
  const prodId = opts.prodId || '-//Paperasse Lux//Assistant administratif//FR';
  const alarme = Number.isFinite(opts.alarmeJours) ? opts.alarmeJours : 7;

  const l = ['BEGIN:VCALENDAR', 'VERSION:2.0', `PRODID:${prodId}`, 'CALSCALE:GREGORIAN'];
  if (opts.nomCalendrier) l.push(`X-WR-CALNAME:${escape(opts.nomCalendrier)}`);

  let n = 0;
  for (const ev of evenements) {
    const date = ev.deadline || ev.date;
    if (!date) continue; // pas d'échéance → pas d'entrée calendrier
    n += 1;
    const uid = `${escape(ev.mission || 'mission')}-${escape(ev.id || n)}@paperasse-lux`;
    l.push('BEGIN:VEVENT');
    l.push(`UID:${uid}`);
    l.push(`DTSTAMP:${dtstamp}`);
    l.push(`DTSTART;VALUE=DATE:${jour(date)}`);
    l.push(`SUMMARY:${escape((ev.priority === 'high' ? '⚠ ' : '') + ev.title)}`);
    const desc = [ev.mission ? `Mission : ${ev.mission}` : null, ev.blocking ? 'Étape bloquante.' : null, ev.source ? `Source : ${ev.source}` : null]
      .filter(Boolean).join('\n');
    if (desc) l.push(`DESCRIPTION:${escape(desc)}`);
    l.push(`STATUS:${ev.status === 'done' ? 'COMPLETED' : 'CONFIRMED'}`);
    // Rappel N jours avant l'échéance.
    l.push('BEGIN:VALARM', 'ACTION:DISPLAY', `TRIGGER:-P${alarme}D`, `DESCRIPTION:${escape('Rappel : ' + ev.title)}`, 'END:VALARM');
    l.push('END:VEVENT');
  }
  l.push('END:VCALENDAR');
  return l.join('\r\n') + '\r\n';
}
