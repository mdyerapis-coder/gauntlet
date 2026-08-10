#!/usr/bin/env python3
"""
gauntlet-proxy.py — tiny same-origin CORS proxy for The Agent Engineer's Gauntlet.

WHY: The browser blocks cross-origin calls to opencode.ai/zen (and most cloud LLM
APIs) unless they send permissive CORS headers. This proxy runs on YOUR machine,
forwards the request server-side, and returns it to the browser from localhost —
so no CORS block.

USAGE:
  1. python3 gauntlet-proxy.py            # serves http://localhost:8000
  2. In the gauntlet app's ⚙ AI Coder gear:
       Provider: OpenCode
       Base URL: http://localhost:8000/zen/v1     <-- points at the proxy
       (the proxy forwards /zen/* to https://opencode.ai/zen/*)
       API key: your Zen key
       Model: deepseek-v4-flash-free
  3. Hit "Run with AI".

The proxy forwards ANY path you give it:
  /zen/v1/chat/completions  -> https://opencode.ai/zen/v1/chat/completions
  /v1/chat/completions      -> https://api.openai.com/v1/chat/completions   (if you edit TARGETS)
Adding another provider is just another entry in TARGETS below.

No external deps. Python 3.8+.
"""
import http.server
import urllib.request
import json
import sys

PORT = 8000

# Prefix -> upstream base. Add more to route other providers through the proxy.
TARGETS = {
    "/zen": "https://opencode.ai/zen",
    "/openrouter": "https://openrouter.ai/api",
    "/openai": "https://api.openai.com",
    "/anthropic": "https://api.anthropic.com",
}

# If the browser path doesn't match a known prefix, try the raw hostless form
# (e.g. a path starting with /v1 is treated as OpenAI-compatible against OpenCode Zen).
FALLBACK = "https://opencode.ai"


class Handler(http.server.BaseHTTPRequestHandler):
    def _send(self, code, body, headers=None):
        self.send_response(code)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        if headers:
            for k, v in headers.items():
                self.send_header(k, v)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def do_OPTIONS(self):
        self._send(204, b"")

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else b""
        self._proxy(body)

    def do_GET(self):
        self._proxy(b"")

    def _proxy(self, body):
        path = self.path.split("?", 1)[0]
        target = None
        for prefix, base in TARGETS.items():
            if path.startswith(prefix):
                target = base + path[len(prefix):]
                break
        if target is None:
            # default: treat leading /v1 etc as OpenCode Zen
            target = FALLBACK + path

        # Forward only safe headers (drop Host; let urllib set it)
        fwd = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
            "Origin": f"http://{self.headers.get('Host', 'localhost')}",
        }
        for h in ("authorization", "content-type", "anthropic-version",
                  "anthropic-dangerous-direct-browser-access"):
            if h in self.headers:
                fwd[h] = self.headers[h]

        req = urllib.request.Request(target, data=body or None, headers=fwd, method=self.command)
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = resp.read()
                ctype = resp.headers.get("content-type", "application/json")
                self._send(resp.status, data, {"Content-Type": ctype})
        except urllib.error.HTTPError as e:
            self._send(e.code, e.read(), {"Content-Type": "application/json"})
        except Exception as e:  # noqa
            err = json.dumps({"type": "error", "error": {"type": "ProxyError", "message": str(e)}}).encode()
            self._send(502, err, {"Content-Type": "application/json"})

    def log_message(self, *a):
        pass  # quiet


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    srv = http.server.HTTPServer(("127.0.0.1", port), Handler)
    print(f"Gauntlet proxy on http://localhost:{port}")
    print(f"  forwards /zen/* -> https://opencode.ai/zen/*")
    print(f"  In the app gear set Base URL: http://localhost:{port}/zen/v1")
    print("Ctrl+C to stop.")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped.")
