🌡️ Climate Data Explorer: A Scientific Programming Project

This project was developed as part of a Scientific Programming course and investigates climate trends using temperature data from the OpenWeather API. The goal is to demonstrate scientific coding practices, modular structure, and interactive visualization via a Streamlit dashboard.

📚 Project Overview
We fetch and analyze real-time temperature data from various cities using the OpenWeather API. The project is structured in clearly separated parts and culminates in a Streamlit-based web application that visualizes temperature trends.

🧩 Project Structure
climate-data-project/
│
├── part01_fetch_data.py        # Fetches temperature data via OpenWeather API
├── part02_store_data.py        # Saves and structures the data
├── part03_process_data.py      # Processes and cleans the data
├── part04_analysis.py          # Performs analysis
├── part05_visualization.py     # Visualization logic used by the Streamlit app
│
├── streamlit_app.py            # Interactive dashboard for data exploration
│
├── .env                        # Contains your OpenWeather API key (not committed)
├── requirements.txt            # Required Python packages
└── README.md                   # Project documentation (this file)

🔍 Features
🌍 Fetch live temperature data from selected cities
🧹 Clean and structure raw API responses
📊 Analyze temperature trends and variations
📈 Visualize results in an interactive Streamlit dashboard
🔐 API key stored safely using .env

🚀 How to Run
Install dependencies:
pip install -r requirements.txt
Set your API-Key:
API_KEY=your_api_key_here
Launch the Streamlit app:
streamlit run streamlit_app.py

🛠 Technologies Used
Python 3.9+
OpenWeather API – live weather and temperature data
Streamlit – for building the interactive web app
Requests – for API calls
Python-dotenv – for securely managing API keys
Pandas – for data handling and transformation
NumPy – for numerical processing
Matplotlib – for basic plotting
Plotly – for interactive visualizations (in Streamlit)
JSON & OS libraries – for data storage and file management

📌 Notes
The project is modularized to reflect best practices in scientific computing.
The temperature data is stored locally to allow offline analysis and reproducibility.
Cities and parameters can easily be customized in the source files.