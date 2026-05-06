import pandas as pd
from sqlalchemy import create_engine
import os

# Processed data reading
try:
    df = pd.read_csv('data/esg_processed_data.csv')
except FileNotFoundError:
    print("Processed file not found. Pehle esg_analysis.py run karein.")
    exit()

# SQLite Database Connection String
DB_URL = 'sqlite:///esg_database.db'

try:
    engine = create_engine(DB_URL)
    df.to_sql('esg_carbon_metrics', con=engine, if_exists='replace', index=False)
    print(f"Data successfully loaded into the database using: {DB_URL}")
except Exception as e:
    print("Database connection failed:", e)