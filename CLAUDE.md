# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Time Planner is a multilingual (6 languages) time tracking application with an integrated Pomodoro timer and TODO list, built as a Tauri desktop application.

**Supported Languages**: 🇵🇱 Polski (PL), 🇬🇧 English (EN), 🇩🇪 Deutsch (DE), 🇪🇸 Español (ES), 🇮🇹 Italiano (IT), 🇫🇷 Français (FR)

**CRITICAL: Always edit `src/index.html`, NOT `Plan.html`**. The Tauri build system reads from `src/` directory. Plan.html is deprecated legacy file kept for historical reference only.

## Build System & Development Commands

### Common Commands

```bash
# Development mode (with hot reload and DevTools)
npm run dev              # Runs build-minify.js, then tauri dev

# Production build (creates native executable)
npm run build            # Runs build-minify.js, then tauri build

# Manual minification only (without Tauri)
npm run build:minify     # Runs node build-minify.js standalone
```

### Build Pipeline

1. **Source**: `src/index.html` (~320KB unminified)
2. **Process**: `build-minify.js` compresses HTML/CSS/JS via html-minifier-terser
3. **Output**: `src-dist/index.html` (~160KB - 50% reduction)
4. **Assets**: `src/fonts/` → `src-dist/fonts/`, `src/translations/*.json` → `src-dist/translations/`
5. **Tauri reads**: `src-dist/` directory (frontendDist config in tauri.conf.json)

**Important**:
- Build triggers automatically via `beforeDevCommand` and `beforeBuildCommand` in tauri.conf.json
- WSL builds create Linux binaries - use Windows PowerShell/CMD for Windows .exe
- Production builds go to `src-tauri/target/release/bundle/`

## Architecture

### Single-File Application Structure

- **HTML**: Semantic structure with ARIA accessibility attributes
- **CSS**: Embedded styles using CSS custom properties (lines 1-1500)
- **JavaScript**: Vanilla JS, no external dependencies (lines 1500+)
- **Assets**: Local fonts (src/fonts/) and translation files (src/translations/)

### State Management (localStorage)

All application state managed through 8 LocalStorageManager instances:
- `entriesStorage` - Timesheet entries with EntryValidator integration
- `projectsStorage` - Project list
- `taskTypesStorage` - Task type categories
- `sectionVisibilityStorage` - UI section toggle states
- `pomodoroDataStorage` - Timer state and session history
- `pomodoroSettingsStorage` - Timer duration settings
- `todoTasksStorage` - TODO widget tasks
- `widgetLayoutStorage` - Widget position and size

**Key Pattern**: Dual data structures for entries
- `entries` array: Primary data source
- `entriesMap` Map: O(1) lookups by ID
- Call `rebuildEntriesMap()` after modifying `entries` array directly

### Core Modules

**DraggableWidget Class** (lines 2938-3355):
- Unified OOP implementation for widget drag/resize
- Controllers: `pomodoroWidgetController`, `todoWidgetController`
- Features: 8 resize handles, touch support, viewport constraints
- Eliminates ~20 global state variables

**Internationalization System**:
- **Default**: English (EN) embedded in HTML
- **Lazy Loading**: PL/DE/ES/IT/FR load from `src/translations/{lang}.json`
- **Path**: Uses `./translations/${langCode}.json` (explicit `./` required for Tauri)
- **Function**: `t(key, params)` with parameter interpolation and EN fallback
- **Updates**: `updateUILanguage()` applies translations to `data-i18n` elements

**Date/Time Handling**:
- **CRITICAL**: Always use local timezone, never UTC
- Helper functions:
  - `getTodayLocalDate()` - returns "YYYY-MM-DD" in local timezone
  - `getTodayLocalDateObject()` - returns Date object at midnight local time
- Used in: `isOverdue()`, `cloneEntry()`, `resetForm()`, `completeCurrentTask()`, `setupFormHandlers()`
- **Problem**: `new Date().toISOString()` returns UTC which can be wrong day in some timezones

