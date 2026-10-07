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

The instrument information is stored in `data/sample/instruments.json`:

```json
{
  "ticker": "AAPL",
  "name": "Apple Inc.",
  "currency": "USD",
  "market": "NASDAQ"
}
```

### Benchmark

```json
{
  "ticker": "SP500",
  "name": "S&P 500",
  "currency": "USD",
  "market": "US"
}
```

The instrument and benchmark information is stored in `data/sample/instruments.json`.

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
