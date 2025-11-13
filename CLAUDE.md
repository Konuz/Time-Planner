# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Time Planner is a multilingual (6 languages) time tracking application with an integrated Pomodoro timer and TODO list, built as both a standalone HTML file and a Tauri desktop application.

**Dual Architecture**:
- **Standalone HTML**: `Plan.html` - self-contained single-file application (legacy)
- **Tauri Desktop**: `src/index.html` → compiled to native Windows/Linux/macOS executable

**Supported Languages**: Polski (PL), English (EN), Deutsch (DE), Español (ES), Italiano (IT), Français (FR)

## Architecture

### Dual Build System

**Source Architecture** (src/index.html):
- **HTML**: Semantic structure with ARIA accessibility attributes
- **CSS**: Embedded styles using CSS custom properties for theming
- **JavaScript**: Vanilla JS with no external dependencies
- **Assets**: Local fonts (src/fonts/) and translation files (src/translations/)

**Build Output** (src-dist/index.html):
- **Automated Minification**: `build-minify.js` compresses HTML/CSS/JS
- **Size Reduction**: 276,043 bytes → 146,896 bytes (47% reduction)
- **Optimization Settings**:
  - `collapseWhitespace: true` - removes unnecessary whitespace
  - `minifyCSS: true` - compresses embedded CSS
  - `minifyJS: true` - compresses embedded JavaScript
  - `removeComments: true` - strips all HTML/CSS/JS comments
  - `removeAttributeQuotes: true` - removes unnecessary attribute quotes
- **Asset Copying**: Fonts and translations automatically copied to src-dist/

**Legacy Standalone** (Plan.html):
- Single-file HTML application without build process
- Kept for backward compatibility and standalone browser use
- No minification, includes all assets inline

### State Management
All application state is managed through browser localStorage:
- `timesheet-entries`: Work entries with date, task type, project, hours, task number
- `timesheet-projects`: User-defined project list
- `timesheet-task-types`: User-defined task type categories
- `section-visibility`: UI section toggle states
- `pomodoro-data`: Pomodoro timer state and session history
- `pomodoro-settings`: Pomodoro duration settings
- `todo-tasks`: TODO widget task list with priorities and due dates

Key architectural pattern: Dual data structures for entries:
- `entries` array: Primary data source, persisted to localStorage
- `entriesMap` Map: Performance optimization for O(1) lookups by ID
- Call `rebuildEntriesMap()` after any direct modification to `entries` array

### Core Modules

**Entry Management** (lines 3497-3635):
- `addEntry()`, `editEntry()`, `deleteEntry()`: CRUD operations
- `renderEntries()`: Table rendering with pagination (20 entries default)
- `validateForm()`: Multi-field validation with accessibility feedback

**Project/Task Type Management** (lines 3140-3370):
- Generic `createItemManager()` factory pattern for managing lists
- Separate managers: `projectManager`, `taskTypeManager`, `modalProjectManager`
- Each manager handles add/edit/delete with input validation and DOM updates

**Pomodoro Timer** (lines 3894-5460):
- Three modes: work (30min), short break (5min), long break (15min)
- Auto-creates timesheet entries on work session completion
- Draggable/resizable widget with minimize functionality
- Persistent session counting and statistics

**TODO Widget** (lines 4953-5460):
- Priority-based task management (high/medium/low)
- Drag-and-drop reordering within dated/undated sections
- Integration with Pomodoro timer (send task to timer)
- Integration with timesheet (create entry on task completion)
- Draggable/resizable widget with minimize functionality
- Auto-sorting by date for dated tasks

**Internationalization System**:

**6 Supported Languages**:
- 🇵🇱 Polski (PL) - embedded in HTML
- 🇬🇧 English (EN) - embedded in HTML
- 🇩🇪 Deutsch (DE) - lazy loaded
- 🇪🇸 Español (ES) - lazy loaded
- 🇮🇹 Italiano (IT) - lazy loaded
- 🇫🇷 Français (FR) - lazy loaded

