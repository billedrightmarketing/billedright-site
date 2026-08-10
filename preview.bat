@echo off
cd /d "%~dp0"
echo Rebuilding site from pages/ + templates/ ...
python build.py
if errorlevel 1 (
  echo.
  echo Build failed - see errors above.
  pause
  exit /b 1
)
echo.
echo Opening http://localhost:8843 in your browser...
start "" http://localhost:8843
echo.
echo Local preview server running. Leave this window open while previewing.
echo Press Ctrl+C to stop, then close this window when done.
echo.
python -m http.server 8843 --directory dist
