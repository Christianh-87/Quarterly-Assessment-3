@echo off
REM === Run AI-Powered Country Music Newsletter ===
REM This version automatically runs from the batch file's directory,
REM so it works on any computer without needing to change file paths.

REM Change directory to the folder containing this .bat file
cd /d "%~dp0"

REM Run the main Python newsletter script using Python 3.13 via launcher
py -3.13 "newsletter_main.py"

REM Log the date and time of each run for verification
echo %date% %time% - Newsletter run complete. >> run_log.txt

REM Pause so the user can see the output when run manually
pause
