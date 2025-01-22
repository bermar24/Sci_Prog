import pandas as pd

# import datasets
movies_df = pd.read_csv("movie_dataset.csv")
print(movies_df.head())
print("\nColumns:\n", movies_df.columns)

netflix_df = pd.read_csv('netflix_titles.csv')
print(netflix_df.head())
print("\nColumns:\n", netflix_df.columns())
