import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from category_encoders import TargetEncoder

# Import movies dataset
movies_df = pd.read_csv("../SP_class_3/movie_dataset.csv")
print(movies_df.columns)

# 1.Predict how much money a movie will make at the box office based on details like its budget, genre, director, and ratings.
# Split the data into features (X) and target (y)
X = movies_df[['budget', 'genres', 'director', 'vote_average']]
y = movies_df['revenue']

# Apply Target Encoding to 'genres' and 'director'
target_encoder = TargetEncoder()
X_encoding = target_encoder.fit_transform(X[['genres', 'director']], y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoding, y, test_size=0.2, random_state=42)
# Initialize the RandomForestRegressor (the final prediction is the average of the predictions from all the trees)
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
# Train the regressor
rf_regressor.fit(X_train, y_train)
# Make prediction
y_pred = rf_regressor.predict(X_test)
# Calculate metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
# Print results
print(f'Mean Absolute Error: {mae}')
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")


# 2.Sort movies into genres (like Action, Comedy, or Drama) using features such as budget and release year.

movies_df['release_year'] = pd.to_datetime(movies_df['release_date'], errors='coerce').dt.year
movies_df['release_year'] = movies_df['release_year'].fillna(movies_df['release_year'].mean()).astype(float)
movies_df['budget'] = movies_df['budget'].fillna(movies_df['budget'].mean())
movies_df['vote_average'] = movies_df['vote_average'].fillna(movies_df['vote_average'].mean())
movies_df = movies_df.dropna()
X = movies_df[['budget', 'release_year', 'vote_average']]
y = movies_df['genres']
# Handle any missing years if they exist and converting data type to float


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize RandomForestClassifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
# Fit the classifier to the training data
rf_classifier.fit(X_train, y_train)
# Make prediction
y_pred2 = rf_classifier.predict(X_test)
# Calculate accuracy and classification report
accuracy = accuracy_score(y_test, y_pred2)
classification_rep = classification_report(y_test, y_pred2, zero_division=0)
# Print the results
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_rep)


# 3.Guess the rating of a movie, either as a specific number or by grouping ratings into categories.
