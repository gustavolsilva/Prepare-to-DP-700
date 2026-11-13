# 🎓 Prepare to DP-700: Microsoft Certified Fabric Data Engineer Associate

> **Plataforma Educacional Interativa, Centro Oficial de Simulados Pearson VUE e Laboratórios Práticos no Padrão Microsoft Learn, 100% Alinhados ao Guia Oficial do Exame DP-700.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Certification](https://img.shields.io/badge/Exam-DP--700-blue?style=flat&logo=microsoft)](https://learn.microsoft.com/en-us/credentials/certifications/fabric-data-engineer-associate/)
[![Test Suite](https://img.shields.io/badge/Tests-15%20Passing-brightgreen.svg)](#suíte-de-testes-unitários)
[![Questions](https://img.shields.io/badge/Question%20Bank-182%20Questions-orange.svg)](#centro-oficial-de-simulados-dp-700)

---

## 🌟 Destaques da Plataforma

* **📚 15 Lições Completas:** Cobertura de 100% dos Domínios 1, 2 e 3 do exame oficial DP-700 divididas em 4 módulos curriculares.
* **🎯 Centro Oficial de Simulados Pearson VUE (`simulados/index.html`):**
  * **Banco com 182 Questões Comentadas:** Mais que o triplo do banco original, cobrindo com precisão as três competências oficiais.
  * Questões de **Escolha Única (*Single-Choice*)** com análise e justificativa individualizada.
  * Questões de **Múltipla Resposta (*Multi-Select*)** exigindo estritamente **2 alternativas corretas** para pontuar.
  * **8 Casos de Estudo Corporativos (*Case Studies*)** em layout de tela dividida (*Split-Screen*) com 4 abas contextuais (*Visão Geral*, *Ambiente Atual*, *Requisitos de Dados*, *Requisitos Técnicos*).
  * **🚩 Marcação para Revisão (*Flag for Review*)** e **📋 Mapa de Questões (*Review Matrix*)** com grade interativa de 182 posições.
  * **Modo Exame Oficial Cronometrado (100 minutos):** Escala de 0 a 1000 pontos (corte em 700) e **Breakdown visual de desempenho por Domínio**.
  * **🎲 Randomização Dinâmica:** Embaralhamento automático de alternativas a cada tentativa para eliminar qualquer vício de posicionamento.
* **🧪 15 Laboratórios no Padrão Microsoft Learn:**
  * Exercícios guiados passo a passo com cenários práticos de negócios, pré-requisitos, diagramas SVG de alta resolução, comandos do terminal e caixas de validação de sucesso.
  * Scripts autônomos em Python executáveis localmente sob `./labs/`.
* **🧠 Metodologia VARK Multissensorial:**
  * **Visual (V):** Diagramas SVG e infográficos colunares interativos.
  * **Aural (A):** Narração técnica neural com voz `pt-BR-AntonioNeural` e pronúncia de mais de 60 termos técnicos em inglês.
  * **Read/Write (R):** Textos técnicos com fundamentação formal e referências oficiais da Microsoft.
  * **Kinesthetic (K):** Simuladores cinestésicos no navegador e laboratórios práticos.
* **👓 6 Lentes Pedagógicas de Senioridade:** Alterne entre os perfis **Unificado**, **Júnior**, **Pleno**, **Sênior & DP-700**, **Staff** e **C-Level / FinOps** com sincronização global em `localStorage`.
* **📑 6 Folhas de Referência Imprimíveis (`reference/`):** Guias compactos e *cheat-sheets* prontos para revisão pré-prova ou exportação em PDF via `window.print()`.
* **🎨 Design System Figma TOTC:** Interface fluida, moderna, responsiva com suporte a **Modo Claro (Light)** e **Modo Escuro (Dark / Midnight Edition)**.

---

## 🚀 Como Executar em Qualquer Ambiente Local

A plataforma foi projetada para rodar de forma leve em qualquer sistema operacional (**Linux**, **macOS** ou **Windows**) sem requerer servidores web de terceiros ou frameworks pesados.

### Pré-requisitos
* **Python 3.10** ou superior instalado ([python.org](https://www.python.org/downloads/)).
* Qualquer navegador web moderno (Chrome, Edge, Firefox, Safari ou Brave).

---

### Opção 1: Inicialização Automática Rápida (Linux / macOS / WSL / Git Bash)

No terminal, execute o script autônomo `run.sh`:
```bash
git clone <URL_DO_REPOSITORIO>
cd Prepare-to-DP-700
./run.sh
```
O script cria o ambiente virtual `.venv`, verifica dependências, roda a suíte de testes unitários e inicia o servidor web sem cache em `http://localhost:8000/`.

---

### Opção 2: Configuração Manual Passo a Passo

#### No Linux / macOS:
```bash
# 1. Clone o repositório e acesse a pasta
git clone <URL_DO_REPOSITORIO>
cd Prepare-to-DP-700

# 2. Crie e ative o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie o servidor web local sem cache
python scripts/dev_server.py
```

#### No Windows (PowerShell):
```powershell
# 1. Clone o repositório e acesse a pasta
git clone <URL_DO_REPOSITORIO>
cd Prepare-to-DP-700

# 2. Crie e ative o ambiente virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie o servidor web local sem cache
python scripts/dev_server.py
```

Abra o seu navegador em: **[http://localhost:8000/](http://localhost:8000/)**

---

## 🛠️ Comandos do Makefile

Se você utiliza `make` (Linux/macOS), os seguintes atalhos estão disponíveis:

```bash
make serve       # Inicia o servidor local sem cache na porta 8000
make test        # Executa todos os 15 testes unitários (tests/)
make labs        # Executa em lote os 15 laboratórios práticos em Python
make verify      # Executa a auditoria completa de saúde do workspace
make build-exam  # Compila o banco modular de 182 questões do simulado
make clean       # Remove arquivos temporários de cache Python
```

---

## 🧪 Suíte de Testes Unitários

O projeto possui uma suíte de testes automatizada construída sobre o módulo padrão `unittest` do Python:

```bash
# Executar todos os testes
./.venv/bin/python -m unittest discover tests

# Ou através do script verificador:
./.venv/bin/python scripts/verify_workspace.py
```

### O que os 15 testes validam:
1. **`tests/test_lessons_integrity.py`:** Garante que todas as 15 lições existem, contêm DOCTYPE, CSS/JS corretos, todas as 6 lentes de senioridade, áudios MP3 válidos e formulários de quiz balanceados.
2. **`tests/test_exam_questions.py`:** Garante que o banco contém no mínimo 174 questões (182 ativas), valida tipos *Single* (1 correta), *Multi* (2 corretas), *Case Studies* (8 casos com 4 abas obrigatórias) e distribuição de distratores (>500 analisados).
3. **`tests/test_labs_execution.py`:** Executa em subprocesso cada um dos 15 laboratórios em Python dentro de `./labs/` e assegura saída com código `0`.
4. **`tests/test_reference_and_portal.py`:** Valida que o portal principal (`index.html`) referencia todas as 15 lições e 6 folhas de referência, e que todas as folhas de referência têm botões de impressão e alternador de tema.

---

## 📂 Estrutura Completa de Diretórios

```
Prepare-to-DP-700/
├── assets/                     # Estilos, scripts globais, áudios e motor do simulador
│   ├── audio/                  # Arquivos de áudio neural gerados (lesson-XXXX-pt.mp3)
│   ├── images/                 # Diagramas SVG de alta fidelidade
│   ├── exam-questions.js       # Banco compilado de 182 questões do simulador
│   ├── exam-simulator.js       # Motor do simulador de exames Pearson VUE
│   ├── exam-simulator.css      # Estilização do simulador e tela dividida (Split-Screen)
│   ├── lens.js                 # Controlador global das 6 lentes e tema Light/Dark
│   ├── quiz.js                 # Validador e randomizador dos quizzes das lições
│   ├── tufte.css               # Design system principal (Figma TOTC)
│   └── vark.css                # Estilização das modalidades VARK
├── docs/                       # Documentação técnica, especificações, planejamento e histórico
│   ├── README.md               # Índice mestre da documentação
│   ├── ARCHITECTURE.md         # Arquitetura detalhada, VARK e design tokens
│   ├── MAINTAINERS.md          # Guia de manutenção e expansão para contribuidores
│   ├── planning/               # Missão, calibragem pedagógica e fontes primárias
│   └── learning-records/       # Diário de bordo cronológico com 20 marcos técnicos
├── labs/                       # 15 Laboratórios práticos em Python (hands-on)
│   ├── 0001-oltp-olap-and-smoothing/
│   ├── ...
│   └── 0015-monitoring-capacity-metrics-dmvs/
├── lessons/                    # 15 Lições completas em HTML (0001 a 0015)
│   ├── 0001-data-engineering-foundations-oltp-olap-fabric.html
│   └── ...
├── reference/                  # 6 Folhas de referência prontas para impressão / PDF
│   ├── 01-glossary-and-fundamentals-visual-guide.html
│   ├── ...
│   └── 06-performance-vorder-clustering-monitoring-cheatsheet.html
├── scripts/                    # Utilitários de desenvolvimento e automação
│   ├── dev_server.py           # Servidor HTTP local sem cache
│   ├── build_full_180_exam_bank.py # Compilador modular do banco de questões
│   ├── exam_data/              # Definições modulares das 182 questões do simulado
│   ├── generate_audio.py       # Gerador central de áudio neural com dicionário fonético
│   ├── run_all_labs.py         # Executor em lote dos 15 laboratórios práticos
│   └── verify_workspace.py     # Script de verificação e auditoria de saúde do projeto
├── simulados/                  # Portal do Centro de Simulados DP-700
│   └── index.html              # Interface do simulador oficial Pearson VUE
├── tests/                      # Suíte oficial de testes unitários automatizados (15 testes)
│   ├── test_exam_questions.py
│   ├── test_labs_execution.py
│   ├── test_lessons_integrity.py
│   └── test_reference_and_portal.py
├── index.html                  # Portal principal com índice interativo e divisão modular
├── Makefile                    # Automação de tarefas para desenvolvedores
├── requirements.txt            # Dependências Python do ambiente virtual
├── run.sh                      # Script de inicialização rápida multiplataforma
└── README.md                   # Este arquivo de documentação
```

---

## 📖 Documentação Adicional
* **[Guia de Arquitetura Técnica (ARCHITECTURE.md)](docs/ARCHITECTURE.md):** Detalhes sobre o modelo pedagógico, tokens do Figma TOTC e motor do simulador.
* **[Guia do Mantenedor (MAINTAINERS.md)](docs/MAINTAINERS.md):** Instruções passo a passo sobre como criar novas lições, adicionar questões e expandir os laboratórios.
* **[Registros de Aprendizado (Learning Records)](docs/learning-records/README.md):** Histórico detalhado dos 20 marcos de desenvolvimento do projeto.

---

## 📄 Licença
Distribuído sob a licença MIT. Consulte o arquivo de licença para mais informações.
