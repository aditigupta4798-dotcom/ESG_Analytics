from statistics import correlation

import pandas as pd
df=pd.read_excel("../data/BRSR_Master_Dataset.xlsx", header=2)

print(df.shape)

print(df.columns)

print(df.info())

print(df.isnull().sum())

print(df.dtypes)

print(df.describe())


sector_avg=df.groupby("Sector").mean(numeric_only=True)
print(sector_avg)

import matplotlib.pyplot as plt
# Find Women Employees in Sector wise
sector_avg["Women Employees % (Including other than permanent)"].plot(kind="bar")
plt.title("Average Women Employees by Sector")
plt.xlabel("Sector")
plt.ylabel("Women Employees (%)")
plt.show()

# Sort companies from highest to lowest renewable energy
renewable = df.sort_values(by="Renewable Energy %", ascending=False)

# Create chart
plt.figure(figsize=(10,6))

plt.barh(renewable["Company"], renewable["Renewable Energy %"])

plt.title("Renewable Energy Usage by Company")
plt.xlabel("Renewable Energy (%)")
plt.ylabel("Company")

plt.show()

# Sort Sectors from highest to lowest scope 1 emissions production
scope1_avg = df.groupby("Sector")["Scope 1 ( tCo2e)"].mean().plot(kind="bar")
plt.title("Average Scope 1 Emissions by Sector")
plt.xlabel("Sector")
plt.ylabel("Scope 1 ( tCo2e)")

plt.show()

#Correlation Heatmap
import seaborn as sns
correlation = df.corr(numeric_only=True)
print(correlation)
plt.figure(figsize=(12,8))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of ESG Indicators")
plt.show()

