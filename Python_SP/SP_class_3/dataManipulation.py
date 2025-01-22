import pandas as pd

# TODO Advanced Data Manipulation
# Sample DataFrames
df1 = pd.DataFrame({'key': [1, 2, 3], 'A': ['a1', 'a2', 'a3']})
df2 = pd.DataFrame({'key': [2, 3, 4], 'B': ['b1', 'b2', 'b3']})
print("Initial DataFrames:\n", df1, "\n", df2)

# Merge: COMBINES DATA BASED ON COMMON COLUMNS OR INDICES (LIKE SQL JOINS).
merged_df = pd.merge(df1, df2, on='key', how='inner') #Intersection
print("Merged DataFrame:\n", merged_df)
# Joining : SIMILAR TO MERGING, BUT PRIMARILY FOR COMBINING DATAFRAMES ON INDICES.

# Concatenate: STACKS DATAFRAMES EITHER VERTICALLY (ROWS) OR HORIZONTALLY (COLUMNS).
df_concat = pd.concat([df1, df2], axis=0) # Stack rows
print("\nConcatenated DataFrame:\n", df_concat)


# Grouping and Aggregation
data = {'Region': ['North', 'South', 'North', 'West'],
        'Sales': [200, 150, 300, 400],
        'Profit': [20, 10, 40, 50]}
df = pd.DataFrame(data)

# Grouping and Aggregation
grouped = df.groupby('Region').agg({'Sales': 'sum', 'Profit':
'mean'})
print("\nGrouped and Aggregated Data:\n", grouped)

# TODO: Pivot Tables
# Pivot Table
pivot = df.pivot_table(values='Sales', index='Region',
aggfunc='sum')
print("\nPivot Table:\n", pivot)
# Cross-tabulation
crosstab = pd.crosstab(index=df['Region'], columns=df['Profit'] > 20)
print("\nCross-tabulation:\n", crosstab)


# TODO: Handling Missing Data
df_missing = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
print("\nBefore Filling:\n", df_missing)
df_filled = df_missing.fillna(df_missing.mean()) # Fill with column mean
print("\nAfter Filling:\n", df_filled)

# TODO: Advanced String Operations
df_strings = pd.DataFrame({'Names': ['John-Doe', 'Jane-Doe', 'Alice-Jones']})
# String Split and Regex
df_strings['First Name'] = df_strings['Names'].str.split('-').str[0]
print("\nSplit String DataFrame:\n", df_strings)
