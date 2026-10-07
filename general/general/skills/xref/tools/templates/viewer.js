// Xref Viewer JavaScript

(function() {
    'use strict';

    let currentPanel = null;

    document.addEventListener('DOMContentLoaded', init);

    function init() {
        setupTabs();
        setupSearch();
        setupInteractiveElements();
        setupKeyboardShortcuts();
        setupNavigation();
        setupGlossary();
    }

    function setupTabs() {
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const tabName = btn.dataset.tab;

                document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
                const tab = document.getElementById(`tab-${tabName}`);
                if (tab) tab.classList.add('active');
            });
        });
    }

    function setupSearch() {
        const searchBox = document.getElementById('search-box');
        const status = document.getElementById('search-status');
        if (!searchBox) return;

        searchBox.addEventListener('input', e => {
            const query = e.target.value.trim().toLowerCase();
            clearSearchMatches();

            if (query.length < 2) {
                if (status) status.textContent = '';
                return;
            }

            const blocks = Array.from(document.querySelectorAll('.document-text p, .document-text h2, .document-text h3, .document-text h4, .document-text h5, .document-text h6'));
            const matches = blocks.filter(block => block.textContent.toLowerCase().includes(query));

            matches.forEach(block => block.classList.add('search-match'));
            if (status) {
                status.textContent = matches.length === 1 ? '1 match' : `${matches.length} matches`;
            }
            if (matches[0]) {
                matches[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });
    }

    function clearSearchMatches() {
        document.querySelectorAll('.search-match').forEach(el => el.classList.remove('search-match'));
    }

    function setupInteractiveElements() {
        document.querySelectorAll('[data-panel-id]').forEach(el => {
            el.addEventListener('mouseenter', handleHover);
            el.addEventListener('mouseleave', handleUnhover);
            el.addEventListener('click', handleClick);
        });

        document.addEventListener('click', e => {
            if (currentPanel &&
                !e.target.closest('.hover-panel') &&
                !e.target.closest('[data-panel-id]')) {
                hidePanel();
            }
        });
    }

    function handleHover(e) {
        const panelId = e.currentTarget.dataset.panelId;
        if (panelId) showPanel(panelId, e.currentTarget);
    }

    function handleUnhover() {
        if (!currentPanel || currentPanel.classList.contains('pinned')) return;

        setTimeout(() => {
            if (currentPanel && !currentPanel.matches(':hover')) {
                hidePanel();
            }
        }, 120);
    }

    function handleClick(e) {
        const panelId = e.currentTarget.dataset.panelId;
        if (!panelId) return;

        e.preventDefault();
        e.stopPropagation();

        if (!currentPanel || currentPanel.id !== panelId) {
            showPanel(panelId, e.currentTarget);
        }
        if (currentPanel) {
            currentPanel.classList.toggle('pinned');
        }
    }

    function showPanel(panelId, anchor) {
        hidePanel();

        const panel = document.getElementById(panelId);
        if (!panel) return;

        currentPanel = panel;
        panel.classList.add('visible');

        const rect = anchor.getBoundingClientRect();
        panel.style.top = `${rect.bottom + 10}px`;
        panel.style.left = `${rect.left}px`;

        requestAnimationFrame(() => {
            const panelRect = panel.getBoundingClientRect();
            if (panelRect.right > window.innerWidth) {
                panel.style.left = `${Math.max(16, window.innerWidth - panelRect.width - 20)}px`;
            }
            if (panelRect.bottom > window.innerHeight) {
                panel.style.top = `${Math.max(16, rect.top - panelRect.height - 10)}px`;
            }
        });
    }

    function hidePanel() {
        if (!currentPanel) return;
        currentPanel.classList.remove('visible', 'pinned');
        currentPanel = null;
    }

    function setupNavigation() {
        document.querySelectorAll('.jump-link, .toc-item a').forEach(link => {
            link.addEventListener('click', e => {
                const target = getHashTarget(link);
                if (!target) return;

                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                target.classList.add('highlight');
                window.history.replaceState(null, '', link.getAttribute('href'));

                setTimeout(() => target.classList.remove('highlight'), 2200);
                hidePanel();
            });
        });
    }

    function getHashTarget(link) {
        const href = link.getAttribute('href');
        if (!href || !href.startsWith('#')) return null;
        return document.getElementById(href.substring(1));
    }

    function setupKeyboardShortcuts() {
        document.addEventListener('keydown', e => {
            if (isTyping(e.target)) return;

            if (e.key === 'Escape') {
                hidePanel();
            } else if (e.key === 'g' && !e.ctrlKey && !e.metaKey) {
                clickTab('glossary');
            } else if (e.key === 'h' && !e.ctrlKey && !e.metaKey) {
                clickTab('health');
            } else if (e.key === 't' && !e.ctrlKey && !e.metaKey) {
                clickTab('toc');
            } else if (e.key === '/' || e.key === 's') {
                e.preventDefault();
                const search = document.getElementById('search-box');
                if (search) search.focus();
            } else if (e.key === 'n' || e.key === 'N') {
                navigateUnresolved(e.key === 'N');
            }
        });
    }

    function isTyping(target) {
        if (!target) return false;
        const tag = target.tagName;
        return tag === 'INPUT' || tag === 'TEXTAREA' || target.isContentEditable;
    }

    function clickTab(tabName) {
        const tab = document.querySelector(`[data-tab="${tabName}"]`);
        if (tab) tab.click();
    }

    function navigateUnresolved(backwards) {
        const unresolved = Array.from(document.querySelectorAll('.broken-reference, .undefined-term, .external-doc-ref'));
        if (!unresolved.length) return;

        const currentIndex = unresolved.findIndex(el => {
            const rect = el.getBoundingClientRect();
            return rect.top >= 0 && rect.top < window.innerHeight;
        });

        let targetIndex;
        if (backwards) {
            targetIndex = currentIndex > 0 ? currentIndex - 1 : unresolved.length - 1;
        } else {
            targetIndex = currentIndex >= 0 && currentIndex < unresolved.length - 1 ? currentIndex + 1 : 0;
        }

        unresolved[targetIndex].scrollIntoView({ behavior: 'smooth', block: 'center' });
        unresolved[targetIndex].classList.add('highlight');
        setTimeout(() => unresolved[targetIndex].classList.remove('highlight'), 2200);
    }

    function setupGlossary() {
        document.querySelectorAll('.glossary-item').forEach(item => {
            item.addEventListener('click', () => {
                const term = item.dataset.term;
                const firstOccurrence = Array.from(document.querySelectorAll('.defined-term'))
                    .find(el => el.dataset.term === term);

                if (!firstOccurrence) return;

                firstOccurrence.scrollIntoView({ behavior: 'smooth', block: 'center' });
                firstOccurrence.classList.add('highlight');
                setTimeout(() => firstOccurrence.classList.remove('highlight'), 2200);
            });
        });
    }
})();
