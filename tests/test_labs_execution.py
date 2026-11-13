#!/usr/bin/env python3
"""
Testes Unitários de Execução dos Laboratórios Hands-On (0001 a 0015)
Executa cada script em Python dentro do ambiente virtual e valida retorno de saída com código 0.
"""

import os
import sys
import glob
import subprocess
import unittest

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABS_DIR = os.path.join(WORKSPACE_ROOT, "labs")

class TestLabsExecution(unittest.TestCase):

    def test_all_15_labs_execute_cleanly(self):
        """Descobre e executa todos os 15 laboratórios em Python garantindo saída limpa"""
        lab_scripts = sorted(glob.glob(os.path.join(LABS_DIR, "00*", "lab_simulation.py")))
        self.assertEqual(len(lab_scripts), 15, f"Esperados 15 laboratórios, encontrados: {len(lab_scripts)}")

        for script in lab_scripts:
            folder_name = os.path.basename(os.path.dirname(script))
            with self.subTest(lab=folder_name):
                result = subprocess.run(
                    [sys.executable, script],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                self.assertEqual(
                    result.returncode,
                    0,
                    f"Falha ao executar o laboratório {folder_name}.\nStderr:\n{result.stderr}\nStdout:\n{result.stdout}"
                )
                self.assertGreater(
                    len(result.stdout.strip()),
                    50,
                    f"Laboratório {folder_name} não produziu saída no terminal."
                )

if __name__ == "__main__":
    unittest.main()

