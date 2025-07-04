import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("synthetic_natural_disasters_dataset.csv")

# Convert Damage from USD to INR (₹)
df['Damage_INR'] = df['Damage_USD'] * 83

# 1. Total Deaths by Disaster Type
df.groupby('Disaster_Type')['Total_Deaths'].sum().sort_values(ascending=False).plot(
    kind='bar', color='firebrick', title='Total Deaths by Disaster Type')
plt.ylabel("Total Deaths")
plt.xlabel("Disaster Type")
plt.tight_layout()
plt.show()

# 2. Average Damage by Disaster Type (INR)
df.groupby('Disaster_Type')['Damage_INR'].mean().sort_values(ascending=False).plot(
    kind='bar', color='darkorange', title='Avg Damage by Disaster Type (INR)')
plt.ylabel("Avg Damage (₹)")
plt.xlabel("Disaster Type")
plt.tight_layout()
plt.show()

# 3. Top 10 Countries by Displaced People
df.groupby('Country')['Displaced_People'].sum().sort_values(ascending=False).head(10).plot(
    kind='barh', color='royalblue', title='Top 10 Countries by Displaced People')
plt.xlabel("Displaced People")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# 4. Yearly Total Damage Trend (INR)
df.groupby('Year')['Damage_INR'].sum().sort_index().plot(
    kind='line', marker='o', color='seagreen', title='Yearly Total Damage (INR)')
plt.xlabel("Year")
plt.ylabel("Total Damage (₹)")
plt.tight_layout()
plt.show()

# 5. Average Displaced People by Disaster Type
df.groupby('Disaster_Type')['Displaced_People'].mean().sort_values(ascending=False).plot(
    kind='bar', color='mediumpurple', title='Avg Displaced People by Disaster Type')
plt.ylabel("Avg Displaced People")
plt.xlabel("Disaster Type")
plt.tight_layout()
plt.show()

# 6. Histogram of Total Deaths per Event
df['Total_Deaths'].plot(
    kind='hist', bins=30, color='crimson', title='Distribution of Deaths per Disaster')
plt.xlabel("Deaths per Event")
plt.tight_layout()
plt.show()
