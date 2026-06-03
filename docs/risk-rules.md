# Risk Rules

## Capital

Starting balance: $10

This is a very small balance, so fees and slippage matter. The agent should trade less, not more.

## Main Rules

```text
Leverage: 10x
Margin per trade: $2
Position value: about $20
Max SL: 0.5% price move
Min TP: 1.2% price move
Max daily loss: $0.50
Max trades per day: 3
Max consecutive losses: 2
```

## Stop Loss

The stop loss must be at or below 0.5% from entry.

If the setup needs a wider stop loss, the agent must skip the trade.

## Take Profit

Minimum target is 1.2% from entry. This leaves more room for fee and slippage than a 1.0% target.

Preferred exit:

```text
TP1: +0.8% partial close
TP2: +1.2% main target
Runner: trailing stop only if momentum is strong
```

## Stop Trading Conditions

The agent must stop scanning for execution if:

```text
Daily loss reaches $0.50
2 losses happen in a row
3 trades already happened today
Market is choppy
Spread is high
Funding is unfavorable
```
