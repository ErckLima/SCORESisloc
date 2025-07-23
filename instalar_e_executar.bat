@echo off
echo ========================================
echo  Sistema de Calculo de Score - Analistas
echo ========================================
echo.
echo Instalando dependencias...
pip install -r requirements.txt
echo.
echo Iniciando aplicacao...
echo Acesse: http://localhost:5000
echo.
echo Para parar a aplicacao, pressione Ctrl+C
echo.
python app.py
pause

