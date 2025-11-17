# Time Planner - Design System & UI Style Guide

Przewodnik po systemie designu aplikacji Time Planner. Wszystkie nowe funkcje muszą przestrzegać tych zasad dla zachowania spójności wizualnej.

---

## 1. Paleta Kolorów

### Kolory Główne (Primary)
```css
--primary-color: #1976d2;      /* Główny niebieski - przyciski, akcenty */
--primary-dark: #1565c0;       /* Ciemniejszy niebieski - hover states */
--primary-light: #2196F3;      /* Jaśniejszy niebieski - subtle highlights */
```

**Użycie**:
- Główne przyciski (Add Entry, Apply)
- Nagłówki (h1)
- Focus states na inputach
- Linki i elementy interaktywne

### Kolory Semantyczne

**Sukces (Success)**:
```css
--success-color: #28a745;      /* Standardowy zielony */
--success-dark: #218838;       /* Hover state */
--success-light: #51cf66;      /* Gradient start */
--success-lighter: #37b24d;    /* Gradient end */
```
**Użycie**: Potwierdzenia, przyciski "Complete Task", pozytywne akcje

**Błąd (Error)**:
```css
--error-color: #dc3545;        /* Czerwony - błędy, delete */
```
**Użycie**: Komunikaty błędów, przyciski usuwania, walidacja formularzy

**Ostrzeżenie (Warning)**:
```css
--warning-color: #fab005;      /* Złoty/żółty */
--warning-light: #ffd43b;      /* Jaśniejszy wariant */
```
**Użycie**: Pause button, ostrzeżenia, powiadomienia wymagające uwagi

**Neutralne (Secondary)**:
```css
--secondary-color: #6c757d;    /* Szary */
--secondary-dark: #5a6268;     /* Ciemniejszy szary */
```
**Użycie**: Reset button, Cancel, opcjonalne akcje, przyciski drugoplanowe

### Kolory Tła (Background)

```css
--bg-dark: #1e1e1e;           /* Najciemniejsze tło (body fallback) */
--bg-medium: #2d2d2d;         /* Średnie tło */
--bg-light: #222222;          /* Główne tło (body) */
--bg-lighter: #303030;        /* Container, karty */
--bg-highlight: #292929;      /* Wyróżnione sekcje, table headers */
```

**Hierarchia**:
1. `bg-light` - tło body
2. `bg-lighter` - główny container
3. `bg-light` - sekcje wewnętrzne (formularze, filtry)
4. `bg-highlight` - wyróżnienia (table headers, hover states)

### Kolory Tekstu

```css
--text-color: #797979;        /* Główny kolor tekstu (szary) */
--text-light: #fff;           /* Biały tekst na ciemnych przyciskach */
```

### Kolory Ramek

```css
--border-color: #5f5f5f;      /* Standardowy kolor ramki */
```

**Użycie**: Inputy, tabele, separatory, obramowania widgetów

---

## 2. Typografia

### Rodzina Czcionek

**Podstawowa czcionka systemowa**:
```css
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
```

**Czcionka Pomodoro Widget (custom)**:
```css
font-family: 'Orbitron', monospace;  /* Tylko dla licznika timera */
```

### Rozmiary Czcionek

| Element | Rozmiar | Waga | Użycie |
|---------|---------|------|--------|
| h1 | default | 700 | Główny tytuł aplikacji |
| h2 | 24px | 500 | Tytuły sekcji (Settings, Summary) |
| h3 | 18px | 500 | Podtytuły sekcji (modal headers) |
| body | 16px | normal | Standardowy tekst |
| button | 16px | 600 | Przyciski główne |
| timer-btn | 13px | 600 | Przyciski w widgetach |
| table | 14px | normal | Tekst w tabelach |
| label | default | 600 | Etykiety formularzy |
| small text | 12px | normal | Pomocniczy tekst, etykiety w widgetach |

### Line Height

```css
line-height: 1.6;  /* Standardowa wysokość linii dla całej aplikacji */
```

