# Exercício Prático: CI/CD com Integração Git e Deployment Pipelines

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
Configurar o ciclo de vida de desenvolvimento de software (DevOps) no Fabric, conectando workspaces ao Git e utilizando Deployment Pipelines de 3 estágios (Dev &gt; Test &gt; Prod) com regras de parâmetros de conexão.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Vincular o Workspace ao Repositório Git
1. Nas configurações do Workspace, clique em Integração com Git (Git integration).
2. Conecte à sua conta do Azure DevOps ou GitHub, selecione o repositório e a branch dev.
3. Observe a barra de status de sincronização indicando alterações pendentes de commit.

#### Tarefa 2: Configurar o Pipeline de Implantação de 3 Estágios
1. Crie um novo Deployment Pipeline.
2. Atribua o workspace de Desenvolvimento ao estágio 1 (Dev), Teste ao estágio 2 (Test) e Produção ao estágio 3 (Prod).
3. Configure Deployment Rules para substituir conexões de banco de dados e nomes de Lakehouses entre os estágios.
4. Execute a promoção de artefatos de Dev para Test com validação automática.

---

## ⚠️ Ponto Crítico para o Exame DP-700
Atenção para o exame: Deployment Pipelines facilitam a transição entre ambientes; as Regras de Parâmetros garantem que o código em Produção aponte automaticamente para o Lakehouse de Produção sem necessidade de editar manualmente os scripts.

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0013-cicd-git-deployment-pipelines/lab_simulation.py
```
