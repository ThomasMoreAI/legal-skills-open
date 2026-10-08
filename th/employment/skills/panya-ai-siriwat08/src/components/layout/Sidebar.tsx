'use client';

import { useEffect, useState } from 'react';
import { Scale, Search, Bookmark, MessageSquare, Home, BookOpen, FileText, Menu, X, ChevronLeft, Grid3x3, FileSearch, Wand2, Database } from 'lucide-react';
import { useNavigation } from '@/lib/navigation';
import { PersonaSwitcher } from '@/components/onboarding/PersonaSwitcher';
import { RecentlyViewed } from '@/components/common/RecentlyViewed';
import { cn } from '@/lib/utils';

const NAV_ITEMS = [
  { view: { name: 'home' } as const, label: 'หน้าแรก', icon: Home },
  { view: { name: 'ask' } as const, label: 'ถาม AI', icon: MessageSquare, badge: 'AI' },
  { view: { name: 'pdf-builder' } as const, label: 'สร้างเอกสาร', icon: Wand2 },
  { view: { name: 'risk-matrix' } as const, label: 'Risk Matrix', icon: Grid3x3 },
  { view: { name: 'contract-analysis' } as const, label: 'วิเคราะห์สัญญา', icon: FileSearch },
  { view: { name: 'laws' } as const, label: 'กฎหมาย', icon: BookOpen },
  { view: { name: 'judgments' } as const, label: 'คำพิพากษา', icon: Scale },
  { view: { name: 'search' } as const, label: 'ค้นหา', icon: Search },
  { view: { name: 'templates' } as const, label: 'เทมเพลต', icon: FileText, badge: '63' },
  { view: { name: 'data-dashboard' } as const, label: 'สถานะข้อมูล', icon: Database },
  { view: { name: 'bookmarks' } as const, label: 'บันทึก', icon: Bookmark },
];

// Logged-in user email (single-tenant app — could be replaced with real auth session)
const USER_EMAIL = 'siriwat@panya-ai.co.th';

