# Registro de Aprendizado 0017: Organização Profissional do Workspace, Suíte de Testes e Documentação

- **Data:** 13 de Novembro de 2026
- **Status:** Concluído com Sucesso

## 1. Motivação e Objetivos
Organizar a topologia de diretórios do repositório para permitir escalabilidade, manutenibilidade por terceiros, facilidade de inicialização local por qualquer pessoa em qualquer sistema operacional (Linux, macOS, Windows) e introduzir testes unitários automatizados para garantir que nenhuma alteração futura quebre lições, simulados ou laboratórios.

## 2. Estrutura de Diretórios Estabelecida

1. **`docs/` (Documentação da Plataforma):**
   - `ARCHITECTURE.md`: Visão arquitetural completa, modelo VARK, 6 lentes de senioridade, tokens do Figma TOTC, motor Pearson VUE e mapeamento com os 3 Domínios do Guia DP-700.
   - `MAINTAINERS.md`: Guia para novos desenvolvedores com checklists para adicionar lições, labs, questões e atualizar o dicionário fonético de áudio neural.

2. **`scripts/` (Ferramental Operacional):**
   - `dev_server.py`: Servidor HTTP local sem cache com headers `Cache-Control: no-store`.
   - `generate_audio.py`: Atalho de geração de áudio neural com pronúncia técnica em inglês.
   - `run_all_labs.py`: Executor em lote dos 15 laboratórios com medição de tempo e saída formatada.
   - `verify_workspace.py`: Auditor automatizado de saúde do workspace.

3. **`tests/` (Suíte Oficial de Testes Unitários - 14 Testes Passando):**
   - `test_lessons_integrity.py`: Validação de DOCTYPE, CSS/JS, 6 lentes de senioridade, áudios MP3 existentes (>100KB), quizzes e links de labs nas 15 lições.
   - `test_exam_questions.py`: Validação de consistência do banco de questões (Single-Choice = 1 correta, Multi-Select = 2 corretas, Case Studies com as 4 abas obrigatórias).
   - `test_labs_execution.py`: Execução automatizada dos 15 laboratórios em Python garantindo retorno de saída 0.
   - `test_reference_and_portal.py`: Validação das 6 folhas de referência e links de navegação no `index.html`.

4. **Raiz do Projeto (Padronização e Portabilidade):**
   - `README.md`: Documentação completa em português com badges, guia passo a passo para Linux/macOS/Windows, arquitetura e instruções.
   - `Makefile`: Comandos rápidos (`make serve`, `make test`, `make labs`, `make verify`).
   - `run.sh`: Inicializador universal com verificação de ambiente virtual e testes prévios.
   - `requirements.txt`: Dependências Python congeladas.

