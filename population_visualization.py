
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_123525.csv", skiprows=4)

# Filter and prepare top 10 countries by population for 2022
year = "2022"
df_year = df[["Country Name", year]].dropna()
df_year[year] = pd.to_numeric(df_year[year], errors='coerce')
top10 = df_year.sort_values(by=year, ascending=False).head(10)
top10.to_csv("top10_population_2022.csv", index=False)

# Plot and save chart
plt.figure(figsize=(12, 6))
plt.bar(top10["Country Name"], top10[year], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Population")
plt.title("Top 10 Most Populous Countries in 2022")
plt.tight_layout()
plt.savefig("top10_population_2022.png")
plt.show()
