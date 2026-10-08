/**
 * PDF text extractor — client-side only (runs in browser, never sends file to server)
 *
 * Uses pdfjs-dist (Mozilla PDF.js) to extract text from PDF files directly
 * in the browser. No file upload, no server processing — the PDF stays on
 * the user's device.
 *
 * Thai text support: pdfjs-dist handles Thai encoding correctly, unlike
 * server-side libraries like pdf-parse which often produce garbled output
 * for Thai fonts.
 *
 * Usage:
 *   import { extractTextFromPDF } from '@/lib/pdf-extract';
 *   const text = await extractTextFromPDF(file);
 *   console.log(text);
 */

// Dynamic import — pdfjs-dist only works in browser (uses Web Workers)
// We import it inside the function so Next.js doesn't try to bundle it server-side
// Use 'unknown' + cast to avoid TS mismatch between our local type and pdfjs-dist's exported type
type AnyPdfDocument = {
  numPages: number;
  getPage: (pageNum: number) => Promise<{
    getTextContent: () => Promise<{
      items: Array<{ str: string; hasEOL?: boolean; transform?: number[] }>;
    }>;
  }>;
};

// eslint-disable-next-line @typescript-eslint/no-explicit-any
let pdfjsPromise: Promise<any> | null = null;

// eslint-disable-next-line @typescript-eslint/no-explicit-any
async function loadPdfJs(): Promise<any> {
  // @ts-ignore — pdfjs-dist is installed at runtime, TS may not find types in all configs
  pdfjsPromise ??= import('pdfjs-dist');
  const pdfjs = await pdfjsPromise;
  configurePdfWorker(pdfjs);
  return pdfjs;
}

