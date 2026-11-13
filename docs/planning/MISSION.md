# Mission: Microsoft Fabric Data Engineering (From Zero to DP-700 & Enterprise Production)

## Why
Capacitar qualquer profissional — desde quem tem 0 anos em dados até Engenheiros Sênior, Staff e Executivos (C-Level/Head) — a dominar o ecossistema do Microsoft Fabric, aplicando padrões de arquitetura corporativa em produção e obtendo a aprovação no Exame Oficial DP-700 (Microsoft Certified: Fabric Data Engineer Associate).

## Success looks like
- O aluno iniciante/Júnior compreende os conceitos fundamentais de armazenamento analítico (OLAP, Parquet, Delta Lake, Medallion, Star Schema) e opera o Fabric com confiança.
- O engenheiro Pleno/Sênior domina PySpark, T-SQL, KQL, pipelines de orquestração, segurança granular (RLS/CLS/DDM) e passa no exame DP-700 com pontuação ≥ 850.
- O Arquiteto/Staff Engineer domina o funcionamento interno (Native Execution Engine, Smoothing de 24h, Concurrency, V-Order em nível de row group, Direct Lake fallback).
- O C-Level/Head de Dados obtém uma visão clara de FinOps (Capacity Units, F-SKUs, sizing, controle de custos), governança enterprise (Purview, Domains) e TCO.
- Todos os laboratórios práticos (`./labs/`) e scripts executam de forma isolada dentro do ambiente virtual (`.venv/`), sem afetar o sistema operacional global.

## Constraints
- Basear todo o currículo rigorosamente no Guia Oficial do Exame DP-700 da Microsoft (3 domínios oficiais: Implementar e Gerenciar [30-35%], Ingerir e Transformar [30-35%], Monitorar e Otimizar [30-35%]).
- Progressive Disclosure: cada lição permite visualização dedicada aos 6 perfis selecionáveis no início do curso (`unificado`, `junior`, `pleno`, `senior`, `staff`, `clevel`), com suporte completo a **Light Mode** e **Dark Mode** inspirado no layout TOTC E-Learning (Figma).
- **Simulado Oficial DP-700 Fiel à Prova Real (Pearson VUE):**
  - Sessão dedicada de Simulado com amplo banco de questões cobrindo 100% dos tópicos reais da prova.
  - **Questões de 1 Alternativa Correta (Single-Choice):** Múltipla escolha tradicional (incluindo análise de código T-SQL, PySpark e KQL).
  - **Questões de 2 Alternativas Corretas (Multiple-Response / Multi-Select):** Com caixas de seleção (checkboxes) onde o candidato deve marcar exatamente 2 respostas corretas (*"Cada seleção correta apresenta parte da solução / uma solução completa. Escolha duas."*).
  - **Questões de Caso de Uso / Estudo de Caso (Case Studies em Split-Screen):** Interface dividida idêntica ao exame real com abas navegáveis à esquerda (`Visão Geral`, `Ambiente Atual`, `Requisitos de Dados`, `Requisitos Técnicos e de Segurança`) e bateria de questões conectadas às restrições do cenário à direita.
  - Modos de **Treino Comentado** (feedback imediato por alternativa) e **Exame Cronometrado** (100 minutos, escala 0–1000, nota de corte 700, diagnóstico por domínio).
- Quizzes padronizados sem pistas visuais (alternativas com contagem rigorosa de palavras).
- Áudio neural em Português (`edge-tts` `pt-BR-AntonioNeural`) com dicionário fonético auditado para termos técnicos em inglês.
- Todo código local deve rodar dentro de `.venv/`.

## Out of scope
- Administração profunda de Power BI / DAX avançado voltado para visualização puramente estética (fora do escopo do DP-700).
- Conceitos de infraestrutura de rede legada on-premises que não dialoguem com os conectores e gateways do Fabric.

