import pandas as pd
import matplotlib.pyplot as plt

# data (copy the table into a CSV or dict)
data = {
    "Year": list(range(1972, 2025)),
    "PctChange": [4.9,6.7,5.1,2.9,3.8,4.2,4.6,5.2,6.1,5.5,4.0,5.1,5.0,3.8,4.2,4.5,
                  3.9,4.1,4.3,2.2,1.9,1.5,2.0,3.4,3.2,3.5,2.9,3.0,4.0,2.8,3.3,3.5,
                  3.9,4.5,4.2,4.1,2.5,-2.5,5.0,3.5,2.0,2.1,2.6,2.4,2.9,2.8,2.5,2.2,
                 -1.7,6.8,4.9,5.1,2.3]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10,5))
plt.plot(df['Year'], df['PctChange'], marker='o')
plt.axhline(0, color='gray', linewidth=0.8)
plt.title('Year‑on‑Year % Change in UK GDP per Working‑Age Person (16‑64)')
plt.xlabel('Year')
plt.ylabel('Percentage change (%)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
