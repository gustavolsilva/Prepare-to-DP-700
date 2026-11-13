#!/usr/bin/env python3
"""
Atalho de Execução: Gerador de Áudio Neural com Dicionário Fonético
Delega para o módulo principal de geração em labs/generate_audio.py.
"""

import os
import sys

# Garante que o diretório raiz e labs/ estejam no PATH
WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(WORKSPACE_ROOT, "labs"))

if __name__ == "__main__":
    import generate_audio
    # Repassa argumentos de linha de comando
    sys.exit(os.system(f"{sys.executable} {os.path.join(WORKSPACE_ROOT, 'labs', 'generate_audio.py')} {' '.join(sys.argv[1:])}"))

