// Shared API helper functions for pdf route — extracted for testability.

/** Convert markdown to HTML (headers, bold, italic, lists, lines, paragraphs). */
export function markdownToHtml(text: string): string {
  let html = text
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;');

  html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
  html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');
  html = html.replace(/^# (.+)$/gm, '<h1>$1</h1>');
  html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
  html = html.replace(/^[-*] (.+)$/gm, '<li>$1</li>');
  html = html.replace(/(<li>[\s\S]+?<\/li>)/g, '<ul>$1</ul>');
  html = html.replace(/^---$/gm, '<hr/>');
  html = html.replaceAll('\n\n', '</p><p>');
  return '<p>' + html + '</p>';
}

/** Fill employee name in first 5 blank fields. */
export function fillEmployeeName(html: string, name: string): string {
  if (!name) return html;
  let count = 0;
  return html.replace(/_{3,}/g, (match) => {
    if (count < 5 && match.includes('___')) {
      count++;
      return `<u>&nbsp;${name}&nbsp;</u>`;
    }
    return match;
  });
}

/** Fill position in first 2 position fields. */
export function fillPosition(html: string, position: string): string {
  if (!position) return html;
  let posCount = 0;
  return html.replace(/ตำแหน่ง\s*[:.]\s*_{2,}/g, () => {
    if (posCount < 2) {
      posCount++;
      return `ตำแหน่ง: <u>&nbsp;${position}&nbsp;</u>`;
    }
    return 'ตำแหน่ง: ___________';
  });
}

/** Fill start date in date field. */
export function fillStartDate(html: string, startDate: string): string {
  if (!startDate) return html;
  return html.replace(
    /วันที่\s*_{2,}\s*เดือน\s*_{2,}\s*พ\.ศ\.\s*_{2,}/g,
    `วันที่ <u>&nbsp;${startDate}&nbsp;</u>`
  );
}

/** Fill salary amounts (first 2 amounts < 1000) using split+join (no regex backtracking). */
export function fillSalary(html: string, salary: string): string {
  if (!salary) return html;
  const marker = ' บาท';
  const parts = html.split(marker);
  let salCount = 0;
  const trailingDigits = /\d{1,6}$/;
  for (let idx = 1; idx < parts.length; idx++) {
    const before = parts[idx - 1];
    const match = trailingDigits.exec(before);
    if (match) {
      const numVal = Number.parseInt(match[0], 10);
      if (salCount < 2 && numVal < 1000) {
        salCount++;
        parts[idx - 1] = before.slice(0, match.index) + `<u>&nbsp;${salary}&nbsp;</u>`;
      }
    }
  }
  return parts.join(marker);
}
