# Importing necessary libraries
import pandas as pd

# Loading a dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
# OR df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Viewing data
print("First 5 rows:\n", df.head())
print("\nSummary Info:\n", df.info())
print("\nLast few rows:\n", df.tail())
print("\nDescriptive statistics:\n", df.describe())

# Accessing data
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Access using iloc:\n", df.iloc[0:2, 0:2])
print("Access using loc:\n", df.loc[0:2, ["sepal_length", "sepal_width"]])



# TODO: other way to import and convert to panda DataFrame
# # Load the Iris dataset
# # iris = load_iris()
# # iris.data[0:3]
# # iris.feature_names
# # iris.target
#
# # Convert to a pandas DataFrame
# data = pd.DataFrame(
#     data=iris.data,  # Features
#     columns=iris.feature_names  # Feature names
# )
#
# # Add the target column (species)
# data['species'] = iris.target
#
# # Map target numbers to species names
# data['species'] = data['species'].map({
#     0: 'setosa',
#     1: 'versicolor',
#     2: 'virginica'
# })

# Count the number of samples per species
# print("\nSample count per species:")
# print(data['species'].value_counts())