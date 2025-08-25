import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Download FRED data and calculate ratio')
parser.add_argument('series_ids', type=str, nargs=2, help='FRED series IDs (top 0.1% and bottom 50%)')
args = parser.parse_args()

# FRED API Key
api_key = "e13c8cee393d1c8cb726df61858ff73a"

# Series IDs from command-line arguments
series_ids = args.series_ids

# Create a FRED object
fred = Fred(api_key)

# Download data
data = {}
for series_id in series_ids:
 try:
 data[series_id] = fred.get_series(series_id, observation_start='1989-01-01')
 except Exception as e:
 print(f"Error retrieving series {series_id}: {str(e)}")
 if data.get(series_id) is not None and not data[series_id].empty:
 print(f"Warning: Data retrieved for series {series_id}")
 else:
 print(f"Warning: No data retrieved for series {series_id}")

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

# Adjust the data for equivalent number of depositors
try:
 df["adjusted"] = df[series_ids[1]] / 500
except Exception as e:
 print(f"Error adjusting data: {str(e)}")
 exit()

# Calculate the ratio
try:
 df["ratio"] = df[series_ids[0]] / df["adjusted"]
except ZeroDivisionError:
 print("Error: Division by zero when calculating ratio.")
 exit()
except Exception as e:
 print(f"Error calculating ratio: {str(e)}")
 exit()

# Create a table with all dates
table = pd.DataFrame({
 "Date": df.index.strftime('%Y-%m-%d'),
 f"{series_ids[0]}": df[series_ids[0]],
 f"{series_ids[1]} (adjusted)": df["adjusted"],
 "Ratio": df["ratio"]
})

# Print the table in Markdown format
print(table.to_markdown(index=False))

# Plot the ratio over time
plt.figure(figsize=(10,6))
plt.plot(df.index, df["ratio"])
plt.title('Ratio of Top0.1% to Bottom50% Checking Deposits Over Time', fontsize=24)
plt.xlabel('Year', fontsize=20)
plt.ylabel('Ratio', fontsize=20)
plt.grid(True)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()
