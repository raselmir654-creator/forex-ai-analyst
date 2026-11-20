import streamlit as st
from market_data import get_market_data
from forex_analyzer import analyze_market

st.set_page_config(
    page_title="Forex AI Analyst",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Forex AI Analyst")
st.write("Your Personal Forex Analysis Dashboard")

pair = st.selectbox(
    "Select Currency Pair",
    ["EURUSD=X", "GBPUSD=X", "JPY=X", "AUDUSD=X"]
)

if st.button("Analyze Market"):
    with st.spinner("Analyzing market..."):
        try:
            data = get_market_data(pair)
            result = analyze_market(pair)

            if data is not None:
                st.subheader("Market Data")
                st.dataframe(data)

            st.subheader("Market Analysis")
            st.write(result)

        except Exception as error:
            st.error(f"Analysis failed: {error}")
