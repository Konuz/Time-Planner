# ⏰ Time Planner

> Multilingual time tracking application with integrated Pomodoro timer and To-Do list

**Time Planner** is a free, lightweight Windows desktop application that helps you track work hours, boost productivity with the Pomodoro technique, and manage your tasks efficiently. Perfect for freelancers, remote workers, and teams who need accurate time tracking without the complexity.

🎯 **All-in-One Solution**: Timesheet + Pomodoro Timer + To-Do List in one full app
---

## 📸 Screenshots
<img width="1918" height="1035" alt="1" src="https://github.com/user-attachments/assets/4e476eb7-d7b7-41c0-9088-752f6f8b4994" />
<img width="1919" height="1032" alt="2" src="https://github.com/user-attachments/assets/e2eb2855-a180-478a-a11e-4ac9f78f8a7c" />
<img width="1906" height="1003" alt="3" src="https://github.com/user-attachments/assets/6352501c-1f7a-44be-8ea6-df119542bff5" />
<img width="1917" height="1032" alt="4" src="https://github.com/user-attachments/assets/46c9308e-34ad-47b4-94d8-01cb82e4aa1f" />


---

## 🌍 Languages

Fully localized in **6 languages**:
- 🇵🇱 Polski (Polish)
- 🇬🇧 English
- 🇩🇪 Deutsch (German)
- 🇪🇸 Español (Spanish)
- 🇮🇹 Italiano (Italian)
- 🇫🇷 Français (French)

> **Note**: The "To-Do" widget name remains untranslated across all languages for consistency.

