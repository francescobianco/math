PORT ?= 5040
PY   ?= python3

.DEFAULT_GOAL := help

.PHONY: help start build clean

help: ## Mostra questo aiuto
	@echo "Math Wiki — comandi disponibili:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

start: ## Avvia il wiki in locale su http://127.0.0.1:$(PORT)
	$(PY) server.py $(PORT)

build: ## Rigenera content/index.json dai file .md presenti
	$(PY) server.py --build

clean: ## Rimuove file temporanei
	@find . -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
	@echo "Pulizia completata."