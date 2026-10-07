from pathlib import Path
import csv
import json


DATA_DIR = Path("data/sample")

LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    result = []

    for row in prices:
        if row["ticker"] == ticker:
            result.append(row)

    return result


def get_first_close(prices):
    first_price = prices[0]
    close = first_price["close"]

    return float(close)


def get_last_close(prices):
    last_price = prices[-1]
    close = last_price["close"]

    return float(close)


def display_market_summary(asset, prices, show_currency=True):
    ticker = asset["ticker"]
    name = asset["name"]

    first_close = get_first_close(prices)
    last_close = get_last_close(prices)

    print(ticker + " - " + name)
    print("Observations :", len(prices))

    if show_currency:
        currency = asset["currency"]

        print("First close :", first_close, currency)
        print("Last close :", last_close, currency)

    else:
        print("First close :", first_close)
        print("Last close :", last_close)


def main():
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(
        prices,
        instrument["ticker"]
    )

    benchmark_prices = filter_prices(
        prices,
        benchmark["ticker"]
    )

    print("=== MarketPulse ===")
    print()

    print("Market configuration")
    print("Period :", LOOKBACK_LABEL)
    print("Interval :", INTERVAL_LABEL)
    print()

    print("Instrument")
    display_market_summary(
        instrument,
        instrument_prices,
        True
    )
    print()

    print("Benchmark")
    display_market_summary(
        benchmark,
        benchmark_prices,
        False
    )


if __name__ == "__main__":
    main()
