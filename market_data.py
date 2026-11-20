import yfinance as yf

def get_market_data(pair="EURUSD=X"):
    data = yf.download(
        pair,
        period="5d",
        interval="1h",
        progress=False
    )

    if data.empty:
        return None

    return data.tail(20)

if __name__ == "__main__":
    market = get_market_data()
    if market is not None:
        print(market)
    else:
        print("Market data unavailable")
