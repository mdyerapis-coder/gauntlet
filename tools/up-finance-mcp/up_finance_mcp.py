#!/usr/bin/env python3
"""Hermes MCP connector for read-only Up transaction budgeting."""
from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.up.com.au/api/v1"
mcp = FastMCP("up-finance")


def _api_token() -> str:
    token = os.environ.get("UP_API_KEY", "").strip()
    if token:
        return token
    # Hermes deliberately filters most environment variables from MCP
    # subprocesses, so read the owner-only Hermes .env as a fallback.
    env_path = os.environ.get("HERMES_ENV_PATH", str(Path.home() / ".hermes" / ".env"))
    try:
        for line in open(env_path, encoding="utf-8"):
            line = line.strip()
            if line.startswith("UP_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    except OSError:
        pass
    return ""


def _get(path: str, params: dict[str, str] | None = None) -> dict[str, Any]:
    token = _api_token()
    if not token:
        raise RuntimeError("UP_API_KEY is not configured; run setup_up_finance.py")
    url = f"{BASE_URL}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def _api_boundary(value: str, end: bool = False) -> str:
    if "T" in value:
        return value
    return f"{value}T{'23:59:59' if end else '00:00:00'}Z"


def _transactions(start: str | None, end: str | None) -> list[dict[str, Any]]:
    params: dict[str, str] = {"page[size]": "100"}
    if start:
        params["filter[since]"] = _api_boundary(start)
    if end:
        params["filter[until]"] = _api_boundary(end, end=True)

    records: list[dict[str, Any]] = []
    path = "/transactions"
    while path:
        payload = _get(path, params)
        records.extend(payload.get("data", []))
        next_url = (payload.get("links") or {}).get("next")
        if not next_url:
            break
        parsed = urllib.parse.urlsplit(next_url)
        path = parsed.path.replace("/api/v1", "", 1) or "/transactions"
        params = dict(urllib.parse.parse_qsl(parsed.query))
    return records


def _category(transaction: dict[str, Any]) -> str:
    attrs = transaction.get("attributes") or {}
    category = attrs.get("category")
    if isinstance(category, dict):
        return category.get("name") or category.get("id") or "uncategorized"
    return str(category or "uncategorized")


@mcp.tool()
def financial_budget_preview(
    pay_cycle_start: str | None = None,
    pay_cycle_end: str | None = None,
) -> dict[str, Any]:
    """Create a read-only budget preview from Up transactions.

    Dates use YYYY-MM-DD. If omitted, the preview covers the current fortnight
    beginning on the most recent Monday and ending today.
    """
    today = date.today()
    if not pay_cycle_end:
        pay_cycle_end = today.isoformat()
    if not pay_cycle_start:
        pay_cycle_start = (today - timedelta(days=today.weekday() + 7)).isoformat()

    rows = _transactions(pay_cycle_start, pay_cycle_end)
    by_category: dict[str, float] = defaultdict(float)
    spending = 0.0
    income = 0.0
    transaction_count = 0

    for row in rows:
        attrs = row.get("attributes") or {}
        amount = attrs.get("amount") or {}
        value = float(amount.get("value", 0) or 0)
        if value >= 0:
            income += value
        else:
            spending += abs(value)
            by_category[_category(row)] += abs(value)
        transaction_count += 1

    return {
        "source": "Up API",
        "read_only": True,
        "pay_cycle": {"start": pay_cycle_start, "end": pay_cycle_end},
        "transaction_count": transaction_count,
        "income": round(income, 2),
        "spending": round(spending, 2),
        "net": round(income - spending, 2),
        "spending_by_category": dict(sorted(by_category.items(), key=lambda x: -x[1])),
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
