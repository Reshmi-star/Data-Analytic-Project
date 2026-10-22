"""Week 3 Logistics EDA. Hypothetical sample data, not real company data.
Install: pip install pandas matplotlib numpy
Run: python week3_logistics_eda_visualization.py
"""
import pandas as pd
import matplotlib.pyplot as plt

data = [
[101,"North","Road",120,2.1,18,2,"On Time"],[102,"South","Road",85,1.4,12,1,"On Time"],
[103,"East","Air",310,0.8,8,0,"On Time"],[104,"West","Road",160,3.2,25,4,"Delayed"],
[105,"North","Rail",190,2.5,30,2,"On Time"],[106,"South","Road",95,1.8,15,3,"Delayed"],
[107,"East","Road",140,2.2,20,1,"On Time"],[108,"West","Air",340,0.7,9,0,"On Time"],
[109,"North","Road",130,2.9,22,3,"Delayed"],[110,"South","Rail",175,2.4,28,1,"On Time"],
[111,"East","Road",115,1.9,16,2,"On Time"],[112,"West","Road",155,3.5,27,5,"Delayed"],
[113,"North","Air",295,0.9,10,0,"On Time"],[114,"South","Road",105,2.7,21,4,"Delayed"],
[115,"East","Rail",205,2.3,31,2,"On Time"],[116,"West","Road",170,3.1,24,3,"Delayed"],
[117,"North","Road",125,2.0,17,1,"On Time"],[118,"South","Air",325,0.8,9,0,"On Time"],
[119,"East","Road",145,2.6,23,3,"Delayed"],[120,"West","Rail",185,2.8,32,2,"On Time"],
[121,"North","Road",135,2.4,20,2,"On Time"],[122,"South","Road",90,3.0,24,4,"Delayed"],
[123,"East","Air",305,0.9,11,0,"On Time"],[124,"West","Road",165,3.3,26,4,"Delayed"]]
cols=["Shipment_ID","Region","Transport_Mode","Shipment_Volume_kg","Delivery_Time_days","Transport_Cost_USD","Delay_Days","Delivery_Status"]
df=pd.DataFrame(data,columns=cols)
numeric=["Shipment_Volume_kg","Delivery_Time_days","Transport_Cost_USD","Delay_Days"]

print("Preview:\\n",df.head())
print("\\nDescriptive statistics:\\n",df[numeric].describe().round(2))
print("\\nStatus counts:\\n",df["Delivery_Status"].value_counts())
print("\\nAverage cost by mode:\\n",df.groupby("Transport_Mode")["Transport_Cost_USD"].mean().round(2))
print("\\nAverage delivery time by region:\\n",df.groupby("Region")["Delivery_Time_days"].mean().round(2))
print("\\nCorrelation matrix:\\n",df[numeric].corr().round(2))

plt.figure(figsize=(8,5)); plt.hist(df["Delivery_Time_days"],bins=7,edgecolor="black")
plt.title("Distribution of Delivery Time"); plt.xlabel("Delivery time (days)"); plt.ylabel("Shipment count")
plt.tight_layout(); plt.savefig("week3_delivery_time_distribution.png",dpi=150); plt.show()

mode_cost=df.groupby("Transport_Mode")["Transport_Cost_USD"].mean().reindex(["Road","Rail","Air"])
plt.figure(figsize=(8,5)); plt.bar(mode_cost.index,mode_cost.values)
plt.title("Average Transportation Cost by Mode"); plt.xlabel("Transport mode"); plt.ylabel("Average cost (USD)")
plt.tight_layout(); plt.savefig("week3_average_cost_by_mode.png",dpi=150); plt.show()

plt.figure(figsize=(8,5)); plt.scatter(df["Delivery_Time_days"],df["Transport_Cost_USD"])
plt.title("Delivery Time vs Transportation Cost"); plt.xlabel("Delivery time (days)"); plt.ylabel("Transportation cost (USD)")
plt.tight_layout(); plt.savefig("week3_delivery_time_vs_cost.png",dpi=150); plt.show()

counts=df["Delivery_Status"].value_counts().reindex(["On Time","Delayed"],fill_value=0)
plt.figure(figsize=(8,5)); plt.bar(counts.index,counts.values)
plt.title("On-Time vs Delayed Shipments"); plt.xlabel("Delivery status"); plt.ylabel("Shipment count")
plt.tight_layout(); plt.savefig("week3_delivery_status.png",dpi=150); plt.show()

corr=df[numeric].corr()
plt.figure(figsize=(8,5)); plt.imshow(corr.values,aspect="auto")
plt.xticks(range(len(numeric)),numeric,rotation=25,ha="right"); plt.yticks(range(len(numeric)),numeric)
plt.colorbar(label="Correlation"); plt.title("Correlation Heatmap")
for i in range(len(numeric)):
    for j in range(len(numeric)): plt.text(j,i,f"{corr.iloc[i,j]:.2f}",ha="center",va="center")
plt.tight_layout(); plt.savefig("week3_correlation_heatmap.png",dpi=150); plt.show()

region_time=df.groupby("Region")["Delivery_Time_days"].mean().reindex(["North","South","East","West"])
plt.figure(figsize=(8,5)); plt.bar(region_time.index,region_time.values)
plt.title("Average Delivery Time by Region"); plt.xlabel("Region"); plt.ylabel("Average delivery time (days)")
plt.tight_layout(); plt.savefig("week3_average_delivery_by_region.png",dpi=150); plt.show()

df.to_csv("week3_hypothetical_logistics_data.csv",index=False)
print("Saved PNG charts and week3_hypothetical_logistics_data.csv")
