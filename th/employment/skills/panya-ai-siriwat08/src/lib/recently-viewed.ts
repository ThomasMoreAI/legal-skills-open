// Recently Viewed — tracks the last 20 items the user visited
// (laws, sections, judgments) using localStorage.

export interface RecentlyViewedItem {
  type: 'law' | 'section' | 'judgment';
  id: number;
  label: string;
  url: string;
  viewedAt: string; // ISO timestamp
}

const STORAGE_KEY = 'panya_recently_viewed';
const MAX_ITEMS = 20;

export function getRecentlyViewed(): RecentlyViewedItem[] {
  if (typeof window === 'undefined') return [];
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return [];
    const items = JSON.parse(raw) as RecentlyViewedItem[];
    return Array.isArray(items) ? items : [];
  } catch {
    return [];
  }
}

export function addRecentlyViewed(item: Omit<RecentlyViewedItem, 'viewedAt'>): void {
  if (typeof window === 'undefined') return;
  try {
    const items = getRecentlyViewed();
    // Remove duplicate (same type + id)
    const filtered = items.filter(i => !(i.type === item.type && i.id === item.id));
    // Add new item at front
    filtered.unshift({ ...item, viewedAt: new Date().toISOString() });
    // Trim to max
    const trimmed = filtered.slice(0, MAX_ITEMS);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(trimmed));
    window.dispatchEvent(new Event('panya-recently-viewed-changed'));
  } catch {
    // localStorage might be full or unavailable
  }
}

export function clearRecentlyViewed(): void {
  if (typeof window === 'undefined') return;
  localStorage.removeItem(STORAGE_KEY);
  window.dispatchEvent(new Event('panya-recently-viewed-changed'));
}

/** Hook for React components to subscribe to recently viewed changes. */
export function useRecentlyViewed() {
  // This is a simple hook — components call getRecentlyViewed() on render
  // and listen to the 'panya-recently-viewed-changed' event.
  // We keep it simple to avoid adding a state management library.
  return {
    items: getRecentlyViewed(),
    add: addRecentlyViewed,
    clear: clearRecentlyViewed,
  };
}
