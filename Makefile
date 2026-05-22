PORT ?= 5040
PY   ?= python3

.DEFAULT_GOAL := help

.PHONY: help start build clean

help: ## Show this help
	@echo "Math Wiki — available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

start: ## Serve files locally at http://127.0.0.1:$(PORT) (read-only)
	$(PY) -m http.server $(PORT) --bind 127.0.0.1

build: ## Rebuild content/index.json from the .md files
	@$(PY) -c "$$BUILD_MANIFEST_PY"

clean: ## Remove temporary files
	@find . -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
	@echo "Done."

# Tree manifest generator (also used by the GitHub Action).
define BUILD_MANIFEST_PY
import json, os
content = "content"
def frontmatter(raw):
    meta = {}
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    meta[key.strip()] = value.strip()
    return meta
docs = []
for name in sorted(os.listdir(content)):
    if not name.endswith(".md"):
        continue
    with open(os.path.join(content, name), encoding="utf-8") as fh:
        meta = frontmatter(fh.read())
    docs.append({
        "slug": name[:-3],
        "title": meta.get("title", name[:-3]),
        "type": meta.get("type", "notes"),
        "created": meta.get("created", ""),
        "updated": meta.get("updated", ""),
    })
docs.sort(key=lambda d: d.get("updated", ""), reverse=True)
with open(os.path.join(content, "index.json"), "w", encoding="utf-8") as fh:
    json.dump({"documents": docs}, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
print("index.json rebuilt: %d documents." % len(docs))
endef
export BUILD_MANIFEST_PY
