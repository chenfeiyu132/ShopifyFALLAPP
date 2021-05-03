import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data.csv")
print("AOV: ", sum(data["order_amount"])/data.shape[0])
print("Max order amount", max(data["order_amount"]))
print("Average Item value: ", sum(data["order_amount"])/sum(data["total_items"]))
print("Median: ", data["order_amount"].median())
print("Mode: ", data["order_amount"].mode())
print("90 quantile: ", data["order_amount"].quantile(.90))
data = data[data["order_amount"].between(data["order_amount"].quantile(0), data["order_amount"].quantile(.98))]
print("AOV: ", sum(data["order_amount"])/data.shape[0])

shop_customers_purchases = {}
for index, row in data.iterrows(): 
    if row["shop_id"] in shop_customers_purchases:
        shop_customers_purchases[row["shop_id"]][row["user_id"]] = shop_customers_purchases[row["shop_id"]].setdefault(row["user_id"], 0) + 1
    else:
        shop_customers_purchases[row["shop_id"]] = {}

revenues = [0]*100
for index, row in data.iterrows():
    revenues[row["shop_id"]-1] += row["order_amount"]
rev_df = pd.DataFrame({"shop_id": range(1, len(revenues)+1), "revenue": revenues})

filtered_revenue = rev_df[rev_df["revenue"] < rev_df["revenue"].quantile(.95)]["revenue"]
print("average revenue", sum(filtered_revenue)/len(filtered_revenue))
print("difference between best and worst performer: ", max(filtered_revenue)-min(filtered_revenue))