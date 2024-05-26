import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

st.title("Indian Stock Market Tracker")

# Create a list to store the stock names
stock_names = []

# Create a text input for the user to enter the stock names
for i in range(5):
    stock_name = st.text_input(f"Enter stock name {i+1}:")
    if stock_name:
        stock_names.append(stock_name)

# Create a dropdown menu for the user to select the duration
duration = st.slider("Select duration (years):", 1, 50)

# Create a button to trigger the data retrieval
if st.button("Get Stock Prices"):
    # Retrieve the stock prices for the selected duration
    stock_data = {}
    for stock_name in stock_names:
        ticker = yf.Ticker(f"{stock_name}.NS")
        hist = ticker.history(period=f"{duration}y")
        stock_data[stock_name] = hist

    # Create a figure for the plot
    fig = go.Figure(data=[go.Scatter(x=stock_data[stock_name].index, y=stock_data[stock_name]['Close'], name=stock_name) for stock_name in stock_names])

    # Add a title and labels to the plot
    fig.update_layout(title=f"Stock Prices for the last {duration} years", xaxis_title="Date", yaxis_title="Price", legend_title="Stock Names")

    # Display the plot
    st.plotly_chart(fig)

    # Create a table to display the stock prices
    st.write("Stock Prices:")
    for stock_name in stock_names:
        st.write(f"{stock_name}:")
        st.write(stock_data[stock_name].head())
        st.write()