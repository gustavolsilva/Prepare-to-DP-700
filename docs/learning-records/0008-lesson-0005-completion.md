# Registro de Aprendizado: 0008 - Lição 0005 Concluída

- **Data/Hora:** 2026-11-13T08:52:00-03:00
- **Contexto:** Entrega da Lição 0005 (Guia de Decisão Arquitetural do Microsoft Fabric).
- **Implementações Realizadas:**
  1. **Servidor HTTP Local Restabelecido:**
     - Após o reinício do ambiente, o servidor sem cache (`labs/dev_server.py`) foi colocado em execução no background (`task-541`) servindo a porta 8000.
  2. **Lição 0005 (`lessons/0005-architectural-decision-guide-lakehouse-warehouse-eventhouse.html`):**
     - Matriz de decisão oficial cobrindo Lakehouse, Data Warehouse, Eventhouse e SQL Database.
     - Ênfase na regra de ouro da prova: o **SQL Analytics Endpoint do Lakehouse é estritamente somente leitura (Read-Only)**; comandos DML (UPDATE, DELETE, MERGE) exigem o **Fabric Data Warehouse**.
     - Critérios para seleção de **Eventhouse** (KQL, séries temporais, telemetria de alta frequência e baixa latência).
     - Áudio neural sintetizado via `edge-tts` com voz Microsoft `pt-BR-AntonioNeural` (`assets/audio/lesson-0005-pt.mp3`).
     - Script Python interativo de decisão (`labs/0005-architectural-decision-guide/lab_simulation.py`) executado com sucesso no `.venv/`.
     - Quiz DP-700 com 4 alternativas rigorosamente isomórficas sobre escolha de armazenamento com Stored Procedures e comandos DML.
  3. **Catálogo de Lições Atualizado (`index.html`):**
     - Adicionado card oficial da Lição 0005.