**Translation Architecture**:
- **Files**: `src/translations/{lang}.json` - 180+ keys per language
- **Lazy Loading**: `loadTranslations(langCode)` - async fetch with error handling
- **Translation Function**: `t(key, params)` - supports parameter interpolation
  ```javascript
  t("pomodoro.notif.timeAdded", { task: "ABC-123", hours: 2.5 })
  // → "Time added: ABC-123 (+2.5h)" (EN)
  // → "Czas dodany: ABC-123 (+2.5h)" (PL)
  ```
- **Dynamic Updates**: `updateUILanguage()` - applies translations to all `data-i18n` elements
- **Attributes**: `data-i18n="key"` (text content), `data-i18n-title="key"` (title attribute)

**UI Components**:
- **Language Dropdown**: Flag-based selector with animated menu (CSS lines 1446-1557)
- **SUPPORTED_LANGUAGES**: Array of language objects with code, name, and flag emoji
- **Storage**: Current language persisted to `localStorage['app-language']`
- **Fallback**: Falls back to Polish (PL) if translation loading fails

**Translation Loading Flow**:
1. Page loads → Check `localStorage['app-language']` or default to PL
2. PL/EN available immediately (embedded in HTML)
3. User selects DE/ES/IT/FR → `fetch('translations/{lang}.json')`
4. On success: Cache in `translations` object, update UI
5. On error: Log error, fallback to PL, show console warning

**Data Export** (lines 3936-3998):
- CSV export for current month's entries
- Columns: Date, Task Type, Project, Hours, Task Number
- Client-side generation with automatic download

### Security Architecture

**EntryValidator Class** (lines 2217-2433):
- Validates all data types, ranges, and required fields before operations
- `validate()`: Type checking, range validation (hours: 0.25-8), required fields
- `sanitize()`: HTML tag removal, string length limits, XSS prevention
- `sanitizeString()`: Removes all HTML tags using `.replace(/<[^>]*>/g, '')`
- `ValidationError`: Custom error class with context for debugging

**Content Security Policy**:
- **Tauri CSP** (src-tauri/tauri.conf.json): Managed by Tauri for desktop app
  - `connect-src 'self' asset: https://asset.localhost` - allows local file fetching for translations
  - `script-src 'self' 'unsafe-inline'` - only bundled scripts allowed
  - `font-src 'self' data:` - local fonts from src/fonts/
- **HTML CSP** (legacy Plan.html line 7): Meta tag for browser version
  - `connect-src 'none'` - blocks external connections (standalone mode)

**XSS Prevention Pattern**:
```javascript
// NEVER use innerHTML for user data - use createElement + textContent
const cell = document.createElement('td');
cell.textContent = entry.taskNumber; // Safe: textContent escapes HTML
cell.title = entry.taskNumber; // Safe: setAttribute escapes HTML

// WRONG: cell.innerHTML = entry.taskNumber; // VULNERABLE to XSS
```

**Runtime Validation** (all CRUD operations):
- `loadEntries()` (lines 3494-3533): Sanitizes and validates on load, removes invalid entries
- `addEntry()` (lines 4034-4068): Validates before adding, shows ValidationError context
- `editEntry()` (lines 4096-4131): Validates before updating entry
- Console warnings for invalid entries: `⚠️ Invalid entry removed from localStorage`

**Sanitization Strategy**:
- All user input sanitized before storage: projects, taskTypes, entries
- HTML tags stripped from all text fields
- Validation on both UI (form validation) and runtime (EntryValidator)

### Storage Architecture

**Safe Storage Pattern** (lines 2857-2897):
- `safeLocalStorageSave()`: Debounced saves (300ms) with quota exceeded handling
- Error recovery: Shows user-friendly alerts on storage failures
- Individual save timers per storage key to prevent save collisions

**Data Loading Pattern**:
1. Load from localStorage or use defaults
2. **Sanitize and validate** all loaded data (EntryValidator)
3. Rebuild in-memory indexes (entriesMap)
4. Update DOM elements (selects, tables, filters)
5. Restore UI state (section visibility, language)

### DOM Optimization

**DOM Caching** (lines 2336-2463):
- `domCache` object stores frequently accessed elements
- `initDOMCache()` called once on app initialization
- Reduces repeated DOM queries for better performance
- Always cache before using `getElementById()` or `querySelector()` in frequently called functions
- Add new elements to cache when adding repetitive DOM access patterns

