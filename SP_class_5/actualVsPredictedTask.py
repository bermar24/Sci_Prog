# Generate synthetic data
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Create dataset
data = pd.DataFrame({    'Time': range(100),    'Value': np.sin(np.linspace(0, 10, 100)) + np.random.normal(scale=0.1, size=100)})

# Add lagged features
data['Lag_1'] = data['Value'].shift(1)
data['Lag_2'] = data['Value'].shift(2)
data.dropna(inplace=True)

# Train-test split
X = data[['Lag_1', 'Lag_2']]
y = data['Value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predict and evaluate
y_pred = rf.predict(X_test)
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

#Create a plot of Actual vs Predicted response values, as a function of time, in R
# Add predictions to the dataset for plotting
data.loc[X_test.index, 'Predicted'] = y_pred

# Create a plot of Actual vs Predicted response values as a function of time
plt.figure(figsize=(10, 6))
plt.plot(data['Time'], data['Value'], label='Observed', color='orange', marker='o', markersize=4, linestyle='-')
plt.plot(data['Time'], data['Predicted'], label='Predicted', color='deepskyblue', marker='o', markersize=4, linestyle='-')
plt.xlabel('Time')
plt.ylabel('Response')
plt.title('Actual vs Predicted Response Values')
plt.legend()
plt.grid(True)
plt.show()