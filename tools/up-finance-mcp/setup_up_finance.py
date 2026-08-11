#!/usr/bin/env python3
"""Securely configure the Up API token for Hermes."""
from __future__ import annotations

import getpass
import os
import stat
from pathlib import Path

ENV_PATH = Path(os.environ.get("HERMES_HOME", str(Path.home() / ".hermes"))) / ".env"


def main() -> int:
    print("Up Finance connector setup")
    print("Your token will not be displayed or echoed.")
    token = getpass.getpass("Enter your Up API key: ").strip()
    if not token:
        print("No token entered; nothing changed.")
        return 1

    ENV_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = ENV_PATH.read_text(encoding="utf-8") if ENV_PATH.exists() else ""
    lines = [line for line in existing.splitlines() if not line.startswith("UP_API_KEY=")]
    lines.append(f"UP_API_KEY={token}")
    ENV_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    os.chmod(ENV_PATH, stat.S_IRUSR | stat.S_IWUSR)
    print(f"Saved Up API key to {ENV_PATH} with owner-only permissions.")
    print("Next: restart Hermes, then ask for a financial budget preview.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
