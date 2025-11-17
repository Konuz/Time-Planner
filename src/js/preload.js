/**
 * Preload Script - Runs before page render to prevent FOUC
 * Sets initial language, section visibility, and scroll position
 */
(function() {
    'use strict';

    // Initialize language from localStorage
    try {
        const storedLang = localStorage.getItem('app-language');
        const supportedLangs = ['pl', 'en', 'de', 'es', 'it', 'fr'];
        window.__INITIAL_LANG__ = supportedLangs.includes(storedLang) ? storedLang : 'en';
        document.documentElement.lang = window.__INITIAL_LANG__;
    } catch (e) {
        console.warn('Failed to load language from localStorage:', e);
        window.__INITIAL_LANG__ = 'en';
        document.documentElement.lang = 'en';
    }

    // Initialize section visibility from localStorage
    try {
        const storedVisibility = localStorage.getItem('section-visibility');
        if (storedVisibility) {
            window.__SECTION_VISIBILITY__ = JSON.parse(storedVisibility);
        } else {
            window.__SECTION_VISIBILITY__ = {
                'entry-form': true,
                'entries-list': true,
                'summary': true
            };
        }
    } catch (e) {
        console.warn('Failed to load section visibility from localStorage:', e);
        window.__SECTION_VISIBILITY__ = {
            'entry-form': true,
            'entries-list': true,
            'summary': true
        };
    }

    // Initialize scroll position from sessionStorage
    try {
        const storedScroll = sessionStorage.getItem('scrollPosition');
        if (storedScroll) {
            window.__SCROLL_POS__ = JSON.parse(storedScroll);
        } else {
            window.__SCROLL_POS__ = { x: 0, y: 0 };
        }
    } catch (e) {
        console.warn('Failed to load scroll position from sessionStorage:', e);
        window.__SCROLL_POS__ = { x: 0, y: 0 };
    }

    // Save scroll position before page unload
    window.addEventListener('beforeunload', function() {
        try {
            sessionStorage.setItem('scrollPosition', JSON.stringify({
                x: window.scrollX || window.pageXOffset || 0,
                y: window.scrollY || window.pageYOffset || 0
            }));
        } catch (e) {
            console.warn('Failed to save scroll position:', e);
        }
    });
})();
