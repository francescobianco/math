#!/usr/bin/env python3
"""Dev server with live reload via Server-Sent Events. No extra dependencies."""
import http.server
import os
import queue
import threading
import time

PORT = int(os.environ.get("PORT", 5040))
WATCH_EXTS = {".html", ".md", ".json"}

RELOAD_SCRIPT = b"""\
<script>
(function(){
  var es = new EventSource("/_livereload");
  es.onmessage = function(){ location.reload(); };
  es.onerror   = function(){ setTimeout(function(){ location.reload(); }, 800); };
})();
</script>
"""

# ---- SSE client registry ----
_clients = []
_lock = threading.Lock()


def _broadcast():
    with _lock:
        for q in _clients:
            try:
                q.put_nowait("r")
            except Exception:
                pass


# ---- file watcher (polling, no deps) ----
def _watch():
    mtimes = {}

    def scan():
        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs
                       if not d.startswith(".") and d not in ("__pycache__",)]
            for f in files:
                if os.path.splitext(f)[1] in WATCH_EXTS:
                    yield os.path.join(root, f)

    for p in scan():
        try:
            mtimes[p] = os.stat(p).st_mtime
        except OSError:
            pass

    while True:
        time.sleep(0.5)
        changed = False
        for p in scan():
            try:
                t = os.stat(p).st_mtime
                if mtimes.get(p) != t:
                    mtimes[p] = t
                    print("  ❖ changed:", p)
                    changed = True
            except OSError:
                pass
        if changed:
            _broadcast()


# ---- request handler ----
class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        # SSE live-reload endpoint
        if self.path == "/_livereload":
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.send_header("Access-Control-Allow-Origin", "*")
            super().end_headers()  # bypass our override for this endpoint
            q = queue.Queue()
            with _lock:
                _clients.append(q)
            try:
                while True:
                    try:
                        q.get(timeout=20)
                        self.wfile.write(b"data: r\n\n")
                        self.wfile.flush()
                    except queue.Empty:
                        self.wfile.write(b": ping\n\n")  # keep-alive heartbeat
                        self.wfile.flush()
            except Exception:
                pass
            finally:
                with _lock:
                    if q in _clients:
                        _clients.remove(q)
            return

        # Serve HTML with injected reload script
        local = self.translate_path(self.path)
        if os.path.isdir(local):
            local = os.path.join(local, "index.html")
        if local.endswith(".html") and os.path.isfile(local):
            with open(local, "rb") as fh:
                body = fh.read()
            body = body.replace(b"</body>", RELOAD_SCRIPT + b"</body>", 1)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        super().do_GET()

    def do_PUT(self):
        if self.path.startswith("/_save/"):
            rel = self.path[len("/_save/"):]
            # Normalise and restrict to library/*.md and index.json only
            import posixpath
            rel = posixpath.normpath(rel).lstrip("/")
            allowed = rel == "index.json" or (
                rel.startswith("library/") and rel.endswith(".md")
                and "/" not in rel[len("library/"):]
            )
            if not allowed:
                self.send_response(403)
                self.end_headers()
                return
            length = int(self.headers.get("Content-Length", 0))
            data = self.rfile.read(length)
            parent = os.path.dirname(rel)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(rel, "wb") as fh:
                fh.write(data)
            print(f"  ✎ saved: {rel}")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return
        self.send_response(405)
        self.end_headers()

    def do_DELETE(self):
        if self.path.startswith("/_delete/"):
            rel = self.path[len("/_delete/"):]
            import posixpath
            rel = posixpath.normpath(rel).lstrip("/")
            allowed = (
                rel.startswith("library/") and rel.endswith(".md")
                and "/" not in rel[len("library/"):]
            )
            if not allowed:
                self.send_response(403)
                self.end_headers()
                return
            try:
                os.remove(rel)
                print(f"  ✗ deleted: {rel}")
            except FileNotFoundError:
                pass
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return
        self.send_response(405)
        self.end_headers()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        if args and str(args[0]).startswith("GET /_livereload"):
            return
        super().log_message(fmt, *args)


if __name__ == "__main__":
    threading.Thread(target=_watch, daemon=True).start()
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"  Math Wiki  →  http://127.0.0.1:{PORT}")
        print("  Live reload active — watching .html .md .json")
        httpd.serve_forever()