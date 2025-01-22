# Import necesary libraries
import pandas as pd
import numpy as np

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
df = dataframe.dropna(subset=['Date'])

# 3. Ensure the Date column is in the correct datetime format
# dataframe['Date'] = pd.to_datetime(dataframe['Date'], errors='coerce')
#
# # Drop rows where Date could not be converted (optional, depending on your needs)
# #dataframe = dataframe.dropna(subset=['Date'])
#
# # 4. Create a new column called Revenue if it’s missing
# if 'Revenue' not in dataframe.columns:
#     dataframe['Revenue'] = dataframe['Quantity'] * dataframe['Price']
#
# # Output the cleaned dataframe
# print("Cleaned DataFrame:")
# print(dataframe.head())
