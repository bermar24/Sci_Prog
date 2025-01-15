import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85, 90, 95]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Accessing a Series
print("Series:\n", df["Age"])

# Loading a dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Viewing data
print("First 5 rows:\n", df.head())
print("\nSummary Info:\n")
df.info()

# Accessing data
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Access using iloc:\n", df.iloc[0:2, 0:2])
print("Access using loc:\n", df.loc[0:2, ["sepal_length", "sepal_width"]])