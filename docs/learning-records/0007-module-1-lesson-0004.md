# Registro de Aprendizado: 0007 - Módulo 1 Iniciado (Lição 0004)

- **Data/Hora:** 2026-11-12T22:25:00-03:00
- **Contexto:** Implementação da Lição 0004, abrindo o Módulo 1 (Domínio 1 da Certificação DP-700: Implementar e Gerenciar uma Solução Analítica).
- **Implementações Realizadas:**
  1. **Lição 0004 (`lessons/0004-onelake-capacities-smoothing-domains-spark-pools.html`):**
     - Explicação completa de Capacidades F-SKU e Capacity Units (CUs).
     - Mecânica do algoritmo de Smoothing: janela móvel de 24 horas para background jobs vs. 5 minutos para operações interativas.
     - Estágios de Throttling (Interactive Delay, Interactive Rejection 429, Background Rejection).
     - Governança corporativa com Domínios (Data Mesh) no OneLake.
     - Dimensionamento e concorrência: Starter Pools (inicialização em 5s) vs. Custom Spark Pools (Node size, Autoscale, Dynamic Allocation).
     - Áudio neural gerado via `edge-tts` com voz Microsoft `pt-BR-AntonioNeural` (`assets/audio/lesson-0004-pt.mp3`).
     - Script prático em Python (`labs/0004-onelake-capacities-spark-pools/lab_simulation.py`) rodando dentro de `.venv/` calculando a diluição matemática de CUs e dimensionamento de vCores.
     - Quiz DP-700 cobrando a regra mandatória de licenciamento da capacidade mínima F64.
  2. **Catálogo de Lições Atualizado (`index.html`):**
     - Adicionado card oficial da Lição 0004 com atalho e meta-informações.

