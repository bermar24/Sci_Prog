import pandas as pd
import seaborn as sns

# Import weather dataset
URL = ""
weather_df = pd.read_csv(URL)
print(f'Heard weather dataset\n {weather_df.head()}')
print(f'columns \n {weather_df.columns}')



# For the Movies Dataset, you can:
#
# Predict how much money a movie will make at the box office based on details like its budget, genre, director, and ratings.
# Sort movies into genres (like Action, Comedy, or Drama) using features such as budget and release year.
# Guess the rating of a movie, either as a specific number or by grouping ratings into categories.
