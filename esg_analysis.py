import pandas as pd
import numpy as np
import os

try:
    df = pd.read_csv('esg_carbon_data.csv')
except FileNotFoundError:
    # Dummy fallback data
    df = pd.DataFrame({
        'Facility_ID': [f'Facility_{i}' for i in range(10)],
        'Scope_1_Emissions_Tons': np.random.uniform(150, 800, 10),
        'Scope_2_Emissions_Tons': np.random.uniform(200, 1200, 10),
        'Operational_Cost_USD': np.random.uniform(500000, 4000000, 10),
        'Carbon_Credits_Held': np.random.uniform(50, 500, 10)
    })

# Analytics Calculations
df['Total_Emissions'] = df['Scope_1_Emissions_Tons'] + df['Scope_2_Emissions_Tons']
df['Emission_Intensity'] = (df['Total_Emissions'] / df['Operational_Cost_USD']) * 1000000
df['Credit_Deficit'] = (df['Total_Emissions'] * 0.8) - df['Carbon_Credits_Held']

# Anomaly Detection
high_emission_threshold = df['Emission_Intensity'].quantile(0.75)
df['ESG_Risk_Flag'] = df['Emission_Intensity'] > high_emission_threshold

# Save file to a 'data' folder
os.makedirs('data', exist_ok=True)
df.to_csv('data/esg_processed_data.csv', index=False)
print("Analysis complete! File saved to data/esg_processed_data.csv")