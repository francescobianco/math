PORT ?= 5040
PY   ?= python3

.DEFAULT_GOAL := help

.PHONY: help start pull clean

help: ## Show this help
	@echo "Math Wiki — available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

start: ## Serve files locally at http://127.0.0.1:$(PORT) with live reload
	PORT=$(PORT) $(PY) server.py

pull: ## Pull latest changes from remote before pushing
	git pull --rebase origin main

clean: ## Remove temporary files
	@find . -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
	@echo "Done."
