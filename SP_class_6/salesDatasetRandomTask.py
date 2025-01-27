# For the Superstore Sales Dataset, you can:
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder



# Import DateFrame using url
url = "https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv"
super_df = pd.read_csv(url)
# convert to panda DataFrame???

# Exploratory Data Analysis (EDA)
# print("Display head:\n", super_df.head(n=10))
print("Display columns:\n", super_df.columns)
# print("Display cat reg:\n", super_df[['category', 'region']].head())

#Handling missing data
# print(f'missing data:\n {super_df.isnull().sum()}')
super_df = super_df.dropna()

# 1.Predict the total sales of an order by looking at details like product category, region, and quantity sold.
# Split df
X = super_df[['category', 'region', 'quantity']] # Feature
y = super_df['sales'] # Target
# encode X
X = pd.get_dummies(X, columns=['category', 'region'])
print(X.head())
# X.loc[:,'category'] = LabelEncoder().fit_transform(X['category'])
# X.loc[:,'region'] = LabelEncoder().fit_transform(X['region'])

# print(f'X head:\n{X.head()}')
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize RandomForestRegretion
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
# Train the regressor
rf_regressor.fit(X_train, y_train)
# Make prediction
y_pred = rf_regressor.predict(X_test)
# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error Sales: {mse:.2f}")
r2 = r2_score(y_test, y_pred)
print(f"R-squared Score Sales: {r2:.2f}")

# 2.Estimate the profit from a sale using similar features like region, product type, and quantity.
# Split df
X = super_df[['region', 'subcategory', 'quantity']] # Feature
y = super_df['profit'] # Target
# encode X
X.loc[:,'subcategory'] = LabelEncoder().fit_transform(X['subcategory'])
X.loc[:,'region'] = LabelEncoder().fit_transform(X['region'])
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize RandomForestRegretion
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
# Train the regressor
rf_regressor.fit(X_train, y_train)
# Make prediction
y_pred = rf_regressor.predict(X_test)
# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error Profit: {mse:.2f}")
r2 = r2_score(y_test, y_pred)
print(f"R-squared Score Profit: {r2:.2f}")

# Divide orders into "high profit" or "low profit" categories based on how much profit they generate.

# Predict if sales in a region or for a product category will be above or below a certain amount.

# Find out which features, such as product category or region, have the biggest impact on sales or profit.

# Each task involves cleaning the data, splitting it into training and test sets, training the Random Forest model, and evaluating its performance.