# Team

## Repository

**Working directory:**

```text
/workspaces/esilv-marketpulse-G01-PME
```

**Current branch:**

```text
Paul_IGOUT
```

## Repository structure

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

## Sample data

### Instrument

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

The instrument and benchmark information is stored in:

```text
data/sample/instruments.json
```

## Price data

The price data is stored in:

```text
data/sample/prices.csv
```

The CSV contains the following columns:

```text
date
ticker
open
high
low
close
volume
```

It contains daily observations for:

* **AAPL** — Apple Inc.
* **SP500** — S&P 500

There are **21 observations for AAPL** and **21 observations for SP500**.

## Environment

### Python

```text
Python 3.14.2
```

### Git

```text
git version 2.55.0
```

## MarketPulse execution

The application is launched with:

```bash
python src/main.py
```

The program successfully returns:

```text
=== MarketPulse ===

Instrument
AAPL - Apple Inc.
Last price: 266.20 USD

Benchmark
SP500 - S&P 500
Last level: 6742.00

Period: 1 month
Interval: Daily

Observations
AAPL: 21
SP500: 21
```

## Project files used

```text
src/main.py
data/sample/instruments.json
data/sample/prices.csv
```

### Summary

```text
Instrument : AAPL - Apple Inc.
Benchmark  : SP500 - S&P 500
Period     : 1 month
Interval   : Daily
Provider   : CSV
```
