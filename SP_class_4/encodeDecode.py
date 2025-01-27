import pandas as pd

# Sample data
data = {
    'Fruit': ['Apple', 'Banana', 'Orange', 'Apple', 'Orange'],
    'Test': ['eee', 'fff', 'eee', 'bbbb', 'kkk']
    }
df = pd.DataFrame(data)

# TODO 1. One-Hot Encoding
#     Converts each unique value in a categorical column into a separate binary (0/1) column.
#     Best for categorical variables with a small number of unique values.
# Encoding using get_dummies
encoded_df = pd.get_dummies(df, columns=['Fruit'])
print("Encoded DataFrame:\n", encoded_df)

# Decoding back to the original categorical data
# Extract columns related to 'Fruit' and find the maximum index
fruit_columns = [col for col in encoded_df.columns if 'Fruit_' in col]
decoded_fruit = encoded_df[fruit_columns].idxmax(axis=1).str.replace('Fruit_', '')
#decoded_df = encoded_df.idxmax(axis=1).str.replace('Fruit_', '')
df_decoded = pd.DataFrame({'Fruit':  decoded_fruit, 'Test': df['Test']})

print("Decoded DataFrame:", df_decoded)

#TODO 2. Label Encoding
#     Assigns a unique integer to each category.
#     Best for ordinal data (e.g., "Low," "Medium," "High") or when the number of unique categories is very large.
#     Less memory-intensive than one-hot encoding.
#     Warning: Can introduce unintended ordinal relationships (e.g., "Action" might be encoded as 1, "Drama" as 2).
# from sklearn.preprocessing import LabelEncoder
#
# # Apply Label Encoding to 'genres' and 'director'
# label_encoder = LabelEncoder()
#
# X['genres'] = label_encoder.fit_transform(X['genres'])
# X['director'] = label_encoder.fit_transform(X['director'])

# TODO 3. Target Encoding
#     Encodes categories based on the mean or median of the target variable (y) for each category.
#     Best for high-cardinality categorical variables, like director, which may have many unique values.
#     Caution: Can lead to data leakage if not applied properly (should be done within cross-validation folds).
# from category_encoders import TargetEncoder
#
# # Apply Target Encoding to 'genres' and 'director'
# target_encoder = TargetEncoder()
# X[['genres', 'director']] = target_encoder.fit_transform(X[['genres', 'director']], y)

