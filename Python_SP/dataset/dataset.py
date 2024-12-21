# Importing necessary libraries
import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
iris.data[0:3]
iris.feature_names
iris.target

# Convert to a pandas DataFrame
data = pd.DataFrame(
    data=iris.data,  # Features
    columns=iris.feature_names  # Feature names
)

# Add the target column (species)
data['species'] = iris.target

# Map target numbers to species names
data['species'] = data['species'].map({
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
})

# Display the first few rows of the DataFrame
print("First 5 rows of the Iris dataset:")
print(data.head())

# Display basic information about the DataFrame
print("\nDataFrame Info:")
print(data.info())

# Display basic statistics of the numerical columns
print("\nSummary Statistics:")
print(data.describe())

# Count the number of samples per species
print("\nSample count per species:")
print(data['species'].value_counts())