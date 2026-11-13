# Makefile para o Projeto Prepare-to-DP-700
# Atalhos para execução local, testes, simulador e laboratórios

PYTHON ?= ./.venv/bin/python
PORT ?= 8000

.PHONY: help serve test labs verify build-exam clean

help:
	@echo "=========================================================================="
	@echo "Comandos Disponíveis para o Preparatório DP-700:"
	@echo "=========================================================================="
	@echo "  make serve       - Inicia o servidor HTTP sem cache na porta $(PORT)"
	@echo "  make test        - Executa a suíte completa de testes unitários (tests/)"
	@echo "  make labs        - Executa em lote todos os 15 laboratórios práticos"
	@echo "  make verify      - Executa a auditoria completa de saúde do workspace"
	@echo "  make build-exam  - Compila o banco oficial de 182 questões do simulado"
	@echo "  make clean       - Remove caches e saídas temporárias de execução dos labs"
	@echo "=========================================================================="

serve:
	@$(PYTHON) scripts/dev_server.py $(PORT)

test:
	@$(PYTHON) -m unittest discover tests

labs:
	@$(PYTHON) scripts/run_all_labs.py

verify:
	@$(PYTHON) scripts/verify_workspace.py

build-exam:
	@$(PYTHON) scripts/build_full_180_exam_bank.py

clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type f -name "*.log" -delete 2>/dev/null || true
	@rm -rf labs/*/bronze labs/*/silver_delta labs/*/external_aws_s3_bucket labs/*/external_adls_gen2 labs/*/lakehouse_onelake labs/*/mirrored_azure_sql 2>/dev/null || true
	@echo "Workspace limpo com sucesso."
