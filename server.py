#!/usr/bin/env python3
"""Server di sviluppo locale per il Math Wiki.

Serve l'index.html statico e offre una piccola API che scrive i documenti
come file Markdown dentro ./content, rigenerando il manifesto index.json.

Solo libreria standard, nessuna dipendenza:

    python3 server.py [porta]      # default 8080
    python3 server.py --build      # rigenera solo content/index.json ed esce
"""
import json
import os
import re
import sys
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(ROOT, "content")
VALID_TYPES = {"paper", "book", "notes"}


def now_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(text):
    text = (text or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "senza-titolo"


def safe_slug(slug):
    """Sanifica uno slug ricevuto dal client per evitare path traversal."""
    return re.sub(r"[^a-z0-9-]", "", (slug or "").lower())


def parse_frontmatter(raw):
    meta, body = {}, raw
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    meta[key.strip()] = value.strip()
            body = parts[2].lstrip("\n")
    return meta, body


def list_documents():
    docs = []
    if os.path.isdir(CONTENT_DIR):
        for name in sorted(os.listdir(CONTENT_DIR)):
            if not name.endswith(".md"):
                continue
            with open(os.path.join(CONTENT_DIR, name), encoding="utf-8") as fh:
                meta, _ = parse_frontmatter(fh.read())
            slug = name[:-3]
            docs.append({
                "slug": slug,
                "title": meta.get("title", slug),
                "type": meta.get("type", "notes"),
                "created": meta.get("created", ""),
                "updated": meta.get("updated", ""),
            })
    docs.sort(key=lambda d: d.get("updated", ""), reverse=True)
    return docs


def write_manifest():
    os.makedirs(CONTENT_DIR, exist_ok=True)
    docs = list_documents()
    with open(os.path.join(CONTENT_DIR, "index.json"), "w", encoding="utf-8") as fh:
        json.dump({"documents": docs}, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    return docs


def save_document(data):
    title = (data.get("title") or "Senza titolo").strip()
    dtype = data.get("type") if data.get("type") in VALID_TYPES else "notes"
    content = data.get("content") or ""
    slug = safe_slug(data.get("slug"))
    created = data.get("created") or now_iso()
    updated = now_iso()

    if slug:
        path = os.path.join(CONTENT_DIR, slug + ".md")
        if os.path.exists(path):  # editing: conserva la data di creazione
            meta, _ = parse_frontmatter(open(path, encoding="utf-8").read())
            created = meta.get("created", created)
    else:
        slug = slugify(title)
        path = os.path.join(CONTENT_DIR, slug + ".md")
        n = 2
        while os.path.exists(path):
            slug = f"{slugify(title)}-{n}"
            path = os.path.join(CONTENT_DIR, slug + ".md")
            n += 1

    os.makedirs(CONTENT_DIR, exist_ok=True)
    front = (
        f"---\ntitle: {title}\ntype: {dtype}\n"
        f"created: {created}\nupdated: {updated}\n---\n\n{content.rstrip()}\n"
    )
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(front)
    write_manifest()
    return {"slug": slug, "title": title, "type": dtype,
            "created": created, "updated": updated}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def _send_json(self, code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.split("?")[0] == "/api/documents":
            self._send_json(200, {"documents": list_documents()})
            return
        super().do_GET()

    def do_POST(self):
        if self.path.split("?")[0] != "/api/documents":
            self._send_json(404, {"error": "endpoint sconosciuto"})
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length) or b"{}")
            saved = save_document(data)
            self._send_json(200, saved)
        except Exception as exc:  # noqa: BLE001 - dev server
            self._send_json(400, {"error": str(exc)})

    def log_message(self, fmt, *args):  # output più sobrio
        sys.stderr.write("  %s\n" % (fmt % args))


def main():
    args = sys.argv[1:]
    if "--build" in args:
        docs = write_manifest()
        print(f"index.json rigenerato: {len(docs)} documenti.")
        return

    port = int(args[0]) if args else 8080
    write_manifest()
    httpd = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"  Math Wiki  →  http://127.0.0.1:{port}")
    print("  Ctrl+C per fermare.\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server fermato.")


if __name__ == "__main__":
    main()