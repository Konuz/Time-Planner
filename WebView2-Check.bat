@echo off
echo ================================================================
echo   WebView2 Runtime - Installation Check
echo ================================================================
echo.

REM Check if WebView2 Runtime is installed by looking for common registry keys
reg query "HKLM\SOFTWARE\WOW6432Node\Microsoft\EdgeUpdate\Clients\{F3017226-FE2A-4295-8BDF-00C3A9A7E4C5}" >nul 2>&1
if %errorlevel% == 0 (
    echo [OK] WebView2 Runtime is INSTALLED
    echo.
    echo Your system has WebView2 Runtime installed.
    echo Time Planner should work without any additional setup.
    echo.
) else (
    reg query "HKLM\SOFTWARE\Microsoft\EdgeUpdate\Clients\{F3017226-FE2A-4295-8BDF-00C3A9A7E4C5}" >nul 2>&1
    if %errorlevel% == 0 (
        echo [OK] WebView2 Runtime is INSTALLED
        echo.
        echo Your system has WebView2 Runtime installed.
        echo Time Planner should work without any additional setup.
        echo.
    ) else (
        echo [WARNING] WebView2 Runtime is NOT INSTALLED
        echo.
        echo Time Planner requires WebView2 Runtime to function.
        echo.
        echo DOWNLOAD FROM:
        echo https://go.microsoft.com/fwlink/p/?LinkId=2124703
        echo.
        echo FILE SIZE: ~2MB bootstrapper
        echo.
        echo After installation, Time Planner will work properly.
        echo.
    )
)

echo ================================================================
echo   System Information
echo ================================================================
echo.

REM Display Windows version
ver
echo.

REM Check if Microsoft Edge is installed (usually includes WebView2)
if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" (
    echo Microsoft Edge: INSTALLED
    echo.
    echo Note: Edge includes WebView2, but a separate WebView2 Runtime
    echo       installation may still be required for some applications.
    echo.
) else (
    echo Microsoft Edge: NOT FOUND
    echo.
)

echo ================================================================
echo.
echo Press any key to close this window...
pause >nul
