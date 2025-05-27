import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import os

# Dynamically get absolute path to the database
base_dir = os.path.dirname(__file__)
db_path = os.path.join(base_dir, "..", "notebooks", "climate_data.db")

conn = sqlite3.connect(db_path)

df = pd.read_sql_query("SELECT * FROM avg_temperatures", conn)

# UI
st.title("Swiss Climate Trends (2014–2023)")

city = st.selectbox("Choose a city", df["City"].unique())
df_city = df[df["City"] == city]

st.line_chart(df_city.set_index("Year")["AvgMaxTemp"])

# Optional stats
st.write("Average temperature over 10 years:")
st.metric(label="Average Max Temp (°C)", value=f"{df_city['AvgMaxTemp'].mean():.2f}")