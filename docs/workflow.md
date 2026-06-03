# Trading Agent Workflow

## Phase 1: Scanner

Goal: find potential long/short setups without opening trades.

```text
Hyperliquid market data
-> Liquidity filter
-> Trend check
-> Momentum check
-> Support/resistance check
-> Fee/slippage filter
-> SL/TP validation
-> Output LONG / SHORT / WAIT
```

Output example:

```text
MARKET: BTC
BIAS: LONG
SCORE: 84
ENTRY_ZONE: 70000 - 70050
SL: 69650 (-0.5%)
TP1: 70560 (+0.8%)
TP2: 70840 (+1.2%)
ACTION: WATCH
REASON:
- 15m trend bullish
- price reclaim level
- volume confirmation
- TP remains realistic after fee/slippage
```

## Phase 2: Signal + Risk Manager

The agent may produce a setup, but still cannot trade.

```text
Signal found
-> Check SL max 0.5%
-> Check TP min 1.2%
-> Check RR min 1:2
-> Check daily loss limit
-> Check no recent loss cooldown
-> Return APPROVE / SKIP recommendation
```

## Phase 3: Paper Trading

The agent simulates entry, stop loss, take profit, fee, slippage, and PnL.

Only continue if paper results are stable.

## Phase 4: Manual Approval Execution

The agent prepares an order and waits for user approval.

```text
APPROVE -> send order
CANCEL -> ignore
EDIT -> change setup
```

## Phase 5: Auto Execution

Auto execution should only be enabled after paper trading and small-size real testing.

Default setting:

```text
auto_execution_enabled: false
require_manual_approval: true
```
