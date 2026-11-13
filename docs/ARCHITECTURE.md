# Arquitetura Técnica & Pedagógica: Preparatório DP-700

## 1. Visão Geral do Sistema
O projeto **Prepare to DP-700** é uma plataforma educacional interativa de alta fidelidade desenhada para preparar engenheiros e arquitetos de dados para a certificação oficial **Microsoft Certified: Fabric Data Engineer Associate (Exam DP-700)**.

A plataforma é construída 100% sobre tecnologias web padronizadas (HTML5 semântico, CSS3 com Design Tokens do Figma TOTC, Vanilla JavaScript ES6+) e rotinas de backend/laboratório em Python 3.10+, sem dependência de frameworks pesados (como React ou Angular), garantindo carregamento instantâneo, portabilidade e independência de servidores complexos.

---

## 2. Pilares Pedagógicos

### 2.1. O Modelo Multidimensional VARK
A aprendizagem é distribuída através das 4 modalidades do modelo VARK:
- **Visual (V):** Diagramas SVG interativos, esquemas colunares Parquet vs. Linhas, fluxos de arquitetura OneLake e topologias de rede.
- **Aural (A):** Narrações completas em áudio geradas por síntese neural de voz (`Microsoft pt-BR-AntonioNeural`), com um dicionário fonético que traduz mais de 60 termos técnicos em inglês para a pronúncia correta da língua de origem.
- **Read/Write (R):** Textos técnicos detalhados com rigor matemático e referências oficiais da documentação do Microsoft Fabric, segmentados por 6 lentes de senioridade.
- **Kinesthetic (K):** Simuladores visuais interativos em JavaScript no navegador e 15 laboratórios práticos estruturados no padrão Microsoft Learn em Python dentro de `./labs/`.

### 2.2. As Seis Lentes de Senioridade (`assets/lens.js`)
Cada lição possui 6 visualizações de conteúdo mantidas sincronizadas globalmente via `localStorage` (`fabric_dp700_global_lens`):
1. **Unificado (`unificado`):** Visão completa e canônica que equilibra conceitos teóricos, código prático e exigências do exame.
2. **Júnior (`junior`):** Foco em fundamentos, metáforas do cotidiano e intuição analítica.
3. **Pleno (`pleno`):** Foco em implementação prática, comandos T-SQL/PySpark/KQL, pipelines e orquestração.
4. **Sênior (`senior`):** Foco em armadilhas de arquitetura, pegadinhas e critérios do guia de estudos oficial DP-700.
5. **Staff (`staff`):** Foco em mecanismos sob o capô (*under the hood*), serialização binária de arquivos Parquet, min/max skipping e internals do V-Order e Delta Lake.
6. **C-Level (`clevel`):** Foco em governança executiva, conformidade regulatória (SOX, LGPD/GDPR), FinOps, Capacidades F-SKU e TCO.

---

## 3. Design System & Tokens Visuais (Figma TOTC)
O visual da plataforma é diretamente inspirado no template de E-Learning **TOTC Community do Figma**, estruturado em `assets/tufte.css` e `assets/vark.css`:

### 3.1. Paleta de Cores Principais
- **Brand Teal (Cor Primária):** `#49BBBD` / Dark: `#00CBB8`
- **Brand Dark Blue (Títulos):** `#2F327D` / Dark: `#60A5FA`
- **Brand Orange (Destaques e Simulador):** `#F48C06`
- **Brand Coral (Alertas e Erros):** `#EE645B`
- **Fundo Claro:** `#FDFBF7` / `#FFFFFF`
- **Fundo Escuro (Midnight Edition):** `#0F172A` / `#1E293B`

### 3.2. Sincronização de Tema Light/Dark
- Gerenciado pela função global `window.toggleAppTheme()`.
- Persistido na chave `fabric_dp700_theme` do `localStorage`.
- Aplica o atributo `data-theme="dark"` no elemento `<html>` e `<body>`.

---

## 4. Arquitetura do Simulador Oficial Pearson VUE (`assets/exam-simulator.js`)
O simulador oficial reproduz com rigor a experiência real da prova de certificação da Microsoft:
- **Banco de 182 Questões Comentadas:** Mais que o triplo do banco original, cobrindo com profundidade todas as competências do guia de estudos oficial.
- **Modo Treino Comentado:** Exibe filtros dinâmicos por Domínio (1, 2, 3) e por Tipo de Questão, explicações técnicas detalhadas e justificativas imediatas divididas em:
  - `✅ Por que a alternativa correta está certa`
  - `❌ Análise dos Distratores`
  - `💡 Dica de Prova DP-700`
- **Modo Exame Oficial Cronometrado:** Temporizador de 100 minutos com alerta nos últimos 5 minutos, bloqueio de feedback imediato, pontuação oficial escalada (0 a 1000 pontos, corte em 700) e **Breakdown visual de desempenho pelos 3 Domínios**.
- **🚩 Marcação para Revisão (Flag for Review):** Permite sinalizar questões para verificação posterior (atalho `R`).
- **📋 Matriz de Questões (Question Matrix Modal):** Grade completa de 182 posições com cores de status (Respondida, Em Branco, Marcada, Correta e Incorreta).
- **Estudos de Caso (Case Studies) em Split-Screen:** 8 casos de estudo com 4 abas obrigatórias (*Visão Geral*, *Ambiente Atual*, *Requisitos de Dados* e *Requisitos Técnicos*).
- **🎲 Randomização Estocástica:** Alternativas embaralhadas a cada execução para eliminar vícios de posição.

---

## 5. Mapeamento com o Guia Oficial DP-700
O currículo cobre integralmente os três domínios do exame com os pesos oficiais estabelecidos pela Microsoft:

| Domínio Oficial DP-700 | Peso no Exame | Lições Cobertas | Questões no Banco |
| :--- | :---: | :---: | :---: |
| **Domínio 1: Implementar e gerenciar um ambiente analítico** | 15–20% | Lições 0001, 0004, 0005, 0006, 0012, 0013 | 38 + Casos de Estudo |
| **Domínio 2: Ingerir e transformar dados** | 40–45% | Lições 0002, 0003, 0007, 0008, 0009, 0010, 0011 | 82 + Casos de Estudo |
| **Domínio 3: Monitorar e otimizar uma solução analítica** | 20–25% | Lições 0014, 0015 | 38 + Casos de Estudo |
| **Total Geral** | **100%** | **15 Lições + 6 Referências** | **182 Questões (3x Banco)** |

---

## 6. Arquitetura do Portal Principal (`index.html`)
- **Navegação Superior:** Barra fixa com atalhos diretos para cada módulo (`#modulo-0`, `#modulo-1`, `#modulo-2`, `#modulo-3`, `#simulados` e `#referencias`).
- **Diretório Rápido (`#quick-index`):** Grade de chips clicáveis para acesso instantâneo a cada uma das 15 lições sem necessidade de rolagem manual.
- **Botões de Ação Padronizados (`.btn-access-lesson`):** Componente em largura total com sombra e animação de seta no hover, eliminando quebras de layout.
