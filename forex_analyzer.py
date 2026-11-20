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

    close = data["Close"]

    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    close = pd.to_numeric(
        close, errors="coerce"
    ).dropna()

    if len(close) < 20:
        return "Not enough market data."

    current = float(close.iloc[-1])
    sma = float(close.rolling(20).mean().iloc[-1])

    if current > sma:
        trend = "Bullish"
    elif current < sma:
        trend = "Bearish"
    else:
        trend = "Neutral"

    return {
        "Pair": pair,
        "Price": round(current, 5),
        "Trend": trend
    }
