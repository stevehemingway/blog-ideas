import matplotlib.pyplot as plt

# Data from IQ-and-national-income.md
data = [
    ("Singapore", 108, 64133),
    ("South Korea", 106, 34994),
    ("Japan", 105, 44914),
    ("Italy", 102, 34483),
    ("Spain", 101, 30996),
    ("United States", 98, 69862),
    ("United Kingdom", 100, 43734),
    ("France", 98, 43551),
    ("Germany", 99, 49396),
    ("Australia", 98, 52610),
    ("Canada", 99, 52144),
    ("China", 104, 12961),
    ("India", 81, 7056),
    ("Brazil", 87, 14845),
    ("Russia", 96, 23549),
    ("South Africa", 84, 13454),
    ("Nigeria", 69, 5353),
    ("Ethiopia", 63, 2423),
]

# Extract data into separate lists
countries = [d[0] for d in data]
iq_values = [d[1] for d in data]
gdp_values = [d[2] for d in data]

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(iq_values, gdp_values)

# Annotate points with country names
for i, country in enumerate(countries):
    plt.annotate(country, (iq_values[i], gdp_values[i]))

# Set labels and title
plt.xlabel("Average IQ")
plt.ylabel("GDP per capita (USD)")
plt.title("Average IQ vs GDP per capita")

# Show plot
plt.show()
