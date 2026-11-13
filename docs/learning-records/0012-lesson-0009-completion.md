# Registro de Aprendizado: 0012 - Lição 0009 Concluída

- **Data/Hora:** 2026-11-13T09:30:00-03:00
- **Contexto:** Entrega da Lição 0009 (Transformações Batch em PySpark & T-SQL: MERGE, COPY, Schema Evolution e Table Clones).
- **Implementações Realizadas:**
  1. **Lição 0009 (`lessons/0009-batch-transformations-sql-spark-clones.html`):**
     - Comandos canônicos de transformação batch no Microsoft Fabric:
       - **COPY INTO:** Ingestão paralela massiva de arquivos externos em tabelas do Warehouse.
       - **MERGE INTO:** Operações atômicas de Upsert com garantia ACID.
       - **Schema Evolution (`mergeSchema=true`):** Expansão segura de colunas no Delta Lake em PySpark.
       - **Zero-Copy Table Clones (`CREATE TABLE ... AS CLONE OF`):** Criação instantânea de ambientes de teste e homologação no Warehouse sem duplicar custos de armazenamento no OneLake.
     - Áudio neural gerado via `edge-tts` com voz Microsoft `pt-BR-AntonioNeural` (`assets/audio/lesson-0009-pt.mp3`).
     - Script Python interativo (`labs/0009-batch-transformations-sql-spark-clones/lab_simulation.py`) executado com sucesso no `.venv/`.
     - Quiz DP-700 cobrando a sintaxe oficial de clonagem zero-copy para validação e testes.
  2. **Catálogo de Lições Atualizado (`index.html`):**
     - Adicionado card oficial da Lição 0009.

