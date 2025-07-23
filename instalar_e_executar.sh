#!/bin/bash

echo "========================================"
echo " Sistema de Cálculo de Score - Analistas"
echo "========================================"
echo ""
echo "Instalando dependências..."
pip install -r requirements.txt
echo ""
echo "Iniciando aplicação..."
echo "Acesse: http://localhost:5000"
echo ""
echo "Para parar a aplicação, pressione Ctrl+C"
echo ""
python app.py

