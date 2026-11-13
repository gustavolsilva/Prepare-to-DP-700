# Registro de Aprendizado: 0014 - Conclusão do Módulo 2 (Lição 0011)

- **Data/Hora:** 2026-11-13T09:59:00-03:00
- **Contexto:** Entrega da Lição 0011 e conclusão oficial do Módulo 2 (Ingestão e Transformação de Dados: Domínio 2 da Certificação DP-700).
- **Implementações Realizadas:**
  1. **Lição 0011 (`lessons/0011-kql-eventhouse-update-policies-materialized-views.html`):**
     - O poder do **Kusto Engine (KQL)** no Eventhouse e Real-Time Intelligence.
     - **Update Policies:** Transformação atômica e parsing contínuo de JSON na ingestão sem orquestradores externos.
     - **Materialized Views:** Tabelas pré-agregadas que mantêm métricas e contadores consolidados incrementalmente.
     - Operadores fundamentais para o exame: `summarize arg_max()`, `make-series`, `parse_json`, `mv-expand` e a regra de ouro de performance de `has` (índice invertido em milissegundos) vs. `contains` (varredura linear lenta).
     - Áudio neural gerado via `edge-tts` com voz Microsoft `pt-BR-AntonioNeural` (`assets/audio/lesson-0011-pt.mp3`).
     - Script Python interativo (`labs/0011-kql-eventhouse-update-policies/lab_simulation.py`) executado com sucesso no `.venv/`.
     - Quiz DP-700 avaliando o uso de Update Policy para enriquecimento na ingestão contínua.
  2. **Catálogo de Lições Atualizado (`index.html`):**
     - O Módulo 2 está concluído com sucesso com as Lições 0007, 0008, 0009, 0010 e 0011 catalogadas.

