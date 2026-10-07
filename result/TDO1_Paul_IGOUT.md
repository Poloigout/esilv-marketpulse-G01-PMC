


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
<img width="716" height="509" alt="Capt1td1" src="https://github.com/user-attachments/assets/e98edb4f-4826-42ab-b0e7-87037129b13f" />
## Result

A `result/` directory has been created for the project outputs:

```text
result/
```
<img width="778" height="378" alt="Capture d&#39;écran 2026-10-07 155347" src="https://github.com/user-attachments/assets/f2ae9a92-3a60-493a-8a99-c1305d1fda1a" />
Sample data
Instrument
{
  "ticker": "AAPL",
  "name": "Apple Inc.",
  "currency": "USD",
  "market": "NASDAQ"
}
Benchmark
{
  "ticker": "SP500",
  "name": "S&P 500",
  "currency": "USD",
  "market": "US"
}

The instrument and benchmark information is stored in:

data/sample/instruments.json
Price data

The price data is stored in:

data/sample/prices.csv

The CSV contains the following columns:

date
ticker
open
high
low
close
volume

It contains daily observations for:

AAPL — Apple Inc.
SP500 — S&P 500

There are 21 observations for AAPL and 21 observations for SP500.

Environment
Python
Python 3.14.2
Git
git version 2.55.0
MarketPulse execution

The application is launched with:

python src/main.py

The program successfully returns:

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
Project files used
src/main.py
data/sample/instruments.json
data/sample/prices.csv
Summary
Instrument : AAPL - Apple Inc.
Benchmark  : SP500 - S&P 500
Period     : 1 month
Interval   : Daily
Provider   : CSV
<img width="599" height="409" alt="Capture d&#39;écran 2026-10-07 155704" src="https://github.com/user-attachments/assets/a9bc04d9-2771-4241-aad3-680955892dc4" />