## Key Implementation Details

### Entry Filtering System
Multi-dimensional filtering with independent toggles:
- Month filter: Show only current month entries
- Week filter: Show only current week entries
- Task type filter: Multi-select checkboxes (all task types)
- All filters work together via `renderEntries()` which applies all active filters

### Pomodoro Integration
Work sessions automatically create timesheet entries:
- Uses same project/task type from timer settings
- Accumulates hours across multiple pomodoros for same task number
- Updates existing entry if task number matches, creates new otherwise

### TODO Widget Integration
Tasks can be integrated with other features:
- **Complete task**: Option to create timesheet entry automatically
- **Move to Pomodoro**: Sends task description to timer's task number field
- **Drag & Drop**: Reorder tasks within sections
- **Overdue indicator**: Visual warning for tasks past due date

### Form Validation Strategy
Multi-field validation with real-time feedback:
- Date: Required, must be valid date
- Task type: Required selection
- Project: Required selection
- Hours: Required, numeric, 0.25-8 range
- Task number: Required, non-empty string

Invalid fields show:
- Red border via `.is-invalid` class
- Error message via `.invalid-feedback` element
- ARIA live region announcements for accessibility

### Section Toggle System
Three main sections can be hidden/shown:
- Entry form (`section-entry-form`)
- Entries list (`section-entries-list`)
- Summary (`section-summary`)

State persisted to localStorage and restored on page load.

### Widget Layout System
Both Pomodoro and TODO widgets support:
- Drag to reposition anywhere on screen
- Resize from 8 handles (N, S, E, W, NE, NW, SE, SW)
- Minimize to icon in corner
- Position/size constrained to viewport boundaries
- State persisted across sessions

**Critical Implementation Detail - Scrollbar Interaction**:
- East resize handles (`.resize-handle-e`) use `pointer-events: none` to allow scrollbar interaction
- Corner handles (NE, SE) use `pointer-events: auto` to preserve resize functionality
- This prevents the 8px-wide resize handle from blocking the 8px-wide scrollbar
- All scrollbar CSS is unified in lines 1461-1496 to avoid duplication

## Build System & Development Workflow

### Tauri Desktop Application

**Build Pipeline** (automated minification):
1. **Source**: `src/index.html` (276KB unminified)
2. **Process**: `build-minify.js` - HTML/CSS/JS compression via html-minifier-terser
3. **Output**: `src-dist/index.html` (147KB - 47% reduction)
4. **Assets Copied**: `src/fonts/` → `src-dist/fonts/`, `src/translations/` → `src-dist/translations/`

**Common Commands**:
```bash
# Development mode (with auto-rebuild on changes)
npm run dev              # Runs build-minify.js, then tauri dev
npm run tauri:dev        # Alias for above

# Production build (creates native executable)
npm run build            # Runs build-minify.js, then tauri build
npm run tauri:build      # Alias for above

# Manual minification only (without Tauri)
npm run build:minify     # Runs build-minify.js standalone
```

**Output Locations**:
- **Development**: Opens app window with DevTools support (F12 enabled via `withGlobalTauri: true`)
- **Production Build**: `src-tauri/target/release/bundle/`
  - Windows: `time-planner.exe` (~12-15MB with embedded WebView2 bootstrapper)
  - Linux: `.deb`, `.rpm`, `.AppImage` packages
  - macOS: `.app` and `.dmg` files

**Build Configuration**:
- `src-tauri/tauri.conf.json`: Window settings, CSP policy, bundle configuration
- `src-tauri/Cargo.toml`: Rust dependencies, optimization flags (strip, LTO, opt-level="z")
- `package.json`: npm scripts and dependencies

**Important Notes**:
- **WSL Build = Linux binaries**: Build in Windows PowerShell for Windows `.exe`
- **Single Instance**: Plugin prevents multiple windows (focuses existing window)
- **Offline Ready**: All assets bundled, no external dependencies (local fonts, no CDN)
- **File Export Permissions**: CSV export configured for $DOWNLOAD, $DOCUMENT, $DESKTOP directories

### Testing Changes

