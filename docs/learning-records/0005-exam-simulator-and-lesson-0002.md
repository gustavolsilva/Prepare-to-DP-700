# Registro de Aprendizado: 0005 - Centro de Simulados DP-700 e Lição 0002

- **Data/Hora:** 2026-11-12T21:37:00-03:00
- **Contexto:** Expansão da plataforma educacional DP-700 após aprovação do plano de execução pelo usuário.
- **Implementações Realizadas:**
  1. **Centro Oficial de Simulados DP-700 (`simulados/index.html`):**
     - Criado motor completo (`assets/exam-simulator.js` e `assets/exam-simulator.css`) suportando Light & Dark Mode.
     - Suporte a dois modos: **Modo Treino Comentado** (com explicação detalhada de cada alternativa/distrator) e **Modo Exame Oficial** (cronômetro de 100 minutos, escala 0 a 1000, nota de corte 700).
     - **Questões de 1 Alternativa (Single-Choice):** Avaliando decisões arquiteturais de Lakehouse vs. Warehouse, V-Order em PySpark, Update Policies em KQL e Smoothing de CUs em 24h.
     - **Questões de 2 Alternativas (Multi-Select):** Validação estrita de marcação de exatamente duas opções (OneLake Shortcuts sem duplicação de dados em S3/ADLS Gen2, T-SQL MERGE + Zero-Copy Table Clones, e DMVs `queryinsights.exec_requests_history` + `queryinsights.frequently_run_queries`).
     - **Estudo de Caso Split-Screen (Case Study):** Cenário corporativo multinacional (*Contoso Global Retail*) com abas navegáveis à esquerda (`Visão Geral`, `Ambiente Atual`, `Requisitos de Dados`, `Requisitos Técnicos`) e bateria de questões contextualizadas à direita (Mirroring do Azure SQL, Shortcuts S3, e RLS no Semantic Model para evitar fallback do Power BI Direct Lake).
  2. **Lição 0002 Completa (`lessons/0002-storage-fundamentals-parquet-delta-medallion.html`):**
     - Estrutura de layout 2 colunas Figma TOTC (`Course Full View`).
     - Áudio neural gerado com `edge-tts` (`pt-BR-AntonioNeural`) e dicionário fonético auditado para termos técnicos (`assets/audio/lesson-0002-pt.mp3`).
     - Diagrama interativo de `_delta_log` e commits atômicos em SVG.
     - Laboratório local em Python isolado (`labs/0002-parquet-delta-medallion/lab_simulation.py`) executando dentro de `.venv/` com PyArrow demonstrando criação de commits atômicos e Time Travel.
     - Quiz DP-700 com 4 opções isomórficas sobre `VACUUM` e `FileNotFoundException`.
  3. **Portal Principal Atualizado (`index.html`):**
     - Adicionado botão de acesso direto ao Centro de Simulados no Hero e Card de destaque no catálogo de módulos.

