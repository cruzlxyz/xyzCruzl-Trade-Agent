# Gas Trade Hyper Trigger

Trigger phrase:

```text
gas trade hyper
```

CLI command:

```text
.\run.bat gas-trade-hyper
```

## Purpose

This command is the future one-shot auto trading trigger for Hyperliquid.

It must never mean "trade blindly". It means:

```text
Scan -> validate -> trade only if setup is clean -> attach SL/TP -> stop if limits are hit
```

## Required Safety Gates

Before any real order is allowed:

```text
Hyperliquid API connected
Agent wallet authorized
Auto execution enabled in config
Only 1 open position
Signal score >= 80
Max SL <= 0.5%
Min TP >= 1.2%
RR >= 1:2
Margin per trade <= $2
Daily loss < $0.50
Consecutive losses < 2
Spread/slippage acceptable
Cooldown is not active
```

## Execution Behavior

If a valid setup exists:

```text
1. Choose the highest score setup
2. Place limit entry if possible
3. Attach stop loss immediately
4. Attach take profit immediately
5. Monitor until TP, SL, or timeout
6. Journal the result
```

If no valid setup exists:

```text
Do nothing.
Return WAIT.
```

## Current Status

Dry-run only. It does not connect to Hyperliquid and does not place real orders yet.
