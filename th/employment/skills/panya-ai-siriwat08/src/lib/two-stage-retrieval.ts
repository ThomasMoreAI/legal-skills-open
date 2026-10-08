/**
 * Two-Stage Retrieval — REC-006 from Genspark review
 *
 * Stage 1: Classify the user's question into one of the 8 legal categories
 *          (A-H) using keyword matching. Returns a category hint.
 * Stage 2: The RAG retrieveRelevant() function uses the category hint to
 *          filter the search scope — only searching tables for that category.
 *
 * This reduces noise by ~60% (per Genspark estimate) because:
 *   - Labor questions only search labor laws + labor judgments
 *   - Criminal questions only search criminal laws + criminal judgments
 *   - Civil questions only search civil laws + civil judgments
 *   - etc.
 *
 * Categories match the manifest structure:
 *   A = labor (แรงงาน)
 *   B = criminal (อาญา)
 *   C = civil (แพ่ง)
 *   D = other (ภาษี/IP/ขนส่ง)
 *   E = business (ธุรกิจ)
 *   F = templates (เอกสาร/สัญญา)
 *   G = judgments (คำพิพากษาฎีกา)
 *   H = regulations (อนุบัญญัติ/กฎกระทรัวง)
 */

// ---------------------------------------------------------------------------
// Category definitions
// ---------------------------------------------------------------------------
export type LegalCategory = 'labor' | 'criminal' | 'civil' | 'business' | 'tax' | 'transport' | 'other' | 'all';

export interface CategoryDefinition {
  code: string;          // A, B, C, D, E
  name: string;          // labor, criminal, civil, etc.
  thaiName: string;      // แรงงาน, อาญา, etc.
  keywords: string[];    // Thai + English keywords that signal this category
}

export const CATEGORIES: CategoryDefinition[] = [
  {
    code: 'A',
    name: 'labor',
    thaiName: 'แรงงาน',
    keywords: [
      'แรงงาน', 'คุ้มครองแรงงาน', 'ประกันสังคม', 'เงินทดแทน', 'สวัสดิการ',
      'ลูกจ้าง', 'นายจ้าง', 'ค่าจ้าง', 'เงินเดือน', 'โบนัส', 'ค่าล่วงเวลา',
      'เลิกจ้าง', 'เลิกจ้าง', 'ทำงาน', 'วันหยุด', 'วันลา', 'ลาป่วย', 'ลากิจ',
      'ลาคลอด', 'ทดลองงาน', 'สัญญาจ้าง', 'แรงงานสัมพันธ์', 'ศาลแรงงาน',
      'กองทุนเงินทดแทน', 'ความปลอดภัยในการทำงาน', 'พักงาน', 'ย้ายตำแหน่ง',
      'ลดค่าจ้าง', 'หักเงินเดือน', 'ค่าชดเชย', 'สินจ้าง', 'บุริมสิทธิ์',
      'สหภาพแรงงาน', 'ผู้รับเหมาช่วง', 'จ้างทำของ', 'จ้างแรงงาน',
      'work from home', 'WFH', 'labor', 'employment', 'wage', 'overtime',
      'severance', 'termination', 'employee', 'employer',
    ],
  },
  {
    code: 'B',
    name: 'criminal',
    thaiName: 'อาญา',
    keywords: [
      'อาญา', 'ความผิด', 'คดีอาญา', 'จำคุก', 'ปรับ', 'จำเลย', 'โจทก์',
      'คอมพิวเตอร์', 'PDPA', 'ข้อมูลส่วนบุคคล', 'ยาเสพติด', 'ฉ้อโกง',
      'ยักยอก', 'ปลอมเอกสาร', 'หมิ่นประมาท', 'ฆ่า', 'ลักทรัพย์', 'ชิงทรัพย์',
      'ป.อ.', 'ป.วิ.อ.', 'วิธีพิจารณาความอาญา', 'อุทธรณ์', 'ฎีกา',
      'criminal', 'crime', 'felony', 'misdemeanor', 'penal',
    ],
  },
  {
    code: 'C',
    name: 'civil',
    thaiName: 'แพ่งและพาณิชย์',
    keywords: [
      'แพ่ง', 'พาณิชย์', 'ป.พ.พ.', 'สัญญา', 'ละเมิด', 'ค่าเสียหาย',
      'ค่าสินไหม', 'จำนอง', 'จำนำ', 'ค้ำประกัน', 'กู้ยืม', 'เช่า',
      'ซื้อขาย', 'ตัวแทน', 'นายหน้า', 'NDA', 'ความลับ', 'ไม่แข่งขัน',
      'Non-compete', 'ล้มละลาย', 'ที่ดิน', 'ทรัพย์สิน', 'ครอบครอง',
      'พินัยกรรม', 'มรดก', 'หุ้นส่วน', 'บริษัท', 'นิติบุคคล',
      'civil', 'commercial', 'contract', 'tort', 'property', 'inheritance',
    ],
  },
  {
    code: 'D',
    name: 'tax',
    thaiName: 'ภาษี/IP/ขนส่ง',
    keywords: [
      'ภาษี', 'ภ.ง.ด.', 'รัษฎากร', 'VAT', 'ภาษีมูลค่าเพิ่ม', 'ภาษีเงินได้',
      'ลิขสิทธิ์', 'สิทธิบัตร', 'ทรัพย์สินทางปัญญา', 'trademark', 'patent',
      'ขนส่ง', 'การเดินอากาศ', 'การรับขน', 'ทะเล', 'เรือ', 'รถ',
      'จราจร', 'ขนส่งทางบก', 'logistics', 'transport', 'shipping',
    ],
  },
  {
    code: 'E',
    name: 'business',
    thaiName: 'ธุรกิจ',
    keywords: [
      'บริษัทมหาชน', 'หลักทรัพย์', 'ตลาดทุน', 'ธุรกรรมอิเล็กทรอนิกส์',
      'e-Commerce', 'บริษัทจำกัด', 'ห้างหุ้นส่วน', 'กรรมการ', 'ผู้ถือหุ้น',
      'บัญชี', 'งบการเงิน', 'ผู้สอบบัญชี', 'business', 'corporate',
      'securities', 'stock', 'company',
    ],
  },
];