/** Configure the PDF.js Web Worker to use a CDN that matches the installed version. */
function configurePdfWorker(pdfjs: { version: string; GlobalWorkerOptions?: { workerSrc: string } }): void {
  if (typeof window === 'undefined' || !pdfjs.GlobalWorkerOptions) return;
  pdfjs.GlobalWorkerOptions.workerSrc = `https://cdn.jsdelivr.net/npm/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;
}

export interface PDFExtractResult {
  text: string;
  pageCount: number;
  fileName: string;
  fileSize: number;
}

export interface PdfPageText {
  pageNumber: number;
  text: string;
  charCount: number;
  isSkippable: boolean;
  skipReason?: string;
}

export interface PDFPagesResult {
  pages: PdfPageText[];
  totalChars: number;
  pageCount: number;
  fileName: string;
  fileSize: number;
}

export interface PDFExtractError {
  error: string;
  fileName: string;
}

/**
 * Extract text from a PDF File object in the browser.
 *
 * @param file — PDF File from <input type="file"> or drag-drop
 * @param onProgress — optional callback(page, total) for progress UI
 * @returns PDFExtractResult with concatenated text from all pages
 *
 * Throws Error if:
 *   - file is not a PDF
 *   - file is too large (>10MB client-side limit, well within browser memory)
 *   - pdfjs fails to load or parse
 */
export async function extractTextFromPDF(
  file: File,
  onProgress?: (currentPage: number, totalPages: number) => void,
): Promise<PDFExtractResult> {
  validatePdfFile(file);

  try {
    const pdfjs = await loadPdfJs();
    const arrayBuffer = await file.arrayBuffer();
    const loadingTask = pdfjs.getDocument({ data: arrayBuffer });
    const pdf: AnyPdfDocument = await loadingTask.promise;
    const fullText = await extractAllPages(pdf, onProgress);
    validateExtractedText(fullText);

    return {
      text: fullText.trim(),
      pageCount: pdf.numPages,
      fileName: file.name,
      fileSize: file.size,
    };
  } catch (err: unknown) {
    throw wrapPdfError(err);
  }
}

/** Validate file type and non-emptiness. No size limit — browser handles large files. */
function validatePdfFile(file: File): void {
  if (!file.type.includes('pdf') && !file.name.toLowerCase().endsWith('.pdf')) {
    throw new Error(`ไฟล์ต้องเป็น PDF เท่านั้น (ได้รับ: ${file.type || 'unknown'})`);
  }
  if (file.size === 0) {
    throw new Error('ไฟล์ว่างเปล่า — อาจเสียหาย');
  }
}

/** Extract text from all pages, calling onProgress for each page. */
async function extractAllPages(
  pdf: AnyPdfDocument,
  onProgress?: (currentPage: number, totalPages: number) => void,
): Promise<string> {
  let fullText = '';
  for (let i = 1; i <= pdf.numPages; i++) {
    onProgress?.(i, pdf.numPages);
    const page = await pdf.getPage(i);
    const textContent = await page.getTextContent();
    const pageText = buildPageText(textContent.items);
    const separator = i < pdf.numPages ? `\n\n--- หน้า ${i + 1} ---\n\n` : '';
    fullText += pageText + separator;
  }
  return fullText;
}

/** Reconstruct text from pdfjs text items, handling line breaks. */
function buildPageText(items: Array<{ str: string; hasEOL?: boolean; transform?: number[] }>): string {
  let text = '';
  let lastY: number | null = null;
  for (const item of items) {
    const str = item.str || '';
    if (!str) {
      if (item.hasEOL) text += '\n';
      continue;
    }
    if (item.transform && item.transform.length >= 6) {
      const y = item.transform[5];
      if (lastY !== null && Math.abs(y - lastY) > 2) {
        text += '\n';
      }
      lastY = y;
    }
    text += str;
    if (item.hasEOL) {
      text += '\n';
      lastY = null;
    }
  }
  return text;
}

/** Validate that extracted text is not empty (could be scanned PDF). */
function validateExtractedText(text: string): void {
  if (!text.trim()) {
    throw new Error('ไม่พบข้อความใน PDF — อาจเป็น PDF ที่เป็นภาพสแกน (scanned PDF). กรุณาใช้ PDF ที่มีข้อความจริง ไม่ใช่ภาพ');
  }
}

/** Wrap pdfjs errors with user-friendly Thai messages. */
function wrapPdfError(err: unknown): Error {
  const message = err instanceof Error ? err.message : String(err);
  if (message.includes('ไฟล์')) {
    return err instanceof Error ? err : new Error(message);
  }
  const errName = (err as { name?: string }).name;
  if (errName === 'PasswordException') {
    return new Error('PDF นี้มีรหัสผ่าน — กรุณาถอดรหัสก่อนอัปโหลด');
  }
  if (errName === 'InvalidPDFException') {
    return new Error('ไฟล์ PDF เสียหายหรือไม่ใช่ PDF ที่ถูกต้อง');
  }
  return new Error(`ไม่สามารถอ่าน PDF ได้: ${message}`);
}

/**
 * Format file size for display.
 */
export function formatFileSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / 1024 / 1024).toFixed(1)} MB`;
}

// =========================================================================
// Page-level extraction (for contract chunker)
// =========================================================================

/**
 * Extract text from a PDF, page by page, with auto-filtering of skippable pages.
 *
 * Returns PdfPageText[] where each page has:
 *   - pageNumber: 1-indexed
 *   - text: extracted text
 *   - charCount: length of text
 *   - isSkippable: true if page looks like cover/TOC/blank
 *   - skipReason: why it was skipped (for UI display)
 *
 * @param file PDF File object
 * @param onProgress callback(currentPage, totalPages)
 */
