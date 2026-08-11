#!/bin/sh
set -eu
DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ -x "$DIR/.venv/bin/python" ]; then
  exec "$DIR/.venv/bin/python" "$DIR/up_finance_mcp.py"
fi
if command -v uv >/dev/null 2>&1; then
  exec uv run --with mcp "$DIR/up_finance_mcp.py"
fi
printf '%s\n' "Missing MCP runtime. Run install_up_finance.sh first." >&2
exit 1