---

## 3. Spacing (Odstępy)

### System 8px Grid

Wszystkie marginesy, paddingi i gappy używają wielokrotności **8px** (4px dla małych odstępów):

| Nazwa | Wartość | Użycie |
|-------|---------|--------|
| xs | 4px | Małe odstępy w widgetach |
| sm | 8px | Standardowe gappy między elementami |
| md | 12px | Padding w inputach, button padding |
| lg | 16px | Sekcje, margin-bottom głównych bloków |
| xl | 20px | Padding w formularzu, container padding |
| 2xl | 25px | Container padding top/bottom |
| 3xl | 30px | Header margin-bottom |
| 4xl | 40px | Duże odstępy między sekcjami |

### Konkretne Zastosowania

**Container**:
```css
padding: 25px;
max-width: 1000px;
margin: 0 auto;
```

**Formularze**:
```css
.form-group { margin-bottom: 20px; }
.entry-form { padding: 20px; }
label { margin-bottom: 8px; }
```

**Przyciski**:
```css
padding: 12px 20px;     /* Standardowe przyciski */
padding: 10px;          /* Timer buttons (widgety) */
gap: 10px;              /* .btn-group */
gap: 8px;               /* Timer controls, flexbox buttons */
```

**Tabele**:
```css
th, td { padding: 8px 10px; }
```

**Widgety (Pomodoro/TODO)**:
```css
padding: 16px;               /* Widget content */
gap: 8px;                    /* Między przyciskami */
margin-bottom: 16px;         /* Sekcje wewnętrzne */
```

---

## 4. Border Radius

### Standardowe Promienie

```css
--border-radius: 4px;        /* Mały radius (container, headers) */
border-radius: 8px;          /* Standardowy (przyciski, inputy, karty) */
border-radius: 12px;         /* Większy (widgety, modals) */
border-radius: 50%;          /* Okrągłe elementy (minimize buttons) */
```

### Zasady Stosowania

| Element | Radius | Powód |
|---------|--------|-------|
| Container główny | 4px | Subtelne zaokrąglenie |
| Buttons, Inputs | 8px | Standardowy, przyjazny wygląd |
| Widgets (Pomodoro, TODO) | 12px | Wyróżnienie jako osobne komponenty |
| Modals | 12px | Podobnie jak widgety |
| Icons (minimize) | 50% | Okrągłe przyciski |

---

## 5. Cienie (Shadows)

### Standardowy Cień

```css
--shadow: 0 0 10px rgba(0, 0, 0, 0.1);
```

**Użycie**:
- Container główny
- Tabele
- Modals
- Widgety (Pomodoro, TODO)

### Cień Focus State

```css
box-shadow: 0 0 0 3px rgba(25, 118, 210, 0.25);  /* Primary color z alpha */
```

**Użycie**: Focus na inputach i select elementach

---

## 6. Transitions & Animations

### Standardowy Transition

```css
--transition: all 0.3s ease;
transition: var(--transition);
```

**Użycie**: Większość interaktywnych elementów (buttons, inputs, links)

### Specyficzne Transitions

```css
/* Buttons hover - natychmiastowa zmiana opacity */
transition: opacity 0.2s ease;

/* Background transitions */
transition: background 0.2s ease;

/* Widget resize handle hover */
transition: background-color 0.2s ease;
```

### Animacje

**Language Dropdown**:
```css
@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
animation: slideDown 0.2s ease-out;
```

---

## 7. Przyciski (Buttons)

### Podstawowy Styl

```css
button {
    background-color: var(--primary-color);
    color: var(--text-light);
    border: none;
    padding: 12px 20px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
    font-weight: 600;
    transition: var(--transition);
    flex: 1;  /* W .btn-group */
}

button:hover {
    background-color: var(--primary-dark);
}
```

### Warianty Przycisków

**Primary** (domyślny):
```css
background-color: var(--primary-color);
color: var(--text-light);
```

