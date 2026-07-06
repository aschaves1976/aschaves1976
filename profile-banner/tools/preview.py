#!/usr/bin/env python3
"""Start local HTTP server to preview the banner."""
from __future__ import annotations

import argparse
import http.server
import socketserver
import sys
import webbrowser
from pathlib import Path

from lib.paths import BANNER_SRC, ROOT


HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Banner Preview</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #0f172a; color: #e2e8f0; min-height: 100vh; }
    header { padding: 1rem 1.5rem; border-bottom: 1px solid #1e293b; }
    main { padding: 2rem 1.5rem; max-width: 1500px; margin: 0 auto; }
    .frame { background: #020617; border: 1px solid #1e293b; border-radius: 8px; padding: 1rem; margin-bottom: 2rem; }
    .frame h2 { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; color: #94a3b8; margin-bottom: 0.75rem; }
    img { width: 100%; height: auto; display: block; }
    .light { background: #f8fafc; }
  </style>
</head>
<body>
  <header><h1>Profile Banner Preview</h1></header>
  <main>
    <div class="frame">
      <h2>Dark background</h2>
      <img src="/src/banner.svg" alt="Banner preview"/>
    </div>
    <div class="frame light">
      <h2>Light background</h2>
      <img src="/src/banner.svg" alt="Banner preview"/>
    </div>
  </main>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Preview banner in browser")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--no-open", action="store_true")
    args = parser.parse_args()

    if not BANNER_SRC.exists():
        print(f"ERROR: {BANNER_SRC} not found")
        return 1

    preview_html = ROOT / "preview.html"
    preview_html.write_text(HTML, encoding="utf-8")

    handler = http.server.SimpleHTTPRequestHandler

    class QuietHandler(handler):
        def log_message(self, format: str, *args) -> None:
            pass

    os.chdir = __import__("os").chdir
    os.chdir(ROOT)

    with socketserver.TCPServer(("", args.port), QuietHandler) as httpd:
        url = f"http://localhost:{args.port}/preview.html"
        print(f"Serving {ROOT}")
        print(f"Preview: {url}")
        if not args.no_open:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
