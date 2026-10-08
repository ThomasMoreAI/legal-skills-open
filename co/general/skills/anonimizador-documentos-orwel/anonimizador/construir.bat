@echo off
setlocal
cd /d "%~dp0"

echo [1/4] Instalando dependencias...
python -m pip install -r requirements.txt
if errorlevel 1 goto error

echo.
echo [2/4] Descargando modelo de lenguaje espanol (spaCy)...
python -m spacy download es_core_news_sm
if errorlevel 1 goto error

echo.
echo [3/4] Compilando ejecutable (puede tardar varios minutos)...
python -m PyInstaller anonimizador.spec --noconfirm
if errorlevel 1 goto error

echo.
echo [4/4] Copiando archivos de configuracion...
copy /Y reemplazos.json dist\reemplazos.json >nul
copy /Y lista_blanca.json dist\lista_blanca.json >nul
if exist LEEME.txt copy /Y LEEME.txt dist\LEEME.txt >nul

echo.
echo Listo. Reparte la carpeta dist\ completa:
echo   - Anonimizador-Trifuerza.exe
echo   - reemplazos.json
echo   - lista_blanca.json
echo   - LEEME.txt
pause
exit /b 0

:error
echo.
echo Error en la compilacion.
pause
exit /b 1
