duration=[103,101,99,100,100,95,95,96,93,90]
movie_dict={'Years':[2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
            'Duration':[103,101,99,100,100,95,95,96,93,90]}
print(movie_dict)

import pandas as pd
durations_df=pd.DataFrame(movie_dict)
print(durations_df)

import matplotlib.pyplot as plt
plt.plot([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],[103,101,99,100,100,95,95,96,93,90])
plt.title('Netflix Movie Duration 2011-2020')
plt.xlabel('Years')
plt.ylabel('Duration')
plt.show

import pandas as pd
netflix_df=pd.read_csv("netflix_data.csv")
print(netflix_df.head(5))

netflix_df_movies_only=netflix_df[netflix_df["type"]=="Movie"]
print(netflix_df_movies_only.head)

netflix_movies_col_subset=netflix_df_movies_only[["title","country","genre","release_year","duration"]]
print(netflix_movies_col_subset.head(5))

import pandas as pd
import matplotlib.pyplot as plt
netflix_movies_col_subset=netflix_df_movies_only[["title","country","genre","release_year","duration"]]
df=pd.DataFrame(netflix_movies_col_subset.head(5))
plt.scatter(df.release_year, df.duration)
plt.title('Movie Duration by year of Release')
plt.xlabel('Release year')
plt.ylabel('Duration')
plt.show()

short_movies=netflix_movies_col_subset[netflix_movies_col_subset["duration"]<60]
print(short_movies.head(20))

# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for lab,row in netflix_movies_col_subset.iterrows():
    if row["genre"] == "Children" :
        colors.append("red")
    elif row["genre"] == "Stand-Up" :
        colors.append("blue")
    elif row["genre"] == "Documentaries":
        colors.append("green")
    else:
        colors.append("black")
        
# Inspect the first 10 values in your list        
print(colors[0:10])


# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(df.release_year, df.duration, c=colors)

# Create a title and axis labels
plt.title('Movie Duration by year of Release')
plt.xlabel('Release year')
plt.ylabel('Duration(min)')
# Show the plot
plt.show()

# Are we certain that movies are getting shorter?
are_movies_getting_shorter = "No"