# Scanner Logic

The scanner finds the best long or short candidates. It does not force trades.

## Markets

Allowed markets:

```text
BTC
ETH
SOL
HYPE
```

## Score System

```text
Trend alignment: 25 points
Volume confirmation: 20 points
Support/resistance quality: 20 points
Momentum: 15 points
Risk/reward valid: 15 points
Fee/slippage condition: 5 points
```

Required score:

```text
80+ = valid watchlist setup
90+ = strong setup
Below 80 = skip
```

## Long Conditions

```text
5m and 15m trend bullish
price above important moving average or reclaimed key level
volume increasing
entry close to invalidation
SL <= 0.5%
TP >= 1.2%
RR >= 1:2
```

## Short Conditions

```text
5m and 15m trend bearish
price rejected key resistance or lost support
sell volume increasing
entry close to invalidation
SL <= 0.5%
TP >= 1.2%
RR >= 1:2
```

## Wait Conditions

```text
sideways chop
wide spread
large candle spike already happened
support/resistance too close to TP
SL needs more than 0.5%
news or high volatility event
```
