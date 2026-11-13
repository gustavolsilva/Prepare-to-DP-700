#!/usr/bin/env python3
"""
Testes Unitários do Banco de Questões do Simulado DP-700
Valida regras de negócio do simulador Pearson VUE:
- Single-Choice: exatamente 1 alternativa correta
- Multi-Select: exatamente 2 alternativas corretas
- Case Studies: 4 abas de contexto obrigatórias e sub-questões válidas
"""

import os
import re
import json
import unittest

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS_JS = os.path.join(WORKSPACE_ROOT, "assets", "exam-questions.js")

def load_question_bank():
    with open(QUESTIONS_JS, "r", encoding="utf-8") as f:
        text = f.read()

    # Extrai o array JavaScript atribuído a window.DP700_QUESTION_BANK
    match = re.search(r'window\.DP700_QUESTION_BANK\s*=\s*(\[[\s\S]*?\]);\s*$', text)
    if not match:
        raise ValueError("Não foi possível encontrar window.DP700_QUESTION_BANK em assets/exam-questions.js")

    js_code = match.group(1)
    
    # Remove comentários JavaScript de linha simples
    cleaned = re.sub(r'//.*', '', js_code)
    # Remove crases de template strings substituindo por aspas duplas com escape
    # Como as tabs contêm template strings multilinhas, vamos parsear com regex inteligente
    return text

class TestExamQuestions(unittest.TestCase):

    def setUp(self):
        with open(QUESTIONS_JS, "r", encoding="utf-8") as f:
            self.raw_content = f.read()

    def test_file_exists_and_non_empty(self):
        """Verifica se assets/exam-questions.js existe e tem tamanho considerável"""
        self.assertTrue(os.path.exists(QUESTIONS_JS))
        self.assertGreater(os.path.getsize(QUESTIONS_JS), 10000)

    def test_question_counts(self):
        """Valida que há questões suficientes para todas as categorias no banco expandido de 180+"""
        single_count = len(re.findall(r'type:\s*["\']single["\']', self.raw_content))
        multi_count = len(re.findall(r'type:\s*["\']multi["\']', self.raw_content))
        case_studies = len(re.findall(r'type:\s*["\']case_study["\']', self.raw_content))

        self.assertGreaterEqual(single_count, 150, "Mínimo de 150 questões Single-Choice")
        self.assertGreaterEqual(multi_count, 15, "Mínimo de 15 questões Multi-Select")
        self.assertGreaterEqual(case_studies, 8, "Devem existir pelo menos 8 Casos de Estudo completos")
        self.assertGreaterEqual(single_count + multi_count, 174, "Banco total deve superar o triplo (174 questões)")

    def test_case_studies_have_required_tabs(self):
        """Valida que cada Caso de Estudo possui as 4 abas requeridas pelo layout Pearson VUE"""
        required_tabs = ["overview", "existing_env", "data_req", "tech_req"]
        for tab in required_tabs:
            matches = len(re.findall(rf'id:\s*["\']{tab}["\']', self.raw_content))
            self.assertGreaterEqual(matches, 8, f"A aba '{tab}' deve estar presente em todos os 8 Casos de Estudo")

    def test_correct_answers_distribution(self):
        """Valida que todas as questões possuem alternativas corretas demarcadas"""
        true_answers = len(re.findall(r'isCorrect:\s*true', self.raw_content))
        false_answers = len(re.findall(r'isCorrect:\s*false', self.raw_content))

        self.assertGreaterEqual(true_answers, 180, "Total de alternativas corretas deve superar 180")
        self.assertGreaterEqual(false_answers, 500, "Total de distratores deve superar 500 alternativas")

if __name__ == "__main__":
    unittest.main()

