import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Load Iris dataset
iris = load_iris()

# Create a DataFrame for better visualization
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target  # Add the target column

print("First 5 rows of the dataset:", data.head())

# TODO Data Preprocessing
# Split into features (X) and target (y)
X = data.iloc[:, :-1]  # Features
y = data['target']     # Target

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\nTraining data shape: {X_train.shape}")
print(f"Testing data shape: {X_test.shape}")

#  TODO Decision Tree Classifier
# Initialize and train the Decision Tree Classifier
dt_classifier = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
dt_classifier.fit(X_train, y_train)

print("\nDecision Tree trained successfully.")

# Export the decision tree in text form
tree_rules = export_text(dt_classifier, feature_names=list(X.columns))
print("\nDecision Tree Rules:\n", tree_rules)

# TODO Evaluate
# Predict on the test set
y_pred = dt_classifier.predict(X_test)

# Calculate and print accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Generate and display a classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

#  TODO Visualization
# Plot the decision tree
plt.figure(figsize=(12, 8))
plot_tree(dt_classifier, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()