import yfinance as yf
import pandas as pd
import numpy as np
import pandas_datareader as data
import matplotlib.pyplot as plt
from keras.models import load_model
import streamlit as st

start = "2010-01-01"
end = "2019-12-31"

st.title('Stock Trend Prediction')

user_input = st.text_input("Enter Stock Symbol", 'AAPL')
# Fetch historical stock data using yfinance
df = yf.download(user_input, start=start, end=end)


# Describing Data
st.subheader('Data from 2010 - 2019')
st.write(df.describe())