**Success** (zielony):
```css
background: #28a745;
color: white;
```
Użycie: Complete Task (✓), Apply, Submit

**Secondary** (szary):
```css
background: linear-gradient(135deg, #868e96 0%, #495057 100%);
color: white;
```
Użycie: Reset, Cancel, New Task

**Error/Danger** (czerwony):
```css
background-color: var(--error-color);
color: var(--text-light);
```
Użycie: Delete, Remove All

**Warning** (żółty):
```css
background: linear-gradient(135deg, var(--warning-light) 0%, var(--warning-color) 100%);
color: var(--bg-dark);
```
Użycie: Pause

### Przyciski w Widgetach (Timer Buttons)

```css
.timer-btn {
    padding: 10px;
    font-size: 13px;
    font-weight: 600;
    flex: 1;
}
```

**Gradient Buttons** (Start, Pause):
```css
/* Start (zielony gradient) */
background: linear-gradient(135deg, var(--success-light) 0%, var(--success-lighter) 100%);

/* Pause (żółty gradient) */
background: linear-gradient(135deg, var(--warning-light) 0%, var(--warning-color) 100%);
```

### Hover & Active States

```css
button:hover {
    background-color: var(--primary-dark);
    /* LUB dla gradientów: */
    opacity: 0.9;
}

button:active {
    opacity: 0.8;
}
```

### Icon Buttons

**Minimize/Maximize** (widgety):
```css
width: 24px;
height: 24px;
border-radius: 50%;
background: rgba(255, 255, 255, 0.1);
font-size: 18px;
padding: 0;
```

**Action Buttons** (Edit, Clone, Delete):
```css
padding: 4px 8px;
font-size: 11px;
margin-right: 4px;
```

---

## 8. Formularze (Inputs & Selects)

### Podstawowy Styl

```css
input, select {
    width: 100%;
    padding: 12px;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    font-size: 16px;
    transition: var(--transition);
}

input:focus, select:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(25, 118, 210, 0.25);
}
```

### Warianty

**Date Input**:
```css
color-scheme: dark;  /* Dark calendar picker w ciemnym motywie */
```

**Select Dropdown**:
```css
background-color: var(--bg-light);
color: var(--text-color);
cursor: pointer;
```

**Checkbox**:
```css
input[type="checkbox"] {
    width: auto;
    margin-right: 8px;
}
```

### Walidacja (Validation States)

**Błąd**:
```css
.is-invalid {
    border-color: var(--error-color) !important;
    box-shadow: 0 0 0 3px rgba(220, 53, 69, 0.25) !important;
}
```

**Komunikat błędu**:
```css
.invalid-feedback {
    color: var(--error-color);
    font-size: 14px;
    margin-top: 4px;
    display: none;
}

.is-invalid ~ .invalid-feedback {
    display: block;
}
```

### Labels

```css
label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: var(--text-color);
}
```

---

## 9. Tabele (Tables)

### Podstawowy Styl

```css
table {
    width: 100%;
    border-collapse: collapse;
    box-shadow: var(--shadow);
    font-size: 14px;
}

th, td {
    padding: 8px 10px;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

th {
    background-color: var(--bg-highlight);
    font-weight: 600;
    color: var(--text-color);
}
```

### Kolumny Tabeli (task-table)

| Kolumna | Szerokość | Zawartość |
|---------|-----------|-----------|
| Data | 10% | yyyy-mm-dd |
| Rodzaj zadania | 18% | Task type |
| Projekt | 18% | Project name |
| Godziny | 8% | Hours (0.5-8) |
| Numer/Nazwa | 16% | Task ID |
| Akcje | 30% | Edit/Clone/Delete buttons |

### Hover State

```css
tbody tr:hover {
    background-color: var(--bg-highlight);
}
```

### Tooltips

```css
td {
    title: [full text content];  /* Dla długich tekstów */
}
```

---

## 10. Widgety (Pomodoro & TODO)

