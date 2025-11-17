# Instrukcja budowania Windows Portable EXE

## Krok 1: Otwórz Windows PowerShell
- Naciśnij `Win + X` i wybierz "Windows PowerShell" lub "Terminal"
- LUB Wyszukaj "PowerShell" w menu Start

## Krok 2: Przejdź do katalogu projektu
```powershell
cd C:\Users\micha\Desktop\Plan
```

## Krok 3: Zbuduj aplikację Windows
```powershell
npm run tauri:build
```

## Czas budowania
- **Pierwszy build**: 5-10 minut (pobieranie i kompilacja zależności)
- **Kolejne buildy**: 1-3 minuty

## Rezultat
Po zakończeniu buildu, znajdziesz pliki w:

### Portable EXE (to czego potrzebujesz):
```
src-tauri\target\release\time-planner.exe (~12-15MB)
```

### Instalatory (opcjonalnie):
```
src-tauri\target\release\bundle\nsis\Time Planner_1.0.0_x64-setup.exe
src-tauri\target\release\bundle\msi\Time Planner_1.0.0_x64_en-US.msi
```

## Testowanie
1. Uruchom `time-planner.exe` bezpośrednio z folderu `target\release\`
2. Aplikacja powinna otworzyć się w natywnym oknie Windows
3. Wszystkie funkcje powinny działać identycznie jak w wersji HTML

## Troubleshooting

### Problem: "WebView2 is not installed"
**Rozwiązanie**: Pobierz i zainstaluj WebView2 Runtime
- Link: https://go.microsoft.com/fwlink/p/?LinkId=2124703
- Na Windows 11 jest już preinstalowany

### Problem: Błędy kompilacji
**Rozwiązanie**:
1. Upewnij się, że Rust jest zainstalowany: `rustc --version`
2. Zaktualizuj Rust: `rustup update`
3. Wyczyść cache i spróbuj ponownie:
   ```powershell
   cd src-tauri
   cargo clean
   cd ..
   npm run tauri:build
   ```

### Problem: "Cannot find module @tauri-apps/cli"
**Rozwiązanie**:
```powershell
npm install
npm run tauri:build
```

## Dystrybucja

### Portable ZIP Package
Po zbudowaniu możesz utworzyć paczkę portable:

```
Time-Planner-Portable-v1.0.0.zip
├── time-planner.exe (~12-15MB)
├── README.txt (instrukcje)
└── WebView2-Check.bat (skrypt sprawdzający)
```

### Gdzie dane są przechowywane
```
C:\Users\{username}\AppData\Roaming\com.timeplanner.app\
```

Dane NIE są przechowywane w katalogu aplikacji, tylko w profilu użytkownika.
