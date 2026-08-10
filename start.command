#!/bin/bash
# Gauntlet launcher (macOS / Linux)
# Starts the CORS proxy, then opens gauntlet.html in your default browser.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

cleanup() { [ -n "$PID" ] && kill "$PID" 2>/dev/null; }
trap cleanup EXIT INT TERM

echo "Starting Gauntlet proxy on http://localhost:8000 ..."
python3 gauntlet-proxy.py 8000 &
PID=$!

# give the proxy a moment to bind
sleep 1.5

# open the app in the default browser
if command -v xdg-open >/dev/null 2>&1; then
  xdg-open "$DIR/gauntlet.html" >/dev/null 2>&1 &
elif command -v open >/dev/null 2>&1; then
  open "$DIR/gauntlet.html"
else
  echo "Open this in your browser: file://$DIR/gauntlet.html"
fi

echo "Gauntlet is running. Close this window to stop the proxy."
wait "$PID"
