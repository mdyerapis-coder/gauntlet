@echo off
REM Gauntlet launcher (Windows)
REM Starts the CORS proxy, then opens gauntlet.html in your default browser.
setlocal
cd /d "%~dp0"

start "" python gauntlet-proxy.py 8000

REM give the proxy a moment to bind
timeout /t 2 >nul

start "" "gauntlet.html"

echo Gauntlet is running. Close the proxy window to stop it.
pause