// ---------------------------------------------------------------------------
// Stage 1: Classify question into a category
// ---------------------------------------------------------------------------
export interface ClassificationResult {
  category: LegalCategory;
  categoryCode: string;     // A, B, C, D, E, or '' for 'all'
  confidence: number;       // 0.0 to 1.0
  matchedKeywords: string[];
  allScores: Record<string, number>;  // category name → score
}

/**
 * Classify a user's legal question into one of the 5 categories (A-E).
 * Returns 'all' if no category matches with sufficient confidence.
 *
 * Algorithm:
 *   1. For each category, count how many of its keywords appear in the question
 *   2. Score = matched_keyword_count / total_keyword_count (capped at 1.0)
 *   3. Pick the category with the highest score
 *   4. If top score < 0.05 (very low confidence), return 'all' (search everything)
 *
 * @param question The user's question (Thai or English)
 * @returns ClassificationResult with category + confidence + scores
 */
export function classifyQuestion(question: string): ClassificationResult {
  if (!question || question.trim().length === 0) {
    return {
      category: 'all',
      categoryCode: '',
      confidence: 0,
      matchedKeywords: [],
      allScores: {},
    };
  }

  const q = question.toLowerCase();
  const scores: Record<string, number> = {};
  const matched: Record<string, string[]> = {};

  for (const cat of CATEGORIES) {
    let matchCount = 0;
    const matchedKw: string[] = [];
    for (const kw of cat.keywords) {
      if (q.includes(kw.toLowerCase())) {
        matchCount++;
        matchedKw.push(kw);
      }
    }
    // Score = matched / total, but weighted: more matches = higher confidence
    // Use a sigmoid-like curve: score = matchCount / (matchCount + 5)
    // This gives: 1 match → 0.17, 3 matches → 0.38, 5 matches → 0.50, 10 → 0.67
    const score = matchCount / (matchCount + 5);
    scores[cat.name] = score;
    matched[cat.name] = matchedKw;
  }

  // Find the category with the highest score
  let bestCategory: LegalCategory = 'all';
  let bestCode = '';
  let bestScore = 0;
  let bestMatched: string[] = [];
  for (const cat of CATEGORIES) {
    if (scores[cat.name] > bestScore) {
      bestScore = scores[cat.name];
      bestCategory = cat.name as LegalCategory;
      bestCode = cat.code;
      bestMatched = matched[cat.name];
    }
  }

  // If best score is too low (no clear signal), search all
  const MIN_CONFIDENCE = 0.10;
  if (bestScore < MIN_CONFIDENCE) {
    return {
      category: 'all',
      categoryCode: '',
      confidence: bestScore,
      matchedKeywords: bestMatched,
      allScores: scores,
    };
  }

  return {
    category: bestCategory,
    categoryCode: bestCode,
    confidence: bestScore,
    matchedKeywords: bestMatched,
    allScores: scores,
  };
}

