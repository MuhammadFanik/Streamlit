import streamlit as st
import yfinance as yf
from datetime import date, timedelta

st.title("Stock Price Viewer")

st.sidebar.header("Settings")
ticker = st.sidebar.text_input("Enter stock ticker symbol (e.g. AAPL, GOOGL, TSLA):")
start_date = st.sidebar.date_input("Start date", value=date.today() - timedelta(days=365))
end_date = st.sidebar.date_input("End date", value=date.today())

if ticker:
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)

    current_price = data["Close"].iloc[-1]
    previous_price = data["Close"].iloc[-2]
    price_change = current_price - previous_price
    percent_change = (price_change / previous_price) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Current Price", f"${current_price:.2f}")
    col2.metric("Daily Change", f"${price_change:.2f}", f"{percent_change:.2f}%")
    col3.metric("Previous Close", f"${previous_price:.2f}")

    st.subheader("Closing Price")
    st.line_chart(data["Close"])

    st.subheader("Trading Volume")
    st.bar_chart(data["Volume"])

    st.subheader("Raw Data")
    st.dataframe(data)