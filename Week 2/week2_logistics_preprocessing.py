"""
Week 2: Logistics data preprocessing demonstration.
The data below are synthetic practice records, not real company data.
Replace them with a permitted public dataset before reporting real findings.
"""
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = [
    {"shipment_id":"S001","distance_km":12,"shipping_cost":140,"delivery_days":1,"region":"North"},
    {"shipment_id":"S002","distance_km":35,"shipping_cost":320,"delivery_days":3,"region":"South"},
    {"shipment_id":"S003","distance_km":None,"shipping_cost":190,"delivery_days":2,"region":"north"},
    {"shipment_id":"S004","distance_km":42,"shipping_cost":None,"delivery_days":3,"region":"East"},
    {"shipment_id":"S005","distance_km":9,"shipping_cost":110,"delivery_days":1,"region":"West"},
    {"shipment_id":"S006","distance_km":27,"shipping_cost":260,"delivery_days":2,"region":"South"},
    {"shipment_id":"S006","distance_km":27,"shipping_cost":260,"delivery_days":2,"region":"South"},
    {"shipment_id":"S007","distance_km":950,"shipping_cost":900,"delivery_days":4,"region":"East"},
    {"shipment_id":"S008","distance_km":16,"shipping_cost":175,"delivery_days":2,"region":"West"},
]
df = pd.DataFrame(data)

print("Raw preview:\n", df.head())
print("\nShape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nExact duplicate rows:", df.duplicated().sum())

# Remove confirmed exact duplicate rows; investigate repeated IDs in real data.
df = df.drop_duplicates().copy()

# Standardize category formatting.
df["region"] = df["region"].astype("string").str.strip().str.title()

# Demonstration only: median imputation for missing numeric values.
for col in ["distance_km", "shipping_cost", "delivery_days"]:
    df[col] = df[col].fillna(df[col].median())

# Flag possible distance outliers using the IQR rule; do not delete automatically.
q1 = df["distance_km"].quantile(0.25)
q3 = df["distance_km"].quantile(0.75)
iqr = q3 - q1
low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
df["distance_outlier_flag"] = ~df["distance_km"].between(low, high)
print("\nPossible distance outliers:\n",
      df.loc[df["distance_outlier_flag"], ["shipment_id", "distance_km"]])

# Scaling example. In predictive modelling, fit scalers on training data only.
numeric_cols = ["distance_km", "shipping_cost", "delivery_days"]
minmax = MinMaxScaler()
df[[c + "_minmax" for c in numeric_cols]] = minmax.fit_transform(df[numeric_cols])
standard = StandardScaler()
df[[c + "_standard" for c in numeric_cols]] = standard.fit_transform(df[numeric_cols])

print("\nProcessed data:\n", df)
df.to_csv("cleaned_logistics_example.csv", index=False)
print("\nSaved cleaned_logistics_example.csv")

# Important: these rows are synthetic and demonstrate the process only.
