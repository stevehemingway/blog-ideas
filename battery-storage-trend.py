# --------------------------------------------------------------
# Battery‑storage cost trend (domestic lithium‑ion) – 2010‑2022
# --------------------------------------------------------------
# Author: ChatGPT (Compound Mini)
# Requirements: matplotlib, numpy
# --------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 1. Data – known anchor points (source: JoinACT / other industry data)
#    2010  ≈ $1,100/kWh
#    2022  ≈ $137/kWh
# ------------------------------------------------------------------
year_start, cost_start = 2010, 1100.0  # $/kWh
year_end, cost_end = 2022, 137.0  # $/kWh

# Build a yearly array
years = np.arange(year_start, year_end + 1)

# Interpolate on a log‑scale (cost roughly follows an exponential decay)
log_costs = np.linspace(np.log10(cost_start), np.log10(cost_end), len(years))
costs = 10**log_costs  # back‑to‑linear values

# ------------------------------------------------------------------
# 2. Plotting
# ------------------------------------------------------------------
plt.figure(figsize=(9, 5))
plt.plot(years, costs, marker="o", linestyle="-", color="steelblue")

# Use a logarithmic y‑axis to show the exponential drop more clearly
plt.yscale("log")
plt.grid(which="both", linestyle="--", linewidth=0.5, alpha=0.7)

plt.title("Domestic Lithium‑Ion Battery‑Storage Cost (2010‑2022)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Cost ($/kWh, log scale)", fontsize=12)

# Annotate the start and end points
plt.annotate(
    f"${cost_start:,.0f}/kWh (2010)",
    xy=(year_start, cost_start),
    xycoords="data",
    xytext=(-40, 30),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->", color="gray"),
)

plt.annotate(
    f"${cost_end:,.0f}/kWh (2022)",
    xy=(year_end, cost_end),
    xycoords="data",
    xytext=(-40, -40),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->", color="gray"),
)

plt.tight_layout()
plt.show()
