import yfinance as yf
import streamlit as st
import pandas as pd

PAIRS = {
    "EUR/USD": "EURUSD=X",
    "GBP/USD": "GBPUSD=X",
    "USD/JPY": "JPY=X",
    "AUD/USD": "AUDUSD=X",
    "USD/CAD": "CAD=X",
    "USD/CHF": "CHF=X",
    "NZD/USD": "NZDUSD=X"
}

def get_prices():
    results = []

    for name, symbol in PAIRS.items():
        try:
            data = yf.download(
                symbol,
                period="5d",
                interval="5m",
                progress=False,
                auto_adjust=False,
                multi_level_index=False
            )

            if data.empty:
                continue

            latest = data["Close"].dropna().iloc[-1]

            results.append({
                "Currency Pair": name,
                "Latest Available Price": round(float(latest), 5)
            })

        except Exception:
            continue

    return pd.DataFrame(results)


st.title("Forex Currency Monitor")

st.write("Educational Market Data Viewer")

if st.button("Refresh Market Data"):
    with st.spinner("Fetching market data..."):
        prices = get_prices()

        if not prices.empty:
            st.dataframe(prices, use_container_width=True)
        else:
            st.warning("Market data unavailable. Try again later.")

st.caption(
    "Data may be delayed or incomplete. "
    "Not a trading signal or financial advice."
)
