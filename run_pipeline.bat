@echo off
title Smartest Factory Pipeline
echo ===================================================
echo   SMART FACTORY PIPELINE LAUNCHER (uv-managed)
echo ===================================================
echo.

REM --- Detect WSL availability ---
wsl --version >nul 2>&1
if %errorlevel%==0 (
    echo [INFO] Detected WSL2 environment. Running inside Ubuntu...
    echo.
    REM Change path if your project directory differs:
    wsl -d Ubuntu bash -ic "cd ~/smartestfactory && uv run python pipeline_incremental.py --data-dir data --index-dir index"
) else (
    echo [WARN] WSL2 not found. Attempting local Windows run...
    echo.
    REM Fallback if you have uv + Python on Windows:
    cd /d "%~dp0"
    uv run python pipeline_incremental.py --data-dir data --index-dir index
)

echo.
echo [DONE] Smartest Factory indexing pipeline finished.
echo.
pause
