import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
         # Simple stock price application
         >Shown are the stock **closing price** and volume of Google.         
         """)

ticker_code = "GOOGL"

ticker_data = yf.Ticker(ticker=ticker_code)

ticker_df = ticker_data.history(
  period="1d",
  start="2019-01-01",
  end="2022-06-01"
)

st.write("""
         #### Close value
         """)
st.line_chart(ticker_df.Close)
st.write("""
         #### Volume value
         """)
st.line_chart(ticker_df.Volume)