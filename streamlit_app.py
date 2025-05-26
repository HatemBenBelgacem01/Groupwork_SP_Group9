import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Load data from SQLite
conn = sqlite3.connect("climate_data.db")
df = pd.read_sql_query("SELECT * FROM avg_temperatures", conn)

# UI
st.title("Swiss Climate Trends (2014–2023)")

city = st.selectbox("Choose a city", df["City"].unique())
df_city = df[df["City"] == city]

st.line_chart(df_city.set_index("Year")["AvgMaxTemp"])

# Optional stats
st.write("Average temperature over 10 years:")
st.metric(label="Average Max Temp (°C)", value=f"{df_city['AvgMaxTemp'].mean():.2f}")