// Shared types for Panya-AI

export type LawCategory =
  | 'labor'
  | 'civil'
  | 'criminal'
  | 'civil_procedure'
  | 'criminal_procedure'
  | 'land'
  | 'rent'
  | 'narcotics'
  | 'traffic'
  | 'other';

export type JudgmentCategory = 'labor' | 'criminal' | 'civil' | 'other';

export type View =
  | { name: 'home' }
  | { name: 'laws' }
  | { name: 'law'; lawId: number }
  | { name: 'section'; sectionId: number }
  | { name: 'judgments' }
  | { name: 'judgment'; judgmentId: number }
  | { name: 'search'; q?: string; type?: 'all' | 'sections' | 'judgments' | 'laws' }
  | { name: 'bookmarks' }
  | { name: 'templates' }
  | { name: 'data-dashboard' }
  | { name: 'ask' }
  | { name: 'pdf-builder'; templateId?: number }
  | { name: 'risk-matrix' }
  | { name: 'contract-analysis' };

export interface LawSummary {
  lawId: number;
  lawNameTh: string;
  lawNameEn: string | null;
  year: string | null;
  category: string;
  isLaborLaw: number;
  status: string | null;
  sourceUrl: string | null;
  sectionCount: number;
  laborSectionCount: number;
}

export interface LawDetail extends LawSummary {
  fullText: string | null;
  notes: string | null;
  krisdikaSysid: string | null;
  lawGoThId: string | null;
}

export interface SectionSummary {
  sectionId: number;
  lawId: number;
  lawNameTh: string;
  articleKey: string | null;
  sectionNumber: string | null;
  sectionText: string;
  isLaborRelated: number;
  isCancelled: number;
  chapter: string | null;
  notes: string | null;
}

export interface SectionDetail extends SectionSummary {
  relatedJudgments: JudgmentSummary[];
}

export interface JudgmentSummary {
  judgmentId: number;
  caseNumber: string | null;
  caseYear: string | null;
  category: string | null;
  title: string | null;
  fact: string | null;
  decision: string | null;
  sourceUrl: string | null;
  sourceName: string | null;
  licenseNote: string | null;
}

export interface JudgmentDetail extends JudgmentSummary {
  court: string | null;
  categoryCode: string | null;
  issueNumber: string | null;
  lawReferences: string | null;
  relatedSections: SectionSummary[];
  sourceDescription: string | null;
  sourceUrl: string | null;
}

export interface DashboardStats {
  totalLaws: number;
  totalSections: number;
  totalJudgments: number;
  totalLaborSections: number;
  totalLaborJudgments: number;
  totalCriminalJudgments: number;
  laborLawCount: number;
  caseLawLinks: number;
  ragChunks: number;
  lawsByCategory: { category: string; count: number; sectionCount: number }[];
}

export interface SearchResult {
  type: 'section' | 'judgment' | 'law';
  id: number;
  title: string;
  snippet: string;
  meta: string;
  url: string;
}

export interface ChatMessage {
  role: 'user' | 'assistant' | 'system';
  content: string;
  citations?: Citation[];
}

export interface Citation {
  type: 'section' | 'judgment';
  id: number;
  label: string;
  ref: string;
  snippet: string;
  url: string;
}
