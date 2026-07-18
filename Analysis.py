import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel("../Data/BRSR_Master_Dataset.xlsx",header=2)
renewable_ranking= df.sort_values(by="Renewable Energy %",
ascending=False)
print(renewable_ranking[["Company","Renewable Energy %"]])

# Sector Scorecard
import pandas as pd


df=pd.read_excel("../Data/BRSR_Master_Dataset.xlsx",header=2)
sector_score= df.groupby("Sector")["Renewable Energy %"].mean()
print(sector_score)

#Calculate Overall Average
overall_avg = df["Renewable Energy %"].mean()
print("Overall Renewable Energy %:",overall_avg)
#Comparing every sector with overall average
sector_score = sector_score.to_frame()
sector_score["Overall Average"] = overall_avg
sector_score["Performance"] = sector_score["Renewable Energy %"].apply(
    lambda x: "Above Average" if x > overall_avg else "Below Average")

print(sector_score)

#Company Benchmark
import pandas as pd

df = pd.read_excel("../Data/BRSR_Master_Dataset.xlsx", header=2)

sector_avg = df.groupby("Sector")["Renewable Energy %"].mean()

print(sector_avg)
df["Sector Average"] = df["Sector"].map(sector_avg)
df["Performance"] = df.apply(
    lambda row: "Above Sector Average"
    if row["Renewable Energy %"] > row["Sector Average"]
    else "Below Sector Average",
    axis=1)
print(df[[
    "Company",
    "Sector",
    "Renewable Energy %",
    "Performance"]])

# Executive KPIs
total_companies = df["Company"].nunique()
print("Total Companies:", total_companies)
avg_renewable = df["Renewable Energy %"].mean()
print("Average Renewable Energy:", round(avg_renewable * 100, 2), "%")

best_company = df.loc[df["Renewable Energy %"].idxmax()]
print("Best Company:", best_company["Company"])

worst_company = df.loc[df["Renewable Energy %"].idxmin()]
print("Lowest Company:", worst_company["Company"])
