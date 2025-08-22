import matplotlib.pyplot as plt

# Data from coal-and-renewables.md
data = [
    ("Mexico", 4.3, 25),
    ("Chile", 5.6, 40),
    ("USA", 12, 20),
    ("Canada", 12, 65),
    ("Norway", 15, 95),
    ("Japan", 16, 20),
    ("Korea", 16, 6),
    ("Australia", 17, 25),
    ("Israel", 18, 8),
    ("Turkey", 18, 40),
    ("Spain", 22, 45),
    ("Portugal", 23, 60),
    ("Greece", 24, 35),
    ("Italy", 25, 35),
    ("Slovenia", 25, 35),
    ("Estonia", 26, 15),
    ("Czech Republic", 27, 15),
    ("Slovakia", 27, 25),
    ("Hungary", 28, 15),
    ("Poland", 28, 15),
    ("Denmark", 33, 50),
    ("Germany", 38, 45),
    ("Ireland", 38, 35),
    ("Belgium", 39, 20),
    ("Netherlands", 40, 20),
    ("UK", 40, 40),
    ("Switzerland", 42, 60),
    ("Austria", 43, 75),
    ("Luxembourg", 44, 15),
    ("France", 45, 25),
]

# Extract the data
costs = [d[1] for d in data]
renewables_percent = [d[2] for d in data]

# Create the plot
plt.scatter(renewables_percent, costs)
plt.xlabel("Renewables Percentage")
plt.ylabel("Energy Cost (¢/kWh USD)")
plt.title("Energy Cost vs Renewables Percentage")
plt.grid(True)

# Save the plot to a file
plt.savefig("energy_cost_vs_renewables.png")

# Show the plot
plt.show()
