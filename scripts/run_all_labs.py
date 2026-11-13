#!/usr/bin/env python3
"""
Utilitário de Execução em Lote dos Laboratórios DP-700
Executa os 15 laboratórios práticos sequencialmente e exibe tabela de status.
"""

import os
import sys
import glob
import time
import subprocess

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABS_DIR = os.path.join(WORKSPACE_ROOT, "labs")

def main():
    print("=" * 90)
    print("EXECUÇÃO EM LOTE DOS LABORATÓRIOS HANDS-ON DO CURSO PREPARATÓRIO DP-700")
    print("=" * 90)

    scripts = sorted(glob.glob(os.path.join(LABS_DIR, "00*", "lab_simulation.py")))
    if not scripts:
        print("❌ Nenhum laboratório encontrado em labs/00*/lab_simulation.py")
        sys.exit(1)

    print(f"Total de Laboratórios Identificados: {len(scripts)}\n")
    print(f"{'#':<4} | {'Laboratório':<48} | {'Status':<12} | {'Tempo'}")
    print("-" * 90)

    all_passed = True
    start_total = time.time()

    for idx, s in enumerate(scripts, 1):
        folder = os.path.basename(os.path.dirname(s))
        t0 = time.time()
        res = subprocess.run([sys.executable, s], capture_output=True, text=True)
        duration = time.time() - t0

        if res.returncode == 0:
            status = "✅ SUCESSO"
        else:
            status = "❌ FALHA"
            all_passed = False

        print(f"{idx:<4} | {folder:<48} | {status:<12} | {duration:.2f}s")
        if res.returncode != 0:
            print(f"\n[ERRO NO LAB {folder}]:\n{res.stderr}\n")

    total_time = time.time() - start_total
    print("-" * 90)
    if all_passed:
        print(f"🎉 Todos os {len(scripts)} laboratórios foram executados com sucesso em {total_time:.2f}s!")
    else:
        print("⚠️ Houve falhas na execução de alguns laboratórios. Verifique as mensagens acima.")
        sys.exit(1)

if __name__ == "__main__":
    main()

