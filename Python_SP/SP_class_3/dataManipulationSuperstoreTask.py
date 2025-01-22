# Import necessary libraries
import pandas as pd

from Python_SP.SP_class_3.dataManipulation import df_missing

# Import DateFrame using url
url = "https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv"
df = pd.read_csv(url)


# Group sales by Region and Category.
grouped = df.groupby(['region', "category"])['sales'].sum()
print("\nGroup sales by Region and Category\n", grouped)

# Handle missing sales data using fillna().
df["sales"] = df["sales"].fillna(0)

# Create a pivot table for monthly sales trends.
# Extract month from the Date column
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['month'] = df['order_date'].dt.to_period('M')
pivot = df.pivot_table(index='month', values='sales', aggfunc='sum')
print("\nPivot Table:\n", pivot)