/**
 * Get the SQL filter clause for a category to apply to law_sections + judgments.
 *
 * For 'labor' (A): filter to laws.category = 'labor' AND judgments.case_type = 'แรงงาน'
 * For 'criminal' (B): filter to laws.category = 'criminal' AND judgments.case_type contains 'อาญา'
 * For 'civil' (C): filter to laws.category = 'civil' OR 'land'
 * For 'tax' (D): filter to laws.category = 'tax' OR 'transport' OR 'other'
 * For 'business' (E): filter to laws.category = 'business'
 * For 'all': no filter (search everything)
 *
 * Returns an object with `lawFilter` and `judgmentFilter` SQL fragments
 * (without WHERE keyword) that can be ANDed into existing queries.
 */
export function getCategoryFilters(category: LegalCategory): {
  lawFilter: string;
  judgmentFilter: string;
  regulationFilter: string;
} {
  switch (category) {
    case 'labor':
      return {
        lawFilter: "AND (l.category = 'labor' OR l.category = 'labor_related')",
        judgmentFilter: "AND j.case_type = 'แรงงาน'",
        regulationFilter: "AND (r.category = 'min_wage' OR r.category = 'wage' OR r.category = 'welfare' OR r.category = 'compensation_fund' OR r.category = 'social_security' OR r.category = 'safety' OR r.category = 'subcontracting' OR r.category = 'prohibited_work')",
      };
    case 'criminal':
      return {
        lawFilter: "AND l.category = 'criminal'",
        judgmentFilter: "AND (j.case_type LIKE '%อาญา%' OR j.case_type LIKE '%criminal%')",
        regulationFilter: "AND 1=0", // no criminal regulations in our corpus
      };
    case 'civil':
      return {
        lawFilter: "AND (l.category = 'civil' OR l.category = 'land')",
        judgmentFilter: "AND (j.case_type LIKE '%แพ่ง%' OR j.case_type LIKE '%civil%')",
        regulationFilter: "AND 1=0",
      };
    case 'tax':
      return {
        lawFilter: "AND (l.category = 'tax' OR l.category = 'transport' OR l.category = 'other')",
        judgmentFilter: "AND 1=0", // few tax judgments in our corpus
        regulationFilter: "AND r.category = 'tax'",
      };
    case 'business':
      return {
        lawFilter: "AND l.category = 'business'",
        judgmentFilter: "AND (j.case_type LIKE '%ธุรกิจ%' OR j.case_type LIKE '%business%')",
        regulationFilter: "AND r.category = 'business'",
      };
    case 'transport':
      return {
        lawFilter: "AND l.category = 'transport'",
        judgmentFilter: "AND 1=0",
        regulationFilter: "AND 1=0",
      };
    case 'other':
    case 'all':
    default:
      return {
        lawFilter: '', // no filter — search all
        judgmentFilter: '',
        regulationFilter: '',
      };
  }
}
