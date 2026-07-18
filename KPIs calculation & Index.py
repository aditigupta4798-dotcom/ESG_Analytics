import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# Read Dataset
df = pd.read_excel("../Data/BRSR_Master_Dataset.xlsx", header=2)
# DERIVED KPIs
# 1. Carbon Intensity
df["Carbon Intensity"] = (df["Scope 1 ( tCo2e)"] / df["Total Employees"])
# 2. Energy Intensity
df["Energy Intensity"] = (
    df["Total Energy Consumed ( GJ )"] /
    df["Total Employees"])
# 3. Water Intensity
df["Water Intensity"] = (
    df["Water Withdrawal (in kilolitres)"] /
    df["Total Employees"])
# 4. Waste Intensity
df["Waste Intensity"] = (
    df["Waste Generated ( in metric tonnes)"] /
    df["Total Employees"])
# 5. Renewable Energy Ratio (%)
df["Renewable Energy Ratio"] = (
    df["Renewable Energy %"] * 100)
# 6. Employee Diversity Index
df["Employee Diversity Index"] = (
    df["Women Employees % (Including other than permanent)"] +
    df["Women Directors %"]) / 2
# 7. Employee Stability Index
df["Employee Stability Index"] = (
    100 - df["Employee Turnover %"])
# 8. Sustainability Efficiency Score
df["Sustainability Efficiency"] = ((df["Renewable Energy %"] * 100) /(
        df["Carbon Intensity"] +
        df["Energy Intensity"] +
        df["Water Intensity"] ))
# Display Results
print(df[["Company",
    "Carbon Intensity",
    "Energy Intensity",
    "Water Intensity",
    "Waste Intensity",
    "Renewable Energy Ratio"]])

#KPI Ranking
carbon_rank = df.sort_values(
    by="Carbon Intensity",
    ascending=True)
print(carbon_rank[["Company", "Carbon Intensity"]])

energy_rank = df.sort_values(
    by="Energy Intensity",
    ascending=True)
print(energy_rank[["Company", "Energy Intensity"]])

water_rank = df.sort_values(
    by="Water Intensity",
    ascending=True)
print(water_rank[["Company", "Water Intensity"]])

waste_rank = df.sort_values(
    by="Waste Intensity",
    ascending=True)
print(waste_rank[["Company", "Waste Intensity"]])

#KPI Correlation
kpi_columns = ["Carbon Intensity",
    "Energy Intensity",
    "Water Intensity",
    "Waste Intensity",
    "Employee Diversity Index",
    "Employee Stability Index",
    "Sustainability Efficiency"]
kpi_corr = df[kpi_columns].corr()
print(kpi_corr)


# ESG Index
scaler = MinMaxScaler()
kpi_columns = ["Renewable Energy %",
    "Carbon Intensity",
    "Energy Intensity",
    "Water Intensity",
    "Waste Intensity",
    "Women Employees % (Including other than permanent)",
    "Employee Diversity Index",
    "Employee Stability Index",
    "Women Directors %"]
scaled = scaler.fit_transform(df[kpi_columns])
scaled_df = pd.DataFrame(scaled,columns=kpi_columns)
print(scaled_df.head())

scaled_df["Carbon Intensity"] = 1 - scaled_df["Carbon Intensity"]

scaled_df["Energy Intensity"] = 1 - scaled_df["Energy Intensity"]

scaled_df["Water Intensity"] = 1 - scaled_df["Water Intensity"]

scaled_df["Waste Intensity"] = 1 - scaled_df["Waste Intensity"]


scaled_df["Environmental Score"] = (
    scaled_df["Renewable Energy %"] * 0.30 +
    scaled_df["Carbon Intensity"] * 0.25 +
    scaled_df["Energy Intensity"] * 0.15 +
    scaled_df["Water Intensity"] * 0.15 +
    scaled_df["Waste Intensity"] * 0.15)

scaled_df["Social Score"] = (
    scaled_df["Women Employees % (Including other than permanent)"] * 0.40 +
    scaled_df["Employee Diversity Index"] * 0.30 +
    scaled_df["Employee Stability Index"] * 0.30)

scaled_df["Governance Score"] = (scaled_df["Women Directors %"])

scaled_df["ESG Performance Index"] = (scaled_df["Environmental Score"] * 0.40 + scaled_df["Social Score"] * 0.35 + scaled_df["Governance Score"] * 0.25)

scaled_df["ESG Performance Index"] = (scaled_df["ESG Performance Index"] * 100)

scaled_df["Company"] = df["Company"]
scaled_df["Sector"] = df["Sector"]

esg_rank = scaled_df.sort_values(
    by="ESG Performance Index",
    ascending=False)

print(esg_rank[[
    "Company",
    "Sector",
    "Environmental Score",
    "Social Score",
    "Governance Score",
    "ESG Performance Index"]])

def classify(score):
    if score >= 85:
        return "ESG Leader"
    elif score >= 70:
        return "Strong Performer"
    elif score >= 50:
        return "Average Performer"
    else:
        return "ESG Laggard"

scaled_df["ESG Category"] = scaled_df["ESG Performance Index"].apply(classify)

print(
    scaled_df[
        ["Company",
         "Sector",
         "ESG Performance Index",
         "ESG Category"]
    ].sort_values(
        by="ESG Performance Index",
        ascending=False))

import matplotlib.pyplot as plt

category_count = scaled_df["ESG Category"].value_counts()

category_count.plot(kind="bar")

plt.title("Distribution of ESG Categories")
plt.xlabel("Category")
plt.ylabel("Number of Companies")

plt.show()

# ============================
# Create Final Master Dataset
# ============================

final_dataset = df.copy()

# Add Derived KPIs
final_dataset["Carbon Intensity"] = df["Carbon Intensity"]
final_dataset["Energy Intensity"] = df["Energy Intensity"]
final_dataset["Water Intensity"] = df["Water Intensity"]
final_dataset["Waste Intensity"] = df["Waste Intensity"]
final_dataset["Employee Diversity Index"] = df["Employee Diversity Index"]
final_dataset["Employee Stability Index"] = df["Employee Stability Index"]
final_dataset["Sustainability Efficiency"] = df["Sustainability Efficiency"]

# Add ESG Scores
final_dataset["Environmental Score"] = scaled_df["Environmental Score"]
final_dataset["Social Score"] = scaled_df["Social Score"]
final_dataset["Governance Score"] = scaled_df["Governance Score"]
final_dataset["ESG Performance Index"] = scaled_df["ESG Performance Index"]
final_dataset["ESG Category"] = scaled_df["ESG Category"]

# Save Dataset
final_dataset.to_excel("../Data/BRSR_Final_Dataset.xlsx", index=False)

print("Final Master Dataset Saved Successfully!")
