# Registro de Aprendizado: 0011 - Lição 0008 Concluída

- **Data/Hora:** 2026-11-13T09:23:00-03:00
- **Contexto:** Entrega da Lição 0008 (Carga Incremental, Watermarking, Change Data Capture e SCD 1/2/3).
- **Implementações Realizadas:**
  1. **Lição 0008 (`lessons/0008-incremental-loading-watermark-scd.html`):**
     - Padrão **High Watermarking** (uso de carimbos temporais ou colunas sequenciais em fuso UTC).
     - **Change Data Capture (CDC):** Ingestão com leitura direta de logs de transação sem degradação do banco operacional.
     - **Slowly Changing Dimensions (SCD):**
       - **SCD Tipo 1:** Sobrescrita direta (sem preservação de histórico).
       - **SCD Tipo 2:** Versionamento temporal completo com `SurrogateKey`, `ValidFrom`, `ValidTo` e `IsCurrent`.
       - **SCD Tipo 3:** Preservação de atributos anteriores em colunas adicionais.
     - Áudio neural gerado via `edge-tts` com voz Microsoft `pt-BR-AntonioNeural` (`assets/audio/lesson-0008-pt.mp3`).
     - Script Python interativo de simulação (`labs/0008-incremental-loading-watermark-scd/lab_simulation.py`) executado com sucesso no `.venv/`.
     - Quiz DP-700 avaliando o caso clássico de auditoria histórica bancária via SCD Tipo 2.
  2. **Catálogo de Lições Atualizado (`index.html`):**
     - Adicionado card oficial da Lição 0008.

