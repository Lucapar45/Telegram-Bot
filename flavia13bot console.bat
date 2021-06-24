@echo off
title pygame console
@echo Starting...
timeout /t 2 >nul
@echo.


title flavia13bot-telegram console
goto WAIT

:RESTART
echo Vuoi riavviare? [S/N/W]
set/p "cho= $ "
if %cho% == s goto START
if %cho% == S goto START

if %cho% == n goto END
if %cho% == N goto END

if %cho% == w goto WAIT
if %cho% == W goto WAIT

if %cho% == c cls
if %cho% == C cls
echo invalid choice
pause

goto RESTART

:START
cls
@echo Started the game
python main.py
goto RESTART

:WAIT
@echo Started the game
python main.py
goto RESTART

:END