'use client';

import { useEffect, useState } from 'react';
import { Hero } from '@/components/home/Hero';
import { LawList } from '@/components/home/LawList';
import type { DashboardStats, LawSummary } from '@/lib/types';

export function HomeView() {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [laws, setLaws] = useState<LawSummary[]>([]);

  useEffect(() => {
    fetch('/api/stats')
      .then(r => r.json())
      .then(setStats)
      .catch(console.error);
    fetch('/api/laws')
      .then(r => r.json())
      .then(setLaws)
      .catch(console.error);
  }, []);

  return (
    <>
      <Hero stats={stats} />
      <LawList laws={laws} />
    </>
  );
}
