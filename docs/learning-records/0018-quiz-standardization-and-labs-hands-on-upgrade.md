# Registro de Aprendizado 0018: Padronização de Quizzes, Eliminação de Vício de Alternativa e Upgrade dos Labs no Padrão Microsoft Learn

- **Data:** 13 de Novembro de 2026
- **Status:** Concluído com Sucesso

## 1. Motivação e Objetivos
1. **Eliminação de Vício Cognitivo nos Quizzes:** Identificou-se que todas as respostas corretas dos desafios das 15 lições estavam posicionadas estaticamente na alternativa "B", prejudicando a avaliação real do estudante.
2. **Upgrade dos Laboratórios Práticos:** Os laboratórios precisavam evoluir de meros scripts de terminal para uma experiência completa no estilo dos módulos práticos do **Microsoft Learn**, com passos guiados, objetivos claros, pré-requisitos, diagramas visuais e caixas de verificação de sucesso.
3. **Correção de Diagramas SVG:** Resolver sobreposições de texto e estouro de caixas em diagramas de arquitetura (como `fabric-ui-*.svg` e SVGs inline nas Lições 0002, 0012, etc.).

## 2. Implementações Realizadas

### 2.1. Randomização Dinâmica & Distribuição Isomórfica dos Quizzes
- Desenvolvido o utilitário `scripts/standardize_all_quizzes.py` e `scripts/distribute_static_quizzes.py` que reestruturou todos os formulários `.quiz-form` das 15 lições.
- As alternativas estáticas foram balanceadas uniformemente (distribuídas entre A, B, C e D) e o script `assets/quiz.js` foi aprimorado para suportar embaralhamento estocástico a cada carregamento de página, garantindo que mesmo após recarregar a lição, a alternativa correta ocupe posições variadas.

### 2.2. Upgrade dos 15 Laboratórios no Padrão Microsoft Learn
- O script `scripts/upgrade_all_labs.py` aplicou a reestruturação dos 15 laboratórios práticos em `lessons/*.html`:
  - Seção com **Objetivo do Laboratório & Cenário de Negócio**.
  - **Tabela de Pré-requisitos & Ferramentas** (OneLake, Spark, T-SQL, KQL).
  - **Passo a Passo Guiado (Exercício Prático)** com comandos do terminal, telas simuladas em SVG e janelas de execução em código ASCII.
  - **Critérios de Validação & Checkpoints de Sucesso** para certificar que os dados foram gerados ou processados corretamente.
  - Comando executável local correspondente em `./.venv/bin/python labs/XXXX-*/lab_simulation.py`.

### 2.3. Auditoria e Correção de Diagramas SVG
- Diagnosticados e corrigidos problemas de overflow e quebra de fontes nos diagramas vetoriais (`assets/images/fabric-ui-*.svg`), garantindo renderização nítida em telas de alta densidade de pixels (Retina/4K) e perfeito contraste no tema escuro.