### Podstawowa Struktura

```css
.pomodoro-widget, .todo-widget {
    position: fixed;
    width: 320px;
    background-color: var(--bg-lighter);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    box-shadow: var(--shadow);
    z-index: 1000;
    resize: both;
    overflow: hidden;
}
```

### Header Widgetu

```css
.pomodoro-header, .todo-header {
    background: var(--bg-highlight);
    padding: 12px 16px;
    border-bottom: 1px solid var(--border-color);
    cursor: move;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.widget-title {
    font-size: 14px;
    font-weight: 700;
    color: var(--text-color);
}
```

### Zawartość Widgetu

```css
.pomodoro-content, .todo-content {
    padding: 16px;
    max-height: 500px;
    overflow-y: auto;
}
```

### Scrollbar (Custom)

```css
.pomodoro-content::-webkit-scrollbar,
.todo-content::-webkit-scrollbar {
    width: 8px;
}

.pomodoro-content::-webkit-scrollbar-track,
.todo-content::-webkit-scrollbar-track {
    background: var(--bg-light);
}

.pomodoro-content::-webkit-scrollbar-thumb,
.todo-content::-webkit-scrollbar-thumb {
    background: var(--border-color);
    border-radius: 4px;
}

.pomodoro-content::-webkit-scrollbar-thumb:hover,
.todo-content::-webkit-scrollbar-thumb:hover {
    background: #757575;
}
```

### Resize Handles

```css
.resize-handle {
    position: absolute;
    background-color: transparent;
    transition: background-color 0.2s ease;
}

.resize-handle:hover {
    background-color: rgba(25, 118, 210, 0.3);  /* Primary color z alpha */
}

/* Rozmiary handle'i */
.resize-handle-n, .resize-handle-s { height: 8px; width: 100%; }
.resize-handle-e, .resize-handle-w { width: 8px; height: 100%; }
.resize-handle-ne, .resize-handle-nw,
.resize-handle-se, .resize-handle-sw { width: 16px; height: 16px; }
```

### Minimized State

```css
.pomodoro-minimized, .todo-minimized {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: var(--bg-lighter);
    border: 2px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    cursor: pointer;
    box-shadow: var(--shadow);
    z-index: 999;
}
```

---

## 11. Modals (Okna Modalne)

### Struktura

```css
.modal {
    display: none;
    position: fixed;
    z-index: 2000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6);  /* Semi-transparent overlay */
}

.modal-content {
    background-color: var(--bg-lighter);
    margin: 5% auto;
    padding: 0;
    border: 1px solid var(--border-color);
    border-radius: 12px;
    width: 90%;
    max-width: 600px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}
```

### Modal Header

```css
.modal-header {
    background-color: var(--bg-highlight);
    padding: 16px 20px;
    border-bottom: 1px solid var(--border-color);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.modal-header h2 {
    margin: 0;
    font-size: 24px;
    color: var(--text-color);
}
```

### Modal Body

```css
.modal-body {
    padding: 20px;
    max-height: 60vh;
    overflow-y: auto;
}
```

### Close Button (×)

```css
.close {
    color: var(--text-color);
    font-size: 32px;
    font-weight: bold;
    cursor: pointer;
    background: none;
    border: none;
    padding: 0;
    line-height: 1;
}

.close:hover {
    color: var(--text-light);
}
```

---

## 12. Ikony & Emoji

### Używane Emoji

| Emoji | Znaczenie | Gdzie używane |
|-------|-----------|---------------|
| 🍅 | Pomodoro timer | Widget icon, session counter |
| 📋 | TODO list | Widget icon |
| ⚙️ | Settings | Settings button, modal header |
| ℹ️ | Information | Info/Help button |
| 🗑️ | Delete | Delete all button |
| ✓ | Complete/Success | Complete task button |
| ✕ | Cancel | Cancel task in TODO |
| → | Send to Pomodoro | TODO to Pomodoro button |
| − | Minimize | Widget minimize button |
| ○ | Empty session | Pomodoro session indicator |

