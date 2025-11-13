# Repository Guidelines

## Project Structure & Module Organization
Time Planner lives entirely in `Plan.html`, which embeds semantic HTML, a 1,200-line CSS block (custom properties handle theming), and a ~2,500-line vanilla JS module. JavaScript is organized by feature sections (entry management, project/task managers, Pomodoro widget, i18n, storage helpers); keep new logic colocated with the closest existing section and rebuild `entriesMap` after mutating `entries`. Use `.claude/` for agent prompt configs and treat `logs/*.log` as read-only telemetry when diagnosing automation runs.

## Build, Test, and Development Commands
- `python3 -m http.server 4173` — serves `Plan.html` for consistent CORS/storage behavior.
- `xdg-open Plan.html` (or `open` on macOS) — quickest manual preview; refresh with `Ctrl+Shift+R` to bust cache.
- `rg --no-heading -n "safeLocalStorageSave" Plan.html` — preferred way to locate shared utilities in the single file.
No bundler or package install is required; keep the file standalone and inlined fonts/assets.

## Coding Style & Naming Conventions
Follow the existing 4-space indentation visible in `<style>` and `<script>` blocks. JavaScript uses camelCase functions (`addEntry`, `renderEntries`), SCREAMING_SNAKE_CASE constants, and module-level `const`/`let` for shared state. CSS classes stay kebab-case, and ARIA/data attributes (`data-i18n`, `role="dialog"`) are mandatory for new UI. Prefer descriptive helper functions over comments; when unavoidable, keep comments high-level and before complex logic.

## Testing Guidelines
There is no automated test suite; rely on manual verification in a browser. Exercise workflows: add/edit/delete entries, switch language between Polish/English, toggle visibility sections, and complete a Pomodoro cycle to ensure automatic entry creation. Inspect `localStorage` keys (`timesheet-entries`, `timesheet-projects`, `timesheet-task-types`, `section-visibility`, `pomodoro-*`) via DevTools > Application. If you adjust storage schemas, document the migration path in your PR and test with both empty and populated storage (clear via `localStorage.removeItem(...)` when needed).

## Commit & Pull Request Guidelines
Recent history (`git log`) shows short, imperative messages, often bilingual; keep the form “Verb object” and reference user-facing language when relevant. Each PR should include: concise summary, testing notes (browser + scenario), screenshots or GIFs for UI deltas, and mention of impacted localStorage keys or translations. Link issues when available and call out any follow-up work so maintainers can triage quickly.

## Local Storage & Safety Tips
Use `safeLocalStorageSave` helpers for persistence to retain debounced writes and quota handling. When touching entry or project data, update both the array source and any derived maps, then call `renderEntries()` and related DOM refreshers to keep pagination and filters aligned. Keep translations in sync by adding keys to both Polish and English dictionaries and invoking `updateUILanguage()` after dynamic changes.
