import streamlit as st
from agents import app

st.set_page_config(page_title="📈 Stock Market Assistant", layout="centered")

st.title("📈 AI-Powered Stock Market Assistant")
st.markdown("Analyze stocks, get insights, and simulated Buy/Sell/Hold recommendations.")

symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, MSFT):")

if st.button("Analyze"):
    if symbol:
        with st.spinner("Fetching and analyzing data..."):
            result = app.invoke({"symbol": symbol})
        
        st.subheader("Recommendation")
        st.write(f"**Action:** {result['recommendation']}")
        st.write(f"**Justification:** {result['justification']}")

        st.subheader("Indicators")
        st.json(result["analysis"])
    else:
        st.warning("Please enter a stock symbol.")