### Rozmiary Emoji

```css
/* Widget icons (minimized state) */
font-size: 24px;

/* Header icons */
font-size: 18px;

/* Inline icons (przyciski) */
font-size: inherit;
```

---

## 13. Language Dropdown

### Struktura

```css
.language-selector {
    position: relative;
    display: inline-block;
}

.language-btn {
    background: var(--bg-highlight);
    border: 1px solid var(--border-color);
    padding: 6px 12px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.language-dropdown {
    position: absolute;
    top: calc(100% + 4px);
    right: 0;
    background: var(--bg-lighter);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    min-width: 180px;
    z-index: 1000;
    animation: slideDown 0.2s ease-out;
}

.language-option {
    padding: 10px 16px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
}

.language-option:hover {
    background: var(--bg-highlight);
}

.language-option.active {
    background: var(--primary-color);
    color: var(--text-light);
}
```

---

## 14. Accessibility (Dostępność)

### ARIA Attributes

**Zawsze używaj**:
```html
<button aria-label="Opis akcji">Icon</button>
<div role="button" tabindex="0" aria-label="Opis">...</div>
<div role="status" aria-live="polite">Powiadomienie</div>
<div role="group" aria-label="Grupa kontrolek">...</div>
```

### Focus States

**Wszystkie interaktywne elementy muszą mieć widoczny focus**:
```css
element:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(25, 118, 210, 0.25);
}
```

### Keyboard Navigation

- Tab - przechodzenie między elementami
- Enter - aktywacja przycisków/linków
- Escape - zamykanie modali/dropdownów
- Arrow keys - nawigacja w listach (TODO drag-drop)

### Screen Reader Support

```html
<!-- Ukrywanie wizualne, ale dostępne dla czytników -->
<span class="sr-only">Tekst dla czytników ekranu</span>

<!-- Dynamiczne powiadomienia -->
<div aria-live="polite" aria-atomic="true">
    Wpis został dodany
</div>
```

---

## 15. Responsive Design

### Breakpoints

Aplikacja dostosowuje się do szerokości ekranu:

```css
/* Mobile - brak specjalnych reguł, podstawowy layout */

/* Tablet & Desktop */
@media (min-width: 768px) {
    /* Zwiększone odstępy, więcej kolumn w gridzie */
}

/* Desktop */
@media (min-width: 1024px) {
    /* Pełna szerokość containerów */
}
```

### Container Constraints

```css
max-width: 1000px;  /* Container główny */
min-width: 800px;   /* Okno Tauri (desktop) */
```

### Widgety - Minimum Sizes

```css
/* Pomodoro Widget */
min-width: 280px;
min-height: 200px;

/* TODO Widget */
min-width: 280px;
min-height: 200px;
```

---

## 16. Zasady Implementacji Nowych Funkcji

### ✅ DO (Zawsze stosuj)

1. **Kolory**:
   - Używaj CSS custom properties (`var(--primary-color)`)
   - NIE twórz nowych kolorów bez uzasadnienia
   - Gradient tylko dla przycisków akcji (Start, Pause)

2. **Spacing**:
   - Wielokrotności 8px (lub 4px dla małych odstępów)
   - Używaj konsystentnych wartości: 8px, 12px, 16px, 20px

3. **Border Radius**:
   - 8px - standardowy (przyciski, inputy)
   - 12px - widgety i modals
   - 4px - container główny

4. **Typography**:
   - 16px dla głównych elementów UI
   - 14px dla tabel i secondary text
   - 13px dla przycisków w widgetach
   - Font weight: 600 dla przycisków i labels

5. **Transitions**:
   - Używaj `var(--transition)` jako domyślnego
   - 0.2s dla szybkich animacji (hover, opacity)
   - 0.3s dla standardowych przejść

6. **Accessibility**:
   - Zawsze dodawaj `aria-label` do ikon i action buttons
   - Focus states muszą być widoczne
   - Keyboard navigation dla wszystkich interaktywnych elementów

