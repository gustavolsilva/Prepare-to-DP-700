#!/usr/bin/env python3
"""
Testes Unitários de Folhas de Referência e do Portal Principal (index.html)
Valida integridade do catálogo, links de navegação e componentes imprimíveis.
"""

import os
import unittest

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFERENCE_DIR = os.path.join(WORKSPACE_ROOT, "reference")
INDEX_HTML = os.path.join(WORKSPACE_ROOT, "index.html")
SIMULADO_HTML = os.path.join(WORKSPACE_ROOT, "simulados", "index.html")

EXPECTED_REFERENCES = [
    "01-glossary-and-fundamentals-visual-guide.html",
    "02-storage-delta-medallion-shortcuts-guide.html",
    "03-architectural-engines-decision-matrix.html",
    "04-three-languages-sql-pyspark-kql-cheatsheet.html",
    "05-security-governance-purview-fallback-guide.html",
    "06-performance-vorder-clustering-monitoring-cheatsheet.html",
]

class TestReferenceAndPortal(unittest.TestCase):

    def test_all_six_reference_sheets_exist(self):
        """Valida que todas as 6 folhas de referência existem e têm botões de impressão e tema"""
        for ref in EXPECTED_REFERENCES:
            path = os.path.join(REFERENCE_DIR, ref)
            self.assertTrue(os.path.exists(path), f"Folha de referência ausente: {ref}")
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            with self.subTest(ref=ref):
                self.assertIn("window.print()", content, "Falta botão de impressão")
                self.assertIn("window.toggleAppTheme()", content, "Falta alternador de tema")
                self.assertIn("tufte.css", content, "Falta tufte.css")
                self.assertIn("vark.css", content, "Falta vark.css")

    def test_portal_index_links_all_15_lessons(self):
        """Valida que o portal principal index.html referencia todas as 15 lições"""
        with open(INDEX_HTML, "r", encoding="utf-8") as f:
            content = f.read()

        for i in range(1, 16):
            lesson_prefix = f"{i:04d}-"
            self.assertIn(lesson_prefix, content, f"Lição {lesson_prefix} não encontrada no index.html")

    def test_portal_index_links_all_six_references(self):
        """Valida que o portal principal index.html referencia todas as 6 folhas de referência"""
        with open(INDEX_HTML, "r", encoding="utf-8") as f:
            content = f.read()

        for ref in EXPECTED_REFERENCES:
            self.assertIn(ref, content, f"Referência {ref} não encontrada no index.html")

    def test_exam_simulator_assets_linked(self):
        """Valida que o simulador de exame carrega as questões e o motor JavaScript"""
        with open(SIMULADO_HTML, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("exam-questions.js", content, "Falta exam-questions.js no simulador")
        self.assertIn("exam-simulator.js", content, "Falta exam-simulator.js no simulador")
        self.assertIn("exam-simulator.css", content, "Falta exam-simulator.css no simulador")

if __name__ == "__main__":
    unittest.main()

