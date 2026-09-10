@echo off
rem CCPID biweekly detection round against ccnt.igdp.cn.
rem Launched by the Windows scheduled task "CCPID CCNT Biweekly Review".
chcp 65001 >nul
cd /d "%~dp0.."

rem --- Mechanical steps run here in cmd, outside the Claude session ---
python scripts\check_ccnt_updates.py --catchup-days 60 > logs\ccnt_checker_run.log 2>&1

rem Resolve today's date for the report filename (locale-independent).
for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set RPTDATE=%%i

rem --- Headless analysis: Claude only reads files (Read/Grep/Glob) and
rem prints the review report to stdout, which is saved directly as the
rem report file. With no shell and no write tools it cannot touch the
rem database or run commands. ---
(echo Today's date: %RPTDATE%& echo.& type review\ccnt\prompt.md) | "%APPDATA%\npm\claude.cmd" -p --allowedTools "Read,Grep,Glob" > "review\ccnt\reports\%RPTDATE%.md" 2> "logs\ccnt_review_last_run.log"

rem --- Mark candidates as seen only if a non-trivial report was produced ---
powershell -NoProfile -Command "$f='review\ccnt\reports\%RPTDATE%.md'; if((Test-Path $f) -and (Get-Item $f).Length -gt 200){exit 0}else{exit 1}" && python scripts\check_ccnt_updates.py --mark-seen >> logs\ccnt_checker_run.log 2>&1