export function Sidebar() {
  const { getView, navigate } = useNavigation();
  const [currentView, setCurrentView] = useState<{ name: string }>({ name: 'home' });
  const [collapsed, setCollapsed] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    const update = () => setCurrentView(getView() as any);
    update();
    window.addEventListener('popstate', update);
    return () => window.removeEventListener('popstate', update);
  }, [getView]);

  return (
    <>
      {/* Mobile toggle button — fixed top-left, only on mobile.
          When sidebar is open on mobile, this button hides so it
          doesn't overlap with the logo inside the sidebar. */}
      {!mobileOpen && (
        <button
          type="button"
          onClick={() => setMobileOpen(true)}
          className="fixed top-4 left-4 z-50 md:hidden flex h-10 w-10 items-center justify-center rounded-lg bg-card-soft border border-border/60 shadow-lg"
          aria-label="เปิดเมนู"
        >
          <Menu className="h-5 w-5" />
        </button>
      )}

      {/* Mobile overlay — native <button> so it's keyboard-accessible & screen-reader friendly */}
      {mobileOpen && (
        <button
          type="button"
          onClick={() => setMobileOpen(false)}
          className="fixed inset-0 z-40 bg-black/50 md:hidden cursor-default"
          aria-label="ปิดเมนู"
        />
      )}

      {/* Sidebar */}
      <aside
        className={cn(
          'fixed md:sticky top-0 z-40 flex h-screen flex-col border-r border-border/60 bg-navy transition-all duration-240',
          collapsed ? 'w-[72px]' : 'w-[264px]',
          mobileOpen ? 'left-0' : '-left-[264px] md:left-0'
        )}
        style={{ background: 'var(--navy)' }}
      >
        {/* Brand */}
        <div className="flex items-center gap-3 border-b border-border/40 p-5">
          {/* Mobile close button — replaces the floating hamburger when sidebar is open */}
          {mobileOpen && (
            <button
              type="button"
              onClick={() => setMobileOpen(false)}
              className="md:hidden -ml-2 mr-1 flex h-8 w-8 items-center justify-center rounded-md text-muted-foreground hover:text-foreground hover:bg-accent/40"
              aria-label="ปิดเมนู"
            >
              <X className="h-5 w-5" />
            </button>
          )}

          <button
            type="button"
            onClick={() => { navigate({ name: 'home' }); setMobileOpen(false); }}
            className="flex items-center gap-3 group"
            aria-label="Panya-AI"
          >
            <img
              src="/mascot/mascot-front.png"
              alt="Panya-AI"
              className="h-12 w-12 rounded-lg object-contain ring-1 ring-gold/20"
            />
            {!collapsed && (
              <div className="flex flex-col items-start leading-none">
                <span className="text-base font-bold tracking-tight">
                  <span className="text-gradient-gold">ปัญญา AI</span>
                </span>
                <span className="text-[10px] text-muted-foreground tracking-widest uppercase">Panya-AI</span>
              </div>
            )}
          </button>
          {!collapsed && !mobileOpen && (
            <button
              type="button"
              onClick={() => setCollapsed(true)}
              className="ml-auto hidden md:inline-flex text-muted-foreground hover:text-foreground"
              aria-label="ย่อเมนู"
            >
              <ChevronLeft className="h-4 w-4" />
            </button>
          )}
          {collapsed && (
            <button
              type="button"
              onClick={() => setCollapsed(false)}
              className="mx-auto hidden md:inline-flex text-muted-foreground hover:text-foreground"
              aria-label="ขยายเมนู"
            >
              <Menu className="h-4 w-4" />
            </button>
          )}
        </div>

        {/* Nav */}
        <nav className="flex-1 overflow-y-auto p-3">
          {!collapsed && (
            <div className="px-2 pb-2 pt-3 text-[10px] font-semibold uppercase tracking-wider text-muted-foreground">
              เมนูหลัก
            </div>
          )}
          {NAV_ITEMS.map((item) => {
            const Icon = item.icon;
            const isActive = currentView.name === item.view.name;
            return (
              <button
                type="button"
                key={item.view.name}
                onClick={() => { navigate(item.view); setMobileOpen(false); }}
                className={cn(
                  'flex w-full items-center gap-3 rounded-lg border-l-2 px-3 py-2.5 text-sm transition',
                  collapsed ? 'justify-center' : 'justify-start',
                  isActive
                    ? 'border-l-gold bg-gold/10 font-semibold text-gold'
                    : 'border-l-transparent text-muted-foreground hover:bg-accent/50 hover:text-foreground'
                )}
                title={collapsed ? item.label : undefined}
              >
                <Icon className="h-[18px] w-[18px] flex-shrink-0" strokeWidth={isActive ? 1.8 : 1.5} />
                {!collapsed && (
                  <>
                    <span className="flex-1 text-left">{item.label}</span>
                    {item.badge && (
                      <span className={cn(
                        'rounded-full px-2 py-0.5 text-[10px] font-semibold',
                        item.badge === 'AI'
                          ? 'bg-gold text-navy'
                          : 'bg-white/10 text-muted-foreground'
                      )}>
                        {item.badge}
                      </span>
                    )}
                  </>
                )}
              </button>
            );
          })}
        </nav>

        {/* Recently viewed — quick access to recently opened items */}
        {!collapsed && <RecentlyViewed />}

        {/* User info — show email + persona switcher */}
        {!collapsed && (
          <div className="border-t border-border/40 p-4 space-y-2">
            {/* Persona switcher — quick change role */}
            <PersonaSwitcher />
            {/* User email */}
            <div className="flex items-center gap-3 pt-1">
              <div className="flex h-9 w-9 items-center justify-center rounded-full bg-gradient-to-br from-gold to-gold/70 text-sm font-bold text-navy flex-shrink-0">
                ศว
              </div>
              <div className="min-w-0 flex-1">
                <div className="text-[11px] text-muted-foreground uppercase tracking-wider">อีเมลผู้ใช้</div>
                <div className="truncate text-xs font-medium text-foreground/90" title={USER_EMAIL}>
                  {USER_EMAIL}
                </div>
              </div>
            </div>
          </div>
        )}
        {collapsed && (
          <div className="border-t border-border/40 p-3 flex justify-center">
            <button
              type="button"
              onClick={() => setCollapsed(false)}
              className="h-9 w-9 rounded-full bg-gradient-to-br from-gold/80 to-gold/50 text-navy flex items-center justify-center text-xs font-bold"
              title="ขยายเมนูเพื่อเปลี่ยนบทบาท"
              aria-label="ขยายเมนู"
            >
              ศว
            </button>
          </div>
        )}
      </aside>
    </>
  );
}
