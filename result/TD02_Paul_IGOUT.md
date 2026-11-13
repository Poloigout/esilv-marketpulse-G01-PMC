# TD02 - Python + CSV / JSON

## Business requirement

```text
"The trading desk still sends local CSV and JSON market files."
```

## Context

- **Working directory:** `/workspaces/esilv-marketpulse-G01-PME`
- **Current branch:** `Paul_IGOUT`
- **Starter configuration:**

```text
Instrument : AAPL - Apple Inc.
Benchmark  : S&P 500
Lookback   : 1 month
Interval   : Daily
Provider   : CSV
```

The trading desk provides instrument metadata in JSON and daily market prices in CSV. MarketPulse loads both files, distinguishes the primary instrument from its benchmark, filters the correct observations and displays a reusable summary. No return is calculated in TD02.

**Environment**

| Tool | Version |
|------|---------|
| Python | 3.14.2 |
| Git | 2.55.0 |

**Repository structure**

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

**Data directory** (`/workspaces/esilv-marketpulse-G01-PME/data`) contains `sample/`, which holds:

```text
bloomberg_reference_expected.json
bloomberg_reference_sample.json
instruments.json
prices.csv
```

---

# CORE

## Part 1 - Review the starter

The main file is `src/main.py`. It is launched with:

```bash
python src/main.py
```

Elements identified in the starter:

```text
import csv
import json
Path
DATA_DIR
load_instruments()
load_prices()
filter_prices()
main()
```

| Question | Answer |
|----------|--------|
| Which function reads JSON? | `load_instruments()` |
| Which function reads CSV? | `load_prices()` |
| Which function selects one ticker? | `filter_prices()` |
| Which function coordinates execution? | `main()` |
| Where are the input files stored? | `data/sample/` (via `DATA_DIR`) |

## Part 2 - JSON and dictionaries

Command used:

```bash
cat data/sample/instruments.json
```

Content of `data/sample/instruments.json`:

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

The file is read with `json.load()`:

```python
with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
    instruments = json.load(file)
```

What this gives:

```text
instruments  = dictionary containing two business objects
instrument   = dictionary describing the primary instrument (AAPL - Apple Inc., USD, NASDAQ)
benchmark    = dictionary describing the comparison benchmark (SP500 - S&P 500, USD, US)
```

Fields are accessed by key, for example `instrument["ticker"]`, `instrument["name"]`, `benchmark["ticker"]`.

<img width="601" height="230" alt="Capture d&#39;écran 2026-10-07 162636" src="https://github.com/user-attachments/assets/c6005d8f-9ff8-40dd-942d-3edbd8ad3e50" />

## Part 3 - CSV and lists of dictionaries

Command used:

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

The columns are `date`, `ticker`, `open`, `high`, `low`, `close`, `volume`.

The file is read with `csv.DictReader`:

```python
def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))
```

```text
prices     = list
prices[0]  = dictionary (one observation)
```

### CSV values are text

`csv.DictReader` returns every field as a string, including `close`. A numeric value must be converted explicitly before any numerical use:

```python
close = float(prices[0]["close"])
```

```text
CSV text -> explicit numeric conversion -> safe numerical use
```

## Part 4 - Filtering instrument and benchmark rows

Both series are stored in the same CSV. The helper `filter_prices()` selects one ticker:

```python
def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]
```

It is used for both business objects:

```python
instrument_prices = filter_prices(prices, instrument["ticker"])
benchmark_prices = filter_prices(prices, benchmark["ticker"])
```

Result:

| Series | Observations |
|--------|--------------|
| AAPL - Apple Inc. | 21 |
| SP500 - S&P 500 | 21 |

The list comprehension is equivalent to a loop with a condition and an append:

```text
loop + condition + append = filtering
```

## Part 5 - First and last close helpers

Two small functions return a close value converted to `float`:

- `get_first_close(prices)`: reads `close` of the first observation;
- `get_last_close(prices)`: reads `close` of the last observation.

| Series | First close | Last close |
|--------|-------------|------------|
| AAPL | 250.0 | 266.2 |
| SP500 | 6600.0 | 6742.0 |

## Part 6 - One reusable market summary

A single summary function is used for both the instrument and the benchmark, instead of one implementation per series:

```text
same operation + different data = reusable function
```

It displays the ticker, the name, the number of observations, the first close and the last close. The currency is shown for the instrument only.

## Part 7 - Readable `main()`

`main()` keeps a clear flow and delegates the work to small functions:

```text
load metadata
      |
      v
load prices
      |
      v
select instrument + benchmark
      |
      v
filter both series
      |
      v
display configuration
      |
      v
display both summaries
```

## Part 8 - Final output validation

Command:

```bash
python src/main.py
```

Output:

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

Values are displayed with one decimal (`250.0`) instead of two (`250.00`). This is a small formatting difference, which the TD accepts.

Required behaviour:

```text
[x] instrument identified
[x] benchmark identified
[x] both series filtered
[x] 21 observations for AAPL
[x] 21 observations for SP500
[x] first close displayed
[x] last close displayed
[x] numerical conversion performed
[x] reusable summary logic used
```

## Part 9 - Python concepts recap

| Concept | Example in MarketPulse |
|---------|------------------------|
| list | `prices[0]` |
| dictionary | `instrument["ticker"]` |
| function | `def get_last_close(prices):` |
| condition | `if row["ticker"] == ticker:` |
| loop | `for row in prices:` |
| type conversion | `float(row["close"])` |

## Part 10 - Handoff to TD03

- The Python changes work and run with `python src/main.py`.
- No Pull Request and no extra feature branch were created.
- The TD02 changes are left in the working tree, ready for TD03 (`git status`, `git diff`, `git add`, `git commit`, `git log`).

---

# CORE definition of done

```text
[x] still runs with python src/main.py
[x] loads instruments.json
[x] loads prices.csv
[x] separates AAPL and SP500 rows
[x] has 21 observations for each series
[x] displays the first close for each series
[x] displays the last close for each series
[x] converts close values to numeric form before numerical use
[x] uses reusable summary logic
[x] has meaningful Python changes ready for TD03 Git work
```

# Final readiness check

Concepts explained:

```text
[x] what a Python list is
[x] what a Python dictionary is
[x] what csv.DictReader returns
[x] why CSV numeric values need conversion
[x] how MarketPulse filters by ticker
[x] why one reusable summary function is useful
[x] where instrument metadata is stored
[x] where price observations are stored
```

Team confirmation:

```text
[x] MarketPulse runs
[x] AAPL has 21 observations
[x] SP500 has 21 observations
[x] first and last closes are displayed
[x] no external Python library was required
[x] no return calculation was added
```

# Result

The TD02 program loads the JSON and CSV files, separates the AAPL and SP500 data, converts the closing prices to numeric values and displays the expected market summary.

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
