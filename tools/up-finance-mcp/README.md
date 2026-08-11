# Up Finance MCP connector

This local connector adds a read-only `financial_budget_preview` tool to Hermes.

## Configure the token

From a terminal, run:

```bash
uv run --with mcp python /home/ubuntu/up-finance-mcp/setup_up_finance.py
```

The prompt hides the token and stores it in:

```text
/srv/hermes-stack/state/hermes-home/.env
```

with owner-only permissions.

## Add to Hermes

Add this under `mcp_servers` in the active Hermes config:

```yaml
mcp_servers:
  up_finance:
    command: "uv"
    args: ["run", "--with", "mcp", "/home/ubuntu/up-finance-mcp/up_finance_mcp.py"]
    env:
      UP_API_KEY: "${UP_API_KEY}"
    timeout: 120
    connect_timeout: 30
```

Restart Hermes after adding the server:

```bash
hermes gateway restart
hermes tools list
```

Then ask:

```text
Use financial_budget_preview with the current pay-cycle Up transaction records.
```

The tool accepts optional `pay_cycle_start` and `pay_cycle_end` dates in `YYYY-MM-DD` format. It performs read-only transaction retrieval and returns income, spending, net, transaction count, and spending by category.
