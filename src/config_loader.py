from pathlib import Path


DEFAULT_CONFIG = {
    "starting_capital_usd": "10",
    "leverage": "10",
    "margin_per_trade_usd": "2",
    "max_stop_loss_pct": "0.5",
    "min_take_profit_pct": "1.2",
    "min_risk_reward": "2",
    "max_daily_loss_usd": "0.5",
    "max_trades_per_day": "3",
    "max_consecutive_losses": "2",
    "max_open_positions": "1",
    "min_signal_score": "80",
    "allowed_markets": "BTC,ETH,SOL,HYPE",
}


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_dotenv(path: Path) -> dict:
    values = {}
    if not path.exists():
        return values

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip().lower()] = value.strip()
    return values


def load_config() -> dict:
    env_values = load_dotenv(project_root() / ".env")
    config = DEFAULT_CONFIG.copy()
    config.update(env_values)
    return config


def allowed_markets(config: dict) -> list[str]:
    raw = config.get("allowed_markets", DEFAULT_CONFIG["allowed_markets"])
    return [market.strip().upper() for market in raw.split(",") if market.strip()]