> **Translation Help**: Native speakers are welcome to suggest improvements! If you spot any translation errors, please [create an issue](https://github.com/yourusername/time-planner/issues) or discussion.

## ✨ Features

### 📊 Time Tracking
- **Entry Management**: Add, edit, clone, and delete time entries
- **Project Organization**: Custom projects and task types
- **Smart Filtering**: Filter by month, week, or task type
- **Monthly Summary**: Automatic calculation of total hours
- **CSV Export**: Export entries with native file dialog support

### 🍅 Pomodoro Timer
- **Customizable Sessions**: Work (25min), short break (5min), long break (15min)
- **Auto-Tracking**: Automatically creates timesheet entries on work completion
- **Session Statistics**: Track daily completed pomodoros
- **Smart Accumulation**: Multiple sessions for the same task combine into single entry
- **Draggable Widget**: Position and resize anywhere on screen

### ✅ To-Do Widget
- **Priority Levels**: High, medium, low priority tasks
- **Date Management**: Due dates with deadline indicators (same-day alerts)
- **Drag & Drop**: Reorder tasks within dated/undated sections
- **Integration**: Send tasks to Pomodoro timer or create timesheet entries
- **Draggable Widget**: Position and resize anywhere on screen

### 🎨 User Experience
- **Modern UI**: Clean and simple gradient-based design with smooth animations
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support
- **Responsive**: Adapts to different window sizes
- **Single Instance**: Prevents multiple app windows
- **Offline Ready**: No internet connection required, all assets bundled

## 🚀 Installation

### Quick Start (3 Easy Steps)

1. **Download** the latest version: [📥 time-planner.exe](https://github.com/yourusername/time-planner/releases) (~3MB)
2. **Run** the downloaded file - Windows may show a security warning (click "More info" → "Run anyway")
3. **Start tracking** - The app opens ready to use, no setup required!

### System Requirements

- ✅ Windows 10 or later (64-bit)
- ✅ 100MB RAM
- ✅ 20MB disk space
- ✅ Internet connection (only for initial WebView2 download if needed)

**Note**: Windows may automatically download WebView2 on first launch if not already installed.

## 📖 Usage Guide

### Getting Started

1. **Launch the app** - The application opens with the timesheet entry form
2. **Select language** - Click the language dropdown (top-right) to choose your preferred language
3. **Add projects and task types** - Click ⚙️ Settings to customize your workspace
   - Projects: Add project numbers or descriptions from your company's timesheet tool
   - Tasks: Add task types used in your company (e.g., CTASK from ServiceNow)

### Adding Time Entries

1. Fill in the entry form:
   - **Date**: Select the work date
   - **Task Type**: Choose from your categories (e.g., Development, Meeting)
   - **Project**: Select the project
   - **Hours**: Enter time worked (0.5-8 hours)
   - **Task Number**: Reference number or name
2. Click **Add Entry** or press Enter
3. View entries in the table below with automatic monthly summary

### Using Pomodoro Timer

1. Click 🍅 icon to expand the Pomodoro widget
2. Enter task number/name in the input field
3. Configure your projects (number/description from company tool) and task types (e.g., CTASK from ServiceNow) in Settings (⚙️)
4. Click **Start** to begin a 25-minute work session
5. Click ✓ **Complete Task** button to finish and auto-create timesheet entry
6. Timer automatically tracks your daily sessions

**Tip**: Multiple pomodoros for the same task number accumulate hours in a single entry!

### Managing To-Do Tasks

1. Click ✅ icon to expand the To-Do widget
2. Fill in task details:
   - **Task name**: What needs to be done
   - **Priority**: High (red), Medium (yellow), Low (green)
   - **Due date**: Optional deadline
3. Click **Add Task**
4. Drag tasks to reorder within sections
5. Complete tasks or send them to Pomodoro timer

### Exporting Data

1. Click **Export CSV** button in the header
2. Choose save location using native file dialog
3. CSV includes: Date, Task Type, Project, Hours, Task Number
4. Opens with Excel, Google Sheets, or any CSV reader

### 💡 Quick Tips

- **Keyboard shortcut**: Press Enter after filling the form to quickly add entries
- **Clone entries**: Use the Clone button in the Actions column to duplicate similar entries
- **Auto-accumulation**: Pomodoro sessions with the same task number automatically combine hours
- **Widget positioning**: Drag Pomodoro and To-Do widgets to your preferred screen position
- **Filter quickly**: Use month/week filters to focus on specific time periods
- **Multi-language**: Switch languages anytime from the top-right dropdown

## 🔒 Privacy & Security

- **100% Offline**: No internet connection required, works completely offline
- **Local Storage**: All data stored on your computer in `%LOCALAPPDATA%\com.timeplanner.app\` (user data) and `%APPDATA%\Time Planner\` (app files)
- **No Tracking**: Zero telemetry, analytics, or data collection
- **No Cloud**: Your data never leaves your computer
- **Secure**: Input validation and sanitization on all user data

## 💬 Feedback & Feature Requests

Your feedback is valuable! If you have suggestions or encounter issues:

- **Bug Reports**: [Create an Issue](https://github.com/yourusername/time-planner/issues)
- **Feature Requests**: [Start a Discussion](https://github.com/yourusername/time-planner/discussions)
- **Translation Corrections**: Since I don't speak German, Spanish, Italian, or French, I'd greatly appreciate feedback from native speakers on any translation errors or improvements in these versions
- **Questions**: Check existing discussions or create a new one

## ℹ️ About

**Time Planner** is a Windows desktop application designed for professionals who need to track their work hours accurately and efficiently. Built with modern web technologies wrapped in a native Windows application using Tauri framework.

### Origin Story

Born from frustration with the daily reality of corporate time tracking: logging into **clunky, unintuitive enterprise timesheet systems** just to enter a few hours, or wrestling with **Excel spreadsheets** that quickly become disorganized and time-consuming to maintain.

Time Planner was created to solve this specific pain point: **capture your work as it happens** (tasks from ServiceNow, Jira, or any ticketing system), keep everything organized in a clean, searchable table throughout the month, then **batch-export everything at month's end** to your corporate timesheet in minutes instead of hours.

No more:
- ❌ Daily logins to slow enterprise portals
- ❌ Excel chaos with misaligned rows and manual calculations
- ❌ Trying to remember what you worked on two weeks ago
- ❌ Spending 30+ minutes every month reconstructing your timesheet

Instead:
- ✅ Quick entry as you work (5 seconds per task)
- ✅ Automatic organization and monthly summaries
- ✅ CSV export ready for any corporate system
- ✅ Complete work history at your fingertips

What started as a ServiceNow-focused solution has evolved into a **universal time tracking tool** that works seamlessly with any ticketing or project management system. Whether you're managing tasks in **Jira**, tracking issues in **Azure DevOps**, organizing work in **Monday.com**, **Asana**, **Linear**, **ClickUp**, **Redmine**, **Zendesk**, or any other platform, Time Planner provides the same simple, efficient workflow.

**The key insight**: You don't need complex integrations—just a simple place to collect task numbers, track hours, and export when ready.

### Why Time Planner?

- ✅ **Simple & Fast**: No complex setup, just download and start tracking
- ✅ **Privacy First**: All data stays on your computer
- ✅ **Universal Compatibility**: Works with ServiceNow, Jira, Azure DevOps, Monday.com, and any ticketing system
- ✅ **Multilingual**: Works in your language (6 languages supported)
- ✅ **No Subscription**: One-time download, no recurring fees
- ✅ **Lightweight**: Small file size (~15MB), minimal resource usage

## ❓ Frequently Asked Questions

### Is Time Planner free?
Yes, Time Planner is completely free to download and use. No subscription, no hidden fees.

### Does it require internet connection?
No, Time Planner works completely offline. All data is stored locally on your computer.

### Is my data safe?
Absolutely. Your data never leaves your computer. No cloud sync, no telemetry, no tracking.

### Can I export my data?
Yes, you can export your timesheet entries to CSV format, which opens in Excel or Google Sheets.

### Which languages are supported?
Time Planner supports 6 languages: Polish, English, German, Spanish, Italian, and French.

### Will there be a Mac/Linux version?
Mac and Linux support is planned for future releases. Currently only Windows is supported.

### How do I backup my data?
Your data is stored in two locations:
- **Application data** (CSV exports, logs): `%APPDATA%\Time Planner\`
- **User data** (entries, projects, tasks): `%LOCALAPPDATA%\com.timeplanner.app\EBWebView\`

For complete backup, save both folders.

### How do I reset the app to factory settings?

**Option 1 - Complete Reset (recommended):**
1. Close Time Planner
2. Delete folder: `%LOCALAPPDATA%\com.timeplanner.app`
3. Restart the app (fresh install state)

**Option 2 - Quick Reset via DevTools:**
1. Open Time Planner
2. Press F12 to open DevTools
3. In Console tab, type:
   ```javascript
   localStorage.clear();
   location.reload();
   ```
4. All data will be cleared and app will reload

## 🗺️ Roadmap

Future updates planned:
- [ ] Linux and macOS support
- [ ] Dark/Light theme toggle
- [ ] Custom Pomodoro duration presets (currently follows classic Pomodoro philosophy: 25min work, 5min short break, 15min long break)
- [ ] Advanced reporting and analytics

## ☕ Support the Project

If Time Planner helps you save time and stay productive, consider supporting its development!

Your support helps maintain the app, add new features, and keep it free for everyone.

**[☕ Support on Gumroad](https://michalverse23.gumroad.com/l/amseic)**

Every contribution, no matter how small, is greatly appreciated and motivates continued development! 🙏

---

⭐ Star this repo if you find it useful!
