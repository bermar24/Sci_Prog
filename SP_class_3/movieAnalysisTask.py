import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import datasets
movies_df = pd.read_csv("movie_dataset.csv")
print(movies_df.head())
print("\nColumns movies:\n", movies_df.columns)

netflix_df = pd.read_csv('netflix_titles.csv')
print(netflix_df.head())
print("\nColumns netflix:\n", netflix_df.columns)

# marge the dataset
marge_df = pd.merge(movies_df, netflix_df, how='left', on='title')
print("Marge columns: \n" , marge_df.columns)

# creat Profit
marge_df["profit"] = marge_df["revenue"] - marge_df["budget"]

# Sort movies by profit in descending order
df_sorted = marge_df.sort_values(by='profit', ascending=False)
print("\nMore profitable movies:\n", df_sorted[["title", "profit"]].head())

# Group by country
grouped = marge_df.groupby('genres').agg({'profit': 'sum'})
grouped_sorted = grouped.sort_values(by='profit', ascending=False)
print("\nGrouped by genres:\n", grouped_sorted.head())

# Plot the distribution of movie ratings
plt.figure(figsize=(10, 6))
sns.histplot(data=marge_df, x='rating', kde=True, bins=20, color='blue')
plt.title('Distribution of Movie Ratings', fontsize=16)
plt.xlabel('Rating', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Create a bar plot for top genres by average rating
# Calculate average rating for each genre
genre_avg_rating = marge_df.groupby('genres').agg({'vote_average': 'sum'})

# Get the top genres (e.g., top 10 by average rating)
top_genres = genre_avg_rating.head(10)

# Plot the bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x='vote_average', y='genres', data=top_genres, palette="muted", hue='vote_average', legend=False)
plt.title('Top Genres by Average Rating', fontsize=16)
plt.xlabel('Average Rating', fontsize=14)
plt.ylabel('Genre', fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
