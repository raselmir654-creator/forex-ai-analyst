import yfinance as yf
import pandas as pd

def get_market_data(pair="EURUSD=X"):
    data = yf.download(
        pair,
        period="5d",
        interval="1h",
        progress=False,
        auto_adjust=False
    )

    if data is None or data.empty:
        return None

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    return data.tail(20)

if __name__ == "__main__":
    market = get_market_data()
    if market is not None:
        print(market)
    else:
        print("Market data unavailable")
