import argparse

from config_loader import allowed_markets, load_config


def money(value: str) -> str:
    return f"${float(value):.2f}"


def show_workflow(config: dict) -> None:
    print("xyzCruzl Trade Agent")
    print()
    print("Mode workflow:")
    print("1. Scanner: find LONG / SHORT / WAIT candidates")
    print("2. Signal: validate setup quality")
    print("3. Risk manager: check size, SL, TP, and daily limits")
    print("4. Paper trading: simulate before real execution")
    print("5. Manual approval execution: only after you approve")
    print()
    print("Current safety config:")
    print(f"- Capital: {money(config['starting_capital_usd'])}")
    print(f"- Leverage: {config['leverage']}x")
    print(f"- Margin per trade: {money(config['margin_per_trade_usd'])}")
    print(f"- Max SL: {config['max_stop_loss_pct']}%")
    print(f"- Min TP: {config['min_take_profit_pct']}%")
    print(f"- Min RR: 1:{config['min_risk_reward']}")
    print(f"- Max daily loss: {money(config['max_daily_loss_usd'])}")


def run_scanner(config: dict) -> None:
    print("Scanner mode: dry run")
    print("No Hyperliquid order will be sent.")
    print()
    print("Allowed markets:")
    for market in allowed_markets(config):
        print(f"- {market}: WAIT")
    print()
    print("Reason:")
    print("Live market API is not connected yet. This mode is ready for scanner logic wiring.")


def run_gas_trade_hyper(config: dict) -> None:
    print("GAS TRADE HYPER: safety gate")
    print()
    print("Status: DRY RUN ONLY")
    print("No Hyperliquid order will be sent yet.")
    print()
    print("When live mode is added, this command must follow:")
    print("1. Scan allowed markets")
    print("2. Pick only the best setup with score >= min signal score")
    print("3. Validate max SL, min TP, RR, spread, fee, and cooldown")
    print("4. Open only 1 position max")
    print("5. Attach stop loss and take profit immediately")
    print("6. Stop after max daily loss or consecutive losses")
    print()
    print("Current trigger rules:")
    print(f"- Markets: {', '.join(allowed_markets(config))}")
    print(f"- Leverage: {config['leverage']}x")
    print(f"- Margin per trade: {money(config['margin_per_trade_usd'])}")
    print(f"- Max SL: {config['max_stop_loss_pct']}%")
    print(f"- Min TP: {config['min_take_profit_pct']}%")
    print(f"- Min score: {config['min_signal_score']}")
    print(f"- Max open positions: {config['max_open_positions']}")


def run_risk_check(config: dict, entry: float, side: str) -> None:
    sl_pct = float(config["max_stop_loss_pct"])
    tp_pct = float(config["min_take_profit_pct"])
    margin = float(config["margin_per_trade_usd"])
    leverage = float(config["leverage"])
    position_value = margin * leverage

    if side == "long":
        stop_loss = entry * (1 - sl_pct / 100)
        take_profit = entry * (1 + tp_pct / 100)
    else:
        stop_loss = entry * (1 + sl_pct / 100)
        take_profit = entry * (1 - tp_pct / 100)

    expected_loss = position_value * (sl_pct / 100)
    expected_profit = position_value * (tp_pct / 100)

    print("Risk check")
    print(f"- Side: {side.upper()}")
    print(f"- Entry: {entry:.4f}")
    print(f"- Stop loss: {stop_loss:.4f} ({sl_pct}%)")
    print(f"- Take profit: {take_profit:.4f} ({tp_pct}%)")
    print(f"- Margin: ${margin:.2f}")
    print(f"- Position value: ${position_value:.2f}")
    print(f"- Expected loss before fee/slippage: ${expected_loss:.4f}")
    print(f"- Expected profit before fee/slippage: ${expected_profit:.4f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="xyzCruzl Trade Agent CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("workflow", help="Show the agent workflow")
    subparsers.add_parser("scanner", help="Run dry scanner mode")
    subparsers.add_parser("gas-trade-hyper", help="Run the guarded Hyperliquid trading trigger")

    risk_parser = subparsers.add_parser("risk", help="Calculate SL/TP for a sample setup")
    risk_parser.add_argument("--side", choices=["long", "short"], required=True)
    risk_parser.add_argument("--entry", type=float, required=True)

    args = parser.parse_args()
    config = load_config()

    if args.command == "workflow":
        show_workflow(config)
    elif args.command == "scanner":
        run_scanner(config)
    elif args.command == "gas-trade-hyper":
        run_gas_trade_hyper(config)
    elif args.command == "risk":
        run_risk_check(config, args.entry, args.side)


if __name__ == "__main__":
    main()
