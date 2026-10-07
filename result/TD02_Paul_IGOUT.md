# TD02 - Python + CSV / JSON

## Repository

**Working directory:**

```text
/workspaces/esilv-marketpulse-G01-PME
```

**Current branch:**

```text
Paul_IGOUT
```

**Repository structure:**

```text
CONTRIBUTING.md
README.md
TEAM_TEMPLATE.md
config/
data/
evidence/
labs/
readiness/
requirements.txt
result/
src/
```

## Data

The data directory is located at:

```text
/workspaces/esilv-marketpulse-G01-PME/data
```

It contains:

```text
sample/
```

### Sample data

The sample directory is located at:

```text
/workspaces/esilv-marketpulse-G01-PME/data/sample
```

Files currently available:

```text
bloomberg_reference_expected.json
bloomberg_reference_sample.json
instruments.json
prices.csv
```

### Instrument

The instrument and benchmark information is stored in `data/sample/instruments.json`.

Command used to display it:

```bash
cat data/sample/instruments.json
```

Content:

```json
{
  "instrument": {
    "ticker": "AAPL",
    "name": "Apple Inc.",
    "currency": "USD",
    "market": "NASDAQ"
  },
  "benchmark": {
    "ticker": "SP500",
    "name": "S&P 500",
    "currency": "USD",
    "market": "US"
  }
}
```

- `instrument`: AAPL - Apple Inc. (USD, NASDAQ)
- `benchmark`: SP500 - S&P 500 (USD, US)

<img width="601" height="230" alt="Capture d&#39;écran 2026-10-07 162636" src="https://github.com/user-attachments/assets/c6005d8f-9ff8-40dd-942d-3edbd8ad3e50" />



### Price data

The price data is stored in `data/sample/prices.csv`.

The CSV contains the following columns:

- `date`
- `ticker`
- `open`
- `high`
- `low`
- `close`
- `volume`

Command used to preview the file:

```bash
head data/sample/prices.csv
```

```text
date,ticker,open,high,low,close,volume
2026-09-01,AAPL,249.20,251.50,248.00,250.00,38000000
2026-09-01,SP500,6592.00,6615.00,6580.00,6600.00,0
2026-09-02,AAPL,250.80,252.80,249.60,251.30,39500000
2026-09-02,SP500,6607.00,6627.00,6595.00,6612.00,0
2026-09-03,AAPL,249.60,251.30,248.40,249.80,41000000
2026-09-03,SP500,6596.00,6613.00,6584.00,6598.00,0
2026-09-04,AAPL,251.30,253.60,250.10,252.10,42500000
2026-09-04,SP500,6612.00,6635.00,6600.00,6620.00,0
2026-09-08,AAPL,251.90,253.90,250.70,252.40,44000000
```

<img width="638" height="153" alt="image" src="https://github.com/user-attachments/assets/92e93237-bc5a-4959-bf34-b2ded5ce632f" />


It contains daily observations for:

- AAPL - Apple Inc.
- SP500 - S&P 500

There are 21 observations for AAPL and 21 observations for SP500.

## Python program

The main Python file is `src/main.py`.

The program includes functions to:

- load the JSON data;
- load the CSV data;
- filter prices by ticker;
- get the first closing price;
- get the last closing price;
- display a market summary.

The CSV closing prices are converted to numeric values using `float()`.

## Environment

| Tool | Version |
|------|---------|
| Python | 3.14.2 |
| Git | 2.55.0 |

## MarketPulse execution

The application is launched with:

```bash
python src/main.py
```

The program successfully returns:

```text
=== MarketPulse ===

Market configuration
Period : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First close : 250.0 USD
Last close : 266.2 USD

Benchmark
SP500 - S&P 500
Observations : 21
First close : 6600.0
Last close : 6742.0
```

<img width="644" height="252" alt="Capture d&#39;écran 2026-10-07 160627" src="https://github.com/user-attachments/assets/252b9ba9-a270-4420-9c25-699d08e80965" />


## Project files used

- `src/main.py`
- `data/sample/instruments.json`
- `data/sample/prices.csv`

## Result

The TD02 program successfully loads the JSON and CSV files, separates the AAPL and SP500 data, converts the closing prices to numeric values and displays the expected market summary.

## Summary

| Item | Value |
|------|-------|
| Instrument | AAPL - Apple Inc. |
| Benchmark | SP500 - S&P 500 |
| Period | 1 month |
| Interval | Daily |
| Observations | 21 AAPL / 21 SP500 |
| First AAPL close | 250.0 USD |
| Last AAPL close | 266.2 USD |
| First SP500 close | 6600.0 |
| Last SP500 close | 6742.0 |
