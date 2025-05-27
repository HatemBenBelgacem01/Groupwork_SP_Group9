import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

# Set correct database path
BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "..", "climate_data.db")

@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM avg_temperatures", conn)  # Or avg_temperatures_cleaned
    conn.close()
    return df

df = load_data()

# --- Page UI ---
st.title("🌍 European Climate Trends (2014–2023)")
st.subheader("Average Maximum Temperature by City")

# City selection
city = st.selectbox("Choose a city", df["City"].unique())
df_city = df[df["City"] == city]

# --- Trend Analysis ---
slope, intercept, r_value, p_value, _ = linregress(df_city["Year"], df_city["AvgMaxTemp"])
predicted = intercept + slope * df_city["Year"]

# --- Line Chart ---
fig, ax = plt.subplots()
ax.plot(df_city["Year"], df_city["AvgMaxTemp"], marker='o', label="Observed")
ax.plot(df_city["Year"], predicted, color='red', linestyle='--', label="Trend")
ax.set_title(f"{city} – Avg Max Temp Trend")
ax.set_xlabel("Year")
ax.set_ylabel("Temperature (°C)")
ax.legend()
st.pyplot(fig)

# --- Metrics ---
st.metric("Trend Slope (°C/year)", f"{slope:.3f}")
st.metric("p-value", f"{p_value:.4f}")
st.metric("R²", f"{r_value**2:.3f}")

# --- Optional: LLM Summary via Hugging Face ---
if "HF_API_KEY" in st.secrets:
    from transformers import pipeline
    from huggingface_hub import login

    login(st.secrets["HF_API_KEY"])
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    # Build summary input text based on data
    text = (
        f"From 2014 to 2023, {city}'s average max temperature rose from "
        f"{df_city['AvgMaxTemp'].iloc[0]:.1f}°C to {df_city['AvgMaxTemp'].iloc[-1]:.1f}°C. "
        f"The trend slope was {slope:.3f} with a p-value of {p_value:.4f}, "
        f"indicating {'statistical significance' if p_value < 0.05 else 'no significant trend'}."
    )

    # Show input text for transparency (optional)
    st.text_area("🔍 Summary Input Text", value=text, height=120)

    # Button to trigger the LLM
    if st.button("🧠 Generate Summary"):
        try:
            summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
            st.subheader("🧠 LLM Summary")
            st.write(summary[0]["summary_text"])
        except Exception as e:
            st.error(f"❌ LLM failed: {e}")
else:
    st.info("🔐 Hugging Face API key not found. Add it to `.streamlit/secrets.toml` to enable summaries.")