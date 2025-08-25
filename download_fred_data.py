import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt

# FRED API Key
api_key = "e13c8cee393d1c8cb726df61858ff73a"

# Series IDs
series_ids = ["WFRBLTP1228", "WFRBLB50086"]

# Create a FRED object
fred = Fred(api_key)

# Download data
data = {}
for series_id in series_ids:
 try:
 data[series_id] = fred.get_series(series_id, observation_start='1989-01-01')
 if data[series_id] is None or data[series_id].empty:
 print(f"Warning: No data retrieved for series {series_id}")
 except Exception as e:
 print(f"Error retrieving series {series_id}: {str(e)}")

# Check if data is available
if not data or any(df is None or df.empty for df in data.values()):
 print("No data available. Exiting.")
 exit()

# Create a DataFrame
try:
 df = pd.DataFrame(data)
except Exception as e:
 print(f"Error creating DataFrame: {str(e)}")
 exit()

# Calculate the ratio
try:
 df["ratio"] = df["WFRBLTP1228"] / df["WFRBLB50086"]
except ZeroDivisionError:
 print("Error: Division by zero when calculating ratio.")
 exit()
except Exception as e:
 print(f"Error calculating ratio: {str(e)}")
 exit()

# Normalize the data to 1989 values
try:
 df_normalized = df / df.loc[df.index.year == 1989].iloc[0] * 100
except Exception as e:
 print(f"Error normalizing data: {str(e)}")
 exit()

# Create a table with all dates
table = pd.DataFrame({
 "Date": df_normalized.index.strftime('%Y-%m-%d'),
 "Top0.1% Checking Deposits": df_normalized["WFRBLTP1228"],
 "Bottom50% Checking Deposits": df_normalized["WFRBLB50086"],
 "Ratio": df_normalized["ratio"]
})

# Print the table in Markdown format
print(table.to_markdown(index=False))

# Plot the ratio over time
plt.figure(figsize=(10,6))
plt.plot(df_normalized.index, df_normalized["ratio"])
plt.title('Ratio of Top 0.1% to Bottom 50% Checking Deposits Over Time')
plt.xlabel('Year')
plt.ylabel('Ratio (Normalized to 1989)')
plt.grid(True)
plt.show()