export async function extractPdfPages(
  file: File,
  onProgress?: (currentPage: number, totalPages: number) => void,
): Promise<PDFPagesResult> {
  validatePdfFile(file);

  try {
    const pdfjs = await loadPdfJs();
    const arrayBuffer = await file.arrayBuffer();
    const loadingTask = pdfjs.getDocument({ data: arrayBuffer });
    const pdf: AnyPdfDocument = await loadingTask.promise;

    const pages: PdfPageText[] = [];
    let totalChars = 0;

    for (let i = 1; i <= pdf.numPages; i++) {
      onProgress?.(i, pdf.numPages);
      const page = await pdf.getPage(i);
      const textContent = await page.getTextContent();
      const pageText = buildPageText(textContent.items).trim();
      const charCount = pageText.length;
      totalChars += charCount;

      const skip = classifyPage(i, pageText, charCount, pdf.numPages);
      pages.push({
        pageNumber: i,
        text: pageText,
        charCount,
        isSkippable: skip.skippable,
        skipReason: skip.reason,
      });
    }

    if (totalChars === 0) {
      throw new Error('ไม่พบข้อความใน PDF — อาจเป็น PDF ที่เป็นภาพสแกน (scanned PDF)');
    }

    return {
      pages,
      totalChars,
      pageCount: pdf.numPages,
      fileName: file.name,
      fileSize: file.size,
    };
  } catch (err: unknown) {
    throw wrapPdfError(err);
  }
}

/**
 * Classify whether a page should be skipped during analysis.
 *
 * Skip rules:
 *   1. Blank page: < 50 chars (likely scanned image or intentional blank)
 *   2. Cover page: first 1-2 pages, short text, contains company keywords
 *   3. Table of contents: contains many page numbers (e.g., "หน้า 1", ".... 5")
 *   4. Appendix with no legal content: contains "ภาคผนวก" + minimal text
 *
 * Returns { skippable: boolean, reason?: string }
 */
function classifyPage(
  pageNum: number,
  text: string,
  charCount: number,
  totalPages: number,
): { skippable: boolean; reason?: string } {
  const blank = checkBlankPage(charCount);
  if (blank) return blank;

  const cover = checkCoverPage(pageNum, charCount, text);
  if (cover) return cover;

  const toc = checkTableOfContents(text);
  if (toc) return toc;

  const sig = checkSignaturePage(pageNum, totalPages, charCount, text);
  if (sig) return sig;

  return { skippable: false };
}

/** Rule 1: Blank or near-blank pages (< 50 chars). */
function checkBlankPage(charCount: number): { skippable: boolean; reason?: string } | null {
  if (charCount < 50) {
    return { skippable: true, reason: 'หน้าว่างหรือข้อความน้อยเกินไป' };
  }
  return null;
}

/** Rule 2: Cover page — first 2 pages, short text with company keywords. */
function checkCoverPage(pageNum: number, charCount: number, text: string): { skippable: boolean; reason?: string } | null {
  if (pageNum > 2 || charCount >= 500) return null;
  const coverKeywords = ['สัญญา', 'บริษัท', 'ห้างหุ้นส่วน', 'จำกัด', 'ทำขึ้น', 'ระหว่าง'];
  if (coverKeywords.some(kw => text.includes(kw))) {
    return { skippable: true, reason: 'หน้าปกสัญญา' };
  }
  return null;
}

/** Rule 3: Table of contents — many page number references (e.g., ".... 5"). */
function checkTableOfContents(text: string): { skippable: boolean; reason?: string } | null {
  let pageRefCount = 0;
  let dotStreak = 0;
  for (const char of text) {
    if (char === '.') {
      dotStreak++;
    } else if (dotStreak >= 2 && char >= '0' && char <= '9') {
      pageRefCount++;
      dotStreak = 0;
      if (pageRefCount >= 5) return { skippable: true, reason: 'สารบัญ (มีเลขหน้าอ้างอิงจำนวนมาก)' };
    } else {
      dotStreak = 0;
    }
  }
  return null;
}

/** Rule 4: Signature page — last page, very short, has signature keywords. */
function checkSignaturePage(pageNum: number, totalPages: number, charCount: number, text: string): { skippable: boolean; reason?: string } | null {
  if (pageNum < totalPages - 1 || charCount >= 200) return null;
  const sigKeywords = ['ลงนาม', 'ผู้จ้าง', 'ลูกจ้าง', 'พยาน', 'วันที่'];
  const hasSig = sigKeywords.some(kw => text.includes(kw));
  if (hasSig && !text.includes('มาตรา')) {
    return { skippable: true, reason: 'หน้าลงนาม (ไม่มีเนื้อหากฎหมาย)' };
  }
  return null;
}