### ❌ DON'T (Unikaj)

1. NIE używaj inline styles (tylko w wyjątkowych przypadkach jak `style="display: none"`)
2. NIE twórz własnych wariantów kolorów bez uzasadnienia
3. NIE używaj hardcoded wartości - używaj CSS variables
4. NIE ignoruj accessibility (ARIA, keyboard support)
5. NIE łam hierarchii kolorów tła (bg-light → bg-lighter → bg-light → bg-highlight)
6. NIE używaj różnych font-family (tylko Segoe UI + Orbitron dla timera)

---

## 17. Przykłady Implementacji

### Nowy Przycisk

```html
<button class="btn-primary" aria-label="Dodaj wpis">
    Dodaj wpis
</button>
```

```css
.btn-primary {
    background-color: var(--primary-color);
    color: var(--text-light);
    border: none;
    padding: 12px 20px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: var(--transition);
}

.btn-primary:hover {
    background-color: var(--primary-dark);
}
```

### Nowy Input

```html
<div class="form-group">
    <label for="new-field">Nazwa pola:</label>
    <input type="text" id="new-field" aria-label="Nazwa pola">
    <div class="invalid-feedback">To pole jest wymagane</div>
</div>
```

```css
/* Używa globalnych stylów input - tylko dodaj specyficzne reguły jeśli potrzebne */
```

### Nowa Sekcja

```html
<section class="new-section">
    <h2>Tytuł Sekcji</h2>
    <div class="section-content">
        <!-- Zawartość -->
    </div>
</section>
```

```css
.new-section {
    background-color: var(--bg-light);
    padding: 20px;
    border-radius: var(--border-radius);
    margin-bottom: 16px;
}

.new-section h2 {
    font-size: 24px;
    font-weight: 500;
    margin-bottom: 16px;
    color: var(--text-color);
}
```

---

## 18. Checklist dla Nowych Funkcji

Przed zatwierdzeniem zmian sprawdź:

- [ ] Używam CSS custom properties dla kolorów
- [ ] Spacing jest wielokrotnością 8px (lub 4px)
- [ ] Border radius: 8px (standard) lub 12px (widgety/modals)
- [ ] Dodałem aria-label do wszystkich ikon i action buttons
- [ ] Focus states są widoczne i używają primary color
- [ ] Transitions używają `var(--transition)` lub 0.2s
- [ ] Font size: 16px (UI), 14px (tabele), 13px (widget buttons)
- [ ] Font weight: 600 (przyciski, labels), normal (tekst)
- [ ] Hover states zmieniają kolor/opacity
- [ ] Keyboard navigation działa poprawnie
- [ ] Nowe tłumaczenia dodane do wszystkich 6 języków
- [ ] JSON tłumaczeń zwalidowany (`python3 -m json.tool`)
- [ ] Kod zminifikowany (`npm run build:minify`)

---

## 19. Narzędzia Deweloperskie

### Walidacja Kolorów

```bash
# Sprawdź czy używasz tylko zdefiniowanych kolorów
grep -E "#[0-9a-fA-F]{3,6}" src/index.html
# Powinny być tylko w sekcji :root i wyjątkowych przypadkach
```

### Walidacja JSON Tłumaczeń

```bash
# Sprawdź wszystkie pliki tłumaczeń
for lang in pl en de es fr it; do
    echo "Validating $lang.json..."
    python3 -m json.tool src/translations/$lang.json > /dev/null && echo "✅ $lang.json OK" || echo "❌ $lang.json INVALID"
done
```

### Build & Test

```bash
# Minifikacja
npm run build:minify

# Development mode z hot reload
npm run dev

# Production build
npm run build
```

---

**Last Updated**: 2025-11-14
**Version**: 1.1.5
**Author**: Michał Kania

Przestrzeganie tego przewodnika zapewni spójność wizualną i funkcjonalną aplikacji Time Planner.
