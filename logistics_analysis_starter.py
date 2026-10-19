"""
Week 1 - Logistics Delivery Performance and Cost Analysis
Illustrative starter script for a strategic-planning assignment.

IMPORTANT:
- The rows below are small illustrative examples, not real company data.
- Replace them with a permitted public dataset before reporting real findings.
- This script calculates basic KPIs; predictive modelling is proposed in the report
  and should only be attempted after checking the dataset's fields and quality.
"""

import pandas as pd

# Illustrative data only. Replace with a public dataset CSV when ready.
data = {
    "shipment_id": ["S001", "S002", "S003", "S004", "S005", "S006"],
    "distance_km": [12, 35, 18, 42, 9, 27],
    "shipping_cost": [140, 320, 190, 410, 110, 260],
    "promised_days": [1, 2, 1, 3, 1, 2],
    "actual_days": [1, 3, 2, 3, 1, 2],
    "delivery_status": ["On time", "Delayed", "Delayed", "On time", "On time", "On time"],
    "region": ["North", "South", "North", "East", "West", "South"],
}

df = pd.DataFrame(data)

# 1. Basic data checks
print("First rows:")
print(df.head())
print("\nMissing values per column:")
print(df.isna().sum())
print("\nDuplicate shipment IDs:", df["shipment_id"].duplicated().sum())

# 2. Calculate KPIs
total_shipments = len(df)
on_time_rate = (df["actual_days"] <= df["promised_days"]).mean() * 100
average_shipping_cost = df["shipping_cost"].mean()
average_delivery_days = df["actual_days"].mean()
delayed_shipments = (df["actual_days"] > df["promised_days"]).sum()

print("\n--- Illustrative KPI summary (not real business findings) ---")
print(f"Total shipments: {total_shipments}")
print(f"On-time delivery rate: {on_time_rate:.1f}%")
print(f"Average shipping cost: {average_shipping_cost:.2f}")
print(f"Average delivery time: {average_delivery_days:.2f} days")
print(f"Delayed shipments: {delayed_shipments}")

# 3. Explore performance by region
region_summary = df.groupby("region").agg(
    shipments=("shipment_id", "count"),
    mean_cost=("shipping_cost", "mean"),
    mean_delivery_days=("actual_days", "mean"),
    on_time_rate=("actual_days", lambda x: (
        x <= df.loc[x.index, "promised_days"]
    ).mean() * 100),
).round(2)

print("\nPerformance by region:")
print(region_summary)

# 4. Optional: save the summary to a CSV file
region_summary.to_csv("regional_kpi_summary.csv")
print("\nSaved regional_kpi_summary.csv")

# Planned next step (not implemented here):
# After sourcing and cleaning a sufficiently large, appropriate dataset,
# build a regression model to estimate delivery time. Split the data into
# training and test sets, evaluate on unseen data, and compare with a simple
# baseline. Avoid using information that would not be known at prediction time.
