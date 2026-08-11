#!/bin/sh
set -eu
DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
python3 -m venv "$DIR/.venv"
"$DIR/.venv/bin/python" -m pip install --upgrade pip
"$DIR/.venv/bin/python" -m pip install mcp
printf '%s\n' "Up Finance MCP runtime installed in $DIR/.venv"
