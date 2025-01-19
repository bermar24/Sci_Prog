# Import necessary libraries
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset directly from seaborn (it's available online)
#df = sns.load_dataset('tips')
df = pd.read_csv('https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv')

# Inspect the dataset
print(df.head())

# Data Preprocessing
# Check for missing values
print(df.isnull().sum())

# Encode categorical variables using one-hot encoding
#df_encoded = pd.get_dummies(df, drop_first=True)

# Select target variable (Total Bill) and features
#X = df_encoded.drop(columns=['profit'])
#y = df_encoded['profit']

# Train-Test Split (80% train, 20% test)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model 1: Linear Regression
#lr_model = LinearRegression()
#lr_model.fit(X_train, y_train)

#penguins https://github.com/mwaskom/seaborn-data/blob/master/penguins.csv
df_penguins = sns.load_dataset('penguins')
print(df_penguins.head())
