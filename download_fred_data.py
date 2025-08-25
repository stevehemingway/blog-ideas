import pandas as pd
from fredapi import Fred

# FRED API Key
api_key = "e13c8cee393d1c8cb726df61858ff73a"

# Series IDs
series_ids = ["WFRBLTP1228", "WFRBLB50086"]

# Create a FRED object
fred = Fred(api_key)

# Download data
data = {}
for series_id in series_ids:
    data[series_id] = fred.get_series(series_id)

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the ratio
df["ratio"] = df["WFRBLTP1228"] / df["WFRBLB50086"]

# Normalize the data to 1989 values
df_normalized = df / df.loc[df.index.year == 1989] * 100

# Create a table
table = df_normalized.loc[df_normalized.index.year == df_normalized.index.year.max()]
table = pd.DataFrame({
    "Top 0.1% Checking Deposits": [df_normalized["WFRBLTP1228"].iloc[-1]],
    "Bottom 50% Checking Deposits": [df_normalized["WFRBLB50086"].iloc[-1]],
    "Ratio": [df_normalized["ratio"].iloc[-1]]
})

# Print the table in Markdown format
print(table.to_markdown(index=False))
