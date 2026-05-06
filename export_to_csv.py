import sqlite3
import pandas as pd

# SQLite connection 
conn = sqlite3.connect('esg_database.db')

# Table's data is load into dataframe
df = pd.read_sql_query("SELECT * FROM esg_carbon_metrics", conn)

# saved as CSV file
df.to_csv('data/esg_dashboard_data.csv', index=False)

print("Data successfully exported to data/esg_dashboard_data.csv! Safe to import in Power BI.")
conn.close()