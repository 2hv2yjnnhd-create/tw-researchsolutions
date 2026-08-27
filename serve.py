#!/usr/bin/env python3
"""Local dev server for the COA site.

Mirrors GitHub Pages behaviour by serving 404.html for any path that
doesn't match a real file. That's what makes the dedicated per-batch
routes (/pdf/<stack>/<batch>) render the viewer locally the same way
they do in production.

Usage:
  python3 serve.py           # port 8000
  python3 serve.py 8080      # custom port
"""
import http.server
import os
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
ROOT = os.path.dirname(os.path.abspath(__file__))
FALLBACK = os.path.join(ROOT, "404.html")


class Handler(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        if code == 404 and os.path.isfile(FALLBACK):
            with open(FALLBACK, "rb") as f:
                body = f.read()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().send_error(code, message, explain)


os.chdir(ROOT)
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving {ROOT} at http://localhost:{PORT}  (Ctrl-C to stop)")
    httpd.serve_forever()
