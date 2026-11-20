import yfinance as yf
import pandas as pd

def analyze_market(pair="EURUSD=X"):
    data = yf.download(
        pair,
        period="1mo",
        interval="1h",
        progress=False
    )

    if data.empty:
        return "Market data unavailable."

    close = data["Close"].dropna()

    if len(close) < 20:
        return "Not enough market data."

    sma = close.rolling(20).mean().iloc[-1]
    current = close.iloc[-1]

    if current > sma:
        trend = "Bullish"
    elif current < sma:
        trend = "Bearish"
    else:
        trend = "Neutral"

    return {
        "Pair": pair,
        "Price": round(float(current), 5),
        "Trend": trend
    }

if __name__ == "__main__":
    print(analyze_market())