**Standalone HTML** (legacy):
1. Open `Plan.html` directly in browser (no build step required)
2. Open browser DevTools console for debugging
3. Check localStorage in Application tab for state inspection
4. Test all 6 language modes (PL, EN, DE, ES, IT, FR)

**Tauri Application**:
1. Run `npm run dev` to start development mode with hot reload
2. Press F12 to open DevTools in Tauri window
3. Test native features: window controls, file system access, single instance
4. Verify minification: Check `src-dist/index.html` size reduction
5. Test all 6 languages with lazy loading (check Console for "✅ Translations loaded")

### Debugging Storage Issues
```javascript
// Clear all app data
localStorage.removeItem('timesheet-entries');
localStorage.removeItem('timesheet-projects');
localStorage.removeItem('timesheet-task-types');
localStorage.removeItem('pomodoro-data');
localStorage.removeItem('pomodoro-settings');
localStorage.removeItem('section-visibility');
localStorage.removeItem('app-language');
localStorage.removeItem('todo-tasks');
```

### Adding New Translations
1. Add translation key to ALL 6 language files in `src/translations/`:
   - `pl.json` (Polski)
   - `en.json` (English)
   - `de.json` (Deutsch)
   - `es.json` (Español)
   - `it.json` (Italiano)
   - `fr.json` (Français)
2. Add `data-i18n="key"` or `data-i18n-title="key"` attribute to HTML element
3. Call `updateUILanguage()` if adding dynamically
4. Test all languages: Dropdown menu allows switching between all 6 languages
5. Verify lazy loading: Check browser Console for "✅ Translations loaded: {lang}"

**Translation File Structure**:
```json
{
  "app.title": "TIME PLANNER",
  "app.settings": "Settings",
  "pomodoro.notif.workComplete": "Work time complete! Time for a break."
}
```

**Parameter Interpolation**:
```javascript
// Translation with parameters: "Time added: {task} (+{hours}h)"
t("pomodoro.notif.timeAdded", { task: "ABC-123", hours: 2.5 })
// Output: "Time added: ABC-123 (+2.5h)"
```

### Modifying Storage Schema
When changing data structures:
1. Update storage key loading function (e.g., `loadEntries()`)
2. Update corresponding save function (e.g., `saveEntries()`)
3. Consider migration logic for existing users' data
4. Test with both empty and populated localStorage

## Code Conventions

- Function naming: camelCase (`addEntry`, `renderProjects`)
- Constants: SCREAMING_SNAKE_CASE (`STORAGE_KEY`, `ENTRIES_LIMIT`)
- Global state: Module-level variables at top of script section
- CSS classes: kebab-case (`.entry-form`, `.modal-content`)
- Event handlers: Inline delegation preferred over individual listeners
- Comments: Minimal, only for complex logic, security, and performance optimizations

**CSS Organization**:
- Unified scrollbar styles (lines 1461-1496) for `.pomodoro-content`, `.todo-content`, `.info-modal-body`, `.modal-body`
- Custom properties for theming: `--primary-color`, `--bg-light`, `--border-color`, etc.
- Avoid duplicating scrollbar CSS - use the unified selectors
- Avoid unnecessary `!important` declarations except for preload overrides

## Security Best Practices

**CRITICAL: XSS Prevention**
1. **NEVER use innerHTML with user data** - always use `createElement()` + `textContent`
2. **Always sanitize localStorage data** - use `EntryValidator.sanitize()` before rendering
3. **Validate all inputs** - both UI validation AND runtime validation with EntryValidator
4. **Use title attribute for tooltips** - safe alternative to dynamic HTML

**When Adding New Features**:
1. Add validation rules to `EntryValidator.validate()` if new fields added
2. Use `createElement()` pattern for all DOM manipulation with user data
3. Sanitize new localStorage keys in their load functions
4. Test with XSS payloads: `<script>alert('XSS')</script>`, `<img src=x onerror=alert('XSS')>`

**Code Review Checklist**:
- [ ] No innerHTML with user data
- [ ] All user input validated with EntryValidator
- [ ] All localStorage loads use sanitize()
- [ ] New DOM elements use createElement() + textContent
- [ ] Tooltips added for long text fields (cell.title = text)

