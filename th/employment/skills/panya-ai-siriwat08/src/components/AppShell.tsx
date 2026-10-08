'use client';

import { useEffect, useState } from 'react';
import { Sidebar } from '@/components/layout/Sidebar';
import { HomeView } from '@/components/home/HomeView';
import { LawsView } from '@/components/law/LawsView';
import { LawView } from '@/components/law/LawView';
import { SectionView } from '@/components/law/SectionView';
import { JudgmentsView } from '@/components/judgment/JudgmentsView';
import { JudgmentView } from '@/components/judgment/JudgmentView';
import { SearchView } from '@/components/search/SearchView';
import { AskView } from '@/components/chat/AskView';
import { BookmarksView } from '@/components/common/BookmarksView';
import { TemplatesView } from '@/components/templates/TemplatesView';
import { DataDashboardView } from '@/components/admin/DataDashboardView';
import { PdfBuilderView } from '@/components/pdf/PdfBuilderView';
import { RiskMatrixView } from '@/components/risk/RiskMatrixView';
import { ContractAnalysisView } from '@/components/contract/ContractAnalysisView';
import { PersonaOnboarding } from '@/components/onboarding/PersonaOnboarding';
import { isOnboarded } from '@/lib/persona';
import type { View } from '@/lib/types';

function parseView(): View {
  if (typeof window === 'undefined') return { name: 'home' };
  const params = new URLSearchParams(window.location.search);
  const v = params.get('view');
  const id = params.get('id');
  const q = params.get('q');
  const type = params.get('type') as any;

  switch (v) {
    case 'laws': return { name: 'laws' };
    case 'law': return { name: 'law', lawId: id ? Number.parseInt(id, 10) : 0 };
    case 'section': return { name: 'section', sectionId: id ? Number.parseInt(id, 10) : 0 };
    case 'judgments': return { name: 'judgments' };
    case 'judgment': return { name: 'judgment', judgmentId: id ? Number.parseInt(id, 10) : 0 };
    case 'search': return { name: 'search', q: q || undefined, type: type || 'all' };
    case 'bookmarks': return { name: 'bookmarks' };
    case 'templates': return { name: 'templates' };
    case 'data-dashboard': return { name: 'data-dashboard' };
    case 'ask': return { name: 'ask' };
    case 'pdf-builder': return { name: 'pdf-builder', templateId: id ? Number.parseInt(id, 10) : undefined };
    case 'risk-matrix': return { name: 'risk-matrix' };
    case 'contract-analysis': return { name: 'contract-analysis' };
    default: return { name: 'home' };
  }
}

export function AppShell() {
  const [view, setView] = useState<View>({ name: 'home' });
  const [showOnboarding, setShowOnboarding] = useState(false);

  useEffect(() => {
    const update = () => {
      setView(parseView());
      // Scroll to top on view change (except when only query changes for search)
      window.scrollTo({ top: 0, behavior: 'instant' });
    };
    update();
    window.addEventListener('popstate', update);
    // Trigger persona onboarding on first visit
    if (!isOnboarded()) {
      // Small delay so the home page renders first
      const t = setTimeout(() => setShowOnboarding(true), 800);
      return () => {
        window.removeEventListener('popstate', update);
        clearTimeout(t);
      };
    }
    return () => window.removeEventListener('popstate', update);
  }, []);

  return (
    <div className="flex min-h-screen">
      <Sidebar />
      <main className={`flex-1 bg-background pl-14 md:pl-0 ${view.name === 'ask' ? 'overflow-hidden h-screen' : 'overflow-y-auto'}`}>
        {view.name === 'home' && <HomeView />}
        {view.name === 'laws' && <LawsView />}
        {view.name === 'law' && view.lawId > 0 && <LawView lawId={view.lawId} />}
        {view.name === 'law' && view.lawId <= 0 && <InvalidId message="ไม่พบกฎหมาย" />}
        {view.name === 'section' && view.sectionId > 0 && <SectionView sectionId={view.sectionId} />}
        {view.name === 'section' && view.sectionId <= 0 && <InvalidId message="ไม่พบมาตรา" />}
        {view.name === 'judgments' && <JudgmentsView />}
        {view.name === 'judgment' && view.judgmentId > 0 && <JudgmentView judgmentId={view.judgmentId} />}
        {view.name === 'judgment' && view.judgmentId <= 0 && <InvalidId message="ไม่พบคำพิพากษา" />}
        {view.name === 'search' && (
          <SearchView initialQ={view.q} initialType={view.type as any} />
        )}
        {view.name === 'ask' && <AskView />}
        {view.name === 'pdf-builder' && <PdfBuilderView initialTemplateId={view.templateId} />}
        {view.name === 'risk-matrix' && <RiskMatrixView />}
        {view.name === 'contract-analysis' && <ContractAnalysisView />}
        {view.name === 'bookmarks' && <BookmarksView />}
        {view.name === 'templates' && <TemplatesView />}
        {view.name === 'data-dashboard' && <DataDashboardView />}
      </main>

      {/* Persona onboarding modal — shown on first visit */}
      {showOnboarding && (
        <PersonaOnboarding onClose={() => setShowOnboarding(false)} />
      )}
    </div>
  );
}

function InvalidId({ message }: { readonly message: string }) {
  return (
    <div className="mx-auto max-w-2xl px-4 py-20 text-center">
      <p className="text-destructive">{message}</p>
    </div>
  );
}
