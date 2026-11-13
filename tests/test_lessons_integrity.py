#!/usr/bin/env python3
"""
Testes Unitários de Integridade das Lições do Curso DP-700
Valida estrutura HTML, links de CSS/JS, 6 lentes pedagógicas, reprodutor de áudio e quizzes.
"""

import os
import re
import unittest

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS_DIR = os.path.join(WORKSPACE_ROOT, "lessons")
ASSETS_DIR = os.path.join(WORKSPACE_ROOT, "assets")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
LABS_DIR = os.path.join(WORKSPACE_ROOT, "labs")

EXPECTED_LESSONS = [
    "0001-data-engineering-foundations-oltp-olap-fabric.html",
    "0002-storage-fundamentals-parquet-delta-medallion.html",
    "0003-dimensional-modeling-and-three-languages-sql-spark-kql.html",
    "0004-onelake-capacities-smoothing-domains-spark-pools.html",
    "0005-architectural-decision-guide-lakehouse-warehouse-eventhouse.html",
    "0006-shortcuts-and-mirroring-zero-copy-integration.html",
    "0007-orchestration-pipelines-dataflows-dag.html",
    "0008-incremental-loading-watermark-scd.html",
    "0009-batch-transformations-sql-spark-clones.html",
    "0010-streaming-eventstreams-spark-windows.html",
    "0011-kql-eventhouse-update-policies-materialized-views.html",
    "0012-security-governance-rls-cls-direct-lake-fallback.html",
    "0013-cicd-git-deployment-pipelines-sqlproj.html",
    "0014-performance-vorder-liquid-clustering-tuning.html",
    "0015-monitoring-hub-capacity-metrics-troubleshooting.html",
]

REQUIRED_LENSES = ["unificado", "junior", "pleno", "senior", "staff", "clevel"]

