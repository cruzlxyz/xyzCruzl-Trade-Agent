@echo off

where py >nul 2>nul
if %errorlevel%==0 (
  py -3 "%~dp0src\main.py" %*
  exit /b %errorlevel%
)

where python >nul 2>nul
if %errorlevel%==0 (
  python "%~dp0src\main.py" %*
  exit /b %errorlevel%
)

echo Python not found. Install Python 3.10+ from https://www.python.org/downloads/
exit /b 1
