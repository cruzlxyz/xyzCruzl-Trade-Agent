# xyzCruzl Trade Agent

Agent trading pribadi untuk Hyperliquid dengan fokus awal pada modal kecil `$10`, leverage `10x`, stop loss maksimal `0.5%`, dan take profit minimal `1.2%`.

Project ini masih tahap **dry-run workflow**, belum live trading. Tujuan awalnya adalah membangun scanner dan risk manager yang rapi sebelum masuk ke auto execution.

## Manfaat Utama

- Scan potensi market `BTC`, `ETH`, `SOL`, dan `HYPE`
- Menentukan bias `LONG`, `SHORT`, atau `WAIT`
- Menghitung SL/TP sesuai rule risiko
- Mengurangi overtrade, fee damage, dan entry asal
- Menjadi fondasi untuk paper trading dan auto execution Hyperliquid

Untuk detail cara kerja lengkap, buka:

- `docs/workflow.md`
- `docs/scanner-logic.md`
- `docs/risk-rules.md`
- `docs/gas-trade-hyper.md`

## Rule Awal

```text
Capital: $10
Leverage: 10x
Margin per trade: $2
Max SL: 0.5%
Min TP: 1.2%
Min RR: 1:2
Max open position: 1
Max trades per day: 3
Max daily loss: $0.50
```

Detail risk management ada di:

```text
docs/risk-rules.md
config/trading_rules.yaml
```

## Cara Menjalankan

Install Python `3.10+`, lalu clone/download repo ini.

Masuk ke folder hasil clone/download:

```powershell
cd "xyzCruzl Trade Agent"
```

Lihat workflow:

```powershell
.\run.bat workflow
```

Jalankan scanner dry-run:

```powershell
.\run.bat scanner
```

Jalankan trigger `gas trade hyper` dry-run:

```powershell
.\run.bat gas-trade-hyper
```

Hitung risk contoh long/short:

```powershell
.\run.bat risk --side long --entry 70000
.\run.bat risk --side short --entry 70000
```

Alternatif tanpa `run.bat`:

```powershell
python src/main.py workflow
python src/main.py scanner
python src/main.py gas-trade-hyper
python src/main.py risk --side long --entry 70000
```

Untuk Linux/macOS:

```bash
python3 src/main.py workflow
python3 src/main.py scanner
python3 src/main.py gas-trade-hyper
python3 src/main.py risk --side long --entry 70000
```

## Struktur Folder

```text
config/   Rule trading utama
docs/     Penjelasan workflow, scanner, risk, dan trigger
prompts/  Prompt untuk mode analyst, scanner, risk manager
src/      Kode CLI awal
```

Detail struktur ada di masing-masing folder/file.

## Status

Sudah bisa:

```text
workflow dry-run
scanner dummy
risk calculator
gas-trade-hyper safety gate
```

Belum dibuat:

```text
live Hyperliquid API
live candle scanner
real order execution
auto long/short
journal trading
```

## Keamanan

Jangan upload private key asli ke GitHub.

File `.env` saat ini masih placeholder. Kalau sudah diisi private key asli, jangan commit file tersebut.

Detail konfigurasi ada di:

```text
.env.example
config/trading_rules.yaml
```

## Roadmap Singkat

```text
1. Live market data Hyperliquid
2. Scanner score asli
3. Paper trading journal
4. Manual approval execution
5. Auto execution
```

Detail roadmap teknis bisa dilanjutkan dari `docs/workflow.md`.
