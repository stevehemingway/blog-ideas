import pandas as pd
import matplotlib.pyplot as plt

# Load the normalized DataFrame
df_normalized = pd.read_csv('normalized_data.csv', index_col='Date', parse_dates=['Date'])

# Plot the ratio over time
plt.figure(figsize=(10,6))
plt.plot(df_normalized.index, df_normalized["Ratio"])
plt.title('Ratio of Top 0.1% to Bottom 50% Checking Deposits Over Time')
plt.xlabel('Year')
plt.ylabel('Ratio (Normalized to 1989)')
plt.grid(True)
plt.savefig('ratio_over_time.png', bbox_inches='tight')
