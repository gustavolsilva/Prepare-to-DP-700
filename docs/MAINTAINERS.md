# Guia do Mantenedor & Desenvolvedor: Prepare to DP-700

Este documento orienta engenheiros, educadores e mantenedores sobre como evoluir, testar e documentar o repositório sem introduzir quebras ou inconsistências de design.

---

## 1. Estrutura de Diretórios do Projeto

```
Prepare-to-DP-700/
├── assets/                     # Estilos, scripts globais, imagens e áudios
│   ├── audio/                  # Arquivos de áudio neural gerados (lesson-XXXX-pt.mp3)
│   ├── exam-questions.js       # Banco compilado de 182 questões do simulador DP-700
│   ├── exam-simulator.js       # Motor do simulador (Pearson VUE)
│   ├── exam-simulator.css      # Estilos dedicados do simulador e split-screen
│   ├── lens.js                 # Gerenciador global de lentes de senioridade e temas
│   ├── quiz.js                 # Validador de quizzes embutidos nas lições
│   ├── tufte.css               # Design system base inspirado no Figma TOTC
│   └── vark.css                # Estilos dos botões e layouts pedagógicos VARK
├── docs/                       # Central de documentação técnica, specs e histórico
│   ├── README.md               # Índice mestre da documentação
│   ├── ARCHITECTURE.md         # Arquitetura geral, VARK, 6 lentes e design tokens
│   ├── MAINTAINERS.md          # Este guia para contribuidores e mantenedores
│   ├── planning/               # Especificações do curso, missão e fontes oficiais
│   └── learning-records/       # Diário de bordo cronológico de decisões técnicas (0001 a 0020)
├── labs/                       # 15 Laboratórios práticos hands-on em Python
│   ├── 0001-oltp-olap-and-smoothing/
│   ├── ...
│   └── 0015-monitoring-capacity-metrics-dmvs/
├── lessons/                    # Lições interativas em HTML (0001 a 0015)
│   └── 0001-*.html             # Páginas com 6 lentes, labs guiados e quizzes
├── reference/                  # Folhas de referência resumidas prontas para impressão A4
│   └── 01-*.html               # Cheat sheets de consulta rápida (01 a 06)
├── scripts/                    # Scripts operacionais e de automação
│   ├── dev_server.py           # Servidor local HTTP sem cache (porta 8000)
│   ├── build_full_180_exam_bank.py # Compilador do banco de 182 questões do simulador
│   ├── exam_data/              # Dados modulares do simulador (domain1, domain2, domain3, case_studies)
│   ├── generate_audio.py       # Atalho para síntese de voz neural com fonética
│   ├── run_all_labs.py         # Executor em lote dos 15 laboratórios práticos
│   └── verify_workspace.py     # Auditor de integridade e saúde do repositório
├── simulados/                  # Página do Centro Oficial de Simulados DP-700
│   └── index.html              # Interface do simulador oficial Pearson VUE
├── tests/                      # Suíte oficial de testes unitários automatizados (15 testes)
│   ├── test_exam_questions.py  # Validação das regras do banco e simulador
│   ├── test_labs_execution.py  # Execução dos scripts Python dos 15 labs
│   ├── test_lessons_integrity.py # Integridade de HTML, CSS, JS e áudios
│   └── test_reference_and_portal.py # Validação de links do catálogo e referências
├── index.html                  # Portal principal de entrada e índice interativo do curso
├── Makefile                    # Atalhos (make serve, test, labs, verify, build-exam, clean)
├── requirements.txt            # Dependências Python travadas
├── run.sh                      # Inicializador universal multiplataforma
└── README.md                   # Documentação principal para o usuário final
```

---

## 2. Como Adicionar ou Modificar Questões no Simulador

As questões do simulador são organizadas de forma modular em `scripts/exam_data/`:
- `scripts/exam_data/domain1.py` (Domínio 1)
- `scripts/exam_data/domain2.py` (Domínio 2)
- `scripts/exam_data/domain3.py` (Domínio 3)
- `scripts/exam_data/case_studies.py` (Casos de Estudo Split-Screen)

### 2.1. Estrutura Padrão de Questão
```python
{
    "id": "d1_q01",
    "domain": "domain1",
    "type": "single",  # ou "multi"
    "title": "Título Técnico",
    "question": "Enunciado detalhado no padrão Pearson VUE...",
    "options": [
        {"id": "A", "text": "Texto A", "isCorrect": False},
        {"id": "B", "text": "Texto B", "isCorrect": True},
        {"id": "C", "text": "Texto C", "isCorrect": False},
        {"id": "D", "text": "Texto D", "isCorrect": False}
    ],
    "explanation": make_explanation(
        "Por que B é a alternativa correta...",
        [
            "<strong>A:</strong> Motivo do erro...",
            "<strong>C e D:</strong> Motivo do erro..."
        ],
        "Dica essencial que cai na prova DP-700..."
    )
}
```

### 2.2. Compilação do Banco
Após editar os módulos sob `scripts/exam_data/`, execute:
```bash
make build-exam
# ou
./.venv/bin/python scripts/build_full_180_exam_bank.py
```
Isso atualizará `assets/exam-questions.js`. Em seguida, execute `make test` para certificar que os critérios de aprovação foram atendidos.

---

## 3. Como Adicionar uma Nova Lição (Checklist)

Ao criar uma nova lição (ex: `lessons/0016-*.html`):
1. **Copie o Boilerplate Padrão:** Use `lessons/0015-*.html` como base.
2. **Preserve a Estrutura Semântica Obrigatória:**
   - Sidebar com links de navegação para as seções `#bloco-contexto`, `#bloco-audio`, `#bloco-teoria`, `#bloco-pratica` e `#bloco-quiz`.
   - Barra de lentes com botões para as 6 senioridades: `data-lens="unificado"`, `junior`, `pleno`, `senior`, `staff`, `clevel`.
   - Laboratório no padrão Microsoft Learn com Pré-requisitos, Passo a Passo e Validação de Sucesso.
   - Desafio com formulário `.quiz-form` e alternativas isomórficas balanceadas.
3. **Crie o Laboratório Python:** Crie `labs/0016-nome-da-licao/lab_simulation.py`.
4. **Atualize o Portal Principal (`index.html`):** Adicione a lição no `#quick-index` e na seção do módulo correspondente.
5. **Execute a Suíte de Testes:**
   ```bash
   make test
   make verify
   ```
