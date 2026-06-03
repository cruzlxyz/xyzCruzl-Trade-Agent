# Source Skeleton

This folder is reserved for implementation.

Planned modules:

```text
config_loader.py      Read .env and YAML rules
hyperliquid_client.py Market data and order API wrapper
scanner.py            Long/short candidate scanner
risk_manager.py       SL, TP, position sizing, and limits
journal.py            Trade log and stats
main.py               CLI entry point
```

Current status: workflow-first scaffold with a dry-run CLI.

Run from project root:

```text
python src/main.py workflow
python src/main.py scanner
python src/main.py risk --side long --entry 70000
python src/main.py risk --side short --entry 70000
```

The scanner is dry-run only. It does not connect to Hyperliquid and cannot place orders yet.
