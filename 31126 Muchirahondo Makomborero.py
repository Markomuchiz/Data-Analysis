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
plt.show

import pandas as pd
netflix_df=pd.read_csv("netflix_data.csv")
print(netflix_df.head(5))

netflix_df_movies_only=netflix_df[netflix_df["type"]=="Movie"]
print(netflix_df_movies_only.head)

netflix_movies_col_subset=netflix_df_movies_only[["title","country","genre","release_year","duration"]]
print(netflix_movies_col_subset.head(5))