**Security - EntryValidator Class** (lines 2217-2433):
- Validates data types, ranges (hours: 0.5-8), required fields
- Sanitizes all user input: removes HTML tags, enforces length limits
- Used by all CRUD operations and storage managers

### CSV Export

- Uses Tauri native file dialog + `fs.writeTextFile()` API
- **Permissions Required**:
  - `fs:allow-write-text-file` (create files)
  - `fs:allow-truncate` (overwrite existing files)
- **Scope**: $DOWNLOAD, $DOCUMENT, $DESKTOP directories
- **Error Translation**: `translateSystemError()` converts OS errors to user's language

### Widget System

Both Pomodoro and TODO widgets support:
- Drag to reposition anywhere on screen
- Resize from 8 handles (N, S, E, W, NE, NW, SE, SW)
- Minimize to icon in corner
- State persisted across sessions

**Scrollbar Interaction Fix**:
- East resize handles use `pointer-events: none` to allow scrollbar clicks
- Corner handles (NE, SE) use `pointer-events: auto` to preserve resize
- Prevents 8px resize handle from blocking 8px scrollbar

## Code Conventions

- Function naming: camelCase (`addEntry`, `renderProjects`)
- Constants: SCREAMING_SNAKE_CASE (`STORAGE_KEY`, `ENTRIES_LIMIT`)
- CSS classes: kebab-case (`.entry-form`, `.modal-content`)
- Event handlers: Inline delegation preferred over individual listeners

**XSS Prevention - ALWAYS**:
```javascript
// CORRECT - use createElement + textContent
const cell = document.createElement('td');
cell.textContent = entry.taskNumber;
cell.title = entry.taskNumber;

// WRONG - NEVER use innerHTML with user data
// cell.innerHTML = entry.taskNumber; // VULNERABLE
```

## Translation System

### Adding New Translations

1. Add key to ALL 6 files in `src/translations/`: pl.json, en.json, de.json, es.json, it.json, fr.json
2. Update embedded EN translations in src/index.html
3. **Use only ASCII quotes (`"`)** - no typographic quotes („ ")
4. Escape quotes in content with apostrophes: `"Click 'Add' to save"`
5. Validate: `python3 -m json.tool src/translations/{lang}.json`
6. Run `npm run build:minify` to copy to src-dist/
7. Test all 6 languages via dropdown menu

**Translation with parameters**:
```javascript
t("pomodoro.notif.timeAdded", { task: "ABC-123", hours: 2.5 })
// Output: "Time added: ABC-123 (+2.5h)"
```

## Testing Changes

**After editing src/index.html**:
1. Run `npm run build:minify` to update src-dist/
2. Restart dev mode: Ctrl+C, then `npm run dev`
3. Press F12 to open DevTools
4. Test all 6 languages (check Console for "✅ Translations loaded: {lang}")

**Debugging storage**:
```javascript
// In DevTools Console (F12):
localStorage.clear();          // Reset all data
location.reload();            // Reload app
```

## Common Issues

**Changes don't appear in dev mode**:
- Hard refresh: Ctrl+Shift+R
- Run `npm run build:minify` manually
- Restart dev server completely

**Translation showing keys instead of text**:
- Check Console for load errors
- Verify JSON syntax: `python3 -m json.tool file.json`
- Common: typographic quotes („ ") instead of ASCII (")

**CSV export can't overwrite files**:
- Add `fs:allow-truncate` to src-tauri/capabilities/main.json
- Rebuild Tauri app after capability changes

**Date shows yesterday's date**:
- Use `getTodayLocalDate()` instead of `new Date().toISOString().split('T')[0]`
- Always use local timezone helpers, never UTC

**Tauri build creates Linux binaries**:
- Build in Windows PowerShell/CMD, NOT WSL terminal
