#!/usr/bin/env bash
# ==============================================================================
# Script de Inicialização Rápida: Prepare to DP-700
# Funciona em qualquer ambiente Linux ou macOS (e Git Bash no Windows)
# ==============================================================================

set -e

PORT="${1:-8000}"
WORKSPACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$WORKSPACE_DIR"

echo "=============================================================================="
echo "🎯 PREPARATÓRIO MICROSOFT CERTIFIED: FABRIC DATA ENGINEER ASSOCIATE (DP-700)"
echo "=============================================================================="

# 1. Verifica ou cria o ambiente virtual Python (.venv)
if [ ! -d ".venv" ]; then
    echo "📦 Criando ambiente virtual Python (.venv)..."
    python3 -m venv .venv
fi

# 2. Seleciona o executável Python do .venv
if [ -f ".venv/bin/python" ]; then
    VENV_PYTHON=".venv/bin/python"
    VENV_PIP=".venv/bin/pip"
elif [ -f ".venv/Scripts/python.exe" ]; then
    # Suporte para Windows (Git Bash)
    VENV_PYTHON=".venv/Scripts/python.exe"
    VENV_PIP=".venv/Scripts/pip.exe"
else
    echo "❌ Erro: Não foi possível localizar o executável do Python dentro de .venv."
    exit 1
fi

# 3. Instala dependências se requirements.txt existir
if [ -f "requirements.txt" ]; then
    echo "📋 Verificando dependências do projeto..."
    "$VENV_PIP" install -q -r requirements.txt || true
fi

# 4. Executa a auditoria de integridade do workspace
echo "🧪 Executando suíte de testes unitários..."
"$VENV_PYTHON" -m unittest discover tests

# 5. Inicia o servidor HTTP sem cache
echo "🚀 Iniciando servidor web local na porta $PORT..."
echo "👉 Abra no seu navegador: http://localhost:$PORT/"
echo "🛑 Pressione Ctrl+C para encerrar o servidor."
echo "=============================================================================="

exec "$VENV_PYTHON" scripts/dev_server.py "$PORT"

