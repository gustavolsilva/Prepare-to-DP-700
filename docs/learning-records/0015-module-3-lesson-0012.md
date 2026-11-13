# Registro de Aprendizado: 0015 - Módulo 3 Iniciado (Lição 0012)

- **Data/Hora:** 2026-11-13T10:11:00-03:00
- **Contexto:** Entrega da Lição 0012, inaugurando o Módulo 3 (Governança, Segurança, CI/CD e Otimização: Domínios 1 e 3 do Exame DP-700).
- **Implementações Realizadas:**
  1. **Lição 0012 (`lessons/0012-security-governance-rls-cls-direct-lake-fallback.html`):**
     - **Workspace Roles (RBAC):** Admin, Member, Contributor e Viewer.
     - **Segurança Granular em T-SQL:** Row-Level Security (RLS), Column-Level Security (CLS) e Dynamic Data Masking (DDM) com funções `email()`, `partial()`, `default()`.
     - **Direct Lake Fallback:** O dilema arquitetural de por que RLS no SQL Analytics Endpoint do Lakehouse força o Fallback para DirectQuery e a solução recomendada pela Microsoft (RLS no Semantic Model com Fixed Identity).
     - **Governança Enterprise:** Rótulos de sensibilidade do Microsoft Purview e Endorsement de dados (Promoted vs. Certified).
     - Áudio neural gerado via `edge-tts` com voz Microsoft `pt-BR-AntonioNeural` (`assets/audio/lesson-0012-pt.mp3`).
     - Script Python interativo (`labs/0012-security-governance-rls-cls-fallback/lab_simulation.py`) executado com sucesso no `.venv/`.
     - Quiz DP-700 cobrando a solução de preservação da velocidade do Direct Lake com RLS.
  2. **Catálogo de Lições Atualizado (`index.html`):**
     - Adicionado card oficial da Lição 0012.

