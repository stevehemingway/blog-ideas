import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt
import argparse
import os

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Download FRED data and calculate ratio')
parser.add_argument('top_series_id', type=str, help='FRED series ID for top0.1%')
parser.add_argument('bottom_series_id', type=str, help='FRED series ID for bottom50%')
args = parser.parse_args()

# FRED API Key from environmental variable
api_key = os.environ.get('FRED_API_KEY')
if api_key is None:
    print("Error: FRED_API_KEY environmental variable is not set.")
    exit()

# Series IDs from command-line arguments
series_ids = [args.top_series_id, args.bottom_series_id]

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
    df["adjusted"] = df[args.bottom_series_id] / 500
except Exception as e:
    print(f"Error adjusting data: {str(e)}")
    exit()

# Calculate the ratio
try:
    df["ratio"] = df[args.top_series_id] / df["adjusted"]
except ZeroDivisionError:
    print("Error: Division by zero when calculating ratio.")
    exit()
except Exception as e:
    print(f"Error calculating ratio: {str(e)}")
    exit()

# Create a table with all dates
table = pd.DataFrame({
    "Date": df.index.strftime('%Y-%m-%d'),
    f"{args.top_series_id}": df[args.top_series_id],
    f"{args.bottom_series_id} (adjusted)": df["adjusted"],
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
