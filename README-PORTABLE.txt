================================================================
  Time Planner - Portable Edition v1.0.0
================================================================

SYSTEM REQUIREMENTS:
- Windows 10/11 (64-bit)
- WebView2 Runtime (usually pre-installed on Windows 11)

INSTALLATION:
1. Extract all files from the ZIP to any location
2. Double-click time-planner.exe to run
3. If the app doesn't start, install WebView2 Runtime (see below)

NO INSTALLATION REQUIRED - This is a portable application!

================================================================
  WEBVIEW2 RUNTIME
================================================================

WebView2 is a Microsoft component that allows applications to
display web content. It's usually pre-installed on Windows 11.

IF THE APP DOESN'T START:
1. Run WebView2-Check.bat to check if WebView2 is installed
2. If not installed, download from:
   https://go.microsoft.com/fwlink/p/?LinkId=2124703
3. Install and restart Time Planner

FILE SIZE: ~2MB bootstrapper, or ~140MB full runtime

================================================================
  DATA STORAGE
================================================================

Your data is automatically saved and stored in:
  %APPDATA%\com.timeplanner.app\

This means:
- Your data persists across app updates
- Each Windows user has their own separate data
- Data is NOT portable with the application file

TO BACKUP YOUR DATA:
1. Close Time Planner
2. Copy the folder: %APPDATA%\com.timeplanner.app\
3. Paste it to your backup location

TO RESTORE DATA ON ANOTHER COMPUTER:
1. Install WebView2 Runtime (if needed)
2. Run time-planner.exe once to create the data folder
3. Close the app
4. Replace %APPDATA%\com.timeplanner.app\ with your backup
5. Start the app again

================================================================
  FEATURES
================================================================

✓ Track work hours with date, task type, and project
✓ Integrated Pomodoro timer for productivity
✓ TODO widget with drag-and-drop
✓ Bilingual interface (Polish/English)
✓ CSV export for current month
✓ Offline functionality - no internet required
✓ Single instance - prevents multiple windows

================================================================
  USAGE TIPS
================================================================

1. LANGUAGE SWITCHING:
   - Click the language icon in the header (PL/EN)
   - Your preference is saved automatically

2. POMODORO TIMER:
   - Drag to reposition the widget
   - Resize from corners and edges
   - Minimize to icon when not needed
   - Work sessions automatically create timesheet entries

3. TODO WIDGET:
   - Drag tasks to reorder
   - Set priorities: High, Medium, Low
   - Add due dates for time tracking
   - Complete tasks and optionally create timesheet entries

4. DATA EXPORT:
   - Export button generates CSV file
   - Contains current month's entries
   - Open in Excel, Google Sheets, etc.

5. FILTERS:
   - Month filter: Show only current month
   - Week filter: Show only current week
   - Task type filter: Multi-select checkboxes

================================================================
  TROUBLESHOOTING
================================================================

PROBLEM: Application doesn't start
SOLUTION:
  - Install WebView2 Runtime (link above)
  - Check if antivirus is blocking the exe
  - Run as Administrator (right-click → Run as administrator)

PROBLEM: Data is not saving
SOLUTION:
  - Check if %APPDATA% folder is accessible
  - Ensure you have write permissions
  - Close and reopen the application

PROBLEM: Fonts look different
SOLUTION:
  - This is normal - fonts are now embedded locally
  - Appearance may vary slightly from browser version

PROBLEM: Cannot open second instance
SOLUTION:
  - This is intentional (single-instance mode)
  - Second attempt will focus the existing window
  - If you need multiple instances, close the app first

================================================================
  SUPPORT & FEEDBACK
================================================================

For issues, questions, or feedback:
- Create an issue on GitHub (if applicable)
- Contact: [Your contact information]

================================================================
  LICENSE & CREDITS
================================================================

Time Planner v1.0.0
Built with Tauri + Vanilla JavaScript

Fonts: Roboto (Google Fonts, Apache License 2.0)
Framework: Tauri (MIT License)

================================================================
  VERSION HISTORY
================================================================

v1.0.0 (2025-01-12)
- Initial portable Windows release
- Offline functionality with local fonts
- Single-instance mode
- WebView2 integration

================================================================

Thank you for using Time Planner!
Enjoy tracking your productivity! 📊⏱️

================================================================
