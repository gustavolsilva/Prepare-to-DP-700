# NOTES.md - Calibragem, Perfil e Diretrizes Pedagógicas

## Perfil do Usuário & Propósito do Projeto
- **Perfil do Instrutor / Usuário Líder:** Engenheiro de Dados Sênior (10+ anos de experiência, certificado Databricks Data Engineer Professional, domínio pleno de Apache Spark, Delta Lake, SQL Server e arquitetura Medallion).
- **Missão do Produto:** Criar uma plataforma educacional completa de Engenharia de Dados no Microsoft Fabric + Certificação DP-700 que atenda desde iniciantes sem experiência prévia em dados (Júnior/Transição) até profissionais Staff, Especialistas e C-Level (Head/CTO).

## Arquitetura Multi-Lens (Progressive Disclosure)
Cada lição HTML é construída sobre quatro camadas navegáveis via `./assets/lens.js` e estilizadas com `./assets/tufte.css`:
1. 🌱 **Lente Júnior / Fundamentos:** Explicação conceitual a partir do zero, sem pré-requisitos presumidos, com analogias visuais e glossário.
2. 🛠️ **Lente Sênior / DP-700:** Implementação prática direta, foco cirúrgico no Guia Oficial DP-700 e armadilhas da prova.
3. ⚙️ **Lente Staff / Under-the-Hood:** Detalhes de baixo nível, motores C++ (Velox/Gluten), algoritmos de concorrência, ordenação binária e matemática de Smoothing/Throttling.
4. 🏛️ **Lente C-Level / FinOps:** TCO, dimensionamento de F-SKUs, governança com Microsoft Purview, estratégias de Data Mesh e impacto no negócio.

## Isolamento de Ambiente
- Toda dependência Python local deve ser instalada e executada estritamente dentro do ambiente virtual `.venv/`.
- Nunca utilizar flags globais ou instalar pacotes no ambiente do sistema operacional.

## Regras de Quizzes e Simulados Oficiais DP-700 (skill teach + Padrão Pearson VUE)
- **Quizzes de Retenção nas Lições:**
  - Alternativas com **exatamente a mesma contagem de palavras** (isomorfismo estrito) para evitar pistas visuais de comprimento.
  - Posição da resposta correta variando entre as opções.
  - Explicação imediata de cada distrator após a seleção do usuário.
- **Centro de Simulados do Exame DP-700 (`simulados/`):**
  - Formato idêntico à experiência real da prova Microsoft DP-700 (100 minutos, pontuação de 0 a 1000, aprovação em 700 pontos, distribuído entre os 3 Domínios Oficiais: 30-35% cada).
  - **Tipo 1 — Escolha Única (Single-Choice - 1 correta):** Seleção de arquitetura, troubleshooting de erros e avaliação de trechos de código em **PySpark**, **T-SQL** e **KQL**.
  - **Tipo 2 — Múltipla Resposta (Multi-Select - 2 corretas):** Questões explícitas do tipo *"Escolha duas alternativas"* (seja para compor uma solução em duas etapas ou indicar duas formas independentes de resolver o requisito), exigindo marcação exata de 2 checkboxes.
  - **Tipo 3 — Casos de Uso / Estudos de Caso (Case Studies Split-Screen):** Cenários empresariais extensos (ex: *Contoso Retail*, *Litware IoT & Energy*, *Fabrikam Financial Services*) com painel de abas à esquerda (`Overview`, `Existing Environment`, `Data Requirements`, `Technical Requirements`) e painel de questões à direita exigindo cruzamento de restrições técnicas (ex: *"Minimize development effort"*, *"Prevent data duplication"*, *"Ensure caching is disabled"*, *"Workspace Identity / Private Link"*).

