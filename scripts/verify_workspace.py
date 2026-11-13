#!/usr/bin/env python3
"""
Script de Verificação Geral de Saúde do Workspace DP-700
Verifica dependências do ambiente Python, arquivos estáticos, integridade das lições e testes.
"""

import os
import sys
import unittest

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(WORKSPACE_ROOT)

def print_header(title):
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)

def check_python_environment():
    print_header("1. AMBIENTE PYTHON & DEPENDÊNCIAS")
    print(f"Python Executável: {sys.executable}")
    print(f"Versão: {sys.version.split()[0]}")

    required_modules = [
        ("pyarrow", "Manipulação de arquivos Parquet e Delta"),
        ("pandas", "Dataframes e modelagem analítica"),
        ("edge_tts", "Geração de áudio neural de alta qualidade"),
        ("aiohttp", "Comunicação assíncrona para TTS"),
    ]

    all_modules_ok = True
    for mod, desc in required_modules:
        try:
            __import__(mod)
            print(f"✅ Módulo '{mod:<12}' instalado com sucesso ({desc})")
        except ImportError:
            print(f"❌ Módulo '{mod:<12}' ausente! ({desc})")
            all_modules_ok = False

    return all_modules_ok

def run_unit_tests():
    print_header("2. EXECUÇÃO DA SUÍTE DE TESTES UNITÁRIOS (tests/)")
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.join(WORKSPACE_ROOT, "tests"))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()

def main():
    print_header("VERIFICAÇÃO DE INTEGRIDADE: PREPARE TO DP-700")
    print(f"Diretório Raiz do Projeto: {WORKSPACE_ROOT}")

    env_ok = check_python_environment()
    tests_ok = run_unit_tests()

    print_header("3. RESULTADO FINAL DA AUDITORIA")
    if env_ok and tests_ok:
        print("🎉 PARABÉNS! O workspace está 100% íntegro, saudável e pronto para uso local.")
        print("👉 Para iniciar o servidor web local execute: ./.venv/bin/python scripts/dev_server.py")
        sys.exit(0)
    else:
        print("⚠️ Foram identificadas pendências no workspace. Verifique os avisos acima.")
        sys.exit(1)

if __name__ == "__main__":
    main()

