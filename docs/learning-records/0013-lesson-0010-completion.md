# Registro de Aprendizado: 0013 - Lição 0010 Concluída

- **Data/Hora:** 2026-11-13T09:47:00-03:00
- **Contexto:** Entrega da Lição 0010 (Engenharia de Streaming: Eventstreams e Spark Structured Streaming).
- **Implementações Realizadas:**
  1. **Lição 0010 (`lessons/0010-streaming-eventstreams-spark-windows.html`):**
     - Panorama completo de streaming no Microsoft Fabric:
       - **Fabric Eventstreams:** Ingestão visual sem código para Event Hubs, IoT Hub e Kafka, com filtros e roteamento via Derived Streams.
       - **Spark Structured Streaming:** Processamento contínuo em código com PySpark sobre tabelas Delta.
     - As 4 Janelas Temporais do Exame DP-700:
       - **Tumbling Window:** Fixa, contígua, sem sobreposição.
       - **Hopping Window:** Duração fixa com avanço periódico e sobreposição (médias móveis).
       - **Sliding Window:** Avaliação disparada por evento.
       - **Session Window:** Agrupamento por períodos de inatividade.
     - Tratamento de dados atrasados via `withWatermark()` e controle de estado em memória (*RocksDB State Store*).
     - Áudio neural gerado via `edge-tts` com voz Microsoft `pt-BR-AntonioNeural` (`assets/audio/lesson-0010-pt.mp3`).
     - Script Python interativo (`labs/0010-streaming-eventstreams-spark-windows/lab_simulation.py`) executado com sucesso no `.venv/`.
     - Quiz DP-700 cobrando a seleção de Hopping Window para cálculo de média móvel contínua.
  2. **Catálogo de Lições Atualizado (`index.html`):**
     - Adicionado card oficial da Lição 0010.

