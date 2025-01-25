import pandas as pd

# Sample data
data = {
    'Fruit': ['Apple', 'Banana', 'Orange', 'Apple', 'Orange'],
    'Test': ['eee', 'fff', 'eee', 'bbbb', 'kkk']
    }
df = pd.DataFrame(data)

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
