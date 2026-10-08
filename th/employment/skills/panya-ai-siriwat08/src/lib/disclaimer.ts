/**
 * Disclaimer Layer — REC-005 from Genspark review
 *
 * Adds a mandatory legal disclaimer to every AI response to:
 * 1. Protect the operator (หจก.เผ่าปัญญา ทรานสปอร์ต) from liability
 * 2. Inform users that AI output is NOT formal legal advice
 * 3. Recommend consulting a licensed lawyer for real cases
 *
 * Usage in API routes:
 *   import { withDisclaimer, DISCLAIMER_TEXT } from '@/lib/disclaimer';
 *   const response = { answer: '...', citations: [...] };
 *   return Response.json(withDisclaimer(response));
 *
 * The disclaimer is appended to the answer text + included as a top-level
 * `disclaimer` field for the UI to render separately if desired.
 */

/**
 * The standard legal disclaimer text (Thai).
 * Worded to comply with Thai legal practice — explicitly states:
 *   - Information only, not formal legal advice
 *   - Should consult a licensed lawyer before acting
 *   - AI may cite outdated laws — always verify with current sources
 */
export const DISCLAIMER_TEXT =
  '\n\n---\n\n' +
  '⚠️ **คำเตือนทางกฎหมาย:** ข้อมูลนี้จัดทำเพื่อการให้ข้อมูลทั่วไปเท่านั้น ' +
  'ไม่ใช่คำแนะนำทางกฎหมายอย่างเป็นทางการ ' +
  'กฎหมายอาจมีการแก้ไขเพิ่มเติม และคำพิพากษาฎีกาใหม่อาจเปลี่ยนแนวทางการตีความ ' +
  'ก่อนตัดสินใจดำเนินการใด ๆ ตามคำตอบนี้ โปรดตรวจสอบกับตัวบทกฎหมายฉบับเต็ม ' +
  'และปรึกษาทนายความหรือผู้เชี่ยวชาญทางกฎหมายที่มีใบอนุญาตสำหรับกรณีเฉพาะของท่าน';

/**
 * Short version for chat UI (less verbose, same legal effect).
 */
export const DISCLAIMER_SHORT =
  '⚠️ ข้อมูลเพื่อการอ้างอิงเท่านั้น ไม่ใช่คำแนะนำทางกฎหมาย — ปรึกษาทนายความก่อนตัดสินใจ';

/**
 * Wrap an API response object to include the disclaimer.
 * Appends DISCLAIMER_TEXT to the `answer` field (if present) and adds
 * a top-level `disclaimer` field with the short version.
 *
 * @example
 *   const apiResponse = { answer: 'นายจ้างต้องจ่าย...', citations: [...] };
 *   return Response.json(withDisclaimer(apiResponse));
 *   // → { answer: '...+\n\n---\n\n⚠️ คำเตือน...', citations: [...], disclaimer: '⚠️ ข้อมูล...' }
 */
export function withDisclaimer<T extends { answer?: string }>(response: T): T & { disclaimer: string } {
  return {
    ...response,
    answer: response.answer ? response.answer + DISCLAIMER_TEXT : response.answer,
    disclaimer: DISCLAIMER_SHORT,
  };
}

/**
 * Determine if a disclaimer should be shown at all.
 * Returns false for non-legal responses (e.g., greeting, system messages).
 *
 * Heuristic: show disclaimer if the answer contains legal references
 * (มาตรา, ฎีกา, พ.ร.บ., ป.พ.พ., ป.อ., ค่าชดเชย, etc.) OR if it's from
 * the ask API (which always deals with legal questions).
 */
export function shouldShowDisclaimer(answer: string): boolean {
  if (!answer || answer.length < 20) return false;
  const legalMarkers = [
    'มาตรา', 'ฎีกา', 'พ.ร.บ.', 'ป.พ.พ.', 'ป.อ.', 'ป.วิ.',
    'ค่าชดเชย', 'เลิกจ้าง', 'ลูกจ้าง', 'นายจ้าง', 'ค่าจ้าง',
    'ประกันสังคม', 'เงินทดแทน', 'ศาลแรงงาน', 'คำพิพากษา',
    'สัญญาจ้าง', 'ลาป่วย', 'วันหยุด', 'ค่าล่วงเวลา',
  ];
  return legalMarkers.some(marker => answer.includes(marker));
}
