# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Import DateFrame using url
url = "https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv"
dataframe = pd.read_csv(url)

# Display head and firast 10 rows
print("Display head and firast 10 rows:\n", dataframe.head(n=10))
print("Display description:\n", dataframe.describe())

# Display basic information about the DataFrame
print("\nDataFrame Info:\n", dataframe.info())

# 1. Check for missing values
missing_values_summary = dataframe.isnull().sum()
print("Missing Values Summary:\n", missing_values_summary)

# 2. Handle missing values
# Example: Fill missing values in 'Price' and 'Quantity' with 0, and drop rows with missing 'Date'
dataframe['sales'] = dataframe['sales'].fillna(0)
dataframe['quantity'] = dataframe['quantity'].fillna(0)
df = dataframe.dropna(subset=['order_date'])

# 3. Ensure the Date column is in the correct datetime format
dataframe['order_date'] = pd.to_datetime(dataframe['order_date'], errors='coerce')

# Drop rows where Date could not be converted (optional, depending on your needs)
dataframe = dataframe.dropna(subset=['order_date'])

# 4. Create a new column called Revenue if it’s missing
if 'revenue' not in dataframe.columns:
    dataframe['revenue'] = dataframe['quantity'] * dataframe['sales']

# Output the cleaned dataframe
print("Cleaned DataFrame:")
print(dataframe.head())

# Visualization: Plot a bar chart showing the top 5 products by revenue.
products_df = dataframe.sort_values(by='revenue', ascending=False).head(5)
plt.figure(figsize=(8, 6))
plt.bar(products_df['product_name'], products_df['revenue'], color='skyblue')
plt.title('Top 5 Products by Revenue')
plt.xlabel('Products')
plt.ylabel('Revenue')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Create a line graph to visualize daily revenue trends.
plt.figure(figsize=(10, 6))
plt.plot(dataframe['order_date'], dataframe['revenue'], marker='o', linestyle='-', color='green')
plt.title('Daily Revenue Trends')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.grid(True)
plt.tight_layout()
plt.show()

