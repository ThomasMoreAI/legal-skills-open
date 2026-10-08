// Client-side navigation hook — uses URL query string to manage view state.
// All views render on the same "/" route (per sandbox restriction).

'use client';

import { useCallback, useMemo } from 'react';
import type { View } from '@/lib/types';

export function useNavigation() {
  const getView = useCallback((): View => {
    if (typeof window === 'undefined') return { name: 'home' };
    const params = new URLSearchParams(window.location.search);
    const v = params.get('view');
    const id = params.get('id');
    const q = params.get('q');
    const type = params.get('type') as View extends { name: 'search' } ? any : never;

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
  }, []);

  const navigate = useCallback((view: View) => {
    const params = new URLSearchParams();
    switch (view.name) {
      case 'home': break;
      case 'laws': params.set('view', 'laws'); break;
      case 'law': params.set('view', 'law'); params.set('id', String(view.lawId)); break;
      case 'section': params.set('view', 'section'); params.set('id', String(view.sectionId)); break;
      case 'judgments': params.set('view', 'judgments'); break;
      case 'judgment': params.set('view', 'judgment'); params.set('id', String(view.judgmentId)); break;
      case 'search':
        params.set('view', 'search');
        if (view.q) params.set('q', view.q);
        if (view.type) params.set('type', view.type);
        break;
      case 'bookmarks': params.set('view', 'bookmarks'); break;
      case 'templates': params.set('view', 'templates'); break;
      case 'data-dashboard': params.set('view', 'data-dashboard'); break;
      case 'ask': params.set('view', 'ask'); break;
      case 'pdf-builder':
        params.set('view', 'pdf-builder');
        if (view.templateId) params.set('id', String(view.templateId));
        break;
      case 'risk-matrix': params.set('view', 'risk-matrix'); break;
      case 'contract-analysis': params.set('view', 'contract-analysis'); break;
    }
    const qs = params.toString();
    const newUrl = qs ? `/?${qs}` : '/';
    window.history.pushState({ view: view.name }, '', newUrl);
    // Dispatch event so components can re-render
    window.dispatchEvent(new PopStateEvent('popstate'));
    // Scroll to top on navigation
    window.scrollTo({ top: 0, behavior: 'instant' });
  }, []);

  return useMemo(() => ({ getView, navigate }), [getView, navigate]);
}

// Bookmark hook (localStorage)
export function useBookmarks() {
  const STORAGE_KEY = 'thai_law_hub_bookmarks';

  const getBookmarks = useCallback((): Array<{ type: 'section' | 'judgment' | 'law'; id: number; label: string; url: string; savedAt: string }> => {
    if (typeof window === 'undefined') return [];
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch {
      return [];
    }
  }, []);

  const saveBookmarks = useCallback((items: any[]) => {
    if (typeof window === 'undefined') return;
    localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
    window.dispatchEvent(new Event('bookmarks-changed'));
  }, []);

  const addBookmark = useCallback((item: { type: 'section' | 'judgment' | 'law'; id: number; label: string; url: string }) => {
    const items = getBookmarks();
    if (!items.some(b => b.type === item.type && b.id === item.id)) {
      items.unshift({ ...item, savedAt: new Date().toISOString() });
      saveBookmarks(items);
    }
  }, [getBookmarks, saveBookmarks]);

  const removeBookmark = useCallback((type: string, id: number) => {
    const items = getBookmarks();
    const filtered = items.filter(b => !(b.type === type && b.id === id));
    saveBookmarks(filtered);
  }, [getBookmarks, saveBookmarks]);

  const isBookmarked = useCallback((type: string, id: number) => {
    const items = getBookmarks();
    return items.some(b => b.type === type && b.id === id);
  }, [getBookmarks]);

  return { getBookmarks, addBookmark, removeBookmark, isBookmarked };
}