class TestLessonsIntegrity(unittest.TestCase):

    def test_all_15_lessons_exist(self):
        """Verifica se todas as 15 lições existem na pasta lessons/"""
        for lesson in EXPECTED_LESSONS:
            path = os.path.join(LESSONS_DIR, lesson)
            self.assertTrue(os.path.exists(path), f"Lição ausente: {lesson}")
            self.assertGreater(os.path.getsize(path), 5000, f"Arquivo da lição muito pequeno: {lesson}")

    def test_lesson_html_structure_and_assets(self):
        """Valida DOCTYPE, CSS, JS e meta tags de cada lição"""
        for lesson in EXPECTED_LESSONS:
            path = os.path.join(LESSONS_DIR, lesson)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            with self.subTest(lesson=lesson):
                self.assertIn("<!DOCTYPE html>", content, "Falta DOCTYPE html")
                self.assertIn('<html lang="pt-BR">', content, "Falta lang='pt-BR'")
                self.assertIn("tufte.css", content, "Falta tufte.css")
                self.assertIn("vark.css", content, "Falta vark.css")
                self.assertIn("lens.js", content, "Falta lens.js")
                self.assertIn("window.toggleAppTheme()", content, "Falta botão de tema toggleAppTheme()")

    def test_lesson_six_lenses_present(self):
        """Valida que todas as 6 lentes pedagógicas possuem botão e painel em cada lição"""
        for lesson in EXPECTED_LESSONS:
            path = os.path.join(LESSONS_DIR, lesson)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            with self.subTest(lesson=lesson):
                for lens in REQUIRED_LENSES:
                    # Verifica botão seletor (.lens-btn ou .lens-tab)
                    btn_pattern = rf'data-lens=["\']{lens}["\']'
                    self.assertTrue(re.search(btn_pattern, content), f"Botão da lente '{lens}' ausente em {lesson}")
                    # Verifica painel de conteúdo (data-lens-content ou class="lens-text-content" data-lens)
                    panel_pattern = rf'(data-lens-content=["\']{lens}["\']|class=["\']lens-text-content["\']\s+data-lens=["\']{lens}["\'])'
                    self.assertTrue(re.search(panel_pattern, content), f"Painel da lente '{lens}' ausente em {lesson}")

    def test_lesson_audio_player_and_files(self):
        """Valida que cada lição possui reprodutor de áudio apontando para um MP3 real e válido"""
        for lesson in EXPECTED_LESSONS:
            path = os.path.join(LESSONS_DIR, lesson)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            with self.subTest(lesson=lesson):
                self.assertIn('id="bloco-audio"', content, "Elemento #bloco-audio ausente")
                has_audio_el = ('id="vark-audio-element"' in content) or ('id="lesson-audio-player"' in content) or ('<audio' in content)
                self.assertTrue(has_audio_el, f"Elemento <audio> ausente em {lesson}")

                # Extrai nome do arquivo MP3
                match = re.search(r'src=["\'](?:\.\./assets/audio/|../assets/audio/)?(lesson-\d{4}-pt\.mp3)', content)
                self.assertIsNotNone(match, f"Referência a áudio MP3 não encontrada em {lesson}")
                audio_file = match.group(1)
                audio_path = os.path.join(AUDIO_DIR, audio_file)
                self.assertTrue(os.path.exists(audio_path), f"Arquivo de áudio físico não existe: {audio_file}")
                # Áudios gravados têm pelo menos 100 KB
                self.assertGreater(os.path.getsize(audio_path), 100000, f"Áudio corrompido/incompleto: {audio_file}")

    def test_lesson_quiz_and_lab_links(self):
        """Valida a presença de formulário de quiz e referência ao lab executável"""
        for lesson in EXPECTED_LESSONS:
            path = os.path.join(LESSONS_DIR, lesson)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            with self.subTest(lesson=lesson):
                self.assertIn('id="bloco-quiz"', content, "Seção de quiz ausente")
                has_quiz = ('quiz-form' in content) or ('quiz-card' in content) or ('quiz-container-box' in content)
                self.assertTrue(has_quiz, f"Estrutura de quiz ausente em {lesson}")
                self.assertIn('id="bloco-pratica"', content, "Seção de lab prático ausente")

                # Verifica comando do laboratório Python
                match_lab = re.search(r'\./\.venv/bin/python\s+labs/([a-zA-Z0-9\-_]+)/lab_simulation\.py', content)
                self.assertIsNotNone(match_lab, f"Comando de execução do lab não encontrado em {lesson}")
                lab_folder = match_lab.group(1)
                lab_script = os.path.join(LABS_DIR, lab_folder, "lab_simulation.py")
                self.assertTrue(os.path.exists(lab_script), f"Script de lab referenciado não existe: {lab_script}")

    def test_sidebar_autohide_and_responsive_support(self):
        """Valida que o CSS e JS fornecem suporte ao layout remissivo, gaveta mobile e recolhimento"""
        tufte_css = os.path.join(ASSETS_DIR, "tufte.css")
        with open(tufte_css, "r", encoding="utf-8") as f:
            css = f.read()

        self.assertIn(".course-app-shell.sidebar-collapsed", css, "CSS deve suportar estado .sidebar-collapsed")
        self.assertIn(".course-app-shell.sidebar-open", css, "CSS deve suportar estado .sidebar-open (mobile)")
        self.assertIn(".sidebar-backdrop", css, "CSS deve conter backdrop para gaveta mobile")
        self.assertIn(".floating-sidebar-toggle", css, "CSS deve conter botão flutuante de sumário")

        lens_js = os.path.join(ASSETS_DIR, "lens.js")
        with open(lens_js, "r", encoding="utf-8") as f:
            js = f.read()

        self.assertIn("window.toggleCourseSidebar", js, "JS deve expor window.toggleCourseSidebar")
        self.assertIn("fabric_dp700_sidebar_collapsed", js, "JS deve persistir estado da barra no localStorage")

if __name__ == "__main__":
    unittest.main()