## Accessibility Features

- Semantic HTML structure with proper heading hierarchy
- ARIA labels and roles throughout (`role="dialog"`, `aria-live="polite"`)
- Keyboard navigation support (Tab, Enter, Escape)
- Screen reader announcements for dynamic content updates
- Focus management for modals and interactive elements
- Tooltips for long text fields: All table cells with text content have `title` attribute for hover preview

## Recent Major Changes

### v1.0.3 (2025-11-13) - Tauri Build System + 6 Languages
**Build Pipeline**:
- Added automated HTML/CSS/JS minification (47% size reduction: 276KB → 147KB)
- Integrated `build-minify.js` with Tauri `beforeDevCommand` and `beforeBuildCommand`
- Created `src-dist/` output directory with minified assets

**Internationalization Expansion**:
- Expanded from 2 languages (PL, EN) to 6 languages (PL, EN, DE, ES, IT, FR)
- Implemented lazy loading system: only PL/EN embedded, DE/ES/IT/FR loaded on demand
- Created 6 JSON translation files in `src/translations/` (180+ keys each)
- Replaced 2-state button with dropdown language selector (flags + language names)
- Added CSS animations and ARIA accessibility for dropdown menu

**Enhanced File System Permissions**:
- Added `fs:allow-write-text-file` and `fs:allow-truncate` capabilities
- Extended fs:scope for CSV export to $DOWNLOAD, $DOCUMENT, $DESKTOP directories

**UI/UX Improvements**:
- Standardized border-radius to 8px across all components
- Enhanced task type dropdown styling with flexbox and hover effects
- Improved button typography (14px → 16px font-size, font-weight: 600)

### v1.0.0 (2025-11-11) - Security Hardening
**Priority 1 XSS Fixes Implemented:**
1. Added `EntryValidator` class with comprehensive validation and sanitization
2. Implemented Content Security Policy (CSP) meta tag
3. Fixed 3 critical XSS vulnerabilities in `createEntryRow()`, `renderItemsList()`, `renderTaskTypeFilters()`
4. Added runtime validation to all CRUD operations
5. Implemented sanitization for projects and taskTypes from localStorage
6. Fixed tooltip functionality for all table columns (taskType, client, taskNumber)

**Backup Files**:
- `Plan-backup-2025-11-11.html`: Pre-security-fixes version

**Breaking Changes**: None - all changes are backward compatible with existing localStorage data

## Testing & Quality Assurance

**Manual Testing**:
1. Open Plan.html directly in browser (no build step)
2. Test both Polish (PL) and English (EN) language modes
3. Verify localStorage persistence across page reloads
4. Test XSS protection with malicious payloads (see Security section)

**Security Testing**:
- Test XSS payloads in all input fields (taskNumber, project names, task types)
- Test localStorage manipulation: inject invalid data and verify sanitization on reload
- Check console for validation warnings: `⚠️ Invalid entry removed from localStorage`
- Verify CSP errors are limited to known false-positive: `frame-ancestors` meta tag limitation

**Regression Testing Checklist**:
- [ ] Add/Edit/Clone/Delete entries work correctly
- [ ] Form validation shows errors for invalid data (hours >8, empty fields)
- [ ] Language switching (all 6 languages) updates all UI elements
- [ ] Language dropdown shows flags and language names correctly
- [ ] Lazy loading works: DE/ES/IT/FR load on first selection (check Console)
- [ ] Filters work (month, week, task type multi-select)
- [ ] Summary calculates total hours correctly
- [ ] Pomodoro timer creates timesheet entries
- [ ] TODO widget integrates with Pomodoro and timesheet
- [ ] CSV export generates correct file (test file permissions in Tauri)
- [ ] Tooltips show full text on hover for long entries
- [ ] Tauri build: Single instance works (2nd launch focuses existing window)
- [ ] Tauri build: DevTools (F12) opens correctly
- [ ] Minification: Verify 47% size reduction in src-dist/

**Test Files**:
- `SECURITY_TEST_REPORT.md`: Comprehensive security test results
- `test_security.py`: Automated Playwright security tests (requires Python + Playwright)
